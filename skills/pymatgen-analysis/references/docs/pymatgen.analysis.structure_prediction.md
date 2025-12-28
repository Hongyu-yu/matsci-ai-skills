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
  class="reference internal">pymatgen.analysis.structure_prediction
  package</a>
  - <a href="#submodules" class="reference internal">Submodules</a>
  - <a
    href="#module-pymatgen.analysis.structure_prediction.dopant_predictor"
    class="reference internal">pymatgen.analysis.structure_prediction.dopant_predictor
    module</a>
    - <a
      href="#pymatgen.analysis.structure_prediction.dopant_predictor.get_dopants_from_shannon_radii"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">get_dopants_from_shannon_radii()</code></span></a>
    - <a
      href="#pymatgen.analysis.structure_prediction.dopant_predictor.get_dopants_from_substitution_probabilities"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">get_dopants_from_substitution_probabilities()</code></span></a>
  - <a
    href="#module-pymatgen.analysis.structure_prediction.substitution_probability"
    class="reference internal">pymatgen.analysis.structure_prediction.substitution_probability
    module</a>
    - <a
      href="#pymatgen.analysis.structure_prediction.substitution_probability.SubstitutionPredictor"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">SubstitutionPredictor</code></span></a>
      - <a
        href="#pymatgen.analysis.structure_prediction.substitution_probability.SubstitutionPredictor.composition_prediction"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SubstitutionPredictor.composition_prediction()</code></span></a>
      - <a
        href="#pymatgen.analysis.structure_prediction.substitution_probability.SubstitutionPredictor.list_prediction"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SubstitutionPredictor.list_prediction()</code></span></a>
    - <a
      href="#pymatgen.analysis.structure_prediction.substitution_probability.SubstitutionProbability"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">SubstitutionProbability</code></span></a>
      - <a
        href="#pymatgen.analysis.structure_prediction.substitution_probability.SubstitutionProbability.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SubstitutionProbability.as_dict()</code></span></a>
      - <a
        href="#pymatgen.analysis.structure_prediction.substitution_probability.SubstitutionProbability.cond_prob"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SubstitutionProbability.cond_prob()</code></span></a>
      - <a
        href="#pymatgen.analysis.structure_prediction.substitution_probability.SubstitutionProbability.cond_prob_list"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SubstitutionProbability.cond_prob_list()</code></span></a>
      - <a
        href="#pymatgen.analysis.structure_prediction.substitution_probability.SubstitutionProbability.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SubstitutionProbability.from_dict()</code></span></a>
      - <a
        href="#pymatgen.analysis.structure_prediction.substitution_probability.SubstitutionProbability.get_lambda"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SubstitutionProbability.get_lambda()</code></span></a>
      - <a
        href="#pymatgen.analysis.structure_prediction.substitution_probability.SubstitutionProbability.get_px"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SubstitutionProbability.get_px()</code></span></a>
      - <a
        href="#pymatgen.analysis.structure_prediction.substitution_probability.SubstitutionProbability.pair_corr"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SubstitutionProbability.pair_corr()</code></span></a>
      - <a
        href="#pymatgen.analysis.structure_prediction.substitution_probability.SubstitutionProbability.prob"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SubstitutionProbability.prob()</code></span></a>
  - <a href="#module-pymatgen.analysis.structure_prediction.substitutor"
    class="reference internal">pymatgen.analysis.structure_prediction.substitutor
    module</a>
    - <a
      href="#pymatgen.analysis.structure_prediction.substitutor.Substitutor"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Substitutor</code></span></a>
      - <a
        href="#pymatgen.analysis.structure_prediction.substitutor.Substitutor.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Substitutor.as_dict()</code></span></a>
      - <a
        href="#pymatgen.analysis.structure_prediction.substitutor.Substitutor.charge_balanced_tol"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Substitutor.charge_balanced_tol</code></span></a>
      - <a
        href="#pymatgen.analysis.structure_prediction.substitutor.Substitutor.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Substitutor.from_dict()</code></span></a>
      - <a
        href="#pymatgen.analysis.structure_prediction.substitutor.Substitutor.get_allowed_species"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Substitutor.get_allowed_species()</code></span></a>
      - <a
        href="#pymatgen.analysis.structure_prediction.substitutor.Substitutor.pred_from_comp"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Substitutor.pred_from_comp()</code></span></a>
      - <a
        href="#pymatgen.analysis.structure_prediction.substitutor.Substitutor.pred_from_list"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Substitutor.pred_from_list()</code></span></a>
      - <a
        href="#pymatgen.analysis.structure_prediction.substitutor.Substitutor.pred_from_structures"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Substitutor.pred_from_structures()</code></span></a>
  - <a
    href="#module-pymatgen.analysis.structure_prediction.volume_predictor"
    class="reference internal">pymatgen.analysis.structure_prediction.volume_predictor
    module</a>
    - <a
      href="#pymatgen.analysis.structure_prediction.volume_predictor.DLSVolumePredictor"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">DLSVolumePredictor</code></span></a>
      - <a
        href="#pymatgen.analysis.structure_prediction.volume_predictor.DLSVolumePredictor.get_predicted_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DLSVolumePredictor.get_predicted_structure()</code></span></a>
      - <a
        href="#pymatgen.analysis.structure_prediction.volume_predictor.DLSVolumePredictor.predict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DLSVolumePredictor.predict()</code></span></a>
    - <a
      href="#pymatgen.analysis.structure_prediction.volume_predictor.RLSVolumePredictor"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">RLSVolumePredictor</code></span></a>
      - <a
        href="#pymatgen.analysis.structure_prediction.volume_predictor.RLSVolumePredictor.get_predicted_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RLSVolumePredictor.get_predicted_structure()</code></span></a>
      - <a
        href="#pymatgen.analysis.structure_prediction.volume_predictor.RLSVolumePredictor.predict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RLSVolumePredictor.predict()</code></span></a>

