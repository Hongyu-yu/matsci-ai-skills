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

- <a href="#" class="reference internal">pymatgen.analysis.interfaces
  package</a>
  - <a href="#submodules" class="reference internal">Submodules</a>
  - <a href="#module-pymatgen.analysis.interfaces.coherent_interfaces"
    class="reference internal">pymatgen.analysis.interfaces.coherent_interfaces
    module</a>
    - <a
      href="#pymatgen.analysis.interfaces.coherent_interfaces.CoherentInterfaceBuilder"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">CoherentInterfaceBuilder</code></span></a>
      - <a
        href="#pymatgen.analysis.interfaces.coherent_interfaces.CoherentInterfaceBuilder.get_interfaces"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CoherentInterfaceBuilder.get_interfaces()</code></span></a>
    - <a
      href="#pymatgen.analysis.interfaces.coherent_interfaces.from_2d_to_3d"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">from_2d_to_3d()</code></span></a>
    - <a
      href="#pymatgen.analysis.interfaces.coherent_interfaces.get_2d_transform"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">get_2d_transform()</code></span></a>
    - <a
      href="#pymatgen.analysis.interfaces.coherent_interfaces.get_rot_3d_for_2d"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">get_rot_3d_for_2d()</code></span></a>
  - <a href="#module-pymatgen.analysis.interfaces.substrate_analyzer"
    class="reference internal">pymatgen.analysis.interfaces.substrate_analyzer
    module</a>
    - <a
      href="#pymatgen.analysis.interfaces.substrate_analyzer.SubstrateAnalyzer"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">SubstrateAnalyzer</code></span></a>
      - <a
        href="#pymatgen.analysis.interfaces.substrate_analyzer.SubstrateAnalyzer.calculate"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SubstrateAnalyzer.calculate()</code></span></a>
      - <a
        href="#pymatgen.analysis.interfaces.substrate_analyzer.SubstrateAnalyzer.generate_surface_vectors"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SubstrateAnalyzer.generate_surface_vectors()</code></span></a>
    - <a
      href="#pymatgen.analysis.interfaces.substrate_analyzer.SubstrateMatch"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">SubstrateMatch</code></span></a>
      - <a
        href="#pymatgen.analysis.interfaces.substrate_analyzer.SubstrateMatch.elastic_energy"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SubstrateMatch.elastic_energy</code></span></a>
      - <a
        href="#pymatgen.analysis.interfaces.substrate_analyzer.SubstrateMatch.film_miller"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SubstrateMatch.film_miller</code></span></a>
      - <a
        href="#pymatgen.analysis.interfaces.substrate_analyzer.SubstrateMatch.from_zsl"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SubstrateMatch.from_zsl()</code></span></a>
      - <a
        href="#pymatgen.analysis.interfaces.substrate_analyzer.SubstrateMatch.ground_state_energy"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SubstrateMatch.ground_state_energy</code></span></a>
      - <a
        href="#pymatgen.analysis.interfaces.substrate_analyzer.SubstrateMatch.strain"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SubstrateMatch.strain</code></span></a>
      - <a
        href="#pymatgen.analysis.interfaces.substrate_analyzer.SubstrateMatch.substrate_miller"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SubstrateMatch.substrate_miller</code></span></a>
      - <a
        href="#pymatgen.analysis.interfaces.substrate_analyzer.SubstrateMatch.total_energy"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SubstrateMatch.total_energy</code></span></a>
      - <a
        href="#pymatgen.analysis.interfaces.substrate_analyzer.SubstrateMatch.von_mises_strain"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SubstrateMatch.von_mises_strain</code></span></a>
  - <a href="#module-pymatgen.analysis.interfaces.zsl"
    class="reference internal">pymatgen.analysis.interfaces.zsl module</a>
    - <a href="#pymatgen.analysis.interfaces.zsl.ZSLGenerator"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">ZSLGenerator</code></span></a>
      - <a
        href="#pymatgen.analysis.interfaces.zsl.ZSLGenerator.generate_sl_transformation_sets"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ZSLGenerator.generate_sl_transformation_sets()</code></span></a>
      - <a
        href="#pymatgen.analysis.interfaces.zsl.ZSLGenerator.get_equiv_transformations"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ZSLGenerator.get_equiv_transformations()</code></span></a>
    - <a href="#pymatgen.analysis.interfaces.zsl.ZSLMatch"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">ZSLMatch</code></span></a>
      - <a href="#pymatgen.analysis.interfaces.zsl.ZSLMatch.film_sl_vectors"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ZSLMatch.film_sl_vectors</code></span></a>
      - <a href="#pymatgen.analysis.interfaces.zsl.ZSLMatch.film_transformation"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ZSLMatch.film_transformation</code></span></a>
      - <a href="#pymatgen.analysis.interfaces.zsl.ZSLMatch.film_vectors"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ZSLMatch.film_vectors</code></span></a>
      - <a href="#pymatgen.analysis.interfaces.zsl.ZSLMatch.match_area"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ZSLMatch.match_area</code></span></a>
      - <a
        href="#pymatgen.analysis.interfaces.zsl.ZSLMatch.match_transformation"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ZSLMatch.match_transformation</code></span></a>
      - <a
        href="#pymatgen.analysis.interfaces.zsl.ZSLMatch.substrate_sl_vectors"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ZSLMatch.substrate_sl_vectors</code></span></a>
      - <a
        href="#pymatgen.analysis.interfaces.zsl.ZSLMatch.substrate_transformation"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ZSLMatch.substrate_transformation</code></span></a>
      - <a href="#pymatgen.analysis.interfaces.zsl.ZSLMatch.substrate_vectors"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ZSLMatch.substrate_vectors</code></span></a>
    - <a href="#pymatgen.analysis.interfaces.zsl.fast_norm"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">fast_norm()</code></span></a>
    - <a href="#pymatgen.analysis.interfaces.zsl.gen_sl_transform_matrices"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">gen_sl_transform_matrices()</code></span></a>
    - <a href="#pymatgen.analysis.interfaces.zsl.get_factors"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">get_factors()</code></span></a>
    - <a href="#pymatgen.analysis.interfaces.zsl.is_same_vectors"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">is_same_vectors()</code></span></a>
    - <a href="#pymatgen.analysis.interfaces.zsl.reduce_vectors"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">reduce_vectors()</code></span></a>
    - <a href="#pymatgen.analysis.interfaces.zsl.rel_angle"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">rel_angle()</code></span></a>
    - <a href="#pymatgen.analysis.interfaces.zsl.rel_strain"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">rel_strain()</code></span></a>
    - <a href="#pymatgen.analysis.interfaces.zsl.vec_angle"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">vec_angle()</code></span></a>
    - <a href="#pymatgen.analysis.interfaces.zsl.vec_area"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">vec_area()</code></span></a>

