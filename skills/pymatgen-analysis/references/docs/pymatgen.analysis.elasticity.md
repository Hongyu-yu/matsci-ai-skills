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

- <a href="#" class="reference internal">pymatgen.analysis.elasticity
  package</a>
  - <a href="#submodules" class="reference internal">Submodules</a>
  - <a href="#module-pymatgen.analysis.elasticity.elastic"
    class="reference internal">pymatgen.analysis.elasticity.elastic
    module</a>
    - <a href="#pymatgen.analysis.elasticity.elastic.ComplianceTensor"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">ComplianceTensor</code></span></a>
    - <a href="#pymatgen.analysis.elasticity.elastic.ElasticTensor"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">ElasticTensor</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.agne_diffusive_thermalcond"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensor.agne_diffusive_thermalcond()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.cahill_thermalcond"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensor.cahill_thermalcond()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.clarke_thermalcond"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensor.clarke_thermalcond()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.compliance_tensor"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensor.compliance_tensor</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.debye_temperature"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensor.debye_temperature()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.directional_elastic_mod"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensor.directional_elastic_mod()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.directional_poisson_ratio"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensor.directional_poisson_ratio()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.from_independent_strains"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensor.from_independent_strains()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.from_pseudoinverse"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensor.from_pseudoinverse()</code></span></a>
      - <a href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.g_reuss"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensor.g_reuss</code></span></a>
      - <a href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.g_voigt"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensor.g_voigt</code></span></a>
      - <a href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.g_vrh"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensor.g_vrh</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.get_structure_property_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensor.get_structure_property_dict()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.green_kristoffel"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensor.green_kristoffel()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.homogeneous_poisson"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensor.homogeneous_poisson</code></span></a>
      - <a href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.k_reuss"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensor.k_reuss</code></span></a>
      - <a href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.k_voigt"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensor.k_voigt</code></span></a>
      - <a href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.k_vrh"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensor.k_vrh</code></span></a>
      - <a href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.long_v"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensor.long_v()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.property_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensor.property_dict</code></span></a>
      - <a href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.snyder_ac"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensor.snyder_ac()</code></span></a>
      - <a href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.snyder_opt"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensor.snyder_opt()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.snyder_total"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensor.snyder_total()</code></span></a>
      - <a href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.trans_v"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensor.trans_v()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.universal_anisotropy"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensor.universal_anisotropy</code></span></a>
      - <a href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.y_mod"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensor.y_mod</code></span></a>
    - <a href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">ElasticTensorExpansion</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.calculate_stress"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensorExpansion.calculate_stress()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.energy_density"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensorExpansion.energy_density()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.from_diff_fit"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensorExpansion.from_diff_fit()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.get_compliance_expansion"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensorExpansion.get_compliance_expansion()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.get_effective_ecs"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensorExpansion.get_effective_ecs()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.get_ggt"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensorExpansion.get_ggt()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.get_gruneisen_parameter"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensorExpansion.get_gruneisen_parameter()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.get_heat_capacity"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensorExpansion.get_heat_capacity()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.get_stability_criteria"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensorExpansion.get_stability_criteria()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.get_strain_from_stress"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensorExpansion.get_strain_from_stress()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.get_symmetric_wallace_tensor"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensorExpansion.get_symmetric_wallace_tensor()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.get_tgt"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensorExpansion.get_tgt()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.get_wallace_tensor"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensorExpansion.get_wallace_tensor()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.get_yield_stress"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensorExpansion.get_yield_stress()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.omega"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensorExpansion.omega()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.order"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensorExpansion.order</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.thermal_expansion_coeff"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElasticTensorExpansion.thermal_expansion_coeff()</code></span></a>
    - <a href="#pymatgen.analysis.elasticity.elastic.NthOrderElasticTensor"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">NthOrderElasticTensor</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.NthOrderElasticTensor.GPa_to_eV_A3"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NthOrderElasticTensor.GPa_to_eV_A3</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.NthOrderElasticTensor.calculate_stress"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NthOrderElasticTensor.calculate_stress()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.NthOrderElasticTensor.energy_density"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NthOrderElasticTensor.energy_density()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.NthOrderElasticTensor.from_diff_fit"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NthOrderElasticTensor.from_diff_fit()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.NthOrderElasticTensor.order"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NthOrderElasticTensor.order</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.elastic.NthOrderElasticTensor.symbol"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NthOrderElasticTensor.symbol</code></span></a>
    - <a href="#pymatgen.analysis.elasticity.elastic.diff_fit"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">diff_fit()</code></span></a>
    - <a href="#pymatgen.analysis.elasticity.elastic.find_eq_stress"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">find_eq_stress()</code></span></a>
    - <a href="#pymatgen.analysis.elasticity.elastic.generate_pseudo"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">generate_pseudo()</code></span></a>
    - <a href="#pymatgen.analysis.elasticity.elastic.get_diff_coeff"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">get_diff_coeff()</code></span></a>
    - <a href="#pymatgen.analysis.elasticity.elastic.get_strain_state_dict"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">get_strain_state_dict()</code></span></a>
    - <a href="#pymatgen.analysis.elasticity.elastic.get_symbol_list"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">get_symbol_list()</code></span></a>
    - <a href="#pymatgen.analysis.elasticity.elastic.raise_if_unphysical"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">raise_if_unphysical()</code></span></a>
    - <a href="#pymatgen.analysis.elasticity.elastic.subs"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">subs()</code></span></a>
  - <a href="#module-pymatgen.analysis.elasticity.strain"
    class="reference internal">pymatgen.analysis.elasticity.strain
    module</a>
    - <a href="#pymatgen.analysis.elasticity.strain.Deformation"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Deformation</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.strain.Deformation.apply_to_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Deformation.apply_to_structure()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.strain.Deformation.from_index_amount"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Deformation.from_index_amount()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.strain.Deformation.get_perturbed_indices"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Deformation.get_perturbed_indices()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.strain.Deformation.green_lagrange_strain"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Deformation.green_lagrange_strain</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.strain.Deformation.is_independent"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Deformation.is_independent()</code></span></a>
      - <a href="#pymatgen.analysis.elasticity.strain.Deformation.symbol"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Deformation.symbol</code></span></a>
    - <a href="#pymatgen.analysis.elasticity.strain.DeformedStructureSet"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">DeformedStructureSet</code></span></a>
    - <a href="#pymatgen.analysis.elasticity.strain.Strain"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Strain</code></span></a>
      - <a href="#pymatgen.analysis.elasticity.strain.Strain.from_deformation"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Strain.from_deformation()</code></span></a>
      - <a href="#pymatgen.analysis.elasticity.strain.Strain.from_index_amount"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Strain.from_index_amount()</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.strain.Strain.get_deformation_matrix"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Strain.get_deformation_matrix()</code></span></a>
      - <a href="#pymatgen.analysis.elasticity.strain.Strain.symbol"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Strain.symbol</code></span></a>
      - <a href="#pymatgen.analysis.elasticity.strain.Strain.von_mises_strain"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Strain.von_mises_strain</code></span></a>
    - <a
      href="#pymatgen.analysis.elasticity.strain.convert_strain_to_deformation"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">convert_strain_to_deformation()</code></span></a>
  - <a href="#module-pymatgen.analysis.elasticity.stress"
    class="reference internal">pymatgen.analysis.elasticity.stress
    module</a>
    - <a href="#pymatgen.analysis.elasticity.stress.Stress"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Stress</code></span></a>
      - <a
        href="#pymatgen.analysis.elasticity.stress.Stress.dev_principal_invariants"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Stress.dev_principal_invariants</code></span></a>
      - <a href="#pymatgen.analysis.elasticity.stress.Stress.deviator_stress"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Stress.deviator_stress</code></span></a>
      - <a href="#pymatgen.analysis.elasticity.stress.Stress.mean_stress"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Stress.mean_stress</code></span></a>
      - <a href="#pymatgen.analysis.elasticity.stress.Stress.piola_kirchoff_1"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Stress.piola_kirchoff_1()</code></span></a>
      - <a href="#pymatgen.analysis.elasticity.stress.Stress.piola_kirchoff_2"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Stress.piola_kirchoff_2()</code></span></a>
      - <a href="#pymatgen.analysis.elasticity.stress.Stress.symbol"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Stress.symbol</code></span></a>
      - <a href="#pymatgen.analysis.elasticity.stress.Stress.von_mises"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Stress.von_mises</code></span></a>

