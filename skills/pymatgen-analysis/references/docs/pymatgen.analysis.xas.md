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

- <a href="#" class="reference internal">pymatgen.analysis.xas package</a>
  - <a href="#submodules" class="reference internal">Submodules</a>
  - <a href="#module-pymatgen.analysis.xas.spectrum"
    class="reference internal">pymatgen.analysis.xas.spectrum module</a>
    - <a href="#pymatgen.analysis.xas.spectrum.XAS"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">XAS</code></span></a>
      - <a href="#pymatgen.analysis.xas.spectrum.XAS.x"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">XAS.x</code></span></a>
      - <a href="#pymatgen.analysis.xas.spectrum.XAS.y"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">XAS.y</code></span></a>
      - <a href="#pymatgen.analysis.xas.spectrum.XAS.absorbing_element"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">XAS.absorbing_element</code></span></a>
      - <a href="#pymatgen.analysis.xas.spectrum.XAS.edge"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">XAS.edge</code></span></a>
      - <a href="#pymatgen.analysis.xas.spectrum.XAS.spectrum_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">XAS.spectrum_type</code></span></a>
      - <a href="#pymatgen.analysis.xas.spectrum.XAS.absorbing_index"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">XAS.absorbing_index</code></span></a>
      - <a href="#pymatgen.analysis.xas.spectrum.XAS.zero_negative_intensity"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">XAS.zero_negative_intensity</code></span></a>
      - <a href="#pymatgen.analysis.xas.spectrum.XAS.XLABEL"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">XAS.XLABEL</code></span></a>
      - <a href="#pymatgen.analysis.xas.spectrum.XAS.YLABEL"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">XAS.YLABEL</code></span></a>
      - <a href="#pymatgen.analysis.xas.spectrum.XAS.stitch"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">XAS.stitch()</code></span></a>
    - <a href="#pymatgen.analysis.xas.spectrum.site_weighted_spectrum"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">site_weighted_spectrum()</code></span></a>

</div>

</div>

</div>

<div class="section wy-nav-content-wrap" toggle="wy-nav-shift">

[pymatgen](index.html)

<div class="wy-nav-content">

<div class="rst-content style-external-links">

<div role="navigation" aria-label="Page navigation">

- <a href="index.html" class="icon icon-home" aria-label="Home"></a>
- pymatgen.analysis.xas package
- <a
  href="https://github.com/materialsproject/pymatgen/blob/master/docs_rst/pymatgen.analysis.xas.rst"
  class="fa fa-github">Edit on GitHub</a>

------------------------------------------------------------------------

</div>

<div class="document" role="main" itemscope="itemscope"
itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="module-pymatgen.analysis.xas" class="section">

<span id="pymatgen-analysis-xas-package"></span>

# pymatgen.analysis.xas package<a href="#module-pymatgen.analysis.xas" class="headerlink"
title="Link to this heading"></a>

Package for analysis of X-ray Absorption Spectroscopy.

<div id="submodules" class="section">

## Submodules<a href="#submodules" class="headerlink"
title="Link to this heading"></a>

</div>

<div id="module-pymatgen.analysis.xas.spectrum" class="section">

<span id="pymatgen-analysis-xas-spectrum-module"></span>

## pymatgen.analysis.xas.spectrum module<a href="#module-pymatgen.analysis.xas.spectrum" class="headerlink"
title="Link to this heading"></a>

This module defines classes to represent all xas and stitching methods.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">XAS</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">x</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span></span>*, *<span class="n"><span class="pre">y</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">absorbing_element</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.periodic_table.Element"
class="reference internal"
title="pymatgen.core.periodic_table.Element"><span
class="pre">Element</span></a></span>*, *<span class="n"><span class="pre">edge</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'K'</span></span>*, *<span class="n"><span class="pre">spectrum_type</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'XANES'</span></span>*, *<span class="n"><span class="pre">absorbing_index</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">zero_negative_intensity</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/xas/spectrum.py#L31-L223"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.xas.spectrum.XAS" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="pymatgen.core.html#pymatgen.core.spectrum.Spectrum"
class="reference internal" title="pymatgen.core.spectrum.Spectrum"><span
class="pre"><code class="sourceCode python">Spectrum</code></span></a>

Basic XAS object.

Parameters<span class="colon">:</span>  
- **x** – A sequence of x-ray energies in eV

- **y** – A sequence of mu(E)

- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  Structure associated with the spectrum

- **absorbing_element**
  (<a href="pymatgen.core.html#pymatgen.core.periodic_table.Element"
  class="reference internal"
  title="pymatgen.core.periodic_table.Element"><em>Element</em></a>) –
  Element associated with the spectrum

- **edge** (*str*) – Absorption edge associated with the spectrum

- **spectrum_type** (*str*) – ‘XANES’ or ‘EXAFS’

- **absorbing_index** (*None* *or* *int*) – If None, the spectrum is
  assumed to be a site-weighted spectrum, which is comparable to
  experimental one. Otherwise, it indicates that the absorbing_index for
  a site-wise spectrum.

