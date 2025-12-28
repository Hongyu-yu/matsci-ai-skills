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

- <a href="#" class="reference internal">pymatgen.io.pwmat package</a>
  - <a href="#submodules" class="reference internal">Submodules</a>
  - <a href="#module-pymatgen.io.pwmat.inputs"
    class="reference internal">pymatgen.io.pwmat.inputs module</a>
    - <a href="#pymatgen.io.pwmat.inputs.ACExtractor"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">ACExtractor</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.ACExtractor.get_coords"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ACExtractor.get_coords()</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.ACExtractor.get_lattice"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ACExtractor.get_lattice()</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.ACExtractor.get_magmoms"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ACExtractor.get_magmoms()</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.ACExtractor.get_n_atoms"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ACExtractor.get_n_atoms()</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.ACExtractor.get_types"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ACExtractor.get_types()</code></span></a>
    - <a href="#pymatgen.io.pwmat.inputs.ACExtractorBase"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">ACExtractorBase</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.ACExtractorBase.get_coords"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ACExtractorBase.get_coords()</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.ACExtractorBase.get_lattice"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ACExtractorBase.get_lattice()</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.ACExtractorBase.get_magmoms"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ACExtractorBase.get_magmoms()</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.ACExtractorBase.get_n_atoms"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ACExtractorBase.get_n_atoms()</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.ACExtractorBase.get_types"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ACExtractorBase.get_types()</code></span></a>
    - <a href="#pymatgen.io.pwmat.inputs.ACstrExtractor"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">ACstrExtractor</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.ACstrExtractor.get_atom_energies"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ACstrExtractor.get_atom_energies()</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.ACstrExtractor.get_atom_forces"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ACstrExtractor.get_atom_forces()</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.ACstrExtractor.get_coords"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ACstrExtractor.get_coords()</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.ACstrExtractor.get_e_tot"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ACstrExtractor.get_e_tot()</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.ACstrExtractor.get_lattice"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ACstrExtractor.get_lattice()</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.ACstrExtractor.get_magmoms"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ACstrExtractor.get_magmoms()</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.ACstrExtractor.get_n_atoms"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ACstrExtractor.get_n_atoms()</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.ACstrExtractor.get_types"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ACstrExtractor.get_types()</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.ACstrExtractor.get_virial"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ACstrExtractor.get_virial()</code></span></a>
    - <a href="#pymatgen.io.pwmat.inputs.AtomConfig"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">AtomConfig</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.AtomConfig.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AtomConfig.as_dict()</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.AtomConfig.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AtomConfig.from_dict()</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.AtomConfig.from_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AtomConfig.from_file()</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.AtomConfig.from_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AtomConfig.from_str()</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.AtomConfig.get_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AtomConfig.get_str()</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.AtomConfig.write_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AtomConfig.write_file()</code></span></a>
    - <a href="#pymatgen.io.pwmat.inputs.GenKpt"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">GenKpt</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.GenKpt.from_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GenKpt.from_structure()</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.GenKpt.get_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GenKpt.get_str()</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.GenKpt.write_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GenKpt.write_file()</code></span></a>
    - <a href="#pymatgen.io.pwmat.inputs.HighSymmetryPoint"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">HighSymmetryPoint</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.HighSymmetryPoint.from_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">HighSymmetryPoint.from_structure()</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.HighSymmetryPoint.get_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">HighSymmetryPoint.get_str()</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.HighSymmetryPoint.write_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">HighSymmetryPoint.write_file()</code></span></a>
    - <a href="#pymatgen.io.pwmat.inputs.LineLocator"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">LineLocator</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.LineLocator.locate_all_lines"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LineLocator.locate_all_lines()</code></span></a>
    - <a href="#pymatgen.io.pwmat.inputs.ListLocator"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">ListLocator</code></span></a>
      - <a href="#pymatgen.io.pwmat.inputs.ListLocator.locate_all_lines"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ListLocator.locate_all_lines()</code></span></a>
  - <a href="#module-pymatgen.io.pwmat.outputs"
    class="reference internal">pymatgen.io.pwmat.outputs module</a>
    - <a href="#pymatgen.io.pwmat.outputs.DosSpin"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">DosSpin</code></span></a>
      - <a href="#pymatgen.io.pwmat.outputs.DosSpin.dos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DosSpin.dos</code></span></a>
      - <a href="#pymatgen.io.pwmat.outputs.DosSpin.get_partial_dos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DosSpin.get_partial_dos()</code></span></a>
      - <a href="#pymatgen.io.pwmat.outputs.DosSpin.labels"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DosSpin.labels</code></span></a>
    - <a href="#pymatgen.io.pwmat.outputs.Movement"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Movement</code></span></a>
      - <a href="#pymatgen.io.pwmat.outputs.Movement.atom_configs"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Movement.atom_configs</code></span></a>
      - <a href="#pymatgen.io.pwmat.outputs.Movement.atom_forces"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Movement.atom_forces</code></span></a>
      - <a href="#pymatgen.io.pwmat.outputs.Movement.e_atoms"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Movement.e_atoms</code></span></a>
      - <a href="#pymatgen.io.pwmat.outputs.Movement.e_tots"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Movement.e_tots</code></span></a>
      - <a href="#pymatgen.io.pwmat.outputs.Movement.virials"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Movement.virials</code></span></a>
    - <a href="#pymatgen.io.pwmat.outputs.OutFermi"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">OutFermi</code></span></a>
      - <a href="#pymatgen.io.pwmat.outputs.OutFermi.e_fermi"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">OutFermi.e_fermi</code></span></a>
    - <a href="#pymatgen.io.pwmat.outputs.Report"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Report</code></span></a>
      - <a href="#pymatgen.io.pwmat.outputs.Report.eigenvalues"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Report.eigenvalues</code></span></a>
      - <a href="#pymatgen.io.pwmat.outputs.Report.hsps"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Report.hsps</code></span></a>
      - <a href="#pymatgen.io.pwmat.outputs.Report.kpoints"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Report.kpoints</code></span></a>
      - <a href="#pymatgen.io.pwmat.outputs.Report.kpoints_weight"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Report.kpoints_weight</code></span></a>
      - <a href="#pymatgen.io.pwmat.outputs.Report.n_bands"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Report.n_bands</code></span></a>
      - <a href="#pymatgen.io.pwmat.outputs.Report.n_kpoints"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Report.n_kpoints</code></span></a>
      - <a href="#pymatgen.io.pwmat.outputs.Report.spin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Report.spin</code></span></a>

