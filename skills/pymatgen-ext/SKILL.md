---
name: pymatgen-ext
description: "Use for external data access via pymatgen.ext: Materials Project (MPRester), OPTIMADE endpoints, and COD lookups."
metadata:
  short-description: pymatgen external data
---

# Pymatgen External Data

## Overview

Pymatgen external data helpers provide access to Materials Project, OPTIMADE endpoints, and COD structures.

## Required Python Environment

Ensure pymatgen is installed in your Python environment:

```bash
pip install pymatgen mp-api
# or
conda install -c conda-forge pymatgen mp-api
```

Example usage pattern:

```python
from mp_api.client import MPRester
# your code here
```

## When to Use This Skill
- Query Materials Project or other OPTIMADE databases
- Fetch structures or metadata from COD

## Core Capabilities

### 1. Materials Project
- Search summaries and retrieve structures

### 2. OPTIMADE
- Query OPTIMADE-compatible endpoints

### 3. COD
- Fetch structures by COD ID

## Quick Workflow
1. Confirm API keys or endpoints.
2. Query and retrieve structures or metadata.
3. Convert to `Structure` and export as needed.

## Resources

### scripts/
Executable examples in the `scripts/` directory:

- `2013-01-01-Calculating_Reaction_Energies_with_the_Materials_API.py` - Reaction energies using Materials Project data.
- `2013-01-01-Plotting_and_Analyzing_a_Phase_Diagram_using_the_Materials_API.py` - Phase diagram plotting and analysis with MP data.
- `2017-03-02-Getting_data_from_Materials_Project.py` - Querying Materials Project for structures and data.
- `2018-09-25-Structure_Prediction_using_Pymatgen_and_the_Materials_API.py` - Structure prediction with Materials Project data.

Note: These scripts require Materials Project API access; set your API key before running.

### references/
Detailed reference material (load as needed):

- `references/external-data.md` - External data access patterns
- `references/docs/pymatgen.ext.md` - Local API docs
