# Extracted from notebook: 2020-07-15-How to plot a Fermi surface with Boltztrap - notest.ipynb
# Source: pymatgen examples (matgenb)

# Uncomment the subsequent lines in this cell to install dependencies for Google Colab.
# !pip install pymatgen==2022.7.19
from __future__ import annotations

# ---

import os

from pymatgen.electronic_structure.boltztrap import BoltztrapRunner
from pymatgen.electronic_structure.core import Spin
from pymatgen.electronic_structure.plotter import plot_fermi_surface
from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.symmetry.bandstructure import HighSymmKpath

# ---

vrun = Vasprun("boltztrap2_data/vasprun-PbTe_uniform_bs.xml")
bs = vrun.get_band_structure()
nelect = vrun.parameters["NELECT"]

# ---

# specify here the band index you need, in this example the vbm is taken
vbm = bs.get_vbm()["band_index"][Spin.up][-1]

# ---

# create the directory "fermi/vbm" before
os.makedirs("fermi/vbm/", exist_ok=True)

# run the interpolation, lpfac should be between 50 and 150
BoltztrapRunner(
    bs=bs, nelec=nelect, lpfac=10, run_type="FERMI", band_nb=vbm, cond_band=False
).run(path_dir="fermi/vbm/")

# read the output
an = BoltztrapAnalyzer.from_files("fermi/vbm/boltztrap/")

# ---

# prepare high symmetry points labels
st = vrun.final_structure
kpoints_dict = HighSymmKpath(st).kpath["kpoints"]

# ---

# edit or generete a dict like this one to pass the kpoint labels and frac coords you want to plot
kpoints_dict

# ---

an.fermi_surface_data.max()

# ---

# plot the surface in an external window
# vbm is set at 0 eV, so we set an energy level of 0.05 below the vbm
plot_fermi_surface(
    an.fermi_surface_data,
    bs.structure,
    cbm=False,
    energy_levels=[-0.05],
    kpoints_dict=kpoints_dict,
    labels_scale_factor=0.1,
)

# ---

# specify here another band index you need, in this example the cbm is taken
cbm = bs.get_cbm()["band_index"][Spin.up][0]

# ---

# create the directory "fermi/cbm" before
os.makedirs("fermi/cbm/", exist_ok=True)

# run the interpolation, lpfac should be between 50 and 150
BoltztrapRunner(
    bs=bs, nelec=nelect, lpfac=10, run_type="FERMI", band_nb=cbm, cond_band=True
).run(path_dir="fermi/cbm/")

# read the output
an = BoltztrapAnalyzer.from_files("fermi/cbm/boltztrap/")

# ---

an.fermi_surface_data.max()

# ---

# plot the surface in an external window
# cbm is at ~0.83 eV, so we set an energy level of 0.07 above the cbm

plot_fermi_surface(
    an.fermi_surface_data,
    bs.structure,
    cbm=True,
    energy_levels=[0.9],
    kpoints_dict=kpoints_dict,
    labels_scale_factor=0.1,
)

# ---

vrun = Vasprun("boltztrap2_data/vasprun_AlAs.xml.gz")
bs = vrun.get_band_structure()
nelect = vrun.parameters["NELECT"]

# ---

cbm = bs.get_cbm()["band_index"][Spin.up][0]
vb1 = bs.get_vbm()["band_index"][Spin.up][-1]
vb2 = bs.get_vbm()["band_index"][Spin.up][-2]
vb3 = bs.get_vbm()["band_index"][Spin.up][-3]

# ---

cbm, vb1, vb2, vb3

# ---

st = vrun.final_structure
kpoints_dict = HighSymmKpath(st).kpath["kpoints"]

# ---

kpoints_dict

# ---

os.makedirs("fermi/cbm/", exist_ok=True)

# run the interpolation, lpfac should be between 50 and 150
BoltztrapRunner(
    bs=bs, nelec=nelect, lpfac=5, run_type="FERMI", band_nb=cbm, cond_band=True
).run(path_dir="fermi/cbm/")

# read the output
an = BoltztrapAnalyzer.from_files("fermi/cbm/boltztrap/")

# plot the fermi surface and get the figure object
fig, mlab = plot_fermi_surface(
    an.fermi_surface_data,
    bs.structure,
    cbm=True,
    energy_levels=[1.55],
    kpoints_dict=kpoints_dict,
    labels_scale_factor=0.1,
    interative=False,
    multiple_figure=False,
    color=(1, 0, 0),
)

# ---

for vb, tf in zip((vb1, vb2, vb3), (0.2, 0.4, 1)):
    os.makedirs(f"fermi/vb_{vb}", exist_ok=True)
    # run the interpolation, lpfac should be between 50 and 150
    BoltztrapRunner(
        bs=bs, nelec=nelect, lpfac=50, run_type="FERMI", band_nb=vb, cond_band=False
    ).run(path_dir=f"fermi/vb_{vb}/")

    # read the output
    an = BoltztrapAnalyzer.from_files(f"fermi/vb_{vb}/boltztrap/")

    # plot the fermi surface in the previous figure object
    fig, mlab = plot_fermi_surface(
        an.fermi_surface_data,
        bs.structure,
        cbm=False,
        energy_levels=[-0.07],
        kpoints_dict=kpoints_dict,
        labels_scale_factor=0.1,
        interative=False,
        mlab_figure=fig,
        multiple_figure=False,
        transparency_factor=[tf],
    )
mlab.show()

# ---

from pymatgen.electronic_structure.boltztrap import read_cube_file

# decompress boltztrap_BZ.cube.gz before running the following
fs_data = read_cube_file("boltztrap2_data/boltztrap_BZ.cube")
st = Vasprun("boltztrap2_data/vasprun_mp-12103.xml.gz").final_structure
kpoints_dict = HighSymmKpath(st).kpath["kpoints"]

# ---

plot_fermi_surface(
    fs_data,
    st,
    cbm=True,
    kpoints_dict=kpoints_dict,
    labels_scale_factor=0.1,
    color=(1, 0, 0),
)

# ---

from pymatgen.electronic_structure.boltztrap2 import BztInterpolator, VasprunBSLoader

# ---

vrun = Vasprun("boltztrap2_data/vasprun-PbTe_uniform_bs.xml")
bs = vrun.get_band_structure()
nelect = vrun.parameters["NELECT"]

# ---

data = VasprunBSLoader(vrun)

# ---

bztI = BztInterpolator(data, lpfac=10)

# ---

bztI.eband.shape

# ---

from BoltzTraP2 import fermisurface

# ---

# with 2:3 we get the index of the vb, mu is in Ha
fermisurface.plot_fermisurface(data, bztI.equivalences, bztI.eband[2:3, :], mu=-0.003)
