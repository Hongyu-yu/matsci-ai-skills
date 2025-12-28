---
name: pymatgen-phonon
description: "Use for phonon band structure/DOS, Gruneisen, and IR spectra analysis with pymatgen.phonon and phonopy-compatible outputs."
metadata:
  short-description: pymatgen phonon
---

# Pymatgen Phonon

## Overview

Pymatgen phonon tools analyze phonon band structures, DOS, Gruneisen parameters, and IR spectra, often from Phonopy outputs.

## Required Python Environment

Ensure pymatgen and phonopy are installed in your Python environment:

```bash
pip install pymatgen phonopy
# or
conda install -c conda-forge pymatgen phonopy
```

Example usage pattern:

```python
from pymatgen.phonon.bandstructure import PhononBandStructure
# your code here
```

## When to Use This Skill
- Analyze phonon band structures, DOS, or spectra
- Work with Gruneisen parameters or phonopy outputs

## Core Capabilities

### 1. Phonon Data Loading
- Load phonon band structure and DOS from YAML

### 2. Plotting
- Phonon dispersion and DOS plotting utilities

### 3. Gruneisen and IR
- Gruneisen parameters and IR spectra utilities

## Quick Workflow
1. Load phonopy outputs or phonon objects.
2. Compute or plot band structure/DOS/spectra.
3. Export figures or derived data.

## Resources

### scripts/
Executable examples in the `scripts/` directory:

- `2016-09-25-Plotting_phonon_bandstructure_and_dos.py` - Phonon band structure and DOS plotting.

### references/
Detailed reference material (load as needed):

- `references/phonon-workflows.md` - Phonon workflows and examples
- `references/docs/` - Local API docs for `pymatgen.phonon`
