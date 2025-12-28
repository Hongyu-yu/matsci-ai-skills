# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-12-28

### 🎉 Initial Release

First public release of the Materials Science AI Skills Library.

### Added

#### Custom Skills (Created by maintainer)
- **pymatgen-core** - Pymatgen core objects and structure manipulation
- **pymatgen-analysis** - Materials analysis workflows (phase diagrams, Pourbaix, reactions)
- **pymatgen-io** - Non-VASP file I/O (CIF, XYZ, Gaussian, CP2K, QE, etc.)
- **pymatgen-io-vasp** - VASP-specific I/O (input generation, output parsing)
- **pymatgen-ext** - External data access (Materials Project, OPTIMADE, COD)
- **pymatgen-phonon** - Phonon analysis (band structure, DOS, Gruneisen)
- **pymatgen-symmetry** - Symmetry analysis (space groups, k-paths)
- **pymatgen-electronic-structure** - Electronic structure (DOS, bands, COHP/COOP)
- **openmx** - OpenMX v3.9 DFT calculations and workflows

#### Community Skills (Curated)
- **Materials Science**: vasp, python-ase, fairchem, materials-databases, materials-properties
- **Python Scientific Computing**: python-jax, python-optimization, python-multiobjective-optimization, python-plotting, python-regression-statistics, scikit-learn, sympy, astropy, fluidsim
- **Deep Learning**: pytorch-lightning, torch-geometric, transformers
- **ML Symmetry**: symmetry-discovery-questionnaire, symmetry-group-identifier, symmetry-validation-suite, equivariant-architecture-designer, model-equivariance-auditor
- **Document Processing**: pdf, docx, pptx, xlsx, markitdown, latex-posters
- **Decision Frameworks**: brainstorming, planning, decision-matrix, causal-inference-root-cause, decomposition-reconstruction, design-of-experiments, estimation-fermi, meta-prompt-engineering, postmortem, systems-thinking-leverage
- **Utilities**: memory, skill-creator

### Removed
- Quantum computing skills (qiskit, pennylane, cirq, qutip) - out of scope for materials science focus

### Documentation
- Comprehensive README.md with skill categories and usage guide
- Chinese documentation (README_CN.md)
- Contributing guidelines and skill templates

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 1.0.0 | 2025-12-28 | Initial release with 45+ curated skills |

---

## Contributing

See [Contributing Guidelines](README.md#-contributing) for how to submit changes.

When contributing, please update this changelog under the `[Unreleased]` section.
