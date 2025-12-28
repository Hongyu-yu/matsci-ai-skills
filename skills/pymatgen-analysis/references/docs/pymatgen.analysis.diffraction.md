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

- <a href="#" class="reference internal">pymatgen.analysis.diffraction
  package</a>
  - <a href="#submodules" class="reference internal">Submodules</a>
  - <a href="#module-pymatgen.analysis.diffraction.core"
    class="reference internal">pymatgen.analysis.diffraction.core module</a>
    - <a
      href="#pymatgen.analysis.diffraction.core.AbstractDiffractionPatternCalculator"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">AbstractDiffractionPatternCalculator</code></span></a>
      - <a
        href="#pymatgen.analysis.diffraction.core.AbstractDiffractionPatternCalculator.SCALED_INTENSITY_TOL"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractDiffractionPatternCalculator.SCALED_INTENSITY_TOL</code></span></a>
      - <a
        href="#pymatgen.analysis.diffraction.core.AbstractDiffractionPatternCalculator.TWO_THETA_TOL"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractDiffractionPatternCalculator.TWO_THETA_TOL</code></span></a>
      - <a
        href="#pymatgen.analysis.diffraction.core.AbstractDiffractionPatternCalculator.get_pattern"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractDiffractionPatternCalculator.get_pattern()</code></span></a>
      - <a
        href="#pymatgen.analysis.diffraction.core.AbstractDiffractionPatternCalculator.get_plot"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractDiffractionPatternCalculator.get_plot()</code></span></a>
      - <a
        href="#pymatgen.analysis.diffraction.core.AbstractDiffractionPatternCalculator.plot_structures"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractDiffractionPatternCalculator.plot_structures()</code></span></a>
      - <a
        href="#pymatgen.analysis.diffraction.core.AbstractDiffractionPatternCalculator.show_plot"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractDiffractionPatternCalculator.show_plot()</code></span></a>
    - <a href="#pymatgen.analysis.diffraction.core.DiffractionPattern"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">DiffractionPattern</code></span></a>
      - <a href="#pymatgen.analysis.diffraction.core.DiffractionPattern.XLABEL"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DiffractionPattern.XLABEL</code></span></a>
      - <a href="#pymatgen.analysis.diffraction.core.DiffractionPattern.YLABEL"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DiffractionPattern.YLABEL</code></span></a>
    - <a href="#pymatgen.analysis.diffraction.core.get_unique_families"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">get_unique_families()</code></span></a>
  - <a href="#module-pymatgen.analysis.diffraction.neutron"
    class="reference internal">pymatgen.analysis.diffraction.neutron
    module</a>
    - <a href="#pymatgen.analysis.diffraction.neutron.NDCalculator"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">NDCalculator</code></span></a>
      - <a
        href="#pymatgen.analysis.diffraction.neutron.NDCalculator.get_pattern"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NDCalculator.get_pattern()</code></span></a>
  - <a href="#module-pymatgen.analysis.diffraction.tem"
    class="reference internal">pymatgen.analysis.diffraction.tem module</a>
    - <a href="#pymatgen.analysis.diffraction.tem.TEMCalculator"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">TEMCalculator</code></span></a>
      - <a href="#pymatgen.analysis.diffraction.tem.TEMCalculator.bragg_angles"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TEMCalculator.bragg_angles()</code></span></a>
      - <a
        href="#pymatgen.analysis.diffraction.tem.TEMCalculator.cell_intensity"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TEMCalculator.cell_intensity()</code></span></a>
      - <a
        href="#pymatgen.analysis.diffraction.tem.TEMCalculator.cell_scattering_factors"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TEMCalculator.cell_scattering_factors()</code></span></a>
      - <a
        href="#pymatgen.analysis.diffraction.tem.TEMCalculator.electron_scattering_factors"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TEMCalculator.electron_scattering_factors()</code></span></a>
      - <a
        href="#pymatgen.analysis.diffraction.tem.TEMCalculator.generate_points"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TEMCalculator.generate_points()</code></span></a>
      - <a
        href="#pymatgen.analysis.diffraction.tem.TEMCalculator.get_first_point"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TEMCalculator.get_first_point()</code></span></a>
      - <a
        href="#pymatgen.analysis.diffraction.tem.TEMCalculator.get_interplanar_angle"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TEMCalculator.get_interplanar_angle()</code></span></a>
      - <a
        href="#pymatgen.analysis.diffraction.tem.TEMCalculator.get_interplanar_spacings"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TEMCalculator.get_interplanar_spacings()</code></span></a>
      - <a href="#pymatgen.analysis.diffraction.tem.TEMCalculator.get_pattern"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TEMCalculator.get_pattern()</code></span></a>
      - <a href="#pymatgen.analysis.diffraction.tem.TEMCalculator.get_plot_2d"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TEMCalculator.get_plot_2d()</code></span></a>
      - <a
        href="#pymatgen.analysis.diffraction.tem.TEMCalculator.get_plot_2d_concise"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TEMCalculator.get_plot_2d_concise()</code></span></a>
      - <a
        href="#pymatgen.analysis.diffraction.tem.TEMCalculator.get_plot_coeffs"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TEMCalculator.get_plot_coeffs()</code></span></a>
      - <a href="#pymatgen.analysis.diffraction.tem.TEMCalculator.get_positions"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TEMCalculator.get_positions()</code></span></a>
      - <a href="#pymatgen.analysis.diffraction.tem.TEMCalculator.get_s2"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TEMCalculator.get_s2()</code></span></a>
      - <a href="#pymatgen.analysis.diffraction.tem.TEMCalculator.is_parallel"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TEMCalculator.is_parallel()</code></span></a>
      - <a
        href="#pymatgen.analysis.diffraction.tem.TEMCalculator.normalized_cell_intensity"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TEMCalculator.normalized_cell_intensity()</code></span></a>
      - <a href="#pymatgen.analysis.diffraction.tem.TEMCalculator.tem_dots"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TEMCalculator.tem_dots()</code></span></a>
      - <a
        href="#pymatgen.analysis.diffraction.tem.TEMCalculator.wavelength_rel"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TEMCalculator.wavelength_rel()</code></span></a>
      - <a href="#pymatgen.analysis.diffraction.tem.TEMCalculator.x_ray_factors"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TEMCalculator.x_ray_factors()</code></span></a>
      - <a
        href="#pymatgen.analysis.diffraction.tem.TEMCalculator.zone_axis_filter"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TEMCalculator.zone_axis_filter()</code></span></a>
  - <a href="#module-pymatgen.analysis.diffraction.xrd"
    class="reference internal">pymatgen.analysis.diffraction.xrd module</a>
    - <a href="#pymatgen.analysis.diffraction.xrd.XRDCalculator"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">XRDCalculator</code></span></a>
      - <a
        href="#pymatgen.analysis.diffraction.xrd.XRDCalculator.AVAILABLE_RADIATION"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">XRDCalculator.AVAILABLE_RADIATION</code></span></a>
      - <a href="#pymatgen.analysis.diffraction.xrd.XRDCalculator.get_pattern"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">XRDCalculator.get_pattern()</code></span></a>

