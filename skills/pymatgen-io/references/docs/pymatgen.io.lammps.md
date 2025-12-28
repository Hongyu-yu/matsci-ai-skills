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

- <a href="#" class="reference internal">pymatgen.io.lammps package</a>
  - <a href="#submodules" class="reference internal">Submodules</a>
  - <a href="#module-pymatgen.io.lammps.data"
    class="reference internal">pymatgen.io.lammps.data module</a>
    - <a href="#pymatgen.io.lammps.data.CombinedData"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">CombinedData</code></span></a>
      - <a href="#pymatgen.io.lammps.data.CombinedData.as_lammpsdata"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CombinedData.as_lammpsdata()</code></span></a>
      - <a href="#pymatgen.io.lammps.data.CombinedData.disassemble"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CombinedData.disassemble()</code></span></a>
      - <a href="#pymatgen.io.lammps.data.CombinedData.from_ff_and_topologies"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CombinedData.from_ff_and_topologies()</code></span></a>
      - <a href="#pymatgen.io.lammps.data.CombinedData.from_files"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CombinedData.from_files()</code></span></a>
      - <a href="#pymatgen.io.lammps.data.CombinedData.from_lammpsdata"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CombinedData.from_lammpsdata()</code></span></a>
      - <a href="#pymatgen.io.lammps.data.CombinedData.from_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CombinedData.from_structure()</code></span></a>
      - <a href="#pymatgen.io.lammps.data.CombinedData.get_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CombinedData.get_str()</code></span></a>
      - <a href="#pymatgen.io.lammps.data.CombinedData.parse_xyz"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CombinedData.parse_xyz()</code></span></a>
      - <a href="#pymatgen.io.lammps.data.CombinedData.structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CombinedData.structure</code></span></a>
    - <a href="#pymatgen.io.lammps.data.ForceField"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">ForceField</code></span></a>
      - <a href="#pymatgen.io.lammps.data.ForceField.masses"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ForceField.masses</code></span></a>
      - <a href="#pymatgen.io.lammps.data.ForceField.force_fieldct"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ForceField.force_fieldct</code></span></a>
      - <a href="#pymatgen.io.lammps.data.ForceField.maps"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ForceField.maps</code></span></a>
      - <a href="#pymatgen.io.lammps.data.ForceField.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ForceField.from_dict()</code></span></a>
      - <a href="#pymatgen.io.lammps.data.ForceField.from_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ForceField.from_file()</code></span></a>
      - <a href="#pymatgen.io.lammps.data.ForceField.to_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ForceField.to_file()</code></span></a>
    - <a href="#pymatgen.io.lammps.data.LammpsBox"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">LammpsBox</code></span></a>
      - <a href="#pymatgen.io.lammps.data.LammpsBox.get_box_shift"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsBox.get_box_shift()</code></span></a>
      - <a href="#pymatgen.io.lammps.data.LammpsBox.get_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsBox.get_str()</code></span></a>
      - <a href="#pymatgen.io.lammps.data.LammpsBox.to_lattice"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsBox.to_lattice()</code></span></a>
      - <a href="#pymatgen.io.lammps.data.LammpsBox.volume"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsBox.volume</code></span></a>
    - <a href="#pymatgen.io.lammps.data.LammpsData"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">LammpsData</code></span></a>
      - <a href="#pymatgen.io.lammps.data.LammpsData.disassemble"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsData.disassemble()</code></span></a>
      - <a href="#pymatgen.io.lammps.data.LammpsData.from_ff_and_topologies"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsData.from_ff_and_topologies()</code></span></a>
      - <a href="#pymatgen.io.lammps.data.LammpsData.from_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsData.from_file()</code></span></a>
      - <a href="#pymatgen.io.lammps.data.LammpsData.from_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsData.from_structure()</code></span></a>
      - <a href="#pymatgen.io.lammps.data.LammpsData.get_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsData.get_str()</code></span></a>
      - <a href="#pymatgen.io.lammps.data.LammpsData.set_charge_atom"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsData.set_charge_atom()</code></span></a>
      - <a href="#pymatgen.io.lammps.data.LammpsData.set_charge_atom_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsData.set_charge_atom_type()</code></span></a>
      - <a href="#pymatgen.io.lammps.data.LammpsData.structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsData.structure</code></span></a>
      - <a href="#pymatgen.io.lammps.data.LammpsData.write_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsData.write_file()</code></span></a>
    - <a href="#pymatgen.io.lammps.data.Topology"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Topology</code></span></a>
      - <a href="#pymatgen.io.lammps.data.Topology.from_bonding"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Topology.from_bonding()</code></span></a>
    - <a href="#pymatgen.io.lammps.data.lattice_2_lmpbox"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">lattice_2_lmpbox()</code></span></a>
  - <a href="#module-pymatgen.io.lammps.generators"
    class="reference internal">pymatgen.io.lammps.generators module</a>
    - <a href="#pymatgen.io.lammps.generators.BaseLammpsGenerator"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">BaseLammpsGenerator</code></span></a>
      - <a href="#pymatgen.io.lammps.generators.BaseLammpsGenerator.template"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BaseLammpsGenerator.template</code></span></a>
      - <a href="#pymatgen.io.lammps.generators.BaseLammpsGenerator.calc_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BaseLammpsGenerator.calc_type</code></span></a>
      - <a href="#pymatgen.io.lammps.generators.BaseLammpsGenerator.settings"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BaseLammpsGenerator.settings</code></span></a>
      - <a href="#pymatgen.io.lammps.generators.BaseLammpsGenerator.keep_stages"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BaseLammpsGenerator.keep_stages</code></span></a>
      - <a href="#id0" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BaseLammpsGenerator.calc_type</code></span></a>
      - <a href="#pymatgen.io.lammps.generators.BaseLammpsGenerator.data"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BaseLammpsGenerator.data</code></span></a>
      - <a
        href="#pymatgen.io.lammps.generators.BaseLammpsGenerator.get_input_set"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BaseLammpsGenerator.get_input_set()</code></span></a>
      - <a href="#pymatgen.io.lammps.generators.BaseLammpsGenerator.inputfile"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BaseLammpsGenerator.inputfile</code></span></a>
      - <a href="#id1" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BaseLammpsGenerator.keep_stages</code></span></a>
      - <a href="#id2" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BaseLammpsGenerator.settings</code></span></a>
      - <a href="#id3" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BaseLammpsGenerator.template</code></span></a>
    - <a href="#pymatgen.io.lammps.generators.LammpsMinimization"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">LammpsMinimization</code></span></a>
      - <a href="#pymatgen.io.lammps.generators.LammpsMinimization.atom_style"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsMinimization.atom_style</code></span></a>
      - <a href="#pymatgen.io.lammps.generators.LammpsMinimization.boundary"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsMinimization.boundary</code></span></a>
      - <a href="#pymatgen.io.lammps.generators.LammpsMinimization.dimension"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsMinimization.dimension</code></span></a>
      - <a href="#pymatgen.io.lammps.generators.LammpsMinimization.force_field"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsMinimization.force_field</code></span></a>
      - <a href="#pymatgen.io.lammps.generators.LammpsMinimization.read_data"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsMinimization.read_data</code></span></a>
      - <a href="#pymatgen.io.lammps.generators.LammpsMinimization.units"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsMinimization.units</code></span></a>
  - <a href="#module-pymatgen.io.lammps.inputs"
    class="reference internal">pymatgen.io.lammps.inputs module</a>
    - <a href="#pymatgen.io.lammps.inputs.LammpsInputFile"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">LammpsInputFile</code></span></a>
      - <a href="#pymatgen.io.lammps.inputs.LammpsInputFile.add_commands"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsInputFile.add_commands()</code></span></a>
      - <a href="#pymatgen.io.lammps.inputs.LammpsInputFile.add_stage"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsInputFile.add_stage()</code></span></a>
      - <a href="#pymatgen.io.lammps.inputs.LammpsInputFile.append"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsInputFile.append()</code></span></a>
      - <a href="#pymatgen.io.lammps.inputs.LammpsInputFile.contains_command"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsInputFile.contains_command()</code></span></a>
      - <a href="#pymatgen.io.lammps.inputs.LammpsInputFile.from_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsInputFile.from_file()</code></span></a>
      - <a href="#pymatgen.io.lammps.inputs.LammpsInputFile.from_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsInputFile.from_str()</code></span></a>
      - <a href="#pymatgen.io.lammps.inputs.LammpsInputFile.get_args"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsInputFile.get_args()</code></span></a>
      - <a href="#pymatgen.io.lammps.inputs.LammpsInputFile.get_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsInputFile.get_str()</code></span></a>
      - <a href="#pymatgen.io.lammps.inputs.LammpsInputFile.merge_stages"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsInputFile.merge_stages()</code></span></a>
      - <a href="#pymatgen.io.lammps.inputs.LammpsInputFile.ncomments"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsInputFile.ncomments</code></span></a>
      - <a href="#pymatgen.io.lammps.inputs.LammpsInputFile.nstages"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsInputFile.nstages</code></span></a>
      - <a href="#pymatgen.io.lammps.inputs.LammpsInputFile.remove_command"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsInputFile.remove_command()</code></span></a>
      - <a href="#pymatgen.io.lammps.inputs.LammpsInputFile.remove_stage"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsInputFile.remove_stage()</code></span></a>
      - <a href="#pymatgen.io.lammps.inputs.LammpsInputFile.rename_stage"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsInputFile.rename_stage()</code></span></a>
      - <a href="#pymatgen.io.lammps.inputs.LammpsInputFile.set_args"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsInputFile.set_args()</code></span></a>
      - <a href="#pymatgen.io.lammps.inputs.LammpsInputFile.stages_names"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsInputFile.stages_names</code></span></a>
      - <a href="#pymatgen.io.lammps.inputs.LammpsInputFile.write_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsInputFile.write_file()</code></span></a>
    - <a href="#pymatgen.io.lammps.inputs.LammpsRun"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">LammpsRun</code></span></a>
      - <a href="#pymatgen.io.lammps.inputs.LammpsRun.md"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsRun.md()</code></span></a>
      - <a href="#pymatgen.io.lammps.inputs.LammpsRun.write_inputs"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsRun.write_inputs()</code></span></a>
    - <a href="#pymatgen.io.lammps.inputs.LammpsTemplateGen"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">LammpsTemplateGen</code></span></a>
      - <a href="#pymatgen.io.lammps.inputs.LammpsTemplateGen.get_input_set"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsTemplateGen.get_input_set()</code></span></a>
    - <a href="#pymatgen.io.lammps.inputs.write_lammps_inputs"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">write_lammps_inputs()</code></span></a>
  - <a href="#module-pymatgen.io.lammps.outputs"
    class="reference internal">pymatgen.io.lammps.outputs module</a>
    - <a href="#pymatgen.io.lammps.outputs.LammpsDump"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">LammpsDump</code></span></a>
      - <a href="#pymatgen.io.lammps.outputs.LammpsDump.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsDump.as_dict()</code></span></a>
      - <a href="#pymatgen.io.lammps.outputs.LammpsDump.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsDump.from_dict()</code></span></a>
      - <a href="#pymatgen.io.lammps.outputs.LammpsDump.from_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsDump.from_str()</code></span></a>
    - <a href="#pymatgen.io.lammps.outputs.parse_lammps_dumps"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">parse_lammps_dumps()</code></span></a>
    - <a href="#pymatgen.io.lammps.outputs.parse_lammps_log"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">parse_lammps_log()</code></span></a>
  - <a href="#module-pymatgen.io.lammps.sets"
    class="reference internal">pymatgen.io.lammps.sets module</a>
    - <a href="#pymatgen.io.lammps.sets.LammpsInputSet"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">LammpsInputSet</code></span></a>
      - <a href="#pymatgen.io.lammps.sets.LammpsInputSet.from_directory"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsInputSet.from_directory()</code></span></a>
      - <a href="#pymatgen.io.lammps.sets.LammpsInputSet.validate"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsInputSet.validate()</code></span></a>
  - <a href="#module-pymatgen.io.lammps.utils"
    class="reference internal">pymatgen.io.lammps.utils module</a>
    - <a href="#pymatgen.io.lammps.utils.LammpsRunner"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">LammpsRunner</code></span></a>
      - <a href="#pymatgen.io.lammps.utils.LammpsRunner.run"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LammpsRunner.run()</code></span></a>
    - <a href="#pymatgen.io.lammps.utils.PackmolRunner"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">PackmolRunner</code></span></a>
      - <a
        href="#pymatgen.io.lammps.utils.PackmolRunner.convert_obatoms_to_molecule"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PackmolRunner.convert_obatoms_to_molecule()</code></span></a>
      - <a
        href="#pymatgen.io.lammps.utils.PackmolRunner.restore_site_properties"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PackmolRunner.restore_site_properties()</code></span></a>
      - <a href="#pymatgen.io.lammps.utils.PackmolRunner.run"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PackmolRunner.run()</code></span></a>
      - <a href="#pymatgen.io.lammps.utils.PackmolRunner.write_pdb"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PackmolRunner.write_pdb()</code></span></a>
    - <a href="#pymatgen.io.lammps.utils.Polymer"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Polymer</code></span></a>

