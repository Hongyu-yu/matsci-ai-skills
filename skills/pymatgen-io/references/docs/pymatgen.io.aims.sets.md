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

- <a href="#" class="reference internal">pymatgen.io.aims.sets package</a>
  - <a href="#submodules" class="reference internal">Submodules</a>
  - <a href="#module-pymatgen.io.aims.sets.base"
    class="reference internal">pymatgen.io.aims.sets.base module</a>
    - <a href="#pymatgen.io.aims.sets.base.AimsInputGenerator"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">AimsInputGenerator</code></span></a>
      - <a href="#pymatgen.io.aims.sets.base.AimsInputGenerator.user_params"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputGenerator.user_params</code></span></a>
      - <a
        href="#pymatgen.io.aims.sets.base.AimsInputGenerator.user_kpoints_settings"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputGenerator.user_kpoints_settings</code></span></a>
      - <a
        href="#pymatgen.io.aims.sets.base.AimsInputGenerator.use_structure_charge"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputGenerator.use_structure_charge</code></span></a>
      - <a href="#pymatgen.io.aims.sets.base.AimsInputGenerator.d2k"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputGenerator.d2k()</code></span></a>
      - <a href="#pymatgen.io.aims.sets.base.AimsInputGenerator.d2k_recip_cell"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputGenerator.d2k_recip_cell()</code></span></a>
      - <a href="#pymatgen.io.aims.sets.base.AimsInputGenerator.get_input_set"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputGenerator.get_input_set()</code></span></a>
      - <a
        href="#pymatgen.io.aims.sets.base.AimsInputGenerator.get_parameter_updates"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputGenerator.get_parameter_updates()</code></span></a>
      - <a href="#pymatgen.io.aims.sets.base.AimsInputGenerator.k2d"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputGenerator.k2d()</code></span></a>
      - <a href="#id0" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputGenerator.use_structure_charge</code></span></a>
      - <a href="#id1" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputGenerator.user_kpoints_settings</code></span></a>
      - <a href="#id2" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputGenerator.user_params</code></span></a>
    - <a href="#pymatgen.io.aims.sets.base.AimsInputSet"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">AimsInputSet</code></span></a>
      - <a href="#pymatgen.io.aims.sets.base.AimsInputSet.control_in"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputSet.control_in</code></span></a>
      - <a href="#pymatgen.io.aims.sets.base.AimsInputSet.geometry_in"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputSet.geometry_in</code></span></a>
      - <a href="#pymatgen.io.aims.sets.base.AimsInputSet.get_input_files"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputSet.get_input_files()</code></span></a>
      - <a href="#pymatgen.io.aims.sets.base.AimsInputSet.params_json"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputSet.params_json</code></span></a>
      - <a href="#pymatgen.io.aims.sets.base.AimsInputSet.remove_parameters"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputSet.remove_parameters()</code></span></a>
      - <a href="#pymatgen.io.aims.sets.base.AimsInputSet.set_parameters"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputSet.set_parameters()</code></span></a>
      - <a href="#pymatgen.io.aims.sets.base.AimsInputSet.set_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputSet.set_structure()</code></span></a>
    - <a href="#pymatgen.io.aims.sets.base.recursive_update"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">recursive_update()</code></span></a>
  - <a href="#module-pymatgen.io.aims.sets.bs"
    class="reference internal">pymatgen.io.aims.sets.bs module</a>
    - <a href="#pymatgen.io.aims.sets.bs.BandStructureSetGenerator"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">BandStructureSetGenerator</code></span></a>
      - <a href="#pymatgen.io.aims.sets.bs.BandStructureSetGenerator.calc_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructureSetGenerator.calc_type</code></span></a>
      - <a
        href="#pymatgen.io.aims.sets.bs.BandStructureSetGenerator.k_point_density"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructureSetGenerator.k_point_density</code></span></a>
      - <a href="#id3" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructureSetGenerator.calc_type</code></span></a>
      - <a
        href="#pymatgen.io.aims.sets.bs.BandStructureSetGenerator.get_parameter_updates"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructureSetGenerator.get_parameter_updates()</code></span></a>
      - <a href="#id4" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructureSetGenerator.k_point_density</code></span></a>
    - <a href="#pymatgen.io.aims.sets.bs.GWSetGenerator"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">GWSetGenerator</code></span></a>
      - <a href="#pymatgen.io.aims.sets.bs.GWSetGenerator.calc_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GWSetGenerator.calc_type</code></span></a>
      - <a href="#pymatgen.io.aims.sets.bs.GWSetGenerator.k_point_density"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GWSetGenerator.k_point_density</code></span></a>
      - <a href="#id5" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GWSetGenerator.calc_type</code></span></a>
      - <a href="#pymatgen.io.aims.sets.bs.GWSetGenerator.get_parameter_updates"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GWSetGenerator.get_parameter_updates()</code></span></a>
      - <a href="#id6" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GWSetGenerator.k_point_density</code></span></a>
    - <a href="#pymatgen.io.aims.sets.bs.prepare_band_input"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">prepare_band_input()</code></span></a>
  - <a href="#module-pymatgen.io.aims.sets.core"
    class="reference internal">pymatgen.io.aims.sets.core module</a>
    - <a href="#pymatgen.io.aims.sets.core.MDSetGenerator"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">MDSetGenerator</code></span></a>
      - <a href="#pymatgen.io.aims.sets.core.MDSetGenerator.calc_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MDSetGenerator.calc_type</code></span></a>
      - <a href="#pymatgen.io.aims.sets.core.MDSetGenerator.ensemble"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MDSetGenerator.ensemble</code></span></a>
      - <a href="#pymatgen.io.aims.sets.core.MDSetGenerator.ensemble_specs"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MDSetGenerator.ensemble_specs</code></span></a>
      - <a
        href="#pymatgen.io.aims.sets.core.MDSetGenerator.get_parameter_updates"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MDSetGenerator.get_parameter_updates()</code></span></a>
      - <a href="#pymatgen.io.aims.sets.core.MDSetGenerator.init_velocities"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MDSetGenerator.init_velocities</code></span></a>
      - <a href="#pymatgen.io.aims.sets.core.MDSetGenerator.temp"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MDSetGenerator.temp</code></span></a>
      - <a href="#pymatgen.io.aims.sets.core.MDSetGenerator.time"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MDSetGenerator.time</code></span></a>
      - <a href="#pymatgen.io.aims.sets.core.MDSetGenerator.time_step"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MDSetGenerator.time_step</code></span></a>
    - <a href="#pymatgen.io.aims.sets.core.RelaxSetGenerator"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">RelaxSetGenerator</code></span></a>
      - <a href="#pymatgen.io.aims.sets.core.RelaxSetGenerator.calc_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RelaxSetGenerator.calc_type</code></span></a>
      - <a href="#pymatgen.io.aims.sets.core.RelaxSetGenerator.relax_cell"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RelaxSetGenerator.relax_cell</code></span></a>
      - <a href="#pymatgen.io.aims.sets.core.RelaxSetGenerator.max_force"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RelaxSetGenerator.max_force</code></span></a>
      - <a href="#pymatgen.io.aims.sets.core.RelaxSetGenerator.method"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RelaxSetGenerator.method</code></span></a>
      - <a href="#id7" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RelaxSetGenerator.calc_type</code></span></a>
      - <a
        href="#pymatgen.io.aims.sets.core.RelaxSetGenerator.get_parameter_updates"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RelaxSetGenerator.get_parameter_updates()</code></span></a>
      - <a href="#id8" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RelaxSetGenerator.max_force</code></span></a>
      - <a href="#id9" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RelaxSetGenerator.method</code></span></a>
      - <a href="#id10" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RelaxSetGenerator.relax_cell</code></span></a>
    - <a href="#pymatgen.io.aims.sets.core.SocketIOSetGenerator"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">SocketIOSetGenerator</code></span></a>
      - <a href="#pymatgen.io.aims.sets.core.SocketIOSetGenerator.calc_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SocketIOSetGenerator.calc_type</code></span></a>
      - <a href="#pymatgen.io.aims.sets.core.SocketIOSetGenerator.host"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SocketIOSetGenerator.host</code></span></a>
      - <a href="#pymatgen.io.aims.sets.core.SocketIOSetGenerator.port"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SocketIOSetGenerator.port</code></span></a>
      - <a href="#id11" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SocketIOSetGenerator.calc_type</code></span></a>
      - <a
        href="#pymatgen.io.aims.sets.core.SocketIOSetGenerator.get_parameter_updates"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SocketIOSetGenerator.get_parameter_updates()</code></span></a>
      - <a href="#id12" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SocketIOSetGenerator.host</code></span></a>
      - <a href="#id13" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SocketIOSetGenerator.port</code></span></a>
    - <a href="#pymatgen.io.aims.sets.core.StaticSetGenerator"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">StaticSetGenerator</code></span></a>
      - <a href="#pymatgen.io.aims.sets.core.StaticSetGenerator.calc_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">StaticSetGenerator.calc_type</code></span></a>
      - <a href="#id14" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">StaticSetGenerator.calc_type</code></span></a>
      - <a
        href="#pymatgen.io.aims.sets.core.StaticSetGenerator.get_parameter_updates"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">StaticSetGenerator.get_parameter_updates()</code></span></a>
  - <a href="#module-pymatgen.io.aims.sets.magnetism"
    class="reference internal">pymatgen.io.aims.sets.magnetism module</a>
    - <a href="#pymatgen.io.aims.sets.magnetism.MagneticRelaxSetGenerator"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">MagneticRelaxSetGenerator</code></span></a>
      - <a
        href="#pymatgen.io.aims.sets.magnetism.MagneticRelaxSetGenerator.calc_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MagneticRelaxSetGenerator.calc_type</code></span></a>
      - <a
        href="#pymatgen.io.aims.sets.magnetism.MagneticRelaxSetGenerator.relax_cell"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MagneticRelaxSetGenerator.relax_cell</code></span></a>
      - <a
        href="#pymatgen.io.aims.sets.magnetism.MagneticRelaxSetGenerator.max_force"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MagneticRelaxSetGenerator.max_force</code></span></a>
      - <a
        href="#pymatgen.io.aims.sets.magnetism.MagneticRelaxSetGenerator.method"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MagneticRelaxSetGenerator.method</code></span></a>
      - <a
        href="#pymatgen.io.aims.sets.magnetism.MagneticRelaxSetGenerator.get_parameter_updates"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MagneticRelaxSetGenerator.get_parameter_updates()</code></span></a>
    - <a href="#pymatgen.io.aims.sets.magnetism.MagneticStaticSetGenerator"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">MagneticStaticSetGenerator</code></span></a>
      - <a
        href="#pymatgen.io.aims.sets.magnetism.MagneticStaticSetGenerator.calc_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MagneticStaticSetGenerator.calc_type</code></span></a>
      - <a href="#id15" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MagneticStaticSetGenerator.calc_type</code></span></a>
      - <a
        href="#pymatgen.io.aims.sets.magnetism.MagneticStaticSetGenerator.get_parameter_updates"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MagneticStaticSetGenerator.get_parameter_updates()</code></span></a>

