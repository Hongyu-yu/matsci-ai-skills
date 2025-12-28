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

- <a href="#" class="reference internal">pymatgen.analysis.magnetism
  package</a>
  - <a href="#submodules" class="reference internal">Submodules</a>
  - <a href="#module-pymatgen.analysis.magnetism.analyzer"
    class="reference internal">pymatgen.analysis.magnetism.analyzer
    module</a>
    - <a
      href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">CollinearMagneticStructureAnalyzer</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer.get_exchange_group_info"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CollinearMagneticStructureAnalyzer.get_exchange_group_info()</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer.get_ferromagnetic_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CollinearMagneticStructureAnalyzer.get_ferromagnetic_structure()</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer.get_nonmagnetic_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CollinearMagneticStructureAnalyzer.get_nonmagnetic_structure()</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer.get_structure_with_only_magnetic_atoms"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CollinearMagneticStructureAnalyzer.get_structure_with_only_magnetic_atoms()</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer.get_structure_with_spin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CollinearMagneticStructureAnalyzer.get_structure_with_spin()</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer.is_magnetic"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CollinearMagneticStructureAnalyzer.is_magnetic</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer.magmoms"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CollinearMagneticStructureAnalyzer.magmoms</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer.magnetic_species_and_magmoms"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CollinearMagneticStructureAnalyzer.magnetic_species_and_magmoms</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer.matches_ordering"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CollinearMagneticStructureAnalyzer.matches_ordering()</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer.number_of_magnetic_sites"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CollinearMagneticStructureAnalyzer.number_of_magnetic_sites</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer.number_of_unique_magnetic_sites"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CollinearMagneticStructureAnalyzer.number_of_unique_magnetic_sites()</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer.ordering"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CollinearMagneticStructureAnalyzer.ordering</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer.types_of_magnetic_specie"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CollinearMagneticStructureAnalyzer.types_of_magnetic_specie</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer.types_of_magnetic_species"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CollinearMagneticStructureAnalyzer.types_of_magnetic_species</code></span></a>
    - <a href="#pymatgen.analysis.magnetism.analyzer.MagneticDeformation"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">MagneticDeformation</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.analyzer.MagneticDeformation.deformation"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MagneticDeformation.deformation</code></span></a>
      - <a href="#pymatgen.analysis.magnetism.analyzer.MagneticDeformation.type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MagneticDeformation.type</code></span></a>
    - <a
      href="#pymatgen.analysis.magnetism.analyzer.MagneticStructureEnumerator"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">MagneticStructureEnumerator</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.analyzer.MagneticStructureEnumerator.available_strategies"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MagneticStructureEnumerator.available_strategies</code></span></a>
    - <a href="#pymatgen.analysis.magnetism.analyzer.Ordering"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Ordering</code></span></a>
      - <a href="#pymatgen.analysis.magnetism.analyzer.Ordering.AFM"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Ordering.AFM</code></span></a>
      - <a href="#pymatgen.analysis.magnetism.analyzer.Ordering.FM"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Ordering.FM</code></span></a>
      - <a href="#pymatgen.analysis.magnetism.analyzer.Ordering.FiM"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Ordering.FiM</code></span></a>
      - <a href="#pymatgen.analysis.magnetism.analyzer.Ordering.NM"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Ordering.NM</code></span></a>
      - <a href="#pymatgen.analysis.magnetism.analyzer.Ordering.Unknown"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Ordering.Unknown</code></span></a>
    - <a href="#pymatgen.analysis.magnetism.analyzer.OverwriteMagmomMode"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">OverwriteMagmomMode</code></span></a>
      - <a href="#pymatgen.analysis.magnetism.analyzer.OverwriteMagmomMode.none"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">OverwriteMagmomMode.none</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.analyzer.OverwriteMagmomMode.normalize"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">OverwriteMagmomMode.normalize</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.analyzer.OverwriteMagmomMode.replace_all"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">OverwriteMagmomMode.replace_all</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.analyzer.OverwriteMagmomMode.replace_all_if_undefined"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">OverwriteMagmomMode.replace_all_if_undefined</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.analyzer.OverwriteMagmomMode.respect_sign"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">OverwriteMagmomMode.respect_sign</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.analyzer.OverwriteMagmomMode.respect_zeros"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">OverwriteMagmomMode.respect_zeros</code></span></a>
    - <a href="#pymatgen.analysis.magnetism.analyzer.magnetic_deformation"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">magnetic_deformation()</code></span></a>
  - <a href="#module-pymatgen.analysis.magnetism.heisenberg"
    class="reference internal">pymatgen.analysis.magnetism.heisenberg
    module</a>
    - <a href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">HeisenbergMapper</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper.strategy"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">HeisenbergMapper.strategy</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper.sgraphs"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">HeisenbergMapper.sgraphs</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper.unique_site_ids"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">HeisenbergMapper.unique_site_ids</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper.wyckoff_ids"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">HeisenbergMapper.wyckoff_ids</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper.nn_interactions"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">HeisenbergMapper.nn_interactions</code></span></a>
      - <a href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper.dists"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">HeisenbergMapper.dists</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper.ex_mat"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">HeisenbergMapper.ex_mat</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper.ex_params"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">HeisenbergMapper.ex_params</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper.estimate_exchange"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">HeisenbergMapper.estimate_exchange()</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper.get_exchange"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">HeisenbergMapper.get_exchange()</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper.get_heisenberg_model"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">HeisenbergMapper.get_heisenberg_model()</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper.get_interaction_graph"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">HeisenbergMapper.get_interaction_graph()</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper.get_low_energy_orderings"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">HeisenbergMapper.get_low_energy_orderings()</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper.get_mft_temperature"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">HeisenbergMapper.get_mft_temperature()</code></span></a>
    - <a href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergModel"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">HeisenbergModel</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergModel.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">HeisenbergModel.as_dict()</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergModel.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">HeisenbergModel.from_dict()</code></span></a>
    - <a href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergScreener"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">HeisenbergScreener</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergScreener.screened_structures"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">HeisenbergScreener.screened_structures</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergScreener.screened_energies"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">HeisenbergScreener.screened_energies</code></span></a>
  - <a href="#module-pymatgen.analysis.magnetism.jahnteller"
    class="reference internal">pymatgen.analysis.magnetism.jahnteller
    module</a>
    - <a href="#pymatgen.analysis.magnetism.jahnteller.JahnTellerAnalyzer"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">JahnTellerAnalyzer</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.jahnteller.JahnTellerAnalyzer.get_analysis"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JahnTellerAnalyzer.get_analysis()</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.jahnteller.JahnTellerAnalyzer.get_analysis_and_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JahnTellerAnalyzer.get_analysis_and_structure()</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.jahnteller.JahnTellerAnalyzer.get_magnitude_of_effect_from_species"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JahnTellerAnalyzer.get_magnitude_of_effect_from_species()</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.jahnteller.JahnTellerAnalyzer.get_magnitude_of_effect_from_spin_config"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JahnTellerAnalyzer.get_magnitude_of_effect_from_spin_config()</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.jahnteller.JahnTellerAnalyzer.is_jahn_teller_active"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JahnTellerAnalyzer.is_jahn_teller_active()</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.jahnteller.JahnTellerAnalyzer.mu_so"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JahnTellerAnalyzer.mu_so()</code></span></a>
      - <a
        href="#pymatgen.analysis.magnetism.jahnteller.JahnTellerAnalyzer.tag_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JahnTellerAnalyzer.tag_structure()</code></span></a>

