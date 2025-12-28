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

- <a href="#" class="reference internal">pymatgen.io.qchem package</a>
  - <a href="#submodules" class="reference internal">Submodules</a>
  - <a href="#module-pymatgen.io.qchem.inputs"
    class="reference internal">pymatgen.io.qchem.inputs module</a>
    - <a href="#pymatgen.io.qchem.inputs.QCInput"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">QCInput</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.almo_template"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.almo_template()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.cdft_template"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.cdft_template()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.find_sections"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.find_sections()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.from_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.from_file()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.from_multi_jobs_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.from_multi_jobs_file()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.from_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.from_str()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.geom_opt_template"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.geom_opt_template()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.get_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.get_str()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.molecule_template"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.molecule_template()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.multi_job_string"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.multi_job_string()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.nbo_template"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.nbo_template()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.opt_template"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.opt_template()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.pcm_nonels_template"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.pcm_nonels_template()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.pcm_template"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.pcm_template()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.plots_template"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.plots_template()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.read_almo"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.read_almo()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.read_cdft"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.read_cdft()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.read_geom_opt"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.read_geom_opt()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.read_molecule"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.read_molecule()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.read_nbo"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.read_nbo()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.read_opt"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.read_opt()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.read_pcm"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.read_pcm()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.read_pcm_nonels"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.read_pcm_nonels()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.read_plots"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.read_plots()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.read_rem"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.read_rem()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.read_scan"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.read_scan()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.read_smx"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.read_smx()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.read_solvent"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.read_solvent()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.read_svp"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.read_svp()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.read_vdw"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.read_vdw()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.rem_template"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.rem_template()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.scan_template"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.scan_template()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.smx_template"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.smx_template()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.solvent_template"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.solvent_template()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.svp_template"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.svp_template()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.van_der_waals_template"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.van_der_waals_template()</code></span></a>
      - <a href="#pymatgen.io.qchem.inputs.QCInput.write_multi_job_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCInput.write_multi_job_file()</code></span></a>
  - <a href="#module-pymatgen.io.qchem.outputs"
    class="reference internal">pymatgen.io.qchem.outputs module</a>
    - <a href="#pymatgen.io.qchem.outputs.QCOutput"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">QCOutput</code></span></a>
      - <a href="#pymatgen.io.qchem.outputs.QCOutput.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCOutput.as_dict()</code></span></a>
      - <a href="#pymatgen.io.qchem.outputs.QCOutput.multiple_outputs_from_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QCOutput.multiple_outputs_from_file()</code></span></a>
    - <a href="#pymatgen.io.qchem.outputs.check_for_structure_changes"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">check_for_structure_changes()</code></span></a>
    - <a href="#pymatgen.io.qchem.outputs.get_percentage"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">get_percentage()</code></span></a>
    - <a href="#pymatgen.io.qchem.outputs.gradient_parser"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">gradient_parser()</code></span></a>
    - <a href="#pymatgen.io.qchem.outputs.hessian_parser"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">hessian_parser()</code></span></a>
    - <a href="#pymatgen.io.qchem.outputs.jump_to_header"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">jump_to_header()</code></span></a>
    - <a href="#pymatgen.io.qchem.outputs.nbo_parser"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">nbo_parser()</code></span></a>
    - <a href="#pymatgen.io.qchem.outputs.orbital_coeffs_parser"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">orbital_coeffs_parser()</code></span></a>
    - <a href="#pymatgen.io.qchem.outputs.parse_hybridization_character"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">parse_hybridization_character()</code></span></a>
    - <a href="#pymatgen.io.qchem.outputs.parse_hyperbonds"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">parse_hyperbonds()</code></span></a>
    - <a href="#pymatgen.io.qchem.outputs.parse_natural_populations"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">parse_natural_populations()</code></span></a>
    - <a href="#pymatgen.io.qchem.outputs.parse_perturbation_energy"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">parse_perturbation_energy()</code></span></a>
    - <a href="#pymatgen.io.qchem.outputs.z_int"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">z_int()</code></span></a>
  - <a href="#module-pymatgen.io.qchem.sets"
    class="reference internal">pymatgen.io.qchem.sets module</a>
    - <a href="#pymatgen.io.qchem.sets.ForceSet"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">ForceSet</code></span></a>
    - <a href="#pymatgen.io.qchem.sets.FreqSet"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">FreqSet</code></span></a>
    - <a href="#pymatgen.io.qchem.sets.OptSet"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">OptSet</code></span></a>
    - <a href="#pymatgen.io.qchem.sets.PESScanSet"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">PESScanSet</code></span></a>
    - <a href="#pymatgen.io.qchem.sets.QChemDictSet"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">QChemDictSet</code></span></a>
      - <a href="#pymatgen.io.qchem.sets.QChemDictSet.write"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">QChemDictSet.write()</code></span></a>
    - <a href="#pymatgen.io.qchem.sets.SinglePointSet"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">SinglePointSet</code></span></a>
    - <a href="#pymatgen.io.qchem.sets.TransitionStateSet"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">TransitionStateSet</code></span></a>
  - <a href="#module-pymatgen.io.qchem.utils"
    class="reference internal">pymatgen.io.qchem.utils module</a>
    - <a href="#pymatgen.io.qchem.utils.lower_and_check_unique"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">lower_and_check_unique()</code></span></a>
    - <a href="#pymatgen.io.qchem.utils.process_parsed_coords"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">process_parsed_coords()</code></span></a>
    - <a href="#pymatgen.io.qchem.utils.process_parsed_fock_matrix"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">process_parsed_fock_matrix()</code></span></a>
    - <a href="#pymatgen.io.qchem.utils.process_parsed_hess"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">process_parsed_hess()</code></span></a>
    - <a href="#pymatgen.io.qchem.utils.read_matrix_pattern"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">read_matrix_pattern()</code></span></a>
    - <a href="#pymatgen.io.qchem.utils.read_pattern"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">read_pattern()</code></span></a>
    - <a href="#pymatgen.io.qchem.utils.read_table_pattern"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">read_table_pattern()</code></span></a>

</div>

</div>

</div>

<div class="section wy-nav-content-wrap" toggle="wy-nav-shift">

[pymatgen](index.html)

<div class="wy-nav-content">

<div class="rst-content style-external-links">

<div role="navigation" aria-label="Page navigation">

- <a href="index.html" class="icon icon-home" aria-label="Home"></a>
- pymatgen.io.qchem package
- <a
  href="https://github.com/materialsproject/pymatgen/blob/master/docs_rst/pymatgen.io.qchem.rst"
  class="fa fa-github">Edit on GitHub</a>

------------------------------------------------------------------------

</div>

<div class="document" role="main" itemscope="itemscope"
itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="module-pymatgen.io.qchem" class="section">

<span id="pymatgen-io-qchem-package"></span>

# pymatgen.io.qchem package<a href="#module-pymatgen.io.qchem" class="headerlink"
title="Link to this heading"></a>

This package implements modules for input and output to and from Qchem.

<div id="submodules" class="section">

## Submodules<a href="#submodules" class="headerlink"
title="Link to this heading"></a>

</div>

<div id="module-pymatgen.io.qchem.inputs" class="section">

<span id="pymatgen-io-qchem-inputs-module"></span>

## pymatgen.io.qchem.inputs module<a href="#module-pymatgen.io.qchem.inputs" class="headerlink"
title="Link to this heading"></a>

Classes for reading/manipulating/writing QChem input files.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">QCInput</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">molecule</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'read'</span></span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">rem</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*, *<span class="n"><span class="pre">opt</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">pcm</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">solvent</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">smx</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">scan</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">van_der_waals</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">vdw_mode</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'atomic'</span></span>*, *<span class="n"><span class="pre">plots</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">nbo</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">geom_opt</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">cdft</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">almo_coupling</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">svp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">pcm_nonels</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L32-L1273"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="pymatgen.io.html#pymatgen.io.core.InputFile"
class="reference internal" title="pymatgen.io.core.InputFile"><span
class="pre"><code class="sourceCode python">InputFile</code></span></a>

An object representing a QChem input file. QCInput attributes represent
different sections of a QChem input file. To add a new section one needs
to modify \_\_init\_\_, \_\_str\_\_, from_sting and add static methods
to read and write the new section i.e. section_template and
read_section. By design, there is very little (or no) checking that
input parameters conform to the appropriate QChem format, this
responsible lands on the user or a separate error handling software.

Parameters<span class="colon">:</span>  
- **molecule** (*pymatgen Molecule object,* *list* *of* *Molecule
  objects, or* *"read"*) – Input molecule(s). molecule can be set as a
  pymatgen Molecule object, a list of such Molecule objects, or as the
  string “read”. “read” can be used in multi_job QChem input files where
  the molecule is read in from the previous calculation.

- **rem** (*dict*) – A dictionary of all the input parameters for the
  REM section of QChem input file. Ex. rem = {‘method’: ‘rimp2’,
  ‘basis’: ‘6-31\*G++’ … }

- **opt** (*dict* *of* *lists*) – A dictionary of opt sections, where
  each opt section is a key and the corresponding values are a list of
  strings. Strings must be formatted as instructed by the QChem manual.
  The different opt sections are: CONSTRAINT, FIXED, DUMMY, and CONNECT
  Ex. opt = {“CONSTRAINT”: \[“tors 2 3 4 5 25.0”, “tors 2 5 7 9 80.0”\],
  “FIXED”: \[“2 XY”\]}

- **pcm** (*dict*) – A dictionary of the PCM section, defining behavior
  for use of the polarizable continuum model. Ex: pcm = {“theory”:
  “cpcm”, “hpoints”: 194}

- **solvent** (*dict*) – A dictionary defining the solvent parameters
  used with PCM. Ex: solvent = {“dielectric”: 78.39, “temperature”:
  298.15}

- **smx** (*dict*) – A dictionary defining solvent parameters used with
  the SMD method, a solvent method that adds short-range terms to PCM.
  Ex: smx = {“solvent”: “water”}

- **scan** (*dict* *of* *lists*) – A dictionary of scan variables.
  Because two constraints of the same type are allowed (for instance,
  two torsions or two bond stretches), each TYPE of variable (stre,
  bend, tors) should be its own key in the dict, rather than each
  variable. Note that the total number of variable (sum of lengths of
  all lists) CANNOT be more than two. Ex. scan = {“stre”: \[“3 6 1.5 1.9
  0.1”\], “tors”: \[“1 2 3 4 -180 180 15”\]}

- **van_der_waals** (*dict*) – A dictionary of custom van der Waals
  radii to be used when constructing cavities for the PCM model or when
  computing, e.g. Mulliken charges. They keys are strs whose meaning
  depends on the value of vdw_mode, and the values are the custom radii
  in angstroms.

- **vdw_mode** (*str*) – Method of specifying custom van der Waals
  radii - ‘atomic’ or ‘sequential’. In ‘atomic’ mode (default), dict
  keys represent the atomic number associated with each radius (e.g., 12
  = carbon). In ‘sequential’ mode, dict keys represent the sequential
  position of a single specific atom in the input structure.

- **plots** (*dict*) – A dictionary of all the input parameters for the
  plots section of the QChem input file.

- **nbo** (*dict*) – A dictionary of all the input parameters for the
  nbo section of the QChem input file.

- **geom_opt** (*dict*) – A dictionary of input parameters for the
  geom_opt section of the QChem input file. This section is required
  when using the new libopt3 geometry optimizer.

