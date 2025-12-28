# Pymatgen Core Objects - Practical Guide

## Overview

This reference summarizes the core objects in `pymatgen.core` and how to use them for
building, editing, and serializing structures and molecules.

## Core Purpose

Use the core module to:
- Represent chemical elements and species with oxidation states
- Build lattices and periodic/non-periodic structures
- Inspect and edit sites, compositions, and properties
- Serialize objects for storage or downstream workflows

## Key Classes and Modules

### Chemistry primitives
- `Element`, `Specie`, `DummySpecie` (periodic table and oxidation states)
- `Composition` (chemical formula, amounts, normalization)
- `Ion` (charged species for defect or ion chemistry workflows)

### Geometry and structures
- `Lattice` (cell vectors, parameters, coordinate transforms)
- `Site`, `PeriodicSite` (single-site objects)
- `Structure`, `IStructure` (periodic crystals)
- `Molecule`, `IMolecule` (non-periodic molecules)

### Utilities
- `StructureMatcher` and analyses live elsewhere; stay in `pymatgen.analysis` for those
- `as_dict()` / `from_dict()` for Monty serialization

## Common Workflows

### Build a structure from scratch
```python
from pymatgen.core import Lattice, Structure

lattice = Lattice.cubic(3.9)
structure = Structure(
    lattice,
    species=["Li", "Fe", "P", "O", "O", "O", "O"],
    coords=[
        [0, 0, 0],
        [0.5, 0.5, 0.5],
        [0.25, 0.25, 0.25],
        [0.75, 0.75, 0.25],
        [0.75, 0.25, 0.75],
        [0.25, 0.75, 0.75],
        [0.25, 0.25, 0.75],
    ],
)
```

### Load, edit, and save
```python
from pymatgen.core import Structure

structure = Structure.from_file("POSCAR")
structure.make_supercell([2, 2, 1])
structure.translate_sites([0], [0.1, 0.0, 0.0], frac_coords=True)
structure.to("cif", "supercell.cif")
```

### Composition and oxidation states
```python
from pymatgen.core import Composition

comp = Composition("LiFePO4")
print(comp.reduced_formula)
print(comp.get_atomic_fraction("Fe"))
```

## Tips and Pitfalls

- Use `Structure` for periodic crystals and `Molecule` for non-periodic systems.
- Prefer `IStructure` / `IMolecule` when you need immutable objects.
- Avoid analysis-heavy tasks here; move to `pymatgen.analysis` or `pymatgen.symmetry`.
- When serializing, prefer `as_dict()` + `MontyEncoder` to preserve class metadata.
