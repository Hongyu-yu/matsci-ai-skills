# Pymatgen Symmetry - Reference Guide

## Overview

This reference focuses on `pymatgen.symmetry` utilities for space-group analysis,
standardization, symmetry operations, and k-path generation.

## Core Purpose

Use symmetry tools to:
- Determine space groups and symmetry operations
- Standardize and symmetrize structures
- Generate high-symmetry k-paths for band structures

## Key Classes and Modules

- `SpacegroupAnalyzer` (space group, symmetry ops, conventional cells)
- `SymmOp` (symmetry operation object)
- `PointGroupAnalyzer` (molecule point groups)
- `HighSymmKpath`, `KPathSeek` (k-paths for band structures)

## Common Workflows

### Analyze space group and conventional cell
```python
from pymatgen.core import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer

structure = Structure.from_file("POSCAR")
sg = SpacegroupAnalyzer(structure)
print(sg.get_space_group_symbol(), sg.get_space_group_number())
conventional = sg.get_conventional_standard_structure()
```

### Get symmetry operations
```python
ops = sg.get_symmetry_operations(cartesian=False)
print(len(ops))
```

### Generate a high-symmetry k-path
```python
from pymatgen.symmetry.bandstructure import HighSymmKpath

kpath = HighSymmKpath(structure)
print(kpath.kpath)
```

## Tips and Pitfalls

- Always check if your structure is properly standardized before analysis.
- K-path generation depends on lattice settings; use conventional cells when needed.