</div>

</div>

</div>

<div class="section wy-nav-content-wrap" toggle="wy-nav-shift">

[pymatgen](index.html)

<div class="wy-nav-content">

<div class="rst-content style-external-links">

<div role="navigation" aria-label="Page navigation">

- <a href="index.html" class="icon icon-home" aria-label="Home"></a>
- pymatgen.analysis.structure_prediction package
- <a
  href="https://github.com/materialsproject/pymatgen/blob/master/docs_rst/pymatgen.analysis.structure_prediction.rst"
  class="fa fa-github">Edit on GitHub</a>

------------------------------------------------------------------------

</div>

<div class="document" role="main" itemscope="itemscope"
itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="module-pymatgen.analysis.structure_prediction" class="section">

<span id="pymatgen-analysis-structure-prediction-package"></span>

# pymatgen.analysis.structure_prediction package<a href="#module-pymatgen.analysis.structure_prediction"
class="headerlink" title="Link to this heading"></a>

Utilities to predict new structures.

<div id="submodules" class="section">

## Submodules<a href="#submodules" class="headerlink"
title="Link to this heading"></a>

</div>

<div id="module-pymatgen.analysis.structure_prediction.dopant_predictor"
class="section">

<span
id="pymatgen-analysis-structure-prediction-dopant-predictor-module"></span>

## pymatgen.analysis.structure_prediction.dopant_predictor module<a
href="#module-pymatgen.analysis.structure_prediction.dopant_predictor"
class="headerlink" title="Link to this heading"></a>

Predicting potential dopants.

<span class="sig-name descname"><span class="pre">get_dopants_from_shannon_radii</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">bonded_structure</span></span>*, *<span class="n"><span class="pre">num_dopants</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">5</span></span>*, *<span class="n"><span class="pre">match_oxi_sign</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/structure_prediction/dopant_predictor.py#L60-L125"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.structure_prediction.dopant_predictor.get_dopants_from_shannon_radii"
class="headerlink" title="Link to this definition"></a>  
Get dopant suggestions based on Shannon radii differences.

Parameters<span class="colon">:</span>  
- **bonded_structure**
  (<a href="pymatgen.analysis.html#pymatgen.analysis.graphs.StructureGraph"
  class="reference internal"
  title="pymatgen.analysis.graphs.StructureGraph"><em>StructureGraph</em></a>)
  – A pymatgen structure graph decorated with oxidation states. For
  example, generated using the CrystalNN.get_bonded_structure() method.

- **num_dopants** (*int*) – The number of suggestions to return for n-
  and p-type dopants.

- **match_oxi_sign** (*bool*) – Whether to force the dopant and original
  species to have the same sign of oxidation state. E.g. If the original
  site is in a negative charge state, then only negative dopants will be
  returned.

Returns<span class="colon">:</span>  
Dopant suggestions, given as a dictionary with keys “n_type” and  
”p_type”. The suggestions for each doping type are given as a list of
dictionaries, each with they keys:

- ”radii_diff”: The difference between the Shannon radii of the species.

