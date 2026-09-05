# GeantPy

### A Python framework for building, executing, and analyzing Geant4 simulations.

GeantPy is a lightweight Python interface that simplifies Geant4 simulation workflows. It automates experiment configuration, execution, and data generation, producing structured ROOT datasets and analysis-ready outputs without requiring extensive Geant4 boilerplate.

Rather than replacing Geant4, GeantPy provides a reproducible workflow for configuring simulations, collecting particle interaction data, and integrating the results into scientific computing and machine learning pipelines.

> **Note:** GeantPy is an independent project and is not affiliated with or endorsed by the Geant4 Collaboration.

---

## Workflow

```text
YAML Configuration
        │
        ▼
     GeantPy
        │
        ▼
      Geant4
        │
        ▼
 Structured ROOT Datasets
        │
        ▼
 NumPy / ML / Scientific Analysis
```

---

## Current Capabilities

### Simulation

* YAML-based experiment configuration
* Automated Geant4 execution
* Reproducible simulation workflows
* Beam-on-target simulation support

### Data Generation

* Event-level ROOT datasets
* Track-level ROOT datasets
* Automatic configuration logging
* Simulation metadata export

### Analysis

* ROOT dataset inspection
* ROOT → NumPy conversion
* Ready for NumPy, PyTorch, TensorFlow, JAX, and scikit-learn workflows

---

## Output Structure

Each simulation produces a self-contained output directory containing configuration metadata, simulation outputs, and validation datasets.

```text
run_<timestamp>/
├── config.json
├── particle_summary.txt
├── simulation.root
└── validation.root
```

* **config.json** — complete simulation configuration for reproducibility
* **particle_summary.txt** — summary of generated particles
* **simulation.root** — track-level particle transport data
* **validation.root** — event-level collision and interaction data

---

## Data Analysis

GeantPy includes utilities for inspecting ROOT datasets before downstream analysis.

Available tools provide:

* Dataset summaries
* Branch inspection
* Data type information
* Array shape reporting
* Jagged array visualization

Generated ROOT datasets can also be converted into compressed NumPy (`.npz`) files for integration with scientific Python workflows.

---

## Quick Start

See the **[Usage Guide](docs/usage_guide.md)** for installation instructions, simulation setup, and example workflows.

---

## Future Directions

Planned areas of development include:

* Generalized detector and geometry definitions
* Python-native experiment configuration
* Expanded Geant4 bindings
* Additional analysis and visualization utilities

---

## License

MIT License

---

## Acknowledgements

GeantPy builds upon the Geant4 simulation toolkit developed by the Geant4 Collaboration:

[Recent Developments in Geant4](https://www.sciencedirect.com/science/article/pii/S0168900216306957), J. Allison et al., Nucl. Instrum. Meth. A 835 (2016) 186-225<br>
[Geant4 Developments and Applications](https://ieeexplore.ieee.org/document/1610988), J. Allison et al., IEEE Trans. Nucl. Sci. 53 (2006) 270-278<br>
[Geant4 - A Simulation Toolkit](https://www.sciencedirect.com/science/article/abs/pii/S0168900203013688), S. Agostinelli et al., Nucl. Instrum. Meth. A 506 (2003) 250-303

This project is an independent Python framework and is not an official Geant4 project.

## Status (as of 2026-09-06)
Archived. Python interface for automating and orchestrating Geant4 simulation workflows through macro generation.