</div>

</div>

</div>

<div class="section wy-nav-content-wrap" toggle="wy-nav-shift">

[pymatgen](index.html)

<div class="wy-nav-content">

<div class="rst-content style-external-links">

<div role="navigation" aria-label="Page navigation">

- <a href="index.html" class="icon icon-home" aria-label="Home"></a>
- pymatgen.io.pwmat package
- <a
  href="https://github.com/materialsproject/pymatgen/blob/master/docs_rst/pymatgen.io.pwmat.rst"
  class="fa fa-github">Edit on GitHub</a>

------------------------------------------------------------------------

</div>

<div class="document" role="main" itemscope="itemscope"
itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="module-pymatgen.io.pwmat" class="section">

<span id="pymatgen-io-pwmat-package"></span>

# pymatgen.io.pwmat package<a href="#module-pymatgen.io.pwmat" class="headerlink"
title="Link to this heading"></a>

This package implements modules for input and output to and from PWmat.

<div id="submodules" class="section">

## Submodules<a href="#submodules" class="headerlink"
title="Link to this heading"></a>

</div>

<div id="module-pymatgen.io.pwmat.inputs" class="section">

<span id="pymatgen-io-pwmat-inputs-module"></span>

## pymatgen.io.pwmat.inputs module<a href="#module-pymatgen.io.pwmat.inputs" class="headerlink"
title="Link to this heading"></a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ACExtractor</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">file_path</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L95-L189"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.ACExtractor" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.pwmat.inputs.ACExtractorBase"
class="reference internal"
title="pymatgen.io.pwmat.inputs.ACExtractorBase"><span class="pre"><code
class="sourceCode python">ACExtractorBase</code></span></a>

Extract information contained in atom.config : number of atoms, lattice,
types, frac_coords, magmoms.

Initialization function.

Parameters<span class="colon">:</span>  
**file_path** (*str*) – The absolute path of atom.config file.

