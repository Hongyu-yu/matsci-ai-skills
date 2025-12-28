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

- <a href="#"
  class="reference internal">pymatgen.analysis.ferroelectricity
  package</a>
  - <a href="#submodules" class="reference internal">Submodules</a>
  - <a href="#module-pymatgen.analysis.ferroelectricity.polarization"
    class="reference internal">pymatgen.analysis.ferroelectricity.polarization
    module</a>
    - <a href="#pymatgen.analysis.ferroelectricity.polarization.EnergyTrend"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">EnergyTrend</code></span></a>
      - <a
        href="#pymatgen.analysis.ferroelectricity.polarization.EnergyTrend.endpoints_minima"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">EnergyTrend.endpoints_minima()</code></span></a>
      - <a
        href="#pymatgen.analysis.ferroelectricity.polarization.EnergyTrend.max_spline_jump"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">EnergyTrend.max_spline_jump()</code></span></a>
      - <a
        href="#pymatgen.analysis.ferroelectricity.polarization.EnergyTrend.smoothness"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">EnergyTrend.smoothness()</code></span></a>
      - <a
        href="#pymatgen.analysis.ferroelectricity.polarization.EnergyTrend.spline"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">EnergyTrend.spline()</code></span></a>
    - <a href="#pymatgen.analysis.ferroelectricity.polarization.Polarization"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Polarization</code></span></a>
      - <a
        href="#pymatgen.analysis.ferroelectricity.polarization.Polarization.from_outcars_and_structures"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Polarization.from_outcars_and_structures()</code></span></a>
      - <a
        href="#pymatgen.analysis.ferroelectricity.polarization.Polarization.get_lattice_quanta"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Polarization.get_lattice_quanta()</code></span></a>
      - <a
        href="#pymatgen.analysis.ferroelectricity.polarization.Polarization.get_pelecs_and_pions"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Polarization.get_pelecs_and_pions()</code></span></a>
      - <a
        href="#pymatgen.analysis.ferroelectricity.polarization.Polarization.get_polarization_change"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Polarization.get_polarization_change()</code></span></a>
      - <a
        href="#pymatgen.analysis.ferroelectricity.polarization.Polarization.get_polarization_change_norm"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Polarization.get_polarization_change_norm()</code></span></a>
      - <a
        href="#pymatgen.analysis.ferroelectricity.polarization.Polarization.get_same_branch_polarization_data"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Polarization.get_same_branch_polarization_data()</code></span></a>
      - <a
        href="#pymatgen.analysis.ferroelectricity.polarization.Polarization.max_spline_jumps"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Polarization.max_spline_jumps()</code></span></a>
      - <a
        href="#pymatgen.analysis.ferroelectricity.polarization.Polarization.same_branch_splines"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Polarization.same_branch_splines()</code></span></a>
      - <a
        href="#pymatgen.analysis.ferroelectricity.polarization.Polarization.smoothness"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Polarization.smoothness()</code></span></a>
    - <a href="#pymatgen.analysis.ferroelectricity.polarization.calc_ionic"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">calc_ionic()</code></span></a>
    - <a
      href="#pymatgen.analysis.ferroelectricity.polarization.get_nearest_site"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">get_nearest_site()</code></span></a>
    - <a
      href="#pymatgen.analysis.ferroelectricity.polarization.get_total_ionic_dipole"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">get_total_ionic_dipole()</code></span></a>
    - <a
      href="#pymatgen.analysis.ferroelectricity.polarization.zval_dict_from_potcar"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">zval_dict_from_potcar()</code></span></a>

</div>

</div>

</div>

<div class="section wy-nav-content-wrap" toggle="wy-nav-shift">

[pymatgen](index.html)

<div class="wy-nav-content">

<div class="rst-content style-external-links">

<div role="navigation" aria-label="Page navigation">

- <a href="index.html" class="icon icon-home" aria-label="Home"></a>
- pymatgen.analysis.ferroelectricity package
- <a
  href="https://github.com/materialsproject/pymatgen/blob/master/docs_rst/pymatgen.analysis.ferroelectricity.rst"
  class="fa fa-github">Edit on GitHub</a>

------------------------------------------------------------------------

</div>

<div class="document" role="main" itemscope="itemscope"
itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="module-pymatgen.analysis.ferroelectricity" class="section">

<span id="pymatgen-analysis-ferroelectricity-package"></span>

# pymatgen.analysis.ferroelectricity package<a href="#module-pymatgen.analysis.ferroelectricity" class="headerlink"
title="Link to this heading"></a>

