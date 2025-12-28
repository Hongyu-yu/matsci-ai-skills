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

- <a href="#" class="reference internal">pymatgen.io.feff package</a>
  - <a href="#submodules" class="reference internal">Submodules</a>
  - <a href="#module-pymatgen.io.feff.inputs"
    class="reference internal">pymatgen.io.feff.inputs module</a>
    - <a href="#pymatgen.io.feff.inputs.Atoms"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Atoms</code></span></a>
      - <a href="#pymatgen.io.feff.inputs.Atoms.atoms_string_from_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Atoms.atoms_string_from_file()</code></span></a>
      - <a href="#pymatgen.io.feff.inputs.Atoms.cluster"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Atoms.cluster</code></span></a>
      - <a href="#pymatgen.io.feff.inputs.Atoms.cluster_from_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Atoms.cluster_from_file()</code></span></a>
      - <a href="#pymatgen.io.feff.inputs.Atoms.get_lines"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Atoms.get_lines()</code></span></a>
      - <a href="#pymatgen.io.feff.inputs.Atoms.write_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Atoms.write_file()</code></span></a>
    - <a href="#pymatgen.io.feff.inputs.FeffParseError"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">FeffParseError</code></span></a>
    - <a href="#pymatgen.io.feff.inputs.Header"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Header</code></span></a>
      - <a href="#pymatgen.io.feff.inputs.Header.formula"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Header.formula</code></span></a>
      - <a href="#pymatgen.io.feff.inputs.Header.from_cif_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Header.from_cif_file()</code></span></a>
      - <a href="#pymatgen.io.feff.inputs.Header.from_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Header.from_file()</code></span></a>
      - <a href="#pymatgen.io.feff.inputs.Header.from_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Header.from_str()</code></span></a>
      - <a href="#pymatgen.io.feff.inputs.Header.header_string_from_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Header.header_string_from_file()</code></span></a>
      - <a href="#pymatgen.io.feff.inputs.Header.structure_symmetry"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Header.structure_symmetry</code></span></a>
      - <a href="#pymatgen.io.feff.inputs.Header.write_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Header.write_file()</code></span></a>
    - <a href="#pymatgen.io.feff.inputs.Paths"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Paths</code></span></a>
      - <a href="#pymatgen.io.feff.inputs.Paths.write_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Paths.write_file()</code></span></a>
    - <a href="#pymatgen.io.feff.inputs.Potential"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Potential</code></span></a>
      - <a href="#pymatgen.io.feff.inputs.Potential.pot_dict_from_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Potential.pot_dict_from_str()</code></span></a>
      - <a href="#pymatgen.io.feff.inputs.Potential.pot_string_from_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Potential.pot_string_from_file()</code></span></a>
      - <a href="#pymatgen.io.feff.inputs.Potential.write_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Potential.write_file()</code></span></a>
    - <a href="#pymatgen.io.feff.inputs.Tags" class="reference internal"><span
      class="pre"><code
      class="docutils literal notranslate">Tags</code></span></a>
      - <a href="#pymatgen.io.feff.inputs.Tags.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Tags.as_dict()</code></span></a>
      - <a href="#pymatgen.io.feff.inputs.Tags.diff"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Tags.diff()</code></span></a>
      - <a href="#pymatgen.io.feff.inputs.Tags.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Tags.from_dict()</code></span></a>
      - <a href="#pymatgen.io.feff.inputs.Tags.from_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Tags.from_file()</code></span></a>
      - <a href="#pymatgen.io.feff.inputs.Tags.get_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Tags.get_str()</code></span></a>
      - <a href="#pymatgen.io.feff.inputs.Tags.proc_val"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Tags.proc_val()</code></span></a>
      - <a href="#pymatgen.io.feff.inputs.Tags.write_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Tags.write_file()</code></span></a>
    - <a href="#pymatgen.io.feff.inputs.get_absorbing_atom_symbol_index"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">get_absorbing_atom_symbol_index()</code></span></a>
    - <a href="#pymatgen.io.feff.inputs.get_atom_map"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">get_atom_map()</code></span></a>
  - <a href="#module-pymatgen.io.feff.outputs"
    class="reference internal">pymatgen.io.feff.outputs module</a>
    - <a href="#pymatgen.io.feff.outputs.Eels"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Eels</code></span></a>
      - <a href="#pymatgen.io.feff.outputs.Eels.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Eels.as_dict()</code></span></a>
      - <a href="#pymatgen.io.feff.outputs.Eels.atomic_background"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Eels.atomic_background</code></span></a>
      - <a href="#pymatgen.io.feff.outputs.Eels.energies"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Eels.energies</code></span></a>
      - <a href="#pymatgen.io.feff.outputs.Eels.fine_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Eels.fine_structure</code></span></a>
      - <a href="#pymatgen.io.feff.outputs.Eels.from_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Eels.from_file()</code></span></a>
      - <a href="#pymatgen.io.feff.outputs.Eels.total_spectrum"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Eels.total_spectrum</code></span></a>
    - <a href="#pymatgen.io.feff.outputs.LDos"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">LDos</code></span></a>
      - <a href="#pymatgen.io.feff.outputs.LDos.charge_transfer_from_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LDos.charge_transfer_from_file()</code></span></a>
      - <a href="#pymatgen.io.feff.outputs.LDos.charge_transfer_to_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LDos.charge_transfer_to_str()</code></span></a>
      - <a href="#pymatgen.io.feff.outputs.LDos.from_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LDos.from_file()</code></span></a>
    - <a href="#pymatgen.io.feff.outputs.Xmu" class="reference internal"><span
      class="pre"><code
      class="docutils literal notranslate">Xmu</code></span></a>
      - <a href="#pymatgen.io.feff.outputs.Xmu.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Xmu.as_dict()</code></span></a>
      - <a href="#pymatgen.io.feff.outputs.Xmu.calc"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Xmu.calc</code></span></a>
      - <a href="#pymatgen.io.feff.outputs.Xmu.chi"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Xmu.chi</code></span></a>
      - <a href="#pymatgen.io.feff.outputs.Xmu.e_fermi"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Xmu.e_fermi</code></span></a>
      - <a href="#pymatgen.io.feff.outputs.Xmu.edge"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Xmu.edge</code></span></a>
      - <a href="#pymatgen.io.feff.outputs.Xmu.energies"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Xmu.energies</code></span></a>
      - <a href="#pymatgen.io.feff.outputs.Xmu.from_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Xmu.from_file()</code></span></a>
      - <a href="#pymatgen.io.feff.outputs.Xmu.material_formula"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Xmu.material_formula</code></span></a>
      - <a href="#pymatgen.io.feff.outputs.Xmu.mu"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Xmu.mu</code></span></a>
      - <a href="#pymatgen.io.feff.outputs.Xmu.mu0"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Xmu.mu0</code></span></a>
      - <a href="#pymatgen.io.feff.outputs.Xmu.relative_energies"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Xmu.relative_energies</code></span></a>
      - <a href="#pymatgen.io.feff.outputs.Xmu.source"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Xmu.source</code></span></a>
      - <a href="#pymatgen.io.feff.outputs.Xmu.wavenumber"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Xmu.wavenumber</code></span></a>
  - <a href="#module-pymatgen.io.feff.sets"
    class="reference internal">pymatgen.io.feff.sets module</a>
    - <a href="#pymatgen.io.feff.sets.AbstractFeffInputSet"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">AbstractFeffInputSet</code></span></a>
      - <a href="#pymatgen.io.feff.sets.AbstractFeffInputSet.all_input"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractFeffInputSet.all_input()</code></span></a>
      - <a href="#pymatgen.io.feff.sets.AbstractFeffInputSet.atoms"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractFeffInputSet.atoms</code></span></a>
      - <a href="#pymatgen.io.feff.sets.AbstractFeffInputSet.header"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractFeffInputSet.header()</code></span></a>
      - <a href="#pymatgen.io.feff.sets.AbstractFeffInputSet.potential"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractFeffInputSet.potential</code></span></a>
      - <a href="#pymatgen.io.feff.sets.AbstractFeffInputSet.tags"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractFeffInputSet.tags</code></span></a>
      - <a href="#pymatgen.io.feff.sets.AbstractFeffInputSet.write_input"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractFeffInputSet.write_input()</code></span></a>
    - <a href="#pymatgen.io.feff.sets.FEFFDictSet"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">FEFFDictSet</code></span></a>
      - <a href="#pymatgen.io.feff.sets.FEFFDictSet.atoms"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">FEFFDictSet.atoms</code></span></a>
      - <a href="#pymatgen.io.feff.sets.FEFFDictSet.from_directory"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">FEFFDictSet.from_directory()</code></span></a>
      - <a href="#pymatgen.io.feff.sets.FEFFDictSet.header"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">FEFFDictSet.header()</code></span></a>
      - <a href="#pymatgen.io.feff.sets.FEFFDictSet.potential"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">FEFFDictSet.potential</code></span></a>
      - <a href="#pymatgen.io.feff.sets.FEFFDictSet.tags"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">FEFFDictSet.tags</code></span></a>
    - <a href="#pymatgen.io.feff.sets.MPEELSDictSet"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">MPEELSDictSet</code></span></a>
    - <a href="#pymatgen.io.feff.sets.MPELNESSet"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">MPELNESSet</code></span></a>
      - <a href="#pymatgen.io.feff.sets.MPELNESSet.CONFIG"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MPELNESSet.CONFIG</code></span></a>
    - <a href="#pymatgen.io.feff.sets.MPEXAFSSet"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">MPEXAFSSet</code></span></a>
      - <a href="#pymatgen.io.feff.sets.MPEXAFSSet.CONFIG"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MPEXAFSSet.CONFIG</code></span></a>
    - <a href="#pymatgen.io.feff.sets.MPEXELFSSet"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">MPEXELFSSet</code></span></a>
      - <a href="#pymatgen.io.feff.sets.MPEXELFSSet.CONFIG"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MPEXELFSSet.CONFIG</code></span></a>
    - <a href="#pymatgen.io.feff.sets.MPXANESSet"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">MPXANESSet</code></span></a>
      - <a href="#pymatgen.io.feff.sets.MPXANESSet.CONFIG"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MPXANESSet.CONFIG</code></span></a>