</div>

</div>

</div>

<div class="section wy-nav-content-wrap" toggle="wy-nav-shift">

[pymatgen](index.html)

<div class="wy-nav-content">

<div class="rst-content style-external-links">

<div role="navigation" aria-label="Page navigation">

- <a href="index.html" class="icon icon-home" aria-label="Home"></a>
- pymatgen.analysis.magnetism package
- <a
  href="https://github.com/materialsproject/pymatgen/blob/master/docs_rst/pymatgen.analysis.magnetism.rst"
  class="fa fa-github">Edit on GitHub</a>

------------------------------------------------------------------------

</div>

<div class="document" role="main" itemscope="itemscope"
itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="module-pymatgen.analysis.magnetism" class="section">

<span id="pymatgen-analysis-magnetism-package"></span>

# pymatgen.analysis.magnetism package<a href="#module-pymatgen.analysis.magnetism" class="headerlink"
title="Link to this heading"></a>

Package for analysis of magnetic structures.

<div id="submodules" class="section">

## Submodules<a href="#submodules" class="headerlink"
title="Link to this heading"></a>

</div>

<div id="module-pymatgen.analysis.magnetism.analyzer" class="section">

<span id="pymatgen-analysis-magnetism-analyzer-module"></span>

## pymatgen.analysis.magnetism.analyzer module<a href="#module-pymatgen.analysis.magnetism.analyzer"
class="headerlink" title="Link to this heading"></a>

This module provides some useful functions for dealing with magnetic
Structures (e.g. Structures with associated magmom tags).

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">CollinearMagneticStructureAnalyzer</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">overwrite_magmom_mode</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="#pymatgen.analysis.magnetism.analyzer.OverwriteMagmomMode"
class="reference internal"
title="pymatgen.analysis.magnetism.analyzer.OverwriteMagmomMode"><span
class="pre">OverwriteMagmomMode</span></a></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">OverwriteMagmomMode.none</span></span>*, *<span class="n"><span class="pre">round_magmoms</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">detect_valences</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">make_primitive</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">default_magmoms</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">set_net_positive</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">threshold</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">threshold_nonmag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.1</span></span>*, *<span class="n"><span class="pre">threshold_ordering</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-08</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/analyzer.py#L74-L595"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

A class which provides a few helpful methods to analyze collinear
magnetic structures.

If magnetic moments are not defined, moments will be taken either from
default_magmoms.yaml (similar to the default magmoms in MPRelaxSet, with
a few extra definitions) or from a specie:magmom dict provided by the
default_magmoms kwarg.

Input magmoms can be replaced using the ‘overwrite_magmom_mode’ kwarg.
This can be: \* “none” to do nothing, \* “respect_sign” which will
overwrite existing magmoms with

> <div>
>
> those from default_magmoms but will keep sites with positive magmoms
> positive, negative magmoms negative and zero magmoms zero,
>
> </div>

- “respect_zeros”, which will give a ferromagnetic structure (all
  positive magmoms from default_magmoms) but still keep sites with zero
  magmoms as zero,

- “replace_all” which will try to guess initial magmoms for all sites in
  the structure irrespective of input structure (this is most suitable
  for an initial DFT calculation),

