# Extracted from notebook: 2018-11-6-Dopant suggestions using Pymatgen.ipynb
# Source: pymatgen examples (matgenb)

# Uncomment the subsequent lines in this cell to install dependencies for Google Colab.
# !pip install pymatgen==2022.7.19

# ---

# Imports we need for generating dopant suggestions
from __future__ import annotations

from pprint import pprint

from pymatgen.analysis.local_env import CrystalNN
from pymatgen.analysis.structure_prediction.dopant_predictor import (
    get_dopants_from_shannon_radii,
    get_dopants_from_substitution_probabilities,
)
from pymatgen.ext.matproj import MPRester

# ---

# Establish rester for accessing Materials API

api_key = None  # INSERT YOUR OWN API KEY

mpr = MPRester()

# ---

num_dopants = 5  # number of highest probability dopants you wish to see

# ---

mp_id = "mp-856"  # Materials Project id for rutile SnO2

structure = mpr.get_structure_by_material_id(mp_id)

# ---

structure.add_oxidation_state_by_element({"Sn": 4, "O": -2})

# ---

structure.add_oxidation_state_by_guess()

# ---

species = structure.composition.elements

print(species)

# ---

cnn = CrystalNN()
bonded_structure = cnn.get_bonded_structure(structure)

# ---

dopants = get_dopants_from_shannon_radii(bonded_structure, num_dopants=num_dopants)

pprint(dopants)

# ---

threshold = 0.001  # probability threshold for substitution/structure predictions

# ---

dopants = get_dopants_from_substitution_probabilities(
    structure, num_dopants=num_dopants, threshold=threshold
)

pprint(dopants)