- **cdft** (*list* *of* *lists* *of* *dicts*) –

  A list of lists of dictionaries, where each dictionary represents a
  charge constraint in the cdft section of the QChem input file.

  Each entry in the main list represents one state (allowing for
  multi-configuration calculations using constrained density functional
  theory - configuration interaction (CDFT-CI). Each state is
  represented by a list, which itself contains some number of
  constraints (dictionaries).

  Ex:

  1\. For a single-state calculation with two constraints: cdft=\[\[

  > <div>
  >
  > {“value”: 1.0, “coefficients”: \[1.0\], “first_atoms”: \[1\],
  > “last_atoms”: \[2\], “types”: \[None\]}, {“value”: 2.0,
  > “coefficients”: \[1.0, -1.0\], “first_atoms”: \[1, 17\],
  > “last_atoms”: \[3, 19\],
  >
  > > <div>
  > >
  > > ”types”: \[“s”\]}
  > >
  > > </div>
  >
  > </div>

  \]\]

  Note that a type of None will default to a charge constraint (which
  can also be accessed by requesting a type of “c” or “charge”.

  2\. For a multi-reference calculation: cdft=\[

  > <div>
  >
  > \[  
  > {“value”: 1.0, “coefficients”: \[1.0\], “first_atoms”: \[1\], “last_atoms”: \[27\],  
  > ”types”: \[“c”\]},
  >
  > {“value”: 0.0, “coefficients”: \[1.0\], “first_atoms”: \[1\], “last_atoms”: \[27\],  
  > ”types”: \[“s”\]},
  >
  > \], \[
  >
  > > <div>
  > >
  > > {“value”: 0.0, “coefficients”: \[1.0\], “first_atoms”: \[1\], “last_atoms”: \[27\],  
  > > ”types”: \[“c”\]},
  > >
  > > {“value”: -1.0, “coefficients”: \[1.0\], “first_atoms”: \[1\], “last_atoms”: \[27\],  
  > > ”types”: \[“s”\]},
  > >
  > > </div>
  >
  > \]
  >
  > </div>

  \]

- **almo_coupling** (*list* *of* *lists* *of* *int 2-tuples*) –

  A list of lists of int 2-tuples used for calculations of diabatization and state coupling calculations  
  relying on the absolutely localized molecular orbitals (ALMO)
  methodology. Each entry in the main list represents a single state
  (two states are included in an ALMO calculation). Within a single
  state, each 2-tuple represents the charge and spin multiplicity of a
  single fragment.

  ex: almo=\[  
  > <div>
  >
  > \[  
  > (1, 2), (0, 1)
  >
  > \], \[
  >
  > > <div>
  > >
  > > (0, 1), (1, 2)
  > >
  > > </div>
  >
  > \]
  >
  > </div>

  \]

- **svp** (*dict*) –

  Settings for the ISOSVP solvent model, corresponding to the \$svp
  section of the Q-Chem input file, which is formatted as a FORTRAN
  namelist. Note that in pymatgen, these parameters are typically not
  set by the user, but rather are populated automatically by an
  InputSet.

  An example for water may look like:  
  {  
  “RHOISO”: “0.001”, “DIELST”: “78.36”, “NPTLEB”: “1202”, “ITRNGR”: “2”,
  “IROTGR”: “2”, “IPNRF”: “1”, “IDEFESR”: “1”,

  }

  See <a href="https://manual.q-chem.com/6.0/subsec_SS(V)PE.html"
  class="reference external">https://manual.q-chem.com/6.0/subsec_SS(V)PE.html</a>
  in the Q-Chem manual for more details.

- **pcm_nonels** (*dict*) –

  Settings for the non-electrostatic part of the CMIRS solvation model,
  corresponding to the \$pcm_nonels section of the Q-Chem input file/
  Note that in pymatgen, these parameters are typically not set by the
  user, but rather are populated automatically by an InputSet.

  An example for water may look like:  
  {  
  “a”: “-0.006496”, “b”: “0.050833”, “c”: “-566.7”, “d”: “-30.503”,
  “gamma”: “3.2”, “solvrho”: “0.05”, “delta”: 7, “gaulag_n”: 40,

  }

  See <a href="https://manual.q-chem.com/6.0/example_CMIRS-water.html"
  class="reference external">https://manual.q-chem.com/6.0/example_CMIRS-water.html</a>
  in the Q-Chem manual for more details.

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">almo_template</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">almo_coupling</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L717-L742"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.almo_template"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
**almo** – list of lists of int 2-tuples.

Returns<span class="colon">:</span>  
ALMO coupling section.

Return type<span class="colon">:</span>  
str

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">cdft_template</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">cdft</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L671-L715"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.cdft_template"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
**cdft** – list of lists of dicts.

Returns<span class="colon">:</span>  
CDFT section.

Return type<span class="colon">:</span>  
str

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">find_sections</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">string</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L777-L800"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.find_sections"
class="headerlink" title="Link to this definition"></a>  
Find sections in the string.

Parameters<span class="colon">:</span>  
**string** (*str*) – String

Returns<span class="colon">:</span>  
List of sections.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Path</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L382-L394"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.from_file" class="headerlink"
title="Link to this definition"></a>  
Create QcInput from file.

Parameters<span class="colon">:</span>  
**filename** (*str*) – Filename

Returns<span class="colon">:</span>  
QcInput

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_multi_jobs_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">Self</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L396-L411"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.from_multi_jobs_file"
class="headerlink" title="Link to this definition"></a>  
Create list of QcInput from a file.

Parameters<span class="colon">:</span>  
**filename** (*str*) – Filename

Returns<span class="colon">:</span>  
List of QCInput objects

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">string</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L308-L369"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.from_str" class="headerlink"
title="Link to this definition"></a>  
Read QcInput from string.

Parameters<span class="colon">:</span>  
**string** (*str*) – String input.

Returns<span class="colon">:</span>  
QcInput

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">geom_opt_template</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">geom_opt</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L655-L669"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.geom_opt_template"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
**geom_opt** (*dict*) – Geometry optimization section.

Returns<span class="colon">:</span>  
Geometry optimization section.

Return type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">get_str</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L287-L289"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.get_str" class="headerlink"
title="Link to this definition"></a>  
Return a string representation of an entire input file.

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">molecule_template</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">molecule</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'read'</span></span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L413-L455"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.molecule_template"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
**molecule**
(<a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><em>Molecule</em></a>*,* *list*
*of* *Molecules, or* *"read"*)

Returns<span class="colon">:</span>  
Molecule template.

Return type<span class="colon">:</span>  
str

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">multi_job_string</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">job_list</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.io.qchem.inputs.QCInput" class="reference internal"
title="pymatgen.io.qchem.inputs.QCInput"><span
class="pre">QCInput</span></a><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L291-L306"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.multi_job_string"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
**job_list**
(*list\[*<a href="#pymatgen.io.qchem.inputs.QCInput" class="reference internal"
title="pymatgen.io.qchem.inputs.QCInput"><em>QCInput</em></a>*\]*) –
List of QChem jobs.

Returns<span class="colon">:</span>  
String representation of a multi-job input file.

Return type<span class="colon">:</span>  
str

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">nbo_template</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">nbo</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L619-L633"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.nbo_template"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
**nbo** (*dict*) – NBO section.

Returns<span class="colon">:</span>  
NBO section.

Return type<span class="colon">:</span>  
str

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">opt_template</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">opt</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L473-L495"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.opt_template"
class="headerlink" title="Link to this definition"></a>  
Optimization template.

Parameters<span class="colon">:</span>  
**opt** (*dict\[str,* *list\]*) – Optimization section.

Returns<span class="colon">:</span>  
Optimization template.

Return type<span class="colon">:</span>  
str

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">pcm_nonels_template</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">pcm_nonels</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L744-L775"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.pcm_nonels_template"
class="headerlink" title="Link to this definition"></a>  
Template for the \$pcm_nonels section.

Arg  
pcm_nonels: dict of CMIRS parameters, e.g. {

> <div>
>
> “a”: “-0.006736”, “b”: “0.032698”, “c”: “-1249.6”, “d”: “-21.405”,
> “gamma”: “3.7”, “solvrho”: “0.05”, “delta”: 7, “gaulag_n”: 40,
>
> </div>

}

Returns<span class="colon">:</span>  
the \$pcm_nonels section. Note that all parameters will be concatenated onto  
a single line formatted as a FORTRAN namelist. This is necessary because
the non-electrostatic part of the CMIRS solvation model in Q-Chem calls
a secondary code.

Return type<span class="colon">:</span>  
str

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">pcm_template</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">pcm</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L497-L513"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.pcm_template"
class="headerlink" title="Link to this definition"></a>  
PCM run template.

Parameters<span class="colon">:</span>  
**pcm** (*dict*) – PCM section.

Returns<span class="colon">:</span>  
PCM template.

Return type<span class="colon">:</span>  
str

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">plots_template</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">plots</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L604-L617"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.plots_template"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
**plots** (*dict*) – Plots section.

Returns<span class="colon">:</span>  
Plots section.

Return type<span class="colon">:</span>  
str

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">read_almo</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">string</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L1197-L1233"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.read_almo" class="headerlink"
title="Link to this definition"></a>  
Read ALMO coupling parameters from string.

Parameters<span class="colon">:</span>  
**string** (*str*) – String

Returns<span class="colon">:</span>  
ALMO coupling parameters

Return type<span class="colon">:</span>  
list\[list\[tuple\[int, int\]\]\]

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">read_cdft</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">string</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L1139-L1195"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.read_cdft" class="headerlink"
title="Link to this definition"></a>  
Read cdft parameters from string.

Parameters<span class="colon">:</span>  
**string** (*str*) – String

Returns<span class="colon">:</span>  
cdft parameters

Return type<span class="colon">:</span>  
list\[list\[dict\]\]

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">read_geom_opt</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">string</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L1119-L1137"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.read_geom_opt"
class="headerlink" title="Link to this definition"></a>  
Read geom_opt parameters from string.

Parameters<span class="colon">:</span>  
**string** (*str*) – String

Returns<span class="colon">:</span>  
geom_opt parameters.

Return type<span class="colon">:</span>  
dict\[str, str\]

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">read_molecule</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">string</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'read'</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L802-L865"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.read_molecule"
class="headerlink" title="Link to this definition"></a>  
Read molecule from string.

Parameters<span class="colon">:</span>  
**string** (*str*) – String

Returns<span class="colon">:</span>  
Molecule

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">read_nbo</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">string</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L1099-L1117"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.read_nbo" class="headerlink"
title="Link to this definition"></a>  
Read nbo parameters from string.

Parameters<span class="colon">:</span>  
**string** (*str*) – String

Returns<span class="colon">:</span>  
nbo parameters.

Return type<span class="colon">:</span>  
dict\[str, str\]

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">read_opt</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">string</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L883-L947"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.read_opt" class="headerlink"
title="Link to this definition"></a>  
Read opt section from string.

Parameters<span class="colon">:</span>  
**string** (*str*) – String

Returns<span class="colon">:</span>  
Opt section

Return type<span class="colon">:</span>  
dict\[str, list\]

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">read_pcm</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">string</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L949-L968"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.read_pcm" class="headerlink"
title="Link to this definition"></a>  
Read pcm parameters from string.

Parameters<span class="colon">:</span>  
**string** (*str*) – String

Returns<span class="colon">:</span>  
PCM parameters

Return type<span class="colon">:</span>  
dict\[str, str\]

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">read_pcm_nonels</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">string</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L1251-L1273"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.read_pcm_nonels"
class="headerlink" title="Link to this definition"></a>  
Read pcm_nonels parameters from string.

Parameters<span class="colon">:</span>  
**string** (*str*) – String

Returns<span class="colon">:</span>  
PCM parameters

Return type<span class="colon">:</span>  
dict\[str, str\]

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">read_plots</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">string</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L1077-L1097"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.read_plots"
class="headerlink" title="Link to this definition"></a>  
Read plots parameters from string.

Parameters<span class="colon">:</span>  
**string** (*str*) – String

Returns<span class="colon">:</span>  
plots parameters.

Return type<span class="colon">:</span>  
dict\[str, str\]

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">read_rem</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">string</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L867-L881"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.read_rem" class="headerlink"
title="Link to this definition"></a>  
Parse rem from string.

Parameters<span class="colon">:</span>  
**string** (*str*) – String

Returns<span class="colon">:</span>  
REM section

Return type<span class="colon">:</span>  
dict\[str, str\]

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">read_scan</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">string</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L1042-L1075"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.read_scan" class="headerlink"
title="Link to this definition"></a>  
Read scan section from a string.

Parameters<span class="colon">:</span>  
**string** – String to be parsed

Returns<span class="colon">:</span>  
Dict representing Q-Chem scan section

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">read_smx</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">string</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L1016-L1040"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.read_smx" class="headerlink"
title="Link to this definition"></a>  
Read smx parameters from string.

Parameters<span class="colon">:</span>  
**string** (*str*) – String

Returns<span class="colon">:</span>  
dict\[str, str\] SMX parameters.

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">read_solvent</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">string</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L993-L1014"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.read_solvent"
class="headerlink" title="Link to this definition"></a>  
Read solvent parameters from string.

Parameters<span class="colon">:</span>  
**string** (*str*) – String

Returns<span class="colon">:</span>  
Solvent parameters

Return type<span class="colon">:</span>  
dict\[str, str\]

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">read_svp</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">string</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L1235-L1249"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.read_svp" class="headerlink"
title="Link to this definition"></a>  
Read svp parameters from string.

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">read_vdw</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">string</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L970-L991"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.read_vdw" class="headerlink"
title="Link to this definition"></a>  
Read van der Waals parameters from string.

Parameters<span class="colon">:</span>  
**string** (*str*) – String

Returns<span class="colon">:</span>  
(vdW mode (‘atomic’ or ‘sequential’), dict of van der Waals radii)

Return type<span class="colon">:</span>  
tuple\[str, dict\]

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">rem_template</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">rem</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L457-L471"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.rem_template"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
**rem** (*dict\[str,* *Any\]*) – REM section.

Returns<span class="colon">:</span>  
REM template.

Return type<span class="colon">:</span>  
str

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">scan_template</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">scan</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L554-L571"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.scan_template"
class="headerlink" title="Link to this definition"></a>  
Get string representing Q-Chem input format for scan section.

Parameters<span class="colon">:</span>  
**scan** (*dict*) – Dictionary with scan section information. Ex:
{“stre”: \[“3 6 1.5 1.9 0.1”\], “tors”: \[“1 2 3 4 -180 180 15”\]}.

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">smx_template</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">smx</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L532-L552"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.smx_template"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
**smx** (*dict*) – Solvation model with short-range corrections.

Returns<span class="colon">:</span>  
Solvation model with short-range corrections.

Return type<span class="colon">:</span>  
str

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">solvent_template</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">solvent</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L515-L530"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.solvent_template"
class="headerlink" title="Link to this definition"></a>  
Solvent template.

Parameters<span class="colon">:</span>  
**solvent** (*dict*) – Solvent section.

Returns<span class="colon">:</span>  
Solvent section.

Return type<span class="colon">:</span>  
str

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">svp_template</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">svp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L635-L653"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.svp_template"
class="headerlink" title="Link to this definition"></a>  
Template for the \$svp section.

Parameters<span class="colon">:</span>  
- **svp** – dict of SVP parameters, e.g.

- **{"rhoiso"** – “0.001”, “nptleb”: “1202”, “itrngr”: “2”, “irotgr”:
  “2”}

Returns<span class="colon">:</span>  
the \$svp section. Note that all parameters will be concatenated onto  
a single line formatted as a FORTRAN namelist. This is necessary because
the isodensity SS(V)PE model in Q-Chem calls a secondary code.

Return type<span class="colon">:</span>  
str

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">van_der_waals_template</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">radii</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">mode</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'atomic'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L573-L602"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.van_der_waals_template"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
- **radii** (*dict*) – Dictionary with custom van der Waals radii, in
  Angstroms, keyed by either atomic number or sequential atom number
  (see ‘mode’ kwarg). Ex: {1: 1.20, 12: 1.70}

- **mode** – ‘atomic’ or ‘sequential’. In ‘atomic’ mode (default), dict
  keys represent the atomic number associated with each radius (e.g.,
  ‘12’ = carbon). In ‘sequential’ mode, dict keys represent the
  sequential position of a single specific atom in the input structure.
  **NOTE: keys must be given as strings even though they are numbers!**.

Returns<span class="colon">:</span>  
representing Q-Chem input format for van_der_waals section

Return type<span class="colon">:</span>  
str

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">write_multi_job_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">job_list</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.io.qchem.inputs.QCInput" class="reference internal"
title="pymatgen.io.qchem.inputs.QCInput"><span
class="pre">QCInput</span></a><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/inputs.py#L371-L380"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.inputs.QCInput.write_multi_job_file"
class="headerlink" title="Link to this definition"></a>  
Write a multijob file.

Parameters<span class="colon">:</span>  
- **job_list**
  (*list\[*<a href="#pymatgen.io.qchem.inputs.QCInput" class="reference internal"
  title="pymatgen.io.qchem.inputs.QCInput"><em>QCInput</em></a>*\]*) –
  List of QChem jobs.

- **filename** (*str*) – Name of the file to write.

</div>

<div id="module-pymatgen.io.qchem.outputs" class="section">

<span id="pymatgen-io-qchem-outputs-module"></span>

## pymatgen.io.qchem.outputs module<a href="#module-pymatgen.io.qchem.outputs" class="headerlink"
title="Link to this heading"></a>

Parsers for Qchem output files.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">QCOutput</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/outputs.py#L49-L2277"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.outputs.QCOutput" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Parse QChem output files.

Parameters<span class="colon">:</span>  
**filename** (*str*) – Filename to parse.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/outputs.py#L2271-L2277"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.outputs.QCOutput.as_dict" class="headerlink"
title="Link to this definition"></a>  
Get MSONable dict representation of QCOutput.

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">multiple_outputs_from_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span>*, *<span class="n"><span class="pre">keep_sub_files</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/outputs.py#L654-L676"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.outputs.QCOutput.multiple_outputs_from_file"
class="headerlink" title="Link to this definition"></a>  
Parses a QChem output file with multiple calculations \# 1.) Separates
the output into sub-files

> <div>
>
> e.g. qcout -\> qcout.0, qcout.1, qcout.2 … qcout.N a.) Find delimiter
> for multiple calculations b.) Make separate output sub-files
>
> </div>

