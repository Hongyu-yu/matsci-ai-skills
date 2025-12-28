# Extracted from notebook: 2013-01-01-Getting crystal structures from online sources.ipynb
# Source: pymatgen examples (matgenb)

# Uncomment the subsequent lines in this cell to install dependencies for Google Colab.
# !pip install pymatgen==2022.7.19
from __future__ import annotations

# ---

from pymatgen.ext.matproj import MPRester

# Note that you will need to add your Materials API key in your .pmgrc.yaml file as "PMG_MAPI_KEY".
# Alternatively, you will need to supply the API key as an arg to MPRester.
mpr = MPRester()

# ---

# Querying by formula only.
structures = mpr.get_structures("Li2O")
print(structures)

# ---

# Querying by chemical system only.
structures = mpr.get_structures("Li-O")
for s in structures:
    print(s.formula)
# A number of Li-O structures are returned with different Li:O ratios.
