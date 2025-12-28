# Pymatgen IO (Non-VASP) - Reference Guide

## Overview

This reference covers file formats and code interfaces in `pymatgen.io` excluding VASP.
Use it to parse, write, and convert common crystallographic and quantum chemistry files.

## Core Purpose

Use IO modules to:
- Read and write crystal and molecule file formats (CIF, XYZ, etc.)
- Interface with non-VASP DFT/MD codes (Q-Chem, CP2K, QE, ABINIT, LAMMPS, etc.)
- Convert between pymatgen objects and external representations

## Key Modules and Classes

### Common formats
- `pymatgen.io.cif.CifParser`, `CifWriter`
- `pymatgen.io.xyz.XYZ`
- `pymatgen.io.gaussian` (Gaussian input/output)
- `pymatgen.io.ase.AseAtomsAdaptor` (ASE bridge)

### DFT and MD codes
- `pymatgen.io.qchem`
- `pymatgen.io.cp2k`
- `pymatgen.io.pwscf` (Quantum ESPRESSO)
- `pymatgen.io.abinit`
- `pymatgen.io.lammps`
- `pymatgen.io.feff`
- `pymatgen.io.nwchem`
- `pymatgen.io.wannier90`

## Common Workflows

### Parse and write CIF
```python
from pymatgen.io.cif import CifParser, CifWriter

structure = CifParser("input.cif").get_structures()[0]
CifWriter(structure).write_file("output.cif")
```

### Convert to/from ASE
```python
from pymatgen.io.ase import AseAtomsAdaptor
from pymatgen.core import Structure

structure = Structure.from_file("POSCAR")
ase_atoms = AseAtomsAdaptor.get_atoms(structure)
structure_roundtrip = AseAtomsAdaptor.get_structure(ase_atoms)
```

### Read Quantum ESPRESSO input
```python
from pymatgen.io.pwscf import PWInput
from pymatgen.core import Structure

structure = Structure.from_file("POSCAR")
pw = PWInput(structure)
pw.write_file("pw.in")
```

## Tips and Pitfalls

- Many code interfaces depend on external packages (e.g., ASE, OpenBabel).
- Keep IO tasks focused; use analysis modules for property calculations.
- For VASP specifically, switch to the `pymatgen-io-vasp` skill.
