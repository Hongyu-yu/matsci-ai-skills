# Extracted from notebook: 2018-09-25-Structure Prediction using Pymatgen and the Materials API.ipynb
# Source: pymatgen examples (matgenb)

# Uncomment the subsequent lines in this cell to install dependencies for Google Colab.
# !pip install pymatgen==2022.7.19

# ---

# Imports we need for running structure prediction
from __future__ import annotations

from pprint import pprint

from pymatgen.analysis.structure_matcher import ElementComparator, StructureMatcher
from pymatgen.analysis.structure_prediction.substitution_probability import (
    SubstitutionPredictor,
)
from pymatgen.analysis.structure_prediction.substitutor import Substitutor
from pymatgen.core.periodic_table import Specie
from pymatgen.ext.matproj import MPRester
from pymatgen.transformations.standard_transformations import (
    AutoOxiStateDecorationTransformation,
)

# ---

# Establish rester for accessing Materials API
mpr = MPRester()  # INSERT YOUR OWN API KEY

# ---

threshold = 0.001  # threshold for substitution/structure predictions
num_subs = 10  # number of highest probability substitutions you wish to see

# ---

original_species = [
    Specie("Y", 3),
    Specie("Mn", 3),
    Specie("O", -2),
]  # List of original species along with their specified oxidation states for substituting into

# ---

subs = SubstitutionPredictor(threshold=threshold).list_prediction(original_species)
subs.sort(key=lambda x: x["probability"], reverse=True)
subs = subs[0:num_subs]
pprint(subs)

# ---

trial_subs = [list(sub["substitutions"].keys()) for sub in subs]
pprint(trial_subs)

# ---

elem_sys_list = [[specie.element for specie in sub] for sub in trial_subs]

chemsys_set = set()
for sys in elem_sys_list:
    chemsys_set.add("-".join(map(str, sys)))

pprint(chemsys_set)

# ---

all_structs = {}
for chemsys in chemsys_set:
    all_structs[chemsys] = mpr.get_structures(
        chemsys
    )  # Getting all structures -- this can take a while!

# ---

auto_oxi = (
    AutoOxiStateDecorationTransformation()
)  # create object to determine oxidation states at each lattice site

# ---

oxi_structs = {}

for chemsys in all_structs:
    oxi_structs[chemsys] = []

    for num, struct in enumerate(all_structs[chemsys]):
        try:
            oxi_structs[chemsys].append(
                {
                    "structure": auto_oxi.apply_transformation(struct),
                    "id": str(chemsys + "_" + str(num)),
                }
            )
        except Exception:
            continue  # if auto oxidation fails, try next structure

# pprint(oxi_structs)

# ---

sbr = Substitutor(
    threshold=threshold
)  # create a Substitutor object with structure prediction threshold

# ---

trans_structs = {}

for chemsys in oxi_structs:
    trans_structs[chemsys] = sbr.pred_from_structures(
        original_species, oxi_structs[chemsys]
    )

# ---

# create object for structure matching
sm = StructureMatcher(comparator=ElementComparator(), primitive_cell=False)

# ---

filtered_structs = {}  # new filtered dictionary
seen_structs = []  # list of all seen structures, independent of chemical system

n_entries = sum(len(sys) for sys in trans_structs.values())
print(f"Number of entries BEFORE filtering: {n_entries}")

for chemsys in trans_structs:
    filtered_structs[chemsys] = []
    for struct in trans_structs[chemsys]:
        found = False
        for struct2 in seen_structs:
            if sm.fit(struct.final_structure, struct2.final_structure):
                found = True
                break
        if not found:
            filtered_structs[chemsys].append(struct)
            seen_structs.append(struct)

n_entries = sum(len(sys) for sys in filtered_structs.values())
print(f"Number of entries AFTER filtering: {n_entries}")

# ---

# get all known MP structures for original system
known_structs = mpr.get_structures("Y-Mn-O")

# ---

final_filtered_structs = {}
n_entries = sum(len(sys) for sys in filtered_structs.values())
print(f"Number of entries BEFORE filtering against MP: {n_entries}")

for chemsys in filtered_structs:
    final_filtered_structs[chemsys] = []
    for struct in filtered_structs[chemsys]:
        found = False
        for struct2 in known_structs:
            if sm.fit(struct.final_structure, struct2):
                found = True
                break
        if not found:
            final_filtered_structs[chemsys].append(struct)

n_entries = sum(len(sys) for sys in final_filtered_structs.values())
print(f"Number of entries AFTER filtering against MP: {n_entries}")
pprint(final_filtered_structs)

# ---

final_structs = {}
for chemsys in final_filtered_structs:
    final_structs[chemsys] = [
        struct.to_snl([{"name": "Matthew McDermott", "email": "N/A"}])
        for struct in final_filtered_structs[chemsys]
    ]

# Printing one of the StructureNL objects - this is a large dictionary!
# pprint(final_structs['Y-Fe-O'][0].as_dict())