</div>

</div>

</div>

<div class="section wy-nav-content-wrap" toggle="wy-nav-shift">

[pymatgen](index.html)

<div class="wy-nav-content">

<div class="rst-content style-external-links">

<div role="navigation" aria-label="Page navigation">

- <a href="index.html" class="icon icon-home" aria-label="Home"></a>
- pymatgen.analysis.diffraction package
- <a
  href="https://github.com/materialsproject/pymatgen/blob/master/docs_rst/pymatgen.analysis.diffraction.rst"
  class="fa fa-github">Edit on GitHub</a>

------------------------------------------------------------------------

</div>

<div class="document" role="main" itemscope="itemscope"
itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="module-pymatgen.analysis.diffraction" class="section">

<span id="pymatgen-analysis-diffraction-package"></span>

# pymatgen.analysis.diffraction package<a href="#module-pymatgen.analysis.diffraction" class="headerlink"
title="Link to this heading"></a>

This package implements various diffraction analyses.

<div id="submodules" class="section">

## Submodules<a href="#submodules" class="headerlink"
title="Link to this heading"></a>

</div>

<div id="module-pymatgen.analysis.diffraction.core" class="section">

<span id="pymatgen-analysis-diffraction-core-module"></span>

## pymatgen.analysis.diffraction.core module<a href="#module-pymatgen.analysis.diffraction.core" class="headerlink"
title="Link to this heading"></a>

This module implements core classes for calculation of diffraction
patterns.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">AbstractDiffractionPatternCalculator</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/core.py#L42-L202"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.diffraction.core.AbstractDiffractionPatternCalculator"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`ABC`</span>

Abstract base class for computing the diffraction pattern of a crystal.

<span class="sig-name descname"><span class="pre">SCALED_INTENSITY_TOL</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">0.001</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/diffraction/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.diffraction.core.AbstractDiffractionPatternCalculator.SCALED_INTENSITY_TOL"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">TWO_THETA_TOL</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">1e-05</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/diffraction/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.diffraction.core.AbstractDiffractionPatternCalculator.TWO_THETA_TOL"
class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">abstractmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">get_pattern</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">scaled</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">two_theta_range</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">90)</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/core.py#L55-L73"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.diffraction.core.AbstractDiffractionPatternCalculator.get_pattern"
class="headerlink" title="Link to this definition"></a>  
Calculates the diffraction pattern for a structure.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  Input structure