<span class="sig-name descname"><span class="pre">get_coords</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">ndarray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L145-L164"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.ACExtractor.get_coords"
class="headerlink" title="Link to this definition"></a>  
Return the fractional coordinates in structure.

Returns<span class="colon">:</span>  
Fractional coordinates.

Return type<span class="colon">:</span>  
np.ndarray

<span class="sig-name descname"><span class="pre">get_lattice</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">ndarray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L116-L129"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.ACExtractor.get_lattice"
class="headerlink" title="Link to this definition"></a>  
Return the lattice of structure.

Returns<span class="colon">:</span>  
np.ndarray, shape = (9,)

Return type<span class="colon">:</span>  
lattice

<span class="sig-name descname"><span class="pre">get_magmoms</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">ndarray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L166-L189"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.ACExtractor.get_magmoms"
class="headerlink" title="Link to this definition"></a>  
Return the magenetic moments of atoms in structure.

Returns<span class="colon">:</span>  
The magnetic moments of individual atoms.

Return type<span class="colon">:</span>  
np.ndarray

<span class="sig-name descname"><span class="pre">get_n\_atoms</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">int</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L111-L114"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.ACExtractor.get_n_atoms"
class="headerlink" title="Link to this definition"></a>  
Return the number of atoms in the structure.

<span class="sig-name descname"><span class="pre">get_types</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">ndarray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L131-L143"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.ACExtractor.get_types"
class="headerlink" title="Link to this definition"></a>  
Return the atomic number of atoms in structure.

Returns<span class="colon">:</span>  
Atomic numbers in order corresponding to sites

Return type<span class="colon">:</span>  
np.ndarray

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ACExtractorBase</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L71-L92"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.ACExtractorBase" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`ABC`</span>

A parent class of ACExtractor and ACstrExtractor, ensuring that they are
as consistent as possible.

*<span class="k"><span class="pre">abstractmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">get_coords</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">ndarray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L86-L88"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.ACExtractorBase.get_coords"
class="headerlink" title="Link to this definition"></a>  
Get fractional coordinates of atoms in structure defined by atom.config
file.

*<span class="k"><span class="pre">abstractmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">get_lattice</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">ndarray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L78-L80"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.ACExtractorBase.get_lattice"
class="headerlink" title="Link to this definition"></a>  
Get the lattice of structure defined by atom.config file.

*<span class="k"><span class="pre">abstractmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">get_magmoms</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">ndarray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L90-L92"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.ACExtractorBase.get_magmoms"
class="headerlink" title="Link to this definition"></a>  
Get atomic magmoms of atoms in structure defined by atom.config file.

*<span class="k"><span class="pre">abstractmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">get_n\_atoms</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">int</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L74-L76"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.ACExtractorBase.get_n_atoms"
class="headerlink" title="Link to this definition"></a>  
Get the number of atoms in structure defined by atom.config file.

*<span class="k"><span class="pre">abstractmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">get_types</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">ndarray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L82-L84"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.ACExtractorBase.get_types"
class="headerlink" title="Link to this definition"></a>  
Get atomic number of atoms in structure defined by atom.config file.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ACstrExtractor</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">atom_config_str</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L192-L357"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.ACstrExtractor" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.pwmat.inputs.ACExtractorBase"
class="reference internal"
title="pymatgen.io.pwmat.inputs.ACExtractorBase"><span class="pre"><code
class="sourceCode python">ACExtractorBase</code></span></a>

Extract information from atom.config file. You can get str by slicing
the MOVEMENT.

Initialization function.

Parameters<span class="colon">:</span>  
**atom_config_str** (*str*) – A string describing the structure in
atom.config file.

<span class="sig-name descname"><span class="pre">get_atom_energies</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L291-L311"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.ACstrExtractor.get_atom_energies"
class="headerlink" title="Link to this definition"></a>  
Return the energies of individual atoms in material system.

When turning on ENERGY DEPOSITION, PWmat will output energy per atom.

Returns<span class="colon">:</span>  
The energies of individual atoms within the material system.

Return type<span class="colon">:</span>  
np.ndarray \| None

<span class="sig-name descname"><span class="pre">get_atom_forces</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">ndarray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L313-L327"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.ACstrExtractor.get_atom_forces"
class="headerlink" title="Link to this definition"></a>  
Return the force on atoms in material system.

Returns<span class="colon">:</span>  
Forces acting on individual atoms of shape=(num_atoms\*3,)

