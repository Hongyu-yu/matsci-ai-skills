# Pymatgen Electronic Structure - Reference Guide

## Overview

This reference focuses on `pymatgen.electronic_structure` utilities for
band structures, density of states (DOS), COHP data, and plotting helpers.

## Core Purpose

Use these tools to:
- Parse electronic structure data from DFT outputs
- Analyze band structures and DOS
- Work with COHP/COOP data (often from LOBSTER)
- Generate publication-ready plots

## Key Classes and Modules

### Band structure
- `BandStructure`, `BandStructureSymmLine`
- `BSPlotter`, `BSDOSPlotter`
- `HighSymmKpath` (from `pymatgen.symmetry` for k-paths)

### Density of states
- `Dos`, `CompleteDos`
- `DosPlotter`
- Orbital and element projections via `CompleteDos`

### COHP/COOP
- `Cohp`, `CompleteCohp`
- `CohpPlotter`

### Common enums
- `Spin`, `OrbitalType` for spin- and orbital-resolved data

## Common Workflows

### Parse band structure and DOS from VASP
```python
from pymatgen.io.vasp import Vasprun
from pymatgen.electronic_structure.plotter import BSPlotter, DosPlotter

v = Vasprun("vasprun.xml", parse_projected_eigen=True)
bs = v.get_band_structure()
dos = v.complete_dos

bs_plot = BSPlotter(bs).get_plot()
dos_plot = DosPlotter().get_plot(dos)
```

### Element-projected DOS
```python
from pymatgen.electronic_structure.plotter import DosPlotter

plotter = DosPlotter()
plotter.add_dos("total", dos)
plotter.add_dos("Fe", dos.get_element_dos("Fe"))
plotter.get_plot()
```

### COHP plotting (LOBSTER output)
```python
from pymatgen.electronic_structure.cohp import CompleteCohp
from pymatgen.electronic_structure.plotter import CohpPlotter

cohp = CompleteCohp.from_file("COHPCAR.lobster")
plotter = CohpPlotter()
plotter.add_cohp("Fe-O", cohp.get_cohp_by_label("Fe1-O3"))
plotter.get_plot()
```

## Tips and Pitfalls

- Band structure plotting typically needs a symmetry k-path; use
  `HighSymmKpath` or ensure `vasprun.xml` includes line-mode k-points.
- Projected DOS and COHP require that the underlying calculation wrote
  the necessary projections (e.g., LORBIT in VASP, LOBSTER outputs).