Package for analyzing ferroelectricity.

<div id="submodules" class="section">

## Submodules<a href="#submodules" class="headerlink"
title="Link to this heading"></a>

</div>

<div id="module-pymatgen.analysis.ferroelectricity.polarization"
class="section">

<span
id="pymatgen-analysis-ferroelectricity-polarization-module"></span>

## pymatgen.analysis.ferroelectricity.polarization module<a href="#module-pymatgen.analysis.ferroelectricity.polarization"
class="headerlink" title="Link to this heading"></a>

This module contains classes useful for analyzing ferroelectric
candidates. The Polarization class can recover the spontaneous
polarization using multiple calculations along a nonpolar to polar
ferroelectric distortion. The EnergyTrend class is useful for assessing
the trend in energy across the distortion.

See Nicola Spaldin’s “A beginner’s guide to the modern theory of
polarization” (<a href="https://arxiv.org/abs/1202.1831"
class="reference external">https://arxiv.org/abs/1202.1831</a>) for an
introduction to crystal polarization.

VASP reports dipole moment values (used to derive polarization) along
Cartesian directions (see pead.F around line 970 in the VASP source to
confirm this). However, it is most convenient to perform the adjustments
necessary to recover a same branch polarization by expressing the
polarization along lattice directions. For this reason, calc_ionic
calculates ionic contributions to the polarization along lattice
directions. We provide the means to convert Cartesian direction
polarizations to lattice direction polarizations in the Polarization
class.

We recommend using our calc_ionic function for calculating the ionic
polarization rather than the values from OUTCAR. We find that the ionic
dipole moment reported in OUTCAR differ from the naive calculation of
\sum_i Z_i r_i where i is the index of the atom, Z_i is the ZVAL from
the pseudopotential file, and r is the distance in Angstroms along the
lattice vectors. Note, this difference is not simply due to VASP using
Cartesian directions and calc_ionic using lattice direction but rather
how the ionic polarization is computed. Compare calc_ionic to VASP
SUBROUTINE POINT_CHARGE_DIPOL in dipol.F in the VASP source to see the
differences. We are able to recover a smooth same branch polarization
more frequently using the naive calculation in calc_ionic than using the
ionic dipole moment reported in the OUTCAR.

Some definitions of terms used in the comments below:

A polar structure belongs to a polar space group. A polar space group
has a one of the 10 polar point group:

> <div>
>
> (1, 2, m, mm2, 4, 4mm, 3, 3m, 6, 6m)
>
> </div>

Being nonpolar is not equivalent to being centrosymmetric (having
inversion symmetry). For example, any space group with point group 222
is nonpolar but not centrosymmetric.

By symmetry the polarization of a nonpolar material modulo the quantum
of polarization can only be zero or 1/2. We use a nonpolar structure to
help determine the spontaneous polarization because it serves as a
reference point.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">EnergyTrend</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">energies</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/ferroelectricity/polarization.py#L430-L474"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.ferroelectricity.polarization.EnergyTrend"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Analyze the trend in energy across a distortion path.

Parameters<span class="colon">:</span>  
**energies** – Energies.

<span class="sig-name descname"><span class="pre">endpoints_minima</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">slope_cutoff</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.005</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/ferroelectricity/polarization.py#L461-L474"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.ferroelectricity.polarization.EnergyTrend.endpoints_minima"
class="headerlink" title="Link to this definition"></a>  
Test if spline endpoints are at minima for a given slope cutoff.

<span class="sig-name descname"><span class="pre">max_spline_jump</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/ferroelectricity/polarization.py#L456-L459"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.ferroelectricity.polarization.EnergyTrend.max_spline_jump"
class="headerlink" title="Link to this definition"></a>  
Get maximum difference between spline and energy trend.

<span class="sig-name descname"><span class="pre">smoothness</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/ferroelectricity/polarization.py#L444-L454"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.ferroelectricity.polarization.EnergyTrend.smoothness"
class="headerlink" title="Link to this definition"></a>  
Get rms average difference between spline and energy trend.

<span class="sig-name descname"><span class="pre">spline</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/ferroelectricity/polarization.py#L440-L442"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.ferroelectricity.polarization.EnergyTrend.spline"
class="headerlink" title="Link to this definition"></a>  
Fit spline to energy trend data.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Polarization</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">p_elecs</span></span>*, *<span class="n"><span class="pre">p_ions</span></span>*, *<span class="n"><span class="pre">structures</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">p_elecs_in_cartesian</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">p_ions_in_cartesian</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/ferroelectricity/polarization.py#L141-L427"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.ferroelectricity.polarization.Polarization"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Recover the same branch polarization for a set of polarization
calculations along the nonpolar - polar distortion path of a
ferroelectric.

p_elecs, p_ions, and structures lists should be given in order of
nonpolar to polar! For example, the structures returned from:

> <div>
>
> nonpolar.interpolate(polar,interpolate_lattices=True)
>
> </div>

if nonpolar is the nonpolar Structure and polar is the polar structure.

It is assumed that the electronic and ionic dipole moment values are
given in electron Angstroms along the three lattice directions (a,b,c).

p_elecs (np.ndarray): electronic contribution to the polarization with
shape \[N, 3\] p_ions (np.ndarray): ionic contribution to the
polarization with shape \[N, 3\] p_elecs_in_cartesian: whether p_elecs
is along Cartesian directions (rather than lattice directions).

> <div>
>
> Default is True because that is the convention for VASP.
>
> </div>

p_ions_in_cartesian: whether p_ions is along Cartesian directions (rather than lattice directions).  
Default is False because calc_ionic (which we recommend using for
calculating the ionic contribution to the polarization) uses lattice
directions.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_outcars_and_structures</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">outcars</span></span>*, *<span class="n"><span class="pre">structures</span></span>*, *<span class="n"><span class="pre">calc_ionic_from_zval</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/ferroelectricity/polarization.py#L186-L205"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.ferroelectricity.polarization.Polarization.from_outcars_and_structures"
class="headerlink" title="Link to this definition"></a>  
Create Polarization object from list of Outcars and Structures in order
of nonpolar to polar.

Note, we recommend calculating the ionic dipole moment using calc_ionic
than using the values in Outcar (see module comments). To do this set
calc_ionic_from_zval = True

<span class="sig-name descname"><span class="pre">get_lattice_quanta</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">convert_to_muC_per_cm2</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">all_in_polar</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/ferroelectricity/polarization.py#L328-L357"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.ferroelectricity.polarization.Polarization.get_lattice_quanta"
class="headerlink" title="Link to this definition"></a>  
Get the dipole / polarization quanta along a, b, and c for all
structures.

<span class="sig-name descname"><span class="pre">get_pelecs_and_pions</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">convert_to_muC_per_cm2</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/ferroelectricity/polarization.py#L207-L233"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.ferroelectricity.polarization.Polarization.get_pelecs_and_pions"
class="headerlink" title="Link to this definition"></a>  
Get the electronic and ionic dipole moments / polarizations.

convert_to_muC_per_cm2: Convert from electron \* Angstroms to microCoulomb  
per centimeter\*\*2

<span class="sig-name descname"><span class="pre">get_polarization_change</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">convert_to_muC_per_cm2</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">all_in_polar</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/ferroelectricity/polarization.py#L359-L366"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.ferroelectricity.polarization.Polarization.get_polarization_change"
class="headerlink" title="Link to this definition"></a>  
Get difference between nonpolar and polar same branch polarization.

<span class="sig-name descname"><span class="pre">get_polarization_change_norm</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">convert_to_muC_per_cm2</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">all_in_polar</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/ferroelectricity/polarization.py#L368-L378"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.ferroelectricity.polarization.Polarization.get_polarization_change_norm"
class="headerlink" title="Link to this definition"></a>  
Get magnitude of difference between nonpolar and polar same branch
polarization.

<span class="sig-name descname"><span class="pre">get_same_branch_polarization_data</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">convert_to_muC_per_cm2</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">all_in_polar</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/ferroelectricity/polarization.py#L235-L326"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.ferroelectricity.polarization.Polarization.get_same_branch_polarization_data"
class="headerlink" title="Link to this definition"></a>  
Get same branch dipole moment (convert_to_muC_per_cm2=False) or
polarization for given polarization data (convert_to_muC_per_cm2=True).

Polarization is a lattice vector, meaning it is only defined modulo the
quantum of polarization:

> <div>
>
> P = P_0 + \sum_i \frac{n_i e R_i}{\Omega}
>
> </div>

where n_i is an integer, e is the charge of the electron in
microCoulombs, R_i is a lattice vector, and \Omega is the unit cell
volume in cm\*\*3 (giving polarization units of microCoulomb per
centimeter\*\*2).

The quantum of the dipole moment in electron Angstroms (as given by
VASP) is:

> <div>
>
> \sum_i n_i e R_i
>
> </div>

where e, the electron charge, is 1 and R_i is a lattice vector, and n_i
is an integer.

Given N polarization calculations in order from nonpolar to polar, this
algorithm minimizes the distance between adjacent polarization images.
To do this, it constructs a polarization lattice for each polarization
calculation using the pymatgen.core.structure class and calls the
get_nearest_site method to find the image of a given polarization
lattice vector that is closest to the previous polarization lattice
vector image.

Note, using convert_to_muC_per_cm2=True and all_in_polar=True calculates
the “proper polarization” (meaning the change in polarization does not
depend on the choice of polarization branch) while
convert_to_muC_per_cm2=True and all_in_polar=False calculates the
“improper polarization” (meaning the change in polarization does depend
on the choice of branch). As one might guess from the names. We
recommend calculating the “proper polarization”.

convert_to_muC_per_cm2: convert polarization from electron \* Angstroms to  
microCoulomb per centimeter\*\*2

all_in_polar: convert polarization to be in polar (final structure)
polarization lattice

<span class="sig-name descname"><span class="pre">max_spline_jumps</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">convert_to_muC_per_cm2</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">all_in_polar</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/ferroelectricity/polarization.py#L402-L412"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.ferroelectricity.polarization.Polarization.max_spline_jumps"
class="headerlink" title="Link to this definition"></a>  
Get maximum difference between spline and same branch polarization data.

<span class="sig-name descname"><span class="pre">same_branch_splines</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">convert_to_muC_per_cm2</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">all_in_polar</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/ferroelectricity/polarization.py#L380-L400"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.ferroelectricity.polarization.Polarization.same_branch_splines"
class="headerlink" title="Link to this definition"></a>  
Fit splines to same branch polarization. This is used to assess any
jumps in the same branch polarization.

<span class="sig-name descname"><span class="pre">smoothness</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">convert_to_muC_per_cm2</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">all_in_polar</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/ferroelectricity/polarization.py#L414-L427"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.ferroelectricity.polarization.Polarization.smoothness"
class="headerlink" title="Link to this definition"></a>  
Get rms average difference between spline and same branch polarization
data.

<!-- -->

<span class="sig-name descname"><span class="pre">calc_ionic</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">site</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
class="reference internal"
title="pymatgen.core.sites.PeriodicSite"><span
class="pre">PeriodicSite</span></a></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">zval</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">np.ndarray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/ferroelectricity/polarization.py#L84-L95"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.ferroelectricity.polarization.calc_ionic"
class="headerlink" title="Link to this definition"></a>  
Calculate the ionic dipole moment using ZVAL from pseudopotential.

site: PeriodicSite structure: Structure zval: Charge value for ion (ZVAL
for VASP pseudopotential)

Returns polarization in electron Angstroms.

<!-- -->

<span class="sig-name descname"><span class="pre">get_nearest_site</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">struct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">coords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">site</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
class="reference internal"
title="pymatgen.core.sites.PeriodicSite"><span
class="pre">PeriodicSite</span></a></span>*, *<span class="n"><span class="pre">r</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/ferroelectricity/polarization.py#L113-L138"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.ferroelectricity.polarization.get_nearest_site"
class="headerlink" title="Link to this definition"></a>  
Given coords and a site, find closet site to coords.

Parameters<span class="colon">:</span>  
- **coords** (*3x1 array*) – Cartesian coords of center of sphere

- **site** – site to find closest to coords

- **r** (*float*) – radius of sphere. Defaults to diagonal of unit cell

Returns<span class="colon">:</span>  
Closest site and distance.

<!-- -->

<span class="sig-name descname"><span class="pre">get_total_ionic_dipole</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span>*, *<span class="n"><span class="pre">zval_dict</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/ferroelectricity/polarization.py#L98-L110"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.ferroelectricity.polarization.get_total_ionic_dipole"
class="headerlink" title="Link to this definition"></a>  
Get the total ionic dipole moment for a structure.

structure: pymatgen Structure zval_dict: specie, zval dictionary pairs
center (np.array with shape \[3,1\]) : dipole center used by VASP tiny
(float) : tolerance for determining boundary of calculation.

<!-- -->

<span class="sig-name descname"><span class="pre">zval_dict_from_potcar</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">potcar</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/ferroelectricity/polarization.py#L75-L81"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.ferroelectricity.polarization.zval_dict_from_potcar"
class="headerlink" title="Link to this definition"></a>  
Create zval_dictionary for calculating the ionic polarization from
Potcar object.

potcar: Potcar object

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