</div>

</div>

</div>

<div class="section wy-nav-content-wrap" toggle="wy-nav-shift">

[pymatgen](index.html)

<div class="wy-nav-content">

<div class="rst-content style-external-links">

<div role="navigation" aria-label="Page navigation">

- <a href="index.html" class="icon icon-home" aria-label="Home"></a>
- pymatgen.io.aims.sets package
- <a
  href="https://github.com/materialsproject/pymatgen/blob/master/docs_rst/pymatgen.io.aims.sets.rst"
  class="fa fa-github">Edit on GitHub</a>

------------------------------------------------------------------------

</div>

<div class="document" role="main" itemscope="itemscope"
itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="module-pymatgen.io.aims.sets" class="section">

<span id="pymatgen-io-aims-sets-package"></span>

# pymatgen.io.aims.sets package<a href="#module-pymatgen.io.aims.sets" class="headerlink"
title="Link to this heading"></a>

<div id="submodules" class="section">

## Submodules<a href="#submodules" class="headerlink"
title="Link to this heading"></a>

</div>

<div id="module-pymatgen.io.aims.sets.base" class="section">

<span id="pymatgen-io-aims-sets-base-module"></span>

## pymatgen.io.aims.sets.base module<a href="#module-pymatgen.io.aims.sets.base" class="headerlink"
title="Link to this heading"></a>

