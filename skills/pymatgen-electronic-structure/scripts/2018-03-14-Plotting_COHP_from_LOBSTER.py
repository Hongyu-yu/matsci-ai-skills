# Extracted from notebook: 2018-03-14-Plotting COHP from LOBSTER.ipynb
# Source: pymatgen examples (matgenb)

# Uncomment the subsequent lines in this cell to install dependencies for Google Colab.
# !pip install pymatgen==2022.7.19

# ---

from pymatgen.electronic_structure.cohp import Cohp
from pymatgen.electronic_structure.plotter import CohpPlotter
from pymatgen.io.lobster import Cohpcar

COHPCAR_path = "lobster_data/COHPCAR.lobster"
cohpcar = Cohpcar(filename=COHPCAR_path)
cdata = cohpcar.cohp_data
cdata_processed = {}
for key in cdata:
    c = cdata[key]
    c["efermi"] = 0
    c["energies"] = cohpcar.energies
    c["are_coops"] = False
    cdata_processed[key] = Cohp.from_dict(c)
cp = CohpPlotter()
cp.add_cohp_dict(cdata_processed)
ax = cp.get_plot()
ax.set_ylim([-6, 6])
