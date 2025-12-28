# Extracted from notebook: 2019-03-11-Interface Reactions.ipynb
# Source: pymatgen examples (matgenb)

# Uncomment the subsequent lines in this cell to install dependencies for Google Colab.
# !pip install pymatgen==2022.7.19
from __future__ import annotations

# ---

from pymatgen.analysis.interface_reactions import InterfacialReactivity
from pymatgen.analysis.phase_diagram import GrandPotentialPhaseDiagram, PhaseDiagram
from pymatgen.core import Composition, Element
from pymatgen.ext.matproj import MPRester

%matplotlib inline

# Initialize the REST API interface. You may need to put your own API key in as an arg.
mpr = MPRester()

# ---

# Chemical formulae for two solid reactants.
reactant1 = "LiCoO2"
reactant2 = "Li3PS4"

# Is the system open to an elemental reservoir?
grand = True

if grand:
    # Element in the elemental reservoir.
    open_el = "Co"
    # Relative chemical potential vs. pure substance. Must be non-positive.
    relative_mu = -1

# ---

# Get the compositions of the reactants
comp1 = Composition(reactant1)
comp2 = Composition(reactant2)

# Gather all elements involved in the chemical system.
elements = [e.symbol for e in comp1.elements + comp2.elements]
if grand:
    elements.append(open_el)
elements = list(set(elements))  # Remove duplicates

# Get all entries in the chemical system
entries = mpr.get_entries_in_chemsys(elements)

# Build a phase diagram using these entries.
pd = PhaseDiagram(entries)

# For an open system, include the grand potential phase diagram.
if grand:
    # Get the chemical potential of the pure subtance.
    mu = pd.get_transition_chempots(Element(open_el))[0]
    # Set the chemical potential in the elemental reservoir.
    chempots = {open_el: relative_mu + mu}
    # Build the grand potential phase diagram
    gpd = GrandPotentialPhaseDiagram(entries, chempots)
    # Create InterfacialReactivity object.
    interface = InterfacialReactivity(
        comp1,
        comp2,
        gpd,
        norm=True,
        include_no_mixing_energy=True,
        pd_non_grand=pd,
        use_hull_energy=False,
    )
else:
    interface = InterfacialReactivity(
        comp1,
        comp2,
        pd,
        norm=True,
        include_no_mixing_energy=False,
        pd_non_grand=None,
        use_hull_energy=False,
    )

# ---

plt = interface.plot()

# ---

from collections import OrderedDict

import pandas as pd

critical_rxns = [
    OrderedDict(
        [
            ("Atomic fraction", round(ratio, 3)),
            ("Reaction equation", rxn),
            ("E$_{rxt}$ per mol equation (kJ/mol)", round(rxn_energy, 1)),
            ("E$_{rxt}$ per reactant atom (eV/atom)", round(reactivity, 3)),
        ]
    )
    for _, ratio, reactivity, rxn, rxn_energy in interface.get_kinks()
]
interface_reaction_table = pd.DataFrame(critical_rxns)
interface_reaction_table

# ---

import numpy as np

interface_reaction_table["Molar fraction"] = pd.Series(
    np.round(interface.get_critical_original_kink_ratio(), 3)
)
interface_reaction_table

# ---

rxn = critical_rxns[2]["Reaction equation"]
print(rxn)
print(type(rxn))

# ---

# Get interface reaction information for reactants LiCoO2 and Li3PS4 in open system to Co.
kinks_from_API = mpr.get_interface_reactions(
    "LiCoO2", "Li3PS4", open_el="Co", relative_mu=-1, use_hull_energy=False
)

# Get inforamtion for the second critical reaction.
print(kinks_from_API[1])

# ---

critical_rxns_from_API = [
    OrderedDict(
        [
            ("Atomic fraction", round(reaction["ratio_atomic"], 3)),
            ("Molar fraction", round(reaction["ratio_molar"], 3)),
            ("Reaction equation", reaction["rxn_str"]),
            (
                "E$_{rxt}$ per mol equation (kJ/mol)",
                round(float(reaction["rxn_energy_sigdig_kJmol"]), 1),
            ),
            ("E$_{rxt}$ per reactant atom (eV/atom)", round(reaction["energy"], 3)),
        ]
    )
    for reaction in kinks_from_API
]
pd.DataFrame(critical_rxns_from_API)