- “replace_all_if_undefined” is the same as “replace_all” but only if no
  magmoms are defined in input structure, otherwise it will respect
  existing magmoms.

- “normalize” will normalize magmoms to unity, but will respect sign
  (used for comparing orderings), magmoms \< threshold will be set to
  zero

Parameters<span class="colon">:</span>  
- **structure** – input Structure object

- **overwrite_magmom_mode** – “respect_sign”, “respect_zeros”,
  “replace_all”, “replace_all_if_undefined”, “normalize” (default
  “none”)

- **round_magmoms** – will round input magmoms to specified number of
  decimal places if integer is supplied, if set to a float will try and
  group magmoms together using a kernel density estimator of provided
  width, and extracting peaks of the estimator detect_valences: if True,
  will attempt to assign valences to input structure

- **make_primitive** – if True, will transform to primitive magnetic
  cell

- **default_magmoms** – (optional) dict specifying default magmoms

- **set_net_positive** – if True, will change sign of magnetic moments
  such that the net magnetization is positive. Argument will be ignored
  if mode “respect_sign” is used.

- **threshold** – number (in Bohr magnetons) below which magmoms will be
  rounded to zero

- **threshold_nonmag** – number (in Bohr magneton) below which
  nonmagnetic ions (with no magmom specified in default_magmoms) will be
  rounded to zero

- **threshold_ordering** – number (absolute of sum of all magmoms, in
  Bohr magneton) below which total magnetization is treated as zero when
  defining magnetic ordering. Defaults to 1e-8.

<span class="sig-name descname"><span class="pre">get_exchange_group_info</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">symprec</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.01</span></span>*, *<span class="n"><span class="pre">angle_tolerance</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">5</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/analyzer.py#L540-L564"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer.get_exchange_group_info"
class="headerlink" title="Link to this definition"></a>  
Get the information on the symmetry of the Hamiltonian describing the
exchange energy of the system, taking into account relative direction of
magnetic moments but not their absolute direction.

This is not strictly accurate (e.g. some/many atoms will have zero
magnetic moments), but defining symmetry this way is a useful way of
keeping track of distinct magnetic orderings within pymatgen.

Parameters<span class="colon">:</span>  
- **symprec** (*float*) – same as SpacegroupAnalyzer (Default value =
  1e-2)

- **angle_tolerance** (*float*) – same as SpacegroupAnalyzer (Default
  value = 5)

Returns<span class="colon">:</span>  
spacegroup_symbol, international_number

Return type<span class="colon">:</span>  
tuple\[str, int\]

<span class="sig-name descname"><span class="pre">get_ferromagnetic_structure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">make_primitive</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/analyzer.py#L398-L416"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer.get_ferromagnetic_structure"
class="headerlink" title="Link to this definition"></a>  
Get a Structure with all magnetic moments positive or zero.

Parameters<span class="colon">:</span>  
**make_primitive** – Whether to make structure primitive after making
all magnetic moments positive (Default value = True)

Returns<span class="colon">:</span>  
Structure

<span class="sig-name descname"><span class="pre">get_nonmagnetic_structure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">make_primitive</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/analyzer.py#L380-L396"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer.get_nonmagnetic_structure"
class="headerlink" title="Link to this definition"></a>  
Get a Structure without magnetic moments defined.

Parameters<span class="colon">:</span>  
**make_primitive** – Whether to make structure primitive after removing
magnetic information (Default value = True)

Returns<span class="colon">:</span>  
Structure

<span class="sig-name descname"><span class="pre">get_structure_with_only_magnetic_atoms</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">make_primitive</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/analyzer.py#L358-L378"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer.get_structure_with_only_magnetic_atoms"
class="headerlink" title="Link to this definition"></a>  
Get a Structure with only magnetic atoms present.

Parameters<span class="colon">:</span>  
**make_primitive** – Whether to make structure primitive after removing
non-magnetic atoms (Default value = True)

Returns<span class="colon">:</span>  
Structure

<span class="sig-name descname"><span class="pre">get_structure_with_spin</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/analyzer.py#L348-L356"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer.get_structure_with_spin"
class="headerlink" title="Link to this definition"></a>  
Get a Structure with species decorated with spin values instead of using
magmom site properties.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">is_magnetic</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/analyzer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer.is_magnetic"
class="headerlink" title="Link to this definition"></a>  
True if any non-zero magmoms present.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">magmoms</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">NDArray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/analyzer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer.magmoms"
class="headerlink" title="Link to this definition"></a>  
magmoms as a NumPy array.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">magnetic_species_and_magmoms</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/analyzer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer.magnetic_species_and_magmoms"
class="headerlink" title="Link to this definition"></a>  
A dict of magnetic species and the magnitude of their associated
magmoms. Will return a list if there are multiple magmoms per species.

Returns<span class="colon">:</span>  
dict of magnetic species and magmoms

<span class="sig-name descname"><span class="pre">matches_ordering</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/analyzer.py#L566-L595"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer.matches_ordering"
class="headerlink" title="Link to this definition"></a>  
Compares the magnetic orderings of one structure with another.

Parameters<span class="colon">:</span>  
**other** – Structure to compare

Returns<span class="colon">:</span>  
True if magnetic orderings match, False otherwise

Return type<span class="colon">:</span>  
bool

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">number_of_magnetic_sites</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/analyzer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer.number_of_magnetic_sites"
class="headerlink" title="Link to this definition"></a>  
Number of magnetic sites present in structure.