Module defining base FHI-aims input set and generator.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">AimsInputGenerator</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">user_params:</span> <span class="pre">dict\[str</span></span>*, *<span class="n"><span class="pre">\~typing.Any\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">user_kpoints_settings:</span> <span class="pre">dict\[str</span></span>*, *<span class="n"><span class="pre">\~typing.Any\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">use_structure_charge:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/sets/base.py#L189-L447"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.base.AimsInputGenerator"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="pymatgen.io.html#pymatgen.io.core.InputGenerator"
class="reference internal" title="pymatgen.io.core.InputGenerator"><span
class="pre"><code
class="sourceCode python">InputGenerator</code></span></a>

A class to generate Aims input sets.

<span class="sig-name descname"><span class="pre">user_params</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/base.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.base.AimsInputGenerator.user_params"
class="headerlink" title="Link to this definition"></a>  
Updates the default parameters for the FHI-aims calculator

Type<span class="colon">:</span>  
dict\[str, Any\]

<span class="sig-name descname"><span class="pre">user_kpoints_settings</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/base.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.aims.sets.base.AimsInputGenerator.user_kpoints_settings"
class="headerlink" title="Link to this definition"></a>  
The settings used to create the k-grid parameters for FHI-aims

Type<span class="colon">:</span>  
dict\[str, Any\]

<span class="sig-name descname"><span class="pre">use_structure_charge</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/base.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.aims.sets.base.AimsInputGenerator.use_structure_charge"
class="headerlink" title="Link to this definition"></a>  
If set to True, then the overall charge of the structure
(structure.charge) is used to set the charge variable in the control.in.
Default is False.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">d2k</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.IStructure"
class="reference internal"
title="pymatgen.core.structure.IStructure"><span
class="pre">IStructure</span></a></span>*, *<span class="n"><span class="pre">kpt_density</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">5.0</span></span>*, *<span class="n"><span class="pre">even</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Iterable</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/sets/base.py#L376-L397"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.base.AimsInputGenerator.d2k"
class="headerlink" title="Link to this definition"></a>  
Convert k-point density to Monkhorst-Pack grid size.

inspired by \[ase.calculators.calculator.kptdensity2monkhorstpack\]

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  Contains unit cell and information about boundary conditions.

- **kpt_density** (*float* *\|* *list\[float\]*) – Required k-point
  density. Default value is 5.0 point per Ang^-1.

- **even** (*bool*) – Round up to even numbers.

Returns<span class="colon">:</span>  
Monkhorst-Pack grid size in all directions

Return type<span class="colon">:</span>  
dict

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">d2k_recip_cell</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">recip_cell</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">np.ndarray</span></span>*, *<span class="n"><span class="pre">pbc</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">bool</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">kpt_density</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">5.0</span></span>*, *<span class="n"><span class="pre">even</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/sets/base.py#L415-L447"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.base.AimsInputGenerator.d2k_recip_cell"
class="headerlink" title="Link to this definition"></a>  
Convert k-point density to Monkhorst-Pack grid size.

Parameters<span class="colon">:</span>  
- **recip_cell**
  (<a href="pymatgen.io.cp2k.html#pymatgen.io.cp2k.inputs.Cell"
  class="reference internal"
  title="pymatgen.io.cp2k.inputs.Cell"><em>Cell</em></a>) – The
  reciprocal cell

- **pbc** (*Sequence\[bool\]*) – If element of pbc is True then system
  is periodic in that direction

- **kpt_density** (*float* *or* *list\[floats\]*) – Required k-point
  density. Default value is 5 points per Ang^-1.

even(bool): Round up to even numbers.

Returns<span class="colon">:</span>  
Monkhorst-Pack grid size in all directions

Return type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">get_input_set</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">prev_dir</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">properties</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.aims.sets.base.AimsInputSet"
class="reference internal"
title="pymatgen.io.aims.sets.base.AimsInputSet"><span
class="pre">AimsInputSet</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/sets/base.py#L208-L235"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.base.AimsInputGenerator.get_input_set"
class="headerlink" title="Link to this definition"></a>  
Generate an AimsInputSet object.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a> *or*
  <a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
  class="reference internal"
  title="pymatgen.core.structure.Molecule"><em>Molecule</em></a>) –
  Structure or Molecule to generate the input set for.