</div>

</div>

</div>

<div class="section wy-nav-content-wrap" toggle="wy-nav-shift">

[pymatgen](index.html)

<div class="wy-nav-content">

<div class="rst-content style-external-links">

<div role="navigation" aria-label="Page navigation">

- <a href="index.html" class="icon icon-home" aria-label="Home"></a>
- pymatgen.analysis.elasticity package
- <a
  href="https://github.com/materialsproject/pymatgen/blob/master/docs_rst/pymatgen.analysis.elasticity.rst"
  class="fa fa-github">Edit on GitHub</a>

------------------------------------------------------------------------

</div>

<div class="document" role="main" itemscope="itemscope"
itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="module-pymatgen.analysis.elasticity" class="section">

<span id="pymatgen-analysis-elasticity-package"></span>

# pymatgen.analysis.elasticity package<a href="#module-pymatgen.analysis.elasticity" class="headerlink"
title="Link to this heading"></a>

Package for analyzing elastic tensors and properties.

<div id="submodules" class="section">

## Submodules<a href="#submodules" class="headerlink"
title="Link to this heading"></a>

</div>

<div id="module-pymatgen.analysis.elasticity.elastic" class="section">

<span id="pymatgen-analysis-elasticity-elastic-module"></span>

## pymatgen.analysis.elasticity.elastic module<a href="#module-pymatgen.analysis.elasticity.elastic"
class="headerlink" title="Link to this heading"></a>

This module provides a class used to describe the elastic tensor,
including methods used to fit the elastic tensor from linear response
stress-strain data.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ComplianceTensor</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">s_array</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L524-L540"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.elastic.ComplianceTensor"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="pymatgen.core.html#pymatgen.core.tensors.Tensor"
class="reference internal" title="pymatgen.core.tensors.Tensor"><span
class="pre"><code class="sourceCode python">Tensor</code></span></a>

This class represents the compliance tensor, and exists primarily to
keep the voigt-conversion scheme consistent since the compliance tensor
has a unique vscale.

Parameters<span class="colon">:</span>  
**s_array** (*np.ndarray*) – input array for tensor

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ElasticTensor</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">input_array</span></span>*, *<span class="n"><span class="pre">tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.0001</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L130-L521"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.elastic.ElasticTensor"
class="headerlink" title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.analysis.elasticity.elastic.NthOrderElasticTensor"
class="reference internal"
title="pymatgen.analysis.elasticity.elastic.NthOrderElasticTensor"><span
class="pre"><code
class="sourceCode python">NthOrderElasticTensor</code></span></a>

This class extends Tensor to describe the 3x3x3x3 second-order elastic
tensor, C\_{ijkl}, with various methods for estimating other properties
derived from the second order elastic tensor (e.g. bulk modulus, shear
modulus, Young’s modulus, Poisson’s ratio) in units of eV/A^3.

Create an ElasticTensor object. The constructor throws an error if the
shape of the input_matrix argument is not 3x3x3x3, i.e. in true tensor
notation. Issues a warning if the input_matrix argument does not satisfy
standard symmetries. Note that the constructor uses \_\_new\_\_ rather
than \_\_init\_\_ according to the standard method of subclassing numpy
ndarrays.

Parameters<span class="colon">:</span>  
- **input_array** (*3x3x3x3 array-like*) – the 3x3x3x3 array-like
  representing the elastic tensor

