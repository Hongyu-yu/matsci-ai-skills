---
name: pymatgen-analysis
description: "Use for materials analysis tasks in pymatgen.analysis: phase/Pourbaix/chemical-potential diagrams, reactions, structure matching, surfaces/interfaces, local environments, diffraction, elasticity, magnetism, and related analyses."
metadata:
  short-description: pymatgen analysis
---

# Pymatgen Analysis

## Overview

Pymatgen analysis provides higher-level workflows for thermodynamics, reactions, structure comparison, surfaces, and property analyses. Use it once you have structures or entries ready.

## Required Python Environment

Ensure pymatgen is installed in your Python environment:

```bash
pip install pymatgen
# or
conda install -c conda-forge pymatgen
```

Example usage pattern:

```python
from pymatgen.analysis.phase_diagram import PhaseDiagram
# your code here
```

## When to Use This Skill
- Phase diagrams, reactions, Pourbaix, and thermochemistry
- Structure matching, dimensionality, or local environments
- Surface/interface analysis or property analysis (diffraction, elasticity, magnetism)

## Core Capabilities

### 1. Thermodynamics and Phase Stability
- Phase and chemical potential diagrams
- Reaction energies and Pourbaix analysis

### 2. Structure Analysis
- Structure matching and comparison
- Coordination environments (ChemEnv) and dimensionality

### 3. Surfaces and Properties
- Slabs, Wulff shapes, and interfaces
- Diffraction, elasticity, magnetism, and related utilities

## Quick Workflow
1. Gather `Structure`/`Molecule` or `Entry` inputs.
2. Choose the analysis module (phase diagram, matcher, surface, etc.).
3. Run analysis and export plots or derived data.

## Resources

### scripts/
Executable examples in the `scripts/` directory:

- `2013-01-01-Calculating_Reaction_Energies_with_the_Materials_API.py` - Reaction energies using Materials Project data.
- `2013-01-01-Plotting_and_Analyzing_a_Phase_Diagram_using_the_Materials_API.py` - Phase diagram plotting and analysis with MP data.
- `2017-04-03-Slab_generation_and_Wulff_shape.py` - Slab generation and Wulff shape construction.
- `2017-12-15-Plotting_a_Pourbaix_Diagram.py` - Pourbaix diagram plotting.
- `2018-01-01-ChemEnv_-_How_to_automatically_identify_coordination_environments_in_a_structure.py` - Automatic coordination environment identification (ChemEnv).
- `2018-03-09-Computing_the_Reaction_Diagram_between_Two_Compounds.py` - Reaction diagram between compounds.
- `2018-07-24-Adsorption_on_solid_surfaces.py` - Adsorption analysis on solid surfaces.
- `2018-11-6-Dopant_suggestions_using_Pymatgen.py` - Dopant suggestion workflows.
- `2019-03-11-Interface_Reactions.py` - Interface reaction analysis.
- `2021-5-12-Explanation_of_Corrections.py` - Energy correction explanations and usage.
- `2023-03-10-Plotting_a_Pourbaix_Diagram-new.py` - Updated Pourbaix diagram plotting example.
- `2024-06-28-Charge_Density_Difference.py` - Charge density difference analysis.

Note: Some scripts require Materials Project API access; set your API key before running.

### references/
Detailed reference material (load as needed):

- `references/analysis-workflows.md` - Common analyses and examples
- `references/docs/` - Local API docs for `pymatgen.analysis`