</div>

</div>

</div>

<div class="section wy-nav-content-wrap" toggle="wy-nav-shift">

[pymatgen](index.html)

<div class="wy-nav-content">

<div class="rst-content style-external-links">

<div role="navigation" aria-label="Page navigation">

- <a href="index.html" class="icon icon-home" aria-label="Home"></a>
- pymatgen.analysis.interfaces package
- <a
  href="https://github.com/materialsproject/pymatgen/blob/master/docs_rst/pymatgen.analysis.interfaces.rst"
  class="fa fa-github">Edit on GitHub</a>

------------------------------------------------------------------------

</div>

<div class="document" role="main" itemscope="itemscope"
itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="module-pymatgen.analysis.interfaces" class="section">

<span id="pymatgen-analysis-interfaces-package"></span>

# pymatgen.analysis.interfaces package<a href="#module-pymatgen.analysis.interfaces" class="headerlink"
title="Link to this heading"></a>

Module that implements various algorithms related to interface
construction and analysis.

<div id="submodules" class="section">

## Submodules<a href="#submodules" class="headerlink"
title="Link to this heading"></a>

</div>

<div id="module-pymatgen.analysis.interfaces.coherent_interfaces"
class="section">

<span
id="pymatgen-analysis-interfaces-coherent-interfaces-module"></span>

## pymatgen.analysis.interfaces.coherent_interfaces module<a href="#module-pymatgen.analysis.interfaces.coherent_interfaces"
class="headerlink" title="Link to this heading"></a>

