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

- <a href="#" class="reference internal">pymatgen.ext namespace</a>
  - <a href="#submodules" class="reference internal">Submodules</a>
  - <a href="#module-pymatgen.ext.cod"
    class="reference internal">pymatgen.ext.cod module</a>
    - <a href="#pymatgen.ext.cod.COD" class="reference internal"><span
      class="pre"><code
      class="docutils literal notranslate">COD</code></span></a>
      - <a href="#pymatgen.ext.cod.COD.get_cod_ids"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">COD.get_cod_ids()</code></span></a>
      - <a href="#pymatgen.ext.cod.COD.get_structure_by_formula"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">COD.get_structure_by_formula()</code></span></a>
      - <a href="#pymatgen.ext.cod.COD.get_structure_by_id"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">COD.get_structure_by_id()</code></span></a>
  - <a href="#module-pymatgen.ext.matproj"
    class="reference internal">pymatgen.ext.matproj module</a>
    - <a href="#pymatgen.ext.matproj.MPRestError"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">MPRestError</code></span></a>
    - <a href="#pymatgen.ext.matproj.MPRester"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">MPRester</code></span></a>
      - <a href="#pymatgen.ext.matproj.MPRester.MATERIALS_DOCS"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MPRester.MATERIALS_DOCS</code></span></a>
      - <a href="#pymatgen.ext.matproj.MPRester.get_doc"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MPRester.get_doc()</code></span></a>
      - <a href="#pymatgen.ext.matproj.MPRester.get_entries"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MPRester.get_entries()</code></span></a>
      - <a href="#pymatgen.ext.matproj.MPRester.get_entries_in_chemsys"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MPRester.get_entries_in_chemsys()</code></span></a>
      - <a href="#pymatgen.ext.matproj.MPRester.get_entry_by_material_id"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MPRester.get_entry_by_material_id()</code></span></a>
      - <a
        href="#pymatgen.ext.matproj.MPRester.get_initial_structures_by_material_id"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MPRester.get_initial_structures_by_material_id()</code></span></a>
      - <a href="#pymatgen.ext.matproj.MPRester.get_material_ids"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MPRester.get_material_ids()</code></span></a>
      - <a href="#pymatgen.ext.matproj.MPRester.get_materials_ids"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MPRester.get_materials_ids()</code></span></a>
      - <a
        href="#pymatgen.ext.matproj.MPRester.get_phonon_bandstructure_by_material_id"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MPRester.get_phonon_bandstructure_by_material_id()</code></span></a>
      - <a href="#pymatgen.ext.matproj.MPRester.get_phonon_dos_by_material_id"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MPRester.get_phonon_dos_by_material_id()</code></span></a>
      - <a href="#pymatgen.ext.matproj.MPRester.get_structure_by_material_id"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MPRester.get_structure_by_material_id()</code></span></a>
      - <a href="#pymatgen.ext.matproj.MPRester.get_structures"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MPRester.get_structures()</code></span></a>
      - <a href="#pymatgen.ext.matproj.MPRester.get_summary"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MPRester.get_summary()</code></span></a>
      - <a href="#pymatgen.ext.matproj.MPRester.get_summary_by_material_id"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MPRester.get_summary_by_material_id()</code></span></a>
      - <a href="#pymatgen.ext.matproj.MPRester.request"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MPRester.request()</code></span></a>
      - <a href="#pymatgen.ext.matproj.MPRester.search"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MPRester.search()</code></span></a>
      - <a href="#pymatgen.ext.matproj.MPRester.summary_search"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MPRester.summary_search()</code></span></a>
  - <a href="#module-pymatgen.ext.optimade"
    class="reference internal">pymatgen.ext.optimade module</a>
    - <a href="#pymatgen.ext.optimade.OptimadeRester"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">OptimadeRester</code></span></a>
      - <a href="#pymatgen.ext.optimade.OptimadeRester.aliases"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">OptimadeRester.aliases</code></span></a>
      - <a href="#pymatgen.ext.optimade.OptimadeRester.describe"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">OptimadeRester.describe()</code></span></a>
      - <a href="#pymatgen.ext.optimade.OptimadeRester.get_snls"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">OptimadeRester.get_snls()</code></span></a>
      - <a href="#pymatgen.ext.optimade.OptimadeRester.get_snls_with_filter"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">OptimadeRester.get_snls_with_filter()</code></span></a>
      - <a href="#pymatgen.ext.optimade.OptimadeRester.get_structures"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">OptimadeRester.get_structures()</code></span></a>
      - <a
        href="#pymatgen.ext.optimade.OptimadeRester.get_structures_with_filter"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">OptimadeRester.get_structures_with_filter()</code></span></a>
      - <a
        href="#pymatgen.ext.optimade.OptimadeRester.mandatory_response_fields"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">OptimadeRester.mandatory_response_fields</code></span></a>
      - <a href="#pymatgen.ext.optimade.OptimadeRester.refresh_aliases"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">OptimadeRester.refresh_aliases()</code></span></a>
    - <a href="#pymatgen.ext.optimade.Provider"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Provider</code></span></a>
      - <a href="#pymatgen.ext.optimade.Provider.base_url"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Provider.base_url</code></span></a>
      - <a href="#pymatgen.ext.optimade.Provider.description"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Provider.description</code></span></a>
      - <a href="#pymatgen.ext.optimade.Provider.homepage"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Provider.homepage</code></span></a>
      - <a href="#pymatgen.ext.optimade.Provider.name"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Provider.name</code></span></a>
      - <a href="#pymatgen.ext.optimade.Provider.prefix"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Provider.prefix</code></span></a>

