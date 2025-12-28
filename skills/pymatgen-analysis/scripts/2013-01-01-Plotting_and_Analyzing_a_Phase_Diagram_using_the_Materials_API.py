# Extracted from notebook: 2013-01-01-Plotting and Analyzing a Phase Diagram using the Materials API.ipynb
# Source: pymatgen examples (matgenb)

# Uncomment the subsequent lines in this cell to install dependencies for Google Colab.
# !pip install pymatgen==2022.7.19
from __future__ import annotations

# ---

from pymatgen.analysis.phase_diagram import PDPlotter, PhaseDiagram
from pymatgen.ext.matproj import MPRester

%matplotlib inline

# ---

# This initializes the REST adaptor. You may need to put your own API key in as an arg.
mpr = MPRester()

# Entries are the basic unit for thermodynamic and other analyses in pymatgen.
# This gets all entries belonging to the Ca-C-O system.
entries = mpr.get_entries_in_chemsys(["Ca", "C", "O"])

# With entries, you can do many sophisticated analyses, like creating phase diagrams.
pd = PhaseDiagram(entries)

# ---

# Let's show all phases, including unstable ones
plotter = PDPlotter(pd, show_unstable=0.2, backend="matplotlib")
plotter.show()

# ---

import collections

data = collections.defaultdict(list)
for e in entries:
    decomp, ehull = pd.get_decomp_and_e_above_hull(e)
    data["Materials ID"].append(e.entry_id)
    data["Composition"].append(e.composition.reduced_formula)
    data["Ehull"].append(ehull)
    data["Decomposition"].append(
        " + ".join([f"{v:.2f} {k.composition.formula}" for k, v in decomp.items()])
    )

from pandas import DataFrame

df = DataFrame(data, columns=["Materials ID", "Composition", "Ehull", "Decomposition"])

print(df.head(30))