2.) Creates separate QCCalcs for each one from the sub-files.

<!-- -->

<span class="sig-name descname"><span class="pre">check_for_structure_changes</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">mol1</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">mol2</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/outputs.py#L2280-L2342"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.outputs.check_for_structure_changes"
class="headerlink" title="Link to this definition"></a>  
Compares connectivity of two molecules (using MoleculeGraph w/
OpenBabelNN). This function will work with two molecules with different
atom orderings,

> <div>
>
> but for proper treatment, atoms should be listed in the same order.
>
> </div>

Possible outputs include: - no_change: the bonding in the two molecules
is identical - unconnected_fragments: the MoleculeGraph of mol1 is
connected, but the

> <div>
>
> MoleculeGraph is mol2 is not connected
>
> </div>

- fewer_bonds: the MoleculeGraph of mol1 has more bonds (edges) than the
  MoleculeGraph of mol2

- more_bonds: the MoleculeGraph of mol2 has more bonds (edges) than the
  MoleculeGraph of mol1

- bond_change: this case catches any other non-identical MoleculeGraphs

Parameters<span class="colon">:</span>  
- **mol1** – Pymatgen Molecule object to be compared.

- **mol2** – Pymatgen Molecule object to be compared.

Returns<span class="colon">:</span>  
One of \[“unconnected_fragments”, “fewer_bonds”, “more_bonds”,
“bond_change”, “no_change”\]

<!-- -->

<span class="sig-name descname"><span class="pre">get_percentage</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">line</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">orbital</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/outputs.py#L2369-L2392"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.outputs.get_percentage" class="headerlink"
title="Link to this definition"></a>  
Retrieve the percent character of an orbital.

Parameters<span class="colon">:</span>  
- **line** – Line containing orbital and percentage.

- **orbital** – Type of orbital (s, p, d, f).

Returns<span class="colon">:</span>  
Percentage of character.

Raises<span class="colon">:</span>  
**n/a** –

<!-- -->

<span class="sig-name descname"><span class="pre">gradient_parser</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Path</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'131.0'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">NDArray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/outputs.py#L2968-L2991"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.outputs.gradient_parser" class="headerlink"
title="Link to this definition"></a>  
Parse the gradient data from a gradient scratch file.

Parameters<span class="colon">:</span>  
**filename** – Path to the gradient scratch file. Defaults to “131.0”.

Returns<span class="colon">:</span>  
The gradient, in units of Hartree/Bohr.

Return type<span class="colon">:</span>  
NDArray

<!-- -->

<span class="sig-name descname"><span class="pre">hessian_parser</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Path</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'132.0'</span></span>*, *<span class="n"><span class="pre">n_atoms</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">NDArray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/outputs.py#L2994-L3011"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.outputs.hessian_parser" class="headerlink"
title="Link to this definition"></a>  
Parse the Hessian data from a Hessian scratch file.

Parameters<span class="colon">:</span>  
- **filename** – Path to the Hessian scratch file. Defaults to “132.0”.

- **n_atoms** – Number of atoms in the molecule. If None, no reshaping
  will be done.

Returns<span class="colon">:</span>  
Hessian, formatted as 3n_atoms x 3n_atoms. Units are Hartree/Bohr^2/amu.

Return type<span class="colon">:</span>  
NDArray

<!-- -->

<span class="sig-name descname"><span class="pre">jump_to_header</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">lines</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">header</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/outputs.py#L2345-L2366"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.outputs.jump_to_header" class="headerlink"
title="Link to this definition"></a>  
Given a list of lines, truncate the start of the list so that the first
line of the new list contains the header.

Parameters<span class="colon">:</span>  
- **lines** – List of lines.

- **header** – Substring to match.

Returns<span class="colon">:</span>  
Truncated lines.

Raises<span class="colon">:</span>  
**RuntimeError** – If the header is not found.

<!-- -->

<span class="sig-name descname"><span class="pre">nbo_parser</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Path</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">pd.DataFrame</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/outputs.py#L2942-L2965"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.outputs.nbo_parser" class="headerlink"
title="Link to this definition"></a>  
Parse all the important sections of NBO output.

Parameters<span class="colon">:</span>  
**filename** – Path to QChem NBO output.

Returns<span class="colon">:</span>  
Data frames of formatted output.

Raises<span class="colon">:</span>  
**RuntimeError** – If a section cannot be found.

<!-- -->

<span class="sig-name descname"><span class="pre">orbital_coeffs_parser</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Path</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'53.0'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">NDArray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/outputs.py#L3014-L3028"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.outputs.orbital_coeffs_parser"
class="headerlink" title="Link to this definition"></a>  
Parse the orbital coefficients from a scratch file.

Parameters<span class="colon">:</span>  
**filename** – Path to the orbital coefficients file. Defaults to
“53.0”.

Returns<span class="colon">:</span>  
The orbital coefficients

Return type<span class="colon">:</span>  
NDArray

<!-- -->

<span class="sig-name descname"><span class="pre">parse_hybridization_character</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">lines</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">DataFrame</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/outputs.py#L2556-L2790"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.outputs.parse_hybridization_character"
class="headerlink" title="Link to this definition"></a>  
Parse the hybridization character section of NBO output.

Parameters<span class="colon">:</span>  
**lines** – QChem output lines.

Returns<span class="colon">:</span>  
Data frames of formatted output.

Raises<span class="colon">:</span>  
**RuntimeError** – If the header is not found.

<!-- -->

<span class="sig-name descname"><span class="pre">parse_hyperbonds</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">lines</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">DataFrame</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/outputs.py#L2475-L2553"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.outputs.parse_hyperbonds" class="headerlink"
title="Link to this definition"></a>  
Parse the natural populations section of NBO output.

Parameters<span class="colon">:</span>  
**lines** – QChem output lines.

Returns<span class="colon">:</span>  
Data frame of formatted output.

Raises<span class="colon">:</span>  
**RuntimeError** – If the header is not found.

<!-- -->

<span class="sig-name descname"><span class="pre">parse_natural_populations</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">lines</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">DataFrame</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/outputs.py#L2415-L2472"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.outputs.parse_natural_populations"
class="headerlink" title="Link to this definition"></a>  
Parse the natural populations section of NBO output.

Parameters<span class="colon">:</span>  
**lines** – QChem output lines.

Returns<span class="colon">:</span>  
Data frame of formatted output.

Raises<span class="colon">:</span>  
**RuntimeError** – If the header is not found.

<!-- -->

<span class="sig-name descname"><span class="pre">parse_perturbation_energy</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">lines</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">DataFrame</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/outputs.py#L2793-L2939"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.outputs.parse_perturbation_energy"
class="headerlink" title="Link to this definition"></a>  
Parse the perturbation energy section of NBO output.

Parameters<span class="colon">:</span>  
**lines** – QChem output lines.

Returns<span class="colon">:</span>  
Data frame of formatted output.

Raises<span class="colon">:</span>  
**RuntimeError** – If the header is not found.

<!-- -->

<span class="sig-name descname"><span class="pre">z_int</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">string</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">int</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/outputs.py#L2395-L2412"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.outputs.z_int" class="headerlink"
title="Link to this definition"></a>  
Convert string to integer. If string empty, return -1.

Parameters<span class="colon">:</span>  
**string** – Input to be cast to int.

Returns<span class="colon">:</span>  
Int representation.

Raises<span class="colon">:</span>  
**n/a** –

</div>

<div id="module-pymatgen.io.qchem.sets" class="section">

<span id="pymatgen-io-qchem-sets-module"></span>

## pymatgen.io.qchem.sets module<a href="#module-pymatgen.io.qchem.sets" class="headerlink"
title="Link to this heading"></a>

Input sets for Qchem.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ForceSet</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">molecule</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">basis_set</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'def2-tzvpd'</span></span>*, *<span class="n"><span class="pre">scf_algorithm</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'diis'</span></span>*, *<span class="n"><span class="pre">qchem_version</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">5</span></span>*, *<span class="n"><span class="pre">dft_rung</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">4</span></span>*, *<span class="n"><span class="pre">pcm_dielectric</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">isosvp_dielectric</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">smd_solvent</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">cmirs_solvent</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'water'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'acetonitrile'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'dimethyl</span> <span class="pre">sulfoxide'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cyclohexane'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'benzene'</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">custom_smd</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">max_scf_cycles</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">100</span></span>*, *<span class="n"><span class="pre">plot_cubes</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">output_wavefunction</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">nbo_params</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">vdw_mode</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'atomic'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'sequential'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'atomic'</span></span>*, *<span class="n"><span class="pre">cdft_constraints</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">overwrite_inputs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/sets.py#L1229-L1419"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.sets.ForceSet" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.qchem.sets.QChemDictSet"
class="reference internal"
title="pymatgen.io.qchem.sets.QChemDictSet"><span class="pre"><code
class="sourceCode python">QChemDictSet</code></span></a>

QChemDictSet for a force (gradient) calculation.

Parameters<span class="colon">:</span>  
- **molecule** (*Pymatgen Molecule object*)

- **basis_set** (*str*) – Basis set to use. (Default: “def2-tzvpd”)

- **scf_algorithm** (*str*) – Algorithm to use for converging the SCF.
  Recommended choices are “DIIS”, “GDM”, and “DIIS_GDM”. Other
  algorithms supported by Qchem’s GEN_SCFMAN module will also likely
  perform well. Refer to the QChem manual for further details. (Default:
  “diis”)

- **qchem_version** (*int*) – Which major version of Q-Chem will be run.
  Supports 5 and 6. (Default: 5)

- **dft_rung** (*int*) –

  Select the rung on “Jacob’s Ladder of Density Functional
  Approximations” in order of increasing accuracy/cost. For each rung,
  we have prescribed one functional based on our experience, available
  benchmarks, and the suggestions of the Q-Chem manual: 1 (LSDA) = SPW92
  2 (GGA) = B97-D3(BJ) 3 (metaGGA) = B97M-V 4 (hybrid metaGGA) = ωB97M-V
  5 (double hybrid metaGGA) = ωB97M-(2).

  (Default: 4)

  To set a functional not given by one of the above, set the
  overwrite_inputs argument to {“method”:”\<NAME OF FUNCTIONAL\>”}

- **pcm_dielectric** (*float*) –

  Dielectric constant to use for PCM implicit solvation model. (Default:
  None) If supplied, will set up the \$pcm section of the input file for
  a C-PCM calculation. Other types of PCM calculations (e.g., IEF-PCM,
  SS(V)PE, etc.) may be requested by passing custom keywords to
  overwrite_inputs, e.g. overwrite_inputs = {“pcm”: {“theory”: “ssvpe”}}
  Refer to the QChem manual for further details on the models available.

  **Note that only one of pcm_dielectric, isosvp_dielectric,
  smd_solvent, or cmirs_solvent may be set.**