</div>

</div>

</div>

<div class="section wy-nav-content-wrap" toggle="wy-nav-shift">

[pymatgen](index.html)

<div class="wy-nav-content">

<div class="rst-content style-external-links">

<div role="navigation" aria-label="Page navigation">

- <a href="index.html" class="icon icon-home" aria-label="Home"></a>
- pymatgen.io.feff package
- <a
  href="https://github.com/materialsproject/pymatgen/blob/master/docs_rst/pymatgen.io.feff.rst"
  class="fa fa-github">Edit on GitHub</a>

------------------------------------------------------------------------

</div>

<div class="document" role="main" itemscope="itemscope"
itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="module-pymatgen.io.feff" class="section">

<span id="pymatgen-io-feff-package"></span>

# pymatgen.io.feff package<a href="#module-pymatgen.io.feff" class="headerlink"
title="Link to this heading"></a>

This package provides the modules to perform FEFF IO.

FEFF: <a href="http://feffproject.org/feffproject-feff.html"
class="reference external">http://feffproject.org/feffproject-feff.html</a>

<div id="submodules" class="section">

## Submodules<a href="#submodules" class="headerlink"
title="Link to this heading"></a>

</div>

<div id="module-pymatgen.io.feff.inputs" class="section">

<span id="pymatgen-io-feff-inputs-module"></span>

## pymatgen.io.feff.inputs module<a href="#module-pymatgen.io.feff.inputs" class="headerlink"
title="Link to this heading"></a>

This module defines classes for reading/manipulating/writing the main
sections of FEFF input file(feff.inp), namely HEADER, ATOMS, POTENTIAL
and the program control tags.

XANES and EXAFS input files, are available, for non-spin case at this
time.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Atoms</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">struct</span></span>*, *<span class="n"><span class="pre">absorbing_atom</span></span>*, *<span class="n"><span class="pre">radius</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/inputs.py#L373-L529"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.Atoms" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Atomic cluster centered around the absorbing atom.

Parameters<span class="colon">:</span>  
- **struct**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  input structure

- **absorbing_atom** (*str* *\|* *int*) – Symbol for absorbing atom or
  site index

- **radius** (*float*) – radius of the atom cluster in Angstroms.

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">atoms_string_from_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/inputs.py#L418-L448"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.Atoms.atoms_string_from_file"
class="headerlink" title="Link to this definition"></a>  
Reads atomic shells from file such as feff.inp or ATOMS file The lines
are arranged as follows:

x y z ipot Atom Symbol Distance Number

with distance being the shell radius and ipot an integer identifying the
potential used.

Parameters<span class="colon">:</span>  
**filename** – File name containing atomic coord data.

Returns<span class="colon">:</span>  
Atoms string.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">cluster</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/feff/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.Atoms.cluster" class="headerlink"
title="Link to this definition"></a>  
The atomic cluster as a Molecule object.

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">cluster_from_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/inputs.py#L450-L470"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.Atoms.cluster_from_file"
class="headerlink" title="Link to this definition"></a>  
Parse the feff input file and return the atomic cluster as a Molecule
object.

Parameters<span class="colon">:</span>  
**filename** (*str*) – path the feff input file

Returns<span class="colon">:</span>  
the atomic cluster as Molecule object. The absorbing atom  
is the one at the origin.

Return type<span class="colon">:</span>  
<a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule">Molecule</a>

<span class="sig-name descname"><span class="pre">get_lines</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/inputs.py#L472-L507"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.Atoms.get_lines" class="headerlink"
title="Link to this definition"></a>  
Get a list of string representations of the atomic configuration
information(x, y, z, ipot, atom_symbol, distance, id).