- ”dopant_species”: The dopant species.

- ”original_species”: The substituted species.

Return type<span class="colon">:</span>  
dict

<!-- -->

<span class="sig-name descname"><span class="pre">get_dopants_from_substitution_probabilities</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span>*, *<span class="n"><span class="pre">num_dopants</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">5</span></span>*, *<span class="n"><span class="pre">threshold</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.001</span></span>*, *<span class="n"><span class="pre">match_oxi_sign</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/structure_prediction/dopant_predictor.py#L13-L57"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.structure_prediction.dopant_predictor.get_dopants_from_substitution_probabilities"
class="headerlink" title="Link to this definition"></a>  
Get dopant suggestions based on substitution probabilities.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) – A
  pymatgen structure decorated with oxidation states.

- **num_dopants** (*int*) – The number of suggestions to return for n-
  and p-type dopants.

- **threshold** (*float*) – Probability threshold for substitutions.

- **match_oxi_sign** (*bool*) – Whether to force the dopant and original
  species to have the same sign of oxidation state. E.g. If the original
  site is in a negative charge state, then only negative dopants will be
  returned.

Returns<span class="colon">:</span>  
Dopant suggestions, given as a dictionary with keys “n_type” and  
”p_type”. The suggestions for each doping type are given as a list of
dictionaries, each with they keys:

- ”probability”: The probability of substitution.

- ”dopant_species”: The dopant species.

- ”original_species”: The substituted species.

Return type<span class="colon">:</span>  
dict

</div>

<div
id="module-pymatgen.analysis.structure_prediction.substitution_probability"
class="section">

<span
id="pymatgen-analysis-structure-prediction-substitution-probability-module"></span>

## pymatgen.analysis.structure_prediction.substitution_probability module<a
href="#module-pymatgen.analysis.structure_prediction.substitution_probability"
class="headerlink" title="Link to this heading"></a>

This module provides classes for representing species substitution
probabilities.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">SubstitutionPredictor</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">lambda_table</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">alpha</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">-5</span></span>*, *<span class="n"><span class="pre">threshold</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.001</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/structure_prediction/substitution_probability.py#L184-L281"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.structure_prediction.substitution_probability.SubstitutionPredictor"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Predicts likely substitutions either to or from a given composition or
species list using the SubstitutionProbability.

Parameters<span class="colon">:</span>  
- **lambda_table** (*dict*) – Input lambda table.

- **alpha** (*float*) – weight function for never observed substitutions

- **threshold** (*float*) – Threshold to use to identify high
  probability structures.

<span class="sig-name descname"><span class="pre">composition_prediction</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">composition</span></span>*, *<span class="n"><span class="pre">to_this_composition</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/structure_prediction/substitution_probability.py#L252-L281"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.structure_prediction.substitution_probability.SubstitutionPredictor.composition_prediction"
class="headerlink" title="Link to this definition"></a>  
Get charged balanced substitutions from a starting or ending
composition.

Parameters<span class="colon">:</span>  
- **composition** – starting or ending composition

- **to_this_composition** – If true, substitutions with this as a final
  composition will be found. If false, substitutions with this as a
  starting composition will be found (these are slightly different)

Returns<span class="colon">:</span>  
List of predictions in the form of dictionaries. If to_this_composition
is true, the values of the dictionary will be from the list species. If
false, the keys will be from that list.

<span class="sig-name descname"><span class="pre">list_prediction</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">species</span></span>*, *<span class="n"><span class="pre">to_this_composition</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/structure_prediction/substitution_probability.py#L200-L250"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.structure_prediction.substitution_probability.SubstitutionPredictor.list_prediction"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
- **species** – list of species

- **to_this_composition** – If true, substitutions with this as a final
  composition will be found. If false, substitutions with this as a
  starting composition will be found (these are slightly different).

Returns<span class="colon">:</span>  
List of predictions in the form of dictionaries. If to_this_composition
is true, the values of the dictionary will be from the list species. If
false, the keys will be from that list.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">SubstitutionProbability</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/structure_prediction/substitution_probability.py#L35-L181"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.structure_prediction.substitution_probability.SubstitutionProbability"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

This class finds substitution probabilities given lists of atoms to
substitute. The inputs make more sense if you look through the
from_defaults static method.

The substitution prediction algorithm is presented in: Hautier, G.,
Fischer, C., Ehrlacher, V., Jain, A., and Ceder, G. (2011) Data Mined
Ionic Substitutions for the Discovery of New Compounds. Inorganic
Chemistry, 50(2), 656-663. doi:10.1021/ic102031h

