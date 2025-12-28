# Extracted from notebook: 2017-12-15-Plotting a Pourbaix Diagram.ipynb
# Source: pymatgen examples (matgenb)

# Uncomment the subsequent lines in this cell to install dependencies for Google Colab.
# !pip install pymatgen==2022.7.19
from __future__ import annotations

# ---

MP_API_KEY = "<your-legacy-API-key-here>"

# ---

# Import necessary tools from pymatgen
from pymatgen.analysis.pourbaix_diagram import PourbaixDiagram, PourbaixPlotter
from pymatgen.ext.matproj import MPRester

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
entry = [e for e in entries if e.entry_id == "mp-1692"][0]
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
)

# ---

plt = plotter.plot_entry_stability(entry)

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

bivo4_entry = [entry for entry in entries if entry.entry_id == "mp-545850"][0]
plt = plotter.plot_entry_stability(bivo4_entry)

# ---

bio2_entry = [entry for entry in entries if entry.entry_id == "mp-557993"][0]
plt = plotter.plot_entry_stability(bio2_entry)