- **tol** (*float*) – tolerance for initial symmetry test of tensor

<span class="sig-name descname"><span class="pre">agne_diffusive_thermalcond</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*</span></span><span class="n"><span class="pre">args</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L122-L125"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.agne_diffusive_thermalcond"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">cahill_thermalcond</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*</span></span><span class="n"><span class="pre">args</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L122-L125"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.cahill_thermalcond"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">clarke_thermalcond</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*</span></span><span class="n"><span class="pre">args</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L122-L125"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.clarke_thermalcond"
class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">compliance_tensor</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/elasticity/elastic.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.compliance_tensor"
class="headerlink" title="Link to this definition"></a>  
The Voigt notation compliance tensor, which is the matrix inverse of the
Voigt notation elastic tensor.

<span class="sig-name descname"><span class="pre">debye_temperature</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*</span></span><span class="n"><span class="pre">args</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L122-L125"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.debye_temperature"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">directional_elastic_mod</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">n</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L223-L226"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.directional_elastic_mod"
class="headerlink" title="Link to this definition"></a>  
Calculate directional elastic modulus for a specific vector.

<span class="sig-name descname"><span class="pre">directional_poisson_ratio</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">n</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">m</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-08</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L206-L221"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.directional_poisson_ratio"
class="headerlink" title="Link to this definition"></a>  
Calculates the poisson ratio for a specific direction relative to a
second, orthogonal direction.

Parameters<span class="colon">:</span>  
- **n** (*3-d vector*) – principal direction

- **m** (*3-d vector*) – secondary direction orthogonal to n

- **tol** (*float*) – tolerance for testing of orthogonality

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_independent_strains</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">strains</span></span>*, *<span class="n"><span class="pre">stresses</span></span>*, *<span class="n"><span class="pre">eq_stress</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">vasp</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-10</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L489-L521"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.from_independent_strains"
class="headerlink" title="Link to this definition"></a>  
Constructs the elastic tensor least-squares fit of independent strains.

Parameters<span class="colon">:</span>  
- **strains** (*list* *of* *Strains*) – list of strain objects to fit

- **stresses** (*list* *of* *Stresses*) – list of stress objects to use
  in fit corresponding to the list of strains

- **eq_stress** (<a href="#pymatgen.analysis.elasticity.stress.Stress"
  class="reference internal"
  title="pymatgen.analysis.elasticity.stress.Stress"><em>Stress</em></a>)
  – equilibrium stress to use in fitting

- **vasp** (*bool*) – flag for whether the stress tensor should be
  converted based on vasp units/convention for stress

- **tol** (*float*) – tolerance for removing near-zero elements of the
  resulting tensor.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_pseudoinverse</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">strains</span></span>*, *<span class="n"><span class="pre">stresses</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L464-L487"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.from_pseudoinverse"
class="headerlink" title="Link to this definition"></a>  
Class method to fit an elastic tensor from stress/strain data. Method
uses Moore-Penrose pseudo-inverse to invert the s = C\*e equation with
elastic tensor, stress, and strain in voigt notation.

Parameters<span class="colon">:</span>  
- **stresses** (*Nx3x3 array-like*) – list or array of stresses

- **strains** (*Nx3x3 array-like*) – list or array of strains

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">g_reuss</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/elasticity/elastic.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.g_reuss"
class="headerlink" title="Link to this definition"></a>  
The G_r shear modulus (in eV/A^3).

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">g_voigt</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/elasticity/elastic.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.g_voigt"
class="headerlink" title="Link to this definition"></a>  
The G_v shear modulus (in eV/A^3).

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">g_vrh</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/elasticity/elastic.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.g_vrh"
class="headerlink" title="Link to this definition"></a>  
The G_vrh (Voigt-Reuss-Hill) average shear modulus (in eV/A^3).

<span class="sig-name descname"><span class="pre">get_structure_property_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">include_base_props</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">ignore_errors</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L427-L462"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.get_structure_property_dict"
class="headerlink" title="Link to this definition"></a>  
Get a dictionary of properties derived from the elastic tensor and an
associated structure.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  structure object for which to calculate associated properties

- **include_base_props** (*bool*) – whether to include base properties,
  like k_vrh, etc.

- **ignore_errors** (*bool*) – if set to true, will set problem
  properties that depend on a physical tensor to None, defaults to False

<span class="sig-name descname"><span class="pre">green_kristoffel</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">u</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L407-L409"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.green_kristoffel"
class="headerlink" title="Link to this definition"></a>  
Get the Green-Kristoffel tensor for a second-order tensor.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">homogeneous_poisson</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/elasticity/elastic.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.homogeneous_poisson"
class="headerlink" title="Link to this definition"></a>  
The homogeneous poisson ratio.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">k_reuss</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/elasticity/elastic.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.k_reuss"
class="headerlink" title="Link to this definition"></a>  
The K_r bulk modulus (in eV/A^3).

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">k_voigt</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/elasticity/elastic.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.k_voigt"
class="headerlink" title="Link to this definition"></a>  
The K_v bulk modulus (in eV/A^3).

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">k_vrh</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/elasticity/elastic.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.k_vrh"
class="headerlink" title="Link to this definition"></a>  
The K_vrh (Voigt-Reuss-Hill) average bulk modulus (in eV/A^3).

<span class="sig-name descname"><span class="pre">long_v</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*</span></span><span class="n"><span class="pre">args</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L122-L125"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.long_v"
class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">property_dict</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/elasticity/elastic.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.property_dict"
class="headerlink" title="Link to this definition"></a>  
A dictionary of properties derived from the elastic tensor.