Returns<span class="colon">:</span>  
lines sorted by the distance from the absorbing atom.

Return type<span class="colon">:</span>  
list\[list\[str \| int\]\]

<span class="sig-name descname"><span class="pre">write_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'ATOMS'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/inputs.py#L522-L529"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.Atoms.write_file" class="headerlink"
title="Link to this definition"></a>  
Write Atoms list to file.

Parameters<span class="colon">:</span>  
**filename** – path for file to be written

<!-- -->

*<span class="k"><span class="pre">exception</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">FeffParseError</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/inputs.py#L1008-L1011"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.FeffParseError" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="pymatgen.io.html#pymatgen.io.core.ParseError"
class="reference internal" title="pymatgen.io.core.ParseError"><span
class="pre"><code class="sourceCode python">ParseError</code></span></a>

Exception class for Structure. Raised when the structure has problems,
e.g. atoms that are too close.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Header</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">struct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">source</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">''</span></span>*, *<span class="n"><span class="pre">comment</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">''</span></span>*, *<span class="n"><span class="pre">spacegroup_analyzer_settings</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/inputs.py#L146-L370"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.Header" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Create Header for the FEFF input file.

Has the following format:

> <div>
>
> - This feff.inp file generated by pymatgen, materialsproject.org
>
> TITLE comment: TITLE Source: CoO19128.cif TITLE Structure Summary:
> (Co2 O2) TITLE Reduced formula: CoO TITLE space group: P1, space
> number: 1 TITLE abc: 3.297078 3.297078 5.254213 TITLE angles: 90.0
> 90.0 120.0 TITLE sites: 4 \* 1 Co 0.666666 0.333332 0.496324 \* 2 Co
> 0.333333 0.666667 0.996324 \* 3 O 0.666666 0.333332 0.878676 \* 4 O
> 0.333333 0.666667 0.378675
>
> </div>

Parameters<span class="colon">:</span>  
- **struct** – Structure or Molecule object. If a Structure,
  SpaceGroupAnalyzer is used to determine symmetrically-equivalent
  sites. If a Molecule, there is no symmetry checking.

- **source** – User supplied identifier, i.e. for Materials Project this
  would be the material ID number

- **comment** – Comment for first header line

- **spacegroup_analyzer_settings** – keyword arguments passed to
  SpacegroupAnalyzer (only used for Structure inputs).

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">formula</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/feff/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.Header.formula" class="headerlink"
title="Link to this definition"></a>  
Formula of structure.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_cif_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">cif_file</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">source</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">''</span></span>*, *<span class="n"><span class="pre">comment</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">''</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/inputs.py#L203-L219"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.Header.from_cif_file"
class="headerlink" title="Link to this definition"></a>  
Create Header object from cif_file.

Parameters<span class="colon">:</span>  
- **cif_file** – cif_file path and name

- **source** – User supplied identifier, i.e. for Materials Project this
  would be the material ID number

- **comment** – User comment that goes in header

Returns<span class="colon">:</span>  
Header Object

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/inputs.py#L231-L235"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.Header.from_file" class="headerlink"
title="Link to this definition"></a>  
Get Header object from file.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">header_str</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/inputs.py#L281-L332"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.Header.from_str" class="headerlink"
title="Link to this definition"></a>  
Reads Header string and returns Header object if header was generated by
pymatgen. Note: Checks to see if generated by pymatgen, if not it is
impossible

> <div>
>
> to generate structure object so it is not possible to generate header
> object and routine ends.
>
> </div>

Parameters<span class="colon">:</span>  
**header_str** – pymatgen generated feff.inp header

Returns<span class="colon">:</span>  
Structure object.

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">header_string_from_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'feff.inp'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/inputs.py#L237-L279"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.Header.header_string_from_file"
class="headerlink" title="Link to this definition"></a>  
Reads Header string from either a HEADER file or feff.inp file Will also
read a header from a non-pymatgen generated feff.inp file.

Parameters<span class="colon">:</span>  
**filename** – File name containing the Header data.

Returns<span class="colon">:</span>  
Reads header string.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">structure_symmetry</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/feff/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.Header.structure_symmetry"
class="headerlink" title="Link to this definition"></a>  
The space group symbol and space number of the structure.

<span class="sig-name descname"><span class="pre">write_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'HEADER'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/inputs.py#L363-L370"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.Header.write_file" class="headerlink"
title="Link to this definition"></a>  
Write Header to file.

Parameters<span class="colon">:</span>  
**filename** – Filename and path for file to be written to disk

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Paths</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">atoms</span></span>*, *<span class="n"><span class="pre">paths</span></span>*, *<span class="n"><span class="pre">degeneracies</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/inputs.py#L966-L1005"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.Paths" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Set FEFF scattering paths(‘paths.dat’ file used by the ‘genfmt’ module).

Parameters<span class="colon">:</span>  
- **atoms**
  (<a href="#pymatgen.io.feff.inputs.Atoms" class="reference internal"
  title="pymatgen.io.feff.inputs.Atoms"><em>Atoms</em></a>) – Atoms
  object

- **paths** (*list(list)*) – list of paths. Each path is a list of atom
  indices in the atomic cluster(the molecular cluster created by Atoms
  class). e.g. \[\[0, 1, 2\], \[5, 9, 4, 1\]\] -\> 2 paths: one with 3
  legs and the other with 4 legs.

- **degeneracies** (*list*) – list of degeneracies, one for each path.
  Set to 1 if not specified.

<span class="sig-name descname"><span class="pre">write_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'paths.dat'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/inputs.py#L1002-L1005"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.Paths.write_file" class="headerlink"
title="Link to this definition"></a>  
Write paths.dat.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Potential</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">struct</span></span>*, *<span class="n"><span class="pre">absorbing_atom</span></span>*, *<span class="n"><span class="pre">radius</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/inputs.py#L796-L963"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.Potential" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

FEFF atomic potential.

Parameters<span class="colon">:</span>  
- **struct**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  Structure object.

- **absorbing_atom** (*str* *\|* *int*) – Absorbing atom symbol or site
  index.

- **radius** (*float*) – radius of the atom cluster in Angstroms.

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">pot_dict_from_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">pot_data</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/inputs.py#L888-L919"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.Potential.pot_dict_from_str"
class="headerlink" title="Link to this definition"></a>  
Creates atomic symbol/potential number dictionary forward and reverse.

Parameters<span class="colon">:</span>  
**pot_data** – potential data in string format

Returns<span class="colon">:</span>  
forward and reverse atom symbol and potential number dictionaries.

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">pot_string_from_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'feff.inp'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/inputs.py#L842-L886"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.Potential.pot_string_from_file"
class="headerlink" title="Link to this definition"></a>  
Reads Potential parameters from a feff.inp or FEFFPOT file. The lines
are arranged as follows:

> <div>
>
> ipot Z element lmax1 lmax2 stoichometry spinph
>
> </div>

Parameters<span class="colon">:</span>  
**filename** – file name containing potential data.

