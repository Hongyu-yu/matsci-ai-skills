# Pymatgen VASP IO - Reference Guide

## Overview

This reference summarizes `pymatgen.io.vasp` inputs, outputs, and input sets for
building VASP calculations and parsing results.

## Core Purpose

Use VASP IO to:
- Generate INCAR/KPOINTS/POSCAR/POTCAR inputs
- Build standardized input sets (MP, MIT, etc.)
- Parse outputs such as `vasprun.xml` and `OUTCAR`

## Key Classes and Modules

### Inputs
- `Incar` (read/write, parameter checking, diffs)
- `Kpoints` (automatic meshes, line-mode paths)
- `Poscar` (structure, selective dynamics, velocities)
- `Potcar`, `PotcarSingle` (POTCAR assembly and validation)
- `VaspInput` (container for full input set)

### Input sets
- `MPRelaxSet`, `MP24RelaxSet`, `MPSCANRelaxSet`, `MPHSERelaxSet`
- `MITRelaxSet`, `MVLRelax52Set`, `MVLGWSet`
- Base config YAML files in `pymatgen/io/vasp/*.yaml`

### Outputs
- `Vasprun`, `BSVasprun`
- `Outcar`, `Oszicar`, `Eigenval`, `Procar`
- `Chgcar`, `Locpot`

## Common Workflows

### Create a standard relaxation input
```python
from pymatgen.core import Structure
from pymatgen.io.vasp.sets import MPRelaxSet

structure = Structure.from_file("POSCAR")
relax_set = MPRelaxSet(structure)
relax_set.write_input("vasp_relax")
```

### Parse a VASP run
```python
from pymatgen.io.vasp import Vasprun

v = Vasprun("vasprun.xml")
structure = v.final_structure
energy = v.final_energy
```

### Parse band structure (line-mode)
```python
from pymatgen.io.vasp import BSVasprun

v = BSVasprun("vasprun.xml", parse_projected_eigen=True)
bs = v.get_band_structure()
```

## File-to-Class Map

- `INCAR` → `Incar`
- `KPOINTS` → `Kpoints`
- `POSCAR` / `CONTCAR` → `Poscar`
- `POTCAR` → `Potcar` / `PotcarSingle`
- `vasprun.xml` → `Vasprun` / `BSVasprun`
- `OUTCAR` → `Outcar`
- `OSZICAR` → `Oszicar`
- `EIGENVAL` → `Eigenval`
- `CHGCAR` → `Chgcar`
- `LOCPOT` → `Locpot`
- `PROCAR` → `Procar`

## Tips and Pitfalls

- POTCAR files are not bundled; confirm pseudopotential paths before use.
- Prefer input sets for reproducible defaults and override parameters explicitly.
- Do not execute VASP unless explicitly requested by the user.