</div>

</div>

</div>

<div class="section wy-nav-content-wrap" toggle="wy-nav-shift">

[pymatgen](index.html)

<div class="wy-nav-content">

<div class="rst-content style-external-links">

<div role="navigation" aria-label="Page navigation">

- <a href="index.html" class="icon icon-home" aria-label="Home"></a>
- pymatgen.ext namespace
- <a
  href="https://github.com/materialsproject/pymatgen/blob/master/docs_rst/pymatgen.ext.rst"
  class="fa fa-github">Edit on GitHub</a>

------------------------------------------------------------------------

</div>

<div class="document" role="main" itemscope="itemscope"
itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="module-pymatgen.ext" class="section">

<span id="pymatgen-ext-namespace"></span>

# pymatgen.ext namespace<a href="#module-pymatgen.ext" class="headerlink"
title="Link to this heading"></a>

<div id="submodules" class="section">

## Submodules<a href="#submodules" class="headerlink"
title="Link to this heading"></a>

</div>

<div id="module-pymatgen.ext.cod" class="section">

<span id="pymatgen-ext-cod-module"></span>

## pymatgen.ext.cod module<a href="#module-pymatgen.ext.cod" class="headerlink"
title="Link to this heading"></a>

This module provides classes to interface with the Crystallography Open
Database. If you use data from the COD, please cite the following works
(as stipulated by the COD developers).

> <div>
>
> Merkys, A., Vaitkus, A., Butkus, J., Okulič-Kazarinas, M., Kairys, V.
> & Gražulis, S. (2016) “COD::CIF::Parser: an error-correcting CIF
> parser for the Perl language”. Journal of Applied Crystallography 49.
>
> Gražulis, S., Merkys, A., Vaitkus, A. & Okulič-Kazarinas, M. (2015)
> “Computing stoichiometric molecular composition from crystal
> structures”. Journal of Applied Crystallography 48, 85-91.
>
> Gražulis, S., Daškevič, A., Merkys, A., Chateigner, D., Lutterotti,
> L., Quirós, M., Serebryanaya, N. R., Moeck, P., Downs, R. T. & LeBail,
> A. (2012) “Crystallography Open Database (COD): an open-access
> collection of crystal structures and platform for world-wide
> collaboration”. Nucleic Acids Research 40, D420-D427.
>
> Grazulis, S., Chateigner, D., Downs, R. T., Yokochi, A. T., Quiros,
> M., Lutterotti, L., Manakova, E., Butkus, J., Moeck, P. & Le Bail, A.
> (2009) “Crystallography Open Database - an open-access collection of
> crystal structures”. J. Appl. Cryst. 42, 726-729.
>
> Downs, R. T. & Hall-Wallace, M. (2003) “The American Mineralogist
> Crystal Structure Database”. American Mineralogist 88, 247-250.
>
> </div>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">COD</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">timeout</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">60</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/cod.py#L42-L140"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.cod.COD" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

An interface to the Crystallography Open Database.

Reference:  
<a href="https://wiki.crystallography.net/RESTful_API/"
class="reference external">https://wiki.crystallography.net/RESTful_API/</a>

Initialize the COD class.

Parameters<span class="colon">:</span>  
**timeout** (*int*) – request timeout in seconds.

<span class="sig-name descname"><span class="pre">get_cod_ids</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">formula</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/cod.py#L59-L76"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.cod.COD.get_cod_ids" class="headerlink"
title="Link to this definition"></a>  
Query the COD for all COD IDs associated with a formula.

Parameters<span class="colon">:</span>  
**formula** (*str*) – The formula to request

<span class="sig-name descname"><span class="pre">get_structure_by_formula</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">formula</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'structure'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cod_id'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'sg'</span></span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/cod.py#L99-L140"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.cod.COD.get_structure_by_formula"
class="headerlink" title="Link to this definition"></a>  
Query the COD for structures by formula.

Parameters<span class="colon">:</span>  
- **formula** (*str*) – Chemical formula.

- **kwargs** – All kwargs supported by Structure.from_str.

Returns<span class="colon">:</span>  
{“structure”: Structure, “cod_id”: int, “sg”: “P n m a”}

Return type<span class="colon">:</span>  
A list of dict of

<span class="sig-name descname"><span class="pre">get_structure_by_id</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">cod_id</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">timeout</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/cod.py#L78-L97"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.cod.COD.get_structure_by_id" class="headerlink"
title="Link to this definition"></a>  
Query the COD for a structure by ID.

Parameters<span class="colon">:</span>  
- **cod_id** (*int*) – COD ID.

- **timeout** (*int*) – DEPRECATED. request timeout in seconds.