Returns<span class="colon">:</span>  
FEFFPOT string.

<span class="sig-name descname"><span class="pre">write_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'POTENTIALS'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/inputs.py#L956-L963"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.Potential.write_file"
class="headerlink" title="Link to this definition"></a>  
Write to file.

Parameters<span class="colon">:</span>  
**filename** – filename and path to write potential file to.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Tags</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">params</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/inputs.py#L532-L793"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.Tags" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`dict`</span>

FEFF control parameters.

Parameters<span class="colon">:</span>  
**params** – A set of input parameters as a dictionary.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/inputs.py#L564-L574"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.Tags.as_dict" class="headerlink"
title="Link to this definition"></a>  
Dict representation.

Returns<span class="colon">:</span>  
Dictionary of parameters from fefftags object

<span class="sig-name descname"><span class="pre">diff</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/inputs.py#L755-L781"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.Tags.diff" class="headerlink"
title="Link to this definition"></a>  
Diff function. Compares two PARAMETER files and indicates which
parameters are the same and which are not. Useful for checking whether
two runs were done using the same parameters.

Parameters<span class="colon">:</span>  
**other** – The other PARAMETER dictionary to compare to.

Returns<span class="colon">:</span>  
has format {“Same”<span class="classifier">parameters_that_are_the_same,</span>  
”Different”: parameters_that_are_different} Note that the parameters are
return as full dictionaries of values.

Return type<span class="colon">:</span>  
dict\[str, dict\]

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/inputs.py#L576-L587"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.Tags.from_dict" class="headerlink"
title="Link to this definition"></a>  
Creates Tags object from a dictionary.

Parameters<span class="colon">:</span>  
**dct** (*dict*) – Dict of feff parameters and values.

Returns<span class="colon">:</span>  
Tags object

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'feff.inp'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/inputs.py#L657-L706"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.Tags.from_file" class="headerlink"
title="Link to this definition"></a>  
Creates a Tags dictionary from a PARAMETER or feff.inp file.

Parameters<span class="colon">:</span>  
**filename** – Filename for either PARAMETER or feff.inp file

Returns<span class="colon">:</span>  
Tags

<span class="sig-name descname"><span class="pre">get_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">sort_keys</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">pretty</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/inputs.py#L589-L635"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.Tags.get_str" class="headerlink"
title="Link to this definition"></a>  
Get a string representation of the Tags. The reason why this method is
different from the \_\_str\_\_ method is to provide options for pretty
printing.

Parameters<span class="colon">:</span>  
- **sort_keys** – Set to True to sort the Feff parameters
  alphabetically. Defaults to False.

- **pretty** – Set to True for pretty aligned output. Defaults to False.

Returns<span class="colon">:</span>  
String representation of the Tags.

Return type<span class="colon">:</span>  
str

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">proc_val</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">key</span></span>*, *<span class="n"><span class="pre">val</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/inputs.py#L708-L753"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.Tags.proc_val" class="headerlink"
title="Link to this definition"></a>  
Static helper method to convert Feff parameters to proper types, e.g.
integers, floats, lists, etc.

Parameters<span class="colon">:</span>  
- **key** – Feff parameter key

- **val** – Actual value of Feff parameter.

<span class="sig-name descname"><span class="pre">write_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'PARAMETERS'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/inputs.py#L648-L655"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.Tags.write_file" class="headerlink"
title="Link to this definition"></a>  
Write Tags to a Feff parameter tag file.

Parameters<span class="colon">:</span>  
**filename** – filename and path to write to.

<!-- -->

<span class="sig-name descname"><span class="pre">get_absorbing_atom_symbol_index</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">absorbing_atom</span></span>*, *<span class="n"><span class="pre">structure</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/inputs.py#L1034-L1048"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.get_absorbing_atom_symbol_index"
class="headerlink" title="Link to this definition"></a>  
Get the absorbing atom symbol and site index in the given structure.

Parameters<span class="colon">:</span>  
- **absorbing_atom** (*str* *\|* *int*) – symbol or site index

- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>)

Returns<span class="colon">:</span>  
symbol and site index

Return type<span class="colon">:</span>  
str, int

<!-- -->

<span class="sig-name descname"><span class="pre">get_atom_map</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span>*, *<span class="n"><span class="pre">absorbing_atom</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/inputs.py#L1014-L1031"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.inputs.get_atom_map" class="headerlink"
title="Link to this definition"></a>  
Get a dict that maps each atomic symbol to a unique integer starting
from 1.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>)

- **absorbing_atom** (*str*) – symbol

Returns<span class="colon">:</span>  
mapping of atomic symbol to integer starting from 1

Return type<span class="colon">:</span>  
dict\[str, int\]

</div>

<div id="module-pymatgen.io.feff.outputs" class="section">

<span id="pymatgen-io-feff-outputs-module"></span>

## pymatgen.io.feff.outputs module<a href="#module-pymatgen.io.feff.outputs" class="headerlink"
title="Link to this heading"></a>

This module defines classes for parsing the FEFF output files.

Currently supports the xmu.dat, ldos.dat output files are for non-spin
case.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Eels</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">data</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/outputs.py#L380-L427"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.outputs.Eels" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Parse eels.dat file.

Parameters<span class="colon">:</span>  
**data** (*numpy.ndarray*) – data from eels.dat file

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/outputs.py#L423-L427"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.outputs.Eels.as_dict" class="headerlink"
title="Link to this definition"></a>  
Get dict representations of Xmu object.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">atomic_background</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ndarray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/feff/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.outputs.Eels.atomic_background"
class="headerlink" title="Link to this definition"></a>  
The atomic background of EELS.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">energies</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/feff/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.outputs.Eels.energies" class="headerlink"
title="Link to this definition"></a>  
The energies in eV.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">fine_structure</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ndarray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/feff/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.outputs.Eels.fine_structure"
class="headerlink" title="Link to this definition"></a>  
The fine structure of EELS.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">eels_dat_file</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'eels.dat'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/outputs.py#L410-L421"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.outputs.Eels.from_file" class="headerlink"
title="Link to this definition"></a>  
Parse eels spectrum.

Parameters<span class="colon">:</span>  
**eels_dat_file** (*str*) – filename and path for eels.dat

Returns<span class="colon">:</span>  
Eels

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">total_spectrum</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/feff/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.outputs.Eels.total_spectrum"
class="headerlink" title="Link to this definition"></a>  
The total eels spectrum.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">LDos</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">complete_dos</span></span>*, *<span class="n"><span class="pre">charge_transfer</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/outputs.py#L35-L252"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.outputs.LDos" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Parser for ldos files ldos01, ldos02, …

Parameters<span class="colon">:</span>  
- **complete_dos** (<a
  href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.dos.CompleteDos"
  class="reference internal"
  title="pymatgen.electronic_structure.dos.CompleteDos"><em>CompleteDos</em></a>)
  – complete dos object