- **isosvp_dielectric** (*float*) –

  Dielectric constant to use for isodensity SS(V)PE implicit solvation
  model. (Default: None). If supplied, will set solvent_method to
  “isosvp” and populate the \$svp section of the input file with
  appropriate parameters.

  **Note that only one of pcm_dielectric, isosvp_dielectric,
  smd_solvent, or cmirs_solvent may be set.**

- **smd_solvent** (*str*) –

  Solvent to use for SMD implicit solvation model. (Default: None)
  Examples include “water”, “ethanol”, “methanol”, and “acetonitrile”.
  Refer to the QChem manual for a complete list of solvents available.
  To define a custom solvent, set this argument to “custom” and populate
  custom_smd with the necessary parameters.

  **Note that only one of pcm_dielectric, isosvp_dielectric,
  smd_solvent, or cmirs_solvent may be set.**

- **cmirs_solvent** (*str*) –

  Solvent to use for the CMIRS implicit solvation model. (Default:
  None). Only 5 solvents are presently available as of Q-Chem 6:
  “water”, “benzene”, “cyclohexane”, “dimethyl sulfoxide”, and
  “acetonitrile”. Note that selection of a solvent here will also
  populate the iso SS(V)PE dielectric constant, because CMIRS uses the
  isodensity SS(V)PE model to compute electrostatics.

  **Note that only one of pcm_dielectric, isosvp_dielectric,
  smd_solvent, or cmirs_solvent may be set.**

- **custom_smd** (*str*) – List of parameters to define a custom solvent
  in SMD. (Default: None) Must be given as a string of seven comma
  separated values in the following order: “dielectric, refractive
  index, acidity, basicity, surface tension, aromaticity,
  electronegative halogenicity” Refer to the QChem manual for further
  details.

- **max_scf_cycles** (*int*) – Maximum number of SCF iterations.
  (Default: 100)

- **plot_cubes** (*bool*) – Whether to write CUBE files of the electron
  density. (Default: False)