<span class="sig-name descname"><span class="pre">snyder_ac</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*</span></span><span class="n"><span class="pre">args</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L122-L125"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.snyder_ac"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">snyder_opt</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*</span></span><span class="n"><span class="pre">args</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L122-L125"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.snyder_opt"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">snyder_total</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*</span></span><span class="n"><span class="pre">args</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L122-L125"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.snyder_total"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">trans_v</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*</span></span><span class="n"><span class="pre">args</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L122-L125"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.trans_v"
class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">universal_anisotropy</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/elasticity/elastic.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.universal_anisotropy"
class="headerlink" title="Link to this definition"></a>  
The universal anisotropy value.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">y_mod</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/elasticity/elastic.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.elastic.ElasticTensor.y_mod"
class="headerlink" title="Link to this definition"></a>  
Calculates Young’s modulus (in SI units) using the Voigt-Reuss-Hill
averages of bulk and shear moduli.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ElasticTensorExpansion</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">c_list</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L543-L836"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion"
class="headerlink" title="Link to this definition"></a>  
Bases:
<a href="pymatgen.core.html#pymatgen.core.tensors.TensorCollection"
class="reference internal"
title="pymatgen.core.tensors.TensorCollection"><span class="pre"><code
class="sourceCode python">TensorCollection</code></span></a>

This class is a sequence of elastic tensors corresponding to an elastic
tensor expansion, which can be used to calculate stress and energy
density and inherits all of the list-based properties of
TensorCollection (e.g. symmetrization, voigt conversion, etc.).

Initialization method for ElasticTensorExpansion.

Parameters<span class="colon">:</span>  
**c_list** (*list* *or* *tuple*) – sequence of Tensor inputs or tensors
from which the elastic tensor expansion is constructed.

<span class="sig-name descname"><span class="pre">calculate_stress</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">strain</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L579-L584"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.calculate_stress"
class="headerlink" title="Link to this definition"></a>  
Calculate’s a given elastic tensor’s contribution to the stress using
Einstein summation.

<span class="sig-name descname"><span class="pre">energy_density</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">strain</span></span>*, *<span class="n"><span class="pre">convert_GPa_to_eV</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L586-L588"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.energy_density"
class="headerlink" title="Link to this definition"></a>  
Calculate the elastic energy density due to a strain in eV/A^3 or GPa.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_diff_fit</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">strains</span></span>*, *<span class="n"><span class="pre">stresses</span></span>*, *<span class="n"><span class="pre">eq_stress</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-10</span></span>*, *<span class="n"><span class="pre">order</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">3</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L563-L569"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.from_diff_fit"
class="headerlink" title="Link to this definition"></a>  
Generate an elastic tensor expansion via the fitting function defined
below in diff_fit.

<span class="sig-name descname"><span class="pre">get_compliance_expansion</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L733-L754"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.get_compliance_expansion"
class="headerlink" title="Link to this definition"></a>  
Get a compliance tensor expansion from the elastic tensor expansion.

<span class="sig-name descname"><span class="pre">get_effective_ecs</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">strain</span></span>*, *<span class="n"><span class="pre">order</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">2</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L766-L778"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.get_effective_ecs"
class="headerlink" title="Link to this definition"></a>  
Get the effective elastic constants from the elastic tensor expansion.

Parameters<span class="colon">:</span>  
- **strain** (<a href="#pymatgen.analysis.elasticity.strain.Strain"
  class="reference internal"
  title="pymatgen.analysis.elasticity.strain.Strain"><em>Strain</em></a>
  *or* *3x3 array-like*) – strain condition under which to calculate the
  effective constants

- **order** (*int*) – order of the ecs to be returned

<span class="sig-name descname"><span class="pre">get_ggt</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">n</span></span>*, *<span class="n"><span class="pre">u</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L590-L601"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.get_ggt"
class="headerlink" title="Link to this definition"></a>  
Get the Generalized Gruneisen tensor for a given third-order elastic
tensor expansion.

Parameters<span class="colon">:</span>  
- **n** (*3x1 array-like*) – normal mode direction

- **u** (*3x1 array-like*) – polarization direction

<span class="sig-name descname"><span class="pre">get_gruneisen_parameter</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">temperature</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">structure</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">quad</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L641-L654"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.get_gruneisen_parameter"
class="headerlink" title="Link to this definition"></a>  
Get the single average gruneisen parameter from the TGT.

Parameters<span class="colon">:</span>  
- **temperature** (*float*) – Temperature in kelvin, if not specified
  will return non-cv-normalized value

- **structure** (*float*) – Structure to be used in directional heat
  capacity determination, only necessary if temperature is specified

- **quadct** (*dict*) – quadrature for integration, should be dictionary
  with “points” and “weights” keys defaults to quadpy.sphere.Lebedev(19)
  as read from file

<span class="sig-name descname"><span class="pre">get_heat_capacity</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">temperature</span></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">n</span></span>*, *<span class="n"><span class="pre">u</span></span>*, *<span class="n"><span class="pre">cutoff</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">100.0</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L656-L677"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.get_heat_capacity"
class="headerlink" title="Link to this definition"></a>  
Get the directional heat capacity for a higher order tensor expansion as
a function of direction and polarization.

Parameters<span class="colon">:</span>  
- **temperature** (*float*) – Temperature in kelvin

- **structure** (*float*) – Structure to be used in directional heat
  capacity determination

- **n** (*3x1 array-like*) – direction for Cv determination

- **u** (*3x1 array-like*) – polarization direction, note that no
  attempt for verification of eigenvectors is made

- **cutoff** (*float*) – cutoff for scale of kt / (hbar \* omega) if
  lower than this value, returns 0

<span class="sig-name descname"><span class="pre">get_stability_criteria</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">s</span></span>*, *<span class="n"><span class="pre">n</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L810-L824"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.get_stability_criteria"
class="headerlink" title="Link to this definition"></a>  
Get the stability criteria from the symmetric Wallace tensor from an
input vector and stress value.

Parameters<span class="colon">:</span>  
- **s** (*float*) – Stress value at which to evaluate the stability
  criteria

- **n** (*3x1 array-like*) – direction of the applied stress

<span class="sig-name descname"><span class="pre">get_strain_from_stress</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">stress</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L756-L764"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.get_strain_from_stress"
class="headerlink" title="Link to this definition"></a>  
Get the strain from a stress state according to the compliance expansion
corresponding to the tensor expansion.

