# Extracted from notebook: 2013-01-01-Calculating Reaction Energies with the Materials API.ipynb
# Source: pymatgen examples (matgenb)

# Uncomment the subsequent lines in this cell to install dependencies for Google Colab.
# !pip install pymatgen==2022.7.19

# ---

from pymatgen.analysis.reaction_calculator import ComputedReaction
from pymatgen.core import Composition
from pymatgen.core.units import FloatWithUnit
from pymatgen.entries.computed_entries import ComputedEntry
from pymatgen.ext.matproj import MPRester

# This initializes the REST adaptor. Put your own API key in if necessary.
mpr = MPRester()

# This gets all entries belonging to the Ca-C-O system.
all_entries = mpr.get_entries_in_chemsys(["Ca", "C", "O"])


# This method simply gets the lowest energy entry for all entry with the same composition.
def get_most_stable_entry(formula):
    relevant_entries = [
        entry
        for entry in all_entries
        if entry.composition.reduced_formula == Composition(formula).reduced_formula
    ]
    relevant_entries = sorted(relevant_entries, key=lambda e: e.energy_per_atom)
    return relevant_entries[0]


CaO = get_most_stable_entry("CaO")
CO2 = get_most_stable_entry("CO2")
CaCO3 = get_most_stable_entry("CaCO3")

reaction = ComputedReaction([CaO, CO2], [CaCO3])
energy = FloatWithUnit(reaction.calculated_reaction_energy, "eV atom^-1")

print("Caculated")
print(reaction)
print("Reaction energy = {}".format(energy.to("kJ mol^-1")))
