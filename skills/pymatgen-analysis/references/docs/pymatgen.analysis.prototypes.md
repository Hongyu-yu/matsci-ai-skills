<div class="wy-grid-for-nav">

<div class="wy-side-scroll">

<div class="wy-side-nav-search"
style="background: linear-gradient(0deg, rgba(23,63,162,1) 0%, rgba(0,70,192,1) 100%)">

[](index.html)

<div role="search">

</div>

</div>

<div class="wy-menu wy-menu-vertical" spy="affix" role="navigation"
aria-label="Navigation menu">

<div class="local-toc">

- <a href="#" class="reference internal">pymatgen.analysis.prototypes
  package</a>
  - <a href="#pymatgen.analysis.prototypes.AflowPrototypeMatcher"
    class="reference internal"><span class="pre"><code
    class="docutils literal notranslate">AflowPrototypeMatcher</code></span></a>
    - <a
      href="#pymatgen.analysis.prototypes.AflowPrototypeMatcher.get_prototypes"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">AflowPrototypeMatcher.get_prototypes()</code></span></a>
  - <a href="#pymatgen.analysis.prototypes.canonicalize_element_wyckoffs"
    class="reference internal"><span class="pre"><code
    class="docutils literal notranslate">canonicalize_element_wyckoffs()</code></span></a>
  - <a href="#pymatgen.analysis.prototypes.count_crystal_dof"
    class="reference internal"><span class="pre"><code
    class="docutils literal notranslate">count_crystal_dof()</code></span></a>
  - <a href="#pymatgen.analysis.prototypes.count_crystal_sites"
    class="reference internal"><span class="pre"><code
    class="docutils literal notranslate">count_crystal_sites()</code></span></a>
  - <a href="#pymatgen.analysis.prototypes.count_distinct_wyckoff_letters"
    class="reference internal"><span class="pre"><code
    class="docutils literal notranslate">count_distinct_wyckoff_letters()</code></span></a>
  - <a href="#pymatgen.analysis.prototypes.count_values_for_wyckoff"
    class="reference internal"><span class="pre"><code
    class="docutils literal notranslate">count_values_for_wyckoff()</code></span></a>
  - <a href="#pymatgen.analysis.prototypes.count_wyckoff_positions"
    class="reference internal"><span class="pre"><code
    class="docutils literal notranslate">count_wyckoff_positions()</code></span></a>
  - <a
    href="#pymatgen.analysis.prototypes.get_anonymous_formula_from_prototype_formula"
    class="reference internal"><span class="pre"><code
    class="docutils literal notranslate">get_anonymous_formula_from_prototype_formula()</code></span></a>
  - <a
    href="#pymatgen.analysis.prototypes.get_formula_from_protostructure_label"
    class="reference internal"><span class="pre"><code
    class="docutils literal notranslate">get_formula_from_protostructure_label()</code></span></a>
  - <a href="#pymatgen.analysis.prototypes.get_protostructure_label"
    class="reference internal"><span class="pre"><code
    class="docutils literal notranslate">get_protostructure_label()</code></span></a>
  - <a
    href="#pymatgen.analysis.prototypes.get_protostructure_label_from_aflow"
    class="reference internal"><span class="pre"><code
    class="docutils literal notranslate">get_protostructure_label_from_aflow()</code></span></a>
  - <a
    href="#pymatgen.analysis.prototypes.get_protostructure_label_from_moyopy"
    class="reference internal"><span class="pre"><code
    class="docutils literal notranslate">get_protostructure_label_from_moyopy()</code></span></a>
  - <a
    href="#pymatgen.analysis.prototypes.get_protostructure_label_from_spg_analyzer"
    class="reference internal"><span class="pre"><code
    class="docutils literal notranslate">get_protostructure_label_from_spg_analyzer()</code></span></a>
  - <a
    href="#pymatgen.analysis.prototypes.get_protostructure_label_from_spglib"
    class="reference internal"><span class="pre"><code
    class="docutils literal notranslate">get_protostructure_label_from_spglib()</code></span></a>
  - <a
    href="#pymatgen.analysis.prototypes.get_protostructures_from_aflow_label_and_composition"
    class="reference internal"><span class="pre"><code
    class="docutils literal notranslate">get_protostructures_from_aflow_label_and_composition()</code></span></a>
  - <a
    href="#pymatgen.analysis.prototypes.get_prototype_formula_from_composition"
    class="reference internal"><span class="pre"><code
    class="docutils literal notranslate">get_prototype_formula_from_composition()</code></span></a>
  - <a
    href="#pymatgen.analysis.prototypes.get_prototype_from_protostructure"
    class="reference internal"><span class="pre"><code
    class="docutils literal notranslate">get_prototype_from_protostructure()</code></span></a>
  - <a
    href="#pymatgen.analysis.prototypes.get_random_structure_for_protostructure"
    class="reference internal"><span class="pre"><code
    class="docutils literal notranslate">get_random_structure_for_protostructure()</code></span></a>
  - <a href="#pymatgen.analysis.prototypes.sort_and_score_element_wyckoffs"
    class="reference internal"><span class="pre"><code
    class="docutils literal notranslate">sort_and_score_element_wyckoffs()</code></span></a>
  - <a href="#pymatgen.analysis.prototypes.split_alpha_numeric"
    class="reference internal"><span class="pre"><code
    class="docutils literal notranslate">split_alpha_numeric()</code></span></a>