<span class="sig-name descname"><span class="pre">get_symmetric_wallace_tensor</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tau</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L799-L808"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.get_symmetric_wallace_tensor"
class="headerlink" title="Link to this definition"></a>  
Get the symmetrized wallace tensor for determining yield strength
criteria.

Parameters<span class="colon">:</span>  
**tau** (*3x3 array-like*) – stress at which to evaluate the wallace
tensor.

<span class="sig-name descname"><span class="pre">get_tgt</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">temperature</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">quad</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L603-L639"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.get_tgt"
class="headerlink" title="Link to this definition"></a>  
Get the thermodynamic Gruneisen tensor (TGT) by via an integration of
the GGT weighted by the directional heat capacity.

See refs:  
R. N. Thurston and K. Brugger, Phys. Rev. 113, A1604 (1964). K. Brugger
Phys. Rev. 137, A1826 (1965).

Parameters<span class="colon">:</span>  
- **temperature** (*float*) – Temperature in kelvin, if not specified
  will return non-cv-normalized value

- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  Structure to be used in directional heat capacity determination, only
  necessary if temperature is specified

- **quadct** (*dict*) – quadrature for integration, should be dictionary
  with “points” and “weights” keys defaults to quadpy.sphere.Lebedev(19)
  as read from file

<span class="sig-name descname"><span class="pre">get_wallace_tensor</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tau</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L780-L797"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.get_wallace_tensor"
class="headerlink" title="Link to this definition"></a>  
Get the Wallace Tensor for determining yield strength criteria.

Parameters<span class="colon">:</span>  
**tau** (*3x3 array-like*) – stress at which to evaluate the wallace
tensor

<span class="sig-name descname"><span class="pre">get_yield_stress</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">n</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L826-L836"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.get_yield_stress"
class="headerlink" title="Link to this definition"></a>  
Get the yield stress for a given direction.

Parameters<span class="colon">:</span>  
**n** (*3x1 array-like*) – direction for which to find the yield stress

<span class="sig-name descname"><span class="pre">omega</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">n</span></span>*, *<span class="n"><span class="pre">u</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L679-L695"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.omega"
class="headerlink" title="Link to this definition"></a>  
Find directional frequency contribution to the heat capacity from
direction and polarization.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  Structure to be used in directional heat capacity determination

- **n** (*3x1 array-like*) – direction for Cv determination

- **u** (*3x1 array-like*) – polarization direction, note that no
  attempt for verification of eigenvectors is made

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">order</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/elasticity/elastic.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.order"
class="headerlink" title="Link to this definition"></a>  
Order of the elastic tensor expansion, i.e. the order of the highest
included set of elastic constants.

<span class="sig-name descname"><span class="pre">thermal_expansion_coeff</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">temperature</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">mode</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'dulong</span> <span class="pre">-</span> <span class="pre">petit'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'debye'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'debye'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L697-L731"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.ElasticTensorExpansion.thermal_expansion_coeff"
class="headerlink" title="Link to this definition"></a>  
Get thermal expansion coefficient from third-order constants.

Parameters<span class="colon">:</span>  
- **temperature** (*float*) – Temperature in kelvin, if not specified
  will return non-cv-normalized value

- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  Structure to be used in directional heat capacity determination, only
  necessary if temperature is specified

- **mode** (*str*) – mode for finding average heat-capacity, current
  supported modes are ‘debye’ and ‘dulong-petit’

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">NthOrderElasticTensor</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">input_array</span></span>*, *<span class="n"><span class="pre">check_rank</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.0001</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L46-L113"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.elastic.NthOrderElasticTensor"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="pymatgen.core.html#pymatgen.core.tensors.Tensor"
class="reference internal" title="pymatgen.core.tensors.Tensor"><span
class="pre"><code class="sourceCode python">Tensor</code></span></a>

An object representing an nth-order tensor expansion of the
stress-strain constitutive equations.

Parameters<span class="colon">:</span>  
- **input_array** (*np.ndarray*) – input array for tensor

- **check_rank** (*int*) – rank of tensor to check

- **tol** (*float*) – tolerance for initial symmetry test of tensor

<span class="sig-name descname"><span class="pre">GPa_to_eV_A3</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">0.006241509074460764</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/elasticity/elastic.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.NthOrderElasticTensor.GPa_to_eV_A3"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">calculate_stress</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">strain</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L74-L88"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.NthOrderElasticTensor.calculate_stress"
class="headerlink" title="Link to this definition"></a>  
Calculate’s a given elastic tensor’s contribution to the stress using
Einstein summation.

Parameters<span class="colon">:</span>  
**strain** (*3x3 array-like*) – matrix corresponding to strain

<span class="sig-name descname"><span class="pre">energy_density</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">strain</span></span>*, *<span class="n"><span class="pre">convert_GPa_to_eV</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L90-L95"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.NthOrderElasticTensor.energy_density"
class="headerlink" title="Link to this definition"></a>  
Calculate the elastic energy density due to a strain.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_diff_fit</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">strains</span></span>*, *<span class="n"><span class="pre">stresses</span></span>*, *<span class="n"><span class="pre">eq_stress</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">order</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">2</span></span>*, *<span class="n"><span class="pre">tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-10</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L97-L113"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.NthOrderElasticTensor.from_diff_fit"
class="headerlink" title="Link to this definition"></a>  
Takes a list of strains and stresses, and returns a list of coefficients
for a polynomial fit of the given order.

Parameters<span class="colon">:</span>  
- **strains** – a list of strain values

- **stresses** – the stress values

- **eq_stress** – The stress at which the material is assumed to be
  elastic.

- **order** – The order of the polynomial to fit. Defaults to 2

- **tol** (*float*) – tolerance for the fit.

Returns<span class="colon">:</span>  
the fitted elastic tensor

