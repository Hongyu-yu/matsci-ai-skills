# Extracted from notebook: 2023-03-10-Plotting a Pourbaix Diagram-new.ipynb
# Source: pymatgen examples (matgenb)

# Uncomment the subsequent lines in this cell to install dependencies for Google Colab.
# !pip install pymatgen==2022.7.19
# !pip install mp-api
from __future__ import annotations

# ---

MP_API_KEY = "<your-legacy-API-key-here>"

# ---

# Import necessary tools from pymatgen
from mp_api.client import MPRester
from pymatgen.analysis.pourbaix_diagram import PourbaixDiagram, PourbaixPlotter

%matplotlib inline

# Initialize the MP Rester
mpr = MPRester()

# ---

# Get all pourbaix entries corresponding to the Cu-O-H chemical system.
entries = mpr.get_pourbaix_entries(["Cu"])

# ---

# Construct the PourbaixDiagram object
pbx = PourbaixDiagram(entries)

# ---

# Get an entry stability as a function of pH and V
entry = [e for e in entries if e.entry_id == "mp-1692-GGA"][0]
print(
    "CuO's potential energy per atom relative to the most",
    f"stable decomposition product is {pbx.get_decomposition_energy(entry, pH=7, V=-0.2):0.2f} eV/atom",
)

# ---

plotter = PourbaixPlotter(pbx)

# ---

plotter.get_pourbaix_plot().show()

# ---

plotter.get_pourbaix_plot(
    limits=[[0, 14], [-2, 2]],  # pH and E limits
    title="Customized Pourbaix Plot",
    label_domains=True,  # set True to label phases
    label_fontsize=10,  # font size for the phase labels
    show_neutral_axes=False,  # show or hide axes at pH=0, E=0
    show_water_lines=False,  # show or hide lines for water stability
).show()

# ---

plt = plotter.plot_entry_stability(entry)
plt.show()

# ---

# Get all pourbaix entries corresponding to the Bi-V-O-H chemical system.
entries = mpr.get_pourbaix_entries(["Bi", "V"])
# Construct the PourbaixDiagram object
pbx = PourbaixDiagram(
    entries,
    comp_dict={"Bi": 0.5, "V": 0.5},
    conc_dict={"Bi": 1e-8, "V": 1e-8},
    filter_solids=True,
)

# ---

# Construct the pourbaix analyzer
plotter = PourbaixPlotter(pbx)
plt = plotter.get_pourbaix_plot()
plt.show()

# ---

bivo4_entry = [entry for entry in entries if entry.entry_id == "mp-545850-GGA+U"][0]
plt = plotter.plot_entry_stability(bivo4_entry)

# ---

bio2_entry = [entry for entry in entries if entry.entry_id == "mp-557993-GGA"][0]
plt = plotter.plot_entry_stability(bio2_entry)

# ---

with MPRester() as m:
    solid_entries = m.get_entries_in_chemsys("Bi-V-O-H")

# ---

from pymatgen.entries.compatibility import MaterialsProjectAqueousCompatibility

aqcompat = MaterialsProjectAqueousCompatibility()
solid_entries = aqcompat.process_entries(solid_entries)

# ---

from pymatgen.analysis.phase_diagram import PhaseDiagram
from pymatgen.analysis.pourbaix_diagram import PourbaixEntry
from pymatgen.entries.computed_entries import ComputedEntry

free_energy_entries = []

pd = PhaseDiagram(solid_entries)
for v in pd.stable_entries:
    if v.composition.chemical_system in ["O", "H", "H-O"]:
        continue
    # create a new ComputedEntry with the formation energy. Copy all other parameters
    # from the original ComputedEntry.
    free_energy_entries.append(
        ComputedEntry(v.composition, pd.get_form_energy(v), parameters=v.parameters)
    )

# ---

with MPRester() as m:
    ion_data = m.get_ion_reference_data_for_chemsys(["Bi", "V"])

# ---

from pymatgen.analysis.phase_diagram import PhaseDiagram

with MPRester() as m:
    ion_entries = m.get_ion_entries(pd, ion_data)

# ---

pbx_entries = [PourbaixEntry(e) for e in free_energy_entries]
pbx_entries.extend([PourbaixEntry(e) for e in ion_entries])

# ---

pbx = PourbaixDiagram(pbx_entries)
pbplotter = PourbaixPlotter(pbx).get_pourbaix_plot().show()