This module provides classes to store, generate, and manipulate material
interfaces.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">CoherentInterfaceBuilder</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">substrate_structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">film_structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">film_miller</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">substrate_miller</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">zslgen</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.analysis.interfaces.zsl.ZSLGenerator"
class="reference internal"
title="pymatgen.analysis.interfaces.zsl.ZSLGenerator"><span
class="pre">ZSLGenerator</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">termination_ftol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.25</span></span>*, *<span class="n"><span class="pre">label_index</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">filter_out_sym_slabs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/interfaces/coherent_interfaces.py#L22-L258"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.interfaces.coherent_interfaces.CoherentInterfaceBuilder"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

This class constructs the coherent interfaces between two crystalline
slabs Coherency is defined by matching lattices not sub-planes.

Parameters<span class="colon">:</span>  
- **substrate_structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  substrate structure

- **film_structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  film structure

- **film_miller** (*tuple\[int,* *int,* *int\]*) – miller index for the
  film layer

- **substrate_miller** (*tuple\[int,* *int,* *int\]*) – miller index for
  the substrate layer

- **zslgen** (<a href="#pymatgen.analysis.interfaces.zsl.ZSLGenerator"
  class="reference internal"
  title="pymatgen.analysis.interfaces.zsl.ZSLGenerator"><em>ZSLGenerator</em></a>
  *\|* *None*) – BiDirectionalZSL if you want custom lattice matching
  tolerances for coherency.

- **termination_ftol** (*float*) – tolerance to distinguish different
  terminating atomic planes.

- **label_index** (*bool*) – If True add an extra index at the beginning
  of the termination label.

- **filter_out_sym_slabs** (*bool*) – If True filter out identical slabs
  with different terminations. This might need to be set as False to
  find more non-identical terminations because slab identity separately
  does not mean combinational identity.

<span class="sig-name descname"><span class="pre">get_interfaces</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">termination</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">gap</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">2.0</span></span>*, *<span class="n"><span class="pre">vacuum_over_film</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">20.0</span></span>*, *<span class="n"><span class="pre">film_thickness</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1</span></span>*, *<span class="n"><span class="pre">substrate_thickness</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1</span></span>*, *<span class="n"><span class="pre">in_layers</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Iterator</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.interface.Interface"
class="reference internal"
title="pymatgen.core.interface.Interface"><span
class="pre">Interface</span></a><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/interfaces/coherent_interfaces.py#L164-L258"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.interfaces.coherent_interfaces.CoherentInterfaceBuilder.get_interfaces"
class="headerlink" title="Link to this definition"></a>  
Generate interface structures given the film and substrate structure as
well as the desired terminations.

Parameters<span class="colon">:</span>  
- **termination** (*tuple\[str,* *str\]*) – termination from
  self.termination list

- **gap** (*float,* *optional*) – gap between film and substrate.
  Defaults to 2.0.

- **vacuum_over_film** (*float,* *optional*) – vacuum over the top of
  the film. Defaults to 20.0.

- **film_thickness** (*float,* *optional*) – the film thickness.
  Defaults to 1.

- **substrate_thickness** (*float,* *optional*) – substrate thickness.
  Defaults to 1.

- **in_layers** (*bool,* *optional*) – set the thickness in layer units.
  Defaults to True.

Yields<span class="colon">:</span>  
*Iterator\[Interface\]* – interfaces from slabs

<!-- -->

<span class="sig-name descname"><span class="pre">from_2d_to_3d</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">mat</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ndarray</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">ndarray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/interfaces/coherent_interfaces.py#L292-L296"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.interfaces.coherent_interfaces.from_2d_to_3d"
class="headerlink" title="Link to this definition"></a>  
Convert a 2D matrix to a 3D matrix.

<!-- -->

<span class="sig-name descname"><span class="pre">get_2d_transform</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">start</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span></span>*, *<span class="n"><span class="pre">end</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">np.ndarray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/interfaces/coherent_interfaces.py#L284-L289"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.interfaces.coherent_interfaces.get_2d_transform"
class="headerlink" title="Link to this definition"></a>  
Gets a 2d transformation matrix that converts start to end.

<!-- -->

<span class="sig-name descname"><span class="pre">get_rot_3d_for_2d</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">film_matrix</span></span>*, *<span class="n"><span class="pre">sub_matrix</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">ndarray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/interfaces/coherent_interfaces.py#L261-L281"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.interfaces.coherent_interfaces.get_rot_3d_for_2d"
class="headerlink" title="Link to this definition"></a>  
Find transformation matrix that will rotate and strain the film to the
substrate while preserving the c-axis.

</div>

