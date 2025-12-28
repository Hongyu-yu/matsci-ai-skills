# Extracted from notebook: 2021-5-12-Explanation of Corrections.ipynb
# Source: pymatgen examples (matgenb)

# Uncomment the subsequent lines in this cell to install dependencies for Google Colab.
# !pip install pymatgen==2022.7.19
from __future__ import annotations

# ---

from pymatgen.entries.compatibility import MaterialsProjectCompatibility
from pymatgen.ext.matproj import MPRester

# ---

# retrieve
with MPRester() as m:
    entries = m.get_entries_in_chemsys("Cl-Mo-O")
entry = entries[0]

# ---

entries[25].energy_adjustments

# ---

compat = MaterialsProjectCompatibility()

entries = compat.process_entries(entries)

# ---

entries[25].energy_adjustments

# ---

entries[25].energy_per_atom

# ---

entries[25].correction_per_atom

# ---

entries[25].energy_adjustments = []
entries[25].energy_per_atom

# ---

entries[25].correction_per_atom

# ---

# retrieve
with MPRester() as m:
    entries = m.get_entries_in_chemsys("Cl-Mo-O", compatible_only=False)
entry = entries[0]

# ---

entries[25].energy_adjustments