- **output_wavefunction** (*bool*) – Whether to write a wavefunction
  ([<span id="id2" class="problematic">\*</span>](#id1).wfn) file of the
  electron density (Default: False)

- **vdw_mode** (*'atomic'* *\|* *'sequential'*) – Method of specifying
  custom van der Waals radii. Applies only if you are using
  overwrite_inputs to add a \$van_der_waals section to the input. In
  ‘atomic’ mode (default), dict keys represent the atomic number
  associated with each radius (e.g., ‘12’ = carbon). In ‘sequential’
  mode, dict keys represent the sequential position of a single specific
  atom in the input structure.

- **cdft_constraints** (*list* *of* *lists* *of* *dicts*) –

  A list of lists of dictionaries, where each dictionary represents a
  charge constraint in the cdft section of the QChem input file.

  Each entry in the main list represents one state (allowing for
  multi-configuration calculations using constrained density functional
  theory - configuration interaction (CDFT-CI). Each state is
  represented by a list, which itself contains some number of
  constraints (dictionaries).

  Ex:

  1.  For a single-state calculation with two constraints:

  > <div>
  >
  > cdft_constraints=\[\[  
  > {  
  > “value”: 1.0, “coefficients”: \[1.0\], “first_atoms”: \[1\],
  > “last_atoms”: \[2\], “types”: \[None\]
  >
  > }, {
  >
  > > <div>
  > >
  > > ”value”: 2.0, “coefficients”: \[1.0, -1.0\], “first_atoms”: \[1,
  > > 17\], “last_atoms”: \[3, 19\], “types”: \[“s”\]
  > >
  > > </div>
  >
  > }
  >
  > </div>

  \]\]

  Note that a type of None will default to a charge constraint (which
  can also be accessed by requesting a type of “c” or “charge”).

  2\. For a CDFT-CI multi-reference calculation: cdft_constraints=\[

  > <div>
  >
  > \[  
  > {  
  > “value”: 1.0, “coefficients”: \[1.0\], “first_atoms”: \[1\],
  > “last_atoms”: \[27\], “types”: \[“c”\]
  >
  > }, {
  >
  > > <div>
  > >
  > > ”value”: 0.0, “coefficients”: \[1.0\], “first_atoms”: \[1\],
  > > “last_atoms”: \[27\], “types”: \[“s”\]
  > >
  > > </div>
  >
  > },
  >
  > \], \[
  >
  > > <div>
  > >
  > > {  
  > > “value”: 0.0, “coefficients”: \[1.0\], “first_atoms”: \[1\],
  > > “last_atoms”: \[27\], “types”: \[“c”\]
  > >
  > > }, {
  > >
  > > > <div>
  > > >
  > > > ”value”: -1.0, “coefficients”: \[1.0\], “first_atoms”: \[1\],
  > > > “last_atoms”: \[27\], “types”: \[“s”\]
  > > >
  > > > </div>
  > >
  > > },
  > >
  > > </div>
  >
  > \]
  >
  > </div>

  \]

- **overwrite_inputs** (*dict*) –

  Dictionary of QChem input sections to add or overwrite variables. The
  currently available sections (keys) are rem, pcm, solvent, smx, opt,
  scan, van_der_waals, and plots. The value of each key is a dictionary
  of key value pairs relevant to that section. For example, to add a new
  variable to the rem section that sets symmetry to false, use

  overwrite_inputs = {“rem”: {“symmetry”: “false”}}

  **Note that if something like basis is added to the rem dict it will
  overwrite the default basis.**

  **Note that supplying a van_der_waals section here will automatically
  modify the PCM “radii” setting to “read”.**

  **Note that all keys must be given as strings, even when they are
  numbers!**

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">FreqSet</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">molecule</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">basis_set</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'def2-svpd'</span></span>*, *<span class="n"><span class="pre">scf_algorithm</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'diis'</span></span>*, *<span class="n"><span class="pre">qchem_version</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">5</span></span>*, *<span class="n"><span class="pre">dft_rung</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">4</span></span>*, *<span class="n"><span class="pre">pcm_dielectric</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">isosvp_dielectric</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">smd_solvent</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">cmirs_solvent</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'water'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'acetonitrile'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'dimethyl</span> <span class="pre">sulfoxide'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cyclohexane'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'benzene'</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">custom_smd</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">max_scf_cycles</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">100</span></span>*, *<span class="n"><span class="pre">plot_cubes</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">output_wavefunction</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">nbo_params</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">vdw_mode</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'atomic'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'sequential'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'atomic'</span></span>*, *<span class="n"><span class="pre">cdft_constraints</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">overwrite_inputs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/sets.py#L1422-L1612"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.sets.FreqSet" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.qchem.sets.QChemDictSet"
class="reference internal"
title="pymatgen.io.qchem.sets.QChemDictSet"><span class="pre"><code
class="sourceCode python">QChemDictSet</code></span></a>

QChemDictSet for a frequency calculation.

Parameters<span class="colon">:</span>  
- **molecule** (*Pymatgen Molecule object*)

- **basis_set** (*str*) – Basis set to use. (Default: “def2-svpd”)

- **scf_algorithm** (*str*) – Algorithm to use for converging the SCF.
  Recommended choices are “DIIS”, “GDM”, and “DIIS_GDM”. Other
  algorithms supported by Qchem’s GEN_SCFMAN module will also likely
  perform well. Refer to the QChem manual for further details. (Default:
  “diis”)

- **qchem_version** (*int*) – Which major version of Q-Chem will be run.
  Supports 5 and 6. (Default: 5)

- **dft_rung** (*int*) –

  Select the rung on “Jacob’s Ladder of Density Functional
  Approximations” in order of increasing accuracy/cost. For each rung,
  we have prescribed one functional based on our experience, available
  benchmarks, and the suggestions of the Q-Chem manual: 1 (LSDA) = SPW92
  2 (GGA) = B97-D3(BJ) 3 (metaGGA) = B97M-V 4 (hybrid metaGGA) = ωB97M-V
  5 (double hybrid metaGGA) = ωB97M-(2).

  (Default: 4)

  To set a functional not given by one of the above, set the
  overwrite_inputs argument to {“method”:”\<NAME OF FUNCTIONAL\>”}

- **pcm_dielectric** (*float*) –

  Dielectric constant to use for PCM implicit solvation model. (Default:
  None) If supplied, will set up the \$pcm section of the input file for
  a C-PCM calculation. Other types of PCM calculations (e.g., IEF-PCM,
  SS(V)PE, etc.) may be requested by passing custom keywords to
  overwrite_inputs, e.g. overwrite_inputs = {“pcm”: {“theory”: “ssvpe”}}
  Refer to the QChem manual for further details on the models available.

  **Note that only one of pcm_dielectric, isosvp_dielectric,
  smd_solvent, or cmirs_solvent may be set.**

- **isosvp_dielectric** (*float*) –

  Dielectric constant to use for isodensity SS(V)PE implicit solvation
  model. (Default: None). If supplied, will set solvent_method to
  “isosvp” and populate the \$svp section of the input file with
  appropriate parameters.

  **Note that only one of pcm_dielectric, isosvp_dielectric,
  smd_solvent, or cmirs_solvent may be set.**

- **smd_solvent** (*str*) –

  Solvent to use for SMD implicit solvation model. (Default: None)
  Examples include “water”, “ethanol”, “methanol”, and “acetonitrile”.
  Refer to the QChem manual for a complete list of solvents available.
  To define a custom solvent, set this argument to “custom” and populate
  custom_smd with the necessary parameters.

  **Note that only one of pcm_dielectric, isosvp_dielectric,
  smd_solvent, or cmirs_solvent may be set.**

- **cmirs_solvent** (*str*) –

  Solvent to use for the CMIRS implicit solvation model. (Default:
  None). Only 5 solvents are presently available as of Q-Chem 6:
  “water”, “benzene”, “cyclohexane”, “dimethyl sulfoxide”, and
  “acetonitrile”. Note that selection of a solvent here will also
  populate the iso SS(V)PE dielectric constant, because CMIRS uses the
  isodensity SS(V)PE model to compute electrostatics.

  **Note that only one of pcm_dielectric, isosvp_dielectric,
  smd_solvent, or cmirs_solvent may be set.**

- **custom_smd** (*str*) – List of parameters to define a custom solvent
  in SMD. (Default: None) Must be given as a string of seven comma
  separated values in the following order: “dielectric, refractive
  index, acidity, basicity, surface tension, aromaticity,
  electronegative halogenicity” Refer to the QChem manual for further
  details.

- **max_scf_cycles** (*int*) – Maximum number of SCF iterations.
  (Default: 100)

- **plot_cubes** (*bool*) – Whether to write CUBE files of the electron
  density. (Default: False)

- **output_wavefunction** (*bool*) – Whether to write a wavefunction
  ([<span id="id4" class="problematic">\*</span>](#id3).wfn) file of the
  electron density (Default: False)

- **vdw_mode** (*'atomic'* *\|* *'sequential'*) – Method of specifying
  custom van der Waals radii. Applies only if you are using
  overwrite_inputs to add a \$van_der_waals section to the input. In
  ‘atomic’ mode (default), dict keys represent the atomic number
  associated with each radius (e.g., ‘12’ = carbon). In ‘sequential’
  mode, dict keys represent the sequential position of a single specific
  atom in the input structure.

- **cdft_constraints** (*list* *of* *lists* *of* *dicts*) –

  A list of lists of dictionaries, where each dictionary represents a
  charge constraint in the cdft section of the QChem input file.

  Each entry in the main list represents one state (allowing for
  multi-configuration calculations using constrained density functional
  theory - configuration interaction (CDFT-CI). Each state is
  represented by a list, which itself contains some number of
  constraints (dictionaries).

  Ex:

  1.  For a single-state calculation with two constraints:

  > <div>
  >
  > cdft_constraints=\[\[  
  > {  
  > “value”: 1.0, “coefficients”: \[1.0\], “first_atoms”: \[1\],
  > “last_atoms”: \[2\], “types”: \[None\]
  >
  > }, {
  >
  > > <div>
  > >
  > > ”value”: 2.0, “coefficients”: \[1.0, -1.0\], “first_atoms”: \[1,
  > > 17\], “last_atoms”: \[3, 19\], “types”: \[“s”\]
  > >
  > > </div>
  >
  > }
  >
  > </div>

  \]\]

  Note that a type of None will default to a charge constraint (which
  can also be accessed by requesting a type of “c” or “charge”).

  2\. For a CDFT-CI multi-reference calculation: cdft_constraints=\[

  > <div>
  >
  > \[  
  > {  
  > “value”: 1.0, “coefficients”: \[1.0\], “first_atoms”: \[1\],
  > “last_atoms”: \[27\], “types”: \[“c”\]
  >
  > }, {
  >
  > > <div>
  > >
  > > ”value”: 0.0, “coefficients”: \[1.0\], “first_atoms”: \[1\],
  > > “last_atoms”: \[27\], “types”: \[“s”\]
  > >
  > > </div>
  >
  > },
  >
  > \], \[
  >
  > > <div>
  > >
  > > {  
  > > “value”: 0.0, “coefficients”: \[1.0\], “first_atoms”: \[1\],
  > > “last_atoms”: \[27\], “types”: \[“c”\]
  > >
  > > }, {
  > >
  > > > <div>
  > > >
  > > > ”value”: -1.0, “coefficients”: \[1.0\], “first_atoms”: \[1\],
  > > > “last_atoms”: \[27\], “types”: \[“s”\]
  > > >
  > > > </div>
  > >
  > > },
  > >
  > > </div>
  >
  > \]
  >
  > </div>

  \]

- **overwrite_inputs** (*dict*) –

  Dictionary of QChem input sections to add or overwrite variables. The
  currently available sections (keys) are rem, pcm, solvent, smx, opt,
  scan, van_der_waals, and plots. The value of each key is a dictionary
  of key value pairs relevant to that section. For example, to add a new
  variable to the rem section that sets symmetry to false, use

  overwrite_inputs = {“rem”: {“symmetry”: “false”}}

  **Note that if something like basis is added to the rem dict it will
  overwrite the default basis.**

  **Note that supplying a van_der_waals section here will automatically
  modify the PCM “radii” setting to “read”.**

  **Note that all keys must be given as strings, even when they are
  numbers!**

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">OptSet</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">molecule</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">basis_set</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'def2-svpd'</span></span>*, *<span class="n"><span class="pre">scf_algorithm</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'diis'</span></span>*, *<span class="n"><span class="pre">qchem_version</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">5</span></span>*, *<span class="n"><span class="pre">dft_rung</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">4</span></span>*, *<span class="n"><span class="pre">pcm_dielectric</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">isosvp_dielectric</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">smd_solvent</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">cmirs_solvent</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'water'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'acetonitrile'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'dimethyl</span> <span class="pre">sulfoxide'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cyclohexane'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'benzene'</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">custom_smd</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">max_scf_cycles</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">100</span></span>*, *<span class="n"><span class="pre">plot_cubes</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">output_wavefunction</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">nbo_params</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">opt_variables</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">geom_opt_max_cycles</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">200</span></span>*, *<span class="n"><span class="pre">geom_opt</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">cdft_constraints</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">overwrite_inputs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/sets.py#L878-L1088"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.sets.OptSet" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.qchem.sets.QChemDictSet"
class="reference internal"
title="pymatgen.io.qchem.sets.QChemDictSet"><span class="pre"><code
class="sourceCode python">QChemDictSet</code></span></a>

QChemDictSet for a geometry optimization.

Parameters<span class="colon">:</span>  
- **molecule** (*Pymatgen Molecule object*)

- **job_type** (*str*) – QChem job type to run. Valid options are “opt”
  for optimization, “sp” for single point, “freq” for frequency
  calculation, or “force” for force evaluation.

- **basis_set** (*str*) – Basis set to use. (Default: “def2-svpd”)

- **scf_algorithm** (*str*) – Algorithm to use for converging the SCF.
  Recommended choices are “DIIS”, “GDM”, and “DIIS_GDM”. Other
  algorithms supported by Qchem’s GEN_SCFMAN module will also likely
  perform well. Refer to the QChem manual for further details. (Default:
  “diis”)

- **qchem_version** (*int*) – Which major version of Q-Chem will be run.
  Supports 5 and 6. (Default: 5)

- **dft_rung** (*int*) –

  Select the rung on “Jacob’s Ladder of Density Functional
  Approximations” in order of increasing accuracy/cost. For each rung,
  we have prescribed one functional based on our experience, available
  benchmarks, and the suggestions of the Q-Chem manual: 1 (LSDA) = SPW92
  2 (GGA) = B97-D3(BJ) 3 (metaGGA) = B97M-V 4 (hybrid metaGGA) = ωB97M-V
  5 (double hybrid metaGGA) = ωB97M-(2).

  (Default: 4)

  To set a functional not given by one of the above, set the
  overwrite_inputs argument to {“method”:”\<NAME OF FUNCTIONAL\>”}

- **pcm_dielectric** (*float*) –

  Dielectric constant to use for PCM implicit solvation model. (Default:
  None) If supplied, will set up the \$pcm section of the input file for
  a C-PCM calculation. Other types of PCM calculations (e.g., IEF-PCM,
  SS(V)PE, etc.) may be requested by passing custom keywords to
  overwrite_inputs, e.g. overwrite_inputs = {“pcm”: {“theory”: “ssvpe”}}
  Refer to the QChem manual for further details on the models available.

  **Note that only one of pcm_dielectric, isosvp_dielectric,
  smd_solvent, or cmirs_solvent may be set.**

- **isosvp_dielectric** (*float*) –

  Dielectric constant to use for isodensity SS(V)PE implicit solvation
  model. (Default: None). If supplied, will set solvent_method to
  “isosvp” and populate the \$svp section of the input file with
  appropriate parameters.

  **Note that only one of pcm_dielectric, isosvp_dielectric,
  smd_solvent, or cmirs_solvent may be set.**

- **smd_solvent** (*str*) –

  Solvent to use for SMD implicit solvation model. (Default: None)
  Examples include “water”, “ethanol”, “methanol”, and “acetonitrile”.
  Refer to the QChem manual for a complete list of solvents available.
  To define a custom solvent, set this argument to “custom” and populate
  custom_smd with the necessary parameters.

  **Note that only one of pcm_dielectric, isosvp_dielectric,
  smd_solvent, or cmirs_solvent may be set.**

- **cmirs_solvent** (*str*) –

  Solvent to use for the CMIRS implicit solvation model. (Default:
  None). Only 5 solvents are presently available as of Q-Chem 6:
  “water”, “benzene”, “cyclohexane”, “dimethyl sulfoxide”, and
  “acetonitrile”. Note that selection of a solvent here will also
  populate the iso SS(V)PE dielectric constant, because CMIRS uses the
  isodensity SS(V)PE model to compute electrostatics.

  **Note that only one of pcm_dielectric, isosvp_dielectric,
  smd_solvent, or cmirs_solvent may be set.**

- **custom_smd** (*str*) – List of parameters to define a custom solvent
  in SMD. (Default: None) Must be given as a string of seven comma
  separated values in the following order: “dielectric, refractive
  index, acidity, basicity, surface tension, aromaticity,
  electronegative halogenicity” Refer to the QChem manual for further
  details.

- **max_scf_cycles** (*int*) – Maximum number of SCF iterations.
  (Default: 100)

- **geom_opt_max_cycles** (*int*) – Maximum number of geometry
  optimization iterations. (Default: 200)

- **geom_opt** (*dict*) – A dict containing parameters for the
  \$geom_opt section of the Q-Chem input file, which control the new
  geometry optimizer available starting in version 5.4.2. The new
  optimizer remains under development but was officially released and
  became the default optimizer in Q-Chem version 6.0.0. Note that for
  version 5.4.2, the new optimizer must be explicitly requested by
  passing in a dictionary (empty or otherwise) for this input parameter.
  (Default: False)

- **plot_cubes** (*bool*) – Whether to write CUBE files of the electron
  density. (Default: False)

- **output_wavefunction** (*bool*) – Whether to write a wavefunction
  ([<span id="id6" class="problematic">\*</span>](#id5).wfn) file of the
  electron density (Default: False)

- **vdw_mode** (*'atomic'* *\|* *'sequential'*) – Method of specifying
  custom van der Waals radii. Applies only if you are using
  overwrite_inputs to add a \$van_der_waals section to the input. In
  ‘atomic’ mode (default), dict keys represent the atomic number
  associated with each radius (e.g., ‘12’ = carbon). In ‘sequential’
  mode, dict keys represent the sequential position of a single specific
  atom in the input structure.

- **cdft_constraints** (*list* *of* *lists* *of* *dicts*) –

  A list of lists of dictionaries, where each dictionary represents a
  charge constraint in the cdft section of the QChem input file.

  Each entry in the main list represents one state (allowing for
  multi-configuration calculations using constrained density functional
  theory - configuration interaction (CDFT-CI). Each state is
  represented by a list, which itself contains some number of
  constraints (dictionaries).

  Ex:

  1.  For a single-state calculation with two constraints:

  > <div>
  >
  > cdft_constraints=\[\[  
  > {  
  > “value”: 1.0, “coefficients”: \[1.0\], “first_atoms”: \[1\],
  > “last_atoms”: \[2\], “types”: \[None\]
  >
  > }, {
  >
  > > <div>
  > >
  > > ”value”: 2.0, “coefficients”: \[1.0, -1.0\], “first_atoms”: \[1,
  > > 17\], “last_atoms”: \[3, 19\], “types”: \[“s”\]
  > >
  > > </div>
  >
  > }
  >
  > </div>

  \]\]

  Note that a type of None will default to a charge constraint (which
  can also be accessed by requesting a type of “c” or “charge”).

  2\. For a CDFT-CI multi-reference calculation: cdft_constraints=\[

  > <div>
  >
  > \[  
  > {  
  > “value”: 1.0, “coefficients”: \[1.0\], “first_atoms”: \[1\],
  > “last_atoms”: \[27\], “types”: \[“c”\]
  >
  > }, {
  >
  > > <div>
  > >
  > > ”value”: 0.0, “coefficients”: \[1.0\], “first_atoms”: \[1\],
  > > “last_atoms”: \[27\], “types”: \[“s”\]
  > >
  > > </div>
  >
  > },
  >
  > \], \[
  >
  > > <div>
  > >
  > > {  
  > > “value”: 0.0, “coefficients”: \[1.0\], “first_atoms”: \[1\],
  > > “last_atoms”: \[27\], “types”: \[“c”\]
  > >
  > > }, {
  > >
  > > > <div>
  > > >
  > > > ”value”: -1.0, “coefficients”: \[1.0\], “first_atoms”: \[1\],
  > > > “last_atoms”: \[27\], “types”: \[“s”\]
  > > >
  > > > </div>
  > >
  > > },
  > >
  > > </div>
  >
  > \]
  >
  > </div>

  \]

- **overwrite_inputs** (*dict*) –

  Dictionary of QChem input sections to add or overwrite variables. The
  currently available sections (keys) are rem, pcm, solvent, smx, opt,
  scan, van_der_waals, and plots. The value of each key is a dictionary
  of key value pairs relevant to that section. For example, to add a new
  variable to the rem section that sets symmetry to false, use

  overwrite_inputs = {“rem”: {“symmetry”: “false”}}

  **Note that if something like basis is added to the rem dict it will
  overwrite the default basis.**

  **Note that supplying a van_der_waals section here will automatically
  modify the PCM “radii” setting to “read”.**

  **Note that all keys must be given as strings, even when they are
  numbers!**

- **vdw_mode** – Method of specifying custom van der Waals radii.
  Applies only if you are using overwrite_inputs to add a
  \$van_der_waals section to the input. In ‘atomic’ mode (default), dict
  keys represent the atomic number associated with each radius (e.g.,
  ‘12’ = carbon). In ‘sequential’ mode, dict keys represent the
  sequential position of a single specific atom in the input structure.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">PESScanSet</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">molecule</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">basis_set</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'def2-svpd'</span></span>*, *<span class="n"><span class="pre">scf_algorithm</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'diis'</span></span>*, *<span class="n"><span class="pre">qchem_version</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">5</span></span>*, *<span class="n"><span class="pre">dft_rung</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">4</span></span>*, *<span class="n"><span class="pre">pcm_dielectric</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">isosvp_dielectric</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">smd_solvent</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">cmirs_solvent</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'water'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'acetonitrile'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'dimethyl</span> <span class="pre">sulfoxide'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cyclohexane'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'benzene'</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">custom_smd</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">max_scf_cycles</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">100</span></span>*, *<span class="n"><span class="pre">plot_cubes</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">output_wavefunction</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">nbo_params</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">opt_variables</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">scan_variables</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">overwrite_inputs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">vdw_mode</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'atomic'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'sequential'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'atomic'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/sets.py#L1615-L1764"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.sets.PESScanSet" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.qchem.sets.QChemDictSet"
class="reference internal"
title="pymatgen.io.qchem.sets.QChemDictSet"><span class="pre"><code
class="sourceCode python">QChemDictSet</code></span></a>

QChemDictSet for a potential energy surface scan (PES_SCAN) calculation,
used primarily to identify possible transition states or to sample
different geometries. Note: Because there are no defaults that can be
used for a PES scan (the variables are completely dependent on the
molecular structure), by default scan_variables = None. However, a PES
Scan job should not be run with less than one variable (or more than two
variables).

Parameters<span class="colon">:</span>  
- **molecule** (*Pymatgen Molecule object*)

- **opt_variables** (*dict*) –

  A dictionary of opt sections, where each opt section is a key and the
  corresponding values are a list of strings. Strings must be formatted
  as instructed by the QChem manual. The different opt sections are:
  CONSTRAINT, FIXED, DUMMY, and CONNECT.

  Ex. opt = {“CONSTRAINT”: \[“tors 2 3 4 5 25.0”, “tors 2 5 7 9 80.0”\],
  “FIXED”: \[“2 XY”\]}

- **scan_variables** (*dict*) –

  A dictionary of scan variables. Because two constraints of the same
  type are allowed (for instance, two torsions or two bond stretches),
  each TYPE of variable (stre, bend, tors) should be its own key in the
  dict, rather than each variable. Note that the total number of
  variable (sum of lengths of all lists) CANNOT be more than two.

  Ex. scan_variables = {“stre”: \[“3 6 1.5 1.9 0.1”\], “tors”: \[“1 2 3
  4 -180 180 15”\]}

- **basis_set** (*str*) – Basis set to use. (Default: “def2-svpd”)

- **scf_algorithm** (*str*) – Algorithm to use for converging the SCF.
  Recommended choices are “DIIS”, “GDM”, and “DIIS_GDM”. Other
  algorithms supported by Qchem’s GEN_SCFMAN module will also likely
  perform well. Refer to the QChem manual for further details. (Default:
  “diis”)

- **qchem_version** (*int*) – Which major version of Q-Chem will be run.
  Supports 5 and 6. (Default: 5)

- **dft_rung** (*int*) –

  Select the rung on “Jacob’s Ladder of Density Functional
  Approximations” in order of increasing accuracy/cost. For each rung,
  we have prescribed one functional based on our experience, available
  benchmarks, and the suggestions of the Q-Chem manual: 1 (LSDA) = SPW92
  2 (GGA) = B97-D3(BJ) 3 (metaGGA) = B97M-V 4 (hybrid metaGGA) = ωB97M-V
  5 (double hybrid metaGGA) = ωB97M-(2)

  (Default: 4)

  To set a functional not given by one of the above, set the
  overwrite_inputs argument to {“method”:”\<NAME OF FUNCTIONAL\>”}

- **pcm_dielectric** (*float*) –

  Dielectric constant to use for PCM implicit solvation model. (Default:
  None) If supplied, will set up the \$pcm section of the input file for
  a C-PCM calculation. Other types of PCM calculations (e.g., IEF-PCM,
  SS(V)PE, etc.) may be requested by passing custom keywords to
  overwrite_inputs, e.g. overwrite_inputs = {“pcm”: {“theory”: “ssvpe”}}
  Refer to the QChem manual for further details on the models available.

  **Note that only one of pcm_dielectric, isosvp_dielectric,
  smd_solvent, or cmirs_solvent may be set.**

- **isosvp_dielectric** (*float*) –

  Dielectric constant to use for isodensity SS(V)PE implicit solvation
  model. (Default: None). If supplied, will set solvent_method to
  “isosvp” and populate the \$svp section of the input file with
  appropriate parameters.

  **Note that only one of pcm_dielectric, isosvp_dielectric,
  smd_solvent, or cmirs_solvent may be set.**

- **smd_solvent** (*str*) –

  Solvent to use for SMD implicit solvation model. (Default: None)
  Examples include “water”, “ethanol”, “methanol”, and “acetonitrile”.
  Refer to the QChem manual for a complete list of solvents available.
  To define a custom solvent, set this argument to “custom” and populate
  custom_smd with the necessary parameters.

  **Note that only one of pcm_dielectric, isosvp_dielectric,
  smd_solvent, or cmirs_solvent may be set.**

- **cmirs_solvent** (*str*) –

  Solvent to use for the CMIRS implicit solvation model. (Default:
  None). Only 5 solvents are presently available as of Q-Chem 6:
  “water”, “benzene”, “cyclohexane”, “dimethyl sulfoxide”, and
  “acetonitrile”. Note that selection of a solvent here will also
  populate the iso SS(V)PE dielectric constant, because CMIRS uses the
  isodensity SS(V)PE model to compute electrostatics.

  **Note that only one of pcm_dielectric, isosvp_dielectric,
  smd_solvent, or cmirs_solvent may be set.**

- **custom_smd** (*str*) – List of parameters to define a custom solvent
  in SMD. (Default: None) Must be given as a string of seven comma
  separated values in the following order: “dielectric, refractive
  index, acidity, basicity, surface tension, aromaticity,
  electronegative halogenicity” Refer to the QChem manual for further
  details.

- **max_scf_cycles** (*int*) – Maximum number of SCF iterations.
  (Default: 100)

- **plot_cubes** (*bool*) – Whether to write CUBE files of the electron
  density. (Default: False)

- **output_wavefunction** (*bool*) – Whether to write a wavefunction
  ([<span id="id8" class="problematic">\*</span>](#id7).wfn) file of the
  electron density (Default: False)

- **overwrite_inputs** (*dict*) –

  Dictionary of QChem input sections to add or overwrite variables. The
  currently available sections (keys) are rem, pcm, solvent, smx, opt,
  scan, van_der_waals, and plots. The value of each key is a dictionary
  of key value pairs relevant to that section. For example, to add a new
  variable to the rem section that sets symmetry to false, use

  overwrite_inputs = {“rem”: {“symmetry”: “false”}}

  **Note that if something like basis is added to the rem dict it will
  overwrite the default basis.**

  **Note that supplying a van_der_waals section here will automatically
  modify the PCM “radii” setting to “read”.**

  **Note that all keys must be given as strings, even when they are
  numbers!**

- **vdw_mode** (*'atomic'* *\|* *'sequential'*) – Method of specifying
  custom van der Waals radii. Applies only if you are using
  overwrite_inputs to add a \$van_der_waals section to the input. In
  ‘atomic’ mode (default), dict keys represent the atomic number
  associated with each radius (e.g., ‘12’ = carbon). In ‘sequential’
  mode, dict keys represent the sequential position of a single specific
  atom in the input structure.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">QChemDictSet</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">molecule</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">job_type</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">basis_set</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">scf_algorithm</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">qchem_version</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">5</span></span>*, *<span class="n"><span class="pre">dft_rung</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">4</span></span>*, *<span class="n"><span class="pre">pcm_dielectric</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">isosvp_dielectric</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">smd_solvent</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">cmirs_solvent</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'water'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'acetonitrile'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'dimethyl</span> <span class="pre">sulfoxide'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cyclohexane'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'benzene'</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">custom_smd</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">opt_variables</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">scan_variables</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">max_scf_cycles</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">100</span></span>*, *<span class="n"><span class="pre">geom_opt_max_cycles</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">200</span></span>*, *<span class="n"><span class="pre">plot_cubes</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">output_wavefunction</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">nbo_params</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">geom_opt</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">cdft_constraints</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">almo_coupling_states</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">overwrite_inputs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">vdw_mode</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'atomic'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'sequential'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'atomic'</span></span>*, *<span class="n"><span class="pre">extra_scf_print</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/sets.py#L130-L647"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.sets.QChemDictSet" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.qchem.inputs.QCInput" class="reference internal"
title="pymatgen.io.qchem.inputs.QCInput"><span class="pre"><code
class="sourceCode python">QCInput</code></span></a>

Build a QCInput given all the various input parameters. Can be extended
by standard implementations below.

Parameters<span class="colon">:</span>  
- **molecule** (*Pymatgen Molecule object*) – Molecule to run QChem on.

- **job_type** (*str*) – QChem job type to run. Valid options are “opt”
  for optimization, “sp” for single point, “freq” for frequency
  calculation, or “force” for force evaluation.

- **basis_set** (*str*) – Basis set to use. For example, “def2-tzvpd”.

- **scf_algorithm** (*str*) – Algorithm to use for converging the SCF.
  Recommended choices are “DIIS”, “GDM”, and “DIIS_GDM”. Other
  algorithms supported by Qchem’s GEN_SCFMAN module will also likely
  perform well. Refer to the QChem manual for further details.

- **qchem_version** (*int*) – Which major version of Q-Chem will be run.
  Supports 5 and 6. (Default: 5)

- **dft_rung** (*int*) –

  Select the rung on “Jacob’s Ladder of Density Functional
  Approximations” in order of increasing accuracy/cost. For each rung,
  we have prescribed one functional based on our experience, available
  benchmarks, and the suggestions of the Q-Chem manual: 1 (LSDA) = SPW92
  2 (GGA) = B97-D3(BJ) 3 (metaGGA) = B97M-V 4 (hybrid metaGGA) = ωB97M-V
  5 (double hybrid metaGGA) = ωB97M-(2).

  (Default: 4)

  To set a functional not given by one of the above, set the
  overwrite_inputs argument to {“method”:”\<NAME OF FUNCTIONAL\>”}

- **pcm_dielectric** (*float*) –

  Dielectric constant to use for PCM implicit solvation model. (Default:
  None) If supplied, will set up the \$pcm section of the input file for
  a C-PCM calculation. Other types of PCM calculations (e.g., IEF-PCM,
  SS(V)PE, etc.) may be requested by passing custom keywords to
  overwrite_inputs, e.g. overwrite_inputs = {“pcm”: {“theory”: “ssvpe”}}
  Refer to the QChem manual for further details on the models available.

  **Note that only one of pcm_dielectric, isosvp_dielectric,
  smd_solvent, or cmirs_solvent may be set.**

- **isosvp_dielectric** (*float*) –

  Dielectric constant to use for isodensity SS(V)PE implicit solvation
  model. (Default: None). If supplied, will set solvent_method to
  “isosvp” and populate the \$svp section of the input file with
  appropriate parameters.

  **Note that only one of pcm_dielectric, isosvp_dielectric,
  smd_solvent, or cmirs_solvent may be set.**

- **smd_solvent** (*str*) –

  Solvent to use for SMD implicit solvation model. (Default: None)
  Examples include “water”, “ethanol”, “methanol”, and “acetonitrile”.
  Refer to the QChem manual for a complete list of solvents available.
  To define a custom solvent, set this argument to “custom” and populate
  custom_smd with the necessary parameters.

  **Note that only one of pcm_dielectric, isosvp_dielectric,
  smd_solvent, or cmirs_solvent may be set.**

- **cmirs_solvent** (*str*) –

  Solvent to use for the CMIRS implicit solvation model. (Default:
  None). Only 5 solvents are presently available as of Q-Chem 6:
  “water”, “benzene”, “cyclohexane”, “dimethyl sulfoxide”, and
  “acetonitrile”. Note that selection of a solvent here will also
  populate the iso SS(V)PE dielectric constant, because CMIRS uses the
  isodensity SS(V)PE model to compute electrostatics.

  **Note that only one of pcm_dielectric, isosvp_dielectric,
  smd_solvent, or cmirs_solvent may be set.**

- **custom_smd** (*str*) – List of parameters to define a custom solvent
  in SMD. (Default: None) Must be given as a string of seven comma
  separated values in the following order: “dielectric, refractive
  index, acidity, basicity, surface tension, aromaticity,
  electronegative halogenicity” Refer to the QChem manual for further
  details.

- **opt_variables** (*dict*) –

  A dictionary of opt sections, where each opt section is a key and the
  corresponding values are a list of strings. Strings must be formatted
  as instructed by the QChem manual. The different opt sections are:
  CONSTRAINT, FIXED, DUMMY, and CONNECT.

  Ex. opt = {“CONSTRAINT”: \[“tors 2 3 4 5 25.0”, “tors 2 5 7 9 80.0”\],
  “FIXED”: \[“2 XY”\]}

- **scan_variables** (*dict*) –

  A dictionary of scan variables. Because two constraints of the same
  type are allowed (for instance, two torsions or two bond stretches),
  each TYPE of variable (stre, bend, tors) should be its own key in the
  dict, rather than each variable. Note that the total number of
  variable (sum of lengths of all lists) CANNOT be more than two.

  Ex. scan_variables = {“stre”: \[“3 6 1.5 1.9 0.1”\], “tors”: \[“1 2 3
  4 -180 180 15”\]}

- **max_scf_cycles** (*int*) – Maximum number of SCF iterations.
  (Default: 100)

- **geom_opt_max_cycles** (*int*) – Maximum number of geometry
  optimization iterations. (Default: 200)

- **plot_cubes** (*bool*) – Whether to write CUBE files of the electron
  density. (Default: False)

- **output_wavefunction** (*bool*) – Whether to write a wavefunction
  ([<span id="id10" class="problematic">\*</span>](#id9).wfn) file of
  the electron density (Default: False)

- **nbo_params** (*dict*) – A dict containing the desired NBO params.
  Note that a key:value pair of “version”:7 will trigger NBO7 analysis.
  Otherwise, NBO5 analysis will be performed, including if an empty dict
  is passed. Besides a key of “version”, all other key:value pairs will
  be written into the \$nbo section of the QChem input file. (Default:
  False)

- **geom_opt** (*dict*) – A dict containing parameters for the
  \$geom_opt section of the Q-Chem input file, which control the new
  geometry optimizer available starting in version 5.4.2. The new
  optimizer remains under development but was officially released and
  became the default optimizer in Q-Chem version 6.0.0. Note that for
  version 5.4.2, the new optimizer must be explicitly requested by
  passing in a dictionary (empty or otherwise) for this input parameter.
  (Default: False)

- **vdw_mode** (*'atomic'* *\|* *'sequential'*) –

  Method of specifying custom van der Waals radii. Applies only if you
  are using overwrite_inputs to add a \$van_der_waals section to the
  input. In ‘atomic’ mode (default), dict keys represent the atomic
  number associated with each radius (e.g., ‘12’ = carbon). In
  ‘sequential’ mode, dict keys represent the sequential position of a
  single specific atom in the input structure.

  > <div>
  >
  > cdft_constraints (list of lists of dicts):
  >
  > </div>

  A list of lists of dictionaries, where each dictionary represents a
  charge constraint in the cdft section of the QChem input file.

  Each entry in the main list represents one state (allowing for
  multi-configuration calculations using constrained density functional
  theory - configuration interaction (CDFT-CI). Each state is
  represented by a list, which itself contains some number of
  constraints (dictionaries).

  Ex:

  1.  For a single-state calculation with two constraints:

  > <div>
  >
  > cdft_constraints=\[\[  
  > {  
  > “value”: 1.0, “coefficients”: \[1.0\], “first_atoms”: \[1\],
  > “last_atoms”: \[2\], “types”: \[None\]
  >
  > }, {
  >
  > > <div>
  > >
  > > ”value”: 2.0, “coefficients”: \[1.0, -1.0\], “first_atoms”: \[1,
  > > 17\], “last_atoms”: \[3, 19\], “types”: \[“s”\]
  > >
  > > </div>
  >
  > }
  >
  > </div>

  \]\]

  Note that a type of None will default to a charge constraint (which
  can also be accessed by requesting a type of “c” or “charge”).

  2\. For a CDFT-CI multi-reference calculation: cdft_constraints=\[

  > <div>
  >
  > \[  
  > {  
  > “value”: 1.0, “coefficients”: \[1.0\], “first_atoms”: \[1\],
  > “last_atoms”: \[27\], “types”: \[“c”\]
  >
  > }, {
  >
  > > <div>
  > >
  > > ”value”: 0.0, “coefficients”: \[1.0\], “first_atoms”: \[1\],
  > > “last_atoms”: \[27\], “types”: \[“s”\]
  > >
  > > </div>
  >
  > },
  >
  > \], \[
  >
  > > <div>
  > >
  > > {  
  > > “value”: 0.0, “coefficients”: \[1.0\], “first_atoms”: \[1\],
  > > “last_atoms”: \[27\], “types”: \[“c”\]
  > >
  > > }, {
  > >
  > > > <div>
  > > >
  > > > ”value”: -1.0, “coefficients”: \[1.0\], “first_atoms”: \[1\],
  > > > “last_atoms”: \[27\], “types”: \[“s”\]
  > > >
  > > > </div>
  > >
  > > },
  > >
  > > </div>
  >
  > \]
  >
  > </div>

  \]

- **cdft_constraints** (*list\[list\[dict\]\]*) – A list of lists of
  dictionaries, where each

- **almo_coupling_states** (*list* *of* *lists* *of* *int 2-tuples*) –

  A list of lists of int 2-tuples used for calculations of diabatization
  and state coupling calculations relying on the absolutely localized
  molecular orbitals (ALMO) methodology. Each entry in the main list
  represents a single state (two states are included in an ALMO
  calculation). Within a single state, each 2-tuple represents the
  charge and spin multiplicity of a single fragment. ex:
  almo_coupling_states=\[

  > <div>
  >
  > > <div>
  > >
  > > \[  
  > > (1, 2), (0, 1)
  > >
  > > \], \[
  > >
  > > > <div>
  > > >
  > > > (0, 1), (1, 2)
  > > >
  > > > </div>
  > >
  > > \]
  > >
  > > </div>
  >
  > \]
  >
  > </div>

- **overwrite_inputs** (*dict*) –

  Dictionary of QChem input sections to add or overwrite variables. The
  currently available sections (keys) are rem, pcm, solvent, smx, opt,
  scan, van_der_waals, and plots. The value of each key is a dictionary
  of key value pairs relevant to that section. For example, to add a new
  variable to the rem section that sets symmetry to false, use

  overwrite_inputs = {“rem”: {“symmetry”: “false”}}

  **Note that if something like basis is added to the rem dict it will
  overwrite the default basis.**

  **Note that supplying a van_der_waals section here will automatically
  modify the PCM “radii” setting to “read”.**

  **Note that all keys must be given as strings, even when they are
  numbers!**

- **vdw_mode** – Method of specifying custom van der Waals radii.
  Applies only if you are using overwrite_inputs to add a
  \$van_der_waals section to the input. In ‘atomic’ mode (default), dict
  keys represent the atomic number associated with each radius (e.g.,
  ‘12’ = carbon). In ‘sequential’ mode, dict keys represent the
  sequential position of a single specific atom in the input structure.

- **extra_scf_print** (*bool*) – Whether to store extra information
  generated from the SCF cycle. If switched on, the Fock Matrix,
  coefficients of MO and the density matrix will be stored.

<span class="sig-name descname"><span class="pre">write</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">input_file</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/sets.py#L639-L647"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.sets.QChemDictSet.write" class="headerlink"
title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
**input_file** (*PathLike*) – Filename.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">SinglePointSet</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">molecule</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">basis_set</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'def2-tzvpd'</span></span>*, *<span class="n"><span class="pre">scf_algorithm</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'diis'</span></span>*, *<span class="n"><span class="pre">qchem_version</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">5</span></span>*, *<span class="n"><span class="pre">dft_rung</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">4</span></span>*, *<span class="n"><span class="pre">pcm_dielectric</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">isosvp_dielectric</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">smd_solvent</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">cmirs_solvent</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'water'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'acetonitrile'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'dimethyl</span> <span class="pre">sulfoxide'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cyclohexane'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'benzene'</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">custom_smd</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">max_scf_cycles</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">100</span></span>*, *<span class="n"><span class="pre">plot_cubes</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">output_wavefunction</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">nbo_params</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">vdw_mode</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'atomic'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'sequential'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'atomic'</span></span>*, *<span class="n"><span class="pre">cdft_constraints</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">almo_coupling_states</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">extra_scf_print</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">overwrite_inputs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/sets.py#L650-L875"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.sets.SinglePointSet" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.qchem.sets.QChemDictSet"
class="reference internal"
title="pymatgen.io.qchem.sets.QChemDictSet"><span class="pre"><code
class="sourceCode python">QChemDictSet</code></span></a>

QChemDictSet for a single point calculation.

Parameters<span class="colon">:</span>  
- **molecule** (*Pymatgen Molecule object*)

- **job_type** (*str*) – QChem job type to run. Valid options are “opt”
  for optimization, “sp” for single point, “freq” for frequency
  calculation, or “force” for force evaluation.

- **basis_set** (*str*) – Basis set to use. (Default: “def2-tzvpd”)

- **scf_algorithm** (*str*) – Algorithm to use for converging the SCF.
  Recommended choices are “DIIS”, “GDM”, and “DIIS_GDM”. Other
  algorithms supported by Qchem’s GEN_SCFMAN module will also likely
  perform well. Refer to the QChem manual for further details. (Default:
  “diis”)

- **qchem_version** (*int*) – Which major version of Q-Chem will be run.
  Supports 5 and 6. (Default: 5)

- **dft_rung** (*int*) –

  Select the rung on “Jacob’s Ladder of Density Functional
  Approximations” in order of increasing accuracy/cost. For each rung,
  we have prescribed one functional based on our experience, available
  benchmarks, and the suggestions of the Q-Chem manual: 1 (LSDA) = SPW92
  2 (GGA) = B97-D3(BJ) 3 (metaGGA) = B97M-V 4 (hybrid metaGGA) = ωB97M-V
  5 (double hybrid metaGGA) = ωB97M-(2).

  (Default: 4)

  To set a functional not given by one of the above, set the
  overwrite_inputs argument to {“method”:”\<NAME OF FUNCTIONAL\>”}

- **pcm_dielectric** (*float*) –

  Dielectric constant to use for PCM implicit solvation model. (Default:
  None) If supplied, will set up the \$pcm section of the input file for
  a C-PCM calculation. Other types of PCM calculations (e.g., IEF-PCM,
  SS(V)PE, etc.) may be requested by passing custom keywords to
  overwrite_inputs, e.g. overwrite_inputs = {“pcm”: {“theory”: “ssvpe”}}
  Refer to the QChem manual for further details on the models available.

  **Note that only one of pcm_dielectric, isosvp_dielectric,
  smd_solvent, or cmirs_solvent may be set.**

- **isosvp_dielectric** (*float*) –

  Dielectric constant to use for isodensity SS(V)PE implicit solvation
  model. (Default: None). If supplied, will set solvent_method to
  “isosvp” and populate the \$svp section of the input file with
  appropriate parameters. Note that due to limitations in Q-Chem, use of
  the ISOSVP or CMIRS solvent models will disable the GEN_SCFMAN
  algorithm, which may limit compatible choices for scf_algorithm.

  **Note that only one of pcm_dielectric, isosvp_dielectric,
  smd_solvent, or cmirs_solvent may be set.**

- **smd_solvent** (*str*) –

  Solvent to use for SMD implicit solvation model. (Default: None)
  Examples include “water”, “ethanol”, “methanol”, and “acetonitrile”.
  Refer to the QChem manual for a complete list of solvents available.
  To define a custom solvent, set this argument to “custom” and populate
  custom_smd with the necessary parameters.

  **Note that only one of pcm_dielectric, isosvp_dielectric,
  smd_solvent, or cmirs_solvent may be set.**

- **cmirs_solvent** (*str*) –

  Solvent to use for the CMIRS implicit solvation model. (Default:
  None). Only 5 solvents are presently available as of Q-Chem 6:
  “water”, “benzene”, “cyclohexane”, “dimethyl sulfoxide”, and
  “acetonitrile”. Note that selection of a solvent here will also
  populate the iso SS(V)PE dielectric constant, because CMIRS uses the
  isodensity SS(V)PE model to compute electrostatics. Note also that due
  to limitations in Q-Chem, use of the ISOSVP or CMIRS solvent models
  will disable the GEN_SCFMAN algorithm, which may limit compatible
  choices for scf_algorithm.

  **Note that only one of pcm_dielectric, isosvp_dielectric,
  smd_solvent, or cmirs_solvent may be set.**

- **custom_smd** (*str*) – List of parameters to define a custom solvent
  in SMD. (Default: None) Must be given as a string of seven comma
  separated values in the following order: “dielectric, refractive
  index, acidity, basicity, surface tension, aromaticity,
  electronegative halogenicity” Refer to the QChem manual for further
  details.

- **max_scf_cycles** (*int*) – Maximum number of SCF iterations.
  (Default: 100)

- **plot_cubes** (*bool*) – Whether to write CUBE files of the electron
  density. (Default: False)

- **output_wavefunction** (*bool*) – Whether to write a wavefunction
  ([<span id="id12" class="problematic">\*</span>](#id11).wfn) file of
  the electron density (Default: False)

- **cdft_constraints** (*list* *of* *lists* *of* *dicts*) –

  A list of lists of dictionaries, where each dictionary represents a
  charge constraint in the cdft section of the QChem input file.

  Each entry in the main list represents one state (allowing for
  multi-configuration calculations using constrained density functional
  theory - configuration interaction (CDFT-CI). Each state is
  represented by a list, which itself contains some number of
  constraints (dictionaries).

  Ex:

  1.  For a single-state calculation with two constraints:

  > <div>
  >
  > cdft_constraints=\[\[  
  > {  
  > “value”: 1.0, “coefficients”: \[1.0\], “first_atoms”: \[1\],
  > “last_atoms”: \[2\], “types”: \[None\]
  >
  > }, {
  >
  > > <div>
  > >
  > > ”value”: 2.0, “coefficients”: \[1.0, -1.0\], “first_atoms”: \[1,
  > > 17\], “last_atoms”: \[3, 19\], “types”: \[“s”\]
  > >
  > > </div>
  >
  > }
  >
  > </div>

  \]\]

  Note that a type of None will default to a charge constraint (which
  can also be accessed by requesting a type of “c” or “charge”).

  2\. For a CDFT-CI multi-reference calculation: cdft_constraints=\[

  > <div>
  >
  > \[  
  > {  
  > “value”: 1.0, “coefficients”: \[1.0\], “first_atoms”: \[1\],
  > “last_atoms”: \[27\], “types”: \[“c”\]
  >
  > }, {
  >
  > > <div>
  > >
  > > ”value”: 0.0, “coefficients”: \[1.0\], “first_atoms”: \[1\],
  > > “last_atoms”: \[27\], “types”: \[“s”\]
  > >
  > > </div>
  >
  > },
  >
  > \], \[
  >
  > > <div>
  > >
  > > {  
  > > “value”: 0.0, “coefficients”: \[1.0\], “first_atoms”: \[1\],
  > > “last_atoms”: \[27\], “types”: \[“c”\]
  > >
  > > }, {
  > >
  > > > <div>
  > > >
  > > > ”value”: -1.0, “coefficients”: \[1.0\], “first_atoms”: \[1\],
  > > > “last_atoms”: \[27\], “types”: \[“s”\]
  > > >
  > > > </div>
  > >
  > > },
  > >
  > > </div>
  >
  > \]
  >
  > </div>

  \]

- **almo_coupling_states** (*list* *of* *lists* *of* *int 2-tuples*) –

  A list of lists of int 2-tuples used for calculations of diabatization
  and state coupling calculations relying on the absolutely localized
  molecular orbitals (ALMO) methodology. Each entry in the main list
  represents a single state (two states are included in an ALMO
  calculation). Within a single state, each 2-tuple represents the
  charge and spin multiplicity of a single fragment. ex:
  almo_coupling_states=\[

  > <div>
  >
  > > <div>
  > >
  > > \[  
  > > (1, 2), (0, 1)
  > >
  > > \], \[
  > >
  > > > <div>
  > > >
  > > > (0, 1), (1, 2)
  > > >
  > > > </div>
  > >
  > > \]
  > >
  > > </div>
  >
  > \]
  >
  > </div>

- **vdw_mode** (*'atomic'* *\|* *'sequential'*) – Method of specifying
  custom van der Waals radii. Applies only if you are using
  overwrite_inputs to add a \$van_der_waals section to the input. In
  ‘atomic’ mode (default), dict keys represent the atomic number
  associated with each radius (e.g., ‘12’ = carbon). In ‘sequential’
  mode, dict keys represent the sequential position of a single specific
  atom in the input structure.

- **overwrite_inputs** (*dict*) –

  Dictionary of QChem input sections to add or overwrite variables. The
  currently available sections (keys) are rem, pcm, solvent, smx, opt,
  scan, van_der_waals, and plots. The value of each key is a dictionary
  of key value pairs relevant to that section. For example, to add a new
  variable to the rem section that sets symmetry to false, use

  overwrite_inputs = {“rem”: {“symmetry”: “false”}}

  **Note that if something like basis is added to the rem dict it will
  overwrite the default basis.**

  **Note that supplying a van_der_waals section here will automatically
  modify the PCM “radii” setting to “read”.**

  **Note that all keys must be given as strings, even when they are
  numbers!**

- **vdw_mode** – Method of specifying custom van der Waals radii.
  Applies only if you are using overwrite_inputs to add a
  \$van_der_waals section to the input. In ‘atomic’ mode (default), dict
  keys represent the atomic number associated with each radius (e.g.,
  ‘12’ = carbon). In ‘sequential’ mode, dict keys represent the
  sequential position of a single specific atom in the input structure.

- **extra_scf_print** (*bool*) – Whether to store extra information
  generated from the SCF cycle. If switched on, the Fock Matrix,
  coefficients of MO and the density matrix will be stored.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">TransitionStateSet</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">molecule</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">basis_set</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'def2-svpd'</span></span>*, *<span class="n"><span class="pre">scf_algorithm</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'diis'</span></span>*, *<span class="n"><span class="pre">qchem_version</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">5</span></span>*, *<span class="n"><span class="pre">dft_rung</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">4</span></span>*, *<span class="n"><span class="pre">pcm_dielectric</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">isosvp_dielectric</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">smd_solvent</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">cmirs_solvent</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'water'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'acetonitrile'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'dimethyl</span> <span class="pre">sulfoxide'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cyclohexane'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'benzene'</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">custom_smd</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">max_scf_cycles</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">100</span></span>*, *<span class="n"><span class="pre">plot_cubes</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">output_wavefunction</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">nbo_params</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">opt_variables</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">geom_opt_max_cycles</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">200</span></span>*, *<span class="n"><span class="pre">geom_opt</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">overwrite_inputs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">vdw_mode</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'atomic'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/sets.py#L1091-L1226"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.sets.TransitionStateSet" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.qchem.sets.QChemDictSet"
class="reference internal"
title="pymatgen.io.qchem.sets.QChemDictSet"><span class="pre"><code
class="sourceCode python">QChemDictSet</code></span></a>

QChemDictSet for a transition-state search.

Parameters<span class="colon">:</span>  
- **molecule** (*Pymatgen Molecule object*)

- **basis_set** (*str*) – Basis set to use. (Default: “def2-svpd”)

- **scf_algorithm** (*str*) – Algorithm to use for converging the SCF.
  Recommended choices are “DIIS”, “GDM”, and “DIIS_GDM”. Other
  algorithms supported by Qchem’s GEN_SCFMAN module will also likely
  perform well. Refer to the QChem manual for further details. (Default:
  “diis”)

- **qchem_version** (*int*) – Which major version of Q-Chem will be run.
  Supports 5 and 6. (Default: 5)

- **dft_rung** (*int*) –

  Select the rung on “Jacob’s Ladder of Density Functional
  Approximations” in order of increasing accuracy/cost. For each rung,
  we have prescribed one functional based on our experience, available
  benchmarks, and the suggestions of the Q-Chem manual: 1 (LSDA) = SPW92
  2 (GGA) = B97-D3(BJ) 3 (metaGGA) = B97M-V 4 (hybrid metaGGA) = ωB97M-V
  5 (double hybrid metaGGA) = ωB97M-(2).

  (Default: 4)

  To set a functional not given by one of the above, set the
  overwrite_inputs argument to {“method”:”\<NAME OF FUNCTIONAL\>”}

- **pcm_dielectric** (*float*) –

  Dielectric constant to use for PCM implicit solvation model. (Default:
  None) If supplied, will set up the \$pcm section of the input file for
  a C-PCM calculation. Other types of PCM calculations (e.g., IEF-PCM,
  SS(V)PE, etc.) may be requested by passing custom keywords to
  overwrite_inputs, e.g. overwrite_inputs = {“pcm”: {“theory”: “ssvpe”}}
  Refer to the QChem manual for further details on the models available.

  **Note that only one of pcm_dielectric, isosvp_dielectric,
  smd_solvent, or cmirs_solvent may be set.**

- **isosvp_dielectric** (*float*) –

  Dielectric constant to use for isodensity SS(V)PE implicit solvation
  model. (Default: None). If supplied, will set solvent_method to
  “isosvp” and populate the \$svp section of the input file with
  appropriate parameters.

  **Note that only one of pcm_dielectric, isosvp_dielectric,
  smd_solvent, or cmirs_solvent may be set.**

- **smd_solvent** (*str*) –

  Solvent to use for SMD implicit solvation model. (Default: None)
  Examples include “water”, “ethanol”, “methanol”, and “acetonitrile”.
  Refer to the QChem manual for a complete list of solvents available.
  To define a custom solvent, set this argument to “custom” and populate
  custom_smd with the necessary parameters.

  **Note that only one of pcm_dielectric, isosvp_dielectric,
  smd_solvent, or cmirs_solvent may be set.**

- **cmirs_solvent** (*str*) –

  Solvent to use for the CMIRS implicit solvation model. (Default:
  None). Only 5 solvents are presently available as of Q-Chem 6:
  “water”, “benzene”, “cyclohexane”, “dimethyl sulfoxide”, and
  “acetonitrile”. Note that selection of a solvent here will also
  populate the iso SS(V)PE dielectric constant, because CMIRS uses the
  isodensity SS(V)PE model to compute electrostatics.

  **Note that only one of pcm_dielectric, isosvp_dielectric,
  smd_solvent, or cmirs_solvent may be set.**

- **custom_smd** (*str*) – List of parameters to define a custom solvent
  in SMD. (Default: None) Must be given as a string of seven comma
  separated values in the following order: “dielectric, refractive
  index, acidity, basicity, surface tension, aromaticity,
  electronegative halogenicity” Refer to the QChem manual for further
  details.

- **max_scf_cycles** (*int*) – Maximum number of SCF iterations.
  (Default: 100)

- **geom_opt_max_cycles** (*int*) – Maximum number of geometry
  optimization iterations. (Default: 200)

- **geom_opt** (*dict*) – A dict containing parameters for the
  \$geom_opt section of the Q-Chem input file, which control the new
  geometry optimizer available starting in version 5.4.2. The new
  optimizer remains under development but was officially released and
  became the default optimizer in Q-Chem version 6.0.0. Note that for
  version 5.4.2, the new optimizer must be explicitly requested by
  passing in a dictionary (empty or otherwise) for this input parameter.
  (Default: False)

- **plot_cubes** (*bool*) – Whether to write CUBE files of the electron
  density. (Default: False)

- **output_wavefunction** (*bool*) – Whether to write a wavefunction
  ([<span id="id14" class="problematic">\*</span>](#id13).wfn) file of
  the electron density (Default: False)

- **overwrite_inputs** (*dict*) –

  Dictionary of QChem input sections to add or overwrite variables. The
  currently available sections (keys) are rem, pcm, solvent, smx, opt,
  scan, van_der_waals, and plots. The value of each key is a dictionary
  of key value pairs relevant to that section. For example, to add a new
  variable to the rem section that sets symmetry to false, use

  overwrite_inputs = {“rem”: {“symmetry”: “false”}}

  **Note that if something like basis is added to the rem dict it will
  overwrite the default basis.**

  **Note that supplying a van_der_waals section here will automatically
  modify the PCM “radii” setting to “read”.**

  **Note that all keys must be given as strings, even when they are
  numbers!**

- **vdw_mode** (*'atomic'* *\|* *'sequential'*) – Method of specifying
  custom van der Waals radii. Applies only if you are using
  overwrite_inputs to add a \$van_der_waals section to the input. In
  ‘atomic’ mode (default), dict keys represent the atomic number
  associated with each radius (e.g., ‘12’ = carbon). In ‘sequential’
  mode, dict keys represent the sequential position of a single specific
  atom in the input structure.

</div>

<div id="module-pymatgen.io.qchem.utils" class="section">

<span id="pymatgen-io-qchem-utils-module"></span>

## pymatgen.io.qchem.utils module<a href="#module-pymatgen.io.qchem.utils" class="headerlink"
title="Link to this heading"></a>

Utilities for Qchem io.

<span class="sig-name descname"><span class="pre">lower_and_check_unique</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dict_to_check</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/utils.py#L124-L162"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.utils.lower_and_check_unique"
class="headerlink" title="Link to this definition"></a>  
Takes a dictionary and makes all the keys lower case. Also converts all
numeric values (floats, ints) to str and replaces “jobtype” with
“job_type” just so that key specifically can be called elsewhere without
ambiguity. Finally, ensures that multiple identical keys, that differed
only due to different capitalizations, are not present. If there are
multiple equivalent keys, an Exception is raised.

Parameters<span class="colon">:</span>  
**dict_to_check** (*dict*) – The dictionary to check and standardize

Returns<span class="colon">:</span>  
An identical dictionary but with all keys made  
lower case and no identical keys present.

Return type<span class="colon">:</span>  
dict

<!-- -->

<span class="sig-name descname"><span class="pre">process_parsed_coords</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">coords</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/utils.py#L165-L173"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.utils.process_parsed_coords"
class="headerlink" title="Link to this definition"></a>  
Takes a set of parsed coordinates, which come as an array of strings,
and returns a numpy array of floats.

<!-- -->

<span class="sig-name descname"><span class="pre">process_parsed_fock_matrix</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">fock_matrix</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/utils.py#L176-L203"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.utils.process_parsed_fock_matrix"
class="headerlink" title="Link to this definition"></a>  
The Fock matrix is parsed as a list, while it should actually be a
square matrix, this function takes the list of finds the right
dimensions in order to reshape the matrix.

<!-- -->

<span class="sig-name descname"><span class="pre">process_parsed_hess</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">hess_data</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/utils.py#L206-L229"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.utils.process_parsed_hess"
class="headerlink" title="Link to this definition"></a>  
Takes the information contained in a HESS file and converts it into the
format of the machine-readable 132.0 file which can be printed out to be
read into subsequent optimizations.

<!-- -->

<span class="sig-name descname"><span class="pre">read_matrix_pattern</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">header_pattern</span></span>*, *<span class="n"><span class="pre">footer_pattern</span></span>*, *<span class="n"><span class="pre">elements_pattern</span></span>*, *<span class="n"><span class="pre">text</span></span>*, *<span class="n"><span class="pre">postprocess=\<class</span> <span class="pre">'str'\></span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/utils.py#L43-L56"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.utils.read_matrix_pattern"
class="headerlink" title="Link to this definition"></a>  
Parse a matrix to get the quantities in a numpy array.

<!-- -->

<span class="sig-name descname"><span class="pre">read_pattern</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">text_str</span></span>*, *<span class="n"><span class="pre">patterns</span></span>*, *<span class="n"><span class="pre">terminate_on_match=False</span></span>*, *<span class="n"><span class="pre">postprocess=\<class</span> <span class="pre">'str'\></span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/utils.py#L14-L40"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.utils.read_pattern" class="headerlink"
title="Link to this definition"></a>  
General pattern reading on an input string.

Parameters<span class="colon">:</span>  
- **text_str** (*str*) – the input string to search for patterns

- **patterns** (*dict*) – A dict of patterns, e.g. {“energy”:
  r”energy\\(sigma-\>0\\)\s+=\s+(\[\d\\-.\]+)”}.

- **terminate_on_match** (*bool*) – Whether to terminate when there is
  at least one match in each key in pattern.

- **postprocess** (*callable*) – A post processing function to convert
  all matches. Defaults to str, i.e., no change.

Renders accessible:  
Any attribute in patterns. For example, {“energy”:
r”energy\\(sigma-\>0\\)\s+=\s+(\[\d\\-.\]+)”} will set the value of
matches\[“energy”\] = \[\[-1234\], \[-3453\], …\], to the results from
regex and postprocess. Note that the returned values are lists of lists,
because you can grep multiple items on one line.

<!-- -->

<span class="sig-name descname"><span class="pre">read_table_pattern</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">text_str</span></span>*, *<span class="n"><span class="pre">header_pattern</span></span>*, *<span class="n"><span class="pre">row_pattern</span></span>*, *<span class="n"><span class="pre">footer_pattern</span></span>*, *<span class="n"><span class="pre">postprocess=\<class</span> <span class="pre">'str'\></span></span>*, *<span class="n"><span class="pre">attribute_name=None</span></span>*, *<span class="n"><span class="pre">last_one_only=False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/qchem/utils.py#L59-L121"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.qchem.utils.read_table_pattern" class="headerlink"
title="Link to this definition"></a>  
Parse table-like data. A table composes of three parts: header, main
body, footer. All the data matches “row pattern” in the main body will
be returned.

Parameters<span class="colon">:</span>  
- **text_str** (*str*) – the input string to search for patterns

- **header_pattern** (*str*) – The regular expression pattern matches
  the table header. This pattern should match all the text immediately
  before the main body of the table. For multiple sections table match
  the text until the section of interest. MULTILINE and DOTALL options
  are enforced, as a result, the “.” meta-character will also match “n”
  in this section.

- **row_pattern** (*str*) – The regular expression matches a single line
  in the table. Capture interested field using regular expression
  groups.

- **footer_pattern** (*str*) – The regular expression matches the end of
  the table. E.g. a long dash line.

- **postprocess** (*callable*) – A post processing function to convert
  all matches. Defaults to str, i.e., no change.

- **attribute_name** (*str*) – Name of this table. If present the parsed
  data will be attached to “data. e.g. self.data\[“efg”\] = \[…\]

- **last_one_only** (*bool*) – All the tables will be parsed, if this
  option is set to True, only the last table will be returned. The
  enclosing list will be removed. i.e. Only a single table will be
  returned. Default to be True.

Returns<span class="colon">:</span>  
List of tables. 1) A table is a list of rows. 2) A row if either a list
of attribute values in case the capturing group is defined without name
in row_pattern, or a dict in case that named capturing groups are
defined by row_pattern.

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