- **scaled** (*bool*) – Whether to return scaled intensities. The
  maximum peak is set to a value of 100. Defaults to True. Use False if
  you need the absolute values to combine XRD plots.

- **two_theta_range** (*\[float* *of* *length 2\]*) – Tuple for range of
  two_thetas to calculate in degrees. Defaults to (0, 90). Set to None
  if you want all diffracted beams within the limiting sphere of radius
  2 / wavelength.

Returns<span class="colon">:</span>  
DiffractionPattern

<span class="sig-name descname"><span class="pre">get_plot</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">two_theta_range</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">(0,</span> <span class="pre">90)</span></span>*, *<span class="n"><span class="pre">annotate_peaks</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'compact'</span></span>*, *<span class="n"><span class="pre">ax</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">plt.Axes</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">with_labels</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">fontsize</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">16</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">plt.Axes</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/core.py#L75-L153"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.diffraction.core.AbstractDiffractionPatternCalculator.get_plot"
class="headerlink" title="Link to this definition"></a>  
Get the diffraction plot as a matplotlib Axes.

Parameters<span class="colon">:</span>  
- **structure** – Input structure

- **two_theta_range** (*tuple\[float,* *float\]*) – Range of two_thetas
  to calculate in degrees. Defaults to (0, 90). Set to None if you want
  all diffracted beams within the limiting sphere of radius 2 /
  wavelength.

- **annotate_peaks** (*str* *\|* *None*) – Whether and how to annotate
  the peaks with hkl indices. Default is ‘compact’, i.e. show short
  version (oriented vertically), e.g. 100. If ‘full’, show long version,
  e.g. (1, 0, 0). If None, do not show anything.

- **ax** – matplotlib Axes or None if a new figure should be created.

- **with_labels** – True to add xlabels and ylabels to the plot.

- **fontsize** – (int) fontsize for peak labels.

Returns<span class="colon">:</span>  
matplotlib Axes object

Return type<span class="colon">:</span>  
plt.Axes

<span class="sig-name descname"><span class="pre">plot_structures</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structures</span></span>*, *<span class="n"><span class="pre">fontsize</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">6</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../util/plotting.py#L171-L202"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.diffraction.core.AbstractDiffractionPatternCalculator.plot_structures"
class="headerlink" title="Link to this definition"></a>  
Plot diffraction patterns for multiple structures on the same figure.

Parameters<span class="colon">:</span>  
- **structures**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  List of structures

- **two_theta_range** (*\[float* *of* *length 2\]*) – Tuple for range of
  two_thetas to calculate in degrees. Defaults to (0, 90). Set to None
  if you want all diffracted beams within the limiting sphere of radius
  2 / wavelength.

- **annotate_peaks** (*str* *\|* *None*) – Whether and how to annotate
  the peaks with hkl indices. Default is ‘compact’, i.e. show short
  version (oriented vertically), e.g. 100. If ‘full’, show long version,
  e.g. (1, 0, 0). If None, do not show anything.

- **fontsize** – (int) fontsize for peak labels.

Keyword arguments controlling the display of the figure:

| kwargs       | Meaning                                                                                           |
|--------------|---------------------------------------------------------------------------------------------------|
| title        | Title of the plot (Default: None).                                                                |
| show         | True to show the figure (default: True).                                                          |
| savefig      | “abc.png” or “abc.eps” to save the figure to a file.                                              |
| size_kwargs  | Dictionary with options passed to fig.set_size_inches e.g. size_kwargs=dict(w=3, h=4)             |
| tight_layout | True to call fig.tight_layout (default: False)                                                    |
| ax_grid      | True (False) to add (remove) grid from all axes in fig. Default: None i.e. fig is left unchanged. |
| ax_annotate  | Add labels to subplots e.g. (a), (b). Default: False                                              |
| fig_close    | Close figure. Default: False.                                                                     |

<span class="sig-name descname"><span class="pre">show_plot</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/core.py#L155-L169"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.diffraction.core.AbstractDiffractionPatternCalculator.show_plot"
class="headerlink" title="Link to this definition"></a>  
Show the diffraction plot.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  Input structure

- **two_theta_range** (*\[float* *of* *length 2\]*) – Tuple for range of
  two_thetas to calculate in degrees. Defaults to (0, 90). Set to None
  if you want all diffracted beams within the limiting sphere of radius
  2 / wavelength.

- **annotate_peaks** (*str* *\|* *None*) – Whether and how to annotate
  the peaks with hkl indices. Default is ‘compact’, i.e. show short
  version (oriented vertically), e.g. 100. If ‘full’, show long version,
  e.g. (1, 0, 0). If None, do not show anything.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">DiffractionPattern</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">x</span></span>*, *<span class="n"><span class="pre">y</span></span>*, *<span class="n"><span class="pre">hkls</span></span>*, *<span class="n"><span class="pre">d_hkls</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/core.py#L19-L39"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.diffraction.core.DiffractionPattern"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="pymatgen.core.html#pymatgen.core.spectrum.Spectrum"
