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

- <a href="#" class="reference internal">pymatgen.analysis.topological
  package</a>
  - <a href="#submodules" class="reference internal">Submodules</a>
  - <a href="#module-pymatgen.analysis.topological.spillage"
    class="reference internal">pymatgen.analysis.topological.spillage
    module</a>
    - <a href="#pymatgen.analysis.topological.spillage.SOCSpillage"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">SOCSpillage</code></span></a>
      - <a href="#pymatgen.analysis.topological.spillage.SOCSpillage.isclose"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SOCSpillage.isclose()</code></span></a>
      - <a href="#pymatgen.analysis.topological.spillage.SOCSpillage.orth"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SOCSpillage.orth()</code></span></a>
      - <a
        href="#pymatgen.analysis.topological.spillage.SOCSpillage.overlap_so_spinpol"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SOCSpillage.overlap_so_spinpol()</code></span></a>

</div>

</div>

</div>

<div class="section wy-nav-content-wrap" toggle="wy-nav-shift">

[pymatgen](index.html)

<div class="wy-nav-content">

<div class="rst-content style-external-links">

<div role="navigation" aria-label="Page navigation">

- <a href="index.html" class="icon icon-home" aria-label="Home"></a>
- pymatgen.analysis.topological package
- <a
  href="https://github.com/materialsproject/pymatgen/blob/master/docs_rst/pymatgen.analysis.topological.rst"
  class="fa fa-github">Edit on GitHub</a>

------------------------------------------------------------------------

</div>

<div class="document" role="main" itemscope="itemscope"
itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="module-pymatgen.analysis.topological" class="section">

<span id="pymatgen-analysis-topological-package"></span>

# pymatgen.analysis.topological package<a href="#module-pymatgen.analysis.topological" class="headerlink"
title="Link to this heading"></a>

Module for predicting topological properties.

<div id="submodules" class="section">

## Submodules<a href="#submodules" class="headerlink"
title="Link to this heading"></a>

</div>

<div id="module-pymatgen.analysis.topological.spillage" class="section">

<span id="pymatgen-analysis-topological-spillage-module"></span>

## pymatgen.analysis.topological.spillage module<a href="#module-pymatgen.analysis.topological.spillage"
class="headerlink" title="Link to this heading"></a>

Code to calculate spin-orbit spillage. Modified from JARVIS-Tools
<a href="https://www.nature.com/articles/s41598-019-45028-y"
class="reference external">https://www.nature.com/articles/s41598-019-45028-y</a>
<a href="https://www.nature.com/articles/s41524-020-0319-4"
class="reference external">https://www.nature.com/articles/s41524-020-0319-4</a>.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">SOCSpillage</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">wf_noso</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">''</span></span>*, *<span class="n"><span class="pre">wf_so</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">''</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/topological/spillage.py#L19-L229"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.topological.spillage.SOCSpillage"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Spin-orbit spillage criteria to predict whether a material is
topologically non-trivial. The spillage criteria physically signifies
number of band-inverted electrons. A non-zero, high value (generally
\>0.5) suggests non-trivial behavior.

Requires path to WAVECAR files with and without LSORBIT = .TRUE.

Parameters<span class="colon">:</span>  
- **wf_noso** – WAVECAR without spin-orbit coupling

- **wf_so** – WAVECAR with spin-orbit coupling

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">isclose</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">n1</span></span>*, *<span class="n"><span class="pre">n2</span></span>*, *<span class="n"><span class="pre">rel_tol</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1e-07</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/topological/spillage.py#L37-L40"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.topological.spillage.SOCSpillage.isclose"
class="headerlink" title="Link to this definition"></a>  
Checking if the numbers are close enough.

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">orth</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">A</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/topological/spillage.py#L42-L51"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.topological.spillage.SOCSpillage.orth"
class="headerlink" title="Link to this definition"></a>  
Helper function to create orthonormal basis.

<span class="sig-name descname"><span class="pre">overlap_so_spinpol</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/topological/spillage.py#L53-L229"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.topological.spillage.SOCSpillage.overlap_so_spinpol"
class="headerlink" title="Link to this definition"></a>  
Main function to calculate SOC spillage.

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