Return type<span class="colon">:</span>  
<a href="#pymatgen.analysis.elasticity.elastic.NthOrderElasticTensor"
class="reference internal"
title="pymatgen.analysis.elasticity.elastic.NthOrderElasticTensor">NthOrderElasticTensor</a>

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">order</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/elasticity/elastic.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.NthOrderElasticTensor.order"
class="headerlink" title="Link to this definition"></a>  
Order of the elastic tensor.

<span class="sig-name descname"><span class="pre">symbol</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'C'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/elasticity/elastic.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.elastic.NthOrderElasticTensor.symbol"
class="headerlink" title="Link to this definition"></a>  

<!-- -->

<span class="sig-name descname"><span class="pre">diff_fit</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">strains</span></span>*, *<span class="n"><span class="pre">stresses</span></span>*, *<span class="n"><span class="pre">eq_stress</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">order</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">2</span></span>*, *<span class="n"><span class="pre">tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-10</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L840-L897"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.elastic.diff_fit"
class="headerlink" title="Link to this definition"></a>  
nth order elastic constant fitting function based on central-difference
derivatives with respect to distinct strain states. The algorithm is
summarized as follows:

1.  Identify distinct strain states as sets of indices for which nonzero
    strain values exist, typically \[(0), (1), (2), (3), (4), (5),
    (0, 1) etc.\]

2.  For each strain state, find and sort strains and stresses by strain
    value.

3.  Find first, second .. nth derivatives of each stress with respect to
    scalar variable corresponding to the smallest perturbation in the
    strain.

4.  Use the pseudo-inverse of a matrix-vector expression corresponding
    to the parameterized stress-strain relationship and multiply that
    matrix by the respective calculated first or second derivatives from
    the previous step.

5.  Place the calculated nth-order elastic constants appropriately.

Parameters<span class="colon">:</span>  
- **order** (*int*) – order of the elastic tensor set to return

- **strains** (*nx3x3 array-like*) – Array of 3x3 strains to use in
  fitting of ECs

- **stresses** (*nx3x3 array-like*) – Array of 3x3 stresses to use in
  fitting ECs. These should be PK2 stresses.

- **eq_stress** (*3x3 array-like*) – stress corresponding to equilibrium
  strain (i.e. “0” strain state). If not specified, function will try to
  find the state in the list of provided stresses and strains. If not
  found, defaults to 0.

- **tol** (*float*) – value for which strains below are ignored in
  identifying strain states.

Returns<span class="colon">:</span>  
Set of tensors corresponding to nth order expansion of the stress/strain
relation

<!-- -->

<span class="sig-name descname"><span class="pre">find_eq_stress</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">strains</span></span>*, *<span class="n"><span class="pre">stresses</span></span>*, *<span class="n"><span class="pre">tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-10</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L900-L924"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.elastic.find_eq_stress"
class="headerlink" title="Link to this definition"></a>  
Find stress corresponding to zero strain state in stress-strain list.

Parameters<span class="colon">:</span>  
- **strains** (*Nx3x3 array-like*) – array corresponding to strains

- **stresses** (*Nx3x3 array-like*) – array corresponding to stresses

- **tol** (*float*) – tolerance to find zero strain state

<!-- -->

<span class="sig-name descname"><span class="pre">generate_pseudo</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">strain_states</span></span>*, *<span class="n"><span class="pre">order</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">3</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L982-L1017"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.elastic.generate_pseudo"
class="headerlink" title="Link to this definition"></a>  
Generate the pseudo-inverse for a given set of strains.

Parameters<span class="colon">:</span>  
- **strain_states** (*6xN array like*) – a list of Voigt-notation
  strain-states, i.e. perturbed indices of the strain as a function of
  the smallest strain e.g. (0, 1, 0, 0, 1, 0)

- **order** (*int*) – order of pseudo-inverse to calculate

Returns<span class="colon">:</span>  
for each order tensor, these can be multiplied by the central  
difference derivative of the stress with respect to the strain state

absent_syms: symbols of the tensor absent from the PI expression

Return type<span class="colon">:</span>  
pseudo_inverses

<!-- -->

<span class="sig-name descname"><span class="pre">get_diff_coeff</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">hvec</span></span>*, *<span class="n"><span class="pre">n</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L1064-L1079"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.elastic.get_diff_coeff"
class="headerlink" title="Link to this definition"></a>  
Helper function to find difference coefficients of an derivative on an
arbitrary mesh.

Parameters<span class="colon">:</span>  
- **hvec** (*1D array-like*) – sampling stencil

- **n** (*int*) – degree of derivative to find

<!-- -->

<span class="sig-name descname"><span class="pre">get_strain_state_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">strains</span></span>*, *<span class="n"><span class="pre">stresses</span></span>*, *<span class="n"><span class="pre">eq_stress</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-10</span></span>*, *<span class="n"><span class="pre">add_eq</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">sort</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L927-L979"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.elastic.get_strain_state_dict"
class="headerlink" title="Link to this definition"></a>  
Create a dictionary of voigt notation stress-strain sets keyed by
“strain state”, i.e. a tuple corresponding to the non-zero entries in
ratios to the lowest nonzero value, e.g. \[0, 0.1, 0, 0.2, 0, 0\] -\>
(0,1,0,2,0,0) This allows strains to be collected in stencils as to
evaluate parameterized finite difference derivatives.

Parameters<span class="colon">:</span>  
- **strains** (*Nx3x3 array-like*) – strain matrices

- **stresses** (*Nx3x3 array-like*) – stress matrices

- **eq_stress** (*Nx3x3 array-like*) – equilibrium stress

- **tol** (*float*) – tolerance for sorting strain states

- **add_eq** (*bool*) – Whether to add eq_strain to stress-strain sets
  for each strain state. Defaults to True.

- **sort** (*bool*) – flag for whether to sort strain states

Returns<span class="colon">:</span>  
strain state keys and dictionaries with stress-strain data corresponding
to strain state

Return type<span class="colon">:</span>  
dict

<!-- -->

