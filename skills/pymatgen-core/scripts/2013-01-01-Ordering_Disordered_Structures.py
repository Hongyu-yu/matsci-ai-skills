# Extracted from notebook: 2013-01-01-Ordering Disordered Structures.ipynb
# Source: pymatgen examples (matgenb)

# Uncomment the subsequent lines in this cell to install dependencies for Google Colab.
# !pip install pymatgen==2022.7.19

# ---

# Let us start by creating a disordered CuAu fcc structure.
from pymatgen.core import Lattice, Structure

specie = {"Cu0+": 0.5, "Au0+": 0.5}
cuau = Structure.from_spacegroup("Fm-3m", Lattice.cubic(3.677), [specie], [[0, 0, 0]])
print(cuau)

# ---

from pymatgen.transformations.standard_transformations import (
    OrderDisorderedStructureTransformation,
)

trans = OrderDisorderedStructureTransformation()

ss = trans.apply_transformation(cuau, return_ranked_list=100)

print(len(ss))

print(ss[0])

# ---

from pymatgen.analysis.structure_matcher import StructureMatcher

matcher = StructureMatcher()
groups = matcher.group_structures([d["structure"] for d in ss])
print(len(groups))
print(groups[0][0])

# ---

from pymatgen.transformations.advanced_transformations import (
    EnumerateStructureTransformation,
)

specie = {"Cu": 0.5, "Au": 0.5}
cuau = Structure.from_spacegroup("Fm-3m", Lattice.cubic(3.677), [specie], [[0, 0, 0]])

trans = EnumerateStructureTransformation(max_cell_size=3)
ss = trans.apply_transformation(cuau, return_ranked_list=1000)

# ---

print(len(ss))
print("cell sizes are %s" % ([len(d["structure"]) for d in ss]))

# ---

# The following two lines write all the structures to CIF files with names CuAu_0.cif, CuAu_1.cif, ...
for i, d in enumerate(ss):
    d["structure"].to(filename="CuAu_%d.cif" % i)