- **charge_transfer** (*dict*) – computed charge transfer between atoms
  dictionary.

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">charge_transfer_from_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">feff_inp_file</span></span>*, *<span class="n"><span class="pre">ldos_file</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/outputs.py#L150-L223"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.outputs.LDos.charge_transfer_from_file"
class="headerlink" title="Link to this definition"></a>  
Get charge transfer from file.

Parameters<span class="colon">:</span>  
- **feff_inp_file** (*str*) – name of feff.inp file for run

- **ldos_file** (*str*) – ldos filename for run, assume consecutive
  order, i.e., ldos01.dat, ldos02.dat….

Returns<span class="colon">:</span>  
dictionary of dictionaries in order of potential sites ({“p”: 0.154,
“s”: 0.078, “d”: 0.0, “tot”: 0.232}, …)

<span class="sig-name descname"><span class="pre">charge_transfer_to_str</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/outputs.py#L225-L252"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.outputs.LDos.charge_transfer_to_str"
class="headerlink" title="Link to this definition"></a>  
Get charge transfer as string.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">feff_inp_file</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'feff.inp'</span></span>*, *<span class="n"><span class="pre">ldos_file</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'ldos'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/outputs.py#L48-L148"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.outputs.LDos.from_file" class="headerlink"
title="Link to this definition"></a>  
Creates LDos object from raw Feff ldos files by by assuming they are
numbered consecutively, i.e. ldos01.dat ldos02.dat…

Parameters<span class="colon">:</span>  
- **feff_inp_file** (*str*) – input file of run to obtain structure

- **ldos_file** (*str*) – output ldos file of run to obtain dos info,
  etc.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Xmu</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">header</span></span>*, *<span class="n"><span class="pre">parameters</span></span>*, *<span class="n"><span class="pre">absorbing_atom</span></span>*, *<span class="n"><span class="pre">data</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/outputs.py#L255-L377"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.outputs.Xmu" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Parser for data in ‘xmu.dat’ file. The file ‘xmu.dat’ contains XANES,
EXAFS or NRIXS data depending on the situation; mu, mu_0, and chi = chi
\* mu_0 / mu_0 / (edge+50eV) as functions of absolute energy E, relative
energy E - E_f and wave number k.

Default attributes:  
xmu: Photon absorption cross section of absorbing atom in material
Energies: Energies of data point relative_energies: E - E_fermi
wavenumber: k=sqrt(E -E_fermi) mu: The total absorption cross-section.
mu0: The embedded atomic background absorption. chi: fine structure.
Edge: Absorption Edge Absorbing atom: Species of absorbing atom
Material: Formula of material Source: Source of structure Calculation:
Type of Feff calculation performed

Parameters<span class="colon">:</span>  
- **header** – Header object

- **parameters** – Tags object

- **absorbing_atom** (*str* *\|* *int*) – absorbing atom symbol or index

- **data** (*numpy.ndarray,* *Nx6*) – cross_sections.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/outputs.py#L373-L377"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.outputs.Xmu.as_dict" class="headerlink"
title="Link to this definition"></a>  
Get dict representations of Xmu object.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">calc</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/feff/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.outputs.Xmu.calc" class="headerlink"
title="Link to this definition"></a>  
Type of Feff calculation, XANES or EXAFS.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">chi</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/feff/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.outputs.Xmu.chi" class="headerlink"
title="Link to this definition"></a>  
The normalized fine structure.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">e_fermi</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/feff/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.outputs.Xmu.e_fermi" class="headerlink"
title="Link to this definition"></a>  
The Fermi level in eV.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">edge</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/feff/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.outputs.Xmu.edge" class="headerlink"
title="Link to this definition"></a>  
Excitation edge.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">energies</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/feff/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.outputs.Xmu.energies" class="headerlink"
title="Link to this definition"></a>  
The absolute energies in eV.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">xmu_dat_file</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'xmu.dat'</span></span>*, *<span class="n"><span class="pre">feff_inp_file</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'feff.inp'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/outputs.py#L290-L309"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.outputs.Xmu.from_file" class="headerlink"
title="Link to this definition"></a>  
Get Xmu from file.

Parameters<span class="colon">:</span>  
- **xmu_dat_file** (*str*) – filename and path for xmu.dat

- **feff_inp_file** (*str*) – filename and path of feff.inp input file

Returns<span class="colon">:</span>  
Xmu object

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">material_formula</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/feff/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.outputs.Xmu.material_formula"
class="headerlink" title="Link to this definition"></a>  
Chemical formula of material from feff.inp file.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">mu</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/feff/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.outputs.Xmu.mu" class="headerlink"
title="Link to this definition"></a>  
The total absorption cross-section.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">mu0</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/feff/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.outputs.Xmu.mu0" class="headerlink"
title="Link to this definition"></a>  
The embedded atomic background absorption.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">relative_energies</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/feff/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.outputs.Xmu.relative_energies"
class="headerlink" title="Link to this definition"></a>  
Energy with respect to the Fermi level E - E_f.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">source</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/feff/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.outputs.Xmu.source" class="headerlink"
title="Link to this definition"></a>  
Source identification from Header file.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">wavenumber</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/feff/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.outputs.Xmu.wavenumber" class="headerlink"
title="Link to this definition"></a>  
Get the wave number in units of AA^-1. k=sqrt(E - E_f) where E is the
energy and E_f is the Fermi level computed from electron gas theory at
the average interstitial charge density.

</div>

<div id="module-pymatgen.io.feff.sets" class="section">

<span id="pymatgen-io-feff-sets-module"></span>

## pymatgen.io.feff.sets module<a href="#module-pymatgen.io.feff.sets" class="headerlink"
title="Link to this heading"></a>

This module defines the FeffInputSet abstract base class and a concrete
implementation for the Materials Project. The basic concept behind an
input set is to specify a scheme to generate a consistent set of Feff
inputs from a structure without further user intervention. This ensures
comparability across runs.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">AbstractFeffInputSet</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/sets.py#L48-L115"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.sets.AbstractFeffInputSet" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>, <span
class="pre">`ABC`</span>

Abstract base class representing a set of Feff input parameters. The
idea is that using a FeffInputSet, a complete set of input files
(feffPOT, feffXANES, feffEXAFS, ATOMS, feff.inp)set\_ can be generated
in an automated fashion for any structure.

<span class="sig-name descname"><span class="pre">all_input</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/sets.py#L80-L87"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.sets.AbstractFeffInputSet.all_input"
class="headerlink" title="Link to this definition"></a>  
Get all input files as a dict of {filename: feffio object}.

*<span class="k"><span class="pre">abstract</span></span><span class="w"> </span><span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">atoms</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/feff/sets.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.sets.AbstractFeffInputSet.atoms"
class="headerlink" title="Link to this definition"></a>  
Get Atoms string from a structure that goes in feff.inp file.

Returns<span class="colon">:</span>  
Atoms object.

*<span class="k"><span class="pre">abstractmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">header</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/sets.py#L56-L58"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.sets.AbstractFeffInputSet.header"
class="headerlink" title="Link to this definition"></a>  
Get header to be used in feff.inp file from a pymatgen structure.

