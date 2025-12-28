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

- <a href="#" class="reference internal">pymatgen.analysis.solar
  package</a>
  - <a href="#submodules" class="reference internal">Submodules</a>
  - <a href="#module-pymatgen.analysis.solar.slme"
    class="reference internal">pymatgen.analysis.solar.slme module</a>
    - <a href="#pymatgen.analysis.solar.slme.absorption_coefficient"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">absorption_coefficient()</code></span></a>
    - <a href="#pymatgen.analysis.solar.slme.get_dir_indir_gap"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">get_dir_indir_gap()</code></span></a>
    - <a href="#pymatgen.analysis.solar.slme.optics"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">optics()</code></span></a>
    - <a href="#pymatgen.analysis.solar.slme.parse_dielectric_data"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">parse_dielectric_data()</code></span></a>
    - <a href="#pymatgen.analysis.solar.slme.slme"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">slme()</code></span></a>
    - <a href="#pymatgen.analysis.solar.slme.to_matrix"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">to_matrix()</code></span></a>

</div>

</div>

</div>

<div class="section wy-nav-content-wrap" toggle="wy-nav-shift">

[pymatgen](index.html)

<div class="wy-nav-content">

<div class="rst-content style-external-links">

<div role="navigation" aria-label="Page navigation">

- <a href="index.html" class="icon icon-home" aria-label="Home"></a>
- pymatgen.analysis.solar package
- <a
  href="https://github.com/materialsproject/pymatgen/blob/master/docs_rst/pymatgen.analysis.solar.rst"
  class="fa fa-github">Edit on GitHub</a>

------------------------------------------------------------------------

</div>

<div class="document" role="main" itemscope="itemscope"
itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="module-pymatgen.analysis.solar" class="section">

<span id="pymatgen-analysis-solar-package"></span>

# pymatgen.analysis.solar package<a href="#module-pymatgen.analysis.solar" class="headerlink"
title="Link to this heading"></a>

Module for predicting theoretical solar-cell efficiency.

<div id="submodules" class="section">

## Submodules<a href="#submodules" class="headerlink"
title="Link to this heading"></a>

</div>

<div id="module-pymatgen.analysis.solar.slme" class="section">

<span id="pymatgen-analysis-solar-slme-module"></span>

## pymatgen.analysis.solar.slme module<a href="#module-pymatgen.analysis.solar.slme" class="headerlink"
title="Link to this heading"></a>

Calculate spectroscopy limited maximum efficiency (SLME) given
dielectric function data.

Forked and adjusted from : <a href="https://github.com/usnistgov/jarvis"
class="reference external">https://github.com/usnistgov/jarvis</a>

References: 1) <a href="https://doi.org/10.1021/acs.chemmater.9b02166"
class="reference external">https://doi.org/10.1021/acs.chemmater.9b02166</a> &  
2.  <a href="https://doi.org/10.1103/PhysRevLett.108.068701"
    class="reference external">https://doi.org/10.1103/PhysRevLett.108.068701</a>

<!-- -->

<span class="sig-name descname"><span class="pre">absorption_coefficient</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dielectric</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/solar/slme.py#L87-L117"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.solar.slme.absorption_coefficient"
class="headerlink" title="Link to this definition"></a>  
Calculate the optical absorption coefficient from an input set of
pymatgen vasprun dielectric constant data.

Parameters<span class="colon">:</span>  
**dielectric** (*list*) – A list containing the dielectric response
function in the pymatgen vasprun format. - element 0: list of energies -
element 1: real dielectric tensors, in <span
class="pre">`[xx,`</span>` `<span class="pre">`yy,`</span>` `<span
class="pre">`zz,`</span>` `<span class="pre">`xy,`</span>` `<span
class="pre">`xz,`</span>` `<span class="pre">`yz]`</span> format. -
element 2: imaginary dielectric tensors, in <span
class="pre">`[xx,`</span>` `<span class="pre">`yy,`</span>` `<span
class="pre">`zz,`</span>` `<span class="pre">`xy,`</span>` `<span
class="pre">`xz,`</span>` `<span class="pre">`yz]`</span> format.

Returns<span class="colon">:</span>  
absorption coefficient using eV as frequency units (cm^-1).

Return type<span class="colon">:</span>  
np.ndarray

<!-- -->

