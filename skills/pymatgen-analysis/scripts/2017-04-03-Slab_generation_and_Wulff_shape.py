# Extracted from notebook: 2017-04-03-Slab generation and Wulff shape.ipynb
# Source: pymatgen examples (matgenb)

# Uncomment the subsequent lines in this cell to install dependencies for Google Colab.
# !pip install pymatgen==2022.7.19

# ---

# Import the necessary tools for making a Wulff shape
from __future__ import annotations

from pymatgen.analysis.wulff import WulffShape

# Import the necessary tools to generate surfaces
from pymatgen.core.surface import Lattice, SlabGenerator, Structure, generate_all_slabs

# ---

# Let's start with fcc Ni
lattice = Lattice.cubic(3.508)
Ni = Structure(
    lattice,
    ["Ni", "Ni", "Ni", "Ni"],
    [[0, 0, 0], [0, 0.5, 0], [0.5, 0, 0], [0, 0, 0.5]],
)

# ---

# We'll use the SlabGenerator class to get a single slab. We'll start with the
# (111) slab of Ni. Plug in the CONVENTIONAL unit cell of your structure, the
# maximum Miller index value to generate the different slab orientations along
# with the minimum slab and vacuum size in Angstroms
slabgen = SlabGenerator(Ni, (1, 1, 1), 10, 10)

# If we want to find all terminations for a particular Miller index orientation,
# we use the get_slabs() method. This returns a LIST of slabs rather than a single
# slab. When generating a slab for a particular orientation, there are sometimes
# more than one location we can terminate or cut the structure to create a slab. The
# simplest example of this would be the Si(Fd-3m) (111) slab which can be cut or
# terminated in two different locations along the vector of the Miller index. For a
# fcc structure such as Ni however, there should only be one way to cut a (111) slab.
all_slabs = slabgen.get_slabs()
print("The Ni(111) slab only has %s termination." % (len(all_slabs)))

# ---

# Let's try this for a diamond Silicon structure
lattice = Lattice.cubic(5.46873)
Si = Structure(
    lattice,
    ["Si", "Si", "Si", "Si", "Si", "Si", "Si", "Si"],
    [
        [0.00000, 0.00000, 0.50000],
        [0.75000, 0.75000, 0.75000],
        [0.00000, 0.50000, 0.00000],
        [0.75000, 0.25000, 0.25000],
        [0.50000, 0.00000, 0.00000],
        [0.25000, 0.75000, 0.25000],
        [0.50000, 0.50000, 0.50000],
        [0.25000, 0.25000, 0.75000],
    ],
)

slabgen = SlabGenerator(Si, (1, 1, 1), 10, 10)
print(
    "Notice now there are actually now %s terminations that can be \
generated in the (111) direction for diamond Si"
    % (len(slabgen.get_slabs()))
)

# The simplest way to do this is to just use generate_all_slabs which finds all the unique
# Miller indices for a structure and uses SlabGenerator to create all terminations for all of them.
all_slabs = generate_all_slabs(Si, 3, 10, 10)
print(
    "%s unique slab structures have been found for a max Miller index of 3"
    % (len(all_slabs))
)

# ---

# What are the Miller indices of these slabs?
for slab in all_slabs:
    print(slab.miller_index)
print(
    "Notice some Miller indices are repeated. Again, this is due to there being more than one termination"
)

# ---

# Now let's assume that we then calculated the surface energies for these slabs

# Surface energy values in J/m^2
surface_energies_Ni = {
    (3, 2, 0): 2.3869,
    (1, 1, 0): 2.2862,
    (3, 1, 0): 2.3964,
    (2, 1, 0): 2.3969,
    (3, 3, 2): 2.0944,
    (1, 0, 0): 2.2084,
    (2, 1, 1): 2.2353,
    (3, 2, 2): 2.1242,
    (3, 2, 1): 2.3183,
    (2, 2, 1): 2.1732,
    (3, 3, 1): 2.2288,
    (3, 1, 1): 2.3039,
    (1, 1, 1): 1.9235,
}
miller_list = surface_energies_Ni.keys()
e_surf_list = surface_energies_Ni.values()

# We can now construct a Wulff shape with an accuracy up to a max Miller index of 3
wulffshape = WulffShape(Ni.lattice, miller_list, e_surf_list)

# Let's get some useful information from our wulffshape object
print(
    "shape factor: %.3f, anisotropy: \
%.3f, weighted surface energy: %.3f J/m^2"
    % (
        wulffshape.shape_factor,
        wulffshape.anisotropy,
        wulffshape.weighted_surface_energy,
    )
)


# If we want to see what our Wulff shape looks like
wulffshape.get_plot()

# ---

# Lets try something a little more complicated, say LiFePO4
from pymatgen.util.testing import PymatgenTest

# Get the LiFePO4 structure
LiFePO4 = PymatgenTest.get_structure("LiFePO4")

# Let's add some oxidation states to LiFePO4, this will be
# important when we want to take surface polarity into consideration
LiFePO4.add_oxidation_state_by_element({"Fe": 2, "Li": 1, "P": 5, "O": -2})
slabgen = SlabGenerator(LiFePO4, (0, 0, 1), 10, 10)

# ---

all_slabs = slabgen.get_slabs(bonds={("P", "O"): 2})
# any bond between P and O less than 2 Angstroms cannot be broken when generating slabs
print("For the (001) slab of LiFePO4, there are %s terminations." % (len(all_slabs)))

# ---

for slab in all_slabs:
    print(slab.is_polar(), slab.is_symmetric())
# Notice that none of the terminations in the (001) direction do not simultaneously satisfy
# our two criteria so a (001) surface with a reasonable surface energy cannot be calculated.
# In such cases, we need to modify the surfaces of our slabs. A future release of surface.py
# will implement such modification techniques for these cases.

# ---

# Now let's generate all possible slabs for a max Miller index of 2 for LiFePO4 and see if
# any of these surfaces can be calculated to yield reasonable and accurate surface energy
# values. This may take a while.
all_slabs = generate_all_slabs(LiFePO4, 2, 10, 10, bonds={("P", "O"): 2})

# ---

print(
    "There is a total of %s slabs generated including polar, asymmetric, and \
P-O terminated slabs"
    % (len(all_slabs))
)

# store any slabs for calculation that satisfies our criterias
valid_slabs = []
for slab in all_slabs:
    if not slab.is_polar() and slab.is_symmetric():
        print(slab.miller_index)
        valid_slabs.append(slab)

print(
    "Number of slabs that are nonpolar, symmetric and do not terminate P-O bonds: %s"
    % (len(valid_slabs))
)