<span class="sig-name descname"><span class="pre">number_of_unique_magnetic_sites</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">symprec</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.001</span></span>*, *<span class="n"><span class="pre">angle_tolerance</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">5</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">int</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/analyzer.py#L475-L500"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer.number_of_unique_magnetic_sites"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
- **symprec** (*float*) – same as in SpacegroupAnalyzer (Default value =
  1e-3)

- **angle_tolerance** (*float*) – same as in SpacegroupAnalyzer (Default
  value = 5).

Returns<span class="colon">:</span>  
Number of symmetrically-distinct magnetic sites present in structure.

Return type<span class="colon">:</span>  
int

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ordering</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="#pymatgen.analysis.magnetism.analyzer.Ordering"
class="reference internal"
title="pymatgen.analysis.magnetism.analyzer.Ordering"><span
class="pre">Ordering</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/analyzer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer.ordering"
class="headerlink" title="Link to this definition"></a>  
Apply heuristics to return a magnetic ordering for a collinear magnetic
structure. Result is not guaranteed to be correct, just a best guess.
Tolerance for minimum total magnetization to be considered
ferro/ferrimagnetic is self.threshold_ordering and defaults to 1e-8.

Returns<span class="colon">:</span>  
Enum with values FM: ferromagnetic, FiM: ferrimagnetic,  
AFM: antiferromagnetic, NM: non-magnetic or Unknown. Unknown is returned
if magnetic moments are not defined or structure is not collinear (in
which case a warning is issued).

Return type<span class="colon">:</span>  
<a href="#pymatgen.analysis.magnetism.analyzer.Ordering"
class="reference internal"
title="pymatgen.analysis.magnetism.analyzer.Ordering">Ordering</a>

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">types_of_magnetic_specie</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.periodic_table.Element"
class="reference internal"
title="pymatgen.core.periodic_table.Element"><span
class="pre">Element</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.periodic_table.Species"
class="reference internal"
title="pymatgen.core.periodic_table.Species"><span
class="pre">Species</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.periodic_table.DummySpecies"
class="reference internal"
title="pymatgen.core.periodic_table.DummySpecies"><span
class="pre">DummySpecies</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="p"><span class="pre">...</span></span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/analyzer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer.types_of_magnetic_specie"
class="headerlink" title="Link to this definition"></a>  
Specie-\>Species rename. Used to maintain backwards compatibility.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">types_of_magnetic_species</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.periodic_table.Element"
class="reference internal"
title="pymatgen.core.periodic_table.Element"><span
class="pre">Element</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.periodic_table.Species"
class="reference internal"
title="pymatgen.core.periodic_table.Species"><span
class="pre">Species</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.periodic_table.DummySpecies"
class="reference internal"
title="pymatgen.core.periodic_table.DummySpecies"><span
class="pre">DummySpecies</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="p"><span class="pre">...</span></span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/analyzer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.analyzer.CollinearMagneticStructureAnalyzer.types_of_magnetic_species"
class="headerlink" title="Link to this definition"></a>  
Equivalent to Structure.types_of_specie but only returns magnetic
species.

Returns<span class="colon">:</span>  
types of Species

Return type<span class="colon">:</span>  
tuple

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">MagneticDeformation</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">deformation</span></span>*, *<span class="n"><span class="pre">type</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/analyzer.py#L1070-L1072"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.magnetism.analyzer.MagneticDeformation"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`NamedTuple`</span>

Create new instance of MagneticDeformation(deformation, type)

<span class="sig-name descname"><span class="pre">deformation</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/analyzer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.analyzer.MagneticDeformation.deformation"
class="headerlink" title="Link to this definition"></a>  
Alias for field number 0

<span class="sig-name descname"><span class="pre">type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/analyzer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.magnetism.analyzer.MagneticDeformation.type"
class="headerlink" title="Link to this definition"></a>  
Alias for field number 1

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">MagneticStructureEnumerator</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">default_magmoms</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">strategies</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">('ferromagnetic',</span> <span class="pre">'antiferromagnetic')</span></span>*, *<span class="n"><span class="pre">automatic</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">truncate_by_symmetry</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">max_orderings</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">64</span></span>*, *<span class="n"><span class="pre">transformation_kwargs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/analyzer.py#L598-L1067"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.analyzer.MagneticStructureEnumerator"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Combines MagneticStructureAnalyzer and MagOrderingTransformation to
automatically generate a set of transformations for a given structure
and produce a list of plausible magnetic orderings.

Generate different collinear magnetic orderings for a given input
structure.

If the input structure has magnetic moments defined, it is possible to
use these as a hint as to which elements are magnetic, otherwise
magnetic elements will be guessed (this can be changed using
default_magmoms kwarg).

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  input structure

- **default_magmoms** (*dict\[str,* *float\],* *optional*) – magnetic
  elements to their initial magnetic moments in μB, generally these are
  chosen to be high-spin since they can relax to a low-spin
  configuration during a DFT electronic configuration

- **strategies** (*Sequence\[str\]*) – ordering strategies to use,
  choose from: ferromagnetic, antiferromagnetic,
  antiferromagnetic_by_motif, ferrimagnetic_by_motif and
  ferrimagnetic_by_species (here, “motif”, means to use a different
  ordering parameter for symmetry inequivalent sites)

- **automatic** (*bool*) – if True, will automatically choose sensible
  strategies