<div id="module-pymatgen.analysis.interfaces.substrate_analyzer"
class="section">

<span
id="pymatgen-analysis-interfaces-substrate-analyzer-module"></span>

## pymatgen.analysis.interfaces.substrate_analyzer module<a href="#module-pymatgen.analysis.interfaces.substrate_analyzer"
class="headerlink" title="Link to this heading"></a>

This module provides classes to identify optimal substrates for film
growth.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">SubstrateAnalyzer</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">film_max_miller</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1</span></span>*, *<span class="n"><span class="pre">substrate_max_miller</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/interfaces/substrate_analyzer.py#L86-L203"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.interfaces.substrate_analyzer.SubstrateAnalyzer"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.analysis.interfaces.zsl.ZSLGenerator"
class="reference internal"
title="pymatgen.analysis.interfaces.zsl.ZSLGenerator"><span
class="pre"><code
class="sourceCode python">ZSLGenerator</code></span></a>

This class applies a set of search criteria to identify suitable
substrates for film growth. It first uses a topological search by Zur
and McGill to identify matching super-lattices on various faces of the
two materials. Additional criteria can then be used to identify the most
suitable substrate. Currently, the only additional criteria is the
elastic strain energy of the super-lattices.

Initialize the substrate analyzer.

Parameters<span class="colon">:</span>  
- **zslgen** (<a href="#pymatgen.analysis.interfaces.zsl.ZSLGenerator"
  class="reference internal"
  title="pymatgen.analysis.interfaces.zsl.ZSLGenerator"><em>ZSLGenerator</em></a>)
  – Defaults to a ZSLGenerator with standard tolerances, but can be fed
  one with custom tolerances

- **film_max_miller** (*int*) – maximum miller index to generate for
  film surfaces

- **substrate_max_miller** (*int*) – maximum miller index to generate
  for substrate surfaces.

<span class="sig-name descname"><span class="pre">calculate</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">film</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">substrate</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">elasticity_tensor</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">film_millers</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">substrate_millers</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ground_state_energy</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">lowest</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/interfaces/substrate_analyzer.py#L150-L203"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.interfaces.substrate_analyzer.SubstrateAnalyzer.calculate"
class="headerlink" title="Link to this definition"></a>  
Find all topological matches for the substrate and calculates elastic
strain energy and total energy for the film if elasticity tensor and
ground state energy are provided:

Parameters<span class="colon">:</span>  
- **film**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  conventional standard structure for the film

- **substrate**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  conventional standard structure for the substrate

- **elasticity_tensor** (<a
  href="pymatgen.analysis.elasticity.html#pymatgen.analysis.elasticity.elastic.ElasticTensor"
  class="reference internal"
  title="pymatgen.analysis.elasticity.elastic.ElasticTensor"><em>ElasticTensor</em></a>)
  – elasticity tensor for the film in the IEEE orientation

- **film_millers** (*array*) – film facets to consider in search as
  defined by miller indices

- **substrate_millers** (*array*) – substrate facets to consider in
  search as defined by miller indices

- **ground_state_energy** (*float*) – ground state energy for the film

- **lowest** (*bool*) – only consider lowest matching area for each
  surface

<span class="sig-name descname"><span class="pre">generate_surface_vectors</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">film</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">substrate</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">film_millers</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">substrate_millers</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/interfaces/substrate_analyzer.py#L112-L148"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.interfaces.substrate_analyzer.SubstrateAnalyzer.generate_surface_vectors"
class="headerlink" title="Link to this definition"></a>  
Generate the film/substrate slab combinations for a set of given miller
indices.

Parameters<span class="colon">:</span>  
- **film**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  film structure

- **substrate**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  substrate structure

- **film_millers** (*array*) – all miller indices to generate slabs for
  film