*<span class="k"><span class="pre">abstract</span></span><span class="w"> </span><span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">potential</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/feff/sets.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.sets.AbstractFeffInputSet.potential"
class="headerlink" title="Link to this definition"></a>  
Get POTENTIAL section used in feff.inp from a structure.

*<span class="k"><span class="pre">abstract</span></span><span class="w"> </span><span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">tags</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/feff/sets.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.sets.AbstractFeffInputSet.tags"
class="headerlink" title="Link to this definition"></a>  
Get standard calculation parameters.

<span class="sig-name descname"><span class="pre">write_input</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">output_dir</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'.'</span></span>*, *<span class="n"><span class="pre">make_dir_if_not_present</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/sets.py#L89-L115"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.sets.AbstractFeffInputSet.write_input"
class="headerlink" title="Link to this definition"></a>  
Write a FEFF input set to a directory.

Parameters<span class="colon">:</span>  
- **output_dir** – Directory to output the FEFF input files

- **make_dir_if_not_present** – Set to True if you want the directory (
  and the whole path) to be created if it is not present.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">FEFFDictSet</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">absorbing_atom</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">int</span></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">radius</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">config_dict</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*, *<span class="n"><span class="pre">edge</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'K'</span></span>*, *<span class="n"><span class="pre">spectrum</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'EXAFS'</span></span>*, *<span class="n"><span class="pre">nkpts</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1000</span></span>*, *<span class="n"><span class="pre">user_tag_settings</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">spacegroup_analyzer_settings</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/sets.py#L118-L356"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.sets.FEFFDictSet" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.feff.sets.AbstractFeffInputSet"
class="reference internal"
title="pymatgen.io.feff.sets.AbstractFeffInputSet"><span
class="pre"><code
class="sourceCode python">AbstractFeffInputSet</code></span></a>

Standard implementation of FeffInputSet, which can be extended by
specific implementations.

Parameters<span class="colon">:</span>  
- **absorbing_atom** (*str* *\|* *int*) – absorbing atom symbol or site
  index

- **structure** – Structure or Molecule object. If a Structure,
  SpaceGroupAnalyzer is used to determine symmetrically-equivalent
  sites. If a Molecule, there is no symmetry checking.

- **radius** (*float*) – cluster radius

- **config_dict** (*dict*) – control tag settings dict

- **edge** (*str*) – absorption edge

- **spectrum** (*str*) – type of spectrum to calculate, available
  options : EXAFS, XANES, DANES, XMCD, ELNES, EXELFS, FPRIME, NRIXS,
  XES. The default is EXAFS.

- **nkpts** (*int*) – Total number of kpoints in the brillouin zone.
  Used only when feff is run in the reciprocal space mode.

- **user_tag_settings** (*dict*) –

  override default tag settings. To delete tags, set the key ‘\_del’ in
  the user_tag_settings. eg: user_tag_settings={“\_del”: \[“COREHOLE”,
  “EXCHANGE”\]} To specify a net charge on the structure, pass an “IONS”
  tag containing a list

  > <div>
  >
  > of tuples where the first element is the unique potential value
  > (ipot value) and the second element is the charge to be applied to
  > atoms associated with that potential, e.g. {“IONS”: \[(0, 0.1), (1,
  > 0.1), (2, 0.1)\]} will result in.
  >
  > ION 0 0.1 ION 1 0.1 ION 2 0.1
  >
  > being written to the input file.
  >
  > </div>

- **spacegroup_analyzer_settings** (*dict*) – parameters passed to
  SpacegroupAnalyzer. e.g. {“symprec”: 0.01, “angle_tolerance”: 4}

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">atoms</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="#pymatgen.io.feff.inputs.Atoms" class="reference internal"
title="pymatgen.io.feff.inputs.Atoms"><span class="pre">Atoms</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/feff/sets.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.sets.FEFFDictSet.atoms" class="headerlink"
title="Link to this definition"></a>  
absorber + the rest.

Returns<span class="colon">:</span>  
Atoms

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_directory</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">input_dir</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/sets.py#L290-L356"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.sets.FEFFDictSet.from_directory"
class="headerlink" title="Link to this definition"></a>  
Read in a set of FEFF input files from a directory, which is useful when
existing FEFF input needs some adjustment.

<span class="sig-name descname"><span class="pre">header</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">source</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">''</span></span>*, *<span class="n"><span class="pre">comment</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">''</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/sets.py#L218-L236"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.sets.FEFFDictSet.header" class="headerlink"
title="Link to this definition"></a>  
Creates header string from structure object.

Parameters<span class="colon">:</span>  
- **source** – Source identifier used to create structure, can be
  defined however user wants to organize structures, calculations, etc.
  example would be Materials Project material ID number.

- **comment** – comment to include in header

Returns<span class="colon">:</span>  
Header

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">potential</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="#pymatgen.io.feff.inputs.Potential" class="reference internal"
title="pymatgen.io.feff.inputs.Potential"><span
class="pre">Potential</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/feff/sets.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.sets.FEFFDictSet.potential"
class="headerlink" title="Link to this definition"></a>  
FEFF potential.

Returns<span class="colon">:</span>  
Potential

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">tags</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="#pymatgen.io.feff.inputs.Tags" class="reference internal"
title="pymatgen.io.feff.inputs.Tags"><span class="pre">Tags</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/feff/sets.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.sets.FEFFDictSet.tags" class="headerlink"
title="Link to this definition"></a>  
FEFF job parameters.

Returns<span class="colon">:</span>  
Tags

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">MPEELSDictSet</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">absorbing_atom</span></span>*, *<span class="n"><span class="pre">structure</span></span>*, *<span class="n"><span class="pre">edge</span></span>*, *<span class="n"><span class="pre">spectrum</span></span>*, *<span class="n"><span class="pre">radius</span></span>*, *<span class="n"><span class="pre">beam_energy</span></span>*, *<span class="n"><span class="pre">beam_direction</span></span>*, *<span class="n"><span class="pre">collection_angle</span></span>*, *<span class="n"><span class="pre">convergence_angle</span></span>*, *<span class="n"><span class="pre">config_dict</span></span>*, *<span class="n"><span class="pre">user_eels_settings</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">nkpts</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1000</span></span>*, *<span class="n"><span class="pre">user_tag_settings</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/sets.py#L437-L505"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.sets.MPEELSDictSet" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.feff.sets.FEFFDictSet" class="reference internal"
title="pymatgen.io.feff.sets.FEFFDictSet"><span class="pre"><code
class="sourceCode python">FEFFDictSet</code></span></a>

FeffDictSet for ELNES spectroscopy.

Parameters<span class="colon">:</span>  
- **absorbing_atom** (*str* *\|* *int*) – absorbing atom symbol or site
  index

- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  input structure

- **edge** (*str*) – absorption edge

- **spectrum** (*str*) – ELNES or EXELFS

