# Pymatgen Analysis - Workflow Guide

## Overview

This reference covers analysis tools in `pymatgen.analysis` for thermodynamics,
structure comparison, surfaces, and property calculations.

## Core Purpose

Use analysis modules to:
- Build phase and Pourbaix diagrams
- Compute reactions and energies from entries
- Match and compare structures
- Analyze surfaces/interfaces and local environments
- Access diffraction, elasticity, magnetism, and related utilities

## Key Modules and Classes

### Thermodynamics and phase stability
- `PhaseDiagram`, `GrandPotentialPhaseDiagram`
- `PDPlotter`, `CompoundPhaseDiagram`
- `Reaction`, `ComputedReaction`, `ReactionCalculator`
- `PourbaixDiagram`, `PourbaixPlotter`

### Structure analysis
- `StructureMatcher`, `SpeciesComparator`
- `dimensionality` utilities
- `StructureAnalyzer`, `MoleculeStructureComparator`
- `local_env` and `chemenv` for coordination environments

### Surfaces and interfaces
- `SlabGenerator`, `WulffShape`
- `surface_analysis`, `interface_reactions`

### Physical properties
- `diffraction`, `elasticity`, `magnetism`, `optics`, `xas`, `xps`

## Common Workflows

### Build a phase diagram from entries
```python
from pymatgen.analysis.phase_diagram import PhaseDiagram, PDPlotter
from pymatgen.entries.computed_entries import ComputedEntry

entries = [
    ComputedEntry("Li", -1.0),
    ComputedEntry("Fe", -2.0),
    ComputedEntry("O2", -4.0),
    ComputedEntry("LiFeO2", -10.5),
]

pd = PhaseDiagram(entries)
plotter = PDPlotter(pd)
plotter.get_plot()
```

### Compute a reaction energy
```python
from pymatgen.analysis.reaction_calculator import ComputedReaction
from pymatgen.entries.computed_entries import ComputedEntry

reactants = [ComputedEntry("Li", -1.0), ComputedEntry("Fe", -2.0)]
products = [ComputedEntry("LiFe", -4.2)]
rxn = ComputedReaction(reactants, products)
print(rxn.energy)
```

### Structure matching
```python
from pymatgen.analysis.structure_matcher import StructureMatcher
from pymatgen.core import Structure

s1 = Structure.from_file("POSCAR")
s2 = Structure.from_file("CONTCAR")
matcher = StructureMatcher()
print(matcher.fit(s1, s2))
```

### Local environment analysis
```python
from pymatgen.analysis.local_env import CrystalNN
from pymatgen.core import Structure

structure = Structure.from_file("POSCAR")
cnn = CrystalNN()
for idx in range(len(structure)):
    print(idx, cnn.get_nn_info(structure, idx))
```

## Tips and Pitfalls

- Most thermodynamic analysis expects `ComputedEntry` or compatible entry objects.
- For structure comparison, ensure both structures are standardized (e.g., use
  `StructureMatcher` defaults or apply symmetry reduction first).
- Surface and interface tools assume sensible lattice vectors; validate orientation.
