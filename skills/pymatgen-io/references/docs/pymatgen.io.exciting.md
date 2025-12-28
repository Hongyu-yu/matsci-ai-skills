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

- <a href="#" class="reference internal">pymatgen.io.exciting package</a>
  - <a href="#submodules" class="reference internal">Submodules</a>
  - <a href="#module-pymatgen.io.exciting.inputs"
    class="reference internal">pymatgen.io.exciting.inputs module</a>
    - <a href="#pymatgen.io.exciting.inputs.ExcitingInput"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">ExcitingInput</code></span></a>
      - <a href="#pymatgen.io.exciting.inputs.ExcitingInput.structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ExcitingInput.structure</code></span></a>
      - <a href="#pymatgen.io.exciting.inputs.ExcitingInput.title"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ExcitingInput.title</code></span></a>
      - <a href="#pymatgen.io.exciting.inputs.ExcitingInput.lockxyz"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ExcitingInput.lockxyz</code></span></a>
      - <a href="#pymatgen.io.exciting.inputs.ExcitingInput.bohr2ang"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ExcitingInput.bohr2ang</code></span></a>
      - <a href="#pymatgen.io.exciting.inputs.ExcitingInput.from_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ExcitingInput.from_file()</code></span></a>
      - <a href="#pymatgen.io.exciting.inputs.ExcitingInput.from_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ExcitingInput.from_str()</code></span></a>
      - <a href="#id0" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ExcitingInput.lockxyz</code></span></a>
      - <a href="#pymatgen.io.exciting.inputs.ExcitingInput.write_etree"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ExcitingInput.write_etree()</code></span></a>
      - <a href="#pymatgen.io.exciting.inputs.ExcitingInput.write_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ExcitingInput.write_file()</code></span></a>
      - <a href="#pymatgen.io.exciting.inputs.ExcitingInput.write_string"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ExcitingInput.write_string()</code></span></a>

</div>

</div>

</div>

<div class="section wy-nav-content-wrap" toggle="wy-nav-shift">

[pymatgen](index.html)

<div class="wy-nav-content">

<div class="rst-content style-external-links">

<div role="navigation" aria-label="Page navigation">

- <a href="index.html" class="icon icon-home" aria-label="Home"></a>
- pymatgen.io.exciting package
- <a
  href="https://github.com/materialsproject/pymatgen/blob/master/docs_rst/pymatgen.io.exciting.rst"
  class="fa fa-github">Edit on GitHub</a>

------------------------------------------------------------------------

</div>

<div class="document" role="main" itemscope="itemscope"
itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="module-pymatgen.io.exciting" class="section">

<span id="pymatgen-io-exciting-package"></span>

# pymatgen.io.exciting package<a href="#module-pymatgen.io.exciting" class="headerlink"
title="Link to this heading"></a>

This package contains classes to parse input files from the exciting
code package.

<div id="submodules" class="section">

## Submodules<a href="#submodules" class="headerlink"
title="Link to this heading"></a>

</div>

<div id="module-pymatgen.io.exciting.inputs" class="section">

<span id="pymatgen-io-exciting-inputs-module"></span>

## pymatgen.io.exciting.inputs module<a href="#module-pymatgen.io.exciting.inputs" class="headerlink"
title="Link to this heading"></a>

Classes for reading/manipulating/writing exciting input files.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ExcitingInput</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.IStructure"
class="reference internal"
title="pymatgen.core.structure.IStructure"><span
class="pre">IStructure</span></a></span>*, *<span class="n"><span class="pre">title</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">lockxyz</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/exciting/inputs.py#L37-L419"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.exciting.inputs.ExcitingInput" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Object for representing the data stored in the structure part of the
exciting input.

<span class="sig-name descname"><span class="pre">structure</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/exciting/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.exciting.inputs.ExcitingInput.structure"
class="headerlink" title="Link to this definition"></a>  
Associated Structure.

Type<span class="colon">:</span>  
<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure">Structure</a>

<span class="sig-name descname"><span class="pre">title</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/exciting/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.exciting.inputs.ExcitingInput.title"
class="headerlink" title="Link to this definition"></a>  
Optional title string.

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">lockxyz</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/exciting/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.exciting.inputs.ExcitingInput.lockxyz"
class="headerlink" title="Link to this definition"></a>  
Lockxyz attribute for each site if available.

Type<span class="colon">:</span>  
Nx3 NDArray of booleans

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  Structure object.

- **title** (*str*) – Optional title for exciting input. Defaults to
  unit cell formula of structure. Defaults to None.

- **lockxyz** (*Nx3 array*) – bool values for selective dynamics, where
  N is number of sites. Defaults to None.