- **radius** (*float*) – cluster radius in Angstroms.

- **beam_energy** (*float*) – Incident beam energy in keV

- **beam_direction** (*list*) – Incident beam direction. If None, the
  cross section will be averaged.

- **collection_angle** (*float*) – Detector collection angle in mrad.

- **convergence_angle** (*float*) – Beam convergence angle in mrad.

- **user_eels_settings** (*dict*) – override default EELS config. See
  MPELNESSet.yaml for supported keys.

- **nkpts** (*int*) – Total number of kpoints in the brillouin zone.
  Used only when feff is run in the reciprocal space mode.

- **user_tag_settings** (*dict*) – override default tag settings

- **\*\*kwargs** – Passthrough to FEFFDictSet.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">MPELNESSet</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">absorbing_atom</span></span>*, *<span class="n"><span class="pre">structure</span></span>*, *<span class="n"><span class="pre">edge</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'K'</span></span>*, *<span class="n"><span class="pre">radius</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">10.0</span></span>*, *<span class="n"><span class="pre">beam_energy</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">100</span></span>*, *<span class="n"><span class="pre">beam_direction</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">collection_angle</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1</span></span>*, *<span class="n"><span class="pre">convergence_angle</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1</span></span>*, *<span class="n"><span class="pre">user_eels_settings</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">nkpts</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1000</span></span>*, *<span class="n"><span class="pre">user_tag_settings</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/sets.py#L508-L561"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.sets.MPELNESSet" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.feff.sets.MPEELSDictSet"
class="reference internal"
title="pymatgen.io.feff.sets.MPEELSDictSet"><span class="pre"><code
class="sourceCode python">MPEELSDictSet</code></span></a>

FeffDictSet for ELNES spectroscopy.

Parameters<span class="colon">:</span>  
- **absorbing_atom** (*str* *\|* *int*) – absorbing atom symbol or site
  index

- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  input structure

- **edge** (*str*) – absorption edge

- **radius** (*float*) – cluster radius in Angstroms.

- **beam_energy** (*float*) – Incident beam energy in keV

- **beam_direction** (*list*) – Incident beam direction. If None, the
  cross section will be averaged.

- **collection_angle** (*float*) – Detector collection angle in mrad.

- **convergence_angle** (*float*) – Beam convergence angle in mrad.

- **user_eels_settings** (*dict*) – override default EELS config. See
  MPELNESSet.yaml for supported keys.

- **nkpts** (*int*) – Total number of kpoints in the brillouin zone.
  Used only when feff is run in the reciprocal space mode.

- **user_tag_settings** (*dict*) – override default tag settings

- **\*\*kwargs** – Passthrough to FEFFDictSet.

<span class="sig-name descname"><span class="pre">CONFIG</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">{'CONTROL':</span> <span class="pre">'1</span> <span class="pre">1</span> <span class="pre">1</span> <span class="pre">1</span> <span class="pre">1</span> <span class="pre">1',</span> <span class="pre">'COREHOLE':</span> <span class="pre">'FSR',</span> <span class="pre">'EDGE':</span> <span class="pre">'K',</span> <span class="pre">'ELNES':</span> <span class="pre">{'ANGLES':</span> <span class="pre">'1</span> <span class="pre">1',</span> <span class="pre">'BEAM_DIRECTION':</span> <span class="pre">'0</span> <span class="pre">1</span> <span class="pre">0',</span> <span class="pre">'BEAM_ENERGY':</span> <span class="pre">'100</span> <span class="pre">0</span> <span class="pre">1</span> <span class="pre">1',</span> <span class="pre">'ENERGY':</span> <span class="pre">'4</span> <span class="pre">0.04</span> <span class="pre">0.1',</span> <span class="pre">'MESH':</span> <span class="pre">'50</span> <span class="pre">1',</span> <span class="pre">'POSITION':</span> <span class="pre">'0.0</span> <span class="pre">0.0'},</span> <span class="pre">'EXCHANGE':</span> <span class="pre">'0</span> <span class="pre">0.0</span> <span class="pre">0.0</span> <span class="pre">2',</span> <span class="pre">'FMS':</span> <span class="pre">'7.5</span> <span class="pre">0',</span> <span class="pre">'LDOS':</span> <span class="pre">'-20.0</span> <span class="pre">20.0</span> <span class="pre">0.1',</span> <span class="pre">'PRINT':</span> <span class="pre">'1</span> <span class="pre">0</span> <span class="pre">0</span> <span class="pre">0</span> <span class="pre">0</span> <span class="pre">0',</span> <span class="pre">'S02':</span> <span class="pre">0.0,</span> <span class="pre">'SCF':</span> <span class="pre">'6.0</span> <span class="pre">0</span> <span class="pre">30</span> <span class="pre">0.2</span> <span class="pre">1'}</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/feff/sets.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.sets.MPELNESSet.CONFIG" class="headerlink"
title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">MPEXAFSSet</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">absorbing_atom</span></span>*, *<span class="n"><span class="pre">structure</span></span>*, *<span class="n"><span class="pre">edge</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'K'</span></span>*, *<span class="n"><span class="pre">radius</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">10.0</span></span>*, *<span class="n"><span class="pre">nkpts</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1000</span></span>*, *<span class="n"><span class="pre">user_tag_settings</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/sets.py#L398-L434"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.sets.MPEXAFSSet" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.feff.sets.FEFFDictSet" class="reference internal"
title="pymatgen.io.feff.sets.FEFFDictSet"><span class="pre"><code
class="sourceCode python">FEFFDictSet</code></span></a>

FeffDictSet for EXAFS spectroscopy.

Parameters<span class="colon">:</span>  
- **absorbing_atom** (*str* *\|* *int*) – absorbing atom symbol or site
  index

- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  input structure

- **edge** (*str*) – absorption edge

- **radius** (*float*) – cluster radius in Angstroms.

- **nkpts** (*int*) – Total number of kpoints in the brillouin zone.
  Used only when feff is run in the reciprocal space mode.

- **user_tag_settings** (*dict*) – override default tag settings

- **\*\*kwargs** – Passthrough to FEFFDictSet.