<span class="sig-name descname"><span class="pre">get_symbol_list</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">rank</span></span>*, *<span class="n"><span class="pre">dim</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">6</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L1020-L1041"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.elastic.get_symbol_list"
class="headerlink" title="Link to this definition"></a>  
Get a symbolic representation of the Voigt-notation tensor that places
identical symbols for entries related by index transposition, i.e.
C_1121 = C_1211 etc.

Parameters<span class="colon">:</span>  
- **dim** (*int*) – dimension of matrix/tensor, e.g. 6 for voigt
  notation and 3 for standard

- **rank** (*int*) – rank of tensor, e.g. 3 for third-order ECs

Returns<span class="colon">:</span>  
tuple of arrays representing the distinct  
indices and the tensor with equivalent indices assigned as above

Return type<span class="colon">:</span>  
tuple\[np.array, np.array\]

<!-- -->

<span class="sig-name descname"><span class="pre">raise_if_unphysical</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">func</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L116-L127"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.elastic.raise_if_unphysical"
class="headerlink" title="Link to this definition"></a>  
Wrapper for functions or properties that should raise an error if tensor
is unphysical.

<!-- -->

<span class="sig-name descname"><span class="pre">subs</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">entry</span></span>*, *<span class="n"><span class="pre">cmap</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/elastic.py#L1044-L1056"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.elastic.subs" class="headerlink"
title="Link to this definition"></a>  
Sympy substitution function, primarily for the purposes of numpy
vectorization.

Parameters<span class="colon">:</span>  
- **entry** (*symbol* *or* *exp*) – sympy expr to undergo subs

- **cmap** (*dict*) – map for symbols to values to use in subs

Returns<span class="colon">:</span>  
Evaluated expression with substitution

</div>

<div id="module-pymatgen.analysis.elasticity.strain" class="section">

<span id="pymatgen-analysis-elasticity-strain-module"></span>

## pymatgen.analysis.elasticity.strain module<a href="#module-pymatgen.analysis.elasticity.strain" class="headerlink"
title="Link to this heading"></a>

This module provides classes and methods used to describe deformations
and strains, including applying those deformations to structure objects
and generating deformed structure sets for further calculations.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Deformation</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">deformation_gradient</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/strain.py#L38-L97"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.strain.Deformation"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="pymatgen.core.html#pymatgen.core.tensors.SquareTensor"
class="reference internal"
title="pymatgen.core.tensors.SquareTensor"><span class="pre"><code
class="sourceCode python">SquareTensor</code></span></a>

Subclass of SquareTensor that describes the deformation gradient tensor.

Create a Deformation object. Note that the constructor uses \_\_new\_\_
rather than \_\_init\_\_ according to the standard method of subclassing
numpy arrays.

Parameters<span class="colon">:</span>  
**deformation_gradient** (*3x3 array-like*) – the 3x3 array-like
representing the deformation gradient

<span class="sig-name descname"><span class="pre">apply_to_structure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/strain.py#L70-L82"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.strain.Deformation.apply_to_structure"
class="headerlink" title="Link to this definition"></a>  
Apply the deformation gradient to a structure.

Parameters<span class="colon">:</span>  
**structure** (*Structure object*) – the structure object to be modified
by the deformation

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_index_amount</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">matrix_pos</span></span>*, *<span class="n"><span class="pre">amt</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/strain.py#L84-L97"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.strain.Deformation.from_index_amount"
class="headerlink" title="Link to this definition"></a>  
Factory method for constructing a Deformation object from a matrix
position and amount.

Parameters<span class="colon">:</span>  
- **matrix_pos** (*tuple*) – tuple corresponding the matrix position to
  have a perturbation added

- **amt** (*float*) – amount to add to the identity matrix at position
  matrix_pos

<span class="sig-name descname"><span class="pre">get_perturbed_indices</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-08</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/strain.py#L59-L63"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.strain.Deformation.get_perturbed_indices"
class="headerlink" title="Link to this definition"></a>  
Get indices of perturbed elements of the deformation gradient, i.e.
those that differ from the identity.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">green_lagrange_strain</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/elasticity/strain.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.strain.Deformation.green_lagrange_strain"
class="headerlink" title="Link to this definition"></a>  
Calculate the Euler-Lagrange strain from the deformation gradient.

<span class="sig-name descname"><span class="pre">is_independent</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-08</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/strain.py#L55-L57"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.strain.Deformation.is_independent"
class="headerlink" title="Link to this definition"></a>  
Check to determine whether the deformation is independent.

<span class="sig-name descname"><span class="pre">symbol</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'d'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/elasticity/strain.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.strain.Deformation.symbol"
class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">DeformedStructureSet</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">norm_strains</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">(-0.01,</span> <span class="pre">-0.005,</span> <span class="pre">0.005,</span> <span class="pre">0.01)</span></span>*, *<span class="n"><span class="pre">shear_strains</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">(-0.06,</span> <span class="pre">-0.03,</span> <span class="pre">0.03,</span> <span class="pre">0.06)</span></span>*, *<span class="n"><span class="pre">symmetry</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/strain.py#L100-L153"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.strain.DeformedStructureSet"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`Sequence`</span>

class that generates a set of independently deformed structures that can
be used to calculate linear stress-strain response.

Construct the deformed geometries of a structure. Generates m + n
deformed structures according to the supplied parameters.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  structure to undergo deformation

- **norm_strains** (*list* *of* *floats*) – strain values to apply to
  each normal mode. Defaults to (-0.01, -0.005, 0.005, 0.01).

- **shear_strains** (*list* *of* *floats*) – strain values to apply to
  each shear mode. Defaults to (-0.06, -0.03, 0.03, 0.06).

- **symmetry** (*bool*) – whether or not to use symmetry reduction.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Strain</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">strain_matrix</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/strain.py#L156-L237"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.strain.Strain" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="pymatgen.core.html#pymatgen.core.tensors.SquareTensor"
class="reference internal"
title="pymatgen.core.tensors.SquareTensor"><span class="pre"><code
class="sourceCode python">SquareTensor</code></span></a>

