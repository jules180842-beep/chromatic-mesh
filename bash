chromatic-mesh/
├── ultracore.py # Main node driver - inverse Tree of Life pipeline
├── README.md # Architecture + usage
├── LICENSE # MIT
├── requirements.txt # numpy, asyncio
├──.gitignore
├── hw/
│ ├── bom.md # Bill of materials for v0 hardware
│ ├── schematic.pdf # Photodiode + SLM + laser wiring
│ └── calibrate_slm.py # Map az/el angles → SLM pixel coords
├── sim/
│ └── mesh_sim.py # Pure software sim, no hardware needed
├── examples/
│ ├── three_node.py # Triangle mesh demo
│ └── send_bits.py # Encode data as spectral power
└── docs/
    ├── ARCHITECTURE.md # Kabbalah → Optics mapping
    └── PROTOCOL.md # Wavelength routing spec