- **kwargs** – kwargs passed to Structure.from_str.

Returns<span class="colon">:</span>  
A Structure.

</div>

<div id="module-pymatgen.ext.matproj" class="section">

<span id="pymatgen-ext-matproj-module"></span>

## pymatgen.ext.matproj module<a href="#module-pymatgen.ext.matproj" class="headerlink"
title="Link to this heading"></a>

This module provides classes to interface with the Materials Project
REST API v2 to enable the creation of data structures and pymatgen
objects using Materials Project data.

To make use of the Materials API, you need to be a registered user of
the Materials Project, and obtain an API key by going to your dashboard
at <a href="https://materialsproject.org/dashboard"
class="reference external">https://materialsproject.org/dashboard</a>.

*<span class="k"><span class="pre">exception</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">MPRestError</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/matproj.py#L554-L555"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.matproj.MPRestError" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`Exception`</span>

Exception class for legacy MPRestAdaptor. Raised when query is
malformed.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">MPRester</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">api_key</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">include_user_agent</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/matproj.py#L51-L551"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.matproj.MPRester" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Pymatgen’s implementation of MPRester. Unlike mp-api, this
implementation mirrors the exact MP-API end points without modification.
You just need to refer to
<a href="https://api.materialsproject.org/docs"
class="reference external">https://api.materialsproject.org/docs</a> and
use the field names exactly. No need to deal with strange renames of
various fields. Featurity parity is close to 100% with mp-api.

Furthermore, we support both the mp-api as well as a simplified syntax.
E.g., to query for a summary, you can use
mpr.summary.search(material_ids=”mp-1234”) or
mpr.materials.summary.search(material_ids=”mp-1234”).

If you are a power user that requires some esoteric feature not covered,
feel free to install the mp-api package. All issues regarding that
implementation should be directed to the maintainers of that repository
and not pymatgen. We will support only issues pertaining to our
implementation only.

Attributes: :ivar api_key: API key for authenticating requests to the
Materials Project API. :type api_key: str :ivar preamble: Base endpoint
URL for the Materials Project API. :type preamble: str :ivar session:
HTTP session object for managing API requests. :type session:
requests.Session :ivar materials: Placeholder object for dynamically
adding endpoints related to materials. :type materials: Any

Parameters<span class="colon">:</span>  
- **api_key** (*str*) – A String API key for accessing the
  MaterialsProject REST interface. Please obtain your API key at
  <a href="https://www.materialsproject.org/dashboard"
  class="reference external">https://www.materialsproject.org/dashboard</a>.
  If this is None, the code will check if there is a “PMG_MAPI_KEY”
  setting. If so, it will use that environment variable. This makes
  easier for heavy users to simply add this environment variable to
  their setups and MPRester can then be called without any arguments.

- **include_user_agent** (*bool*) – If True, will include a user agent
  with the HTTP request including information on pymatgen and system
  version making the API request. This helps MP support pymatgen users,
  and is similar to what most web browsers send with each page request.
  Set to False to disable the user agent.

<span class="sig-name descname"><span class="pre">MATERIALS_DOCS</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">('summary',</span> <span class="pre">'core',</span> <span class="pre">'elasticity',</span> <span class="pre">'phonon',</span> <span class="pre">'eos',</span> <span class="pre">'similarity',</span> <span class="pre">'xas',</span> <span class="pre">'grain_boundaries',</span> <span class="pre">'electronic_structure',</span> <span class="pre">'tasks',</span> <span class="pre">'substrates',</span> <span class="pre">'surface_properties',</span> <span class="pre">'robocrys',</span> <span class="pre">'synthesis',</span> <span class="pre">'magnetism',</span> <span class="pre">'insertion_electrodes',</span> <span class="pre">'conversion_electrodes',</span> <span class="pre">'oxidation_states',</span> <span class="pre">'provenance',</span> <span class="pre">'alloys',</span> <span class="pre">'absorption',</span> <span class="pre">'chemenv',</span> <span class="pre">'bonds',</span> <span class="pre">'piezoelectric',</span> <span class="pre">'dielectric')</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/ext/matproj.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.matproj.MPRester.MATERIALS_DOCS"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">get_doc</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">material_id</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">fields</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/matproj.py#L260-L271"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.matproj.MPRester.get_doc" class="headerlink"
title="Link to this definition"></a>  
Get a data corresponding to a material_id.

Parameters<span class="colon">:</span>  
- **material_id** (*str*) – Materials Project ID (e.g. mp-1234).

- **fields** (*list*) – Fields to query for. If None (the default), all
  fields are returned.

Returns<span class="colon">:</span>  
Dict

<span class="sig-name descname"><span class="pre">get_entries</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">criteria</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="keyword-only-separator o"><span class="pre">\*</span></span>*, *<span class="n"><span class="pre">compatible_only</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">property_data</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">summary_data</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/matproj.py#L347-L440"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.matproj.MPRester.get_entries" class="headerlink"
title="Link to this definition"></a>  
Get a list of ComputedEntries or ComputedStructureEntries corresponding
to a chemical system, formula, or materials_id or full criteria.

Parameters<span class="colon">:</span>  
- **criteria** – Chemsys, formula, or mp-id.

