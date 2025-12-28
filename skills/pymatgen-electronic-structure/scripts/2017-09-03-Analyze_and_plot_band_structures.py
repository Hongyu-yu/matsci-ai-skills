# Extracted from notebook: 2017-09-03-Analyze and plot band structures.ipynb
# Source: pymatgen examples (matgenb)

# Uncomment the subsequent lines in this cell to install dependencies for Google Colab.
# !pip install pymatgen==2022.7.19
from __future__ import annotations

# ---

from pymatgen.electronic_structure.core import Spin
from pymatgen.ext.matproj import MPRester

# This initializes the Rest connection to the Materials Project db. Put your own API key if needed.
mpr = MPRester()
# load the band structure from mp-3748, CuAlO2 from the MP db
bs = mpr.get_bandstructure_by_material_id("mp-3748")

# ---

# is the material a metal (i.e., the fermi level cross a band)
print(bs.is_metal())
# print information on the band gap
print(bs.get_band_gap())
# print the energy of the 20th band and 10th kpoint
print(bs.bands[Spin.up][20][10])
# print energy of direct band gap
print(bs.get_direct_band_gap())
# print information on the vbm
print(bs.get_vbm())

# ---

%matplotlib inline
from pymatgen.electronic_structure.plotter import BSPlotter

plotter = BSPlotter(bs)
plotter.get_plot()

# ---

plotter.plot_brillouin()