</div>

</div>

</div>

<div class="section wy-nav-content-wrap" toggle="wy-nav-shift">

[pymatgen](index.html)

<div class="wy-nav-content">

<div class="rst-content style-external-links">

<div role="navigation" aria-label="Page navigation">

- <a href="index.html" class="icon icon-home" aria-label="Home"></a>
- pymatgen.analysis.prototypes package
- <a
  href="https://github.com/materialsproject/pymatgen/blob/master/docs_rst/pymatgen.analysis.prototypes.rst"
  class="fa fa-github">Edit on GitHub</a>

------------------------------------------------------------------------

</div>

<div class="document" role="main" itemscope="itemscope"
itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="module-pymatgen.analysis.prototypes" class="section">

<span id="pymatgen-analysis-prototypes-package"></span>

# pymatgen.analysis.prototypes package<a href="#module-pymatgen.analysis.prototypes" class="headerlink"
title="Link to this heading"></a>

This module is intended to match crystal structures against known
crystallographic “prototype” structures.

In this module, the AflowPrototypeMatcher uses the AFLOW LIBRARY OF
CRYSTALLOGRAPHIC PROTOTYPES. If using this particular class, please cite
their publication appropriately:

Mehl, M. J., Hicks, D., Toher, C., Levy, O., Hanson, R. M., Hart, G., &
Curtarolo, S. (2017). The AFLOW library of crystallographic prototypes:
part 1. Computational Materials Science, 136, S1-S828.
<a href="https://doi.org/10.1016/j.commatsci.2017.01.017"
class="reference external">https://doi.org/10.1016/j.commatsci.2017.01.017</a>

The module also contains functions for getting the protostructure labels
from a variety of symmetry detection libraries (spglib, moyopy,
aflow-sym). The protostructure label is defined as the canonicalized
aflow label with the alphabetically sorted chemical system appended -
aflow_sym_label:chemsys.