Return type<span class="colon">:</span>  
np.ndarray

<span class="sig-name descname"><span class="pre">get_coords</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">ndarray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L240-L254"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.ACstrExtractor.get_coords"
class="headerlink" title="Link to this definition"></a>  
Return the fractional coordinate of atoms in structure.

Returns<span class="colon">:</span>  
Fractional coordinates of atoms of shape=(num_atoms\*3,)

Return type<span class="colon">:</span>  
np.ndarray

<span class="sig-name descname"><span class="pre">get_e\_tot</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">ndarray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L275-L289"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.ACstrExtractor.get_e_tot"
class="headerlink" title="Link to this definition"></a>  
Return the total energy of structure.

Returns<span class="colon">:</span>  
The total energy of the material system.

Return type<span class="colon">:</span>  
np.ndarray

<span class="sig-name descname"><span class="pre">get_lattice</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">ndarray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L213-L226"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.ACstrExtractor.get_lattice"
class="headerlink" title="Link to this definition"></a>  
Return the lattice of structure.

Returns<span class="colon">:</span>  
Lattice basis vectors of shape=(9,)

Return type<span class="colon">:</span>  
np.ndarray

<span class="sig-name descname"><span class="pre">get_magmoms</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">ndarray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L256-L273"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.ACstrExtractor.get_magmoms"
class="headerlink" title="Link to this definition"></a>  
Return the magnetic moments of atoms in structure.

Returns<span class="colon">:</span>  
Atomic magnetic moments.

Return type<span class="colon">:</span>  
np.ndarray

<span class="sig-name descname"><span class="pre">get_n\_atoms</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">int</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L205-L211"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.ACstrExtractor.get_n_atoms"
class="headerlink" title="Link to this definition"></a>  
Return the number of atoms in structure.

Returns<span class="colon">:</span>  
The number of atoms

Return type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">get_types</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">ndarray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L228-L238"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.ACstrExtractor.get_types"
class="headerlink" title="Link to this definition"></a>  
Return the atomic number of atoms in structure.

Returns<span class="colon">:</span>  
Types of elements.

Return type<span class="colon">:</span>  
np.ndarray

<span class="sig-name descname"><span class="pre">get_virial</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L329-L357"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.ACstrExtractor.get_virial"
class="headerlink" title="Link to this definition"></a>  
Return the virial tensor of material system.

Returns<span class="colon">:</span>  
Virial tensor of shape=(9,)

Return type<span class="colon">:</span>  
np.ndarray \| None

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">AtomConfig</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.IStructure"
class="reference internal"
title="pymatgen.core.structure.IStructure"><span
class="pre">IStructure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">sort_structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L360-L483"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.AtomConfig" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Object for representing the data in a atom.config or final.config file.

Initialization function.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  Structure object

- **sort_structure** (*bool,* *optional*) – Whether to sort the
  structure. Useful if species are not grouped properly together.
  Defaults to False.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L473-L483"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.AtomConfig.as_dict"
class="headerlink" title="Link to this definition"></a>  
Returns<span class="colon">:</span>  
dict.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L425-L435"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.AtomConfig.from_dict"
class="headerlink" title="Link to this definition"></a>  
Get a AtomConfig object from a dictionary.

Parameters<span class="colon">:</span>  
**dct** – dict containing atom.config data

Returns<span class="colon">:</span>  
AtomConfig object.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*, *<span class="n"><span class="pre">mag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L411-L423"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.AtomConfig.from_file"
class="headerlink" title="Link to this definition"></a>  
Get a AtomConfig from a file.

Parameters<span class="colon">:</span>  
- **filename** (*PathLike*) – File name containing AtomConfig data

- **mag** (*bool,* *optional*) – Whether to read magnetic moments.
  Defaults to True.

Returns<span class="colon">:</span>  
AtomConfig object.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">data</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">mag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L384-L409"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.AtomConfig.from_str"
class="headerlink" title="Link to this definition"></a>  
Reads a atom.config from a string.

Parameters<span class="colon">:</span>  
- **data** (*str*) – string containing atom.config data

- **mag** (*bool,* *optional*) – Whether to read magnetic moment
  information.

Returns<span class="colon">:</span>  
AtomConfig object