- **prev_dir** (*str* *or* *Path*) – Path to the previous working
  directory

- **properties** (*list\[str\]*) – System properties that are being
  calculated

Returns<span class="colon">:</span>  
The input set for the calculation of structure

Return type<span class="colon">:</span>  
<a href="#pymatgen.io.aims.sets.base.AimsInputSet"
class="reference internal"
title="pymatgen.io.aims.sets.base.AimsInputSet">AimsInputSet</a>

<span class="sig-name descname"><span class="pre">get_parameter_updates</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">prev_parameters</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/sets/base.py#L360-L374"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.aims.sets.base.AimsInputGenerator.get_parameter_updates"
class="headerlink" title="Link to this definition"></a>  
Update the parameters for a given calculation type.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a> *or*
  <a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
  class="reference internal"
  title="pymatgen.core.structure.Molecule"><em>Molecule</em></a>) – The
  system to run

- **prev_parameters** (*dict\[str,* *Any\]*) – Previous calculation
  parameters.

Returns<span class="colon">:</span>  
A dictionary of updates to apply.

Return type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">k2d</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.IStructure"
class="reference internal"
title="pymatgen.core.structure.IStructure"><span
class="pre">IStructure</span></a></span>*, *<span class="n"><span class="pre">k_grid</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">np.ndarray</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/sets/base.py#L399-L413"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.base.AimsInputGenerator.k2d"
class="headerlink" title="Link to this definition"></a>  
Generate the kpoint density in each direction from given k_grid.

Parameters<span class="colon">:</span>  
- **structure** – Structure Contains unit cell and information about
  boundary conditions.

- **k_grid** – np.ndarray\[int\] k_grid that was used.

Returns<span class="colon">:</span>  
Density of kpoints in each direction. result.mean() computes average
density

Return type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">use_structure_charge</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">False</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/base.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id0" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">user_kpoints_settings</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/base.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id1" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">user_params</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/base.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id2" class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">AimsInputSet</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">parameters</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">properties</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">('energy',</span> <span class="pre">'free_energy')</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/sets/base.py#L44-L186"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.base.AimsInputSet" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="pymatgen.io.html#pymatgen.io.core.InputSet"
class="reference internal" title="pymatgen.io.core.InputSet"><span
class="pre"><code class="sourceCode python">InputSet</code></span></a>

A class to represent a set of Aims inputs.

Construct the AimsInputSet.

Parameters<span class="colon">:</span>  
- **parameters** (*dict\[str,* *Any\]*) – The ASE parameters object for
  the calculation

- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a> *or*
  <a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
  class="reference internal"
  title="pymatgen.core.structure.Molecule"><em>Molecule</em></a>) – The
  Structure/Molecule objects to create the inputs for

- **properties** (*Sequence\[str\]*) – The properties to calculate for
  the calculation

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">control_in</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">slice</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.io.html#pymatgen.io.core.InputFile"
class="reference internal" title="pymatgen.io.core.InputFile"><span
class="pre">InputFile</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/base.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.base.AimsInputSet.control_in"
class="headerlink" title="Link to this definition"></a>  
The control.in file contents.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">geometry_in</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">slice</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.io.html#pymatgen.io.core.InputFile"
class="reference internal" title="pymatgen.io.core.InputFile"><span
class="pre">InputFile</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/base.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.base.AimsInputSet.geometry_in"
class="headerlink" title="Link to this definition"></a>  
The geometry.in file contents.

<span class="sig-name descname"><span class="pre">get_input_files</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/sets/base.py#L74-L97"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.base.AimsInputSet.get_input_files"
class="headerlink" title="Link to this definition"></a>  
Get the input file contents for the calculation.

Returns<span class="colon">:</span>  
The contents of the control.in and geometry.in file

Return type<span class="colon">:</span>  
tuple\[str, str\]

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">params_json</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">slice</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.io.html#pymatgen.io.core.InputFile"
class="reference internal" title="pymatgen.io.core.InputFile"><span
class="pre">InputFile</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/base.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.base.AimsInputSet.params_json"
class="headerlink" title="Link to this definition"></a>  
The JSON representation of the parameters dict.

<span class="sig-name descname"><span class="pre">remove_parameters</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">keys</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Iterable</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">str</span></span>*, *<span class="n"><span class="pre">strict</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/sets/base.py#L143-L171"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.base.AimsInputSet.remove_parameters"
class="headerlink" title="Link to this definition"></a>  
Remove the aims parameters listed in keys.

This removes the aims variables from the parameters object.

Parameters<span class="colon">:</span>  
- **keys** (*Iterable\[str\] or* *str*) – string or list of strings with
  the names of the aims parameters to be removed.

- **strict** (*bool*) – whether to raise a KeyError if one of the aims
  parameters to be removed is not present.

Returns<span class="colon">:</span>  
Dictionary with the variables that have been removed.

Return type<span class="colon">:</span>  
dict\[str, Any\]