- **substrate_millers** (*array*) – all miller indices to generate slabs
  for substrate

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">SubstrateMatch</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">film_sl_vectors</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span>*, *<span class="n"><span class="pre">substrate_sl_vectors</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span>*, *<span class="n"><span class="pre">film_vectors</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span>*, *<span class="n"><span class="pre">substrate_vectors</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span>*, *<span class="n"><span class="pre">film_transformation</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span>*, *<span class="n"><span class="pre">substrate_transformation</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span>*, *<span class="n"><span class="pre">film_miller</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">substrate_miller</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">strain</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a
href="pymatgen.analysis.elasticity.html#pymatgen.analysis.elasticity.strain.Strain"
class="reference internal"
title="pymatgen.analysis.elasticity.strain.Strain"><span
class="pre">Strain</span></a></span>*, *<span class="n"><span class="pre">von_mises_strain</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">ground_state_energy</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">elastic_energy</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/interfaces/substrate_analyzer.py#L19-L83"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.interfaces.substrate_analyzer.SubstrateMatch"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.analysis.interfaces.zsl.ZSLMatch"
class="reference internal"
title="pymatgen.analysis.interfaces.zsl.ZSLMatch"><span
class="pre"><code class="sourceCode python">ZSLMatch</code></span></a>

A substrate match building on the Zur and McGill algorithm. This match
class includes the miller planes of the film and substrate the full
strain tensor, the Von Mises strain, the ground state energy if
provided, and the elastic energy.

<span class="sig-name descname"><span class="pre">elastic_energy</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/interfaces/substrate_analyzer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.interfaces.substrate_analyzer.SubstrateMatch.elastic_energy"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">film_miller</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/interfaces/substrate_analyzer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.interfaces.substrate_analyzer.SubstrateMatch.film_miller"
class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_zsl</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">match</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.analysis.interfaces.zsl.ZSLMatch"
class="reference internal"
title="pymatgen.analysis.interfaces.zsl.ZSLMatch"><span
class="pre">ZSLMatch</span></a></span>*, *<span class="n"><span class="pre">film</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">film_miller</span></span>*, *<span class="n"><span class="pre">substrate_miller</span></span>*, *<span class="n"><span class="pre">elasticity_tensor</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ground_state_energy</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/interfaces/substrate_analyzer.py#L34-L78"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.interfaces.substrate_analyzer.SubstrateMatch.from_zsl"
class="headerlink" title="Link to this definition"></a>  
Generate a substrate match from a ZSL match plus metadata.

<span class="sig-name descname"><span class="pre">ground_state_energy</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/interfaces/substrate_analyzer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.interfaces.substrate_analyzer.SubstrateMatch.ground_state_energy"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">strain</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a
href="pymatgen.analysis.elasticity.html#pymatgen.analysis.elasticity.strain.Strain"
class="reference internal"
title="pymatgen.analysis.elasticity.strain.Strain"><span
class="pre">Strain</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/interfaces/substrate_analyzer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.interfaces.substrate_analyzer.SubstrateMatch.strain"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">substrate_miller</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/interfaces/substrate_analyzer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.interfaces.substrate_analyzer.SubstrateMatch.substrate_miller"
class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">total_energy</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/interfaces/substrate_analyzer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.interfaces.substrate_analyzer.SubstrateMatch.total_energy"
class="headerlink" title="Link to this definition"></a>  
Total energy of this match.

<span class="sig-name descname"><span class="pre">von_mises_strain</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/interfaces/substrate_analyzer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.interfaces.substrate_analyzer.SubstrateMatch.von_mises_strain"
class="headerlink" title="Link to this definition"></a>  

</div>

<div id="module-pymatgen.analysis.interfaces.zsl" class="section">

<span id="pymatgen-analysis-interfaces-zsl-module"></span>

## pymatgen.analysis.interfaces.zsl module<a href="#module-pymatgen.analysis.interfaces.zsl" class="headerlink"
title="Link to this heading"></a>

This module implements the Zur and McGill lattice matching algorithm.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ZSLGenerator</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">max_area_ratio_tol</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.09</span></span>*, *<span class="n"><span class="pre">max_area</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">400</span></span>*, *<span class="n"><span class="pre">max_length_tol</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.03</span></span>*, *<span class="n"><span class="pre">max_angle_tol</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.01</span></span>*, *<span class="n"><span class="pre">bidirectional</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/interfaces/zsl.py#L62-L217"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.interfaces.zsl.ZSLGenerator"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

This class generate matching interface super lattices based on the
methodology of lattice vector matching for heterostructural interfaces
proposed by Zur and McGill: Journal of Applied Physics 55 (1984), 378 ;
doi: 10.1063/1.333084 The process of generating all possible matching
super lattices is: 1.) Reduce the surface lattice vectors and calculate
area for the surfaces 2.) Generate all super lattice transformations
within a maximum allowed area

> <div>
>
> limit that give nearly equal area super-lattices for the two
> surfaces - generate_sl_transformation_sets
>
> </div>

