# Extracted from notebook: 2018-03-09-Computing the Reaction Diagram between Two Compounds.ipynb
# Source: pymatgen examples (matgenb)

# Uncomment the subsequent lines in this cell to install dependencies for Google Colab.
# !pip install pymatgen

# ---

from pymatgen.analysis.phase_diagram import PhaseDiagram, ReactionDiagram
from pymatgen.entries.compatibility import ComputedEntry, MaterialsProjectCompatibility
from pymatgen.ext.matproj import MPRester

# ---

mp = MPRester()
compat = MaterialsProjectCompatibility()
chemsys = ["H", "P", "V", "O", "C"]

all_entries = mp.get_entries_in_chemsys(chemsys)

# ---

CO_entries = [e for e in all_entries if e.composition.reduced_formula == "CO"]
CO2_entries = [e for e in all_entries if e.composition.reduced_formula == "CO2"]
H2O_entries = [e for e in all_entries if e.composition.reduced_formula == "H2O"]
VPO5_entries = [e for e in all_entries if e.composition.reduced_formula == "VPO5"]

non_solid = ["CO", "CO2", "H2O", "VPO5"]

entries = list(
    filter(lambda e: e.composition.reduced_formula not in non_solid, all_entries)
)

# ---

potcars = []
for e in all_entries:
    if len(e.composition) == 1 and e.composition.reduced_formula in ["C", "H2", "O2"]:
        potcars.extend(e.parameters["potcar_spec"])

# ---

factor = 1000.0 / 6.0221409e23 / 1.60217662e-19
ec_form_energy = -682.8 * factor

ec = ComputedEntry(
    composition="C3H4O3", energy=0, parameters={"potcar_spec": list(potcars)}
)
ec.data["oxide_type"] = "oxide"

# MaterialsProjectCompatibility
ec = compat.process_entry(ec)

pd = PhaseDiagram(all_entries)
ec.uncorrected_energy = (
    ec_form_energy
    + sum(pd.el_refs[el].energy_per_atom * amt for el, amt in ec.composition.items())
    - ec.correction
)

# ---

vopo4 = []
vc = VaspToComputedEntryDrone()
for d in ["VOPO4/"]:
    e = vc.assimilate(d)
    e.data["oxide_type"] = "oxide"
    e = compat.process_entry(e)
    vopo4.append(e)

hxvopo4 = []
for d in ["HVOPO4/", "H2VOPO4/"]:
    e = vc.assimilate(d)
    e.data["oxide_type"] = "oxide"
    e = compat.process_entry(e)
    hxvopo4.append(e)

# ---

potcars = []
for e in all_entries:
    if len(e.composition) == 1 and e.composition.reduced_formula in ["C", "O2"]:
        potcars.extend(e.parameters["potcar_spec"])

co_form_energy = -110.53 * factor

co = ComputedEntry(
    composition="CO", energy=0, parameters={"potcar_spec": list(potcars)}
)
co.data["oxide_type"] = "oxide"
co = compat.process_entry(co)

pd = PhaseDiagram(all_entries)
co.uncorrected_energy = (
    co_form_energy
    + sum(pd.el_refs[el].energy_per_atom * amt for el, amt in co.composition.items())
    - co.correction
)

# ---

potcars = []
for e in all_entries:
    if len(e.composition) == 1 and e.composition.reduced_formula in ["C", "O2"]:
        potcars.extend(e.parameters["potcar_spec"])

co2_form_energy = -393.52 * factor

co2 = ComputedEntry(
    composition="CO2", energy=0, parameters={"potcar_symbols": list(potcars)}
)
co2.data["oxide_type"] = "oxide"
co2 = compat.process_entry(co2)

pd = PhaseDiagram(all_entries)
co2.uncorrected_energy = (
    co2_form_energy
    + sum(pd.el_refs[el].energy_per_atom * amt for el, amt in co2.composition.items())
    - co2.correction
)

# ---

potcars = []
for e in all_entries:
    if len(e.composition) == 1 and e.composition.reduced_formula in ["H2", "O2"]:
        potcars.extend(e.parameters["potcar_spec"])

h2o_form_energy = -286.629 * factor

h2o = ComputedEntry(
    composition="H2O", energy=0, parameters={"potcar_spec": list(potcars)}
)
h2o.data["oxide_type"] = "oxide"
h2o = compat.process_entry(h2o)

pd = PhaseDiagram(all_entries)
h2o.uncorrected_energy = (
    h2o_form_energy
    + sum(pd.el_refs[el].energy_per_atom * amt for el, amt in h2o.composition.items())
    - h2o.correction
)

# ---

entry1 = vopo4[0]
entry2 = ec
useful_entries = entries + hxvopo4 + [h2o, co2, co]

# ---

import matplotlib as mpl

mpl.rcParams["axes.linewidth"] = 3
mpl.rcParams["lines.markeredgewidth"] = 2
mpl.rcParams["lines.linewidth"] = 3
mpl.rcParams["lines.markersize"] = 13
mpl.rcParams["xtick.major.width"] = 3
mpl.rcParams["xtick.major.size"] = 8
mpl.rcParams["xtick.minor.width"] = 3
mpl.rcParams["xtick.minor.size"] = 4
mpl.rcParams["ytick.major.width"] = 3
mpl.rcParams["ytick.major.size"] = 8
mpl.rcParams["ytick.minor.width"] = 3
mpl.rcParams["ytick.minor.size"] = 4

# ---

ra = ReactionDiagram(entry1=entry1, entry2=entry2, all_entries=useful_entries)
cpd = ra.get_compound_pd()
plotter = PDPlotter(cpd, show_unstable=False)
plotter.get_plot(label_stable=False, label_unstable=False)
for i, l in ra.labels.items():
    print(f"{i} - {l}")