<span class="sig-name descname"><span class="pre">set_parameters</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*</span></span><span class="n"><span class="pre">args</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/sets/base.py#L114-L141"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.base.AimsInputSet.set_parameters"
class="headerlink" title="Link to this definition"></a>  
Set the parameters object for the AimsTemplate.

This sets the parameters object that is passed to an AimsTemplate and
resets the control.in file

One can pass a dictionary mapping the aims variables to their values or
the aims variables as keyword arguments. A combination of the two
options is also allowed.

Returns<span class="colon">:</span>  
dictionary with the variables that have been added.

Return type<span class="colon">:</span>  
dict\[str, Any\]

<span class="sig-name descname"><span class="pre">set_structure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/sets/base.py#L173-L186"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.base.AimsInputSet.set_structure"
class="headerlink" title="Link to this definition"></a>  
Set the structure object for this input set.

Parameters<span class="colon">:</span>  
**structure**
(<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><em>Structure</em></a> *or*
<a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><em>Molecule</em></a>) – The
new Structure or Molecule for the calculation

<!-- -->

<span class="sig-name descname"><span class="pre">recursive_update</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*, *<span class="n"><span class="pre">up</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/sets/base.py#L450-L475"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.base.recursive_update"
class="headerlink" title="Link to this definition"></a>  
Update a dictionary recursively and return it.

Parameters<span class="colon">:</span>  
- **dct** (*dict*) – Input dictionary to modify

- **up** (*dict*) – updates to apply

Returns<span class="colon">:</span>  
The updated dictionary.

Return type<span class="colon">:</span>  
dict

Example

d = {‘activate_hybrid’: {“hybrid_functional”: “HSE06”}} u =
{‘activate_hybrid’: {“cutoff_radius”: 8}}

yields {‘activate_hybrid’: {“hybrid_functional”: “HSE06”,
“cutoff_radius”: 8}}}

</div>

<div id="module-pymatgen.io.aims.sets.bs" class="section">

<span id="pymatgen-io-aims-sets-bs-module"></span>

## pymatgen.io.aims.sets.bs module<a href="#module-pymatgen.io.aims.sets.bs" class="headerlink"
title="Link to this heading"></a>