<span class="sig-name descname"><span class="pre">get_str</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L437-L466"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.AtomConfig.get_str"
class="headerlink" title="Link to this definition"></a>  
Return a string describing the structure in atom.config format.

Returns<span class="colon">:</span>  
String representation of atom.config

Return type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">write_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L468-L471"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.AtomConfig.write_file"
class="headerlink" title="Link to this definition"></a>  
Write AtomConfig to a file.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">GenKpt</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">reciprocal_lattice</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ndarray</span></span>*, *<span class="n"><span class="pre">kpoints</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">ndarray</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">path</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">density</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.01</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L486-L591"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.GenKpt" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Read and write gen.kpt. This file just generates line-mode kpoints.

Initialization function.

Parameters<span class="colon">:</span>  
- **reciprocal_lattice** (*NDArray*) – Reciprocal lattice with factor of
  2\*pi.

- **kpoints** (*dict\[str,* *np.array\]*) – Kpoints and their
  corresponding fractional coordinates.

- **kpath** (*list\[list\[str\]\]*) – All kpaths, with each list
  representing one kpath.

- **density** (*float*) – The density of kpoints mesh with factor of
  2\*pi.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_structure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.IStructure"
class="reference internal"
title="pymatgen.core.structure.IStructure"><span
class="pre">IStructure</span></a></span>*, *<span class="n"><span class="pre">dim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">density</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.01</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L510-L539"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.GenKpt.from_structure"
class="headerlink" title="Link to this definition"></a>  
Obtain a AtomConfig object from Structure object.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) – A
  structure object.

- **dim** (*int*) – The dimension of the material system (2 or 3).

- **density** (*float*) – Kpoints mesh without factor with 2\*pi.
  Program will automatically convert it with 2\*pi.

<span class="sig-name descname"><span class="pre">get_str</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L541-L582"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.GenKpt.get_str" class="headerlink"
title="Link to this definition"></a>  
Get a string to be written as a gen.kpt file.

<span class="sig-name descname"><span class="pre">write_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L584-L591"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.GenKpt.write_file" class="headerlink"
title="Link to this definition"></a>  
Write gen.kpt to a file.

Parameters<span class="colon">:</span>  
**filename** (*PathLike*) – The absolute path of file to be written.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">HighSymmetryPoint</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">reciprocal_lattice</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ndarray</span></span>*, *<span class="n"><span class="pre">kpts</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">path</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">density</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L594-L698"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.HighSymmetryPoint" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Read and write HIGH_SYMMETRY_POINTS file which generate line-mode
kpoints.

Initialization function.

Parameters<span class="colon">:</span>  
- **reciprocal_lattice** (*np.array*) – Reciprocal lattice.

- **kpts** (*dict\[str,* *list\[float\]\]*) – Kpoints and their
  corresponding fractional coordinates.

- **path** (*list\[list\[str\]\]*) – All k-paths, with each list
  representing one k-path.

- **density** (*float*) – Density of kpoints mesh with factor of 2\*pi.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_structure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.IStructure"
class="reference internal"
title="pymatgen.core.structure.IStructure"><span
class="pre">IStructure</span></a></span>*, *<span class="n"><span class="pre">dim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">density</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.01</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L618-L635"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.HighSymmetryPoint.from_structure"
class="headerlink" title="Link to this definition"></a>  
Obtain HighSymmetry object from Structure object.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) – A
  structure object.

- **dim** (*int*) – Dimension of the material system (2 or 3).

- **density** (*float,* *optional*) – Density of kpoints mesh without
  factor of 2\*pi. Defaults to 0.01. The program will automatically
  convert it to with factor of 2\*pi.

<span class="sig-name descname"><span class="pre">get_str</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L637-L693"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.HighSymmetryPoint.get_str"
class="headerlink" title="Link to this definition"></a>  
Get a string describing high symmetry points in HIGH_SYMMETRY_POINTS
format.

<span class="sig-name descname"><span class="pre">write_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L695-L698"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.HighSymmetryPoint.write_file"
class="headerlink" title="Link to this definition"></a>  
Write HighSymmetryPoint to a file.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">LineLocator</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L26-L47"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.LineLocator" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Find the line indices (starts from 1) of a certain paragraph of text
from the file.

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">locate_all_lines</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">file_path</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*, *<span class="n"><span class="pre">content</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">exclusion</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">''</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L29-L47"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.LineLocator.locate_all_lines"
class="headerlink" title="Link to this definition"></a>  
Locate the line in file where a certain paragraph of text is located
(return all indices).