class="reference internal" title="pymatgen.core.spectrum.Spectrum"><span
class="pre"><code class="sourceCode python">Spectrum</code></span></a>

A representation of a diffraction pattern.

Parameters<span class="colon">:</span>  
- **x** – Two theta angles.

- **y** – Intensities

- **hkls** – \[{“hkl”: (h, k, l), “multiplicity”: mult}\], where {“hkl”:
  (h, k, l), “multiplicity”: mult} is a dict of Miller indices for all
  diffracted lattice facets contributing to each intensity.

- **d_hkls** – List of interplanar spacings.

<span class="sig-name descname"><span class="pre">XLABEL</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'\$2\\\Theta\$'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/diffraction/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.diffraction.core.DiffractionPattern.XLABEL"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">YLABEL</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'Intensity'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/diffraction/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.diffraction.core.DiffractionPattern.YLABEL"
class="headerlink" title="Link to this definition"></a>  

<!-- -->

<span class="sig-name descname"><span class="pre">get_unique_families</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">hkls</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/core.py#L205-L237"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.diffraction.core.get_unique_families"
class="headerlink" title="Link to this definition"></a>  
Get unique families of Miller indices. Families must be permutations of
each other.

Parameters<span class="colon">:</span>  
**hkls** (*\[h,* *k,* *l\]*) – List of Miller indices.

Returns<span class="colon">:</span>  
multiplicity}: A dict with unique hkl and multiplicity.

