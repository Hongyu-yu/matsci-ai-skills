# Pymatgen External Data - Reference Guide

## Overview

This reference covers `pymatgen.ext` helpers for external data sources such as
Materials Project, OPTIMADE endpoints, and the Crystallography Open Database (COD).

## Core Purpose

Use external data modules to:
- Query Materials Project for structures and properties
- Access OPTIMADE-compatible materials databases
- Fetch structures by COD IDs

## Key Modules and Classes

### Materials Project
- `pymatgen.ext.matproj.MPRester`
- Typical actions: search summary data, fetch structures, and entries

### OPTIMADE
- `pymatgen.ext.optimade.OptimadeRester` (OPTIMADE API access)

### Crystallography Open Database (COD)
- `pymatgen.ext.cod.COD`

## Common Workflows

### Materials Project query
```python
from pymatgen.ext.matproj import MPRester

with MPRester("YOUR_API_KEY") as mpr:
    # Method names vary by pymatgen version; adjust as needed.
    data = mpr.summary.search(formula="SiO2", fields=["material_id", "band_gap"])
    print(data[0])
```

### Fetch a structure by material ID
```python
from pymatgen.ext.matproj import MPRester

with MPRester("YOUR_API_KEY") as mpr:
    structure = mpr.get_structure_by_material_id("mp-149")
    structure.to("cif", "mp-149.cif")
```

### OPTIMADE search
```python
from pymatgen.ext.optimade import OptimadeRester

optimade = OptimadeRester("https://example.optimade.org")
structures = optimade.get_structures(filter="elements HAS ALL "Si"", page_limit=5)
```

### COD lookup
```python
from pymatgen.ext.cod import COD

cod = COD()
structure = cod.get_structure_by_id(1234567)
```

## Tips and Pitfalls

- Most external services require API keys or rate limits; confirm credentials.
- Method names can differ by pymatgen version; prefer checking the local docs in
  `references/docs/` if something is missing.