3.) For each superlattice set:  
1.) Reduce super lattice vectors 2.) Check length and angle between film
and substrate super lattice

> <div>
>
> vectors to determine if the super lattices are the nearly same and
> therefore coincident - get_equiv_transformations.
>
> </div>

Initialize a Zur Super Lattice Generator for a specific film and  
substrate.

Parameters<span class="colon">:</span>  
- **max_area_ratio_tol** (*float*) – Max tolerance on ratio of
  super-lattices to consider equal

- **max_area** (*float*) – max super lattice area to generate in search

- **max_length_tol** – maximum length tolerance in checking if two
  vectors are of nearly the same length

- **max_angle_tol** – maximum angle tolerance in checking of two sets of
  vectors have nearly the same angle between them.

<span class="sig-name descname"><span class="pre">generate_sl_transformation_sets</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">film_area</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">substrate_area</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Iterator</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/interfaces/zsl.py#L111-L144"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.interfaces.zsl.ZSLGenerator.generate_sl_transformation_sets"
class="headerlink" title="Link to this definition"></a>  
Generate transformation sets for film/substrate pair given the area of
the unit cell area for the film and substrate. The transformation sets
map the film and substrate unit cells to super lattices with a maximum
area.

Parameters<span class="colon">:</span>  
- **film_area** (*int*) – the unit cell area for the film

- **substrate_area** (*int*) – the unit cell area for the substrate

Yields<span class="colon">:</span>  
*transformation_sets* –

a set of transformation_sets defined as:  
1.) the transformation matrices for the film to create a super lattice
of area i\*film area 2.) the transformation matrices for the substrate
to create a super lattice of area j\*film area.

<span class="sig-name descname"><span class="pre">get_equiv_transformations</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">transformation_sets</span></span>*, *<span class="n"><span class="pre">film_vectors</span></span>*, *<span class="n"><span class="pre">substrate_vectors</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/interfaces/zsl.py#L146-L188"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.interfaces.zsl.ZSLGenerator.get_equiv_transformations"
class="headerlink" title="Link to this definition"></a>  
Applies the transformation_sets to the film and substrate vectors to
generate super-lattices and checks if they matches. Returns all matching
vectors sets.

Parameters<span class="colon">:</span>  
- **transformation_sets** (*array*) – an array of transformation sets:
  each transformation set is an array with the (i,j) indicating the area
  multiples of the film and substrate it corresponds to, an array with
  all possible transformations for the film area multiple i and another
  array for the substrate area multiple j.

- **film_vectors** (*array*) – film vectors to generate super lattices

- **substrate_vectors** (*array*) – substrate vectors to generate super
  lattices

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ZSLMatch</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">film_sl_vectors</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span>*, *<span class="n"><span class="pre">substrate_sl_vectors</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span>*, *<span class="n"><span class="pre">film_vectors</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span>*, *<span class="n"><span class="pre">substrate_vectors</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span>*, *<span class="n"><span class="pre">film_transformation</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span>*, *<span class="n"><span class="pre">substrate_transformation</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/interfaces/zsl.py#L19-L59"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.interfaces.zsl.ZSLMatch" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

A match from the Zur and McGill Algorithm. The super_lattice vectors are
listed as \_sl_vectors. These are reduced according to the algorithm in
the paper which effectively a rotation in 3D space. Use the
match_transformation property to get the appropriate transformation
matrix.

<span class="sig-name descname"><span class="pre">film_sl_vectors</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/interfaces/zsl.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.interfaces.zsl.ZSLMatch.film_sl_vectors"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">film_transformation</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/interfaces/zsl.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.interfaces.zsl.ZSLMatch.film_transformation"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">film_vectors</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/interfaces/zsl.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.interfaces.zsl.ZSLMatch.film_vectors"
class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">match_area</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/interfaces/zsl.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.interfaces.zsl.ZSLMatch.match_area"
class="headerlink" title="Link to this definition"></a>  
The area of the match between the substrate and film super lattice
vectors.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">match_transformation</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/interfaces/zsl.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.interfaces.zsl.ZSLMatch.match_transformation"
class="headerlink" title="Link to this definition"></a>  
The transformation matrix to convert the film super lattice vectors to
the substrate.