<span class="sig-name descname"><span class="pre">x</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/xas/spectrum.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.xas.spectrum.XAS.x" class="headerlink"
title="Link to this definition"></a>  
The sequence of energies.

Type<span class="colon">:</span>  
Sequence\[float\]

<span class="sig-name descname"><span class="pre">y</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/xas/spectrum.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.xas.spectrum.XAS.y" class="headerlink"
title="Link to this definition"></a>  
The sequence of mu(E).

Type<span class="colon">:</span>  
Sequence\[float\]

<span class="sig-name descname"><span class="pre">absorbing_element</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/xas/spectrum.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.xas.spectrum.XAS.absorbing_element"
class="headerlink" title="Link to this definition"></a>  
The absorbing element of the spectrum.

Type<span class="colon">:</span>  
str or .Element

<span class="sig-name descname"><span class="pre">edge</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/xas/spectrum.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.xas.spectrum.XAS.edge" class="headerlink"
title="Link to this definition"></a>  
The edge of the spectrum.

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">spectrum_type</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/xas/spectrum.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.xas.spectrum.XAS.spectrum_type"
class="headerlink" title="Link to this definition"></a>  
The type of the spectrum (XANES or EXAFS).

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">absorbing_index</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/xas/spectrum.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.xas.spectrum.XAS.absorbing_index"
class="headerlink" title="Link to this definition"></a>  
The absorbing index of the spectrum.

Type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">zero_negative_intensity</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/xas/spectrum.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.xas.spectrum.XAS.zero_negative_intensity"
class="headerlink" title="Link to this definition"></a>  
Whether to set unphysical negative intensities to zero

Type<span class="colon">:</span>  
bool

Initialize a spectrum object.

<span class="sig-name descname"><span class="pre">XLABEL</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'Energy'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/xas/spectrum.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.xas.spectrum.XAS.XLABEL" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">YLABEL</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'Intensity'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/xas/spectrum.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.xas.spectrum.XAS.YLABEL" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">stitch</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.analysis.xas.spectrum.XAS" class="reference internal"
title="pymatgen.analysis.xas.spectrum.XAS"><span
class="pre">XAS</span></a></span>*, *<span class="n"><span class="pre">num_samples</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">500</span></span>*, *<span class="n"><span class="pre">mode</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'XAFS'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'L23'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'XAFS'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.analysis.xas.spectrum.XAS" class="reference internal"
title="pymatgen.analysis.xas.spectrum.XAS"><span
class="pre">XAS</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/xas/spectrum.py#L100-L223"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.xas.spectrum.XAS.stitch" class="headerlink"
title="Link to this definition"></a>  
Stitch XAS objects to get the full XAFS spectrum or L23 edge XANES
spectrum depending on the mode.

1.  Use XAFS mode for stitching XANES and EXAFS with same absorption edge.  
    The stitching will be performed based on wavenumber, k. for k \<= 3,
    XAS(k) = XAS\[XANES(k)\] for 3 \< k \< max(xanes_k), will
    interpolate according to

    > <div>
    >
    > XAS(k)=f(k)\*mu\[XANES(k)\]+(1-f(k))\*mu\[EXAFS(k)\] where
    > f(k)=cos^2((pi/2) (k-3)/(max(xanes_k)-3)
    >
    > </div>

    for k \> max(xanes_k), XAS(k) = XAS\[EXAFS(k)\]

2.  Use L23 mode for stitching L2 and L3 edge XANES for elements with  
    atomic number \<=30.

Parameters<span class="colon">:</span>  
- **other** – Another XAS object.

- **num_samples** (*int*) – Number of samples for interpolation.

- **mode** (*"XAFS"* *\|* *"L23"*) – Either XAFS mode for stitching
  XANES and EXAFS or L23 mode for stitching L2 and L3.

Returns<span class="colon">:</span>  
The stitched spectrum.

Return type<span class="colon">:</span>  
XAS object

<!-- -->

<span class="sig-name descname"><span class="pre">site_weighted_spectrum</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">xas_list</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.analysis.xas.spectrum.XAS" class="reference internal"
title="pymatgen.analysis.xas.spectrum.XAS"><span
class="pre">XAS</span></a><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">num_samples</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">500</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.analysis.xas.spectrum.XAS" class="reference internal"
title="pymatgen.analysis.xas.spectrum.XAS"><span
class="pre">XAS</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/xas/spectrum.py#L226-L285"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.xas.spectrum.site_weighted_spectrum"
class="headerlink" title="Link to this definition"></a>  
Obtain site-weighted XAS object based on site multiplicity for each
absorbing index and its corresponding site-wise spectrum.

Parameters<span class="colon">:</span>  
- **xas_list**
  (*\[*<a href="#pymatgen.analysis.xas.spectrum.XAS" class="reference internal"
  title="pymatgen.analysis.xas.spectrum.XAS"><em>XAS</em></a>*\]*) –
  List of XAS object to be weighted

- **num_samples** (*int*) – Number of samples for interpolation

Returns<span class="colon">:</span>  
The site-weighted spectrum

Return type<span class="colon">:</span>  
XAS object

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