<span class="sig-name descname"><span class="pre">bohr2ang</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ClassVar</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">0.5291692994629731</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/exciting/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.exciting.inputs.ExcitingInput.bohr2ang"
class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/exciting/inputs.py#L176-L187"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.exciting.inputs.ExcitingInput.from_file"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
**filename** – Filename.

Returns<span class="colon">:</span>  
ExcitingInput

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">data</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/exciting/inputs.py#L83-L174"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.exciting.inputs.ExcitingInput.from_str"
class="headerlink" title="Link to this definition"></a>  
Reads the exciting input from a string.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">lockxyz</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">NDArray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/exciting/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id0" class="headerlink" title="Link to this definition"></a>  
Selective dynamics site properties.

<span class="sig-name descname"><span class="pre">write_etree</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">celltype</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'unchanged'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'conventional'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'primitive'</span></span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">cartesian</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">bandstr</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">symprec</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.4</span></span>*, *<span class="n"><span class="pre">angle_tolerance</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">5</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">ET.Element</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/exciting/inputs.py#L189-L301"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.exciting.inputs.ExcitingInput.write_etree"
class="headerlink" title="Link to this definition"></a>  
Convert the exciting input parameters to an XML Element object.

Parameters<span class="colon">:</span>  
- **celltype** (*str*) – Choice of unit cell. Can be either the unit
  cell from self.structure (“unchanged”), the conventional cell
  (“conventional”), or the primitive unit cell (“primitive”).

- **cartesian** (*bool*) – Whether the atomic positions are provided in
  Cartesian or unit-cell coordinates. Default is False.

- **bandstr** (*bool*) – Whether the bandstructure path along the
  HighSymmKpath is included in the input file. Only supported if the
  celltype is set to “primitive”. Default is False.

- **symprec** (*float*) – Tolerance for the symmetry finding. Default is
  0.4.

- **angle_tolerance** (*float*) – Angle tolerance for the symmetry
  finding. Default is 5.

- **\*\*kwargs** – Additional parameters for the input file.

Returns<span class="colon">:</span>  
ET.Element containing the input XML structure

<span class="sig-name descname"><span class="pre">write_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">celltype</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'unchanged'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'conventional'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'primitive'</span></span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*, *<span class="n"><span class="pre">cartesian</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">bandstr</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">symprec</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.4</span></span>*, *<span class="n"><span class="pre">angle_tolerance</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">5</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/exciting/inputs.py#L342-L375"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.exciting.inputs.ExcitingInput.write_file"
class="headerlink" title="Link to this definition"></a>  
Write exciting input file.

Parameters<span class="colon">:</span>  
- **celltype** (*str*) – Choice of unit cell. Can be either the unit
  cell from self.structure (“unchanged”), the conventional cell
  (“conventional”), or the primitive unit cell (“primitive”).

- **filename** (*PathLike*) – Filename for exciting input.

- **cartesian** (*bool*) – Whether the atomic positions are provided in
  Cartesian or unit-cell coordinates. Default is False.

- **bandstr** (*bool*) – Whether the bandstructure path along the
  HighSymmKpath is included in the input file. Only supported if the
  celltype is set to “primitive”. Default is False.

- **symprec** (*float*) – Tolerance for the symmetry finding. Default is
  0.4.

- **angle_tolerance** (*float*) – Angle tolerance for the symmetry
  finding. Default is 5.

- **\*\*kwargs** – Additional parameters for the input file.

<span class="sig-name descname"><span class="pre">write_string</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">celltype</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'unchanged'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'conventional'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'primitive'</span></span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">cartesian</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">bandstr</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">symprec</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.4</span></span>*, *<span class="n"><span class="pre">angle_tolerance</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">5</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/exciting/inputs.py#L303-L340"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.exciting.inputs.ExcitingInput.write_string"
class="headerlink" title="Link to this definition"></a>  
Convert exciting input to a string.

Parameters<span class="colon">:</span>  
- **celltype** (*str*) – Choice of unit cell. Can be either the unit
  cell from self.structure (“unchanged”), the conventional cell
  (“conventional”), or the primitive unit cell (“primitive”).

- **cartesian** (*bool*) – Whether the atomic positions are provided in
  Cartesian or unit-cell coordinates. Default is False.

- **bandstr** (*bool*) – Whether the bandstructure path along the
  HighSymmKpath is included in the input file. Only supported if the
  celltype is set to “primitive”. Default is False.

- **symprec** (*float*) – Tolerance for the symmetry finding. Default is
  0.4.

- **angle_tolerance** (*float*) – Angle tolerance for the symmetry
  finding. Default is 5.

- **\*\*kwargs** – Additional parameters for the input file.

Returns<span class="colon">:</span>  
str

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
