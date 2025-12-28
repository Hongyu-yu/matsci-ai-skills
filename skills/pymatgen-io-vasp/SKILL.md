---
name: pymatgen-io-vasp
description: "Use for VASP input generation, POTCAR handling, and parsing VASP outputs (vasprun.xml, OUTCAR, OSZICAR, PROCAR, CHGCAR, LOCPOT, EIGENVAL) via pymatgen.io.vasp and input sets."
metadata:
  short-description: pymatgen VASP IO
---

# Pymatgen IO (VASP)

## Overview

Pymatgen VASP IO supports input generation, standard input sets, and output parsing for VASP calculations.

## Required Python Environment

Ensure pymatgen is installed in your Python environment:

```bash
pip install pymatgen
# or
conda install -c conda-forge pymatgen
```

Example usage pattern:

```python
from pymatgen.io.vasp import Vasprun, Outcar
# your code here
```

## When to Use This Skill
- Build VASP inputs or standardized input sets
- Parse VASP outputs for energies, structures, DOS, or band structures

## Core Capabilities

### 1. Input Objects
- INCAR, KPOINTS, POSCAR, POTCAR builders

### 2. Input Sets
- MP/MIT/MVL input set presets

### 3. Output Parsing
- `Vasprun`, `Outcar`, `Oszicar`, `Eigenval`, `Procar`

## Quick Workflow
1. Build input objects or input sets.
2. Write inputs or parse outputs.
3. Extract derived data and plots.

## Resources

### scripts/
Executable examples in the `scripts/` directory:

- `2017-04-14-Inputs_and_Analysis_of_VASP_runs.py` - VASP input setup and output analysis.

Note: POTCAR files are not bundled; confirm pseudopotential paths before use.
Note: Do not execute VASP unless explicitly requested.

### references/
Detailed reference material (load as needed):

- `references/vasp-io.md` - VASP IO classes and examples
- `references/docs/pymatgen.io.vasp.md` - Local API docs
