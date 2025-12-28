# Extracted from notebook: 2018-01-01-ChemEnv - How to automatically identify coordination environments in a structure.ipynb
# Source: pymatgen examples (matgenb)

# Uncomment the subsequent lines in this cell to install dependencies for Google Colab.
# !pip install pymatgen==2022.7.19
from __future__ import annotations

# ---

import logging

from pymatgen.analysis.chemenv.coordination_environments.chemenv_strategies import (
    SimplestChemenvStrategy,
)
from pymatgen.analysis.chemenv.coordination_environments.coordination_geometry_finder import (
    LocalGeometryFinder,
)
from pymatgen.analysis.chemenv.coordination_environments.structure_environments import (
    LightStructureEnvironments,
)
from pymatgen.ext.matproj import MPRester

# ---

# Get a structure from the materials project (alpha-quartz)
mpr = MPRester()
struct = mpr.get_structure_by_material_id("mp-7000")

# ---

# just remove the comment
# from pymatgen.core.structure import Structure
# struct = Structure.from_file("mystructure.cif")

# ---

# Setup the local geometry finder
lgf = LocalGeometryFinder()

# you can also save the logging to a file, just remove the comment
logging.basicConfig(  # filename='chemenv_structure_environments.log',
    format="%(levelname)s:%(module)s:%(funcName)s:%(message)s", level=logging.DEBUG
)
lgf.setup_structure(structure=struct)

# ---

# Get the StructureEnvironments
se = lgf.compute_structure_environments(
    maximum_distance_factor=1.41, only_cations=False
)

# ---

strategy = SimplestChemenvStrategy(distance_cutoff=1.4, angle_cutoff=0.3)
lse = LightStructureEnvironments.from_structure_environments(
    strategy=strategy, structure_environments=se
)

# ---

# print coordination environments for a special site
isite = 5
print(lse.coordination_environments[isite])

# ---

# Get the strategy from D. Waroquiers et al., Chem Mater., 2017, 29, 8346.
from pymatgen.analysis.chemenv.coordination_environments.chemenv_strategies import (
    MultiWeightsChemenvStrategy,
)

strategy = MultiWeightsChemenvStrategy.stats_article_weights_parameters()

lse = LightStructureEnvironments.from_structure_environments(
    strategy=strategy, structure_environments=se
)

# ---

# print coordination environments for a special site
isite = 5
print(lse.coordination_environments[isite])

# ---

# another site where you have only one coordination environment (tetrahedron, T:4)
isite = 1
print(lse.coordination_environments[isite])
