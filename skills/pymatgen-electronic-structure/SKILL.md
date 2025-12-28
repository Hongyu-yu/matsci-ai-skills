---
name: pymatgen-electronic-structure
description: "Use for electronic structure analysis with pymatgen.electronic_structure: DOS, band structures, COHP/COOP, and plotting utilities."
metadata:
  short-description: pymatgen electronic structure
---

# Pymatgen Electronic Structure

## Overview

Pymatgen electronic structure utilities handle band structures, DOS, and COHP/COOP data, plus plotting helpers for common DFT outputs.

## Required Python Environment

Ensure pymatgen is installed in your Python environment:

```bash
pip install pymatgen
# or
conda install -c conda-forge pymatgen
```

Example usage pattern:

```python
from pymatgen.electronic_structure.dos import Dos
from pymatgen.electronic_structure.bandstructure import BandStructure
# your code here
```

## When to Use This Skill
- Band structure or DOS analysis
- COHP/COOP analysis (often from LOBSTER)
- Plotting electronic structure results

## Core Capabilities

### 1. Output Parsing
- Parse `vasprun.xml`/`BSVasprun` or other output objects

### 2. Band Structure and DOS
- Band structure and DOS objects
- Plotting utilities for publication-ready figures

### 3. COHP/COOP
- COHP/COOP data handling and plotting

## Quick Workflow
1. Parse output files into band structure/DOS/COHP objects.
2. Select projection or spin settings as needed.
3. Generate plots or export data.

## Resources

### scripts/
Executable examples in the `scripts/` directory:

- `2013-01-01-Plotting_the_electronic_structure_of_Fe.py` - Electronic structure plotting for Fe.
- `2017-09-03-Analyze_and_plot_band_structures.py` - Band structure analysis and plotting.
- `2018-03-14-Plotting_COHP_from_LOBSTER.py` - COHP plotting from LOBSTER outputs.
- `2020-07-15-How_to_plot_a_Fermi_surface_with_Boltztrap_-_notest.py` - Fermi surface plotting with BoltzTraP (example).

### references/
Detailed reference material (load as needed):

- `references/electronic-structure.md` - Key classes and examples
- `references/docs/` - Local API docs for `pymatgen.electronic_structure`
