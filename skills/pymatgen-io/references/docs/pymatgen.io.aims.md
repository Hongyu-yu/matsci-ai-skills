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

- <a href="#" class="reference internal">pymatgen.io.aims package</a>
  - <a href="#subpackages" class="reference internal">Subpackages</a>
  - <a href="#submodules" class="reference internal">Submodules</a>
  - <a href="#module-pymatgen.io.aims.inputs"
    class="reference internal">pymatgen.io.aims.inputs module</a>
    - <a href="#pymatgen.io.aims.inputs.AimsControlIn"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">AimsControlIn</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsControlIn._parameters"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsControlIn._parameters</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsControlIn.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsControlIn.as_dict()</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsControlIn.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsControlIn.from_dict()</code></span></a>
      - <a
        href="#pymatgen.io.aims.inputs.AimsControlIn.get_aims_control_parameter_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsControlIn.get_aims_control_parameter_str()</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsControlIn.get_content"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsControlIn.get_content()</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsControlIn.get_species_block"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsControlIn.get_species_block()</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsControlIn.parameters"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsControlIn.parameters</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsControlIn.write_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsControlIn.write_file()</code></span></a>
    - <a href="#pymatgen.io.aims.inputs.AimsCube"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">AimsCube</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsCube.type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsCube.type</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsCube.origin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsCube.origin</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsCube.edges"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsCube.edges</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsCube.points"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsCube.points</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsCube.spin_state"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsCube.spin_state</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsCube.kpoint"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsCube.kpoint</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsCube.filename"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsCube.filename</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsCube.format"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsCube.format</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsCube.elf_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsCube.elf_type</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsCube.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsCube.as_dict()</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsCube.control_block"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsCube.control_block</code></span></a>
      - <a href="#id0" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsCube.edges</code></span></a>
      - <a href="#id1" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsCube.elf_type</code></span></a>
      - <a href="#id2" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsCube.filename</code></span></a>
      - <a href="#id3" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsCube.format</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsCube.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsCube.from_dict()</code></span></a>
      - <a href="#id4" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsCube.kpoint</code></span></a>
      - <a href="#id5" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsCube.origin</code></span></a>
      - <a href="#id6" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsCube.points</code></span></a>
      - <a href="#id7" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsCube.spin_state</code></span></a>
      - <a href="#id8" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsCube.type</code></span></a>
    - <a href="#pymatgen.io.aims.inputs.AimsGeometryIn"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">AimsGeometryIn</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsGeometryIn._content"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsGeometryIn._content</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsGeometryIn._structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsGeometryIn._structure</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsGeometryIn.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsGeometryIn.as_dict()</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsGeometryIn.content"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsGeometryIn.content</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsGeometryIn.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsGeometryIn.from_dict()</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsGeometryIn.from_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsGeometryIn.from_file()</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsGeometryIn.from_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsGeometryIn.from_str()</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsGeometryIn.from_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsGeometryIn.from_structure()</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsGeometryIn.get_header"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsGeometryIn.get_header()</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsGeometryIn.structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsGeometryIn.structure</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsGeometryIn.write_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsGeometryIn.write_file()</code></span></a>
    - <a href="#pymatgen.io.aims.inputs.AimsSpeciesFile"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">AimsSpeciesFile</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsSpeciesFile.data"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsSpeciesFile.data</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsSpeciesFile.label"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsSpeciesFile.label</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsSpeciesFile.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsSpeciesFile.as_dict()</code></span></a>
      - <a href="#id9" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsSpeciesFile.data</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsSpeciesFile.element"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsSpeciesFile.element</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsSpeciesFile.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsSpeciesFile.from_dict()</code></span></a>
      - <a
        href="#pymatgen.io.aims.inputs.AimsSpeciesFile.from_element_and_basis_name"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsSpeciesFile.from_element_and_basis_name()</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.AimsSpeciesFile.from_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsSpeciesFile.from_file()</code></span></a>
      - <a href="#id10" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsSpeciesFile.label</code></span></a>
    - <a href="#pymatgen.io.aims.inputs.SpeciesDefaults"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">SpeciesDefaults</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.SpeciesDefaults.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SpeciesDefaults.as_dict()</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.SpeciesDefaults.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SpeciesDefaults.from_dict()</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.SpeciesDefaults.from_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SpeciesDefaults.from_structure()</code></span></a>
      - <a href="#pymatgen.io.aims.inputs.SpeciesDefaults.to_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SpeciesDefaults.to_dict()</code></span></a>
  - <a href="#module-pymatgen.io.aims.outputs"
    class="reference internal">pymatgen.io.aims.outputs module</a>
    - <a href="#pymatgen.io.aims.outputs.AimsOutput"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">AimsOutput</code></span></a>
      - <a href="#pymatgen.io.aims.outputs.AimsOutput.aims_version"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutput.aims_version</code></span></a>
      - <a href="#pymatgen.io.aims.outputs.AimsOutput.all_forces"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutput.all_forces</code></span></a>
      - <a href="#pymatgen.io.aims.outputs.AimsOutput.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutput.as_dict()</code></span></a>
      - <a href="#pymatgen.io.aims.outputs.AimsOutput.band_gap"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutput.band_gap</code></span></a>
      - <a href="#pymatgen.io.aims.outputs.AimsOutput.cbm"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutput.cbm</code></span></a>
      - <a href="#pymatgen.io.aims.outputs.AimsOutput.completed"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutput.completed</code></span></a>
      - <a href="#pymatgen.io.aims.outputs.AimsOutput.direct_band_gap"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutput.direct_band_gap</code></span></a>
      - <a href="#pymatgen.io.aims.outputs.AimsOutput.fermi_energy"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutput.fermi_energy</code></span></a>
      - <a href="#pymatgen.io.aims.outputs.AimsOutput.final_energy"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutput.final_energy</code></span></a>
      - <a href="#pymatgen.io.aims.outputs.AimsOutput.final_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutput.final_structure</code></span></a>
      - <a href="#pymatgen.io.aims.outputs.AimsOutput.forces"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutput.forces</code></span></a>
      - <a href="#pymatgen.io.aims.outputs.AimsOutput.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutput.from_dict()</code></span></a>
      - <a href="#pymatgen.io.aims.outputs.AimsOutput.from_outfile"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutput.from_outfile()</code></span></a>
      - <a href="#pymatgen.io.aims.outputs.AimsOutput.from_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutput.from_str()</code></span></a>
      - <a href="#pymatgen.io.aims.outputs.AimsOutput.get_results_for_image"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutput.get_results_for_image()</code></span></a>
      - <a href="#pymatgen.io.aims.outputs.AimsOutput.initial_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutput.initial_structure</code></span></a>
      - <a href="#pymatgen.io.aims.outputs.AimsOutput.metadata"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutput.metadata</code></span></a>
      - <a href="#pymatgen.io.aims.outputs.AimsOutput.n_images"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutput.n_images</code></span></a>
      - <a href="#pymatgen.io.aims.outputs.AimsOutput.stress"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutput.stress</code></span></a>
      - <a href="#pymatgen.io.aims.outputs.AimsOutput.stresses"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutput.stresses</code></span></a>
      - <a href="#pymatgen.io.aims.outputs.AimsOutput.structure_summary"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutput.structure_summary</code></span></a>
      - <a href="#pymatgen.io.aims.outputs.AimsOutput.structures"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutput.structures</code></span></a>
      - <a href="#pymatgen.io.aims.outputs.AimsOutput.vbm"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutput.vbm</code></span></a>
  - <a href="#module-pymatgen.io.aims.parsers"
    class="reference internal">pymatgen.io.aims.parsers module</a>
    - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">AimsOutCalcChunk</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.E_f"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.E_f</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.cbm"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.cbm</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.converged"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.converged</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.coords"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.coords</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.dielectric_tensor"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.dielectric_tensor</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.dipole"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.dipole</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.direct_gap"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.direct_gap</code></span></a>
      - <a
        href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.electronic_temperature"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.electronic_temperature</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.energy"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.energy</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.forces"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.forces</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.free_energy"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.free_energy</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.gap"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.gap</code></span></a>
      - <a
        href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.hirshfeld_atomic_dipoles"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.hirshfeld_atomic_dipoles</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.hirshfeld_charges"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.hirshfeld_charges</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.hirshfeld_dipole"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.hirshfeld_dipole</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.hirshfeld_volumes"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.hirshfeld_volumes</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.initial_lattice"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.initial_lattice</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.initial_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.initial_structure</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.is_metallic"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.is_metallic</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.k_point_weights"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.k_point_weights</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.k_points"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.k_points</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.lattice"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.lattice</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.magmom"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.magmom</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.mulliken_charges"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.mulliken_charges</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.mulliken_spins"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.mulliken_spins</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.n_atoms"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.n_atoms</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.n_bands"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.n_bands</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.n_electrons"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.n_electrons</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.n_iter"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.n_iter</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.n_k_points"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.n_k_points</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.n_spins"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.n_spins</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.polarization"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.polarization</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.results"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.results</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.species"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.species</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.stress"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.stress</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.stresses"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.stresses</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.structure</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.vbm"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.vbm</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.velocities"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutCalcChunk.velocities</code></span></a>
    - <a href="#pymatgen.io.aims.parsers.AimsOutChunk"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">AimsOutChunk</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutChunk.lines"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutChunk.lines</code></span></a>
      - <a href="#id11" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutChunk.lines</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutChunk.parse_scalar"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutChunk.parse_scalar()</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutChunk.reverse_search_for"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutChunk.reverse_search_for()</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutChunk.search_for_all"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutChunk.search_for_all()</code></span></a>
    - <a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">AimsOutHeaderChunk</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.aims_uuid"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutHeaderChunk.aims_uuid</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.build_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutHeaderChunk.build_type</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.c_compiler"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutHeaderChunk.c_compiler</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.c_compiler_flags"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutHeaderChunk.c_compiler_flags</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.commit_hash"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutHeaderChunk.commit_hash</code></span></a>
      - <a
        href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.electronic_temperature"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutHeaderChunk.electronic_temperature</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.fortran_compiler"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutHeaderChunk.fortran_compiler</code></span></a>
      - <a
        href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.fortran_compiler_flags"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutHeaderChunk.fortran_compiler_flags</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.header_summary"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutHeaderChunk.header_summary</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.initial_charges"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutHeaderChunk.initial_charges</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.initial_lattice"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutHeaderChunk.initial_lattice</code></span></a>
      - <a
        href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.initial_magnetic_moments"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutHeaderChunk.initial_magnetic_moments</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.initial_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutHeaderChunk.initial_structure</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.is_md"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutHeaderChunk.is_md</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.is_relaxation"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutHeaderChunk.is_relaxation</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.k_point_weights"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutHeaderChunk.k_point_weights</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.k_points"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutHeaderChunk.k_points</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.lines"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutHeaderChunk.lines</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.linked_against"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutHeaderChunk.linked_against</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.metadata_summary"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutHeaderChunk.metadata_summary</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.n_atoms"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutHeaderChunk.n_atoms</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.n_bands"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutHeaderChunk.n_bands</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.n_electrons"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutHeaderChunk.n_electrons</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.n_k_points"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutHeaderChunk.n_k_points</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.n_spins"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutHeaderChunk.n_spins</code></span></a>
      - <a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.version_number"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsOutHeaderChunk.version_number</code></span></a>
    - <a href="#pymatgen.io.aims.parsers.AimsParseError"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">AimsParseError</code></span></a>
    - <a href="#pymatgen.io.aims.parsers.ParseError"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">ParseError</code></span></a>
    - <a href="#pymatgen.io.aims.parsers.check_convergence"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">check_convergence()</code></span></a>
    - <a href="#pymatgen.io.aims.parsers.get_aims_out_chunks"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">get_aims_out_chunks()</code></span></a>
    - <a href="#pymatgen.io.aims.parsers.get_header_chunk"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">get_header_chunk()</code></span></a>
    - <a href="#pymatgen.io.aims.parsers.get_lines"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">get_lines()</code></span></a>
    - <a href="#pymatgen.io.aims.parsers.read_aims_header_info"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">read_aims_header_info()</code></span></a>
    - <a href="#pymatgen.io.aims.parsers.read_aims_header_info_from_content"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">read_aims_header_info_from_content()</code></span></a>
    - <a href="#pymatgen.io.aims.parsers.read_aims_output"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">read_aims_output()</code></span></a>
    - <a href="#pymatgen.io.aims.parsers.read_aims_output_from_content"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">read_aims_output_from_content()</code></span></a>

