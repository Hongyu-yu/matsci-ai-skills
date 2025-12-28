---
name: pymatgen-core
description: "Use for pymatgen core objects and structure manipulation: Element/Specie/Composition, Lattice/Site/Structure/Molecule, oxidation states, structure edits, transformations, and serialization."
metadata:
  short-description: pymatgen core structures
---

# Pymatgen Core

## Overview

Pymatgen core provides the fundamental objects for representing chemistry, lattices, sites, and structures. Use it to build, edit, and serialize structures and molecules before moving into specialized analysis or IO modules.

## Required Python Environment

Ensure pymatgen is installed in your Python environment:

```bash
pip install pymatgen
# or
conda install -c conda-forge pymatgen
```

Example usage pattern:

```python
from pymatgen.core import Structure, Lattice, Element
# your code here
```

## When to Use This Skill
- Build or edit `Structure`/`Molecule` objects
- Work with compositions, oxidation states, or lattice transforms
- Serialize objects for storage or downstream workflows

## Core Capabilities

### 1. Structures and Molecules
- `Structure`/`IStructure` for periodic systems
- `Molecule`/`IMolecule` for non-periodic systems
- Site operations and lattice utilities

### 2. Chemistry Primitives
- `Element`, `Specie`, `Composition`, and oxidation states
- Formula reduction and fraction calculations

### 3. Transformations and Serialization
- Structure edits and transformations
- Monty `as_dict()` / `from_dict()` serialization

## Quick Workflow
1. Identify the primary object type (`Structure`, `Molecule`, or `Composition`).
2. Load/build and validate oxidation states or primitive cells.
3. Apply transformations or edits.
4. Serialize with `as_dict()` or export via `.to()`.

## Resources

### scripts/
Executable examples in the `scripts/` directory:

- `2013-01-01-Basic_functionality.py` - Basic structure, lattice, and composition operations.
- `2013-01-01-Ordering_Disordered_Structures.py` - Ordering disordered structures and site occupancy handling.

### references/
Detailed reference material (load as needed):

- `references/modules.md` - Core objects and usage patterns
- `references/docs/usage.md` - Local usage overview
- `references/docs/pymatgen.core.md` - API details