- **truncate_by_symmetry** (*bool*) – if True, will remove very
  unsymmetrical orderings that are likely physically implausible

- **max_orderings** (*int*) – the maximum number of structures to return

- **transformation_kwargs** – keyword arguments to pass to
  MagOrderingTransformation, to change automatic cell size limits, etc.

<span class="sig-name descname"><span class="pre">available_strategies</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ClassVar</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="p"><span class="pre">...</span></span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">('ferromagnetic',</span> <span class="pre">'antiferromagnetic',</span> <span class="pre">'ferrimagnetic_by_motif',</span> <span class="pre">'ferrimagnetic_by_species',</span> <span class="pre">'antiferromagnetic_by_motif',</span> <span class="pre">'nonmagnetic')</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/analyzer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.analyzer.MagneticStructureEnumerator.available_strategies"
class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Ordering</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">value</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/analyzer.py#L51-L59"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.magnetism.analyzer.Ordering"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`Enum`</span>

Enumeration defining possible magnetic orderings.

<span class="sig-name descname"><span class="pre">AFM</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'AFM'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/analyzer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.magnetism.analyzer.Ordering.AFM"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">FM</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'FM'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/analyzer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.magnetism.analyzer.Ordering.FM"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">FiM</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'FiM'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/analyzer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.magnetism.analyzer.Ordering.FiM"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">NM</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'NM'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/analyzer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.magnetism.analyzer.Ordering.NM"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">Unknown</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'Unknown'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/analyzer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.magnetism.analyzer.Ordering.Unknown"
class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">OverwriteMagmomMode</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">value</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/analyzer.py#L62-L71"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.magnetism.analyzer.OverwriteMagmomMode"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`Enum`</span>

Enumeration defining different modes for analyzer.

<span class="sig-name descname"><span class="pre">none</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'none'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/analyzer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.magnetism.analyzer.OverwriteMagmomMode.none"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">normalize</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'normalize'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/analyzer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.analyzer.OverwriteMagmomMode.normalize"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">replace_all</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'replace_all'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/analyzer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.analyzer.OverwriteMagmomMode.replace_all"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">replace_all_if_undefined</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'replace_all_if_undefined'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/analyzer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.analyzer.OverwriteMagmomMode.replace_all_if_undefined"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">respect_sign</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'respect_sign'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/analyzer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.analyzer.OverwriteMagmomMode.respect_sign"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">respect_zeros</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'respect_zeros'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/analyzer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.analyzer.OverwriteMagmomMode.respect_zeros"
class="headerlink" title="Link to this definition"></a>  

<!-- -->

<span class="sig-name descname"><span class="pre">magnetic_deformation</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure_A</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">structure_B</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.analysis.magnetism.analyzer.MagneticDeformation"
class="reference internal"
title="pymatgen.analysis.magnetism.analyzer.MagneticDeformation"><span
class="pre">MagneticDeformation</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/analyzer.py#L1075-L1111"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.magnetism.analyzer.magnetic_deformation"
class="headerlink" title="Link to this definition"></a>  
Calculate ‘magnetic deformation proxy’, a measure of deformation (norm
of finite strain) between ‘non-magnetic’ (non-spin-polarized) and
ferromagnetic structures.

Adapted from Bocarsly et al. 2017, DOI: 10.1021/acs.chemmater.6b04729

Parameters<span class="colon">:</span>  
- **structure_A** – Structure

- **structure_B** – Structure

Returns<span class="colon">:</span>  
MagneticDeformation

</div>

<div id="module-pymatgen.analysis.magnetism.heisenberg" class="section">

<span id="pymatgen-analysis-magnetism-heisenberg-module"></span>

## pymatgen.analysis.magnetism.heisenberg module<a href="#module-pymatgen.analysis.magnetism.heisenberg"
class="headerlink" title="Link to this heading"></a>

This module implements a simple algorithm for extracting nearest
neighbor exchange parameters by mapping low energy magnetic orderings to
a Heisenberg model.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">HeisenbergMapper</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">ordered_structures</span></span>*, *<span class="n"><span class="pre">energies</span></span>*, *<span class="n"><span class="pre">cutoff</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.02</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/heisenberg.py#L38-L664"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Compute exchange parameters from low energy magnetic orderings.

<span class="sig-name descname"><span class="pre">strategy</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/heisenberg.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper.strategy"
class="headerlink" title="Link to this definition"></a>  
Class from pymatgen.analysis.local_env for constructing graphs.

Type<span class="colon">:</span>  
object

<span class="sig-name descname"><span class="pre">sgraphs</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/heisenberg.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper.sgraphs"
class="headerlink" title="Link to this definition"></a>  
StructureGraph objects.

Type<span class="colon">:</span>  
list

<span class="sig-name descname"><span class="pre">unique_site_ids</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/heisenberg.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper.unique_site_ids"
class="headerlink" title="Link to this definition"></a>  
Maps each site to its unique numerical identifier.

Type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">wyckoff_ids</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/heisenberg.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper.wyckoff_ids"
class="headerlink" title="Link to this definition"></a>  
Maps unique numerical identifier to wyckoff position.

Type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">nn_interactions</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/heisenberg.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper.nn_interactions"
class="headerlink" title="Link to this definition"></a>  
{i: j} pairs of NN interactions between unique sites.

Type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">dists</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/heisenberg.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper.dists"
class="headerlink" title="Link to this definition"></a>  
NN, NNN, and NNNN interaction distances

