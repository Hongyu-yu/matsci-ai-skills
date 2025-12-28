# Pymatgen Phonon - Reference Guide

## Overview

This reference covers `pymatgen.phonon` tools for phonon band structures, DOS,
Gruneisen parameters, and IR spectra. It is commonly used with Phonopy outputs.

## Core Purpose

Use phonon tools to:
- Load and analyze phonon band structures and DOS
- Compute or inspect Gruneisen parameters
- Plot phonon dispersions and spectra

## Key Classes and Modules

- `PhononBandStructureSymmLine`
- `PhononDos`, `CompletePhononDos`
- `GruneisenParameter`
- `PhononBandStructureSymmLinePlotter`, `PhononDosPlotter`
- IR spectra utilities in `pymatgen.phonon.ir_spectra`

## Common Workflows

### Load phonon band structure from Phonopy YAML
```python
import yaml
from pymatgen.phonon.bandstructure import PhononBandStructureSymmLine

with open("phonon_band_structure.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

bs = PhononBandStructureSymmLine.from_dict(data)
```

### Plot phonon band structure and DOS
```python
import yaml
from pymatgen.phonon.bandstructure import PhononBandStructureSymmLine
from pymatgen.phonon.dos import PhononDos
from pymatgen.phonon.plotter import PhononBSPlotter, PhononDosPlotter

with open("phonon_band_structure.yaml", "r", encoding="utf-8") as f:
    bs = PhononBandStructureSymmLine.from_dict(yaml.safe_load(f))
with open("phonon_dos.yaml", "r", encoding="utf-8") as f:
    dos = PhononDos.from_dict(yaml.safe_load(f))

PhononBSPlotter(bs).get_plot()
PhononDosPlotter().get_plot(dos)
```

### Gruneisen parameters
```python
import yaml
from pymatgen.phonon.gruneisen import GruneisenParameter

with open("gruneisen.yaml", "r", encoding="utf-8") as f:
    g = GruneisenParameter.from_dict(yaml.safe_load(f))

print(g.gruneisen)
```

## Tips and Pitfalls

- Many phonon workflows require Phonopy-generated YAML files; ensure those are present.
- Units and conventions can vary between generators; validate metadata before plotting.
