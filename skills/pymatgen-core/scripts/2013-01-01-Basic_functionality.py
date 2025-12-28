# Extracted from notebook: 2013-01-01-Basic functionality.ipynb
# Source: pymatgen examples (matgenb)

# Uncomment the subsequent lines in this cell to install dependencies for Google Colab.
# !pip install pymatgen

# ---

import pymatgen.core as mg

# ---

si = mg.Element("Si")
print(f"Atomic mass of Si is {si.atomic_mass}")
print(f"Si has a melting point of {si.melting_point}")
print(f"Ionic radii for Si: {si.ionic_radii}")

# ---

print("Atomic mass of Si in kg: {}".format(si.atomic_mass.to("kg")))

# ---

fe2 = mg.Species("Fe", 2)
print(fe2.atomic_mass)
print(fe2.ionic_radius)

# ---

comp = mg.Composition("Fe2O3")
print(f"Weight of Fe2O3 is {comp.weight}")
print("Amount of Fe in Fe2O3 is {}".format(comp["Fe"]))
print("Atomic fraction of Fe is {}".format(comp.get_atomic_fraction("Fe")))
print("Weight fraction of Fe is {}".format(comp.get_wt_fraction("Fe")))

# ---

# Creates cubic Lattice with lattice parameter 4.2
lattice = mg.Lattice.cubic(4.2)
print(lattice.parameters)

# ---

structure = mg.Structure(lattice, ["Cs", "Cl"], [[0, 0, 0], [0.5, 0.5, 0.5]])
print(f"Unit cell vol = {structure.volume}")
print(f"First site of the structure is {structure[0]}")

# ---

structure.make_supercell([2, 2, 1])  # Make a 3 x 2 x 1 supercell of the structure
del structure[0]  # Remove the first site
structure.append("Na", [0, 0, 0])  # Append a Na atom.
structure[-1] = "Li"  # Change the last added atom to Li.
structure[0] = "Cs", [
    0.01,
    0.5,
    0,
]  # Shift the first atom by 0.01 in fractional coordinates in the x-direction.
immutable_structure = mg.IStructure.from_sites(
    structure
)  # Create an immutable structure (cannot be modified).
print(immutable_structure)

# ---

# Determining the symmetry
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer

finder = SpacegroupAnalyzer(structure)
print(f"The spacegroup is {finder.get_space_group_symbol()}")

# ---

from pymatgen.analysis.structure_matcher import StructureMatcher

# Let's create two structures which are the same topologically, but with different elements, and one lattice is larger.
s1 = mg.Structure(lattice, ["Cs", "Cl"], [[0, 0, 0], [0.5, 0.5, 0.5]])
s2 = mg.Structure(mg.Lattice.cubic(5), ["Rb", "F"], [[0, 0, 0], [0.5, 0.5, 0.5]])
m = StructureMatcher()
print(
    m.fit_anonymous(s1, s2)
)  # Returns a mapping which maps s1 and s2 onto each other. Strict element fitting is also available.

# ---

# Convenient IO to various formats. Format is intelligently determined from file name and extension.
structure.to(filename="POSCAR")
structure.to(filename="CsCl.cif")

# Or if you just supply fmt, you simply get a string.
print(structure.to(fmt="poscar"))
print(structure.to(fmt="cif"))

# ---

# Reading a structure from a file.
structure = mg.Structure.from_file("POSCAR")

# ---

from pymatgen.io.vasp.sets import MPRelaxSet

v = MPRelaxSet(structure)
v.write_input(
    "MyInputFiles"
)  # Writes a complete set of input files for structure to the directory MyInputFiles