Type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">ex_mat</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/heisenberg.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper.ex_mat"
class="headerlink" title="Link to this definition"></a>  
Invertible Heisenberg Hamiltonian for each graph.

Type<span class="colon">:</span>  
DataFrame

<span class="sig-name descname"><span class="pre">ex_params</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/heisenberg.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper.ex_params"
class="headerlink" title="Link to this definition"></a>  
Exchange parameter values (meV/atom)

Type<span class="colon">:</span>  
dict

Exchange parameters are computed by mapping to a classical Heisenberg
model. Strategy is the scheme for generating neighbors. Currently only
MinimumDistanceNN is implemented. n+1 unique orderings are required to
compute n exchange parameters.

First run a MagneticOrderingsWF to obtain low energy collinear magnetic
orderings and find the magnetic ground state. Then enumerate magnetic
states with the ground state as the input structure, find the subset of
supercells that map to the ground state, and do static calculations for
these orderings.

Parameters<span class="colon">:</span>  
- **ordered_structures** (*list*) – Structure objects with magmoms.

- **energies** (*list*) – Total energies of each relaxed magnetic
  structure.

- **cutoff** (*float*) – Cutoff in Angstrom for nearest neighbor search.
  Defaults to 0 (only NN, no NNN, etc.)

- **tol** (*float*) – Tolerance (in Angstrom) on nearest neighbor
  distances being equal.

<span class="sig-name descname"><span class="pre">estimate_exchange</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">fm_struct</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">afm_struct</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">fm_e</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">afm_e</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/heisenberg.py#L454-L489"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper.estimate_exchange"
class="headerlink" title="Link to this definition"></a>  
Estimate \<J\> for a structure based on low energy FM and AFM orderings.

Parameters<span class="colon">:</span>  
- **fm_struct**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) – fm
  structure with ‘magmom’ site property

- **afm_struct**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  afm structure with ‘magmom’ site property

- **fm_e** (*float*) – fm energy/atom

- **afm_e** (*float*) – afm energy/atom

Returns<span class="colon">:</span>  
Average J exchange parameter (meV/atom)

Return type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">get_exchange</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/heisenberg.py#L353-L387"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper.get_exchange"
class="headerlink" title="Link to this definition"></a>  
Take Heisenberg Hamiltonian and corresponding energy for each row and
solve for the exchange parameters.

Returns<span class="colon">:</span>  
Exchange parameters (meV/atom).

Return type<span class="colon">:</span>  
dict\[str, float\]

<span class="sig-name descname"><span class="pre">get_heisenberg_model</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/heisenberg.py#L624-L664"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper.get_heisenberg_model"
class="headerlink" title="Link to this definition"></a>  
Save results of mapping to a HeisenbergModel object.

Returns<span class="colon">:</span>  
MSONable object.

Return type<span class="colon">:</span>  
<a href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergModel"
class="reference internal"
title="pymatgen.analysis.magnetism.heisenberg.HeisenbergModel">HeisenbergModel</a>

<span class="sig-name descname"><span class="pre">get_interaction_graph</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/heisenberg.py#L533-L576"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper.get_interaction_graph"
class="headerlink" title="Link to this definition"></a>  
Get a StructureGraph with edges and weights that correspond to exchange
interactions and J_ij values, respectively.

Parameters<span class="colon">:</span>  
**filename** (*str*) – if not None, save interaction graph to filename.

Returns<span class="colon">:</span>  
Exchange interaction graph.

Return type<span class="colon">:</span>  
<a href="pymatgen.analysis.html#pymatgen.analysis.graphs.StructureGraph"
class="reference internal"
title="pymatgen.analysis.graphs.StructureGraph">StructureGraph</a>

<span class="sig-name descname"><span class="pre">get_low_energy_orderings</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/heisenberg.py#L389-L452"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper.get_low_energy_orderings"
class="headerlink" title="Link to this definition"></a>  
Find lowest energy FM and AFM orderings to compute E_AFM - E_FM.

Returns<span class="colon">:</span>  
fm structure with ‘magmom’ site property afm_struct (Structure): afm
structure with ‘magmom’ site property fm_e (float): fm energy afm_e
(float): afm energy