<span class="sig-name descname"><span class="pre">substrate_sl_vectors</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/interfaces/zsl.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.interfaces.zsl.ZSLMatch.substrate_sl_vectors"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">substrate_transformation</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/interfaces/zsl.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.interfaces.zsl.ZSLMatch.substrate_transformation"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">substrate_vectors</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/interfaces/zsl.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.interfaces.zsl.ZSLMatch.substrate_vectors"
class="headerlink" title="Link to this definition"></a>  

<!-- -->

<span class="sig-name descname"><span class="pre">fast_norm</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">a</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/interfaces/zsl.py#L263-L270"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.interfaces.zsl.fast_norm" class="headerlink"
title="Link to this definition"></a>  
Much faster variant of numpy linalg norm.

<!-- -->

<span class="sig-name descname"><span class="pre">gen_sl_transform_matrices</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">area_multiple</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/interfaces/zsl.py#L220-L242"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.interfaces.zsl.gen_sl_transform_matrices"
class="headerlink" title="Link to this definition"></a>  
Generates the transformation matrices that convert a set of 2D vectors
into a super lattice of integer area multiple as proven in Cassels:

Cassels, John William Scott. An introduction to the geometry of numbers.
Springer Science & Business Media, 2012.

Parameters<span class="colon">:</span>  
- **area_multiple** (*int*) – integer multiple of unit cell area for
  super

- **area** (*lattice*)

Returns<span class="colon">:</span>  
transformation matrices to convert unit vectors to super lattice vectors

Return type<span class="colon">:</span>  
matrix_list

<!-- -->

<span class="sig-name descname"><span class="pre">get_factors</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">n</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/interfaces/zsl.py#L313-L318"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.interfaces.zsl.get_factors"
class="headerlink" title="Link to this definition"></a>  
Generate all factors of n.

<!-- -->

<span class="sig-name descname"><span class="pre">is_same_vectors</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">vec_set1</span></span>*, *<span class="n"><span class="pre">vec_set2</span></span>*, *<span class="n"><span class="pre">bidirectional</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">max_length_tol</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.03</span></span>*, *<span class="n"><span class="pre">max_angle_tol</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.01</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/interfaces/zsl.py#L345-L364"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.interfaces.zsl.is_same_vectors"
class="headerlink" title="Link to this definition"></a>  
Determine if two sets of vectors are the same within length and angle
tolerances :param vec_set1: an array of two vectors :type vec_set1:
array\[array\] :param vec_set2: second array of two vectors. :type
vec_set2: array\[array\]

<!-- -->

<span class="sig-name descname"><span class="pre">reduce_vectors</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">a</span></span>*, *<span class="n"><span class="pre">b</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/interfaces/zsl.py#L287-L310"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.interfaces.zsl.reduce_vectors"
class="headerlink" title="Link to this definition"></a>  
Generate independent and unique basis vectors based on the methodology
of Zur and McGill.

<!-- -->

<span class="sig-name descname"><span class="pre">rel_angle</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">vec_set1</span></span>*, *<span class="n"><span class="pre">vec_set2</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/interfaces/zsl.py#L251-L260"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.interfaces.zsl.rel_angle" class="headerlink"
title="Link to this definition"></a>  
Calculate the relative angle between two vector sets.

Parameters<span class="colon">:</span>  
- **vec_set1** (*array\[array\]*) – an array of two vectors

- **vec_set2** (*array\[array\]*) – second array of two vectors

<!-- -->

<span class="sig-name descname"><span class="pre">rel_strain</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">vec1</span></span>*, *<span class="n"><span class="pre">vec2</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/interfaces/zsl.py#L245-L248"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.interfaces.zsl.rel_strain"
class="headerlink" title="Link to this definition"></a>  
Calculate relative strain between two vectors.

<!-- -->

<span class="sig-name descname"><span class="pre">vec_angle</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">a</span></span>*, *<span class="n"><span class="pre">b</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/interfaces/zsl.py#L273-L278"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.interfaces.zsl.vec_angle" class="headerlink"
title="Link to this definition"></a>  
Calculate angle between two vectors.

<!-- -->

<span class="sig-name descname"><span class="pre">vec_area</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">a</span></span>*, *<span class="n"><span class="pre">b</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/interfaces/zsl.py#L281-L284"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.interfaces.zsl.vec_area" class="headerlink"
title="Link to this definition"></a>  
Area of lattice plane defined by two vectors.

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