- **compatible_only** (*bool*) – Whether to return only “compatible”
  entries. Compatible entries are entries that have been processed using
  the MaterialsProject2020Compatibility class, which performs
  adjustments to allow mixing of GGA and GGA+U calculations for more
  accurate phase diagrams and reaction energies.

- **property_data** (*list*) – Specify additional properties to include
  in entry.data from /materials/thermo endpoint of the API.

- **summary_data** (*list*) – Specify additional properties to include
  in entry.data from /materials/summary endpoint of the API. Note that
  unlike property_data, summary_data refers to the “best” calculation
  done by MP. There are no guarantees that the summary_data will be
  consistent with the entry or property data since the data can come
  from say a r2SCAN calculation but the entry is from a GGA calculation.
  The data will be reported in the entry.data\[“summary”\] dictionary.

- **\*\*kwargs** – Used to catch deprecated kwargs.

Returns<span class="colon">:</span>  
List of ComputedStructureEntry objects.

<span class="sig-name descname"><span class="pre">get_entries_in_chemsys</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">elements</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="o"><span class="pre">\*</span></span><span class="n"><span class="pre">args</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/matproj.py#L456-L479"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.matproj.MPRester.get_entries_in_chemsys"
class="headerlink" title="Link to this definition"></a>  
Helper method to get a list of ComputedEntries in a chemical system. For
example, elements = \[“Li”, “Fe”, “O”\] will return a list of all
entries in the Li-Fe-O chemical system, i.e., all LixOy, FexOy, LixFey,
LixFeyOz, Li, Fe and O phases. Extremely useful for creating phase
diagrams of entire chemical systems.

Parameters<span class="colon">:</span>  
- **elements** (*str* *\|* *list\[str\]*) – Chemical system string
  comprising element symbols separated by dashes, e.g. “Li-Fe-O” or List
  of element symbols, e.g. \[“Li”, “Fe”, “O”\].

- **\*args** – Pass-through to get_entries.

- **\*\*kwargs** – Pass-through to get_entries.

Returns<span class="colon">:</span>  
List of ComputedEntries.

<span class="sig-name descname"><span class="pre">get_entry_by_material_id</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">material_id</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="o"><span class="pre">\*</span></span><span class="n"><span class="pre">args</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a
href="pymatgen.entries.html#pymatgen.entries.computed_entries.ComputedStructureEntry"
class="reference internal"
title="pymatgen.entries.computed_entries.ComputedStructureEntry"><span
class="pre">ComputedStructureEntry</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/matproj.py#L442-L454"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.matproj.MPRester.get_entry_by_material_id"
class="headerlink" title="Link to this definition"></a>  
Get a ComputedEntry corresponding to a material_id.

Parameters<span class="colon">:</span>  
- **material_id** (*str*) – Materials Project material_id (a string,
  e.g. mp-1234).

- **\*args** – Pass-through to get_entries.

- **\*\*kwargs** – Pass-through to get_entries.

Returns<span class="colon">:</span>  
ComputedStructureEntry object.

<span class="sig-name descname"><span class="pre">get_initial_structures_by_material_id</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">material_id</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">conventional_unit_cell</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/matproj.py#L326-L345"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.ext.matproj.MPRester.get_initial_structures_by_material_id"
class="headerlink" title="Link to this definition"></a>  
Get a Structure corresponding to a material_id.

Parameters<span class="colon">:</span>  
- **material_id** (*str*) – Materials Project ID (e.g. mp-1234).

- **final** (*bool*) – Whether to get the final structure, or the
  initial (pre-relaxation) structures. Defaults to True.

- **conventional_unit_cell** (*bool*) – Whether to get the standard
  conventional unit cell

Returns<span class="colon">:</span>  
Structure object.

<span class="sig-name descname"><span class="pre">get_material_ids</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">formula</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/matproj.py#L275-L284"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.matproj.MPRester.get_material_ids"
class="headerlink" title="Link to this definition"></a>  
Get all materials ids for a formula.

Parameters<span class="colon">:</span>  
**formula** (*str*) – A formula (e.g., Fe2O3).

Returns<span class="colon">:</span>  
all materials ids.

Return type<span class="colon">:</span>  
list\[str\]

<span class="sig-name descname"><span class="pre">get_materials_ids</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">formula</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/matproj.py#L275-L284"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.matproj.MPRester.get_materials_ids"
class="headerlink" title="Link to this definition"></a>  
Get all materials ids for a formula.

Parameters<span class="colon">:</span>  
**formula** (*str*) – A formula (e.g., Fe2O3).

Returns<span class="colon">:</span>  
all materials ids.

Return type<span class="colon">:</span>  
list\[str\]

<span class="sig-name descname"><span class="pre">get_phonon_bandstructure_by_material_id</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">material_id</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a
href="pymatgen.phonon.html#pymatgen.phonon.bandstructure.PhononBandStructureSymmLine"
class="reference internal"
title="pymatgen.phonon.bandstructure.PhononBandStructureSymmLine"><span
class="pre">PhononBandStructureSymmLine</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/matproj.py#L508-L534"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.ext.matproj.MPRester.get_phonon_bandstructure_by_material_id"
class="headerlink" title="Link to this definition"></a>  
Get phonon bandstructure by material_id.