Parameters<span class="colon">:</span>  
- **file_path** (*PathLike*) – Absolute path to file.

- **content** (*str*) – Certain paragraph of text that needs to be
  located.

- **exclusion** (*str*) – Certain paragraph of text that is excluded.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ListLocator</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L50-L68"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.ListLocator" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Find the element indices (starts from 0) of a certain paragraph of text
from the list.

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">locate_all_lines</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">strs_lst</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">content</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">exclusion</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">''</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/inputs.py#L53-L68"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.inputs.ListLocator.locate_all_lines"
class="headerlink" title="Link to this definition"></a>  
Locate the elements in list where a certain paragraph of text is located
(return all indices).

Parameters<span class="colon">:</span>  
- **strs_lst** (*list\[str\]*) – List of strings.

- **content** (*str*) – Certain paragraph of text that needs to be
  located.

- **exclusion** (*str*) – Certain paragraph of text that is excluded.

</div>

<div id="module-pymatgen.io.pwmat.outputs" class="section">

<span id="pymatgen-io-pwmat-outputs-module"></span>

## pymatgen.io.pwmat.outputs module<a href="#module-pymatgen.io.pwmat.outputs" class="headerlink"
title="Link to this heading"></a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">DosSpin</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/outputs.py#L329-L383"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.outputs.DosSpin" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Extract information of DOS from DOS_SPIN file: - DOS.totalspin,
DOS.totalspin_projected - DOS.spinup, DOS.spinup_projected -
DOS.spindown, DOS.spindown_projected.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">dos</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ndarray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/pwmat/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.outputs.DosSpin.dos" class="headerlink"
title="Link to this definition"></a>  
Value of density of state.

<span class="sig-name descname"><span class="pre">get_partial_dos</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">part</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">ndarray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/outputs.py#L366-L383"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.outputs.DosSpin.get_partial_dos"
class="headerlink" title="Link to this definition"></a>  
Get partial dos for give element or orbital.

Parameters<span class="colon">:</span>  
**part** (*str*) –

The name of partial dos. e.g. ‘Energy’, ‘Total’, ‘Cr-3S’, ‘Cr-3P’,

> <div>
>
> ’Cr-4S’, ‘Cr-3D’, ‘I-4D’, ‘I-5S’, ‘I-5P’, ‘Cr-3S’, ‘Cr-3Pz’, ‘Cr-3Px’,
> ‘Cr-3Py’, ‘Cr-4S’, ‘Cr-3Dz2’,’Cr-3Dxz’, ‘Cr-3Dyz’, ‘Cr-3D(x^2-y^2)’,
> ‘Cr-3Dxy’, ‘I-4Dz2’, ‘I-4Dxz’, ‘I-4Dyz’, ‘I-4D(x^2-y^2)’, ‘I-4Dxy’,
> ‘I-5S’, ‘I-5Pz’, ‘I-5Px’, ‘I-5Py’
>
> </div>

Returns<span class="colon">:</span>  
np.array

Return type<span class="colon">:</span>  
partial_dos

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">labels</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/pwmat/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.outputs.DosSpin.labels" class="headerlink"
title="Link to this definition"></a>  
The name of the partial density of states.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Movement</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*, *<span class="n"><span class="pre">ionic_step_skip</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ionic_step_offset</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/outputs.py#L26-L159"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.outputs.Movement" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Parser for data in MOVEMENT which records trajectory during MD.

Initialization function.

Parameters<span class="colon">:</span>  
- **filename** (*PathLike*) – The path of MOVEMENT

- **ionic_step_skip** (*int* *\|* *None,* *optional*) – If
  ionic_step_skip is a number \> 1, only every ionic_step_skip ionic
  steps will be read for structure and energies. This is very useful if
  you are parsing very large MOVEMENT files. Defaults to None.

- **ionic_step_offset** (*int* *\|* *None,* *optional*) – Used together
  with ionic_step_skip. If set, the first ionic step read will be offset
  by the amount of ionic_step_offset. Defaults to None.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">atom_configs</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/pwmat/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.outputs.Movement.atom_configs"