</div>

</div>

</div>

<div class="section wy-nav-content-wrap" toggle="wy-nav-shift">

[pymatgen](index.html)

<div class="wy-nav-content">

<div class="rst-content style-external-links">

<div role="navigation" aria-label="Page navigation">

- <a href="index.html" class="icon icon-home" aria-label="Home"></a>
- pymatgen.io.aims package
- <a
  href="https://github.com/materialsproject/pymatgen/blob/master/docs_rst/pymatgen.io.aims.rst"
  class="fa fa-github">Edit on GitHub</a>

------------------------------------------------------------------------

</div>

<div class="document" role="main" itemscope="itemscope"
itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="module-pymatgen.io.aims" class="section">

<span id="pymatgen-io-aims-package"></span>

# pymatgen.io.aims package<a href="#module-pymatgen.io.aims" class="headerlink"
title="Link to this heading"></a>

IO interface for FHI-aims.

<div id="subpackages" class="section">

## Subpackages<a href="#subpackages" class="headerlink"
title="Link to this heading"></a>

<div class="toctree-wrapper compound">

- <a href="pymatgen.io.aims.sets.html"
  class="reference internal">pymatgen.io.aims.sets package</a>
  - <a href="pymatgen.io.aims.sets.html#submodules"
    class="reference internal">Submodules</a>
  - <a href="pymatgen.io.aims.sets.html#module-pymatgen.io.aims.sets.base"
    class="reference internal">pymatgen.io.aims.sets.base module</a>
    - <a
      href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.base.AimsInputGenerator"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">AimsInputGenerator</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.base.AimsInputGenerator.user_params"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputGenerator.user_params</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.base.AimsInputGenerator.user_kpoints_settings"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputGenerator.user_kpoints_settings</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.base.AimsInputGenerator.use_structure_charge"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputGenerator.use_structure_charge</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.base.AimsInputGenerator.d2k"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputGenerator.d2k()</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.base.AimsInputGenerator.d2k_recip_cell"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputGenerator.d2k_recip_cell()</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.base.AimsInputGenerator.get_input_set"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputGenerator.get_input_set()</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.base.AimsInputGenerator.get_parameter_updates"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputGenerator.get_parameter_updates()</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.base.AimsInputGenerator.k2d"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputGenerator.k2d()</code></span></a>
      - <a href="pymatgen.io.aims.sets.html#id0"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputGenerator.use_structure_charge</code></span></a>
      - <a href="pymatgen.io.aims.sets.html#id1"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputGenerator.user_kpoints_settings</code></span></a>
      - <a href="pymatgen.io.aims.sets.html#id2"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputGenerator.user_params</code></span></a>
    - <a
      href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.base.AimsInputSet"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">AimsInputSet</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.base.AimsInputSet.control_in"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputSet.control_in</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.base.AimsInputSet.geometry_in"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputSet.geometry_in</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.base.AimsInputSet.get_input_files"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputSet.get_input_files()</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.base.AimsInputSet.params_json"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputSet.params_json</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.base.AimsInputSet.remove_parameters"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputSet.remove_parameters()</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.base.AimsInputSet.set_parameters"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputSet.set_parameters()</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.base.AimsInputSet.set_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AimsInputSet.set_structure()</code></span></a>
    - <a
      href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.base.recursive_update"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">recursive_update()</code></span></a>
  - <a href="pymatgen.io.aims.sets.html#module-pymatgen.io.aims.sets.bs"
    class="reference internal">pymatgen.io.aims.sets.bs module</a>
    - <a
      href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.bs.BandStructureSetGenerator"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">BandStructureSetGenerator</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.bs.BandStructureSetGenerator.calc_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructureSetGenerator.calc_type</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.bs.BandStructureSetGenerator.k_point_density"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructureSetGenerator.k_point_density</code></span></a>
      - <a href="pymatgen.io.aims.sets.html#id3"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructureSetGenerator.calc_type</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.bs.BandStructureSetGenerator.get_parameter_updates"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructureSetGenerator.get_parameter_updates()</code></span></a>
      - <a href="pymatgen.io.aims.sets.html#id4"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructureSetGenerator.k_point_density</code></span></a>
    - <a
      href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.bs.GWSetGenerator"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">GWSetGenerator</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.bs.GWSetGenerator.calc_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GWSetGenerator.calc_type</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.bs.GWSetGenerator.k_point_density"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GWSetGenerator.k_point_density</code></span></a>
      - <a href="pymatgen.io.aims.sets.html#id5"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GWSetGenerator.calc_type</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.bs.GWSetGenerator.get_parameter_updates"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GWSetGenerator.get_parameter_updates()</code></span></a>
      - <a href="pymatgen.io.aims.sets.html#id6"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GWSetGenerator.k_point_density</code></span></a>
    - <a
      href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.bs.prepare_band_input"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">prepare_band_input()</code></span></a>
  - <a href="pymatgen.io.aims.sets.html#module-pymatgen.io.aims.sets.core"
    class="reference internal">pymatgen.io.aims.sets.core module</a>
    - <a
      href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.core.MDSetGenerator"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">MDSetGenerator</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.core.MDSetGenerator.calc_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MDSetGenerator.calc_type</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.core.MDSetGenerator.ensemble"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MDSetGenerator.ensemble</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.core.MDSetGenerator.ensemble_specs"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MDSetGenerator.ensemble_specs</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.core.MDSetGenerator.get_parameter_updates"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MDSetGenerator.get_parameter_updates()</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.core.MDSetGenerator.init_velocities"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MDSetGenerator.init_velocities</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.core.MDSetGenerator.temp"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MDSetGenerator.temp</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.core.MDSetGenerator.time"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MDSetGenerator.time</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.core.MDSetGenerator.time_step"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MDSetGenerator.time_step</code></span></a>
    - <a
      href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.core.RelaxSetGenerator"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">RelaxSetGenerator</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.core.RelaxSetGenerator.calc_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RelaxSetGenerator.calc_type</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.core.RelaxSetGenerator.relax_cell"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RelaxSetGenerator.relax_cell</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.core.RelaxSetGenerator.max_force"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RelaxSetGenerator.max_force</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.core.RelaxSetGenerator.method"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RelaxSetGenerator.method</code></span></a>
      - <a href="pymatgen.io.aims.sets.html#id7"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RelaxSetGenerator.calc_type</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.core.RelaxSetGenerator.get_parameter_updates"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RelaxSetGenerator.get_parameter_updates()</code></span></a>
      - <a href="pymatgen.io.aims.sets.html#id8"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RelaxSetGenerator.max_force</code></span></a>
      - <a href="pymatgen.io.aims.sets.html#id9"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RelaxSetGenerator.method</code></span></a>
      - <a href="pymatgen.io.aims.sets.html#id10"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RelaxSetGenerator.relax_cell</code></span></a>
    - <a
      href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.core.SocketIOSetGenerator"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">SocketIOSetGenerator</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.core.SocketIOSetGenerator.calc_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SocketIOSetGenerator.calc_type</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.core.SocketIOSetGenerator.host"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SocketIOSetGenerator.host</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.core.SocketIOSetGenerator.port"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SocketIOSetGenerator.port</code></span></a>
      - <a href="pymatgen.io.aims.sets.html#id11"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SocketIOSetGenerator.calc_type</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.core.SocketIOSetGenerator.get_parameter_updates"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SocketIOSetGenerator.get_parameter_updates()</code></span></a>
      - <a href="pymatgen.io.aims.sets.html#id12"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SocketIOSetGenerator.host</code></span></a>
      - <a href="pymatgen.io.aims.sets.html#id13"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SocketIOSetGenerator.port</code></span></a>
    - <a
      href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.core.StaticSetGenerator"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">StaticSetGenerator</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.core.StaticSetGenerator.calc_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">StaticSetGenerator.calc_type</code></span></a>
      - <a href="pymatgen.io.aims.sets.html#id14"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">StaticSetGenerator.calc_type</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.core.StaticSetGenerator.get_parameter_updates"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">StaticSetGenerator.get_parameter_updates()</code></span></a>
  - <a
    href="pymatgen.io.aims.sets.html#module-pymatgen.io.aims.sets.magnetism"
    class="reference internal">pymatgen.io.aims.sets.magnetism module</a>
    - <a
      href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.magnetism.MagneticRelaxSetGenerator"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">MagneticRelaxSetGenerator</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.magnetism.MagneticRelaxSetGenerator.calc_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MagneticRelaxSetGenerator.calc_type</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.magnetism.MagneticRelaxSetGenerator.relax_cell"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MagneticRelaxSetGenerator.relax_cell</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.magnetism.MagneticRelaxSetGenerator.max_force"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MagneticRelaxSetGenerator.max_force</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.magnetism.MagneticRelaxSetGenerator.method"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MagneticRelaxSetGenerator.method</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.magnetism.MagneticRelaxSetGenerator.get_parameter_updates"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MagneticRelaxSetGenerator.get_parameter_updates()</code></span></a>
    - <a
      href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.magnetism.MagneticStaticSetGenerator"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">MagneticStaticSetGenerator</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.magnetism.MagneticStaticSetGenerator.calc_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MagneticStaticSetGenerator.calc_type</code></span></a>
      - <a href="pymatgen.io.aims.sets.html#id15"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MagneticStaticSetGenerator.calc_type</code></span></a>
      - <a
        href="pymatgen.io.aims.sets.html#pymatgen.io.aims.sets.magnetism.MagneticStaticSetGenerator.get_parameter_updates"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MagneticStaticSetGenerator.get_parameter_updates()</code></span></a>

