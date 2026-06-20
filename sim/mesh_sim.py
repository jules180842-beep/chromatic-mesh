# sim/mesh_sim.py
import asyncio
import numpy as np
from ultracore import ChromaticNode

class SimNode(ChromaticNode):
    async def _read_spectrometer(self):
        # Ambient + received from other nodes
        return np.random.rand(5) * 2 + self.rx_buffer
    async def _fire_laser(self, az, el, band, power):
        # Find neighbor at angle, add to their rx_buffer
        for n in SIM_NODES:
            if n!= self and self._angle_match(n):
                n.rx_buffer[band] += power * 0.8 # loss
    async def _read_backscatter(self):
        return np.abs(np.fft.fft2(np.exp(1j * self.slm_state))) * 0.1
    def _angle_match(self, other): return True # simplify
    def __init__(self, *args):
        super().__init__(*args)
        self.rx_buffer = np.zeros(5)

SIM_NODES = []
async def main():
    n1 = SimNode("A", {"B": (0,0), "C": (120,0)})
    n2 = SimNode("B", {"A": (180,0), "C": (60,0)})
    n3 = SimNode("C", {"A": (240,0), "B": (300,0)})
    global SIM_NODES
    SIM_NODES = [n1,n2,n3]
    await asyncio.gather(n1.run(), n2.run(), n3.run())

if __name__ == "__main__":
    asyncio.run(main())