The utilities for determining the protostructure label are upstreamed
from the aviary package (<a href="https://github.com/CompRhys/aviary"
class="reference external">https://github.com/CompRhys/aviary</a>). If
using these functions, please cite the following publications:

Goodall, R. E., Parackal, A. S., Faber, F. A., Armiento, R., & Lee, A.
A. (2022). Rapid discovery of stable materials by coordinate-free coarse
graining. Science advances, 8(30), eabn4117.
<a href="https://doi.org/10.1126/sciadv.abn4117"
class="reference external">https://doi.org/10.1126/sciadv.abn4117</a>

Parackal, A. S., Goodall, R. E., Faber, F. A., & Armiento, R. (2024).
Identifying crystal structures beyond known prototypes from x-ray powder
diffraction spectra. Physical Review Materials, 8(10), 103801.
<a href="https://doi.org/10.1103/PhysRevMaterials.8.103801"
class="reference external">https://doi.org/10.1103/PhysRevMaterials.8.103801</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">AflowPrototypeMatcher</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">initial_ltol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.2</span></span>*, *<span class="n"><span class="pre">initial_stol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.3</span></span>*, *<span class="n"><span class="pre">initial_angle_tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">5</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/prototypes/__init__.py#L116-L218"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.prototypes.AflowPrototypeMatcher"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

This class will match structures to their crystal prototypes, and will
attempt to group species together to match structures derived from
prototypes (e.g. an A_xB_1-x_C from a binary prototype), and will give
these the names the “-like” suffix.

This class uses data from the AFLOW LIBRARY OF CRYSTALLOGRAPHIC
PROTOTYPES. If using this class, please cite their publication
appropriately:

Mehl, M. J., Hicks, D., Toher, C., Levy, O., Hanson, R. M., Hart, G., &
Curtarolo, S. (2017). The AFLOW library of crystallographic prototypes:
part 1. Computational Materials Science, 136, S1-S828.
<a href="https://doi.org/10.1016/j.commatsci.2017.01.017"
class="reference external">https://doi.org/10.1016/j.commatsci.2017.01.017</a>

Tolerances as defined in StructureMatcher. Tolerances will be gradually
decreased until only a single match is found (if possible).

Parameters<span class="colon">:</span>  
- **initial_ltol** (*float*) – fractional length tolerance.

- **initial_stol** (*float*) – site tolerance.

- **initial_angle_tol** (*float*) – angle tolerance.

<span class="sig-name descname"><span class="pre">get_prototypes</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/prototypes/__init__.py#L199-L218"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.prototypes.AflowPrototypeMatcher.get_prototypes"
class="headerlink" title="Link to this definition"></a>  
Get prototype(s) structures for a given input structure. If you use this
method in your work, please cite the appropriate AFLOW publication:

> <div>
>
> Mehl, M. J., Hicks, D., Toher, C., Levy, O., Hanson, R. M., Hart, G.,
> & Curtarolo, S. (2017). The AFLOW library of crystallographic
> prototypes: part 1. Computational Materials Science, 136, S1-S828.
> <a href="https://doi.org/10.1016/j.commatsci.2017.01.017"
> class="reference external">https://doi.org/10.1016/j.commatsci.2017.01.017</a>
>
> </div>

Parameters<span class="colon">:</span>  
**structure**
(<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
structure to match

Returns<span class="colon">:</span>  
A list of dicts with keys “snl” for the matched prototype and  
”tags”, a dict of tags (“mineral”, “strukturbericht” and “aflow”) of
that prototype. This should be a list containing just a single entry,
but it is possible a material can match multiple prototypes.

Return type<span class="colon">:</span>  
list\[dict\] \| None

<!-- -->

<span class="sig-name descname"><span class="pre">canonicalize_element_wyckoffs</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">element_wyckoffs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">spg_num</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/prototypes/__init__.py#L571-L591"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.prototypes.canonicalize_element_wyckoffs"
class="headerlink" title="Link to this definition"></a>  
Given an element ordering, canonicalize the associated Wyckoff positions
based on the alphabetical weight of equivalent choices of origin.

Parameters<span class="colon">:</span>  
- **element_wyckoffs** (*str*) – wyckoff substring section from
  aflow_label with the wyckoff letters for different elements separated
  by underscores.

- **spg_num** (*int* *\|* *str*) – International space group number.

Returns<span class="colon">:</span>  
element_wyckoff string with canonical ordering of the wyckoff letters.

Return type<span class="colon">:</span>  
str

<!-- -->

<span class="sig-name descname"><span class="pre">count_crystal_dof</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">protostructure_label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">int</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/prototypes/__init__.py#L719-L738"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.prototypes.count_crystal_dof"
class="headerlink" title="Link to this definition"></a>  
Count number of free parameters in coarse-grained protostructure_label
representation: how many degrees of freedom would remain to optimize
during a crystal structure relaxation.

Parameters<span class="colon">:</span>  
**protostructure_label** (*str*) – label constructed as
aflow_label:chemsys where aflow_label is an AFLOW-style prototype label
chemsys is the alphabetically sorted chemical system.

Returns<span class="colon">:</span>  
Number of free-parameters in given prototype

Return type<span class="colon">:</span>  
int

<!-- -->

<span class="sig-name descname"><span class="pre">count_crystal_sites</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">protostructure_label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">int</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/prototypes/__init__.py#L741-L755"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.prototypes.count_crystal_sites"
class="headerlink" title="Link to this definition"></a>  
Count number of sites from protostructure_label.

Parameters<span class="colon">:</span>  
**protostructure_label** (*str*) – label constructed as
aflow_label:chemsys where aflow_label is an AFLOW-style prototype label
chemsys is the alphabetically sorted chemical system.

Returns<span class="colon">:</span>  
Number of free-parameters in given prototype

Return type<span class="colon">:</span>  
int

<!-- -->

<span class="sig-name descname"><span class="pre">count_distinct_wyckoff_letters</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">protostructure_label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">int</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/prototypes/__init__.py#L680-L694"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.prototypes.count_distinct_wyckoff_letters"
class="headerlink" title="Link to this definition"></a>  
Count number of distinct Wyckoff letters in protostructure_label.

Parameters<span class="colon">:</span>  
**protostructure_label** (*str*) – label constructed as
aflow_label:chemsys where aflow_label is an AFLOW-style prototype label
chemsys is the alphabetically sorted chemical system.

Returns<span class="colon">:</span>  
number of distinct Wyckoff letters in protostructure_label

Return type<span class="colon">:</span>  
int

<!-- -->

<span class="sig-name descname"><span class="pre">count_values_for_wyckoff</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">element_wyckoffs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">counts</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">spg_num</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">lookup_dict</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/prototypes/__init__.py#L238-L248"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.prototypes.count_values_for_wyckoff"
class="headerlink" title="Link to this definition"></a>  
Count values from a lookup table and scale by wyckoff multiplicities.

<!-- -->

<span class="sig-name descname"><span class="pre">count_wyckoff_positions</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">protostructure_label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">int</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/prototypes/__init__.py#L697-L716"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.prototypes.count_wyckoff_positions"
class="headerlink" title="Link to this definition"></a>  
Count number of Wyckoff positions in protostructure_label.

Parameters<span class="colon">:</span>  
**protostructure_label** (*str*) – label constructed as
aflow_label:chemsys where aflow_label is an AFLOW-style prototype label
chemsys is the alphabetically sorted chemical system.

Returns<span class="colon">:</span>  
number of distinct Wyckoff positions in protostructure_label

Return type<span class="colon">:</span>  
int

<!-- -->

<span class="sig-name descname"><span class="pre">get_anonymous_formula_from_prototype_formula</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">prototype_formula</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/prototypes/__init__.py#L656-L664"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.prototypes.get_anonymous_formula_from_prototype_formula"
class="headerlink" title="Link to this definition"></a>  
Get an anonymous formula from a prototype formula.

<!-- -->

<span class="sig-name descname"><span class="pre">get_formula_from_protostructure_label</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">protostructure_label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/prototypes/__init__.py#L667-L677"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.prototypes.get_formula_from_protostructure_label"
class="headerlink" title="Link to this definition"></a>  
Get a formula from a protostructure label.

<!-- -->

<span class="sig-name descname"><span class="pre">get_protostructure_label</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">struct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">method</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'aflow'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'spglib'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'moyopy'</span></span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">raise_errors</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/prototypes/__init__.py#L251-L282"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.prototypes.get_protostructure_label"
class="headerlink" title="Link to this definition"></a>  
Get protostructure label for a pymatgen Structure.

Parameters<span class="colon">:</span>  
- **struct**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  pymatgen Structure

- **method** (*Literal\["aflow",* *"spglib",* *"moyopy"\]*) – Method to
  use for symmetry

- **detection**

- **raise_errors** (*bool*) – Whether to raise errors or annotate them.
  Defaults to False.

- **\*\*kwargs** – Additional arguments for the specific method

Returns<span class="colon">:</span>  
protostructure_label which is constructed as aflow_label:chemsys or  
explanation of failure if symmetry detection failed and raise_errors is
False.

Return type<span class="colon">:</span>  
str

<!-- -->

<span class="sig-name descname"><span class="pre">get_protostructure_label_from_aflow</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">struct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">raise_errors</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">aflow_executable</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/prototypes/__init__.py#L285-L364"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.prototypes.get_protostructure_label_from_aflow"
class="headerlink" title="Link to this definition"></a>  
Get protostructure label for a pymatgen Structure. Make sure you’re
running a recent version of the aflow CLI as there’s been several
breaking changes. This code was tested under v3.2.12. The protostructure
label is constructed as aflow_label:chemsys.

Install guide: <a href="https://aflow.org/install-aflow/#install_aflow"
class="reference external">https://aflow.org/install-aflow/#install_aflow</a>  
<a href="http://aflow.org/install-aflow/install-aflow.sh"
class="reference external">http://aflow.org/install-aflow/install-aflow.sh</a>
-o install-aflow.sh chmod 555 install-aflow.sh ./install-aflow.sh –slim

Parameters<span class="colon">:</span>  
- **struct**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  pymatgen Structure

- **aflow_executable** (*str*) – path to aflow executable. Defaults to
  which(“aflow”).

- **raise_errors** (*bool*) – Whether to raise errors or annotate them.
  Defaults to False.

Returns<span class="colon">:</span>  
protostructure_label which is constructed as aflow_label:chemsys or  
explanation of failure if symmetry detection failed and raise_errors is
False.

Return type<span class="colon">:</span>  
str

<!-- -->

<span class="sig-name descname"><span class="pre">get_protostructure_label_from_moyopy</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">struct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">raise_errors</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">symprec</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.1</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/prototypes/__init__.py#L505-L568"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.prototypes.get_protostructure_label_from_moyopy"
class="headerlink" title="Link to this definition"></a>  
Get AFLOW prototype label using Moyopy for symmetry detection.

Parameters<span class="colon">:</span>  
- **struct**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  pymatgen Structure object.

- **raise_errors** (*bool*) – Whether to raise errors or annotate them.
  Defaults to False.

- **symprec** (*float*) – Initial symmetry precision for Moyopy.
  Defaults to 0.1.

Returns<span class="colon">:</span>  
protostructure_label which is constructed as aflow_label:chemsys or  
explanation of failure if symmetry detection failed and raise_errors is
False.

Return type<span class="colon">:</span>  
str

<!-- -->

<span class="sig-name descname"><span class="pre">get_protostructure_label_from_spg_analyzer</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">spg_analyzer</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a
href="pymatgen.symmetry.html#pymatgen.symmetry.analyzer.SpacegroupAnalyzer"
class="reference internal"
title="pymatgen.symmetry.analyzer.SpacegroupAnalyzer"><span
class="pre">SpacegroupAnalyzer</span></a></span>*, *<span class="n"><span class="pre">raise_errors</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/prototypes/__init__.py#L406-L451"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.prototypes.get_protostructure_label_from_spg_analyzer"
class="headerlink" title="Link to this definition"></a>  
Get protostructure label for pymatgen SpacegroupAnalyzer.

Parameters<span class="colon">:</span>  
- **spg_analyzer** (<a
  href="pymatgen.symmetry.html#pymatgen.symmetry.analyzer.SpacegroupAnalyzer"
  class="reference internal"
  title="pymatgen.symmetry.analyzer.SpacegroupAnalyzer"><em>SpacegroupAnalyzer</em></a>)
  – pymatgen SpacegroupAnalyzer object.

- **raise_errors** (*bool*) – Whether to raise errors or annotate them.
  Defaults to False.

Returns<span class="colon">:</span>  
protostructure_label which is constructed as aflow_label:chemsys or  
explanation of failure if symmetry detection failed and raise_errors is
False.

Return type<span class="colon">:</span>  
str

<!-- -->

<span class="sig-name descname"><span class="pre">get_protostructure_label_from_spglib</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">struct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">raise_errors</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">init_symprec</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.1</span></span>*, *<span class="n"><span class="pre">fallback_symprec</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-05</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/prototypes/__init__.py#L454-L502"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.prototypes.get_protostructure_label_from_spglib"
class="headerlink" title="Link to this definition"></a>  
Get AFLOW prototype label for pymatgen Structure.

Parameters<span class="colon">:</span>  
- **struct**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  pymatgen Structure object.

- **raise_errors** (*bool*) – Whether to raise errors or annotate them.
  Defaults to False.

- **init_symprec** (*float*) – Initial symmetry precision for spglib.
  Defaults to 0.1.

- **fallback_symprec** (*float*) – Fallback symmetry precision for
  spglib if first symmetry detection failed. Defaults to 1e-5.

Returns<span class="colon">:</span>  
protostructure_label which is constructed as aflow_label:chemsys or  
explanation of failure if symmetry detection failed and raise_errors is
False.

Return type<span class="colon">:</span>  
str

<!-- -->

<span class="sig-name descname"><span class="pre">get_protostructures_from_aflow_label_and_composition</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">aflow_label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">composition</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.composition.Composition"
class="reference internal"
title="pymatgen.core.composition.Composition"><span
class="pre">Composition</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/prototypes/__init__.py#L882-L913"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.prototypes.get_protostructures_from_aflow_label_and_composition"
class="headerlink" title="Link to this definition"></a>  
Get a canonicalized string for the prototype.

Parameters<span class="colon">:</span>  
- **aflow_label** (*str*) – AFLOW-style prototype label

- **composition**
  (<a href="pymatgen.core.html#pymatgen.core.composition.Composition"
  class="reference internal"
  title="pymatgen.core.composition.Composition"><em>Composition</em></a>)
  – pymatgen Composition object

Returns<span class="colon">:</span>  
List of possible protostructure labels that can be generated  
from combinations of the input aflow_label and composition.

Return type<span class="colon">:</span>  
list\[str\]

<!-- -->

<span class="sig-name descname"><span class="pre">get_prototype_formula_from_composition</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">composition</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.composition.Composition"
class="reference internal"
title="pymatgen.core.composition.Composition"><span
class="pre">Composition</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/prototypes/__init__.py#L626-L653"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.prototypes.get_prototype_formula_from_composition"
class="headerlink" title="Link to this definition"></a>  
An anonymized formula. Unique species are arranged in alphabetical order
and assigned ascending alphabets. This format is used in the aflow
structure prototype labelling scheme.

Parameters<span class="colon">:</span>  
**composition**
(<a href="pymatgen.core.html#pymatgen.core.composition.Composition"
class="reference internal"
title="pymatgen.core.composition.Composition"><em>Composition</em></a>)
– Pymatgen Composition to process

Returns<span class="colon">:</span>  
anonymized formula where the species are in alphabetical order

Return type<span class="colon">:</span>  
str

<!-- -->

<span class="sig-name descname"><span class="pre">get_prototype_from_protostructure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">protostructure_label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/prototypes/__init__.py#L775-L829"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.prototypes.get_prototype_from_protostructure"
class="headerlink" title="Link to this definition"></a>  
Get a canonicalized string for the prototype. This prototype should be
the same for all isopointal protostructures.

Parameters<span class="colon">:</span>  
**protostructure_label** (*str*) – label constructed as
aflow_label:chemsys where aflow_label is an AFLOW-style prototype label
chemsys is the alphabetically sorted chemical system.

Returns<span class="colon">:</span>  
Canonicalized AFLOW-style prototype label

Return type<span class="colon">:</span>  
str

<!-- -->

<span class="sig-name descname"><span class="pre">get_random_structure_for_protostructure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">protostructure_label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/prototypes/__init__.py#L916-L962"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.prototypes.get_random_structure_for_protostructure"
class="headerlink" title="Link to this definition"></a>  
Generate a random structure for a given prototype structure.

NOTE that due to the random nature of the generation, the output
structure may be higher symmetry than the requested prototype structure.

Parameters<span class="colon">:</span>  
- **protostructure_label** (*str*) – label constructed as
  aflow_label:chemsys where aflow_label is an AFLOW-style prototype
  label chemsys is the alphabetically sorted chemical system.

- **\*\*kwargs** – Keyword arguments to pass to pyxtal().from_random()

<!-- -->

<span class="sig-name descname"><span class="pre">sort_and_score_element_wyckoffs</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">element_wyckoffs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/prototypes/__init__.py#L594-L623"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.prototypes.sort_and_score_element_wyckoffs"
class="headerlink" title="Link to this definition"></a>  
Determines the order or Wyckoff positions when canonicalizing AFLOW
labels.

Parameters<span class="colon">:</span>  
**element_wyckoffs** (*str*) – wyckoff substring section from
aflow_label with the wyckoff letters for different elements separated by
underscores.

Returns<span class="colon">:</span>  
containing - str: sorted Wyckoff position substring for AFLOW-style
prototype label - int: integer score to rank order when canonicalizing

Return type<span class="colon">:</span>  
tuple

<!-- -->

<span class="sig-name descname"><span class="pre">split_alpha_numeric</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">s</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/prototypes/__init__.py#L221-L235"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.prototypes.split_alpha_numeric"
class="headerlink" title="Link to this definition"></a>  
Split a string into separate lists of alpha and numeric groups.

Parameters<span class="colon">:</span>  
**s** (*str*) – The input string to split.

Returns<span class="colon">:</span>  
A dictionary with keys ‘alpha’ and ‘numeric’,  
each containing a list of the respective groups.

Return type<span class="colon">:</span>  
dict\[str, list\[str\]\]

</div>

</div>

</div>

------------------------------------------------------------------------

<div role="contentinfo">

© Copyright 2011, Pymatgen Development Team.

</div>

Built with [Sphinx](https://www.sphinx-doc.org/) using a
[theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by
[Read the Docs](https://readthedocs.org).

</div>

</div>

</div>

</div>
