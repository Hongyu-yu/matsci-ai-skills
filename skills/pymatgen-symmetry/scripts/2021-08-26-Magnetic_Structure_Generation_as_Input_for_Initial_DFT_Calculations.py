# Extracted from notebook: 2021-08-26-Magnetic Structure Generation as Input for Initial DFT Calculations.ipynb
# Source: pymatgen examples (matgenb)

# Uncomment the subsequent lines in this cell to install dependencies for Google Colab.
# !pip install pymatgen==2022.7.19
from __future__ import annotations

# ---

from pymatgen.analysis.magnetism.analyzer import CollinearMagneticStructureAnalyzer
from pymatgen.ext.matproj import MPRester
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.util.testing import PymatgenTest

# ---

# Specify location of CIF on your device
structure = PymatgenTest.get_structure("LiFePO4")
print(structure)

# ---

magmom = CollinearMagneticStructureAnalyzer(
    structure, overwrite_magmom_mode="replace_all_if_undefined"
)

# ---

# Assume an initial ferromagnetic order
fm_structure = magmom.get_ferromagnetic_structure(make_primitive=True)

# ---

print(fm_structure)

# ---

order = magmom.ordering  # Useful if magnetic order is unknown or not user-defined
print(order)

# ---

spa = SpacegroupAnalyzer(structure)
spa.get_point_group_symbol()

# ---

spa.get_space_group_symbol()

# ---

fm_structure.to(filename="lfp.mcif")  # Save the structure in magCIF format.

# ---

spn_structure = (
    magmom.get_structure_with_spin()
)  # Returns spin decorated values in structure instead of magmom site properties
print(spn_structure)

# ---

# Establish rester for accessing Materials API
mpr = MPRester()
mp_id = "mp-504263"  # Previously reported structure; Co replaced at Fe site
structure_from_mp = mpr.get_structure_by_material_id(mp_id)
print(structure)

# ---

mgmmnt = CollinearMagneticStructureAnalyzer(
    structure_from_mp, overwrite_magmom_mode="replace_all_if_undefined"
)

# ---

mgmmnt.is_magnetic

# ---

mgmmnt.magnetic_species_and_magmoms

# ---

mgmmnt.ordering
