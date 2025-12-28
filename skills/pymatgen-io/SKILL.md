---
name: pymatgen-io
description: "Use for non-VASP input/output tasks in pymatgen.io: CIF/XYZ/Gaussian/OpenBabel and DFT/MD code IO such as CP2K, Q-Chem, ABINIT, LAMMPS, FEFF, NWChem, Quantum ESPRESSO, Wannier90, phonopy/shengbte, etc."
metadata:
  short-description: pymatgen IO (non-VASP)
---

# Pymatgen IO (Non-VASP)

## Overview

Pymatgen IO (non-VASP) handles file formats and interfaces for many DFT/MD codes other than VASP.

## Required Python Environment

Ensure pymatgen is installed in your Python environment:

```bash
pip install pymatgen
# or
conda install -c conda-forge pymatgen
```

Example usage pattern:

```python
from pymatgen.io.cif import CifParser
# your code here
```

## When to Use This Skill
- Parse or write CIF, XYZ, Gaussian, or related formats
- Interface with CP2K, QE, Q-Chem, ABINIT, LAMMPS, FEFF, NWChem, etc.

## Core Capabilities

### 1. Common Formats
- CIF, XYZ, Gaussian, and adapters (ASE/OpenBabel if installed)

### 2. Code Interfaces
- Q-Chem, CP2K, Quantum ESPRESSO, ABINIT, LAMMPS, FEFF

### 3. Conversion
- Convert external formats to `Structure`/`Molecule`

## Quick Workflow
1. Identify the input/output format or code interface.
2. Parse into `Structure` or `Molecule` objects.
3. Write converted outputs or parse results.

## Resources

### scripts/
Executable examples in the `scripts/` directory:

- `2013-01-01-Getting_crystal_structures_from_online_sources.py` - Fetching structures from online sources and parsing formats.

### references/
Detailed reference material (load as needed):

- `references/io-non-vasp.md` - IO patterns and examples
- `references/docs/` - Local API docs for `pymatgen.io`