<span class="sig-name descname"><span class="pre">get_dir_indir_gap</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">run</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">''</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/solar/slme.py#L43-L49"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.solar.slme.get_dir_indir_gap"
class="headerlink" title="Link to this definition"></a>  
Get direct and indirect bandgaps for a vasprun.xml.

<!-- -->

<span class="sig-name descname"><span class="pre">optics</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">path</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">''</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/solar/slme.py#L120-L131"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.solar.slme.optics" class="headerlink"
title="Link to this definition"></a>  
Helper function to calculate optical absorption coefficient.

<!-- -->

<span class="sig-name descname"><span class="pre">parse_dielectric_data</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">data</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/solar/slme.py#L71-L84"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.solar.slme.parse_dielectric_data"
class="headerlink" title="Link to this definition"></a>  
Convert a set of 2D vasprun formatted dielectric data to the eigenvalues
of each corresponding 3x3 symmetric numpy matrices.

Parameters<span class="colon">:</span>  
**data** (*list*) – length N list of dielectric data. Each entry should
be a list of <span class="pre">`[xx,`</span>` `<span
class="pre">`yy,`</span>` `<span class="pre">`zz,`</span>` `<span
class="pre">`xy`</span>` `<span class="pre">`,`</span>` `<span
class="pre">`xz,`</span>` `<span class="pre">`yz`</span>` `<span
class="pre">`]`</span> dielectric tensor elements.

Returns<span class="colon">:</span>  
a Nx3 numpy array. Each row contains the eigenvalues  
for the corresponding row in data.

Return type<span class="colon">:</span>  
np.ndarray

<!-- -->

<span class="sig-name descname"><span class="pre">slme</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">material_energy_for_absorbance_data</span></span>*, *<span class="n"><span class="pre">material_absorbance_data</span></span>*, *<span class="n"><span class="pre">material_direct_allowed_gap</span></span>*, *<span class="n"><span class="pre">material_indirect_gap</span></span>*, *<span class="n"><span class="pre">thickness</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">5e-05</span></span>*, *<span class="n"><span class="pre">temperature</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">293.15</span></span>*, *<span class="n"><span class="pre">absorbance_in_inverse_centimeters</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">cut_off_absorbance_below_direct_allowed_gap</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">plot_current_voltage</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/solar/slme.py#L134-L275"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.solar.slme.slme" class="headerlink"
title="Link to this definition"></a>  
Calculate the SLME.

Parameters<span class="colon">:</span>  
- **material_energy_for_absorbance_data** – energy grid for absorbance
  data

- **material_absorbance_data** – absorption coefficient in m^-1

- **material_direct_allowed_gap** – direct bandgap in eV

- **material_indirect_gap** – indirect bandgap in eV

- **thickness** – thickness of the material in m

- **temperature** – working temperature in K

- **absorbance_in_inverse_centimeters** – whether the absorbance data is
  in the unit of cm^-1

- **cut_off_absorbance_below_direct_allowed_gap** – whether to discard
  all absorption below bandgap

- **plot_current_voltage** – whether to plot the current-voltage curve

Returns<span class="colon">:</span>  
The calculated maximum efficiency.

<!-- -->

<span class="sig-name descname"><span class="pre">to_matrix</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">xx</span></span>*, *<span class="n"><span class="pre">yy</span></span>*, *<span class="n"><span class="pre">zz</span></span>*, *<span class="n"><span class="pre">xy</span></span>*, *<span class="n"><span class="pre">yz</span></span>*, *<span class="n"><span class="pre">xz</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/solar/slme.py#L52-L68"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.solar.slme.to_matrix" class="headerlink"
title="Link to this definition"></a>  
Convert a list of matrix components to a symmetric 3x3 matrix. Inputs
should be in the order xx, yy, zz, xy, yz, xz.

Parameters<span class="colon">:</span>  
- **xx** (*float*) – xx component of the matrix.

- **yy** (*float*) – yy component of the matrix.

- **zz** (*float*) – zz component of the matrix.

- **xy** (*float*) – xy component of the matrix.

- **yz** (*float*) – yz component of the matrix.

- **xz** (*float*) – xz component of the matrix.

Returns<span class="colon">:</span>  
The matrix, as a 3x3 numpy array.

Return type<span class="colon">:</span>  
np.ndarray

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