Parameters<span class="colon">:</span>  
- **lambda_table** – JSON table of the weight functions lambda if None,
  will use the default lambda.json table

- **alpha** (*float*) – weight function for never observed
  substitutions.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/structure_prediction/substitution_probability.py#L162-L170"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.structure_prediction.substitution_probability.SubstitutionProbability.as_dict"
class="headerlink" title="Link to this definition"></a>  
Get MSONable dict.

<span class="sig-name descname"><span class="pre">cond_prob</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">s1</span></span>*, *<span class="n"><span class="pre">s2</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/structure_prediction/substitution_probability.py#L119-L132"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.structure_prediction.substitution_probability.SubstitutionProbability.cond_prob"
class="headerlink" title="Link to this definition"></a>  
Conditional probability of substituting s1 for s2.

Parameters<span class="colon">:</span>  
- **s1** – The *variable* specie

- **s2** – The *fixed* specie

Returns<span class="colon">:</span>  
Conditional probability used by structure predictor.

<span class="sig-name descname"><span class="pre">cond_prob_list</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">l1</span></span>*, *<span class="n"><span class="pre">l2</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/structure_prediction/substitution_probability.py#L143-L160"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.structure_prediction.substitution_probability.SubstitutionProbability.cond_prob_list"
class="headerlink" title="Link to this definition"></a>  
Find the probabilities of 2 lists. These should include ALL species.
This is the probability conditional on l2.

Parameters<span class="colon">:</span>  
- **l1** – lists of species

- **l2** – lists of species

Returns<span class="colon">:</span>  
The conditional probability (assuming these species are in l2)

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/structure_prediction/substitution_probability.py#L172-L181"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.structure_prediction.substitution_probability.SubstitutionProbability.from_dict"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
**dct** (*dict*) – Dict representation.

Returns<span class="colon">:</span>  
Class

<span class="sig-name descname"><span class="pre">get_lambda</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">s1</span></span>*, *<span class="n"><span class="pre">s2</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/structure_prediction/substitution_probability.py#L88-L98"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.structure_prediction.substitution_probability.SubstitutionProbability.get_lambda"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
- **s1** (*SpeciesLike*) – Ion in 1st structure.

- **s2** (*SpeciesLike*) – Ion in 2nd structure.

Returns<span class="colon">:</span>  
Lambda values

<span class="sig-name descname"><span class="pre">get_px</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">sp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">SpeciesLike</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/structure_prediction/substitution_probability.py#L100-L108"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.structure_prediction.substitution_probability.SubstitutionProbability.get_px"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
**sp** (*SpeciesLike*) – Species.

Returns<span class="colon">:</span>  
Probability

Return type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">pair_corr</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">s1</span></span>*, *<span class="n"><span class="pre">s2</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/structure_prediction/substitution_probability.py#L134-L141"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.structure_prediction.substitution_probability.SubstitutionProbability.pair_corr"
class="headerlink" title="Link to this definition"></a>  
Pair correlation of two species.

Returns<span class="colon">:</span>  
The pair correlation of 2 species

<span class="sig-name descname"><span class="pre">prob</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">s1</span></span>*, *<span class="n"><span class="pre">s2</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/structure_prediction/substitution_probability.py#L110-L117"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.structure_prediction.substitution_probability.SubstitutionProbability.prob"
class="headerlink" title="Link to this definition"></a>  
Get the probability of 2 species substitution. Not used by the structure
predictor.

Returns<span class="colon">:</span>  
Probability of s1 and s2 substitution.

</div>

<div id="module-pymatgen.analysis.structure_prediction.substitutor"
class="section">

<span
id="pymatgen-analysis-structure-prediction-substitutor-module"></span>

## pymatgen.analysis.structure_prediction.substitutor module<a href="#module-pymatgen.analysis.structure_prediction.substitutor"
class="headerlink" title="Link to this heading"></a>

This module provides classes for predicting new structures from existing
ones.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Substitutor</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">threshold</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.001</span></span>*, *<span class="n"><span class="pre">symprec</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.1</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/structure_prediction/substitutor.py#L34-L265"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.structure_prediction.substitutor.Substitutor"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

This object uses a data mined ionic substitution approach to propose
compounds likely to be stable. It relies on an algorithm presented in
Hautier, G., Fischer, C., Ehrlacher, V., Jain, A., and Ceder, G. (2011).
Data Mined Ionic Substitutions for the Discovery of New Compounds.
Inorganic Chemistry, 50(2), 656-663. doi:10.1021/ic102031h.