</div>

</div>

<div id="submodules" class="section">

## Submodules<a href="#submodules" class="headerlink"
title="Link to this heading"></a>

</div>

<div id="module-pymatgen.io.aims.inputs" class="section">

<span id="pymatgen-io-aims-inputs-module"></span>

## pymatgen.io.aims.inputs module<a href="#module-pymatgen.io.aims.inputs" class="headerlink"
title="Link to this heading"></a>

Classes for reading/manipulating/writing FHI-aims input files.

Works for aims cube objects, geometry.in and control.in

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">AimsControlIn</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">\_parameters:</span> <span class="pre">dict\[str</span></span>*, *<span class="n"><span class="pre">Any\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/inputs.py#L449-L735"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsControlIn" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

An FHI-aims control.in file.

<span class="sig-name descname"><span class="pre">\_parameters</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsControlIn._parameters"
class="headerlink" title="Link to this definition"></a>  
The parameters dictionary containing all input flags (key) and values
for the control.in file

Type<span class="colon">:</span>  
dict\[str, Any\]

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/inputs.py#L715-L721"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsControlIn.as_dict"
class="headerlink" title="Link to this definition"></a>  
Get a dictionary representation of the geometry.in file.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/inputs.py#L723-L735"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsControlIn.from_dict"
class="headerlink" title="Link to this definition"></a>  
Initialize from dictionary.

Parameters<span class="colon">:</span>  
**dct** (*dict\[str,* *Any\]*) – The MontyEncoded dictionary

Returns<span class="colon">:</span>  
The AimsControlIn for dct

<span class="sig-name descname"><span class="pre">get_aims_control_parameter_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">key</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span></span>*, *<span class="n"><span class="pre">fmt</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/inputs.py#L524-L537"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.aims.inputs.AimsControlIn.get_aims_control_parameter_str"
class="headerlink" title="Link to this definition"></a>  
Get the string needed to add a parameter to the control.in file.

Parameters<span class="colon">:</span>  
- **key** (*str*) – The name of the input flag

- **value** (*Any*) – The value to be set for the flag

- **fmt** (*str*) – The format string to apply to the value

Returns<span class="colon">:</span>  
The line to add to the control.in file

Return type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">get_content</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">verbose_header</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">directory</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Path</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/inputs.py#L539-L646"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsControlIn.get_content"
class="headerlink" title="Link to this definition"></a>  
Get the content of the file.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a> *\|*
  <a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
  class="reference internal"
  title="pymatgen.core.structure.Molecule"><em>Molecule</em></a>) – The
  structure to write the input file for

