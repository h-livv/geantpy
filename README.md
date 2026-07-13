# GeantPy

### GeantPy is a Python framework for building, executing, and analyzing Geant4 simulations.

GeantPy makes Geant4-based particle simulation more accessible by automating simulation workflows and generating structured ROOT datasets, enabling researchers to quickly generate, inspect, and analyze particle interaction data without extensive C++ development.

> **Note:** GeantPy is an independent project and is not affiliated with or endorsed by the Geant4 Collaboration.

---

## Features

- Easily configurable YAML interface
- Event-level and track-level ROOT dataset generation
- Utilities to convert dataset to NumPy arrays

---

## Output Structure
Each simulation produces a dedicated output directory containing:

```
run_<timestamp>/
├── config.json
├── particle_summary.txt
├── simulation.root
└── validation.root
```

### `config.json`

Stores the complete simulation configuration used for the run, ensuring experiments are fully reproducible.

### `particle_summary.txt`

A text file containing an overview of the particles generated.

### `simulation.root`

Track-level particle transport data.

Contains information such as:

- Event IDs
- Track IDs
- PDG particle codes
- Particle positions
- Particle momentum

Each entry corresponds to an individual particle track generated during the simulation.

### `validation.root`

Event-level collision data.

Contains information such as:

- Incident beam properties
- Target information
- Outgoing particle IDs
- Outgoing particle energies
- Outgoing particle momenta
- Particle multiplicities

Each entry corresponds to a single collision event.

---

## Data Analysis

GeantPy includes `data.py` for quickly inspecting ROOT files.

It provides a summary of the objects stored in each dataset, including:

- Branch names
- Data types
- Array shapes
- Jagged array structures

This provides a convenient overview of the generated simulation data before downstream analysis.

---

## ROOT → NumPy Conversion

The `convert.py` utility converts ROOT datasets into compressed NumPy (`.npz`) files for machine learning and scientific computing workflows.

The generated `.npz` files can be loaded directly with NumPy and integrated with libraries such as:

- NumPy
- PyTorch
- TensorFlow
- JAX
- Scikit-learn

---

## Workflow

```
YAML Configuration
        │
        ▼
     GeantPy
        │
        ▼
      Geant4
        │
        ▼
    config.json
 particle_summary.txt
  simulation.root
  validation.root
        │
        ▼
 NumPy / ML / Analysis
```

---

## Getting Started

See the **[Usage Guide](docs/usage_guide.md)** for installation instructions, simulation setup, and example workflows.

> **Note:** Current support is focused on beam-on-target (particle-target collision) simulations.

---

## Future Work

- Generalized detector and geometry definitions
- Python-native experiment configuration
- Extended Geant4 bindings

---

## License

MIT License

---

## Acknowledgements

GeantPy builds upon the excellent Geant4 simulation toolkit developed by the Geant4 Collaboration:

[Recent Developments in Geant4](https://www.sciencedirect.com/science/article/pii/S0168900216306957), J. Allison et al., Nucl. Instrum. Meth. A 835 (2016) 186-225<br>
[Geant4 Developments and Applications](https://ieeexplore.ieee.org/document/1610988), J. Allison et al., IEEE Trans. Nucl. Sci. 53 (2006) 270-278<br>
[Geant4 - A Simulation Toolkit](https://www.sciencedirect.com/science/article/abs/pii/S0168900203013688), S. Agostinelli et al., Nucl. Instrum. Meth. A 506 (2003) 250-303

This project is an independent Python framework and is not an official Geant4 project.
