# Extracted from notebook: 2017-04-14-Inputs and Analysis of VASP runs.ipynb
# Source: pymatgen examples (matgenb)

# Uncomment the subsequent lines in this cell to install dependencies for Google Colab.
# !pip install pymatgen==2022.7.19

# ---

from pymatgen.core import Structure
from pymatgen.io.vasp.sets import MPRelaxSet

s = Structure.from_file("Al-relax/Al.cif", primitive=True)
custom_settings = {"NELMIN": 5}  # user custom incar settings
relax = MPRelaxSet(s, user_incar_settings=custom_settings)
relax.write_input("Al-relax")

# ---

from pymatgen.io.vasp import Vasprun

v = Vasprun("Al-relax/vasprun.xml.gz")
print(v.final_energy)  # final total energy
s = v.final_structure
s.to(fmt="cif")  # save relaxed structure into cif file
print(s)  # relaxed structure

# ---

from pymatgen.io.vasp.sets import MPStaticSet

custom_settings = {"NELM": 60}  # user custom incar settings
static = MPStaticSet.from_prev_calc(
    "Al-relax/", standardize=True, user_incar_settings=custom_settings
)
static.write_input("Al-static")

# ---

from pymatgen.io.vasp import Vasprun

v = Vasprun("Al-static/vasprun.xml.gz")
print(v.final_energy)  # final total energy

# ---

from pymatgen.io.vasp.sets import MPNonSCFSet

# generate uniform k-points for DOS calc.
custom_settings = {"LAECHG": "False", "LVHAR": "False"}  # user custom incar settings
dos = MPNonSCFSet.from_prev_calc(
    "Al-static/",
    mode="uniform",
    reciprocal_density=200,
    user_incar_settings=custom_settings,
)
dos.write_input("Al-dos")

# generate k-points along high symmetry line for band structure calc.
band = MPNonSCFSet.from_prev_calc(
    "Al-static/", mode="line", standardize=True, user_incar_settings=custom_settings
)
band.write_input("Al-band")

# ---

from pymatgen.electronic_structure.plotter import DosPlotter
from pymatgen.io.vasp import Vasprun

v = Vasprun("Al-dos/vasprun.xml.gz")
tdos = v.tdos
plotter = DosPlotter()
plotter.add_dos("Total DOS", tdos)
plotter.show(xlim=[-5, 5], ylim=[0, 4])

# ---

from pymatgen.electronic_structure.plotter import DosPlotter
from pymatgen.io.vasp import Vasprun

v = Vasprun("Al-dos/vasprun.xml.gz")
cdos = v.complete_dos
element_dos = cdos.get_element_dos()
plotter = DosPlotter()
plotter.add_dos_dict(element_dos)
plotter.show(xlim=[-5, 5], ylim=[0, 1])

# ---

from pymatgen.electronic_structure.plotter import DosPlotter
from pymatgen.io.vasp import Vasprun

v = Vasprun("Al-dos/vasprun.xml.gz")
cdos = v.complete_dos
spd_dos = cdos.get_spd_dos()
plotter = DosPlotter()
plotter.add_dos_dict(spd_dos)
plotter.show(xlim=[-5, 5], ylim=[0, 1])

# ---

from pymatgen.electronic_structure.plotter import BSPlotter
from pymatgen.io.vasp import BSVasprun, Vasprun

v = BSVasprun("Al-band/vasprun.xml.gz")
bs = v.get_band_structure(kpoints_filename="Al-band/KPOINTS", line_mode=True)
plt = BSPlotter(bs)
plt.get_plot(vbm_cbm_marker=True)