- **verbose_header** (*bool*) – If True print the input option
  dictionary

- **directory** – str \| Path \| None = The directory for the
  calculation,

Returns<span class="colon">:</span>  
The content of the file for a given structure

Return type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">get_species_block</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">basis_set</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">species_dir</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Path</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/inputs.py#L690-L713"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsControlIn.get_species_block"
class="headerlink" title="Link to this definition"></a>  
Get the basis set information for a structure

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
  class="reference internal"
  title="pymatgen.core.structure.Molecule"><em>Molecule</em></a> *or*
  <a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  The structure to get the basis set information for

- **basis_set** (*str* *\|* *dict\[str,* *str\]*) – a name of a basis
  set (light, tight…) or a mapping from site labels to basis set names.
  The name of a basis set can either correspond to the subfolder in
  defaults_2020 folder or be a full path from the
  FHI-aims/species_defaults directory.

- **species_dir** (*str* *\|* *Path* *\|* *None*) – The base species
  directory

Returns<span class="colon">:</span>  
The block to add to the control.in file for the species

Raises<span class="colon">:</span>  
**ValueError** – If a file for the species is not found

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">parameters</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsControlIn.parameters"
class="headerlink" title="Link to this definition"></a>  
The dictionary of input parameters for control.in.

<span class="sig-name descname"><span class="pre">write_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">directory</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Path</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">verbose_header</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">overwrite</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/inputs.py#L648-L688"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsControlIn.write_file"
class="headerlink" title="Link to this definition"></a>  
Write the control.in file.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a> *\|*
  <a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
  class="reference internal"
  title="pymatgen.core.structure.Molecule"><em>Molecule</em></a>) – The
  structure to write the input file for

- **directory** (*str* *or* *Path*) – The directory to write the
  control.in file. If None use cwd

- **verbose_header** (*bool*) – If True print the input option
  dictionary

- **overwrite** (*bool*) – If True allow to overwrite existing files

Raises<span class="colon">:</span>  
- **ValueError** – If a file must be overwritten and overwrite is False