</div>

</div>

</div>

<div class="section wy-nav-content-wrap" toggle="wy-nav-shift">

[pymatgen](index.html)

<div class="wy-nav-content">

<div class="rst-content style-external-links">

<div role="navigation" aria-label="Page navigation">

- <a href="index.html" class="icon icon-home" aria-label="Home"></a>
- pymatgen.io.lammps package
- <a
  href="https://github.com/materialsproject/pymatgen/blob/master/docs_rst/pymatgen.io.lammps.rst"
  class="fa fa-github">Edit on GitHub</a>

------------------------------------------------------------------------

</div>

<div class="document" role="main" itemscope="itemscope"
itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="module-pymatgen.io.lammps" class="section">

<span id="pymatgen-io-lammps-package"></span>

# pymatgen.io.lammps package<a href="#module-pymatgen.io.lammps" class="headerlink"
title="Link to this heading"></a>

IO for LAMMPS.

<div id="submodules" class="section">

## Submodules<a href="#submodules" class="headerlink"
title="Link to this heading"></a>

</div>

<div id="module-pymatgen.io.lammps.data" class="section">

<span id="pymatgen-io-lammps-data-module"></span>

## pymatgen.io.lammps.data module<a href="#module-pymatgen.io.lammps.data" class="headerlink"
title="Link to this heading"></a>

This module implements a core class LammpsData for generating/parsing
LAMMPS data file, and other bridging classes to build LammpsData from
molecules. This module also implements a subclass CombinedData for
merging LammpsData object.

Only point particle styles are supported for now (atom_style in angle,
atomic, bond, charge, full and molecular only). See the pages below for
more info.

> <div>
>
> <a href="https://docs.lammps.org/atom_style.html"
> class="reference external">https://docs.lammps.org/atom_style.html</a>
> <a href="https://docs.lammps.org/read_data.html"
> class="reference external">https://docs.lammps.org/read_data.html</a>
>
> </div>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">CombinedData</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">list_of_molecules</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span>*, *<span class="n"><span class="pre">list_of_names</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">list_of_numbers</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">coordinates</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">DataFrame</span></span>*, *<span class="n"><span class="pre">atom_style</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'full'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/data.py#L1269-L1576"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.CombinedData" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.lammps.data.LammpsData" class="reference internal"
title="pymatgen.io.lammps.data.LammpsData"><span class="pre"><code
class="sourceCode python">LammpsData</code></span></a>

Object for a collective set of data for a series of LAMMPS data file.
velocities not yet implemented.

Parameters<span class="colon">:</span>  
- **list_of_molecules** – A list of LammpsData objects of a chemical
  cluster. Each LammpsData object (cluster) may contain one or more
  molecule ID.