Note that this method borrows constructor methods built into in the
emmet-core model for this data. Calling the to_pmg method of the
emmet-core data model handles this.

Parameters<span class="colon">:</span>  
**material_id** (*str*) – Materials Project material_id

Returns<span class="colon">:</span>  
A phonon band structure.

Return type<span class="colon">:</span>  
<a
href="pymatgen.phonon.html#pymatgen.phonon.bandstructure.PhononBandStructureSymmLine"
class="reference internal"
title="pymatgen.phonon.bandstructure.PhononBandStructureSymmLine">PhononBandStructureSymmLine</a>

<span class="sig-name descname"><span class="pre">get_phonon_dos_by_material_id</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">material_id</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="pymatgen.phonon.html#pymatgen.phonon.dos.CompletePhononDos"
class="reference internal"
title="pymatgen.phonon.dos.CompletePhononDos"><span
class="pre">CompletePhononDos</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/matproj.py#L536-L551"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.matproj.MPRester.get_phonon_dos_by_material_id"
class="headerlink" title="Link to this definition"></a>  
Get phonon density of states by material_id.

Note that this method borrows constructor methods built into in the
emmet-core model for this data. Calling the to_pmg method of the
emmet-core data model handles this.

Parameters<span class="colon">:</span>  
**material_id** (*str*) – Materials Project material_id

Returns<span class="colon">:</span>  
A phonon DOS object.

Return type<span class="colon">:</span>  
<a href="pymatgen.phonon.html#pymatgen.phonon.dos.CompletePhononDos"
class="reference internal"
title="pymatgen.phonon.dos.CompletePhononDos">CompletePhononDos</a>

<span class="sig-name descname"><span class="pre">get_structure_by_material_id</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">material_id</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">conventional_unit_cell</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/matproj.py#L307-L324"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.matproj.MPRester.get_structure_by_material_id"
class="headerlink" title="Link to this definition"></a>  
Get a Structure corresponding to a material_id.

Parameters<span class="colon">:</span>  
- **material_id** (*str*) – Materials Project ID (e.g. mp-1234).

- **final** (*bool*) – Whether to get the final structure, or the
  initial (pre-relaxation) structures. Defaults to True.

- **conventional_unit_cell** (*bool*) – Whether to get the standard
  conventional unit cell

Returns<span class="colon">:</span>  
Structure object.

<span class="sig-name descname"><span class="pre">get_structures</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">chemsys_formula</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">final</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/matproj.py#L289-L305"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.matproj.MPRester.get_structures"
class="headerlink" title="Link to this definition"></a>  
Get a list of Structures corresponding to a chemical system or formula.

Parameters<span class="colon">:</span>  
- **chemsys_formula** (*str*) – A chemical system, list of chemical
  systems (e.g., Li-Fe-O, Si-*), or single formula (e.g., Fe2O3, Si*).

- **final** (*bool*) – Whether to get the final structure, or the list
  of initial (pre-relaxation) structures. Defaults to True.

Returns<span class="colon">:</span>  
List of Structure objects. (\[Structure\])

<span class="sig-name descname"><span class="pre">get_summary</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">criteria</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*, *<span class="n"><span class="pre">fields</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/matproj.py#L247-L258"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.matproj.MPRester.get_summary" class="headerlink"
title="Link to this definition"></a>  
Get a data corresponding to a criteria.

Parameters<span class="colon">:</span>  
- **criteria** (*dict*) – Materials Project ID (e.g. mp-1234), e.g.
  {“formula”: “Fe2O3,FeO”}

- **fields** (*list*) – Fields to query for. If None (the default), all
  fields are returned.

Returns<span class="colon">:</span>  
List of dict of summary docs.

<span class="sig-name descname"><span class="pre">get_summary_by_material_id</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">material_id</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">fields</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/matproj.py#L260-L271"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.matproj.MPRester.get_summary_by_material_id"
class="headerlink" title="Link to this definition"></a>  
Get a data corresponding to a material_id.

Parameters<span class="colon">:</span>  
- **material_id** (*str*) – Materials Project ID (e.g. mp-1234).

- **fields** (*list*) – Fields to query for. If None (the default), all
  fields are returned.

Returns<span class="colon">:</span>  
Dict

<span class="sig-name descname"><span class="pre">request</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">sub_url</span></span>*, *<span class="n"><span class="pre">payload</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">method</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'GET'</span></span>*, *<span class="n"><span class="pre">mp_decode</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/matproj.py#L166-L192"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.matproj.MPRester.request" class="headerlink"
title="Link to this definition"></a>  
Helper method to make the requests and perform decoding based on
MSONable protocol.

<span class="sig-name descname"><span class="pre">search</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">doc</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/matproj.py#L194-L224"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.matproj.MPRester.search" class="headerlink"
title="Link to this definition"></a>  
Queries a Materials PI end point doc. A notable difference with the
mp-api’s implementation is that this uses the web API to do searches. So
the keywords follow the actual API spec, which is as it should be. For
instance, number of sites is nsites and number of elements is nelements.
The mp-api package has this weird renaming that maps num_elements to
nelements and num_sites to nsites.

