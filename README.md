# GeantPy

### A Python framework for generating and analyzing Geant4 particle simulation datasets.

GeantPy is a high-level Python interface designed to simplify Geant4 workflows for data analysis, machine learning, and scientific computing. It provides a declarative interface for configuring particle collision simulations, automates Geant4 execution, and returns simulation outputs in Python-friendly formats.

The goal is to make Geant4 accessible to researchers who want to generate and analyze particle interaction data without writing extensive C++.

> **Note:** GeantPy is an independent project and is not affiliated with or endorsed by the Geant4 Collaboration.

---

## Motivation

Geant4 is one of the most powerful particle transport toolkits available, but developing new simulations typically requires significant C++ knowledge.

GeantPy bridges this gap by allowing users to:

- Configure simulations in Python or YAML
- Execute Geant4 simulations automatically
- Generate structured datasets for downstream analysis
- Integrate directly with the Python scientific ecosystem

This makes GeantPy particularly well suited for:

- Machine learning dataset generation
- High-energy physics analysis
- Parameter sweeps
- Simulation-driven optimization
- Rapid prototyping of particle interaction experiments

---

## Core Capabilities

- Python-first workflow
- YAML-based experiment configuration
- Automatic Geant4 macro generation
- Automated simulation execution
- Structured particle collision data extraction
- Configurable beam and target parameters
- Multi-threaded simulation support
- Batch experiment generation
- Integration with NumPy, Pandas, and Matplotlib

---

## Workflow

```text
  YAML Configuration
           │
           ▼
        GeantPy
           │
           ▼
   Geant4 Simulation
           │
           ▼
Particle Collision Data (ROOT)
           │
           ▼
Python / Pandas / NumPy / ML
```

## Generated Data

Each simulation produces structured ROOT datasets suitable for scientific analysis.

### validation.root

Event-level collision information

- Beam properties
- Target information
- Outgoing particle lists
- Event multiplicities

### simulation.root

Track-level particle transport data

- Particle identities
- Momentum
- Vertex positions
- Event and track identifiers

---

## Use Cases

- Generate particle collision datasets
- Train machine learning models on Monte Carlo simulations
- Study particle production and transport
- Perform large-scale parameter sweeps
- Analyze detector and target performance
- Build reproducible simulation pipelines

---

## Getting started

- Refer to the [Usage Guide](docs/usage_guide.md) to get started with data generation.

## Roadmap

- [ ] Generic geometry definition
- [ ] Python-native experiment builder
- [ ] Custom detector support
- [ ] Direct geometry construction
- [ ] Improved visualization utilities
- [ ] Native Geant4 bindings for selected components

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