Return type<span class="colon">:</span>  
{hkl

</div>

<div id="module-pymatgen.analysis.diffraction.neutron" class="section">

<span id="pymatgen-analysis-diffraction-neutron-module"></span>

## pymatgen.analysis.diffraction.neutron module<a href="#module-pymatgen.analysis.diffraction.neutron"
class="headerlink" title="Link to this heading"></a>

This module implements a neutron diffraction (ND) pattern calculator.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">NDCalculator</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">wavelength</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1.54184</span></span>*, *<span class="n"><span class="pre">symprec</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">debye_waller_factors</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/neutron.py#L37-L200"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.diffraction.neutron.NDCalculator"
class="headerlink" title="Link to this definition"></a>  
Bases: <a
href="#pymatgen.analysis.diffraction.core.AbstractDiffractionPatternCalculator"
class="reference internal"
title="pymatgen.analysis.diffraction.core.AbstractDiffractionPatternCalculator"><span
class="pre"><code
class="sourceCode python">AbstractDiffractionPatternCalculator</code></span></a>

Computes the powder neutron diffraction pattern of a crystal structure.
This code is a slight modification of XRDCalculator in
pymatgen.analysis.diffraction.xrd. See it for details of the algorithm.
Main changes by using neutron instead of X-ray are as follows:

1.  Atomic scattering length is a constant.

2.  Polarization correction term of Lorentz factor is unnecessary.

Reference: Marc De Graef and Michael E. McHenry, Structure of Materials
2nd ed, Chapter13, Cambridge University Press 2003.

Initialize the ND calculator with a given radiation.

Parameters<span class="colon">:</span>  
- **wavelength** (*float*) – The wavelength of neutron in angstroms.
  Defaults to 1.54, corresponds to Cu K_alpha x-ray radiation.

- **symprec** (*float*) – Symmetry precision for structure refinement.
  If set to 0, no refinement is done. Otherwise, refinement is performed
  using spglib with provided precision.

- **symbol** (*debye_waller_factors* *({element*) – float}): Allows the
  specification of Debye-Waller factors. Note that these factors are
  temperature dependent.

<span class="sig-name descname"><span class="pre">get_pattern</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">scaled</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">two_theta_range</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">90)</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/neutron.py#L69-L200"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.diffraction.neutron.NDCalculator.get_pattern"
class="headerlink" title="Link to this definition"></a>  
Calculates the powder neutron diffraction pattern for a structure.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  Input structure

- **scaled** (*bool*) – Whether to return scaled intensities. The
  maximum peak is set to a value of 100. Defaults to True. Use False if
  you need the absolute values to combine ND plots.

- **two_theta_range** (*\[float* *of* *length 2\]*) – Tuple for range of
  two_thetas to calculate in degrees. Defaults to (0, 90). Set to None
  if you want all diffracted beams within the limiting sphere of radius
  2 / wavelength.

Returns<span class="colon">:</span>  
ND pattern

Return type<span class="colon">:</span>  
<a href="#pymatgen.analysis.diffraction.core.DiffractionPattern"
class="reference internal"
title="pymatgen.analysis.diffraction.core.DiffractionPattern">DiffractionPattern</a>

</div>

<div id="module-pymatgen.analysis.diffraction.tem" class="section">

<span id="pymatgen-analysis-diffraction-tem-module"></span>

## pymatgen.analysis.diffraction.tem module<a href="#module-pymatgen.analysis.diffraction.tem" class="headerlink"
title="Link to this heading"></a>

TEM pattern calculator.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">TEMCalculator</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">symprec</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">voltage</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">200</span></span>*, *<span class="n"><span class="pre">beam_direction</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">(0,</span> <span class="pre">0,</span> <span class="pre">1)</span></span>*, *<span class="n"><span class="pre">camera_length</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">160</span></span>*, *<span class="n"><span class="pre">debye_waller_factors</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">cs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/tem.py#L37-L687"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.diffraction.tem.TEMCalculator"
class="headerlink" title="Link to this definition"></a>  
Bases: <a
href="#pymatgen.analysis.diffraction.core.AbstractDiffractionPatternCalculator"
class="reference internal"
title="pymatgen.analysis.diffraction.core.AbstractDiffractionPatternCalculator"><span
class="pre"><code
class="sourceCode python">AbstractDiffractionPatternCalculator</code></span></a>

Compute the TEM pattern of a crystal structure for multiple Laue zones.
Code partially inspired from XRD calculation implementation. X-ray
factor to electron factor

> <div>
>
> conversion based on the International Table of Crystallography.
>
> </div>

\#TODO: Could add “number of iterations”, “magnification”, “critical value of beam”,  
“twin direction” for certain materials, “sample thickness”, and
“excitation error s”.

Parameters<span class="colon">:</span>  
- **symprec** (*float*) – Symmetry precision for structure refinement.
  If set to 0, no refinement is done. Otherwise, refinement is performed
  using spglib with provided precision.

- **voltage** (*float*) – The wavelength is a function of the TEM
  microscope’s voltage (in kV). Defaults to 200.

- **beam_direction** (*tuple*) – The direction of the electron beam
  fired onto the sample. By default, set to \[0,0,1\], which corresponds
  to the normal direction of the sample plane.

- **camera_length** (*int*) – The distance from the sample to the
  projected diffraction pattern. By default, set to 160 cm. Units in cm.

- **symbol** (*debye_waller_factors* *({element*) – float}): Allows the
  specification of Debye-Waller factors. Note that these factors are
  temperature dependent.

- **cs** (*float*) – The chromatic aberration coefficient (in mm).
  Defaults to 1.

<span class="sig-name descname"><span class="pre">bragg_angles</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">interplanar_spacings</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/tem.py#L145-L159"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.diffraction.tem.TEMCalculator.bragg_angles"
class="headerlink" title="Link to this definition"></a>  
Get the Bragg angles for every hkl point passed in (where n = 1).

Parameters<span class="colon">:</span>  
**interplanar_spacings** (*dict*) – dictionary of hkl to interplanar
spacing

Returns<span class="colon">:</span>  
hkl planes mapped to Bragg angles \[radians\]

Return type<span class="colon">:</span>  
dict\[tuple\[int, int, int\], float\]

<span class="sig-name descname"><span class="pre">cell_intensity</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">bragg_angles</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/tem.py#L261-L277"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.diffraction.tem.TEMCalculator.cell_intensity"
class="headerlink" title="Link to this definition"></a>  
Calculates cell intensity for each hkl plane. For simplicity’s sake,
take I = [<span id="id2" class="problematic">\|</span>](#id1)F\|\*\*2.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  The input structure.

- **bragg_angles** (*dict* *of* *3-tuple to float*) – The Bragg angles
  for each hkl plane.

Returns<span class="colon">:</span>  
dict of hkl plane to cell intensity

<span class="sig-name descname"><span class="pre">cell_scattering_factors</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">bragg_angles</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/tem.py#L234-L259"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.diffraction.tem.TEMCalculator.cell_scattering_factors"
class="headerlink" title="Link to this definition"></a>  
Calculates the scattering factor for the whole cell.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  The input structure.

- **bragg_angles** (*dict* *of* *3-tuple to float*) – The Bragg angles
  for each hkl plane.

Returns<span class="colon">:</span>  
dict of hkl plane (3-tuple) to scattering factor (in angstroms).

<span class="sig-name descname"><span class="pre">electron_scattering_factors</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">bragg_angles</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/tem.py#L207-L232"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.diffraction.tem.TEMCalculator.electron_scattering_factors"
class="headerlink" title="Link to this definition"></a>  
Calculates atomic scattering factors for electrons using the Mott-Bethe
formula (1st order Born approximation).

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  The input structure.

- **bragg_angles** (*dict* *of* *3-tuple to float*) – The Bragg angles
  for each hkl plane.

Returns<span class="colon">:</span>  
dict from atomic symbol to another dict of hkl plane to factor (in
angstroms)

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">generate_points</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">coord_left</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">-10</span></span>*, *<span class="n"><span class="pre">coord_right</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">10</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">ndarray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/tem.py#L90-L105"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.diffraction.tem.TEMCalculator.generate_points"
class="headerlink" title="Link to this definition"></a>  
Generate a bunch of 3D points that span a cube.

Parameters<span class="colon">:</span>  
- **coord_left** (*int*) – The minimum coordinate value.

- **coord_right** (*int*) – The maximum coordinate value.

Returns<span class="colon">:</span>  
2d array

Return type<span class="colon">:</span>  
np.array

<span class="sig-name descname"><span class="pre">get_first_point</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">points</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/tem.py#L359-L377"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.diffraction.tem.TEMCalculator.get_first_point"
class="headerlink" title="Link to this definition"></a>  
Get the first point to be plotted in the 2D DP, corresponding to maximum
d/minimum R.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  The input structure.

- **points** (*list*) – All points to be checked.

Returns<span class="colon">:</span>  
dict of a hkl plane to max interplanar distance.

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">get_interplanar_angle</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">p1</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">p2</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/tem.py#L379-L430"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.diffraction.tem.TEMCalculator.get_interplanar_angle"
class="headerlink" title="Link to this definition"></a>  
Get the interplanar angle (in degrees) between the normal of two crystal
planes. Formulas from International Tables for Crystallography Volume C
pp. 2-9.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  The input structure.

- **p1** (*3-tuple*) – plane 1

- **p2** (*3-tuple*) – plane 2

Returns<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">get_interplanar_spacings</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">points</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.ndarray</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/tem.py#L127-L143"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.diffraction.tem.TEMCalculator.get_interplanar_spacings"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  the input structure.

- **points** (*tuple*) – the desired hkl indices.

Returns<span class="colon">:</span>  
hkl planes mapped to  
interplanar spacings, in angstroms (float).

Return type<span class="colon">:</span>  
dict\[tuple\[int, int, int\], float\]

<span class="sig-name descname"><span class="pre">get_pattern</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">scaled</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">two_theta_range</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">pd.DataFrame</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/tem.py#L279-L317"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.diffraction.tem.TEMCalculator.get_pattern"
class="headerlink" title="Link to this definition"></a>  
Get all relevant TEM DP info in a pandas dataframe.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  The input structure.

- **scaled** (*bool*) – Required value for inheritance, does nothing in
  TEM pattern

- **two_theta_range** (*tuple\[float,* *float\]*) – Required value for
  inheritance, does nothing in TEM pattern

Returns<span class="colon">:</span>  
pd.DataFrame

<span class="sig-name descname"><span class="pre">get_plot_2d</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">go.Figure</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/tem.py#L544-L619"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.diffraction.tem.TEMCalculator.get_plot_2d"
class="headerlink" title="Link to this definition"></a>  
Generate the 2D diffraction pattern of the input structure.

Parameters<span class="colon">:</span>  
**structure**
(<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><em>Structure</em></a>) – The
input structure.

Returns<span class="colon">:</span>  
Figure

<span class="sig-name descname"><span class="pre">get_plot_2d_concise</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">go.Figure</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/tem.py#L621-L687"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.diffraction.tem.TEMCalculator.get_plot_2d_concise"
class="headerlink" title="Link to this definition"></a>  
Generate the concise 2D diffraction pattern of the input structure of a
smaller size and without layout. Does not display.

Parameters<span class="colon">:</span>  
**structure**
(<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><em>Structure</em></a>) – The
input structure.

Returns<span class="colon">:</span>  
Figure

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">get_plot_coeffs</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">p1</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">p2</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">p3</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">ndarray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/tem.py#L432-L454"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.diffraction.tem.TEMCalculator.get_plot_coeffs"
class="headerlink" title="Link to this definition"></a>  
Calculates coefficients of the vector addition required to generate
positions for each DP point by the Moore-Penrose inverse method.

Parameters<span class="colon">:</span>  
- **p1** (*3-tuple*) – The first point. Fixed.

- **p2** (*3-tuple*) – The second point. Fixed.

- **p3** (*3-tuple*) – The point whose coefficients are to be
  calculated.

Returns<span class="colon">:</span>  
Numpy array

<span class="sig-name descname"><span class="pre">get_positions</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">points</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">np.ndarray</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/tem.py#L456-L511"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.diffraction.tem.TEMCalculator.get_positions"
class="headerlink" title="Link to this definition"></a>  
Calculates all the positions of each hkl point in the 2D diffraction
pattern by vector addition. Distance in centimeters.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  The input structure.

- **points** (*list*) – All points to be checked.

Returns<span class="colon">:</span>  
dict of hkl plane to xy-coordinates.

<span class="sig-name descname"><span class="pre">get_s2</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">bragg_angles</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/tem.py#L161-L175"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.diffraction.tem.TEMCalculator.get_s2"
class="headerlink" title="Link to this definition"></a>  
Calculates the s squared parameter (= square of sin theta over lambda)
for each hkl plane.

Parameters<span class="colon">:</span>  
**bragg_angles** (*dict*) – The bragg angles for each hkl plane.

Returns<span class="colon">:</span>  
Dict of hkl plane to s2 parameter, calculates the s squared parameter  
(= square of sin theta over lambda).

<span class="sig-name descname"><span class="pre">is_parallel</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">plane</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">other_plane</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/tem.py#L340-L357"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.diffraction.tem.TEMCalculator.is_parallel"
class="headerlink" title="Link to this definition"></a>  
Checks if two hkl planes are parallel in reciprocal space.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  The input structure.

- **plane** (*3-tuple*) – The first plane to be compared.

- **other_plane** (*3-tuple*) – The other plane to be compared.

Returns<span class="colon">:</span>  
True if the planes are parallel, False otherwise.

Return type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">normalized_cell_intensity</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">bragg_angles</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/tem.py#L319-L338"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.diffraction.tem.TEMCalculator.normalized_cell_intensity"
class="headerlink" title="Link to this definition"></a>  
Normalizes the cell_intensity dict to 1, for use in plotting.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  The input structure.

- **bragg_angles** (*dict* *of* *3-tuple to float*) – The Bragg angles
  for each hkl plane.

Returns<span class="colon">:</span>  
dict of hkl plane to normalized cell intensity

<span class="sig-name descname"><span class="pre">tem_dots</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">points</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/tem.py#L513-L542"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.diffraction.tem.TEMCalculator.tem_dots"
class="headerlink" title="Link to this definition"></a>  
Generate all TEM_dot as named tuples that will appear on the 2D
diffraction pattern.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  The input structure.

- **points** (*list*) – All points to be checked.

Returns<span class="colon">:</span>  
list of TEM_dots

<span class="sig-name descname"><span class="pre">wavelength_rel</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/tem.py#L79-L88"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.diffraction.tem.TEMCalculator.wavelength_rel"
class="headerlink" title="Link to this definition"></a>  
Calculates the wavelength of the electron beam with relativistic kinematic effects taken  
into account.

Returns<span class="colon">:</span>  
Relativistic Wavelength (in angstroms)

Return type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">x_ray_factors</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">bragg_angles</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/tem.py#L177-L205"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.diffraction.tem.TEMCalculator.x_ray_factors"
class="headerlink" title="Link to this definition"></a>  
Calculates x-ray factors, which are required to calculate atomic
scattering factors. Method partially inspired by the equivalent process
in the xrd module.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  The input structure.

- **bragg_angles** (*dict*) – Dictionary of hkl plane to Bragg angle.

Returns<span class="colon">:</span>  
dict of atomic symbol to another dict of hkl plane to x-ray factor (in
angstroms).

<span class="sig-name descname"><span class="pre">zone_axis_filter</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">points</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">ndarray</span></span>*, *<span class="n"><span class="pre">laue_zone</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/tem.py#L107-L125"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.diffraction.tem.TEMCalculator.zone_axis_filter"
class="headerlink" title="Link to this definition"></a>  
Filter out all points that exist within the specified Laue zone
according to the zone axis rule.

Parameters<span class="colon">:</span>  
- **points** (*np.ndarray*) – The list of points to be filtered.

- **laue_zone** (*int*) – The desired Laue zone.

Returns<span class="colon">:</span>  
list of 3-tuples

</div>

<div id="module-pymatgen.analysis.diffraction.xrd" class="section">

<span id="pymatgen-analysis-diffraction-xrd-module"></span>

## pymatgen.analysis.diffraction.xrd module<a href="#module-pymatgen.analysis.diffraction.xrd" class="headerlink"
title="Link to this heading"></a>

This module implements an XRD pattern calculator.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">XRDCalculator</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">wavelength</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'CuKa'</span></span>*, *<span class="n"><span class="pre">symprec</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">debye_waller_factors</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/xrd.py#L57-L280"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.diffraction.xrd.XRDCalculator"
class="headerlink" title="Link to this definition"></a>  
Bases: <a
href="#pymatgen.analysis.diffraction.core.AbstractDiffractionPatternCalculator"
class="reference internal"
title="pymatgen.analysis.diffraction.core.AbstractDiffractionPatternCalculator"><span
class="pre"><code
class="sourceCode python">AbstractDiffractionPatternCalculator</code></span></a>

Computes the XRD pattern of a crystal structure.

This code is implemented by Shyue Ping Ong as part of UCSD’s NANO106 -
Crystallography of Materials. The formalism for this code is based on
that given in Chapters 11 and 12 of Structure of Materials by Marc De
Graef and Michael E. McHenry. This takes into account the atomic
scattering factors and the Lorentz polarization factor, but not the
Debye-Waller (temperature) factor (for which data is typically not
available). Note that the multiplicity correction is not needed since
this code simply goes through all reciprocal points within the limiting
sphere, which includes all symmetrically equivalent facets. The
algorithm is as follows

1.  Calculate reciprocal lattice of structure. Find all reciprocal
    points within the limiting sphere given by frac{2}{lambda}.

2.  For each reciprocal point mathbf{g\_{hkl}} corresponding to lattice
    plane (hkl), compute the Bragg condition sin(theta) = frac{
    lambda}{2d\_{hkl}}

3.  Compute the structure factor as the sum of the atomic scattering
    factors. The atomic scattering factors are given by

    > <div>
    >
    > f(s) = Z - 41.78214 times s^2 times sum limits\_{i=1}^n a_i
    > exp(-b_is^2)
    >
    > </div>

    where s = frac{sin(theta)}{lambda} and a_i and b_i are the fitted
    parameters for each element. The structure factor is then given by

    > <div>
    >
    > F\_{hkl} = sum limits\_{j=1}^N f_j exp(2 pi i mathbf{g\_{hkl}}
    > cdot mathbf{r})
    >
    > </div>

4.  The intensity is then given by the modulus square of the structure
    factor.

    > <div>
    >
    > I\_{hkl} = F\_{hkl}F\_{hkl}^\*
    >
    > </div>

5.  Finally, the Lorentz polarization correction factor is applied. This
    factor is given by:

    > <div>
    >
    > P(theta) = frac{1 + cos^2(2 theta)}{sin^2(theta) cos(theta)}
    >
    > </div>

Initialize the XRD calculator with a given radiation.

Parameters<span class="colon">:</span>  
- **wavelength** (*str* *\|* *float*) – The wavelength can be specified
  as either a float or a string. If it is a string, it must be one of
  the supported definitions in the AVAILABLE_RADIATION class variable,
  which provides useful commonly used wavelengths. If it is a float, it
  is interpreted as a wavelength in angstroms. Defaults to “CuKa”, i.e,
  Cu K_alpha radiation.

- **symprec** (*float*) – Symmetry precision for structure refinement.
  If set to 0, no refinement is done. Otherwise, refinement is performed
  using spglib with provided precision.

- **symbol** (*debye_waller_factors* *({element*) – float}): Allows the
  specification of Debye-Waller factors. Note that these factors are
  temperature dependent.

<span class="sig-name descname"><span class="pre">AVAILABLE_RADIATION</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">('CuKa',</span> <span class="pre">'CuKa2',</span> <span class="pre">'CuKa1',</span> <span class="pre">'CuKb1',</span> <span class="pre">'MoKa',</span> <span class="pre">'MoKa2',</span> <span class="pre">'MoKa1',</span> <span class="pre">'MoKb1',</span> <span class="pre">'CrKa',</span> <span class="pre">'CrKa2',</span> <span class="pre">'CrKa1',</span> <span class="pre">'CrKb1',</span> <span class="pre">'FeKa',</span> <span class="pre">'FeKa2',</span> <span class="pre">'FeKa1',</span> <span class="pre">'FeKb1',</span> <span class="pre">'CoKa',</span> <span class="pre">'CoKa2',</span> <span class="pre">'CoKa1',</span> <span class="pre">'CoKb1',</span> <span class="pre">'AgKa',</span> <span class="pre">'AgKa2',</span> <span class="pre">'AgKa1',</span> <span class="pre">'AgKb1')</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/diffraction/xrd.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.diffraction.xrd.XRDCalculator.AVAILABLE_RADIATION"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">get_pattern</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">scaled</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">two_theta_range</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">90)</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/diffraction/xrd.py#L131-L280"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.diffraction.xrd.XRDCalculator.get_pattern"
class="headerlink" title="Link to this definition"></a>  
Calculates the diffraction pattern for a structure.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  Input structure

- **scaled** (*bool*) – Whether to return scaled intensities. The
  maximum peak is set to a value of 100. Defaults to True. Use False if
  you need the absolute values to combine XRD plots.

- **two_theta_range** (*\[float* *of* *length 2\]*) – Tuple for range of
  two_thetas to calculate in degrees. Defaults to (0, 90). Set to None
  if you want all diffracted beams within the limiting sphere of radius
  2 / wavelength.

Returns<span class="colon">:</span>  
XRD pattern

Return type<span class="colon">:</span>  
<a href="#pymatgen.analysis.diffraction.core.DiffractionPattern"
class="reference internal"
title="pymatgen.analysis.diffraction.core.DiffractionPattern">DiffractionPattern</a>

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