Parameters: - [<span id="id2"
class="problematic">\*\*</span>](#id1)kwargs: keyword arguments for
filtering materials. Fields that do not start with underscores are
filters, while those that start with underscores are fields to retrieve.
Possible filters include:

> <div>
>
> - \_fields (optional): list of fields to retrieve for each material
>
> - Other parameters: filter criteria, where each parameter key
>   corresponds to the field to filter and the parameter value
>   corresponds to the filter value
>
> </div>

Returns: - list of dictionaries, each dictionary representing a material
retrieved based on the filtering criteria

<span class="sig-name descname"><span class="pre">summary_search</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/matproj.py#L226-L245"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.matproj.MPRester.summary_search"
class="headerlink" title="Link to this definition"></a>  
Mirrors mp-api’s mpr.materials.summary.search functionality. Searches
for materials based on the specified criteria. A notable difference with
the mp-api’s implementation is that this uses the web API to do
searches. So the keywords follow the actual API spec, which is as it
should be. For instance, number of sites is nsites and number of
elements is nelements. The mp-api package has this weird renaming that
maps num_elements to nelements and num_sites to nsites.

Parameters: - [<span id="id4"
class="problematic">\*\*</span>](#id3)kwargs: keyword arguments for
filtering materials. Fields that do not start with underscores are
filters, while those that start with underscores are fields to retrieve.
Possible filters include:

> <div>
>
> - \_fields (optional): list of fields to retrieve for each material
>
> - Other parameters: filter criteria, where each parameter key
>   corresponds to the field to filter and the parameter value
>   corresponds to the filter value
>
> </div>

Returns: - list of dictionaries, each dictionary representing a material
retrieved based on the filtering criteria

</div>

<div id="module-pymatgen.ext.optimade" class="section">

<span id="pymatgen-ext-optimade-module"></span>

## pymatgen.ext.optimade module<a href="#module-pymatgen.ext.optimade" class="headerlink"
title="Link to this heading"></a>

Optimade support.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">OptimadeRester</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">aliases_or_resource_urls</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">refresh_aliases</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">timeout</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">5</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/optimade.py#L40-L622"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.optimade.OptimadeRester" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Call OPTIMADE-compliant APIs, see <a href="https://optimade.org"
class="reference external">https://optimade.org</a> and \[1\].

This class is ready to use but considered in-development and subject to
change.

Please also consider using the client in “OPTIMADE Python tools”:

<a
href="https://www.optimade.org/optimade-python-tools/latest/getting_started/client/"
class="reference external">https://www.optimade.org/optimade-python-tools/latest/getting_started/client/</a>

The “OPTIMADE Python tools” client is less integrated with pymatgen, but
more actively developed for the latest OPTIMADE features.

\[1\] Andersen, C.W., *et al*.  
OPTIMADE, an API for exchanging materials data. Sci Data 8, 217 (2021).
<a href="https://doi.org/10.1038/s41597-021-00974-z"
class="reference external">https://doi.org/10.1038/s41597-021-00974-z</a>

OPTIMADE is an effort to provide a standardized interface to retrieve
information from many different materials science databases.

This is a client to retrieve structures from OPTIMADE v1 compliant
endpoints. It does not yet support all features of the OPTIMADE v1
specification but is intended as a way to quickly search an endpoint in
a way familiar to users of pymatgen without needing to know the full
OPTIMADE specification.

For advanced usage, please see the OPTIMADE documentation at
optimade.org and consider calling the APIs directly.

For convenience, known OPTIMADE endpoints have been given aliases in
pymatgen to save typing the full URL.

To get an up-to-date list aliases, generated from the current list of
OPTIMADE providers at optimade.org, call the refresh_aliases() method or
pass refresh_aliases=True when creating instances of this class.

Parameters<span class="colon">:</span>  
- **aliases_or_resource_urls** – the alias or structure resource URL or
  a list of

- **URLs** (*aliases* *or* *resource*)

- **not** (*if providing the resource URL directly it should*)

- **index** (*be an*)

- **"v1/structures"** (*this interface can only currently access the*)

- **URL** (*information from the specified resource*)

- **refresh_aliases** – if True, use an up-to-date list of
  providers/aliases from the live

- **https** (*list* *of* *OPTIMADE providers hosted at*) –
  //providers.optimade.org.

- **timeout** – number of seconds before an attempted request is
  abandoned, a good

- **providers** (*timeout is useful when querying many*)

- **offline** (*some* *of* *which may be*)

<span class="sig-name descname"><span class="pre">aliases</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ClassVar</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">{'aflow':</span> <span class="pre">'https://aflow.org/API/optimade/',</span> <span class="pre">'alexandria':</span> <span class="pre">'https://alexandria.icams.rub.de/pbe',</span> <span class="pre">'alexandria.pbe':</span> <span class="pre">'https://alexandria.icams.rub.de/pbe',</span> <span class="pre">'alexandria.pbesol':</span> <span class="pre">'https://alexandria.icams.rub.de/pbesol',</span> <span class="pre">'cmr':</span> <span class="pre">'https://cmr-optimade.fysik.dtu.dk',</span> <span class="pre">'cod':</span> <span class="pre">'https://www.crystallography.net/cod/optimade',</span> <span class="pre">'jarvis':</span> <span class="pre">'https://jarvis.nist.gov/optimade/jarvisdft',</span> <span class="pre">'mcloud.2dtopo':</span> <span class="pre">'https://aiida.materialscloud.org/2dtopo/optimade',</span> <span class="pre">'mcloud.curated-cofs':</span> <span class="pre">'https://aiida.materialscloud.org/curated-cofs/optimade',</span> <span class="pre">'mcloud.mc2d':</span> <span class="pre">'https://aiida.materialscloud.org/mc2d/optimade',</span> <span class="pre">'mcloud.mc3d':</span> <span class="pre">'https://aiida.materialscloud.org/mc3d/optimade',</span> <span class="pre">'mcloud.optimade-sample':</span> <span class="pre">'https://aiida.materialscloud.org/optimade-sample/optimade',</span> <span class="pre">'mcloud.pyrene-mofs':</span> <span class="pre">'https://aiida.materialscloud.org/pyrene-mofs/optimade',</span> <span class="pre">'mcloud.scdm':</span> <span class="pre">'https://aiida.materialscloud.org/autowannier/optimade',</span> <span class="pre">'mcloud.stoceriaitf':</span> <span class="pre">'https://aiida.materialscloud.org/stoceriaitf/optimade',</span> <span class="pre">'mcloud.tc-applicability':</span> <span class="pre">'https://aiida.materialscloud.org/tc-applicability/optimade',</span> <span class="pre">'mcloud.tin-antimony-sulfoiodide':</span> <span class="pre">'https://aiida.materialscloud.org/tin-antimony-sulfoiodide/optimade',</span> <span class="pre">'mp':</span> <span class="pre">'https://optimade.materialsproject.org',</span> <span class="pre">'mpdd':</span> <span class="pre">'http://mpddoptimade.phaseslab.org',</span> <span class="pre">'mpds':</span> <span class="pre">'https://api.mpds.io',</span> <span class="pre">'nmd':</span> <span class="pre">'https://nomad-lab.eu/prod/rae/optimade/',</span> <span class="pre">'odbx':</span> <span class="pre">'https://optimade.odbx.science',</span> <span class="pre">'odbx.gnome':</span> <span class="pre">'https://optimade-gnome.odbx.science',</span> <span class="pre">'odbx.odbx_misc':</span> <span class="pre">'https://optimade-misc.odbx.science',</span> <span class="pre">'omdb.omdb_production':</span> <span class="pre">'https://optimade.openmaterialsdb.se',</span> <span class="pre">'oqmd':</span> <span class="pre">'https://oqmd.org/optimade/',</span> <span class="pre">'tcod':</span> <span class="pre">'https://www.crystallography.net/tcod/optimade',</span> <span class="pre">'twodmatpedia':</span> <span class="pre">'http://optimade.2dmatpedia.org'}</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/ext/optimade.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.optimade.OptimadeRester.aliases"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">describe</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/optimade.py#L187-L190"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.optimade.OptimadeRester.describe"
class="headerlink" title="Link to this definition"></a>  
Human-readable information about the resources being searched by the
OptimadeRester.

<span class="sig-name descname"><span class="pre">get_snls</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">elements</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">nelements</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">nsites</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">chemical_formula_anonymous</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">chemical_formula_hill</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">additional_response_fields</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">set</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><a href="pymatgen.util.html#pymatgen.util.provenance.StructureNL"
class="reference internal"
title="pymatgen.util.provenance.StructureNL"><span
class="pre">StructureNL</span></a><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/optimade.py#L269-L310"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.optimade.OptimadeRester.get_snls"
class="headerlink" title="Link to this definition"></a>  
Retrieve StructureNL from OPTIMADE providers.

A StructureNL is an object provided by pymatgen which combines Structure
with associated metadata, such as the URL is was downloaded from and any
additional namespaced data.

Not all functionality of OPTIMADE is currently exposed in this
convenience method. To use a custom filter, call
get_structures_with_filter().

Parameters<span class="colon">:</span>  
- **elements** – List of elements

- **nelements** – Number of elements, e.g. 4 or \[2, 5\] for the range
  \>=2 and \<=5

- **nsites** – Number of sites, e.g. 4 or \[2, 5\] for the range \>=2
  and \<=5

- **chemical_formula_anonymous** – The desired chemical formula in
  OPTIMADE anonymous formula format

- **format** (*this is different from the pymatgen*)

- **"A2BC").** (*e.g. pymatgen "ABC2" should become*)

- **chemical_formula_hill** – The desired chemical formula in the
  OPTIMADE take on the Hill formula format.

- **Again** (*(NB.*)

- **format**

- **chemical** (*as the OPTIMADE version is a reduced*)

- **ordering.)** (*formula simply using the IUPAC/Hill*)

- **additional_response_fields** – Any additional fields desired from
  the OPTIMADE API,

- **dictionary.** (*these will be stored under the '\_optimade' key in
  each StructureNL.data*)

Returns<span class="colon">:</span>  
keyed by that database provider’s id system

Return type<span class="colon">:</span>  
dict\[str,
<a href="pymatgen.util.html#pymatgen.util.provenance.StructureNL"
class="reference internal"
title="pymatgen.util.provenance.StructureNL">StructureNL</a>\]

<span class="sig-name descname"><span class="pre">get_snls_with_filter</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">optimade_filter</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">additional_response_fields</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">set</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><a href="pymatgen.util.html#pymatgen.util.provenance.StructureNL"
class="reference internal"
title="pymatgen.util.provenance.StructureNL"><span
class="pre">StructureNL</span></a><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/optimade.py#L329-L378"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.optimade.OptimadeRester.get_snls_with_filter"
class="headerlink" title="Link to this definition"></a>  
Get structures satisfying a given OPTIMADE filter.

Parameters<span class="colon">:</span>  
- **optimade_filter** – An OPTIMADE-compliant filter

- **additional_response_fields** – Any additional fields desired from
  the OPTIMADE API,

Returns<span class="colon">:</span>  
keyed by that database provider’s id system

Return type<span class="colon">:</span>  
dict\[str,
<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure">Structure</a>\]

<span class="sig-name descname"><span class="pre">get_structures</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">elements</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">nelements</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">nsites</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">chemical_formula_anonymous</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">chemical_formula_hill</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/optimade.py#L233-L267"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.optimade.OptimadeRester.get_structures"
class="headerlink" title="Link to this definition"></a>  
Retrieve Structures from OPTIMADE providers.

Not all functionality of OPTIMADE is currently exposed in this
convenience method. To use a custom filter, call
get_structures_with_filter().

Parameters<span class="colon">:</span>  
- **elements** – List of elements

- **nelements** – Number of elements, e.g. 4 or \[2, 5\] for the range
  \>=2 and \<=5

- **nsites** – Number of sites, e.g. 4 or \[2, 5\] for the range \>=2
  and \<=5

- **chemical_formula_anonymous** – The desired chemical formula in
  OPTIMADE anonymous formula format

- **format** (*this is different from the pymatgen*)

- **"A2BC").** (*e.g. pymatgen "ABC2" should become*)

- **chemical_formula_hill** – The desired chemical formula in the
  OPTIMADE take on the Hill formula format.

- **Again** (*(NB.*)

- **format**

- **chemical** (*as the OPTIMADE version is a reduced*)

- **ordering.)** (*formula simply using the IUPAC/Hill*)

Returns<span class="colon">:</span>  
keyed by that database provider’s id system

Return type<span class="colon">:</span>  
dict\[str,
<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure">Structure</a>\]

<span class="sig-name descname"><span class="pre">get_structures_with_filter</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">optimade_filter</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/optimade.py#L312-L327"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.ext.optimade.OptimadeRester.get_structures_with_filter"
class="headerlink" title="Link to this definition"></a>  
Get structures satisfying a given OPTIMADE filter.

Parameters<span class="colon">:</span>  
**optimade_filter** – An OPTIMADE-compliant filter

Returns<span class="colon">:</span>  
keyed by that database provider’s id system

Return type<span class="colon">:</span>  
dict\[str,
<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure">Structure</a>\]

<span class="sig-name descname"><span class="pre">mandatory_response_fields</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">('lattice_vectors',</span> <span class="pre">'cartesian_site_positions',</span> <span class="pre">'species',</span> <span class="pre">'species_at_sites')</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/ext/optimade.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.ext.optimade.OptimadeRester.mandatory_response_fields"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">refresh_aliases</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">providers_url</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'https://providers.optimade.org/providers.json'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/optimade.py#L595-L613"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.optimade.OptimadeRester.refresh_aliases"
class="headerlink" title="Link to this definition"></a>  
Update available OPTIMADE structure resources based on the current list
of OPTIMADE providers.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Provider</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">base_url</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">description</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">homepage</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">prefix</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../ext/optimade.py#L30-L37"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.optimade.Provider" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`NamedTuple`</span>

TODO: Import optimade-python-tool’s data structures will make more
sense.

Create new instance of Provider(name, base_url, description, homepage,
prefix)

<span class="sig-name descname"><span class="pre">base_url</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/ext/optimade.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.optimade.Provider.base_url" class="headerlink"
title="Link to this definition"></a>  
Alias for field number 1

<span class="sig-name descname"><span class="pre">description</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/ext/optimade.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.optimade.Provider.description" class="headerlink"
title="Link to this definition"></a>  
Alias for field number 2

<span class="sig-name descname"><span class="pre">homepage</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/ext/optimade.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.optimade.Provider.homepage" class="headerlink"
title="Link to this definition"></a>  
Alias for field number 3

<span class="sig-name descname"><span class="pre">name</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/ext/optimade.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.optimade.Provider.name" class="headerlink"
title="Link to this definition"></a>  
Alias for field number 0

<span class="sig-name descname"><span class="pre">prefix</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/ext/optimade.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.ext.optimade.Provider.prefix" class="headerlink"
title="Link to this definition"></a>  
Alias for field number 4

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
