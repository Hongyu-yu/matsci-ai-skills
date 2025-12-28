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

- <a href="#" class="reference internal">pymatgen.io.xtb package</a>
  - <a href="#submodules" class="reference internal">Submodules</a>
  - <a href="#module-pymatgen.io.xtb.inputs"
    class="reference internal">pymatgen.io.xtb.inputs module</a>
    - <a href="#pymatgen.io.xtb.inputs.CRESTInput"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">CRESTInput</code></span></a>
      - <a href="#pymatgen.io.xtb.inputs.CRESTInput.constrains_template"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CRESTInput.constrains_template()</code></span></a>
      - <a href="#pymatgen.io.xtb.inputs.CRESTInput.write_input_files"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CRESTInput.write_input_files()</code></span></a>
  - <a href="#module-pymatgen.io.xtb.outputs"
    class="reference internal">pymatgen.io.xtb.outputs module</a>
    - <a href="#pymatgen.io.xtb.outputs.CRESTOutput"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">CRESTOutput</code></span></a>

</div>

</div>

</div>

<div class="section wy-nav-content-wrap" toggle="wy-nav-shift">

[pymatgen](index.html)

<div class="wy-nav-content">

<div class="rst-content style-external-links">

<div role="navigation" aria-label="Page navigation">

- <a href="index.html" class="icon icon-home" aria-label="Home"></a>
- pymatgen.io.xtb package
- <a
  href="https://github.com/materialsproject/pymatgen/blob/master/docs_rst/pymatgen.io.xtb.rst"
  class="fa fa-github">Edit on GitHub</a>

------------------------------------------------------------------------

</div>

<div class="document" role="main" itemscope="itemscope"
itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="module-pymatgen.io.xtb" class="section">

<span id="pymatgen-io-xtb-package"></span>

# pymatgen.io.xtb package<a href="#module-pymatgen.io.xtb" class="headerlink"
title="Link to this heading"></a>

This package implements modules for input and output to and from CREST.

<div id="submodules" class="section">

## Submodules<a href="#submodules" class="headerlink"
title="Link to this heading"></a>

</div>

<div id="module-pymatgen.io.xtb.inputs" class="section">

<span id="pymatgen-io-xtb-inputs-module"></span>

## pymatgen.io.xtb.inputs module<a href="#module-pymatgen.io.xtb.inputs" class="headerlink"
title="Link to this heading"></a>

Classes for writing XTB input files.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">CRESTInput</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">molecule</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">working_dir</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'.'</span></span>*, *<span class="n"><span class="pre">coords_filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'crest_in.xyz'</span></span>*, *<span class="n"><span class="pre">constraints</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/xtb/inputs.py#L21-L94"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.xtb.inputs.CRESTInput" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

An object representing CREST input files. Because CREST is controlled
through command line flags and external files, the CRESTInput class
mainly consists of methods for containing and writing external files.

Parameters<span class="colon">:</span>  
- **molecule**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
  class="reference internal"
  title="pymatgen.core.structure.Molecule"><em>Molecule</em></a>) –
  Molecule object

- **working_dir** (*str*) – Directory to write input files to

- **coords_filename** (*str*) – Name of input coordinates file

- **constraints** (*dict*) – Dictionary of common editable parameters
  for .constrains file. {“atoms”: \[List of 1-indexed atoms to fix\],
  “force_constant”: float\].

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">constrains_template</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">molecule</span></span>*, *<span class="n"><span class="pre">reference_fnm</span></span>*, *<span class="n"><span class="pre">constraints</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/xtb/inputs.py#L62-L94"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.xtb.inputs.CRESTInput.constrains_template"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
- **molecule**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
  class="reference internal"
  title="pymatgen.core.structure.Molecule"><em>Molecule</em></a>) –
  Molecule the constraints will be performed on

- **reference_fnm** (*str*) – Name of file containing reference
  structure in same directory

- **constraints** (*dict*) – Dictionary of common editable parameters
  for .constrains file. {“atoms”: \[List of 1-indexed atoms to fix\],
  “force_constant”: float\].

Returns<span class="colon">:</span>  
for .constrains file

Return type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">write_input_files</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/xtb/inputs.py#L50-L60"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.xtb.inputs.CRESTInput.write_input_files"
class="headerlink" title="Link to this definition"></a>  
Write input files to working directory.

</div>

<div id="module-pymatgen.io.xtb.outputs" class="section">

<span id="pymatgen-io-xtb-outputs-module"></span>

## pymatgen.io.xtb.outputs module<a href="#module-pymatgen.io.xtb.outputs" class="headerlink"
title="Link to this heading"></a>

Parsers for XTB output files and directories.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">CRESTOutput</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">output_filename</span></span>*, *<span class="n"><span class="pre">path</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'.'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/xtb/outputs.py#L25-L167"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.xtb.outputs.CRESTOutput" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Parse CREST output files.

Assumes runtype is iMTD-GC \[default\].

Parameters<span class="colon">:</span>  
- **output_filename** (*str*) – Filename to parse

- **path** (*str*) – Path to directory including output_filename and all
  other xtb output files (crest_best.xyz, etc.)

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