Use the substitution probability class to find good substitutions for a
given chemistry or structure.

Parameters<span class="colon">:</span>  
- **threshold** – probability threshold for predictions

- **symprec** – symmetry precision to determine if two structures are
  duplicates

- **kwargs** – kwargs for the SubstitutionProbability object
  lambda_table, alpha

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/structure_prediction/substitutor.py#L243-L252"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.structure_prediction.substitutor.Substitutor.as_dict"
class="headerlink" title="Link to this definition"></a>  
Get MSONable dict.

<span class="sig-name descname"><span class="pre">charge_balanced_tol</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">1e-09</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/analysis/structure_prediction/substitutor.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.structure_prediction.substitutor.Substitutor.charge_balanced_tol"
class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/structure_prediction/substitutor.py#L254-L265"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.structure_prediction.substitutor.Substitutor.from_dict"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
**dct** (*dict*) – Dict representation.

Returns<span class="colon">:</span>  
Class

<span class="sig-name descname"><span class="pre">get_allowed_species</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/structure_prediction/substitutor.py#L67-L71"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.structure_prediction.substitutor.Substitutor.get_allowed_species"
class="headerlink" title="Link to this definition"></a>  
Get the species in the domain of the probability function any other
specie will not work.

<span class="sig-name descname"><span class="pre">pred_from_comp</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">composition</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/structure_prediction/substitutor.py#L226-L241"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.structure_prediction.substitutor.Substitutor.pred_from_comp"
class="headerlink" title="Link to this definition"></a>  
Similar to pred_from_list except this method returns a list after
checking that compositions are charge balanced.

<span class="sig-name descname"><span class="pre">pred_from_list</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">species_list</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/structure_prediction/substitutor.py#L173-L224"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.structure_prediction.substitutor.Substitutor.pred_from_list"
class="headerlink" title="Link to this definition"></a>  
There are an exceptionally large number of substitutions to look at
(260^n), where n is the number of species in the list. We need a more
efficient than brute force way of going through these possibilities. The
brute force method would be:

> <div>
>
> output = \[\] for p in itertools.product(self.\_sp.species_list,
> repeat=len(species_list)):
>
> > <div>
> >
> > if self.\_sp.conditional_probability_list(p, species_list) \> self.\_threshold:  
> > output.append(dict(zip(species_list, p)))
> >
> > </div>
>
> return output
>
> </div>

Instead of that we do a branch and bound.

Parameters<span class="colon">:</span>  
**species_list** – list of species in the starting structure

Returns<span class="colon">:</span>  
list of dictionaries, each including a substitutions dictionary, and a
probability value

<span class="sig-name descname"><span class="pre">pred_from_structures</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">target_species</span></span>*, *<span class="n"><span class="pre">structures</span></span>*, *<span class="n"><span class="pre">remove_duplicates</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">remove_existing</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a
href="pymatgen.alchemy.html#pymatgen.alchemy.materials.TransformedStructure"
class="reference internal"
title="pymatgen.alchemy.materials.TransformedStructure"><span
class="pre">TransformedStructure</span></a><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/structure_prediction/substitutor.py#L73-L161"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.structure_prediction.substitutor.Substitutor.pred_from_structures"
class="headerlink" title="Link to this definition"></a>  
Performs a structure prediction targeting compounds containing all of
the target_species, based on a list of structure (those structures can
for instance come from a database like the ICSD). It will return all the
structures formed by ionic substitutions with a probability higher than
the threshold.

Notes

If the default probability model is used, input structures must be
oxidation state decorated. See AutoOxiStateDecorationTransformation

This method does not change the number of species in a structure. i.e if
the number of target species is 3, only input structures containing 3
species will be considered.

Parameters<span class="colon">:</span>  
- **target_species** – a list of species with oxidation states e.g.
  \[Species(‘Li+’), Species(‘Ni2+’), Species(‘O-2’)\]

- **structures_list** – list of dictionary of the form {‘structure’:
  Structure object, ‘id’: some id where it comes from} The id can for
  instance refer to an ICSD id.

- **remove_duplicates** – if True, the duplicates in the predicted
  structures will be removed

- **remove_existing** – if True, the predicted structures that already
  exist in the structures_list will be removed

Returns<span class="colon">:</span>  
a list of TransformedStructure objects.

</div>

<div id="module-pymatgen.analysis.structure_prediction.volume_predictor"
class="section">