Subclass of SquareTensor that describes the Green-Lagrange strain
tensor.

Create a Strain object. Note that the constructor uses \_\_new\_\_
rather than \_\_init\_\_ according to the standard method of subclassing
numpy ndarrays. Note also that the default constructor does not include
the deformation gradient.

Parameters<span class="colon">:</span>  
**strain_matrix** (*ArrayLike*) – 3x3 matrix or length-6 Voigt notation
vector representing the Green-Lagrange strain

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_deformation</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">deformation</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/strain.py#L187-L196"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.strain.Strain.from_deformation"
class="headerlink" title="Link to this definition"></a>  
Factory method that returns a Strain object from a deformation gradient.

Parameters<span class="colon">:</span>  
**deformation** (*ArrayLike*) – 3x3 array defining the deformation

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_index_amount</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">idx</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">int</span></span>*, *<span class="n"><span class="pre">amount</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/strain.py#L198-L219"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.strain.Strain.from_index_amount"
class="headerlink" title="Link to this definition"></a>  
Like Deformation.from_index_amount, except generates a strain from the
zero 3x3 tensor or Voigt vector with the amount specified in the index
location. Ensures symmetric strain.

Parameters<span class="colon">:</span>  
- **idx** (*tuple* *or* *integer*) – index to be perturbed, can be Voigt
  or full-tensor notation

- **amount** (*float*) – amount to perturb selected index

<span class="sig-name descname"><span class="pre">get_deformation_matrix</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">shape</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'upper'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'lower'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'symmetric'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'upper'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/strain.py#L221-L230"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.strain.Strain.get_deformation_matrix"
class="headerlink" title="Link to this definition"></a>  
Get the deformation matrix.

Parameters<span class="colon">:</span>  
**shape** (*'upper'* *\|* *'lower'* *\|* *'symmetric'*) – method for
determining deformation ‘upper’ produces an upper triangular defo
‘lower’ produces a lower triangular defo ‘symmetric’ produces a
symmetric defo

<span class="sig-name descname"><span class="pre">symbol</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'e'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/elasticity/strain.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.strain.Strain.symbol"
class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">von_mises_strain</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/elasticity/strain.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.strain.Strain.von_mises_strain"
class="headerlink" title="Link to this definition"></a>  
Equivalent strain to Von Mises Stress.

<!-- -->

<span class="sig-name descname"><span class="pre">convert_strain_to_deformation</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">strain</span></span>*, *<span class="n"><span class="pre">shape</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'upper'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'lower'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'symmetric'</span></span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/strain.py#L240-L260"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.strain.convert_strain_to_deformation"
class="headerlink" title="Link to this definition"></a>  
This function converts a strain to a deformation gradient that will
produce that strain. Supports three methods:

Parameters<span class="colon">:</span>  
- **strain** (*3x3 array-like*) – strain matrix

- **shape** – (‘upper’ \| ‘lower’ \| ‘symmetric’): method for
  determining deformation ‘upper’ produces an upper triangular defo
  ‘lower’ produces a lower triangular defo ‘symmetric’ produces a
  symmetric defo

</div>

<div id="module-pymatgen.analysis.elasticity.stress" class="section">

<span id="pymatgen-analysis-elasticity-stress-module"></span>

## pymatgen.analysis.elasticity.stress module<a href="#module-pymatgen.analysis.elasticity.stress" class="headerlink"
title="Link to this heading"></a>

This module provides the Stress class used to create, manipulate, and
calculate relevant properties of the stress tensor.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Stress</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">stress_matrix</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/stress.py#L28-L101"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.stress.Stress" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="pymatgen.core.html#pymatgen.core.tensors.SquareTensor"
class="reference internal"
title="pymatgen.core.tensors.SquareTensor"><span class="pre"><code
class="sourceCode python">SquareTensor</code></span></a>

This class extends SquareTensor as a representation of the stress.

Create a Stress object. Note that the constructor uses \_\_new\_\_
rather than \_\_init\_\_ according to the standard method of subclassing
numpy ndarrays.

Parameters<span class="colon">:</span>  
**stress_matrix** (*3x3 array-like*) – the 3x3 array-like representing
the stress

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">dev_principal_invariants</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/elasticity/stress.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.elasticity.stress.Stress.dev_principal_invariants"
class="headerlink" title="Link to this definition"></a>  
The principal invariants of the deviatoric stress tensor, which is
calculated by finding the coefficients of the characteristic polynomial
of the stress tensor minus the identity times the mean stress.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">deviator_stress</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/elasticity/stress.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.stress.Stress.deviator_stress"
class="headerlink" title="Link to this definition"></a>  
The deviatoric component of the stress.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">mean_stress</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/elasticity/stress.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.stress.Stress.mean_stress"
class="headerlink" title="Link to this definition"></a>  
The mean stress.

<span class="sig-name descname"><span class="pre">piola_kirchoff_1</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">def_grad</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/stress.py#L79-L89"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.stress.Stress.piola_kirchoff_1"
class="headerlink" title="Link to this definition"></a>  
Calculates the first Piola-Kirchoff stress.

Parameters<span class="colon">:</span>  
**def_grad** (*3x3 array-like*) – deformation gradient tensor

<span class="sig-name descname"><span class="pre">piola_kirchoff_2</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">def_grad</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/elasticity/stress.py#L91-L101"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.stress.Stress.piola_kirchoff_2"
class="headerlink" title="Link to this definition"></a>  
Calculates the second Piola-Kirchoff stress.

Parameters<span class="colon">:</span>  
**def_grad** (*3x3 array-like*) – rate of deformation tensor

<span class="sig-name descname"><span class="pre">symbol</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'s'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/elasticity/stress.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.stress.Stress.symbol"
class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">von_mises</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/elasticity/stress.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.analysis.elasticity.stress.Stress.von_mises"
class="headerlink" title="Link to this definition"></a>  
The von Mises stress.

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
