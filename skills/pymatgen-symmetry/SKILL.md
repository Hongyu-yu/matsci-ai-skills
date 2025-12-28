---
name: pymatgen-symmetry
description: "Use for symmetry analysis, space group determination, standardization, and k-path generation using pymatgen.symmetry."
metadata:
  short-description: pymatgen symmetry
---

# Pymatgen Symmetry

## Overview

Pymatgen symmetry tools determine space groups, symmetry operations, standardized cells, and k-paths for band structure calculations.

## Required Python Environment

Ensure pymatgen is installed in your Python environment:

```bash
pip install pymatgen
# or
conda install -c conda-forge pymatgen
```

Example usage pattern:

```python
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
# your code here
```

## When to Use This Skill
- Determine space group, symmetry operations, or standardized cells
- Generate high-symmetry k-paths for band structures

## Core Capabilities

### 1. Space Group Analysis
- `SpacegroupAnalyzer` for symmetry and conventional cells

### 2. Symmetry Operations
- Symmetry operations and point group analysis

### 3. K-Path Generation
- High-symmetry k-paths for electronic structure

## Quick Workflow
1. Load the structure.
2. Run `SpacegroupAnalyzer` or k-path tools.
3. Export standardized structures or k-path data.

## Resources

### scripts/
Executable examples in the `scripts/` directory:

- `2021-08-26-Magnetic_Structure_Generation_as_Input_for_Initial_DFT_Calculations.py` - Magnetic structure generation for DFT inputs.

### references/
Detailed reference material (load as needed):

- `references/symmetry-tools.md` - Symmetry workflows and examples
- `references/docs/` - Local API docs for `pymatgen.symmetry`