- **ValueError** – If k-grid is not provided for the periodic structures

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">AimsCube</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">type:</span> <span class="pre">str</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">origin:</span> <span class="pre">Sequence\[float\]</span> <span class="pre">\|</span> <span class="pre">tuple\[float</span></span>*, *<span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">float\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">edges:</span> <span class="pre">Sequence\[Sequence\[float\]\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">points:</span> <span class="pre">Sequence\[int\]</span> <span class="pre">\|</span> <span class="pre">tuple\[int</span></span>*, *<span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">int\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">format:</span> <span class="pre">str</span> <span class="pre">=</span> <span class="pre">'cube'</span></span>*, *<span class="n"><span class="pre">spin_state:</span> <span class="pre">int</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">kpoint:</span> <span class="pre">int</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">filename:</span> <span class="pre">str</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">elf_type:</span> <span class="pre">int</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/inputs.py#L282-L446"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsCube" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

The FHI-aims cubes.

<span class="sig-name descname"><span class="pre">type</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsCube.type" class="headerlink"
title="Link to this definition"></a>  
The value to be outputted as a cube file

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">origin</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsCube.origin" class="headerlink"
title="Link to this definition"></a>  
The origin of the cube

Type<span class="colon">:</span>  
Sequence\[float\] or tuple\[float, float, float\]

<span class="sig-name descname"><span class="pre">edges</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsCube.edges" class="headerlink"
title="Link to this definition"></a>  
Specifies the edges of a cube: dx, dy, dz dx (float): The length of the
step in the x direction dy (float): The length of the step in the y
direction dx (float): The length of the step in the x direction

Type<span class="colon">:</span>  
Sequence\[Sequence\[float\]\]

<span class="sig-name descname"><span class="pre">points</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsCube.points" class="headerlink"
title="Link to this definition"></a>  
The number of points along each edge

Type<span class="colon">:</span>  
Sequence\[int\] or tuple\[int, int, int\]

<span class="sig-name descname"><span class="pre">spin_state</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsCube.spin_state"
class="headerlink" title="Link to this definition"></a>  
The spin-channel to use either 1 or 2

Type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">kpoint</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsCube.kpoint" class="headerlink"
title="Link to this definition"></a>  
The k-point to use (the index of the list printed from output
k_point_list)

Type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">filename</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsCube.filename" class="headerlink"
title="Link to this definition"></a>  
The filename to use

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">format</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsCube.format" class="headerlink"
title="Link to this definition"></a>  
The format to output the cube file in: cube, gOpenMol, or xsf

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">elf_type</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsCube.elf_type" class="headerlink"
title="Link to this definition"></a>  
The type of electron localization function to use ( see FHI-aims manual)

Type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/inputs.py#L407-L421"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsCube.as_dict" class="headerlink"
title="Link to this definition"></a>  
Get a dictionary representation of the geometry.in file.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">control_block</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsCube.control_block"
class="headerlink" title="Link to this definition"></a>  
The block of text for the control.in file of the Cube.

<span class="sig-name descname"><span class="pre">edges</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id0" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">elf_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id1" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">filename</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id2" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">format</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'cube'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id3" class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/inputs.py#L423-L446"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsCube.from_dict" class="headerlink"
title="Link to this definition"></a>  
Initialize from dictionary.

Parameters<span class="colon">:</span>  
**dct** (*dict\[str,* *Any\]*) – The MontyEncoded dictionary

Returns<span class="colon">:</span>  
AimsCube

<span class="sig-name descname"><span class="pre">kpoint</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id4" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">origin</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id5" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">points</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id6" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">spin_state</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id7" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id8" class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">AimsGeometryIn</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">\_content</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">\_structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/inputs.py#L41-L250"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsGeometryIn" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Representation of an aims geometry.in file.

<span class="sig-name descname"><span class="pre">\_content</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsGeometryIn._content"
class="headerlink" title="Link to this definition"></a>  
The content of the input file

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">\_structure</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsGeometryIn._structure"
class="headerlink" title="Link to this definition"></a>  
The structure or molecule representation of the file

Type<span class="colon">:</span>  
<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure">Structure</a> \|
<a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule">Molecule</a>

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/inputs.py#L229-L236"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsGeometryIn.as_dict"
class="headerlink" title="Link to this definition"></a>  
Get a dictionary representation of the geometry.in file.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">content</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsGeometryIn.content"
class="headerlink" title="Link to this definition"></a>  
Access the contents of the file.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/inputs.py#L238-L250"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsGeometryIn.from_dict"
class="headerlink" title="Link to this definition"></a>  
Initialize from dictionary.

Parameters<span class="colon">:</span>  
**dct** (*dict\[str,* *Any\]*) – The MontyEncoded dictionary of the
AimsGeometryIn object

Returns<span class="colon">:</span>  
The input object represented by the dict

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filepath</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Path</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/inputs.py#L128-L140"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsGeometryIn.from_file"
class="headerlink" title="Link to this definition"></a>  
Create an AimsGeometryIn from an input file.

Parameters<span class="colon">:</span>  
**filepath** (*str* *\|* *Path*) – The path to the input file (either
plain text of gzipped)

Returns<span class="colon">:</span>  
The input object represented in the file

Return type<span class="colon">:</span>  
<a href="#pymatgen.io.aims.inputs.AimsGeometryIn"
class="reference internal"
title="pymatgen.io.aims.inputs.AimsGeometryIn">AimsGeometryIn</a>

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">contents</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/inputs.py#L54-L126"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsGeometryIn.from_str"
class="headerlink" title="Link to this definition"></a>  
Create an input from the content of an input file.

Parameters<span class="colon">:</span>  
**contents** (*str*) – The content of the file

Returns<span class="colon">:</span>  
The AimsGeometryIn file for the string contents

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_structure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.IStructure"
class="reference internal"
title="pymatgen.core.structure.IStructure"><span
class="pre">IStructure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/inputs.py#L142-L183"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsGeometryIn.from_structure"
class="headerlink" title="Link to this definition"></a>  
Construct an input file from an input structure.

Parameters<span class="colon">:</span>  
**structure**
(<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><em>Structure</em></a> *\|*
<a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><em>Molecule</em></a>) – The
structure for the file

Returns<span class="colon">:</span>  
The input object for the structure

Return type<span class="colon">:</span>  
<a href="#pymatgen.io.aims.inputs.AimsGeometryIn"
class="reference internal"
title="pymatgen.io.aims.inputs.AimsGeometryIn">AimsGeometryIn</a>

<span class="sig-name descname"><span class="pre">get_header</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/inputs.py#L195-L209"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsGeometryIn.get_header"
class="headerlink" title="Link to this definition"></a>  
A header of geometry.in file

Parameters<span class="colon">:</span>  
**filename** (*str*) – A name of the file for the header

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">structure</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsGeometryIn.structure"
class="headerlink" title="Link to this definition"></a>  
Access structure for the file.

<span class="sig-name descname"><span class="pre">write_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">directory</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Path</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">overwrite</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/inputs.py#L211-L227"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsGeometryIn.write_file"
class="headerlink" title="Link to this definition"></a>  
Write the geometry.in file.

Parameters<span class="colon">:</span>  
- **directory** (*str* *\|* *Path* *\|* *None*) – The directory to write
  the geometry.in file

- **overwrite** (*bool*) – If True allow to overwrite existing files

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">AimsSpeciesFile</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">data</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">''</span></span>*, *<span class="n"><span class="pre">label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/inputs.py#L738-L849"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsSpeciesFile" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

An FHI-aims single species’ defaults file.

<span class="sig-name descname"><span class="pre">data</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsSpeciesFile.data"
class="headerlink" title="Link to this definition"></a>  
A string of the complete species defaults file

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">label</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsSpeciesFile.label"
class="headerlink" title="Link to this definition"></a>  
A string representing the name of species

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/inputs.py#L837-L844"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsSpeciesFile.as_dict"
class="headerlink" title="Link to this definition"></a>  
Dictionary representation of the species’ defaults file.

<span class="sig-name descname"><span class="pre">data</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">''</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id9" class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">element</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsSpeciesFile.element"
class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/inputs.py#L846-L849"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsSpeciesFile.from_dict"
class="headerlink" title="Link to this definition"></a>  
Deserialization of the AimsSpeciesFile object

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_element_and_basis_name</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">element</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">basis</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="keyword-only-separator o"><span class="pre">\*</span></span>*, *<span class="n"><span class="pre">species_dir</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Path</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/inputs.py#L771-L820"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.aims.inputs.AimsSpeciesFile.from_element_and_basis_name"
class="headerlink" title="Link to this definition"></a>  
Initialize from element and basis names.

Parameters<span class="colon">:</span>  
- **element** (*str*) – the element name (not to confuse with the
  species)

- **basis** (*str*) – the directory in which the species’ defaults file
  is located relative to the root species_defaults (or
  species_defaults/defaults_2020) directory.\`.

- **label** (*str*) – A string representing the name of species. If not
  specified, then equal to element

Returns<span class="colon">:</span>  
AimsSpeciesFile

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/inputs.py#L757-L769"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.AimsSpeciesFile.from_file"
class="headerlink" title="Link to this definition"></a>  
Initialize from file.

Parameters<span class="colon">:</span>  
- **filename** (*str*) – The filename of the species’ defaults file

- **label** (*str*) – A string representing the name of species

Returns<span class="colon">:</span>  
AimsSpeciesFile

<span class="sig-name descname"><span class="pre">label</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id10" class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">SpeciesDefaults</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">labels</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">basis_set</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="keyword-only-separator o"><span class="pre">\*</span></span>*, *<span class="n"><span class="pre">species_dir</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Path</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">elements</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/inputs.py#L852-L944"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.SpeciesDefaults" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`list`</span>, <span
class="pre">`MSONable`</span>

A list containing a set of species’ defaults objects with methods to
read and write them to files

Parameters<span class="colon">:</span>  
- **labels** (*list\[str\]*) – a list of labels, for which to build
  species’ defaults

- **basis_set** (*str* *\|* *dict\[str,* *str\]*) – a name of a basis
  set (light, tight…) or a mapping from site labels to basis set names.
  The name of a basis set can either correspond to the subfolder in
  defaults_2020 folder or be a full path from the
  FHI-aims/species_defaults directory.

- **species_dir** (*str* *\|* *Path* *\|* *None*) – The base species
  directory

- **elements** (*dict\[str,* *str\]* *\|* *None*) – a mapping from site
  labels to elements. If some label is not in this mapping, it coincides
  with an element.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/inputs.py#L927-L935"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.SpeciesDefaults.as_dict"
class="headerlink" title="Link to this definition"></a>  
Dictionary representation of the species’ defaults

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.aims.inputs.SpeciesDefaults"
class="reference internal"
title="pymatgen.io.aims.inputs.SpeciesDefaults"><span
class="pre">SpeciesDefaults</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/inputs.py#L941-L944"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.SpeciesDefaults.from_dict"
class="headerlink" title="Link to this definition"></a>  
Deserialization of the SpeciesDefaults object

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_structure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">struct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">basis_set</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">species_dir</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Path</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/inputs.py#L910-L925"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.SpeciesDefaults.from_structure"
class="headerlink" title="Link to this definition"></a>  
Initialize species defaults from a structure.

<span class="sig-name descname"><span class="pre">to_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../../../.venv/lib/python3.11/site-packages/monty/dev.py#L937-L939"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.inputs.SpeciesDefaults.to_dict"
class="headerlink" title="Link to this definition"></a>  

</div>

<div id="module-pymatgen.io.aims.outputs" class="section">

<span id="pymatgen-io-aims-outputs-module"></span>

## pymatgen.io.aims.outputs module<a href="#module-pymatgen.io.aims.outputs" class="headerlink"
title="Link to this heading"></a>

A representation of FHI-aims output (based on ASE output parser).

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">AimsOutput</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">results</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">metadata</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">structure_summary</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/outputs.py#L32-L227"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.outputs.AimsOutput" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

The main output file for FHI-aims.

Parameters<span class="colon">:</span>  
- **results**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
  class="reference internal"
  title="pymatgen.core.structure.Molecule"><em>Molecule</em></a> *or*
  <a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a> *or*
  *Sequence\[*<a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
  class="reference internal"
  title="pymatgen.core.structure.Molecule"><em>Molecule</em></a> *or*
  <a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>*\]*)
  – A list of all images in an output file

- **metadata** (*Dict\[str,* *Any\]*) – The metadata of the executable
  used to perform the calculation

- **structure_summary** (*Dict\[str,* *Any\]*) – The summary of the
  starting atomic structure.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">aims_version</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.outputs.AimsOutput.aims_version"
class="headerlink" title="Link to this definition"></a>  
The version of FHI-aims used for the calculation.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">all_forces</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.outputs.AimsOutput.all_forces"
class="headerlink" title="Link to this definition"></a>  
The forces for all images in the calculation.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/outputs.py#L54-L64"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.outputs.AimsOutput.as_dict"
class="headerlink" title="Link to this definition"></a>  
Create a dict representation of the outputs for MSONable.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">band_gap</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.outputs.AimsOutput.band_gap"
class="headerlink" title="Link to this definition"></a>  
The band gap for the final structure in the calculation.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">cbm</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.outputs.AimsOutput.cbm" class="headerlink"
title="Link to this definition"></a>  
The LUMO level for the final structure in the calculation.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">completed</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.outputs.AimsOutput.completed"
class="headerlink" title="Link to this definition"></a>  
Did the calculation complete.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">direct_band_gap</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.outputs.AimsOutput.direct_band_gap"
class="headerlink" title="Link to this definition"></a>  
The direct band gap for the final structure in the calculation.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">fermi_energy</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.outputs.AimsOutput.fermi_energy"
class="headerlink" title="Link to this definition"></a>  
The Fermi energy for the final structure in the calculation.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">final_energy</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.outputs.AimsOutput.final_energy"
class="headerlink" title="Link to this definition"></a>  
The total energy for the final structure in the calculation.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">final_structure</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.outputs.AimsOutput.final_structure"
class="headerlink" title="Link to this definition"></a>  
The final structure for the calculation.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">forces</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.outputs.AimsOutput.forces" class="headerlink"
title="Link to this definition"></a>  
The forces for the final image of the calculation.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/outputs.py#L96-L114"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.outputs.AimsOutput.from_dict"
class="headerlink" title="Link to this definition"></a>  
Construct an AimsOutput from a dictionary.

Parameters<span class="colon">:</span>  
**dct** (*dict\[str,* *Any\]*) – The dictionary used to create
AimsOutput

Returns<span class="colon">:</span>  
AimsOutput

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_outfile</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">outfile</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Path</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/outputs.py#L66-L79"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.outputs.AimsOutput.from_outfile"
class="headerlink" title="Link to this definition"></a>  
Construct an AimsOutput from an output file.

Parameters<span class="colon">:</span>  
**outfile** – str \| Path: The aims.out file to parse

Returns<span class="colon">:</span>  
The AimsOutput object for the output file

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">content</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/outputs.py#L81-L94"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.outputs.AimsOutput.from_str"
class="headerlink" title="Link to this definition"></a>  
Construct an AimsOutput from an output file.

Parameters<span class="colon">:</span>  
**content** (*str*) – The content of the aims.out file

Returns<span class="colon">:</span>  
The AimsOutput for the output file content

<span class="sig-name descname"><span class="pre">get_results_for_image</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">image_ind</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/outputs.py#L116-L125"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.outputs.AimsOutput.get_results_for_image"
class="headerlink" title="Link to this definition"></a>  
Get the results dictionary for a particular image or slice of images.

Parameters<span class="colon">:</span>  
**image_ind** (*int*) – The index of the image to get the results for

Returns<span class="colon">:</span>  
The results of the image with index images_ind

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">initial_structure</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.outputs.AimsOutput.initial_structure"
class="headerlink" title="Link to this definition"></a>  
The initial structure for the calculations.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">metadata</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.outputs.AimsOutput.metadata"
class="headerlink" title="Link to this definition"></a>  
The system metadata.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">n_images</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.outputs.AimsOutput.n_images"
class="headerlink" title="Link to this definition"></a>  
The number of images in results.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">stress</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ndarray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.outputs.AimsOutput.stress" class="headerlink"
title="Link to this definition"></a>  
The stress for the final image of the calculation.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">stresses</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.outputs.AimsOutput.stresses"
class="headerlink" title="Link to this definition"></a>  
The atomic virial stresses for the final image of the calculation.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">structure_summary</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.outputs.AimsOutput.structure_summary"
class="headerlink" title="Link to this definition"></a>  
The summary of the material/molecule that the calculations represent.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">structures</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.outputs.AimsOutput.structures"
class="headerlink" title="Link to this definition"></a>  
All images in the output file.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">vbm</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.outputs.AimsOutput.vbm" class="headerlink"
title="Link to this definition"></a>  
The HOMO level for the final structure in the calculation.

</div>

<div id="module-pymatgen.io.aims.parsers" class="section">

<span id="pymatgen-io-aims-parsers-module"></span>

## pymatgen.io.aims.parsers module<a href="#module-pymatgen.io.aims.parsers" class="headerlink"
title="Link to this heading"></a>

AIMS output parser, taken from ASE with modifications.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">AimsOutCalcChunk</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">lines</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">header</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk"
class="reference internal"
title="pymatgen.io.aims.parsers.AimsOutHeaderChunk"><span
class="pre">AimsOutHeaderChunk</span></a></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/parsers.py#L451-L989"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.aims.parsers.AimsOutChunk"
class="reference internal"
title="pymatgen.io.aims.parsers.AimsOutChunk"><span class="pre"><code
class="sourceCode python">AimsOutChunk</code></span></a>

A part of the aims.out file corresponding to a single structure.

Construct the AimsOutCalcChunk.

Parameters<span class="colon">:</span>  
- **lines** (*list\[str\]*) – The lines used for the structure

- **header** (*.AimsOutHeaderChunk*) – A summary of the relevant
  information from the aims.out header

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">E_f</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.E_f"
class="headerlink" title="Link to this definition"></a>  
The Fermi energy.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">cbm</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.cbm"
class="headerlink" title="Link to this definition"></a>  
The conduction band minimnum.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">converged</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.converged"
class="headerlink" title="Link to this definition"></a>  
True if the calculation is converged.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">coords</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.coords"
class="headerlink" title="Link to this definition"></a>  
The cartesian coordinates of the atoms.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">dielectric_tensor</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.dielectric_tensor"
class="headerlink" title="Link to this definition"></a>  
The dielectric tensor from the aims.out file.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">dipole</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.dipole"
class="headerlink" title="Link to this definition"></a>  
The electric dipole moment from the aims.out file.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">direct_gap</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.direct_gap"
class="headerlink" title="Link to this definition"></a>  
The direct bandgap.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">electronic_temperature</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.electronic_temperature"
class="headerlink" title="Link to this definition"></a>  
The electronic temperature for the chunk.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">energy</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.energy"
class="headerlink" title="Link to this definition"></a>  
The energy from the aims.out file.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">forces</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.forces"
class="headerlink" title="Link to this definition"></a>  
The forces from the aims.out file.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">free_energy</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.free_energy"
class="headerlink" title="Link to this definition"></a>  
The free energy of the calculation.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">gap</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.gap"
class="headerlink" title="Link to this definition"></a>  
The band gap.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">hirshfeld_atomic_dipoles</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.hirshfeld_atomic_dipoles"
class="headerlink" title="Link to this definition"></a>  
The Hirshfeld atomic dipoles of the system.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">hirshfeld_charges</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.hirshfeld_charges"
class="headerlink" title="Link to this definition"></a>  
The Hirshfeld charges of the system.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">hirshfeld_dipole</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.hirshfeld_dipole"
class="headerlink" title="Link to this definition"></a>  
The Hirshfeld dipole of the system.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">hirshfeld_volumes</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.hirshfeld_volumes"
class="headerlink" title="Link to this definition"></a>  
The Hirshfeld atomic dipoles of the system.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">initial_lattice</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.lattice.Lattice"
class="reference internal" title="pymatgen.core.lattice.Lattice"><span
class="pre">Lattice</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.initial_lattice"
class="headerlink" title="Link to this definition"></a>  
The initial Lattice of the structure.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">initial_structure</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.initial_structure"
class="headerlink" title="Link to this definition"></a>  
The initial structure for the calculation.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">is_metallic</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.is_metallic"
class="headerlink" title="Link to this definition"></a>  
Is the system is metallic.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">k_point_weights</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.k_point_weights"
class="headerlink" title="Link to this definition"></a>  
The k-point weights for the calculation.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">k_points</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.k_points"
class="headerlink" title="Link to this definition"></a>  
All k-points listed in the calculation.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">lattice</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.lattice.Lattice"
class="reference internal" title="pymatgen.core.lattice.Lattice"><span
class="pre">Lattice</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.lattice"
class="headerlink" title="Link to this definition"></a>  
The Lattice object for the structure.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">magmom</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.magmom"
class="headerlink" title="Link to this definition"></a>  
The magnetic moment of the structure.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">mulliken_charges</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.mulliken_charges"
class="headerlink" title="Link to this definition"></a>  
The Mulliken charges of the system

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">mulliken_spins</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.mulliken_spins"
class="headerlink" title="Link to this definition"></a>  
The Mulliken spins of the system

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">n_atoms</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.n_atoms"
class="headerlink" title="Link to this definition"></a>  
The number of atoms in the structure.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">n_bands</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.n_bands"
class="headerlink" title="Link to this definition"></a>  
The number of Kohn-Sham states for the chunk.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">n_electrons</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.n_electrons"
class="headerlink" title="Link to this definition"></a>  
The number of electrons for the chunk.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">n_iter</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.n_iter"
class="headerlink" title="Link to this definition"></a>  
The number of steps needed to converge the SCF cycle for the chunk.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">n_k\_points</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.n_k_points"
class="headerlink" title="Link to this definition"></a>  
The number of k_ppoints for the calculation.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">n_spins</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.n_spins"
class="headerlink" title="Link to this definition"></a>  
The number of spin channels for the chunk.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">polarization</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.polarization"
class="headerlink" title="Link to this definition"></a>  
The polarization vector from the aims.out file.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">results</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.results"
class="headerlink" title="Link to this definition"></a>  
Convert an AimsOutChunk to a Results Dictionary.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">species</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.species"
class="headerlink" title="Link to this definition"></a>  
The list of atomic symbols for all atoms in the structure.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">stress</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.stress"
class="headerlink" title="Link to this definition"></a>  
The stress from the aims.out file and convert to kBar.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">stresses</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.stresses"
class="headerlink" title="Link to this definition"></a>  
The stresses from the aims.out file and convert to kBar.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">structure</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.structure"
class="headerlink" title="Link to this definition"></a>  
The pymatgen SiteCollection of the chunk.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">vbm</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.vbm"
class="headerlink" title="Link to this definition"></a>  
The valance band maximum.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">velocities</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk.velocities"
class="headerlink" title="Link to this definition"></a>  
The velocities of the atoms.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">AimsOutChunk</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">lines:</span> <span class="pre">list\[str\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/parsers.py#L64-L122"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutChunk" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Base class for AimsOutChunks.

<span class="sig-name descname"><span class="pre">lines</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutChunk.lines"
class="headerlink" title="Link to this definition"></a>  
The list of all lines in the chunk

Type<span class="colon">:</span>  
list\[str\]

<span class="sig-name descname"><span class="pre">lines</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id11" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">parse_scalar</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">property</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/parsers.py#L107-L122"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutChunk.parse_scalar"
class="headerlink" title="Link to this definition"></a>  
Parse a scalar property from the chunk.

Parameters<span class="colon">:</span>  
**property** (*str*) – The property key to parse

Returns<span class="colon">:</span>  
The scalar value of the property or None if not found

<span class="sig-name descname"><span class="pre">reverse_search_for</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">keys</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">line_start</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">int</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/parsers.py#L74-L88"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutChunk.reverse_search_for"
class="headerlink" title="Link to this definition"></a>  
Find the last time one of the keys appears in self.lines.

Parameters<span class="colon">:</span>  
- **keys** (*list\[str\]*) – The key strings to search for in self.lines

- **line_start** (*int*) – The lowest index to search for in self.lines

Returns<span class="colon">:</span>  
The last time one of the keys appears in self.lines

<span class="sig-name descname"><span class="pre">search_for_all</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">key</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">line_start</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">line_end</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">-1</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/parsers.py#L90-L105"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutChunk.search_for_all"
class="headerlink" title="Link to this definition"></a>  
Find the all times the key appears in self.lines.

Parameters<span class="colon">:</span>  
- **key** (*str*) – The key string to search for in self.lines

- **line_start** (*int*) – The first line to start the search from

- **line_end** (*int*) – The last line to end the search at

Returns<span class="colon">:</span>  
All times the key appears in the lines

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">AimsOutHeaderChunk</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">lines:</span> <span class="pre">list\[str\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">\_cache:</span> <span class="pre">dict\[str</span></span>*, *<span class="n"><span class="pre">Any\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/parsers.py#L125-L448"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.aims.parsers.AimsOutChunk"
class="reference internal"
title="pymatgen.io.aims.parsers.AimsOutChunk"><span class="pre"><code
class="sourceCode python">AimsOutChunk</code></span></a>

The header of the aims.out file containing general information.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">aims_uuid</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.aims_uuid"
class="headerlink" title="Link to this definition"></a>  
The aims-uuid for the calculation.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">build_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.build_type"
class="headerlink" title="Link to this definition"></a>  
The optional build flags passed to cmake.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">c_compiler</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.c_compiler"
class="headerlink" title="Link to this definition"></a>  
The C compiler used to make FHI-aims.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">c_compiler_flags</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.c_compiler_flags"
class="headerlink" title="Link to this definition"></a>  
The C compiler flags used to make FHI-aims.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">commit_hash</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.commit_hash"
class="headerlink" title="Link to this definition"></a>  
The commit hash for the FHI-aims version.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">electronic_temperature</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.electronic_temperature"
class="headerlink" title="Link to this definition"></a>  
The electronic temperature for the chunk.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">fortran_compiler</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.fortran_compiler"
class="headerlink" title="Link to this definition"></a>  
The fortran compiler used to make FHI-aims.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">fortran_compiler_flags</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.fortran_compiler_flags"
class="headerlink" title="Link to this definition"></a>  
The fortran compiler flags used to make FHI-aims.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">header_summary</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.header_summary"
class="headerlink" title="Link to this definition"></a>  
Dictionary summarizing the information inside the header.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">initial_charges</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.initial_charges"
class="headerlink" title="Link to this definition"></a>  
The initial charges for the structure.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">initial_lattice</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.lattice.Lattice"
class="reference internal" title="pymatgen.core.lattice.Lattice"><span
class="pre">Lattice</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.initial_lattice"
class="headerlink" title="Link to this definition"></a>  
The initial lattice vectors from the aims.out file.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">initial_magnetic_moments</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.initial_magnetic_moments"
class="headerlink" title="Link to this definition"></a>  
The initial magnetic Moments.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">initial_structure</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.initial_structure"
class="headerlink" title="Link to this definition"></a>  
The initial structure.

Using the FHI-aims output file recreate the initial structure for the
calculation.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">is_md</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.is_md"
class="headerlink" title="Link to this definition"></a>  
Is the output for a molecular dynamics calculation?

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">is_relaxation</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.is_relaxation"
class="headerlink" title="Link to this definition"></a>  
Is the output for a relaxation?

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">k_point_weights</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.k_point_weights"
class="headerlink" title="Link to this definition"></a>  
The k-point weights for the calculation.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">k_points</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.k_points"
class="headerlink" title="Link to this definition"></a>  
All k-points listed in the calculation.

<span class="sig-name descname"><span class="pre">lines</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.lines"
class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">linked_against</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.linked_against"
class="headerlink" title="Link to this definition"></a>  
All libraries used to link the FHI-aims executable.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">metadata_summary</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.metadata_summary"
class="headerlink" title="Link to this definition"></a>  
Dictionary containing all metadata for FHI-aims build.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">n_atoms</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.n_atoms"
class="headerlink" title="Link to this definition"></a>  
The number of atoms for the material.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">n_bands</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.n_bands"
class="headerlink" title="Link to this definition"></a>  
The number of Kohn-Sham states for the chunk.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">n_electrons</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.n_electrons"
class="headerlink" title="Link to this definition"></a>  
The number of electrons for the chunk.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">n_k\_points</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.n_k_points"
class="headerlink" title="Link to this definition"></a>  
The number of k_ppoints for the calculation.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">n_spins</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.n_spins"
class="headerlink" title="Link to this definition"></a>  
The number of spin channels for the chunk.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">version_number</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/io/aims/parsers.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk.version_number"
class="headerlink" title="Link to this definition"></a>  
The commit hash for the FHI-aims version.

<!-- -->

*<span class="k"><span class="pre">exception</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">AimsParseError</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">message</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/parsers.py#L36-L42"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.AimsParseError" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`Exception`</span>

Exception raised if an error occurs when parsing an Aims output file.

Initialize the error with the message, message.

<!-- -->

*<span class="k"><span class="pre">exception</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ParseError</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/parsers.py#L32-L33"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.ParseError" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`Exception`</span>

Parse error during reading of a file.

<!-- -->

<span class="sig-name descname"><span class="pre">check_convergence</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">chunks</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.io.aims.parsers.AimsOutCalcChunk"
class="reference internal"
title="pymatgen.io.aims.parsers.AimsOutCalcChunk"><span
class="pre">AimsOutCalcChunk</span></a><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">non_convergence_ok</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/parsers.py#L1087-L1101"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.check_convergence" class="headerlink"
title="Link to this definition"></a>  
Check if the aims output file is for a converged calculation.

Parameters<span class="colon">:</span>  
- **chunks** (*list\[.AimsOutCalcChunk\]*) – The list of chunks for the
  aims calculations

- **non_convergence_ok** (*bool*) – True if it is okay for the
  calculation to not be converged

- **chunks** – list\[AimsOutCalcChunk\]:

- **non_convergence_ok** – bool: (Default value = False)

Returns<span class="colon">:</span>  
True if the calculation is converged

<!-- -->

<span class="sig-name descname"><span class="pre">get_aims_out_chunks</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">content</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">TextIOWrapper</span></span>*, *<span class="n"><span class="pre">header_chunk</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk"
class="reference internal"
title="pymatgen.io.aims.parsers.AimsOutHeaderChunk"><span
class="pre">AimsOutHeaderChunk</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Generator</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/parsers.py#L1034-L1084"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.get_aims_out_chunks"
class="headerlink" title="Link to this definition"></a>  
Yield unprocessed chunks (header, lines) for each AimsOutChunk image.

Parameters<span class="colon">:</span>  
- **content** (*str* *or* *TextIOWrapper*) – the content to parse

- **header_chunk**
  (<a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk"
  class="reference internal"
  title="pymatgen.io.aims.parsers.AimsOutHeaderChunk"><em>AimsOutHeaderChunk</em></a>)
  – The AimsOutHeader for the calculation

Yields<span class="colon">:</span>  
The next AimsOutChunk

<!-- -->

<span class="sig-name descname"><span class="pre">get_header_chunk</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">content</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">TextIOWrapper</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.aims.parsers.AimsOutHeaderChunk"
class="reference internal"
title="pymatgen.io.aims.parsers.AimsOutHeaderChunk"><span
class="pre">AimsOutHeaderChunk</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/parsers.py#L1006-L1031"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.get_header_chunk" class="headerlink"
title="Link to this definition"></a>  
Get the header chunk for an output.

Parameters<span class="colon">:</span>  
**content** (*str* *or* *TextIOWrapper*) – the content to parse

Returns<span class="colon">:</span>  
The AimsHeaderChunk of the file

<!-- -->

<span class="sig-name descname"><span class="pre">get_lines</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">content</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">TextIOWrapper</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/parsers.py#L992-L1003"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.get_lines" class="headerlink"
title="Link to this definition"></a>  
Get a list of lines from a str or file of content.

Parameters<span class="colon">:</span>  
**content** – the content of the file to parse

Returns<span class="colon">:</span>  
The list of lines

<!-- -->

<span class="sig-name descname"><span class="pre">read_aims_header_info</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Path</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/parsers.py#L1119-L1144"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.read_aims_header_info"
class="headerlink" title="Link to this definition"></a>  
Read the FHI-aims header information.

Parameters<span class="colon">:</span>  
**filename** (*str* *or* *Path*) – The file to read

Returns<span class="colon">:</span>  
The metadata for the header of the aims calculation

<!-- -->

<span class="sig-name descname"><span class="pre">read_aims_header_info_from_content</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">content</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/parsers.py#L1104-L1116"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.read_aims_header_info_from_content"
class="headerlink" title="Link to this definition"></a>  
Read the FHI-aims header information.

Parameters<span class="colon">:</span>  
**content** (*str*) – The content of the output file to check

Returns<span class="colon">:</span>  
The metadata for the header of the aims calculation

<!-- -->

<span class="sig-name descname"><span class="pre">read_aims_output</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Path</span></span>*, *<span class="n"><span class="pre">index</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">slice</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">-1</span></span>*, *<span class="n"><span class="pre">non_convergence_ok</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/parsers.py#L1172-L1203"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.read_aims_output" class="headerlink"
title="Link to this definition"></a>  
Import FHI-aims output files with all data available.

Includes all structures for relaxations and MD runs with FHI-aims

Parameters<span class="colon">:</span>  
- **filename** (*str* *or* *Path*) – The file to read

- **index** (*int* *or* *slice*) – The index of the images to read

- **non_convergence_ok** (*bool*) – True if the calculations do not have
  to be converged

Returns<span class="colon">:</span>  
The list of images to get

<!-- -->

<span class="sig-name descname"><span class="pre">read_aims_output_from_content</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">content</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">index</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">slice</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">-1</span></span>*, *<span class="n"><span class="pre">non_convergence_ok</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.5.28/src/pymatgen/core/../io/aims/parsers.py#L1147-L1169"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.aims.parsers.read_aims_output_from_content"
class="headerlink" title="Link to this definition"></a>  
Read and aims output file from the content of a file.

Parameters<span class="colon">:</span>  
- **content** (*str*) – The content of the file to read

- **index** – int \| slice: (Default value = -1)

- **non_convergence_ok** – bool: (Default value = False)

Returns<span class="colon">:</span>  
The list of images to get

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