Input sets for band structure calculations.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">BandStructureSetGenerator</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">user_params:</span> <span class="pre">dict\[str</span></span>*, *<span class="n"><span class="pre">Any\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">user_kpoints_settings:</span> <span class="pre">dict\[str</span></span>*, *<span class="n"><span class="pre">Any\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">use_structure_charge:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">calc_type:</span> <span class="pre">str</span> <span class="pre">=</span> <span class="pre">'bands'</span></span>*, *<span class="n"><span class="pre">k_point_density:</span> <span class="pre">float</span> <span class="pre">=</span> <span class="pre">20</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/sets/bs.py#L63-L92"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.bs.BandStructureSetGenerator"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.aims.sets.base.AimsInputGenerator"
class="reference internal"
title="pymatgen.io.aims.sets.base.AimsInputGenerator"><span
class="pre"><code
class="sourceCode python">AimsInputGenerator</code></span></a>

A generator for the band structure calculation input set.

<span class="sig-name descname"><span class="pre">calc_type</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/bs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.bs.BandStructureSetGenerator.calc_type"
class="headerlink" title="Link to this definition"></a>  
The type of calculations

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">k_point_density</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/bs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.aims.sets.bs.BandStructureSetGenerator.k_point_density"
class="headerlink" title="Link to this definition"></a>  
The number of k_points per angstrom

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">calc_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'bands'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/bs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id3" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">get_parameter_updates</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">prev_parameters</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/sets/bs.py#L75-L92"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.aims.sets.bs.BandStructureSetGenerator.get_parameter_updates"
class="headerlink" title="Link to this definition"></a>  
Get the parameter updates for the calculation.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  The structure to calculate the bands for

- **prev_parameters** (*Dict\[str,* *Any\]*) – The previous parameters

Returns<span class="colon">:</span>  
The updated for the parameters for the output section of FHI-aims

Return type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">k_point_density</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">20</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/bs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id4" class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">GWSetGenerator</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">user_params:</span> <span class="pre">dict\[str</span></span>*, *<span class="n"><span class="pre">Any\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">user_kpoints_settings:</span> <span class="pre">dict\[str</span></span>*, *<span class="n"><span class="pre">Any\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">use_structure_charge:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">calc_type:</span> <span class="pre">str</span> <span class="pre">=</span> <span class="pre">'GW'</span></span>*, *<span class="n"><span class="pre">k_point_density:</span> <span class="pre">float</span> <span class="pre">=</span> <span class="pre">20</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/sets/bs.py#L95-L127"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.bs.GWSetGenerator" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.aims.sets.base.AimsInputGenerator"
class="reference internal"
title="pymatgen.io.aims.sets.base.AimsInputGenerator"><span
class="pre"><code
class="sourceCode python">AimsInputGenerator</code></span></a>

A generator for the input set for calculations employing GW self-energy
correction.

<span class="sig-name descname"><span class="pre">calc_type</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/bs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.bs.GWSetGenerator.calc_type"
class="headerlink" title="Link to this definition"></a>  
The type of calculations

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">k_point_density</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/bs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.bs.GWSetGenerator.k_point_density"
class="headerlink" title="Link to this definition"></a>  
The number of k_points per angstrom

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">calc_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'GW'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/bs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id5" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">get_parameter_updates</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">prev_parameters</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/sets/bs.py#L108-L127"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.bs.GWSetGenerator.get_parameter_updates"
class="headerlink" title="Link to this definition"></a>  
Get the parameter updates for the calculation.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a> *or*
  <a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
  class="reference internal"
  title="pymatgen.core.structure.Molecule"><em>Molecule</em></a>) – The
  structure to calculate the bands for

- **prev_parameters** (*Dict\[str,* *Any\]*) – The previous parameters

Returns<span class="colon">:</span>  
The updated for the parameters for the output section of FHI-aims

Return type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">k_point_density</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">20</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/bs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id6" class="headerlink" title="Link to this definition"></a>  

<!-- -->

<span class="sig-name descname"><span class="pre">prepare_band_input</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.IStructure"
class="reference internal"
title="pymatgen.core.structure.IStructure"><span
class="pre">IStructure</span></a></span>*, *<span class="n"><span class="pre">density</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">20</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/sets/bs.py#L25-L60"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.bs.prepare_band_input"
class="headerlink" title="Link to this definition"></a>  
Prepare the band information needed for the FHI-aims control.in file.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  The structure for which the band path is calculated

- **density** (*float*) – Number of kpoints per Angstrom.

</div>

<div id="module-pymatgen.io.aims.sets.core" class="section">

<span id="pymatgen-io-aims-sets-core-module"></span>

## pymatgen.io.aims.sets.core module<a href="#module-pymatgen.io.aims.sets.core" class="headerlink"
title="Link to this heading"></a>

Module defining core FHI-aims input set generators.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">MDSetGenerator</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">user_params:</span> <span class="pre">dict\[str</span></span>*, *<span class="n"><span class="pre">Any\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">user_kpoints_settings:</span> <span class="pre">dict\[str</span></span>*, *<span class="n"><span class="pre">Any\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">use_structure_charge:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">calc_type:</span> <span class="pre">str</span> <span class="pre">=</span> <span class="pre">'md'</span></span>*, *<span class="n"><span class="pre">ensemble:</span> <span class="pre">str</span> <span class="pre">=</span> <span class="pre">'nve'</span></span>*, *<span class="n"><span class="pre">ensemble_specs:</span> <span class="pre">dict\[str</span></span>*, *<span class="n"><span class="pre">Any\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">temp:</span> <span class="pre">float</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">time:</span> <span class="pre">float</span> <span class="pre">=</span> <span class="pre">5.0</span></span>*, *<span class="n"><span class="pre">time_step:</span> <span class="pre">float</span> <span class="pre">=</span> <span class="pre">0.001</span></span>*, *<span class="n"><span class="pre">init_velocities:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/sets/core.py#L110-L202"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.core.MDSetGenerator" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.aims.sets.base.AimsInputGenerator"
class="reference internal"
title="pymatgen.io.aims.sets.base.AimsInputGenerator"><span
class="pre"><code
class="sourceCode python">AimsInputGenerator</code></span></a>

A class for generating FHI-aims input sets for molecular dynamics
calculations.

Parameters<span class="colon">:</span>  
- **ensemble** (*str*) – Molecular dynamics ensemble to run. Options
  include nvt, nve, and gle. Default: nve

- **ensemble_specs** (*dict\[str,* *Any\]*) – A dictionary containing
  the specifications of the molecular dynamics ensemble. Valid keys are
  type (the ensemble type, valid types are defined in \_valid_dynamics
  dict), and parameter - the control parameter for the thermostat (not
  used for nve and nve_4th_order).

- **temp** (*float* *\|* *None*) – Thermostat temperature. Default: None

- **time** (*float*) – Simulation time (in picoseconds). Negative value
  stands for indefinite run. Default: 5 ps

- **time_step** (*float*) – The time step (in picoseconds) for the
  simulation. default: 1 fs

- **\*\*kwargs** – Other keyword arguments that will be passed to <span
  class="pre">`AimsInputGenerator`</span>.

<span class="sig-name descname"><span class="pre">calc_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'md'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.core.MDSetGenerator.calc_type"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">ensemble</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'nve'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.core.MDSetGenerator.ensemble"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">ensemble_specs</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.core.MDSetGenerator.ensemble_specs"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">get_parameter_updates</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">prev_parameters</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/sets/core.py#L144-L202"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.aims.sets.core.MDSetGenerator.get_parameter_updates"
class="headerlink" title="Link to this definition"></a>  
Get the parameter updates for the calculation.

Parameters<span class="colon">:</span>  
- **Molecule)** (*structure* *(Structure or*) – The structure to
  calculate the bands for

- **(Dict\[str** (*prev_parameters*) – The previous parameters

- **Any\])** – The previous parameters

Returns<span class="colon">:</span>  
A dictionary of updates to apply.

Return type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">init_velocities</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">True</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.core.MDSetGenerator.init_velocities"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">temp</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.core.MDSetGenerator.temp"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">time</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">5.0</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.core.MDSetGenerator.time"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">time_step</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">0.001</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.core.MDSetGenerator.time_step"
class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">RelaxSetGenerator</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">user_params:</span> <span class="pre">dict\[str</span></span>*, *<span class="n"><span class="pre">Any\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">user_kpoints_settings:</span> <span class="pre">dict\[str</span></span>*, *<span class="n"><span class="pre">Any\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">use_structure_charge:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">calc_type:</span> <span class="pre">str</span> <span class="pre">=</span> <span class="pre">'relaxation'</span></span>*, *<span class="n"><span class="pre">relax_cell:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">True</span></span>*, *<span class="n"><span class="pre">max_force:</span> <span class="pre">float</span> <span class="pre">=</span> <span class="pre">0.001</span></span>*, *<span class="n"><span class="pre">method:</span> <span class="pre">str</span> <span class="pre">=</span> <span class="pre">'trm'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/sets/core.py#L47-L80"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.core.RelaxSetGenerator"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.aims.sets.base.AimsInputGenerator"
class="reference internal"
title="pymatgen.io.aims.sets.base.AimsInputGenerator"><span
class="pre"><code
class="sourceCode python">AimsInputGenerator</code></span></a>

Generate FHI-aims relax sets for optimizing internal coordinates and
lattice params.

<span class="sig-name descname"><span class="pre">calc_type</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.core.RelaxSetGenerator.calc_type"
class="headerlink" title="Link to this definition"></a>  
The type of calculation

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">relax_cell</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.core.RelaxSetGenerator.relax_cell"
class="headerlink" title="Link to this definition"></a>  
If True then relax the unit cell from the structure

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">max_force</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.core.RelaxSetGenerator.max_force"
class="headerlink" title="Link to this definition"></a>  
Maximum allowed force in the calculation

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">method</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.core.RelaxSetGenerator.method"
class="headerlink" title="Link to this definition"></a>  
Method used for the geometry optimization

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">calc_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'relaxation'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id7" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">get_parameter_updates</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">prev_parameters</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/sets/core.py#L63-L80"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.aims.sets.core.RelaxSetGenerator.get_parameter_updates"
class="headerlink" title="Link to this definition"></a>  
Get the parameter updates for the calculation.

Parameters<span class="colon">:</span>  
**structure**
(<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><em>Structure</em></a> *or*
<a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><em>Molecule</em></a>) – The
structure to calculate the bands for

prev_parameters (Dict\[str, Any\]): The previous parameters

Returns<span class="colon">:</span>  
The updated for the parameters for the output section of FHI-aims

Return type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">max_force</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">0.001</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id8" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">method</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'trm'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id9" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">relax_cell</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">True</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id10" class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">SocketIOSetGenerator</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">user_params:</span> <span class="pre">dict\[str</span></span>*, *<span class="n"><span class="pre">Any\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">user_kpoints_settings:</span> <span class="pre">dict\[str</span></span>*, *<span class="n"><span class="pre">Any\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">use_structure_charge:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">calc_type:</span> <span class="pre">str</span> <span class="pre">=</span> <span class="pre">'multi_scf'</span></span>*, *<span class="n"><span class="pre">host:</span> <span class="pre">str</span> <span class="pre">=</span> <span class="pre">'localhost'</span></span>*, *<span class="n"><span class="pre">port:</span> <span class="pre">int</span> <span class="pre">=</span> <span class="pre">12345</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/sets/core.py#L83-L107"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.core.SocketIOSetGenerator"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.aims.sets.base.AimsInputGenerator"
class="reference internal"
title="pymatgen.io.aims.sets.base.AimsInputGenerator"><span
class="pre"><code
class="sourceCode python">AimsInputGenerator</code></span></a>

Generate FHI-aims input sets for running with the socket.

<span class="sig-name descname"><span class="pre">calc_type</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.core.SocketIOSetGenerator.calc_type"
class="headerlink" title="Link to this definition"></a>  
The type of calculation

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">host</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.core.SocketIOSetGenerator.host"
class="headerlink" title="Link to this definition"></a>  
The hostname for the server the socket is on

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">port</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.core.SocketIOSetGenerator.port"
class="headerlink" title="Link to this definition"></a>  
The port the socket server is listening on

Type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">calc_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'multi_scf'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id11" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">get_parameter_updates</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">prev_parameters</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/sets/core.py#L97-L107"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.aims.sets.core.SocketIOSetGenerator.get_parameter_updates"
class="headerlink" title="Link to this definition"></a>  
Get the parameter updates for the calculation.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a> *or*
  <a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
  class="reference internal"
  title="pymatgen.core.structure.Molecule"><em>Molecule</em></a>) – The
  structure to calculate the bands for

- **prev_parameters** (*Dict\[str,* *Any\]*) – The previous parameters

Returns<span class="colon">:</span>  
The updated for the parameters for the output section of FHI-aims

Return type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">host</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'localhost'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id12" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">port</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">12345</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id13" class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">StaticSetGenerator</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">user_params:</span> <span class="pre">dict\[str</span></span>*, *<span class="n"><span class="pre">Any\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">user_kpoints_settings:</span> <span class="pre">dict\[str</span></span>*, *<span class="n"><span class="pre">Any\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">use_structure_charge:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">calc_type:</span> <span class="pre">str</span> <span class="pre">=</span> <span class="pre">'static'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/sets/core.py#L24-L44"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.core.StaticSetGenerator"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.aims.sets.base.AimsInputGenerator"
class="reference internal"
title="pymatgen.io.aims.sets.base.AimsInputGenerator"><span
class="pre"><code
class="sourceCode python">AimsInputGenerator</code></span></a>

Common class for ground-state generators.

<span class="sig-name descname"><span class="pre">calc_type</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.core.StaticSetGenerator.calc_type"
class="headerlink" title="Link to this definition"></a>  
The type of calculation

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">calc_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'static'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id14" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">get_parameter_updates</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">prev_parameters</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/sets/core.py#L34-L44"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.aims.sets.core.StaticSetGenerator.get_parameter_updates"
class="headerlink" title="Link to this definition"></a>  
Get the parameter updates for the calculation.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a> *or*
  <a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
  class="reference internal"
  title="pymatgen.core.structure.Molecule"><em>Molecule</em></a>) – The
  structure to calculate the bands for

- **prev_parameters** (*Dict\[str,* *Any\]*) – The previous parameters

Returns<span class="colon">:</span>  
The updated for the parameters for the output section of FHI-aims

Return type<span class="colon">:</span>  
dict

</div>

<div id="module-pymatgen.io.aims.sets.magnetism" class="section">

<span id="pymatgen-io-aims-sets-magnetism-module"></span>

## pymatgen.io.aims.sets.magnetism module<a href="#module-pymatgen.io.aims.sets.magnetism" class="headerlink"
title="Link to this heading"></a>

Define the InputSetGenerators for FHI-aims magnetism calculations.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">MagneticRelaxSetGenerator</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">user_params:</span> <span class="pre">dict\[str</span></span>*, *<span class="n"><span class="pre">Any\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">user_kpoints_settings:</span> <span class="pre">dict\[str</span></span>*, *<span class="n"><span class="pre">Any\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">use_structure_charge:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">calc_type:</span> <span class="pre">str</span> <span class="pre">=</span> <span class="pre">'relaxation'</span></span>*, *<span class="n"><span class="pre">relax_cell:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">True</span></span>*, *<span class="n"><span class="pre">max_force:</span> <span class="pre">float</span> <span class="pre">=</span> <span class="pre">0.001</span></span>*, *<span class="n"><span class="pre">method:</span> <span class="pre">str</span> <span class="pre">=</span> <span class="pre">'trm'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/sets/magnetism.py#L44-L71"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.magnetism.MagneticRelaxSetGenerator"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.aims.sets.core.RelaxSetGenerator"
class="reference internal"
title="pymatgen.io.aims.sets.core.RelaxSetGenerator"><span
class="pre"><code
class="sourceCode python">RelaxSetGenerator</code></span></a>

Generate FHI-aims relax sets for optimizing internal coordinates and
lattice params.

<span class="sig-name descname"><span class="pre">calc_type</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/magnetism.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.aims.sets.magnetism.MagneticRelaxSetGenerator.calc_type"
class="headerlink" title="Link to this definition"></a>  
The type of calculation

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">relax_cell</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/magnetism.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.aims.sets.magnetism.MagneticRelaxSetGenerator.relax_cell"
class="headerlink" title="Link to this definition"></a>  
If True then relax the unit cell from the structure

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">max_force</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/magnetism.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.aims.sets.magnetism.MagneticRelaxSetGenerator.max_force"
class="headerlink" title="Link to this definition"></a>  
Maximum allowed force in the calculation

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">method</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/magnetism.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.aims.sets.magnetism.MagneticRelaxSetGenerator.method"
class="headerlink" title="Link to this definition"></a>  
Method used for the geometry optimization

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">get_parameter_updates</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">prev_parameters</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/sets/magnetism.py#L55-L71"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.aims.sets.magnetism.MagneticRelaxSetGenerator.get_parameter_updates"
class="headerlink" title="Link to this definition"></a>  
Get the parameter updates for the calculation.

Parameters<span class="colon">:</span>  
**structure**
(<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><em>Structure</em></a> *or*
<a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><em>Molecule</em></a>) – The
structure to calculate the bands for

prev_parameters (Dict\[str, Any\]): The previous parameters

Returns<span class="colon">:</span>  
The updated for the parameters for the output section of FHI-aims

Return type<span class="colon">:</span>  
dict

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">MagneticStaticSetGenerator</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">user_params:</span> <span class="pre">dict\[str</span></span>*, *<span class="n"><span class="pre">Any\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">user_kpoints_settings:</span> <span class="pre">dict\[str</span></span>*, *<span class="n"><span class="pre">Any\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">use_structure_charge:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">calc_type:</span> <span class="pre">str</span> <span class="pre">=</span> <span class="pre">'static'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/sets/magnetism.py#L16-L41"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.sets.magnetism.MagneticStaticSetGenerator"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.aims.sets.core.StaticSetGenerator"
class="reference internal"
title="pymatgen.io.aims.sets.core.StaticSetGenerator"><span
class="pre"><code
class="sourceCode python">StaticSetGenerator</code></span></a>

Common class for ground-state generators.

<span class="sig-name descname"><span class="pre">calc_type</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/magnetism.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.aims.sets.magnetism.MagneticStaticSetGenerator.calc_type"
class="headerlink" title="Link to this definition"></a>  
The type of calculation

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">calc_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'static'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/sets/magnetism.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id15" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">get_parameter_updates</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">prev_parameters</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/sets/magnetism.py#L26-L41"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.aims.sets.magnetism.MagneticStaticSetGenerator.get_parameter_updates"
class="headerlink" title="Link to this definition"></a>  
Get the parameter updates for the calculation.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a> *or*
  <a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
  class="reference internal"
  title="pymatgen.core.structure.Molecule"><em>Molecule</em></a>) – The
  structure to calculate the bands for

- **prev_parameters** (*Dict\[str,* *Any\]*) – The previous parameters

Returns<span class="colon">:</span>  
The updated for the parameters for the output section of FHI-aims

Return type<span class="colon">:</span>  
dict

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