<span
id="pymatgen-analysis-structure-prediction-volume-predictor-module"></span>

## pymatgen.analysis.structure_prediction.volume_predictor module<a
href="#module-pymatgen.analysis.structure_prediction.volume_predictor"
class="headerlink" title="Link to this heading"></a>

Predict volumes of crystal structures.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">DLSVolumePredictor</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">cutoff</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">4.0</span></span>*, *<span class="n"><span class="pre">min_scaling</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.5</span></span>*, *<span class="n"><span class="pre">max_scaling</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1.5</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/structure_prediction/volume_predictor.py#L132-L241"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.structure_prediction.volume_predictor.DLSVolumePredictor"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Data-mined lattice scaling (DLS) scheme that relies on data-mined bond
lengths to predict the crystal volume of a given structure.

As of 2/12/19, we suggest this method be used in conjunction with
min_scaling and max_scaling to prevent instances of very large,
unphysical predicted volumes found in a small subset of structures.

Parameters<span class="colon">:</span>  
- **cutoff** (*float*) – cutoff radius added to site radius for finding
  site pairs. Necessary to increase only if your initial structure guess
  is extremely bad (atoms way too far apart). In all other instances,
  increasing cutoff gives same answer but takes more time.

- **min_scaling** (*float*) – if not None, this will ensure that the new
  volume is at least this fraction of the original (preventing too-small
  volumes)

- **max_scaling** (*float*) – if not None, this will ensure that the new
  volume is at most this fraction of the original (preventing too-large
  volumes).

<span class="sig-name descname"><span class="pre">get_predicted_structure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">icsd_vol</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/structure_prediction/volume_predictor.py#L228-L241"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.structure_prediction.volume_predictor.DLSVolumePredictor.get_predicted_structure"
class="headerlink" title="Link to this definition"></a>  
Given a structure, returns back the structure scaled to predicted
volume.

Parameters<span class="colon">:</span>  
**structure**
(<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
structure w/unknown volume

Returns<span class="colon">:</span>  
a Structure object with predicted volume

<span class="sig-name descname"><span class="pre">predict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">icsd_vol</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/structure_prediction/volume_predictor.py#L161-L226"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.structure_prediction.volume_predictor.DLSVolumePredictor.predict"
class="headerlink" title="Link to this definition"></a>  
Given a structure, returns the predicted volume.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) – a
  crystal structure with an unknown volume.

- **icsd_vol** (*bool*) – True if the input structure’s volume comes
  from ICSD.

Returns<span class="colon">:</span>  
a float value of the predicted volume.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">RLSVolumePredictor</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">check_isostructural</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">radii_type</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'ionic-atomic'</span></span>*, *<span class="n"><span class="pre">use_bv</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/structure_prediction/volume_predictor.py#L23-L129"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.structure_prediction.volume_predictor.RLSVolumePredictor"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Reference lattice scaling (RLS) scheme that predicts the volume of a
structure based on a known crystal structure.

Parameters<span class="colon">:</span>  
- **check_isostructural** – Whether to test that the two structures are
  isostructural. This algo works best for isostructural compounds.
  Defaults to True.

- **radii_type** (*str*) – Types of radii to use. You can specify
  “ionic” (only uses ionic radii), “atomic” (only uses atomic radii) or
  “ionic-atomic” (uses either ionic or atomic radii, with a preference
  for ionic where possible).

- **use_bv** (*bool*) – Whether to use BVAnalyzer to determine oxidation
  states if not present.

<span class="sig-name descname"><span class="pre">get_predicted_structure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">ref_structure</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/structure_prediction/volume_predictor.py#L113-L129"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.structure_prediction.volume_predictor.RLSVolumePredictor.get_predicted_structure"
class="headerlink" title="Link to this definition"></a>  
Given a structure, returns back the structure scaled to predicted
volume.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  structure w/unknown volume

- **ref_structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) – A
  reference structure with a similar structure but different species.

Returns<span class="colon">:</span>  
a Structure object with predicted volume

<span class="sig-name descname"><span class="pre">predict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">ref_structure</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../analysis/structure_prediction/volume_predictor.py#L46-L111"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.analysis.structure_prediction.volume_predictor.RLSVolumePredictor.predict"
class="headerlink" title="Link to this definition"></a>  
Given a structure, returns the predicted volume.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  structure w/unknown volume

- **ref_structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) – A
  reference structure with a similar structure but different species.

Returns<span class="colon">:</span>  
a float value of the predicted volume

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