class="headerlink" title="Link to this definition"></a>  
AtomConfig for structures contained in MOVEMENT file.

Returns<span class="colon">:</span>  
List of Structure objects for the structure at each ionic step.

Return type<span class="colon">:</span>  
list\[<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure">Structure</a>\]

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">atom_forces</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ndarray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/pwmat/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.outputs.Movement.atom_forces"
class="headerlink" title="Link to this definition"></a>  
Forces on atoms in each structures contained in MOVEMENT.

Returns<span class="colon">:</span>  
The forces on atoms of each ionic step structure,  
with shape of (n_ionic_steps, n_atoms, 3).

Return type<span class="colon">:</span>  
np.ndarray

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">e_atoms</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ndarray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/pwmat/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.outputs.Movement.e_atoms" class="headerlink"
title="Link to this definition"></a>  
Individual energies of atoms in each ionic step structures contained in
MOVEMENT.

Returns<span class="colon">:</span>  
The individual energy of atoms in each ionic step structure,  
with shape of (n_ionic_steps, n_atoms).

Return type<span class="colon">:</span>  
np.ndarray

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">e_tots</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ndarray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/pwmat/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.outputs.Movement.e_tots" class="headerlink"
title="Link to this definition"></a>  
Total energies of each ionic step structures contained in MOVEMENT.

Returns<span class="colon">:</span>  
Total energy of of each ionic step structure,  
with shape of (n_ionic_steps,).

Return type<span class="colon">:</span>  
np.ndarray

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">virials</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ndarray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/pwmat/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.outputs.Movement.virials" class="headerlink"
title="Link to this definition"></a>  
Virial tensor of each ionic step structure contained in MOVEMENT.

Returns<span class="colon">:</span>  
The virial tensor of each ionic step structure,  
with shape of (n_ionic_steps, 3, 3)

Return type<span class="colon">:</span>  
np.ndarray

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">OutFermi</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/outputs.py#L162-L182"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.outputs.OutFermi" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Extract fermi energy (eV) from OUT.FERMI.

Initialization function.

Parameters<span class="colon">:</span>  
**filename** (*PathLike*) – The absolute path of OUT.FERMI file.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">e_fermi</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/pwmat/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.outputs.OutFermi.e_fermi" class="headerlink"
title="Link to this definition"></a>  
The fermi energy level.

Returns<span class="colon">:</span>  
Fermi energy level.

Return type<span class="colon">:</span>  
float

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Report</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/pwmat/outputs.py#L185-L326"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.outputs.Report" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Extract information of spin, kpoints, bands, eigenvalues from REPORT
file.

Initialization function.

Parameters<span class="colon">:</span>  
**filename** (*PathLike*) – The absolute path of REPORT file.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">eigenvalues</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ndarray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/pwmat/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.outputs.Report.eigenvalues"
class="headerlink" title="Link to this definition"></a>  
The eigenvalues.

Returns<span class="colon">:</span>  
The first index represents spin, the second index  
represents kpoint, the third index represents band.

Return type<span class="colon">:</span>  
np.ndarray

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">hsps</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">ndarray</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/pwmat/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.outputs.Report.hsps" class="headerlink"
title="Link to this definition"></a>  
The labels and fractional coordinates of high symmetry points as
dict\[str, np.ndarray\]. Empty dict when task is not line-mode kpath.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">kpoints</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ndarray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/pwmat/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.outputs.Report.kpoints" class="headerlink"
title="Link to this definition"></a>  
The fractional coordinates of kpoints.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">kpoints_weight</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ndarray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/pwmat/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.outputs.Report.kpoints_weight"
class="headerlink" title="Link to this definition"></a>  
The weight of kpoints.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">n_bands</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/pwmat/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.outputs.Report.n_bands" class="headerlink"
title="Link to this definition"></a>  
The number of bands.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">n_kpoints</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/pwmat/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.outputs.Report.n_kpoints" class="headerlink"
title="Link to this definition"></a>  
The number of k-points.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">spin</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/pwmat/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.pwmat.outputs.Report.spin" class="headerlink"
title="Link to this definition"></a>  
The spin switches.

Returns<span class="colon">:</span>  
Spin switches. 1 represents turn on spin, 2 represents turn down spin.

Return type<span class="colon">:</span>  
int

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