Return type<span class="colon">:</span>  
fm_struct
(<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure">Structure</a>)

<span class="sig-name descname"><span class="pre">get_mft_temperature</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">j_avg</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/heisenberg.py#L491-L531"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergMapper.get_mft_temperature"
class="headerlink" title="Link to this definition"></a>  
Crude mean field estimate of critical temperature based on \<J\> for one
sublattice, or solving the coupled equations for a multi-sublattice
material.

Parameters<span class="colon">:</span>  
**j_avg** (*float*) – j_avg (float): Average exchange parameter
(meV/atom)

Returns<span class="colon">:</span>  
Critical temperature mft_t (K)

Return type<span class="colon">:</span>  
float

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">HeisenbergModel</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">formula</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">structures</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">energies</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">cutoff</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">tol</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sgraphs</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">unique_site_ids</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">wyckoff_ids</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">nn_interactions</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">dists</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ex_mat</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ex_params</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">javg</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">igraph</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/heisenberg.py#L802-L983"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergModel"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Store a Heisenberg model fit to low-energy magnetic orderings. Intended
to be generated by HeisenbergMapper.get_heisenberg_model().

Parameters<span class="colon">:</span>  
- **formula** (*str*) – Reduced formula of compound.

- **structures** (*list*) – Structure objects with magmoms.

- **energies** (*list*) – Energies of each relaxed magnetic structure.

- **cutoff** (*float*) – Cutoff in Angstrom for nearest neighbor search.

- **tol** (*float*) – Tolerance (in Angstrom) on nearest neighbor
  distances being equal.

- **sgraphs** (*list*) – StructureGraph objects.

- **unique_site_ids** (*dict*) – Maps each site to its unique numerical
  identifier.

- **wyckoff_ids** (*dict*) – Maps unique numerical identifier to wyckoff
  position.

- **nn_interactions** (*dict*) – {i: j} pairs of NN interactions between
  unique sites.

- **dists** (*dict*) – NN, NNN, and NNNN interaction distances

- **ex_mat** (*DataFrame*) – Invertible Heisenberg Hamiltonian for each
  graph.

- **ex_params** (*dict*) – Exchange parameter values (meV/atom).

- **javg** (*float*) – \<J\> exchange param (meV/atom).

- **igraph**
  (<a href="pymatgen.analysis.html#pymatgen.analysis.graphs.StructureGraph"
  class="reference internal"
  title="pymatgen.analysis.graphs.StructureGraph"><em>StructureGraph</em></a>)
  – Exchange interaction graph.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/heisenberg.py#L861-L882"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergModel.as_dict"
class="headerlink" title="Link to this definition"></a>  
Because some dicts have tuple keys, some sanitization is required for
JSON compatibility.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/heisenberg.py#L884-L938"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergModel.from_dict"
class="headerlink" title="Link to this definition"></a>  
Create a HeisenbergModel from a dict.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">HeisenbergScreener</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structures</span></span>*, *<span class="n"><span class="pre">energies</span></span>*, *<span class="n"><span class="pre">screen</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/heisenberg.py#L667-L799"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergScreener"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Clean and screen magnetic orderings.

Pre-processes magnetic orderings and energies for HeisenbergMapper. It
prioritizes low-energy orderings with large and localized magnetic
moments.

Parameters<span class="colon">:</span>  
- **structures** (*list*) – Structure objects with magnetic moments.

- **energies** (*list*) – Energies/atom of magnetic orderings.

- **screen** (*bool*) – Try to screen out high energy and low-spin
  configurations.

<span class="sig-name descname"><span class="pre">screened_structures</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/heisenberg.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergScreener.screened_structures"
class="headerlink" title="Link to this definition"></a>  
Sorted structures.

Type<span class="colon">:</span>  
list

<span class="sig-name descname"><span class="pre">screened_energies</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/magnetism/heisenberg.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.heisenberg.HeisenbergScreener.screened_energies"
class="headerlink" title="Link to this definition"></a>  
Sorted energies.

Type<span class="colon">:</span>  
list

</div>

<div id="module-pymatgen.analysis.magnetism.jahnteller" class="section">

<span id="pymatgen-analysis-magnetism-jahnteller-module"></span>

## pymatgen.analysis.magnetism.jahnteller module<a href="#module-pymatgen.analysis.magnetism.jahnteller"
class="headerlink" title="Link to this heading"></a>

JahnTeller distortion analysis.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">JahnTellerAnalyzer</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/jahnteller.py#L25-L477"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.magnetism.jahnteller.JahnTellerAnalyzer"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Will attempt to classify if structure *may* be Jahn-Teller active. Class
currently uses datafile of hard-coded common Jahn-Teller active ions. If
structure is annotated with magnetic moments, will estimate if structure
may be high-spin or low-spin. Class aims for more false-positives than
false-negatives.

Init for JahnTellerAnalyzer.

<span class="sig-name descname"><span class="pre">get_analysis</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">calculate_valences</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">guesstimate_spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">op_threshold</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.1</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/jahnteller.py#L215-L249"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.jahnteller.JahnTellerAnalyzer.get_analysis"
class="headerlink" title="Link to this definition"></a>  
Convenience method, uses get_analysis_and_structure method.

Obtain an analysis of a given structure and if it may be Jahn-Teller
active or not. This is a heuristic, and may give false positives and
false negatives (false positives are preferred).

Parameters<span class="colon">:</span>  
- **structure** – input structure

- **calculate_valences** – whether to attempt to calculate valences or
  not, structure should have oxidation states to perform analysis
  (Default value = True)

- **guesstimate_spin** – whether to guesstimate spin state from magnetic
  moments or not, use with caution (Default value = False)

- **op_threshold** – threshold for order parameter above which to
  consider site to match an octahedral or tetrahedral motif, since
  Jahn-Teller structures can often be quite distorted, this threshold is
  smaller than one might expect

Returns<span class="colon">:</span>  
analysis of structure, with key ‘strength’ which may be ‘none’,
‘strong’, ‘weak’, or ‘unknown’ (Default value = 0.1)

<span class="sig-name descname"><span class="pre">get_analysis_and_structure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">calculate_valences</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">guesstimate_spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">op_threshold</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.1</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/jahnteller.py#L82-L213"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.jahnteller.JahnTellerAnalyzer.get_analysis_and_structure"
class="headerlink" title="Link to this definition"></a>  
Obtain an analysis of a given structure and if it may be Jahn-Teller
active or not. This is a heuristic, and may give false positives and
false negatives (false positives are preferred).

Parameters<span class="colon">:</span>  
- **structure** – input structure

- **calculate_valences** – whether to attempt to calculate valences or
  not, structure should have oxidation states to perform analysis
  (Default value = True)

- **guesstimate_spin** – whether to guesstimate spin state from magnetic
  moments or not, use with caution (Default value = False)

- **op_threshold** – threshold for order parameter above which to
  consider site to match an octahedral or tetrahedral motif, since
  Jahn-Teller structures can often be quite distorted, this threshold is
  smaller than one might expect

Returns<span class="colon">:</span>  
analysis of structure, with key ‘strength’ which may be ‘none’,
‘strong’, ‘weak’, or ‘unknown’ (Default value = 0.1) and decorated
structure

<span class="sig-name descname"><span class="pre">get_magnitude_of_effect_from_species</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">species</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.periodic_table.Species"
class="reference internal"
title="pymatgen.core.periodic_table.Species"><span
class="pre">Species</span></a></span>*, *<span class="n"><span class="pre">spin_state</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">motif</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/jahnteller.py#L358-L385"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.jahnteller.JahnTellerAnalyzer.get_magnitude_of_effect_from_species"
class="headerlink" title="Link to this definition"></a>  
Get magnitude of Jahn-Teller effect from provided species, spin state
and motif.

Parameters<span class="colon">:</span>  
- **species** – e.g. Fe2+

- **spin_state** – “high” or “low”

- **motif** – “oct” or “tet”

Returns<span class="colon">:</span>  
“none”, “weak” or “strong”

Return type<span class="colon">:</span>  
str

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">get_magnitude_of_effect_from_spin_config</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">motif</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">spin_config</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/jahnteller.py#L387-L416"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.jahnteller.JahnTellerAnalyzer.get_magnitude_of_effect_from_spin_config"
class="headerlink" title="Link to this definition"></a>  
Roughly, the magnitude of Jahn-Teller distortion will be: \* in
octahedral environments, strong if e_g orbitals unevenly occupied but
weak if t_2g orbitals unevenly occupied \* in tetrahedral environments
always weaker.

Parameters<span class="colon">:</span>  
- **motif** – “oct” or “tet”

- **spin_config** – dict of ‘e’ (e_g) and ‘t’ (t2_g) with number of
  electrons in each state

Returns<span class="colon">:</span>  
“none”, “weak” or “strong”

Return type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">is_jahn_teller_active</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">calculate_valences</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">guesstimate_spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">op_threshold</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.1</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/jahnteller.py#L251-L291"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.jahnteller.JahnTellerAnalyzer.is_jahn_teller_active"
class="headerlink" title="Link to this definition"></a>  
Convenience method, uses get_analysis_and_structure method. Check if a
given structure and if it may be Jahn-Teller active or not. This is a
heuristic, and may give false positives and false negatives (false
positives are preferred).

Parameters<span class="colon">:</span>  
- **structure** – input structure

- **calculate_valences** – whether to attempt to calculate valences or
  not, structure should have oxidation states to perform analysis
  (Default value = True)

- **guesstimate_spin** – whether to guesstimate spin state from magnetic
  moments or not, use with caution (Default value = False)

- **op_threshold** – threshold for order parameter above which to
  consider site to match an octahedral or tetrahedral motif, since
  Jahn-Teller structures can often be quite distorted, this threshold is
  smaller than one might expect

Returns<span class="colon">:</span>  
True if might be Jahn-Teller active, False if not

Return type<span class="colon">:</span>  
bool

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">mu_so</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">species</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.periodic_table.Species"
class="reference internal"
title="pymatgen.core.periodic_table.Species"><span
class="pre">Species</span></a></span>*, *<span class="n"><span class="pre">motif</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'oct'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'tet'</span></span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">spin_state</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'high'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'low'</span></span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/jahnteller.py#L454-L477"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.jahnteller.JahnTellerAnalyzer.mu_so"
class="headerlink" title="Link to this definition"></a>  
Calculate the spin-only magnetic moment for a given species. Only
supports transition metals.

Parameters<span class="colon">:</span>  
- **species** – Species

- **motif** (*"oct"* *\|* *"tet"*) – Tetrahedron or octahedron crystal
  site coordination

- **spin_state** (*"low"* *\|* *"high"*) – Whether the species is in a
  high or low spin state

Returns<span class="colon">:</span>  
Spin-only magnetic moment in Bohr magnetons or None if  
species crystal field not defined

Return type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">tag_structure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">calculate_valences</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">guesstimate_spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">op_threshold</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.1</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/magnetism/jahnteller.py#L293-L334"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.magnetism.jahnteller.JahnTellerAnalyzer.tag_structure"
class="headerlink" title="Link to this definition"></a>  
Convenience method, uses get_analysis_and_structure method. Add a
“possible_jt_active” site property on Structure.

Parameters<span class="colon">:</span>  
- **structure** – input structure

- **calculate_valences** – whether to attempt to calculate valences or
  not, structure should have oxidation states to perform analysis
  (Default value = True)

- **guesstimate_spin** – whether to guesstimate spin state from magnetic
  moments or not, use with caution (Default value = False)

- **op_threshold** – threshold for order parameter above which to
  consider site to match an octahedral or tetrahedral motif, since
  Jahn-Teller structures can often be quite distorted, this threshold is
  smaller than one might expect

Returns<span class="colon">:</span>  
Decorated Structure, will be in primitive setting.

</div>

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