- **list_of_names** – A list of name (string) for each cluster. The
  characters in each name are restricted to word characters (\[[<span
  id="id21" class="problematic">a-zA-Z0-9\_</span>](#id20)\]). If names
  with any non-word characters are passed in, the special characters
  will be substituted by ‘\_’.

- **list_of_numbers** – A list of Integer for counts of each molecule

- **coordinates** (*pandas.DataFrame*) – DataFrame at least containing
  columns of \[“x”, “y”, “z”\] for coordinates of atoms.

- **atom_style** (*str*) – Output atom_style. Default to “full”.

<span class="sig-name descname"><span class="pre">as_lammpsdata</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/data.py#L1551-L1576"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.CombinedData.as_lammpsdata"
class="headerlink" title="Link to this definition"></a>  
Convert a CombinedData object to a LammpsData object. attributes are
deep-copied.

box (LammpsBox): Simulation box. force_fieldct (dict): Data for force
field sections. Optional

> <div>
>
> with default to None. Only keywords in force field and class 2 force
> field are valid keys, and each value is a DataFrame.
>
> </div>

topology (dict): Data for topology sections. Optional with  
default to None. Only keywords in topology are valid keys, and each
value is a DataFrame.

<span class="sig-name descname"><span class="pre">disassemble</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">atom_labels</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">guess_element</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">ff_label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'ff_map'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/data.py#L1383-L1421"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.CombinedData.disassemble"
class="headerlink" title="Link to this definition"></a>  
Breaks down each LammpsData in CombinedData to building blocks
(LammpsBox, ForceField and a series of Topology). RESTRICTIONS
APPLIED: 1. No complex force field defined not just on atom

> <div>
>
> types, where the same type or equivalent types of topology may have
> more than one set of coefficients.
>
> </div>

2.  No intermolecular topologies (with atoms from different  
    molecule-ID) since a Topology object includes data for ONE molecule
    or structure only.

Parameters<span class="colon">:</span>  
- **atom_labels** (*\[str\]*) – List of strings (must be different from
  one another) for labelling each atom type found in Masses section.
  Default to None, where the labels are automatically added based on
  either element guess or dummy specie assignment.

- **guess_element** (*bool*) – Whether to guess the element based on its
  atomic mass. Default to True, otherwise dummy species “Qa”, “Qb”, …
  will be assigned to various atom types. The guessed or assigned
  elements will be reflected on atom labels if atom_labels is None, as
  well as on the species of molecule in each Topology.

- **ff_label** (*str*) – Site property key for labeling atoms of
  different types. Default to “ff_map”.

Returns<span class="colon">:</span>  
\[(LammpsBox, ForceField, \[Topology\]), …\]

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_ff_and_topologies</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/data.py#L1424-L1427"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.CombinedData.from_ff_and_topologies"
class="headerlink" title="Link to this definition"></a>  
Unsupported constructor for CombinedData objects.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_files</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">coordinate_file</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">list_of_numbers</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="o"><span class="pre">\*</span></span><span class="n"><span class="pre">filenames</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/data.py#L1456-L1483"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.CombinedData.from_files"
class="headerlink" title="Link to this definition"></a>  
Constructor that parse a series of data file.

Parameters<span class="colon">:</span>  
- **coordinate_file** (*str*) – The filename of xyz coordinates.

- **list_of_numbers** (*list\[int\]*) – A list of numbers specifying
  counts for each clusters parsed from files.

- **filenames** (*str*) – A series of LAMMPS data filenames in string
  format.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_lammpsdata</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">mols</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span>*, *<span class="n"><span class="pre">names</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span>*, *<span class="n"><span class="pre">list_of_numbers</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span>*, *<span class="n"><span class="pre">coordinates</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">pd.DataFrame</span></span>*, *<span class="n"><span class="pre">atom_style</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/data.py#L1485-L1516"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.CombinedData.from_lammpsdata"
class="headerlink" title="Link to this definition"></a>  
Constructor that can infer atom_style. The input LammpsData objects are
used non-destructively.

Parameters<span class="colon">:</span>  
- **mols** – a list of LammpsData of a chemical cluster.Each LammpsData
  object (cluster) may contain one or more molecule ID.

- **names** – a list of name for each cluster.

- **list_of_numbers** – a list of Integer for counts of each molecule

- **coordinates** (*pandas.DataFrame*) – DataFrame at least containing
  columns of \[“x”, “y”, “z”\] for coordinates of atoms.

- **atom_style** (*str*) – Output atom_style. Default to “full”.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_structure</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/data.py#L1429-L1432"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.CombinedData.from_structure"
class="headerlink" title="Link to this definition"></a>  
Unsupported constructor for CombinedData objects.

<span class="sig-name descname"><span class="pre">get_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">distance</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">6</span></span>*, *<span class="n"><span class="pre">velocity</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">8</span></span>*, *<span class="n"><span class="pre">charge</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">4</span></span>*, *<span class="n"><span class="pre">hybrid</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/data.py#L1518-L1549"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.CombinedData.get_str"
class="headerlink" title="Link to this definition"></a>  
Get the string representation of CombinedData, essentially the string to
be written to a file. Combination info is included as a comment. For
single molecule ID data, the info format is:

> <div>
>
> num name
>
> </div>

For data with multiple molecule ID, the format is:  
num(mols_per_data) name.

Parameters<span class="colon">:</span>  
- **distance** (*int*) – No. of significant figures to output for box
  settings (bounds and tilt) and atomic coordinates. Default to 6.

- **velocity** (*int*) – No. of significant figures to output for
  velocities. Default to 8.

- **charge** (*int*) – No. of significant figures to output for charges.
  Default to 4.

- **hybrid** (*bool*) – Whether to write hybrid coeffs types. Default to
  True. If the data object has no hybrid coeffs types and has large
  coeffs section, one may use False to speed up the process. Otherwise,
  the default is recommended.

Returns<span class="colon">:</span>  
String representation of CombinedData.

Return type<span class="colon">:</span>  
str

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">parse_xyz</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Path</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">DataFrame</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/data.py#L1434-L1454"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.CombinedData.parse_xyz"
class="headerlink" title="Link to this definition"></a>  
Load xyz file generated from packmol (for those who find it hard to
install openbabel).

Returns<span class="colon">:</span>  
pandas.DataFrame

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">structure</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lammps/data.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.CombinedData.structure"
class="headerlink" title="Link to this definition"></a>  
Exports a periodic structure object representing the simulation box.

Returns<span class="colon">:</span>  
Structure

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ForceField</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">mass_info</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span>*, *<span class="n"><span class="pre">nonbond_coeffs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">topo_coeffs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/data.py#L1063-L1266"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.ForceField" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Class carrying most data in masses and force field sections.

<span class="sig-name descname"><span class="pre">masses</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lammps/data.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.ForceField.masses" class="headerlink"
title="Link to this definition"></a>  
DataFrame for masses section.

Type<span class="colon">:</span>  
pandas.DataFrame

<span class="sig-name descname"><span class="pre">force_fieldct</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lammps/data.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.ForceField.force_fieldct"
class="headerlink" title="Link to this definition"></a>  
Force field section keywords (keys) and data (values) as DataFrames.

Type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">maps</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lammps/data.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.ForceField.maps" class="headerlink"
title="Link to this definition"></a>  
Dict for labeling atoms and topologies.

Type<span class="colon">:</span>  
dict

Parameters<span class="colon">:</span>  
- **mass_info** (*list*) – List of atomic mass info. Elements, strings
  (symbols) and floats are all acceptable for the values, with the first
  two converted to the atomic mass of an element. It is recommended to
  use dict.items() to prevent key duplications. \[(“C”, 12.01), (“H”,
  Element(“H”)), (“O”, “O”), …\]

- **nonbond_coeffs** (*list*) – List of Pair or PairIJ coefficients, of
  which the sequence must be sorted according to the species in
  mass_dict. Pair or PairIJ determined by the length of list. Optional
  with default to None.

- **topo_coeffs** (*dict*) –

  Dict with force field coefficients for molecular topologies. Optional
  with default to None. All four valid keys listed below are optional.
  Each value is a list of dicts with non-optional keys “coeffs” and
  “types”, and related class2 force field keywords as optional keys. {

  > <div>
  >
  > ”Bond Coeffs”:  
  > \[{“coeffs”: \[coeff\],  
  > ”types”: \[(“C”, “C”), …\]}, …\],
  >
  > ”Angle Coeffs”:  
  > \[{“coeffs”: \[coeff\],  
  > ”BondBond Coeffs”: \[coeff\], “types”: \[(“H”, “C”, “H”), …\]}, …\],
  >
  > ”Dihedral Coeffs”:  
  > \[{“coeffs”: \[coeff\],  
  > ”BondBond13 Coeffs”: \[coeff\], “types”: \[(“H”, “C”, “C”, “H”),
  > …\]}, …\],
  >
  > ”Improper Coeffs”:  
  > \[{“coeffs”: \[coeff\],  
  > ”AngleAngle Coeffs”: \[coeff\], “types”: \[(“H”, “C”, “C”, “H”),
  > …\]}, …\],
  >
  > </div>

  } Topology of same type or equivalent types (e.g., (“C”, “H”) and
  (“H”, “C”) bonds) are NOT ALLOWED to be defined MORE THAN ONCE with
  DIFFERENT coefficients.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/data.py#L1253-L1266"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.ForceField.from_dict"
class="headerlink" title="Link to this definition"></a>  
Constructor that reads in a dictionary.

Parameters<span class="colon">:</span>  
**dct** (*dict*) – Dictionary to read.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/data.py#L1241-L1251"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.ForceField.from_file"
class="headerlink" title="Link to this definition"></a>  
Constructor that reads in a file in YAML format.

Parameters<span class="colon">:</span>  
**filename** (*str*) – Filename.

<span class="sig-name descname"><span class="pre">to_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/data.py#L1226-L1239"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.ForceField.to_file" class="headerlink"
title="Link to this definition"></a>  
Save force field to a file in YAML format.

Parameters<span class="colon">:</span>  
**filename** (*str*) – Filename.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">LammpsBox</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">bounds</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span></span>*, *<span class="n"><span class="pre">tilt</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/data.py#L115-L195"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.LammpsBox" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Object for representing a simulation box in LAMMPS settings.

Parameters<span class="colon">:</span>  
- **bounds** – A (3, 2) array/list of floats setting the boundaries of
  simulation box.

- **tilt** – A (3,) array/list of floats setting the tilt of simulation
  box. Default to None, i.e., use an orthogonal box.

<span class="sig-name descname"><span class="pre">get_box_shift</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">i</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">np.ndarray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/data.py#L174-L185"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.LammpsBox.get_box_shift"
class="headerlink" title="Link to this definition"></a>  
Calculates the coordinate shift due to PBC.

Parameters<span class="colon">:</span>  
- **i** – A (n, 3) integer array containing the labels for box

- **entries.** (*images* *of* *n*)

Returns<span class="colon">:</span>  
Coordinate shift array with the same shape of i

<span class="sig-name descname"><span class="pre">get_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">significant_figures</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">6</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/data.py#L156-L172"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.LammpsBox.get_str" class="headerlink"
title="Link to this definition"></a>  
Get the string representation of simulation box in LAMMPS data file
format.

Parameters<span class="colon">:</span>  
**significant_figures** (*int*) – No. of significant figures to output
for box settings. Default to 6.

<span class="sig-name descname"><span class="pre">to_lattice</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="pymatgen.core.html#pymatgen.core.lattice.Lattice"
class="reference internal" title="pymatgen.core.lattice.Lattice"><span
class="pre">Lattice</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/data.py#L187-L195"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.LammpsBox.to_lattice"
class="headerlink" title="Link to this definition"></a>  
Convert the simulation box to a more powerful Lattice backend. Note that
Lattice is always periodic in 3D space while a simulation box is not
necessarily periodic in all dimensions.

Returns<span class="colon">:</span>  
Lattice

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">volume</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lammps/data.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.LammpsBox.volume" class="headerlink"
title="Link to this definition"></a>  
Volume of simulation box.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">LammpsData</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">box</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.lammps.data.LammpsBox" class="reference internal"
title="pymatgen.io.lammps.data.LammpsBox"><span
class="pre">LammpsBox</span></a></span>*, *<span class="n"><span class="pre">masses</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">DataFrame</span></span>*, *<span class="n"><span class="pre">atoms</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">DataFrame</span></span>*, *<span class="n"><span class="pre">velocities</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">DataFrame</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">force_field</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">topology</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">DataFrame</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">atom_style</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'full'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/data.py#L227-L921"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.LammpsData" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Object for representing the data in a LAMMPS data file.

Low level constructor designed to work with parsed data or other
bridging objects (ForceField and Topology). Not recommended to use
directly.

Parameters<span class="colon">:</span>  
- **box**
  (<a href="#pymatgen.io.lammps.data.LammpsBox" class="reference internal"
  title="pymatgen.io.lammps.data.LammpsBox"><em>LammpsBox</em></a>) –
  Simulation box.

- **masses** (*pandas.DataFrame*) – DataFrame with one column \[“mass”\]
  for Masses section.

- **atoms** (*pandas.DataFrame*) – DataFrame with multiple columns for
  Atoms section. Column names vary with atom_style.

- **velocities** (*pandas.DataFrame*) – DataFrame with three columns
  \[“vx”, “vy”, “vz”\] for Velocities section. Optional with default to
  None. If not None, its index should be consistent with atoms.

- **force_fieldct** (*dict*) – Data for force field sections. Optional
  with default to None. Only keywords in force field and class 2 force
  field are valid keys, and each value is a DataFrame.

- **topology** (*dict*) – Data for topology sections. Optional with
  default to None. Only keywords in topology are valid keys, and each
  value is a DataFrame.

- **atom_style** (*str*) – Output atom_style. Default to “full”.

<span class="sig-name descname"><span class="pre">disassemble</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">atom_labels</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">guess_element</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">ff_label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'ff_map'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.io.lammps.data.LammpsBox" class="reference internal"
title="pymatgen.io.lammps.data.LammpsBox"><span
class="pre">LammpsBox</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><a href="#pymatgen.io.lammps.data.ForceField" class="reference internal"
title="pymatgen.io.lammps.data.ForceField"><span
class="pre">ForceField</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.io.lammps.data.Topology" class="reference internal"
title="pymatgen.io.lammps.data.Topology"><span
class="pre">Topology</span></a><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/data.py#L479-L637"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.LammpsData.disassemble"
class="headerlink" title="Link to this definition"></a>  
Breaks down LammpsData to building blocks (LammpsBox, ForceField and a
series of Topology). RESTRICTIONS APPLIED:

1.  No complex force field defined not just on atom  
    types, where the same type or equivalent types of topology may have
    more than one set of coefficients.

2.  No intermolecular topologies (with atoms from different  
    molecule-ID) since a Topology object includes data for ONE molecule
    or structure only.

Parameters<span class="colon">:</span>  
- **atom_labels** (*\[str\]*) – List of strings (must be different from
  one another) for labelling each atom type found in Masses section.
  Default to None, where the labels are automatically added based on
  either element guess or dummy specie assignment.

- **guess_element** (*bool*) – Whether to guess the element based on its
  atomic mass. Default to True, otherwise dummy species “Qa”, “Qb”, …
  will be assigned to various atom types. The guessed or assigned
  elements will be reflected on atom labels if atom_labels is None, as
  well as on the species of molecule in each Topology.

- **ff_label** (*str*) – Site property key for labeling atoms of
  different types. Default to “ff_map”.

Returns<span class="colon">:</span>  
LammpsBox, ForceField, \[Topology\]

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_ff_and_topologies</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">box</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.lammps.data.LammpsBox" class="reference internal"
title="pymatgen.io.lammps.data.LammpsBox"><span
class="pre">LammpsBox</span></a></span>*, *<span class="n"><span class="pre">ff</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.lammps.data.ForceField" class="reference internal"
title="pymatgen.io.lammps.data.ForceField"><span
class="pre">ForceField</span></a></span>*, *<span class="n"><span class="pre">topologies</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.io.lammps.data.Topology" class="reference internal"
title="pymatgen.io.lammps.data.Topology"><span
class="pre">Topology</span></a><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">atom_style</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'full'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/data.py#L756-L847"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.LammpsData.from_ff_and_topologies"
class="headerlink" title="Link to this definition"></a>  
Constructor building LammpsData from a ForceField object and a list of
Topology objects. Do not support intermolecular topologies since a
Topology object includes data for ONE molecule or structure only.

Parameters<span class="colon">:</span>  
- **box**
  (<a href="#pymatgen.io.lammps.data.LammpsBox" class="reference internal"
  title="pymatgen.io.lammps.data.LammpsBox"><em>LammpsBox</em></a>) –
  Simulation box.

- **ff**
  (<a href="#pymatgen.io.lammps.data.ForceField" class="reference internal"
  title="pymatgen.io.lammps.data.ForceField"><em>ForceField</em></a>) –
  ForceField object with data for Masses and force field sections.

- **topologies**
  (*\[*<a href="#pymatgen.io.lammps.data.Topology" class="reference internal"
  title="pymatgen.io.lammps.data.Topology"><em>Topology</em></a>*\]*) –
  List of Topology objects with data for Atoms, Velocities and topology
  sections.

- **atom_style** (*str*) – Output atom_style. Default to “full”.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">atom_style</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'full'</span></span>*, *<span class="n"><span class="pre">sort_id</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/data.py#L639-L754"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.LammpsData.from_file"
class="headerlink" title="Link to this definition"></a>  
Constructor that parses a file.

Parameters<span class="colon">:</span>  
- **filename** (*str*) – Filename to read.

- **atom_style** (*str*) – Associated atom_style. Default to “full”.

- **sort_id** (*bool*) – Whether sort each section by id. Default to
  True.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_structure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.IStructure"
class="reference internal"
title="pymatgen.core.structure.IStructure"><span
class="pre">IStructure</span></a></span>*, *<span class="n"><span class="pre">ff_elements</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">atom_style</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'atomic'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'charge'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'charge'</span></span>*, *<span class="n"><span class="pre">is_sort</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/data.py#L849-L893"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.LammpsData.from_structure"
class="headerlink" title="Link to this definition"></a>  
Simple constructor building LammpsData from a structure without force
field parameters and topologies.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  Input structure.

- **ff_elements** (*\[str\]*) – List of strings of elements that must be
  present due to force field settings but not necessarily in the
  structure. Default to None.

- **atom_style** (*str*) – Choose between “atomic” (neutral) and
  “charge” (charged). Default to “charge”.

- **is_sort** (*bool*) – whether to sort sites

<span class="sig-name descname"><span class="pre">get_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">distance</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">6</span></span>*, *<span class="n"><span class="pre">velocity</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">8</span></span>*, *<span class="n"><span class="pre">charge</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">4</span></span>*, *<span class="n"><span class="pre">hybrid</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/data.py#L318-L461"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.LammpsData.get_str" class="headerlink"
title="Link to this definition"></a>  
Get the string representation of LammpsData, essentially the string to
be written to a file. Supports hybrid style coeffs read and write.

Parameters<span class="colon">:</span>  
- **distance** (*int*) – No. of significant figures to output for box
  settings (bounds and tilt) and atomic coordinates. Default to 6.

- **velocity** (*int*) – No. of significant figures to output for
  velocities. Default to 8.

- **charge** (*int*) – No. of significant figures to output for charges.
  Default to 4.

- **hybrid** (*bool*) – Whether to write hybrid coeffs types. Default to
  True. If the data object has no hybrid coeffs types and has large
  coeffs section, one may use False to speed up the process. Otherwise,
  the default is recommended.

Returns<span class="colon">:</span>  
String representation of LammpsData.

Return type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">set_charge_atom</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">charges</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/data.py#L895-L904"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.LammpsData.set_charge_atom"
class="headerlink" title="Link to this definition"></a>  
Set the charges of specific atoms of the data.

Parameters<span class="colon">:</span>  
**charges** – A dictionary with atom indexes as keys and charges as
values, e.g. to set the charge of the atom with index 3 to -2, use {3:
-2}.

<span class="sig-name descname"><span class="pre">set_charge_atom_type</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">charges</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/data.py#L906-L921"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.LammpsData.set_charge_atom_type"
class="headerlink" title="Link to this definition"></a>  
Add or modify charges of all atoms of a given type in the data.

Parameters<span class="colon">:</span>  
**charges** –

Dict containing the charges for the atom types to set. The dict should
contain atom types as integers or labels and charges. Example: change
the charge of Li atoms to +3:

> <div>
>
> charges={“Li”: 3} charges={1: 3} if Li atoms are of type 1
>
> </div>

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">structure</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lammps/data.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.LammpsData.structure"
class="headerlink" title="Link to this definition"></a>  
Exports a periodic structure object representing the simulation box.

Returns<span class="colon">:</span>  
Structure

<span class="sig-name descname"><span class="pre">write_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">distance</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">6</span></span>*, *<span class="n"><span class="pre">velocity</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">8</span></span>*, *<span class="n"><span class="pre">charge</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">4</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/data.py#L463-L477"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.LammpsData.write_file"
class="headerlink" title="Link to this definition"></a>  
Write LammpsData to file.

Parameters<span class="colon">:</span>  
- **filename** (*str*) – Filename.

- **distance** (*int*) – No. of significant figures to output for box
  settings (bounds and tilt) and atomic coordinates. Default to 6.

- **velocity** (*int*) – No. of significant figures to output for
  velocities. Default to 8.

- **charge** (*int*) – No. of significant figures to output for charges.
  Default to 4.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Topology</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">sites</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.sites.Site"
class="reference internal" title="pymatgen.core.sites.Site"><span
class="pre">Site</span></a><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.SiteCollection"
class="reference internal"
title="pymatgen.core.structure.SiteCollection"><span
class="pre">SiteCollection</span></a></span>*, *<span class="n"><span class="pre">ff_label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">charges</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">velocities</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">Sequence</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">topologies</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/data.py#L924-L1060"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.Topology" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Carry most data in Atoms, Velocities and Molecular Topology sections for
ONE SINGLE Molecule or Structure object, or a plain list of Sites.

Parameters<span class="colon">:</span>  
- **sites** (*\[*<a href="pymatgen.core.html#pymatgen.core.sites.Site"
  class="reference internal"
  title="pymatgen.core.sites.Site"><em>Site</em></a>*\] or*
  <a href="pymatgen.core.html#pymatgen.core.structure.SiteCollection"
  class="reference internal"
  title="pymatgen.core.structure.SiteCollection"><em>SiteCollection</em></a>)
  – A group of sites in a list or as a Molecule/Structure.

- **ff_label** (*str*) – Site property key for labeling atoms of
  different types. Default to None, i.e., use site.species_string.

- **charges** (*\[q,* *...\]*) – Charge of each site in a (n,)
  array/list, where n is the No. of sites. Default to None, i.e., search
  site property for charges.

- **velocities** (*\[\[vx,* *vy,* *vz\],* *...\]*) – Velocity of each
  site in a (n, 3) array/list, where n is the No. of sites. Default to
  None, i.e., search site property for velocities.

- **topologies** (*dict*) –

  Bonds, angles, dihedrals and improper dihedrals defined by site
  indices. Default to None, i.e., no additional topology. All four valid
  keys listed below are optional. {

  > <div>
  >
  > ”Bonds”: \[\[i, j\], …\], “Angles”: \[\[i, j, k\], …\], “Dihedrals”:
  > \[\[i, j, k, l\], …\], “Impropers”: \[\[i, j, k, l\], …\]
  >
  > </div>

  }.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_bonding</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">molecule</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">bond</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">angle</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">dihedral</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.1</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/data.py#L994-L1060"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.Topology.from_bonding"
class="headerlink" title="Link to this definition"></a>  
Another constructor that creates an instance from a molecule. Covalent
bonds and other bond-based topologies (angles and dihedrals) can be
automatically determined. Cannot be used for non bond-based topologies,
e.g. improper dihedrals.

Parameters<span class="colon">:</span>  
- **molecule**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
  class="reference internal"
  title="pymatgen.core.structure.Molecule"><em>Molecule</em></a>) –
  Input molecule.

- **bond** (*bool*) – Whether find bonds. If set to False, angle and
  dihedral searching will be skipped. Default to True.

- **angle** (*bool*) – Whether find angles. Default to True.

- **dihedral** (*bool*) – Whether find dihedrals. Default to True.

- **tol** (*float*) – Bond distance tolerance. Default to 0.1. Not
  recommended to alter.

- **\*\*kwargs** – Other kwargs supported by Topology.

<!-- -->

<span class="sig-name descname"><span class="pre">lattice_2\_lmpbox</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">lattice</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.lattice.Lattice"
class="reference internal" title="pymatgen.core.lattice.Lattice"><span
class="pre">Lattice</span></a></span>*, *<span class="n"><span class="pre">origin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">(0,</span> <span class="pre">0,</span> <span class="pre">0)</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.io.lammps.data.LammpsBox" class="reference internal"
title="pymatgen.io.lammps.data.LammpsBox"><span
class="pre">LammpsBox</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.operations.SymmOp"
class="reference internal" title="pymatgen.core.operations.SymmOp"><span
class="pre">SymmOp</span></a><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/data.py#L198-L224"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.data.lattice_2_lmpbox" class="headerlink"
title="Link to this definition"></a>  
Converts a lattice object to LammpsBox, and calculates the symmetry
operation used.

Parameters<span class="colon">:</span>  
- **lattice**
  (<a href="pymatgen.core.html#pymatgen.core.lattice.Lattice"
  class="reference internal"
  title="pymatgen.core.lattice.Lattice"><em>Lattice</em></a>) – Input
  lattice.

- **origin** – A (3,) array/list of floats setting lower bounds of
  simulation box. Default to (0, 0, 0).

Returns<span class="colon">:</span>  
tuple\[LammpsBox, SymmOp\]

</div>

<div id="module-pymatgen.io.lammps.generators" class="section">

<span id="pymatgen-io-lammps-generators-module"></span>

## pymatgen.io.lammps.generators module<a href="#module-pymatgen.io.lammps.generators" class="headerlink"
title="Link to this heading"></a>

Input set generators for LAMMPS. This InputSet and InputGenerator
implementation is based on templates and is not intended to be very
flexible. For instance, pymatgen will not detect whether a given
variable should be adapted based on others (e.g., the number of steps
from the temperature), it will not check for convergence nor will it
actually run LAMMPS. For additional flexibility and automation, use the
atomate2-lammps implementation
(<a href="https://github.com/Matgenix/atomate2-lammps"
class="reference external">https://github.com/Matgenix/atomate2-lammps</a>).

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">BaseLammpsGenerator</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">inputfile:</span> <span class="pre">\~pymatgen.io.lammps.inputs.LammpsInputFile</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">template:</span> <span class="pre">str</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">data:</span> <span class="pre">\~pymatgen.io.lammps.data.LammpsData</span> <span class="pre">\|</span> <span class="pre">\~pymatgen.io.lammps.data.CombinedData</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">settings:</span> <span class="pre">dict</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">calc_type:</span> <span class="pre">str</span> <span class="pre">=</span> <span class="pre">'lammps'</span></span>*, *<span class="n"><span class="pre">keep_stages:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/generators.py#L32-L84"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.generators.BaseLammpsGenerator"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="pymatgen.io.html#pymatgen.io.core.InputGenerator"
class="reference internal" title="pymatgen.io.core.InputGenerator"><span
class="pre"><code
class="sourceCode python">InputGenerator</code></span></a>

Base class to generate LAMMPS input sets. Uses template files for the
input. The variables that can be changed in the input template file are
those starting with a \$ sign, e.g. \$nsteps. This generic class is
specialized for each template in subclasses, e.g. LammpsMinimization.
You can create a template for your own task following those present in
pymatgen/io/lammps/templates. The parameters are then replaced based on
the values found in the settings dictionary that you provide, e.g.
{“nsteps”: 1000}.

<span class="sig-name descname"><span class="pre">template</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lammps/generators.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.generators.BaseLammpsGenerator.template"
class="headerlink" title="Link to this definition"></a>  
Path (string) to the template file used to create the InputFile for
LAMMPS.

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">calc_type</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lammps/generators.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.generators.BaseLammpsGenerator.calc_type"
class="headerlink" title="Link to this definition"></a>  
Human-readable string used to briefly describe the type of computations
performed by LAMMPS.

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">settings</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lammps/generators.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.generators.BaseLammpsGenerator.settings"
class="headerlink" title="Link to this definition"></a>  
Dictionary containing the values of the parameters to replace in the
template.

Type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">keep_stages</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lammps/generators.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.generators.BaseLammpsGenerator.keep_stages"
class="headerlink" title="Link to this definition"></a>  
If True, the string is formatted in a block structure with stage names

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">and</span> <span class="pre">newlines</span> <span class="pre">that</span> <span class="pre">differentiate</span> <span class="pre">commands</span> <span class="pre">in</span> <span class="pre">the</span> <span class="pre">respective</span> <span class="pre">stages</span> <span class="pre">of</span> <span class="pre">the</span> <span class="pre">InputFile.</span></span>  

<span class="sig-name descname"><span class="pre">If</span> <span class="pre">False,</span> <span class="pre">stage</span> <span class="pre">names</span> <span class="pre">are</span> <span class="pre">not</span> <span class="pre">printed</span> <span class="pre">and</span> <span class="pre">all</span> <span class="pre">commands</span> <span class="pre">appear</span> <span class="pre">in</span> <span class="pre">a</span> <span class="pre">single</span> <span class="pre">block.</span></span>  

/!This InputSet and InputGenerator implementation is based on templates
and is not intended to be very flexible. For instance, pymatgen will not
detect whether a given variable should be adapted based on others (e.g.,
the number of steps from the temperature), it will not check for
convergence nor will it actually run LAMMPS. For additional flexibility
and automation, use the atomate2-lammps implementation
(<a href="https://github.com/Matgenix/atomate2-lammps"
class="reference external">https://github.com/Matgenix/atomate2-lammps</a>).

<span class="sig-name descname"><span class="pre">calc_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'lammps'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lammps/generators.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id0" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">data</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="#pymatgen.io.lammps.data.LammpsData" class="reference internal"
title="pymatgen.io.lammps.data.LammpsData"><span
class="pre">LammpsData</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="#pymatgen.io.lammps.data.CombinedData"
class="reference internal"
title="pymatgen.io.lammps.data.CombinedData"><span
class="pre">CombinedData</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lammps/generators.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.generators.BaseLammpsGenerator.data"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">get_input_set</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="#pymatgen.io.lammps.data.LammpsData" class="reference internal"
title="pymatgen.io.lammps.data.LammpsData"><span
class="pre">LammpsData</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="#pymatgen.io.lammps.data.CombinedData"
class="reference internal"
title="pymatgen.io.lammps.data.CombinedData"><span
class="pre">CombinedData</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.lammps.sets.LammpsInputSet"
class="reference internal"
title="pymatgen.io.lammps.sets.LammpsInputSet"><span
class="pre">LammpsInputSet</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/generators.py#L65-L84"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lammps.generators.BaseLammpsGenerator.get_input_set"
class="headerlink" title="Link to this definition"></a>  
Generate a LammpsInputSet from the structure/data, tailored to the
template file.

<span class="sig-name descname"><span class="pre">inputfile</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="#pymatgen.io.lammps.inputs.LammpsInputFile"
class="reference internal"
title="pymatgen.io.lammps.inputs.LammpsInputFile"><span
class="pre">LammpsInputFile</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lammps/generators.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.generators.BaseLammpsGenerator.inputfile"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">keep_stages</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">True</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lammps/generators.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id1" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">settings</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lammps/generators.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id2" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">template</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lammps/generators.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id3" class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">LammpsMinimization</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">template</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">units</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'metal'</span></span>*, *<span class="n"><span class="pre">atom_style</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'full'</span></span>*, *<span class="n"><span class="pre">dimension</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">3</span></span>*, *<span class="n"><span class="pre">boundary</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'p</span> <span class="pre">p</span> <span class="pre">p'</span></span>*, *<span class="n"><span class="pre">read_data</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'system.data'</span></span>*, *<span class="n"><span class="pre">force_field</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'Unspecified</span> <span class="pre">force</span> <span class="pre">field!'</span></span>*, *<span class="n"><span class="pre">keep_stages</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/generators.py#L87-L179"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.generators.LammpsMinimization"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.lammps.generators.BaseLammpsGenerator"
class="reference internal"
title="pymatgen.io.lammps.generators.BaseLammpsGenerator"><span
class="pre"><code
class="sourceCode python">BaseLammpsGenerator</code></span></a>

Generator that yields a LammpsInputSet tailored for minimizing the
energy of a system by iteratively adjusting atom coordinates. Example
usage: <span class="pre">`` ` ``</span>` `<span
class="pre">`structure`</span>` `<span class="pre">`=`</span>` `<span
class="pre">`Structure.from_file("mp-149.cif")`</span>` `<span
class="pre">`lmp_minimization`</span>` `<span
class="pre">`=`</span>` `<span
class="pre">`LammpsMinimization(units="atomic").get_input_set(structure)`</span>` `<span
class="pre">`` ` ``</span>.

Do not forget to specify the force field, otherwise LAMMPS will not be
able to run!

This InputSet and InputGenerator implementation is based on templates
and is not intended to be very flexible. For instance, pymatgen will not
detect whether a given variable should be adapted based on others (e.g.,
the number of steps from the temperature), it will not check for
convergence nor will it actually run LAMMPS. For additional flexibility
and automation, use the atomate2-lammps implementation
(<a href="https://github.com/Matgenix/atomate2-lammps"
class="reference external">https://github.com/Matgenix/atomate2-lammps</a>).

Parameters<span class="colon">:</span>  
- **template** – Path (string) to the template file used to create the
  InputFile for LAMMPS.

- **units** – units to be used for the LAMMPS calculation (see LAMMPS
  docs).

- **atom_style** – atom_style to be used for the LAMMPS calculation (see
  LAMMPS docs).

- **dimension** – dimension to be used for the LAMMPS calculation (see
  LAMMPS docs).

- **boundary** – boundary to be used for the LAMMPS calculation (see
  LAMMPS docs).

- **read_data** – read_data to be used for the LAMMPS calculation (see
  LAMMPS docs).

- **force_field** – force field to be used for the LAMMPS calculation
  (see LAMMPS docs). Note that you should provide all the required
  information as a single string. In case of multiple lines expected in
  the input file, separate them with ‘n’ in force_field.

- **keep_stages** – If True, the string is formatted in a block
  structure with stage names and newlines that differentiate commands in
  the respective stages of the InputFile. If False, stage names are not
  printed and all commands appear in a single block.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">atom_style</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lammps/generators.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.generators.LammpsMinimization.atom_style"
class="headerlink" title="Link to this definition"></a>  
The argument of the command ‘atom_style’ passed to the generator.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">boundary</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lammps/generators.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.generators.LammpsMinimization.boundary"
class="headerlink" title="Link to this definition"></a>  
The argument of the command ‘boundary’ passed to the generator.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">dimension</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lammps/generators.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.generators.LammpsMinimization.dimension"
class="headerlink" title="Link to this definition"></a>  
The argument of the command ‘dimension’ passed to the generator.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">force_field</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lammps/generators.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.generators.LammpsMinimization.force_field"
class="headerlink" title="Link to this definition"></a>  
The details of the force field commands passed to the generator.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">read_data</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lammps/generators.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.generators.LammpsMinimization.read_data"
class="headerlink" title="Link to this definition"></a>  
The argument of the command ‘read_data’ passed to the generator.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">units</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lammps/generators.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.generators.LammpsMinimization.units"
class="headerlink" title="Link to this definition"></a>  
The argument of the command ‘units’ passed to the generator.

</div>

<div id="module-pymatgen.io.lammps.inputs" class="section">

<span id="pymatgen-io-lammps-inputs-module"></span>

## pymatgen.io.lammps.inputs module<a href="#module-pymatgen.io.lammps.inputs" class="headerlink"
title="Link to this heading"></a>

This module implements methods for reading/manipulating/writing LAMMPS
input files. It does not implement methods for automatically creating
inputs based on a structure and computation type. For this, see the
InputSet and InputGenerator in sets.py, or
<a href="https://github.com/Matgenix/atomate2-lammps"
class="reference external">https://github.com/Matgenix/atomate2-lammps</a>.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">LammpsInputFile</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">stages</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/inputs.py#L45-L873"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.inputs.LammpsInputFile" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="pymatgen.io.html#pymatgen.io.core.InputFile"
class="reference internal" title="pymatgen.io.core.InputFile"><span
class="pre"><code class="sourceCode python">InputFile</code></span></a>

LAMMPS input settings file such as in.lammps. Allows for LAMMPS input
generation in line/stage wise manner. A stage here is defined as a block
of LAMMPS input commands usually performing a specific task during the
simulation such as energy minimization or NPT/NVT runs. But more
broadly, a stage can also be a block of LAMMPS input where the
simulation box is set up, a set of variables are declared or quantities
are computed.

The LammpsInputFile is defined by the attribute stages, i.e. a list of
dicts each with keys stage_name and commands, defining the stage names
and the corresponding LAMMPS input settings (list of tuples of two
strings each). The structure is the following: [<span id="id5"
class="problematic">\`\`</span>](#id4)\` stages = \[

> <div>
>
> {“stage_name”: “Stage 1”, “commands”: \[(cmd1, args1), (cmd2,
> args2)\]}, {“stage_name”: “Stage 2”, “commands”: \[(cmd3, args3)\]},
>
> </div>

<div id="id6" class="section">

### \]<a href="#id6" class="headerlink" title="Link to this heading"></a>

where cmd’s are the LAMMPS command names (e.g., “units”, or
“pair_coeff”) and the args are the corresponding arguments. “Stage 1”
and “Stage 2” are examples of stage names.

param stages<span class="colon">:</span>  
list of LAMMPS input settings.

<!-- -->

<span class="sig-name descname"><span class="pre">add_commands</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">stage_name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">commands</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/inputs.py#L364-L426"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.inputs.LammpsInputFile.add_commands"
class="headerlink" title="Link to this definition"></a>  
Method to add a LAMMPS commands and their arguments to a stage of the
LammpsInputFile. The stage name should be provided: a default behavior
is avoided here to avoid mistakes (e.g., the commands are added to the
wrong stage).

Example

In order to add the command <span
class="pre">`pair_coeff`</span>` `<span class="pre">`1`</span>` `<span
class="pre">`1`</span>` `<span class="pre">`morse`</span>` `<span
class="pre">`0.0580`</span>` `<span class="pre">`3.987`</span>` `<span
class="pre">`3.404`</span> to the stage “Definition of the potential”,
simply use [<span id="id8" class="problematic">\`\`</span>](#id7)\`
your_input_file.add_commands(

> <div>
>
> stage_name=”Definition of the potential”, commands=”pair_coeff 1 1
> morse 0.0580 3.987 3.404”
>
> </div>

<div id="id9" class="section">

#### )<a href="#id9" class="headerlink" title="Link to this heading"></a>

To add multiple commands, use a dict or a list, e.g. [<span id="id11"
class="problematic">\`\`</span>](#id10)\` your_input_file.add_commands(

> <div>
>
> stage_name=”Definition of the potential”, commands=\[“pair_coeff 1 1
> morse 0.0580 3.987 3.404”, “units atomic”\],
>
> </div>

) your_input_file.add_commands(

> <div>
>
> stage_name=”Definition of the potential”, commands={“pair_coeff”: “1 1
> morse 0.0580 3.987 3.404”, “units”: “atomic”},
>
> </div>

</div>

<div id="id12" class="section">

#### )<a href="#id12" class="headerlink" title="Link to this heading"></a>

param stage_name<span class="colon">:</span>  
name of the stage to which the command should be added.

type stage_name<span class="colon">:</span>  
str

param commands<span class="colon">:</span>  
LAMMPS command, with or without the arguments.

type commands<span class="colon">:</span>  
str or list or dict

</div>

<!-- -->

<span class="sig-name descname"><span class="pre">add_stage</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">stage</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">commands</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">stage_name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">after_stage</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/inputs.py#L196-L294"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.inputs.LammpsInputFile.add_stage"
class="headerlink" title="Link to this definition"></a>  
Adds a new stage to the LammpsInputFile, either from a whole stage
(dict) or from a stage_name and commands. Both ways are mutually
exclusive.

Examples

1\) In order to add a stage defining the force field to be used, you can
use: [<span id="id14" class="problematic">\`\`</span>](#id13)\`
your_input_file.add_stage(

> <div>
>
> commands=\[“pair_coeff 1 1 morse 0.0580 3.987 3.404”, “pair_coeff 1 4
> morse 0.0408 1.399 3.204”\], stage_name=”Definition of the force
> field”,
>
> </div>

<div id="id15" class="section">

#### )<a href="#id15" class="headerlink" title="Link to this heading"></a>

</div>

<div id="or" class="section">

#### or<a href="#or" class="headerlink" title="Link to this heading"></a>

your_input_file.add_stage(  
{  
“stage_name”: “Definition of the force field”, “commands”: \[

> <div>
>
> (“pair_coeff”, “1 1 morse 0.0580 3.987 3.404”), (“pair_coeff”, “1 4
> morse 0.0408 1.399 3.204”),
>
> </div>

\],

}

</div>

<div id="id16" class="section">

#### )<a href="#id16" class="headerlink" title="Link to this heading"></a>

2\) Another stage could consist in an energy minimization. In that case,
the commands could look like [<span id="id18"
class="problematic">\`\`</span>](#id17)\` commands = \[

> <div>
>
> “thermo 1”, “thermo_style custom step lx ly lz press pxx pyy pzz pe”,
> “dump dmp all atom 5 run.dump”, “min_style cg”, “fix 1 all box/relax
> iso 0.0 vmax 0.001”, “minimize 1.0e-16 1.0e-16 5000 10000”,
> “write_data run.data”,
>
> </div>

</div>

<div id="id19" class="section">

#### \]<a href="#id19" class="headerlink" title="Link to this heading"></a>

or a dictionary such as {“thermo”: 1, …}, or a string with a single
command (e.g., “units atomic”).

param stage<span class="colon">:</span>  
if provided, this is the stage that will be added to the
LammpsInputFile.stages

type stage<span class="colon">:</span>  
dict

param commands<span class="colon">:</span>  
if provided, these are the LAMMPS command(s) that will be included in
the stage to add. Can pass a list of LAMMPS commands with their
arguments. Also accepts a dictionary of LAMMPS commands and
corresponding arguments as key, value pairs. A single string can also be
passed (single command together with its arguments). Not used in case a
whole stage is given.

type commands<span class="colon">:</span>  
str or list or dict

param stage_name<span class="colon">:</span>  
If a stage name is mentioned, the commands are added under that stage
block, else the new stage is named from numbering. If given, stage_name
cannot be one of the already present stage names. Not used in case a
whole stage is given.

type stage_name<span class="colon">:</span>  
str

param after_stage<span class="colon">:</span>  
Name of the stage after which this stage should be added. If None, the
stage is added at the end of the LammpsInputFile.

type after_stage<span class="colon">:</span>  
str

</div>

<!-- -->

<span class="sig-name descname"><span class="pre">append</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">lmp_input_file</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.lammps.inputs.LammpsInputFile"
class="reference internal"
title="pymatgen.io.lammps.inputs.LammpsInputFile"><span
class="pre">LammpsInputFile</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/inputs.py#L476-L502"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.inputs.LammpsInputFile.append"
class="headerlink" title="Link to this definition"></a>  
Appends a LammpsInputFile to another. The stages are merged, and the
numbering of stages/comments is either kept the same or updated.

Parameters<span class="colon">:</span>  
**lmp_input_file** (<a href="#pymatgen.io.lammps.inputs.LammpsInputFile"
class="reference internal"
title="pymatgen.io.lammps.inputs.LammpsInputFile"><em>LammpsInputFile</em></a>)
– LammpsInputFile to append.

<!-- -->

<span class="sig-name descname"><span class="pre">contains_command</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">command</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">stage_name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/inputs.py#L136-L147"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.inputs.LammpsInputFile.contains_command"
class="headerlink" title="Link to this definition"></a>  
Get whether a given command is present in the LammpsInputFile. A stage
name can be given; in this case the search will happen only for this
stage.

Parameters<span class="colon">:</span>  
- **command** (*str*) – String with the command to find in the input
  file (e.g., “units”).

- **stage_name** (*str*) – String giving the stage name where the change
  should take place.

Returns<span class="colon">:</span>  
True if the command is present, False if not.

Return type<span class="colon">:</span>  
bool

<!-- -->

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">path</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Path</span></span>*, *<span class="n"><span class="pre">ignore_comments</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">keep_stages</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/inputs.py#L641-L657"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.inputs.LammpsInputFile.from_file"
class="headerlink" title="Link to this definition"></a>  
Creates an InputFile object from a file.

Parameters<span class="colon">:</span>  
- **path** (*str* *or* *path*) – Filename to read, including path.

- **ignore_comments** (*bool*) – True if only the commands should be
  kept from the input file.

- **keep_stages** (*bool*) – True if the block structure from the input
  file should be kept. If False, a single block is assumed.

Returns<span class="colon">:</span>  
LammpsInputFile

<!-- -->

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">contents</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">ignore_comments</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">keep_stages</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/inputs.py#L559-L639"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.inputs.LammpsInputFile.from_str"
class="headerlink" title="Link to this definition"></a>  
Helper method to parse string representation of LammpsInputFile. If you
created the input file by hand, there is no guarantee that the
representation will be perfect as it is difficult to account for all the
cosmetic changes you could have done on your input script. Always check
that you have what you want ! By default, a single stage containing all
the input settings is created. If the block structure of your input file
should be kept and stored as different stages, set keep_stages to True.

Parameters<span class="colon">:</span>  
- **contents** (*str*) – String representation of LammpsInputFile.

- **ignore_comments** (*bool*) – True if only the commands should be
  kept from the input file.

- **keep_stages** (*bool*) – True if the block structure from the input
  file should be kept. If False, a single block is assumed.

Returns<span class="colon">:</span>  
LammpsInputFile

<!-- -->

<span class="sig-name descname"><span class="pre">get_args</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">command</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">stage_name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/inputs.py#L110-L134"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.inputs.LammpsInputFile.get_args"
class="headerlink" title="Link to this definition"></a>  
Given a command, returns the corresponding arguments (or list of
arguments) in the LammpsInputFile. A stage name can be given; in this
case the search will happen only for this stage. If a stage name is not
given, the command will be searched for through all of them. If the
command is not found, an empty list is returned.

Parameters<span class="colon">:</span>  
- **command** (*str*) – String with the command to find in the input
  file (e.g., “units”).

- **stage_name** (*str*) – String giving the stage name where the change
  should take place.

Returns<span class="colon">:</span>  
Value of the argument corresponding to the command. List if the same
command is used multiple times.

<!-- -->

<span class="sig-name descname"><span class="pre">get_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">ignore_comments</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">keep_stages</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/inputs.py#L504-L539"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.inputs.LammpsInputFile.get_str"
class="headerlink" title="Link to this definition"></a>  
Generate and ² the string representation of the LammpsInputFile. Stages
are separated by empty lines. The headers of the stages will be put in
comments preceding each stage. Other comments will be put inline within
stages, where they have been added.

Parameters<span class="colon">:</span>  
- **ignore_comments** (*bool*) – True if only the commands should be
  kept from the InputFile.

- **keep_stages** (*bool*) – If True, the string is formatted in a block
  structure with stage names and newlines that differentiate commands in
  the respective stages of the InputFile. If False, stage names are not
  printed and all commands appear in a single block.

Returns<span class="colon">:</span>  
String representation of the LammpsInputFile.

Return type<span class="colon">:</span>  
str

<!-- -->

<span class="sig-name descname"><span class="pre">merge_stages</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">stage_names</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/inputs.py#L327-L362"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.inputs.LammpsInputFile.merge_stages"
class="headerlink" title="Link to this definition"></a>  
Merges multiple stages of a LammpsInputFile together. The merged stage
will be at the same index as the first of the stages to be merged. The
others will appear in the same order as provided in the list. Other
non-merged stages will follow.

Parameters<span class="colon">:</span>  
**stage_names** (*list*) – list of strings giving the names of the
stages to be merged.

<!-- -->

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ncomments</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lammps/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.inputs.LammpsInputFile.ncomments"
class="headerlink" title="Link to this definition"></a>  
The number of comments in the current LammpsInputFile. Includes the
blocks of comments as well as inline comments (comment lines within
blocks of LAMMPS commands).

<!-- -->

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">nstages</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lammps/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.inputs.LammpsInputFile.nstages"
class="headerlink" title="Link to this definition"></a>  
The number of stages in the current LammpsInputFile.

<!-- -->

<span class="sig-name descname"><span class="pre">remove_command</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">command</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">stage_name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">remove_empty_stages</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/inputs.py#L428-L474"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.inputs.LammpsInputFile.remove_command"
class="headerlink" title="Link to this definition"></a>  
Removes a given command from a given stage. If no stage is given,
removes all occurrences of the command. In case removing a command
completely empties a stage, the choice whether to keep this stage in the
LammpsInputFile is given by remove_empty_stages.

Parameters<span class="colon">:</span>  
- **command** (*str*) – command to be removed.

- **stage_name** (*str* *or* *list*) – names of the stages where the
  command should be removed.

- **remove_empty_stages** (*bool*) – whether to remove the stages
  emptied by removing the command or not.

<!-- -->

<span class="sig-name descname"><span class="pre">remove_stage</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">stage_name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/inputs.py#L296-L307"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.inputs.LammpsInputFile.remove_stage"
class="headerlink" title="Link to this definition"></a>  
Removes a whole stage from the LammpsInputFile.

Parameters<span class="colon">:</span>  
**stage_name** (*str*) – name of the stage to remove.

<!-- -->

<span class="sig-name descname"><span class="pre">rename_stage</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">stage_name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">new_name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/inputs.py#L309-L325"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.inputs.LammpsInputFile.rename_stage"
class="headerlink" title="Link to this definition"></a>  
Renames a stage stage_name from LammpsInputFile into new_name. First
checks that the stage to rename is present, and that the new name is not
already a stage name.

Parameters<span class="colon">:</span>  
- **stage_name** (*str*) – name of the stage to rename.

- **new_name** (*str*) – new name of the stage.

<!-- -->

<span class="sig-name descname"><span class="pre">set_args</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">command</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">argument</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">stage_name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">how</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'all'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/inputs.py#L149-L194"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.inputs.LammpsInputFile.set_args"
class="headerlink" title="Link to this definition"></a>  
Set the arguments for the given command to the given string. If the
command is not found, nothing is done. Use LammpsInputFile.add_commands
instead. If a stage name is specified, it will be replaced or set only
for this stage. If no stage name is given, it will apply the change in
all of them that contain the given command. If the command is set
multiple times in the file/stage, it will be replaced based on “how”:
either the first occurrence, all of them, or the index of the
occurrence.

Parameters<span class="colon">:</span>  
- **command** (*str*) – String representing the command to change, e.g.
  “units”.

- **argument** (*str*) – String with the new value for the command, e.g.
  “atomic”.

- **stage_name** (*str*) – String giving the stage name where the change
  should take place.

- **how** (*str* *or* *int* *or* *list*) – “all” for changing all
  occurrences of the command within the stage_name or the whole
  InputFile, “first” for the first occurrence, int i for the i-th time
  the command is present in the stage_name or the whole InputFile,
  starting at 0. Can be a list of indexes as well.

<!-- -->

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">stages_names</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lammps/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.inputs.LammpsInputFile.stages_names"
class="headerlink" title="Link to this definition"></a>  
List of names for all the stages present in stages.

<!-- -->

<span class="sig-name descname"><span class="pre">write_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*, *<span class="n"><span class="pre">ignore_comments</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">keep_stages</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/inputs.py#L541-L557"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.inputs.LammpsInputFile.write_file"
class="headerlink" title="Link to this definition"></a>  
Write LAMMPS input file.

Parameters<span class="colon">:</span>  
- **filename** (*str* *or* *path*) – The filename to output to,
  including path.

- **ignore_comments** (*bool*) – True if only the commands should be
  kept from the InputFile.

- **keep_stages** (*bool*) – True if the block structure from the
  InputFile should be kept. If False, a single block is assumed.

</div>

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">LammpsRun</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">script_template</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">settings</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*, *<span class="n"><span class="pre">data</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.lammps.data.LammpsData" class="reference internal"
title="pymatgen.io.lammps.data.LammpsData"><span
class="pre">LammpsData</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">str</span></span>*, *<span class="n"><span class="pre">script_filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/inputs.py#L876-L967"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.inputs.LammpsRun" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Examples for various simple LAMMPS runs with given simulation box, force
field and a few more settings. Experienced LAMMPS users should consider
using write_lammps_inputs method with more sophisticated templates.

Base constructor.

Parameters<span class="colon">:</span>  
- **script_template** (*str*) – String template for input script with
  placeholders. The format for placeholders has to be ‘\$variable_name’,
  e.g. ‘\$temperature’

- **settings** (*dict*) – Contains values to be written to the
  placeholders, e.g. {‘temperature’: 1}.

- **data**
  (<a href="#pymatgen.io.lammps.data.LammpsData" class="reference internal"
  title="pymatgen.io.lammps.data.LammpsData"><em>LammpsData</em></a>
  *or* *str*) – Data file as a LammpsData instance or path to an
  existing data file. Default to None, i.e., no data file supplied.
  Useful only when read_data cmd is in the script.

- **script_filename** (*str*) – Filename for the input script.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">md</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">data</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.lammps.data.LammpsData" class="reference internal"
title="pymatgen.io.lammps.data.LammpsData"><span
class="pre">LammpsData</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">str</span></span>*, *<span class="n"><span class="pre">force_field</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">temperature</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">nsteps</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">other_settings</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.lammps.inputs.LammpsRun"
class="reference internal"
title="pymatgen.io.lammps.inputs.LammpsRun"><span
class="pre">LammpsRun</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/inputs.py#L931-L967"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.inputs.LammpsRun.md" class="headerlink"
title="Link to this definition"></a>  
Example for a simple MD run based on template md.template.

Parameters<span class="colon">:</span>  
- **data**
  (<a href="#pymatgen.io.lammps.data.LammpsData" class="reference internal"
  title="pymatgen.io.lammps.data.LammpsData"><em>LammpsData</em></a>
  *or* *str*) – Data file as a LammpsData instance or path to an
  existing data file.

- **force_field** (*str*) – Combined force field related cmds. For
  example, ‘pair_style eamnpair_coeff \* \* Cu_u3.eam’.

- **temperature** (*float*) – Simulation temperature.

- **nsteps** (*int*) – No. of steps to run.

- **other_settings** (*dict*) – other settings to be filled into
  placeholders.

<span class="sig-name descname"><span class="pre">write_inputs</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">output_dir</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/inputs.py#L910-L929"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.inputs.LammpsRun.write_inputs"
class="headerlink" title="Link to this definition"></a>  
Write all input files (input script, and data if needed). Other
supporting files are not handled at this moment.

Parameters<span class="colon">:</span>  
- **output_dir** (*str*) – Directory to output the input files.

- **\*\*kwargs** – kwargs supported by LammpsData.write_file.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">LammpsTemplateGen</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/inputs.py#L970-L1009"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.inputs.LammpsTemplateGen"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="pymatgen.io.html#pymatgen.io.template.TemplateInputGen"
class="reference internal"
title="pymatgen.io.template.TemplateInputGen"><span class="pre"><code
class="sourceCode python">TemplateInputGen</code></span></a>

Create an InputSet object for a LAMMPS run based on a template file. The
input script is constructed by substituting variables into placeholders
in the template file using python’s Template.safe_substitute() function.
The data file containing coordinates and topology information can be
provided as a LammpsData instance. Alternatively, you can include a
read_data command in the template file that points to an existing data
file. Other supporting files are not handled at the moment.

To write the input files to a directory, call
LammpsTemplateSet.write_input() See pymatgen.io.template.py for
additional documentation of this method.

<span class="sig-name descname"><span class="pre">get_input_set</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">script_template</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*, *<span class="n"><span class="pre">settings</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">script_filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'in.lammps'</span></span>*, *<span class="n"><span class="pre">data</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.lammps.data.LammpsData" class="reference internal"
title="pymatgen.io.lammps.data.LammpsData"><span
class="pre">LammpsData</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="#pymatgen.io.lammps.data.CombinedData"
class="reference internal"
title="pymatgen.io.lammps.data.CombinedData"><span
class="pre">CombinedData</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">data_filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'system.data'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="pymatgen.io.html#pymatgen.io.core.InputSet"
class="reference internal" title="pymatgen.io.core.InputSet"><span
class="pre">InputSet</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/inputs.py#L983-L1009"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.inputs.LammpsTemplateGen.get_input_set"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
- **script_template** – String template for input script with
  placeholders. The format for placeholders has to be ‘\$variable_name’,
  e.g. ‘\$temperature’

- **settings** – Contains values to be written to the placeholders, e.g.
  {‘temperature’: 1}. Default to None.

- **data** – Data file as a LammpsData instance. Default to None, i.e.,
  no data file supplied. Note that a matching ‘read_data’ command must
  be provided in the script template in order for the data file to
  actually be read.

- **script_filename** – Filename for the input file.

- **data_filename** – Filename for the data file, if provided.

<!-- -->

<span class="sig-name descname"><span class="pre">write_lammps_inputs</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">output_dir</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">script_template</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">settings</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">data</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.lammps.data.LammpsData" class="reference internal"
title="pymatgen.io.lammps.data.LammpsData"><span
class="pre">LammpsData</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">script_filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'in.lammps'</span></span>*, *<span class="n"><span class="pre">make_dir_if_not_present</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../../../.venv/lib/python3.11/site-packages/monty/dev.py#L1012-L1116"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.inputs.write_lammps_inputs"
class="headerlink" title="Link to this definition"></a>  
Write input files for a LAMMPS run. Input script is constructed from a
str template with placeholders to be filled by custom settings. Data
file is either written from a LammpsData instance or copied from an
existing file if read_data cmd is inspected in the input script. Other
supporting files are not handled at the moment.

Parameters<span class="colon">:</span>  
- **output_dir** (*str*) – Directory to output the input files.

- **script_template** (*str*) – String template for input script with
  placeholders. The format for placeholders has to be ‘\$variable_name’,
  e.g. ‘\$temperature’

- **settings** (*dict*) – Contains values to be written to the
  placeholders, e.g. {‘temperature’: 1}. Default to None.

- **data**
  (<a href="#pymatgen.io.lammps.data.LammpsData" class="reference internal"
  title="pymatgen.io.lammps.data.LammpsData"><em>LammpsData</em></a>
  *or* *str*) – Data file as a LammpsData instance or path to an
  existing data file. Default to None, i.e., no data file supplied.
  Useful only when read_data cmd is in the script.

- **script_filename** (*str*) – Filename for the input script.

- **make_dir_if_not_present** (*bool*) – Set to True if you want the
  directory (and the whole path) to be created if it is not present.

- **\*\*kwargs** – kwargs supported by LammpsData.write_file.

Examples

<div class="doctest highlight-default notranslate">

<div class="highlight">

    >>> eam_template = '''units           metal
    ... atom_style      atomic
    ...
    ... lattice         fcc 3.615
    ... region          box block 0 20 0 20 0 20
    ... create_box      1 box
    ... create_atoms    1 box
    ...
    ... pair_style      eam
    ... pair_coeff      1 1 Cu_u3.eam
    ...
    ... velocity        all create $temperature 376847 loop geom
    ...
    ... neighbor        1.0 bin
    ... neigh_modify    delay 5 every 1
    ...
    ... fix             1 all nvt temp $temperature $temperature 0.1
    ...
    ... timestep        0.005
    ...
    ... run             $nsteps'''

</div>

</div>

<div class="doctest highlight-default notranslate">

<div class="highlight">

    >>> write_lammps_inputs(".", eam_template, settings={"temperature": 1600.0, "nsteps": 100})

</div>

</div>

<div class="doctest highlight-default notranslate">

<div class="highlight">

    >>> with open("in.lammps", encoding="utf-8") as file:
    ...     script = file.read()

</div>

</div>

<div class="doctest highlight-default notranslate">

<div class="highlight">

    >>> script
    units           metal
    atom_style      atomic

</div>

</div>

lattice fcc 3.615 region box block 0 20 0 20 0 20 create_box 1 box
create_atoms 1 box

pair_style eam pair_coeff 1 1 Cu_u3.eam

velocity all create 1600.0 376847 loop geom

neighbor 1.0 bin neigh_modify delay 5 every 1

fix 1 all nvt temp 1600.0 1600.0 0.1

timestep 0.005

run 100

</div>

<div id="module-pymatgen.io.lammps.outputs" class="section">

<span id="pymatgen-io-lammps-outputs-module"></span>

## pymatgen.io.lammps.outputs module<a href="#module-pymatgen.io.lammps.outputs" class="headerlink"
title="Link to this heading"></a>

This module implements classes and methods for processing LAMMPS output
files (log and dump).

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">LammpsDump</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">timestep</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">natoms</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">box</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.lammps.data.LammpsBox" class="reference internal"
title="pymatgen.io.lammps.data.LammpsBox"><span
class="pre">LammpsBox</span></a></span>*, *<span class="n"><span class="pre">data</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">DataFrame</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/outputs.py#L33-L97"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.outputs.LammpsDump" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Object for representing dump data for a single snapshot.

Base constructor.

Parameters<span class="colon">:</span>  
- **timestep** (*int*) – Current time step.

- **natoms** (*int*) – Total number of atoms in the box.

- **box**
  (<a href="#pymatgen.io.lammps.data.LammpsBox" class="reference internal"
  title="pymatgen.io.lammps.data.LammpsBox"><em>LammpsBox</em></a>) –
  Simulation box.

- **data** (*pd.DataFrame*) – Dumped atomic data.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/outputs.py#L88-L97"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.outputs.LammpsDump.as_dict"
class="headerlink" title="Link to this definition"></a>  
Get MSONable dict.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/outputs.py#L75-L86"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.outputs.LammpsDump.from_dict"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
**dct** (*dict*) – Dict representation.

Returns<span class="colon">:</span>  
LammpsDump

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">string</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/outputs.py#L51-L73"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.outputs.LammpsDump.from_str"
class="headerlink" title="Link to this definition"></a>  
Constructor from string parsing.

Parameters<span class="colon">:</span>  
**string** (*str*) – Input string.

<!-- -->

<span class="sig-name descname"><span class="pre">parse_lammps_dumps</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">file_pattern</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/outputs.py#L100-L127"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.outputs.parse_lammps_dumps"
class="headerlink" title="Link to this definition"></a>  
Generator that parses dump file(s).

Parameters<span class="colon">:</span>  
**file_pattern** (*str*) – Filename to parse. The timestep wildcard
(e.g., dump.atom.’\*’) is supported and the files are parsed in the
sequence of timestep.

Yields<span class="colon">:</span>  
LammpsDump for each available snapshot.

<!-- -->

<span class="sig-name descname"><span class="pre">parse_lammps_log</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'log.lammps'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">DataFrame</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/outputs.py#L130-L189"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.outputs.parse_lammps_log"
class="headerlink" title="Link to this definition"></a>  
Parses log file with focus on thermo data. Both one and multi line
formats are supported. Any incomplete runs (no “Loop time” marker) will
not be parsed.

Notes

SHAKE stats printed with thermo data are not supported yet. They are
ignored in multi line format, while they may cause issues with dataframe
parsing in one line format.

Parameters<span class="colon">:</span>  
**filename** (*str*) – Filename to parse.

Returns<span class="colon">:</span>  
\[pd.DataFrame\] containing thermo data for each completed run.

</div>

<div id="module-pymatgen.io.lammps.sets" class="section">

<span id="pymatgen-io-lammps-sets-module"></span>

## pymatgen.io.lammps.sets module<a href="#module-pymatgen.io.lammps.sets" class="headerlink"
title="Link to this heading"></a>

Input sets for LAMMPS. This InputSet and InputGenerator implementation
is based on templates and is not intended to be very flexible. For
instance, pymatgen will not detect whether a given variable should be
adapted based on others (e.g., the number of steps from the
temperature), it will not check for convergence nor will it actually run
LAMMPS. For additional flexibility and automation, use the
atomate2-lammps implementation
(<a href="https://github.com/Matgenix/atomate2-lammps"
class="reference external">https://github.com/Matgenix/atomate2-lammps</a>).

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">LammpsInputSet</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">inputfile</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.lammps.inputs.LammpsInputFile"
class="reference internal"
title="pymatgen.io.lammps.inputs.LammpsInputFile"><span
class="pre">LammpsInputFile</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">str</span></span>*, *<span class="n"><span class="pre">data</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.lammps.data.LammpsData" class="reference internal"
title="pymatgen.io.lammps.data.LammpsData"><span
class="pre">LammpsData</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="#pymatgen.io.lammps.data.CombinedData"
class="reference internal"
title="pymatgen.io.lammps.data.CombinedData"><span
class="pre">CombinedData</span></a></span>*, *<span class="n"><span class="pre">calc_type</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">''</span></span>*, *<span class="n"><span class="pre">template_file</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">''</span></span>*, *<span class="n"><span class="pre">keep_stages</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/sets.py#L31-L98"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.sets.LammpsInputSet" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="pymatgen.io.html#pymatgen.io.core.InputSet"
class="reference internal" title="pymatgen.io.core.InputSet"><span
class="pre"><code class="sourceCode python">InputSet</code></span></a>

Container class for all LAMMPS inputs. This class is intended to provide
general functionality that can be customized to many purposes.
InputGenerator classes elsewhere in this module are used to create
specific instances of LammpsInputSet that are tailored to specific
purposes.

/!This InputSet and InputGenerator implementation is based on templates
and is not intended to be very flexible. For instance, pymatgen will not
detect whether a given variable should be adapted based on others (e.g.,
the number of steps from the temperature), it will not check for
convergence nor will it actually run LAMMPS. For additional flexibility
and automation, use the atomate2-lammps implementation
(<a href="https://github.com/Matgenix/atomate2-lammps"
class="reference external">https://github.com/Matgenix/atomate2-lammps</a>).

Parameters<span class="colon">:</span>  
- **inputfile** – The input file containing settings. It can be a
  LammpsInputFile object or a string representation.

- **data** – The data file containing structure and topology
  information. It can be a LammpsData or a CombinedData object.

- **calc_type** – Human-readable string used to briefly describe the
  type of computations performed by LAMMPS.

- **template_file** – Path (string) to the template file used to create
  the input file for LAMMPS.

- **keep_stages** – Whether to keep the stage structure of the
  LammpsInputFile or not.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_directory</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">directory</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*, *<span class="n"><span class="pre">keep_stages</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/sets.py#L74-L90"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.sets.LammpsInputSet.from_directory"
class="headerlink" title="Link to this definition"></a>  
Construct a LammpsInputSet from a directory of two or more files.

TODO: accept directories with only the input file, that should include
the structure as well.

Parameters<span class="colon">:</span>  
- **directory** – Directory to read input files from. It should contain
  at least two files: in.lammps for the LAMMPS input file, and
  system.data with the system information.

- **keep_stages** – Whether to keep the stage structure of the
  LammpsInputFile or not.

<span class="sig-name descname"><span class="pre">validate</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/sets.py#L92-L98"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.sets.LammpsInputSet.validate"
class="headerlink" title="Link to this definition"></a>  
A place to implement basic checks to verify the validity of an input
set. Can be as simple or as complex as desired. Will raise a
NotImplementedError unless overloaded by the inheriting class.

</div>

<div id="module-pymatgen.io.lammps.utils" class="section">

<span id="pymatgen-io-lammps-utils-module"></span>

## pymatgen.io.lammps.utils module<a href="#module-pymatgen.io.lammps.utils" class="headerlink"
title="Link to this heading"></a>

This module defines utility classes and functions.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">LammpsRunner</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">input_filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'lammps.in'</span></span>*, *<span class="n"><span class="pre">bin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'lammps'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/utils.py#L440-L465"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.utils.LammpsRunner" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

LAMMPS wrapper.

Parameters<span class="colon">:</span>  
- **input_filename** (*str*) – input file name

- **bin** (*str*) – command to run, excluding the input file name.

<span class="sig-name descname"><span class="pre">run</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">bytes</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">bytes</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/utils.py#L459-L465"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.utils.LammpsRunner.run" class="headerlink"
title="Link to this definition"></a>  
Write the input/data files and run LAMMPS.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">PackmolRunner</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">mols</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span>*, *<span class="n"><span class="pre">param_list</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span>*, *<span class="n"><span class="pre">input_file</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'pack.inp'</span></span>*, *<span class="n"><span class="pre">tolerance</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">2.0</span></span>*, *<span class="n"><span class="pre">filetype</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'xyz'</span></span>*, *<span class="n"><span class="pre">control_params</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">auto_box</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">output_file</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'packed.xyz'</span></span>*, *<span class="n"><span class="pre">bin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'packmol'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/utils.py#L180-L437"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.utils.PackmolRunner" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Wrapper for the Packmol software that can be used to pack various types
of molecules into a one single unit.

Parameters<span class="colon">:</span>  
- **mols** – list of Molecules to pack

- **input_file** – name of the packmol input file

- **tolerance** – min distance between the atoms

- **filetype** – input/output structure file type

- **control_params** – packmol control parameters dictionary. Basically
  all parameters other than structure/atoms

- **param_list** – list of parameters containing dicts for each molecule

- **auto_box** – put the molecule assembly in a box

- **output_file** – output file name. The extension will be adjusted
  according to the filetype.

<span class="sig-name descname"><span class="pre">convert_obatoms_to_molecule</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">atoms</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span></span>*, *<span class="n"><span class="pre">residue_name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">site_property</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'ff_map'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/utils.py#L353-L403"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lammps.utils.PackmolRunner.convert_obatoms_to_molecule"
class="headerlink" title="Link to this definition"></a>  
Convert list of openbabel atoms to Molecule.

Parameters<span class="colon">:</span>  
- **atoms** (*\[OBAtom\]*) – list of OBAtom objects

- **residue_name** (*str*) – the key in self.map_residue_to_mol. Used to
  restore the site properties in the final packed molecule.

- **site_property** (*str*) – the site property to be restored.

Returns<span class="colon">:</span>  
Molecule object

<span class="sig-name descname"><span class="pre">restore_site_properties</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">site_property</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'ff_map'</span></span>*, *<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/utils.py#L405-L437"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lammps.utils.PackmolRunner.restore_site_properties"
class="headerlink" title="Link to this definition"></a>  
Restore the site properties for the final packed molecule.

Parameters<span class="colon">:</span>  
- **site_property** (*str*)

- **filename** (*str*) – path to the final packed molecule.

Returns<span class="colon">:</span>  
Molecule

<span class="sig-name descname"><span class="pre">run</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">site_property</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/utils.py#L295-L321"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.utils.PackmolRunner.run" class="headerlink"
title="Link to this definition"></a>  
Write the input file to the scratch directory, run packmol and return
the packed molecule to the current working directory.

Parameters<span class="colon">:</span>  
**site_property** (*str*) – if set then the specified site property for
the final packed molecule will be restored.

Returns<span class="colon">:</span>  
Molecule object

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">write_pdb</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">mol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">num</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/utils.py#L323-L341"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.utils.PackmolRunner.write_pdb"
class="headerlink" title="Link to this definition"></a>  
Dump the molecule into pdb file with custom residue name and number.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Polymer</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">start_monomer</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">s_head</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">s_tail</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">monomer</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">head</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">tail</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">end_monomer</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">e_head</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">e_tail</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">n_units</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">link_distance</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1.0</span></span>*, *<span class="n"><span class="pre">linear_chain</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lammps/utils.py#L39-L177"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lammps.utils.Polymer" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Generate polymer chain via Random walk. At each position there are a
total of 5 possible moves(excluding the previous direction).

Parameters<span class="colon">:</span>  
- **start_monomer**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
  class="reference internal"
  title="pymatgen.core.structure.Molecule"><em>Molecule</em></a>) –
  Starting molecule

- **s_head** (*int*) – starting atom index of the start_monomer molecule

- **s_tail** (*int*) – tail atom index of the start_monomer

- **monomer**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
  class="reference internal"
  title="pymatgen.core.structure.Molecule"><em>Molecule</em></a>) – The
  monomer

- **head** (*int*) – index of the atom in the monomer that forms the
  head

- **tail** (*int*) – tail atom index. monomers will be connected from
  tail to head

- **end_monomer**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
  class="reference internal"
  title="pymatgen.core.structure.Molecule"><em>Molecule</em></a>) –
  Terminal molecule

- **e_head** (*int*) – starting atom index of the end_monomer molecule

- **e_tail** (*int*) – tail atom index of the end_monomer

- **n_units** (*int*) – number of monomer units excluding the start and
  terminal molecules

- **link_distance** (*float*) – distance between consecutive monomers

- **linear_chain** (*bool*) – linear or random walk polymer chain.

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