<span class="sig-name descname"><span class="pre">CONFIG</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">{'CONTROL':</span> <span class="pre">'1</span> <span class="pre">1</span> <span class="pre">1</span> <span class="pre">1</span> <span class="pre">1</span> <span class="pre">1',</span> <span class="pre">'COREHOLE':</span> <span class="pre">'FSR',</span> <span class="pre">'EDGE':</span> <span class="pre">'K',</span> <span class="pre">'EXAFS':</span> <span class="pre">20,</span> <span class="pre">'PRINT':</span> <span class="pre">'1</span> <span class="pre">0</span> <span class="pre">0</span> <span class="pre">0</span> <span class="pre">0</span> <span class="pre">0',</span> <span class="pre">'RPATH':</span> <span class="pre">10,</span> <span class="pre">'S02':</span> <span class="pre">0.0,</span> <span class="pre">'SCF':</span> <span class="pre">'4.5</span> <span class="pre">0</span> <span class="pre">30</span> <span class="pre">.2</span> <span class="pre">1'}</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/feff/sets.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.sets.MPEXAFSSet.CONFIG" class="headerlink"
title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">MPEXELFSSet</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">absorbing_atom</span></span>*, *<span class="n"><span class="pre">structure</span></span>*, *<span class="n"><span class="pre">edge</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'K'</span></span>*, *<span class="n"><span class="pre">radius</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">10.0</span></span>*, *<span class="n"><span class="pre">beam_energy</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">100</span></span>*, *<span class="n"><span class="pre">beam_direction</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">collection_angle</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1</span></span>*, *<span class="n"><span class="pre">convergence_angle</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1</span></span>*, *<span class="n"><span class="pre">user_eels_settings</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">nkpts</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1000</span></span>*, *<span class="n"><span class="pre">user_tag_settings</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/sets.py#L564-L617"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.sets.MPEXELFSSet" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.feff.sets.MPEELSDictSet"
class="reference internal"
title="pymatgen.io.feff.sets.MPEELSDictSet"><span class="pre"><code
class="sourceCode python">MPEELSDictSet</code></span></a>

FeffDictSet for EXELFS spectroscopy.

Parameters<span class="colon">:</span>  
- **absorbing_atom** (*str* *\|* *int*) – absorbing atom symbol or site
  index

- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  input structure

- **edge** (*str*) – absorption edge

- **radius** (*float*) – cluster radius in Angstroms.

- **beam_energy** (*float*) – Incident beam energy in keV

- **beam_direction** (*list*) – Incident beam direction. If None, the
  cross section will be averaged.

- **collection_angle** (*float*) – Detector collection angle in mrad.

- **convergence_angle** (*float*) – Beam convergence angle in mrad.

- **user_eels_settings** (*dict*) – override default EELS config. See
  MPEXELFSSet.yaml for supported keys.

- **nkpts** (*int*) – Total number of kpoints in the brillouin zone.
  Used only when feff is run in the reciprocal space mode.

- **user_tag_settings** (*dict*) – override default tag settings

- **\*\*kwargs** – Passthrough to FEFFDictSet.

<span class="sig-name descname"><span class="pre">CONFIG</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">{'CONTROL':</span> <span class="pre">'1</span> <span class="pre">1</span> <span class="pre">1</span> <span class="pre">1</span> <span class="pre">1</span> <span class="pre">1',</span> <span class="pre">'COREHOLE':</span> <span class="pre">'FSR',</span> <span class="pre">'EDGE':</span> <span class="pre">'K',</span> <span class="pre">'EXCHANGE':</span> <span class="pre">'0</span> <span class="pre">0.0</span> <span class="pre">0.0</span> <span class="pre">2',</span> <span class="pre">'EXELFS':</span> <span class="pre">{'ANGLES':</span> <span class="pre">'1</span> <span class="pre">1',</span> <span class="pre">'BEAM_DIRECTION':</span> <span class="pre">'0</span> <span class="pre">1</span> <span class="pre">0',</span> <span class="pre">'BEAM_ENERGY':</span> <span class="pre">'100</span> <span class="pre">0</span> <span class="pre">1</span> <span class="pre">1',</span> <span class="pre">'ENERGY':</span> <span class="pre">20,</span> <span class="pre">'MESH':</span> <span class="pre">'50</span> <span class="pre">1',</span> <span class="pre">'POSITION':</span> <span class="pre">'0.0</span> <span class="pre">0.0'},</span> <span class="pre">'PRINT':</span> <span class="pre">'1</span> <span class="pre">0</span> <span class="pre">0</span> <span class="pre">0</span> <span class="pre">0</span> <span class="pre">0',</span> <span class="pre">'RPATH':</span> <span class="pre">10,</span> <span class="pre">'S02':</span> <span class="pre">0.0,</span> <span class="pre">'SCF':</span> <span class="pre">'5.0</span> <span class="pre">0</span> <span class="pre">30</span> <span class="pre">0.2</span> <span class="pre">1'}</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/feff/sets.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.sets.MPEXELFSSet.CONFIG" class="headerlink"
title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">MPXANESSet</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">absorbing_atom</span></span>*, *<span class="n"><span class="pre">structure</span></span>*, *<span class="n"><span class="pre">edge</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'K'</span></span>*, *<span class="n"><span class="pre">radius</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">10.0</span></span>*, *<span class="n"><span class="pre">nkpts</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1000</span></span>*, *<span class="n"><span class="pre">user_tag_settings</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/feff/sets.py#L359-L395"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.sets.MPXANESSet" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.feff.sets.FEFFDictSet" class="reference internal"
title="pymatgen.io.feff.sets.FEFFDictSet"><span class="pre"><code
class="sourceCode python">FEFFDictSet</code></span></a>

FeffDictSet for XANES spectroscopy.

Parameters<span class="colon">:</span>  
- **absorbing_atom** (*str* *\|* *int*) – absorbing atom symbol or site
  index

- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  input

- **edge** (*str*) – absorption edge

- **radius** (*float*) – cluster radius in Angstroms.

- **nkpts** (*int*) – Total number of kpoints in the brillouin zone.
  Used only when feff is run in the reciprocal space mode.

- **user_tag_settings** (*dict*) – override default tag settings

- **\*\*kwargs** – Passthrough to FEFFDictSet.

<span class="sig-name descname"><span class="pre">CONFIG</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">{'CONTROL':</span> <span class="pre">'1</span> <span class="pre">1</span> <span class="pre">1</span> <span class="pre">1</span> <span class="pre">1</span> <span class="pre">1',</span> <span class="pre">'COREHOLE':</span> <span class="pre">'FSR',</span> <span class="pre">'EDGE':</span> <span class="pre">'K',</span> <span class="pre">'EXCHANGE':</span> <span class="pre">'0</span> <span class="pre">0.0</span> <span class="pre">0.0</span> <span class="pre">2',</span> <span class="pre">'FMS':</span> <span class="pre">'7.5</span> <span class="pre">0',</span> <span class="pre">'LDOS':</span> <span class="pre">'-30.</span> <span class="pre">15.</span> <span class="pre">.1',</span> <span class="pre">'PRINT':</span> <span class="pre">'1</span> <span class="pre">0</span> <span class="pre">0</span> <span class="pre">0</span> <span class="pre">0</span> <span class="pre">0',</span> <span class="pre">'S02':</span> <span class="pre">0.0,</span> <span class="pre">'SCF':</span> <span class="pre">'4.5</span> <span class="pre">0</span> <span class="pre">30</span> <span class="pre">.2</span> <span class="pre">1',</span> <span class="pre">'XANES':</span> <span class="pre">'3.7</span> <span class="pre">.04</span> <span class="pre">.1'}</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/feff/sets.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.feff.sets.MPXANESSet.CONFIG" class="headerlink"
title="Link to this definition"></a>  

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
