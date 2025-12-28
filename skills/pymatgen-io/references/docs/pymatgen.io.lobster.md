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

- <a href="#" class="reference internal">pymatgen.io.lobster package</a>
  - <a href="#submodules" class="reference internal">Submodules</a>
  - <a href="#module-pymatgen.io.lobster.inputs"
    class="reference internal">pymatgen.io.lobster.inputs module</a>
    - <a href="#pymatgen.io.lobster.inputs.Lobsterin"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Lobsterin</code></span></a>
      - <a href="#pymatgen.io.lobster.inputs.Lobsterin.AVAILABLE_KEYWORDS"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterin.AVAILABLE_KEYWORDS</code></span></a>
      - <a href="#pymatgen.io.lobster.inputs.Lobsterin.BOOLEAN_KEYWORDS"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterin.BOOLEAN_KEYWORDS</code></span></a>
      - <a href="#pymatgen.io.lobster.inputs.Lobsterin.FLOAT_KEYWORDS"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterin.FLOAT_KEYWORDS</code></span></a>
      - <a href="#pymatgen.io.lobster.inputs.Lobsterin.LIST_KEYWORDS"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterin.LIST_KEYWORDS</code></span></a>
      - <a href="#pymatgen.io.lobster.inputs.Lobsterin.STRING_KEYWORDS"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterin.STRING_KEYWORDS</code></span></a>
      - <a href="#pymatgen.io.lobster.inputs.Lobsterin.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterin.as_dict()</code></span></a>
      - <a href="#pymatgen.io.lobster.inputs.Lobsterin.diff"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterin.diff()</code></span></a>
      - <a href="#pymatgen.io.lobster.inputs.Lobsterin.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterin.from_dict()</code></span></a>
      - <a href="#pymatgen.io.lobster.inputs.Lobsterin.from_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterin.from_file()</code></span></a>
      - <a
        href="#pymatgen.io.lobster.inputs.Lobsterin.get_all_possible_basis_functions"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterin.get_all_possible_basis_functions()</code></span></a>
      - <a href="#pymatgen.io.lobster.inputs.Lobsterin.get_basis"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterin.get_basis()</code></span></a>
      - <a
        href="#pymatgen.io.lobster.inputs.Lobsterin.standard_calculations_from_vasp_files"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterin.standard_calculations_from_vasp_files()</code></span></a>
      - <a href="#pymatgen.io.lobster.inputs.Lobsterin.write_INCAR"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterin.write_INCAR()</code></span></a>
      - <a href="#pymatgen.io.lobster.inputs.Lobsterin.write_KPOINTS"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterin.write_KPOINTS()</code></span></a>
      - <a
        href="#pymatgen.io.lobster.inputs.Lobsterin.write_POSCAR_with_standard_primitive"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterin.write_POSCAR_with_standard_primitive()</code></span></a>
      - <a href="#pymatgen.io.lobster.inputs.Lobsterin.write_lobsterin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterin.write_lobsterin()</code></span></a>
    - <a
      href="#pymatgen.io.lobster.inputs.get_all_possible_basis_combinations"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">get_all_possible_basis_combinations()</code></span></a>
  - <a href="#module-pymatgen.io.lobster.lobsterenv"
    class="reference internal">pymatgen.io.lobster.lobsterenv module</a>
    - <a href="#pymatgen.io.lobster.lobsterenv.ICOHPNeighborsInfo"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">ICOHPNeighborsInfo</code></span></a>
      - <a href="#pymatgen.io.lobster.lobsterenv.ICOHPNeighborsInfo.atoms"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ICOHPNeighborsInfo.atoms</code></span></a>
      - <a
        href="#pymatgen.io.lobster.lobsterenv.ICOHPNeighborsInfo.central_isites"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ICOHPNeighborsInfo.central_isites</code></span></a>
      - <a href="#pymatgen.io.lobster.lobsterenv.ICOHPNeighborsInfo.labels"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ICOHPNeighborsInfo.labels</code></span></a>
      - <a href="#pymatgen.io.lobster.lobsterenv.ICOHPNeighborsInfo.list_icohps"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ICOHPNeighborsInfo.list_icohps</code></span></a>
      - <a href="#pymatgen.io.lobster.lobsterenv.ICOHPNeighborsInfo.n_bonds"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ICOHPNeighborsInfo.n_bonds</code></span></a>
      - <a href="#pymatgen.io.lobster.lobsterenv.ICOHPNeighborsInfo.total_icohp"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ICOHPNeighborsInfo.total_icohp</code></span></a>
    - <a
      href="#pymatgen.io.lobster.lobsterenv.LobsterLightStructureEnvironments"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">LobsterLightStructureEnvironments</code></span></a>
      - <a
        href="#pymatgen.io.lobster.lobsterenv.LobsterLightStructureEnvironments.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LobsterLightStructureEnvironments.as_dict()</code></span></a>
      - <a
        href="#pymatgen.io.lobster.lobsterenv.LobsterLightStructureEnvironments.from_Lobster"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LobsterLightStructureEnvironments.from_Lobster()</code></span></a>
      - <a
        href="#pymatgen.io.lobster.lobsterenv.LobsterLightStructureEnvironments.uniquely_determines_coordination_environments"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LobsterLightStructureEnvironments.uniquely_determines_coordination_environments</code></span></a>
    - <a href="#pymatgen.io.lobster.lobsterenv.LobsterNeighbors"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">LobsterNeighbors</code></span></a>
      - <a href="#pymatgen.io.lobster.lobsterenv.LobsterNeighbors.anion_types"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LobsterNeighbors.anion_types</code></span></a>
      - <a
        href="#pymatgen.io.lobster.lobsterenv.LobsterNeighbors.get_anion_types"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LobsterNeighbors.get_anion_types()</code></span></a>
      - <a
        href="#pymatgen.io.lobster.lobsterenv.LobsterNeighbors.get_info_cohps_to_neighbors"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LobsterNeighbors.get_info_cohps_to_neighbors()</code></span></a>
      - <a
        href="#pymatgen.io.lobster.lobsterenv.LobsterNeighbors.get_info_icohps_between_neighbors"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LobsterNeighbors.get_info_icohps_between_neighbors()</code></span></a>
      - <a
        href="#pymatgen.io.lobster.lobsterenv.LobsterNeighbors.get_info_icohps_to_neighbors"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LobsterNeighbors.get_info_icohps_to_neighbors()</code></span></a>
      - <a
        href="#pymatgen.io.lobster.lobsterenv.LobsterNeighbors.get_light_structure_environment"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LobsterNeighbors.get_light_structure_environment()</code></span></a>
      - <a href="#pymatgen.io.lobster.lobsterenv.LobsterNeighbors.get_nn_info"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LobsterNeighbors.get_nn_info()</code></span></a>
      - <a
        href="#pymatgen.io.lobster.lobsterenv.LobsterNeighbors.molecules_allowed"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LobsterNeighbors.molecules_allowed</code></span></a>
      - <a
        href="#pymatgen.io.lobster.lobsterenv.LobsterNeighbors.plot_cohps_of_neighbors"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LobsterNeighbors.plot_cohps_of_neighbors()</code></span></a>
      - <a
        href="#pymatgen.io.lobster.lobsterenv.LobsterNeighbors.structures_allowed"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LobsterNeighbors.structures_allowed</code></span></a>
  - <a href="#module-pymatgen.io.lobster.outputs"
    class="reference internal">pymatgen.io.lobster.outputs module</a>
    - <a href="#pymatgen.io.lobster.outputs.Bandoverlaps"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Bandoverlaps</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Bandoverlaps.band_overlaps_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Bandoverlaps.band_overlaps_dict</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Bandoverlaps.max_deviation"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Bandoverlaps.max_deviation</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Bandoverlaps.bandoverlapsdict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Bandoverlaps.bandoverlapsdict</code></span></a>
      - <a
        href="#pymatgen.io.lobster.outputs.Bandoverlaps.has_good_quality_check_occupied_bands"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Bandoverlaps.has_good_quality_check_occupied_bands()</code></span></a>
      - <a
        href="#pymatgen.io.lobster.outputs.Bandoverlaps.has_good_quality_maxDeviation"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Bandoverlaps.has_good_quality_maxDeviation()</code></span></a>
    - <a href="#pymatgen.io.lobster.outputs.Bwdf"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Bwdf</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Bwdf.centers"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Bwdf.centers</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Bwdf.bwdf"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Bwdf.bwdf</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Bwdf.bin_width"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Bwdf.bin_width</code></span></a>
    - <a href="#pymatgen.io.lobster.outputs.Charge"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Charge</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Charge.atomlist"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Charge.atomlist</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Charge.is_lcfo"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Charge.is_lcfo</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Charge.types"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Charge.types</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Charge.mulliken"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Charge.mulliken</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Charge.loewdin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Charge.loewdin</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Charge.num_atoms"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Charge.num_atoms</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Charge.Loewdin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Charge.Loewdin</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Charge.Mulliken"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Charge.Mulliken</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Charge.get_structure_with_charges"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Charge.get_structure_with_charges()</code></span></a>
    - <a href="#pymatgen.io.lobster.outputs.Cohpcar"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Cohpcar</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Cohpcar.cohp_data"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cohpcar.cohp_data</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Cohpcar.efermi"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cohpcar.efermi</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Cohpcar.energies"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cohpcar.energies</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Cohpcar.is_spin_polarized"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cohpcar.is_spin_polarized</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Cohpcar.orb_res_cohp"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cohpcar.orb_res_cohp</code></span></a>
    - <a href="#pymatgen.io.lobster.outputs.Doscar"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Doscar</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Doscar.completedos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Doscar.completedos</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Doscar.pdos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Doscar.pdos</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Doscar.tdos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Doscar.tdos</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Doscar.energies"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Doscar.energies</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Doscar.tdensities"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Doscar.tdensities</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Doscar.itdensities"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Doscar.itdensities</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Doscar.is_spin_polarized"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Doscar.is_spin_polarized</code></span></a>
      - <a href="#id0" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Doscar.completedos</code></span></a>
      - <a href="#id1" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Doscar.energies</code></span></a>
      - <a href="#id2" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Doscar.is_spin_polarized</code></span></a>
      - <a href="#id3" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Doscar.itdensities</code></span></a>
      - <a href="#id4" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Doscar.pdos</code></span></a>
      - <a href="#id5" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Doscar.tdensities</code></span></a>
      - <a href="#id6" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Doscar.tdos</code></span></a>
    - <a href="#pymatgen.io.lobster.outputs.Fatband"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Fatband</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Fatband.efermi"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Fatband.efermi</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Fatband.eigenvals"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Fatband.eigenvals</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Fatband.is_spin_polarized"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Fatband.is_spin_polarized</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Fatband.kpoints_array"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Fatband.kpoints_array</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Fatband.label_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Fatband.label_dict</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Fatband.lattice"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Fatband.lattice</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Fatband.nbands"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Fatband.nbands</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Fatband.p_eigenvals"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Fatband.p_eigenvals</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Fatband.structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Fatband.structure</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Fatband.get_bandstructure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Fatband.get_bandstructure()</code></span></a>
    - <a href="#pymatgen.io.lobster.outputs.Grosspop"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Grosspop</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Grosspop.list_dict_grosspop"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Grosspop.list_dict_grosspop</code></span></a>
      - <a
        href="#pymatgen.io.lobster.outputs.Grosspop.get_structure_with_total_grosspop"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Grosspop.get_structure_with_total_grosspop()</code></span></a>
    - <a href="#pymatgen.io.lobster.outputs.Icohplist"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Icohplist</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Icohplist.are_coops"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Icohplist.are_coops</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Icohplist.is_lcfo"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Icohplist.is_lcfo</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Icohplist.is_spin_polarized"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Icohplist.is_spin_polarized</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Icohplist.Icohplist"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Icohplist.Icohplist</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Icohplist.IcohpCollection"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Icohplist.IcohpCollection</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Icohplist.icohpcollection"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Icohplist.icohpcollection</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Icohplist.icohplist"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Icohplist.icohplist</code></span></a>
    - <a href="#pymatgen.io.lobster.outputs.LobsterMatrices"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">LobsterMatrices</code></span></a>
    - <a href="#pymatgen.io.lobster.outputs.Lobsterout"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Lobsterout</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Lobsterout.basis_functions"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterout.basis_functions</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Lobsterout.basis_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterout.basis_type</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Lobsterout.charge_spilling"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterout.charge_spilling</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Lobsterout.dft_program"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterout.dft_program</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Lobsterout.elements"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterout.elements</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Lobsterout.has_charge"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterout.has_charge</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Lobsterout.has_cohpcar"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterout.has_cohpcar</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Lobsterout.has_madelung"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterout.has_madelung</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Lobsterout.has_coopcar"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterout.has_coopcar</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Lobsterout.has_cobicar"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterout.has_cobicar</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Lobsterout.has_doscar"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterout.has_doscar</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Lobsterout.has_doscar_lso"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterout.has_doscar_lso</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Lobsterout.has_projection"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterout.has_projection</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Lobsterout.has_bandoverlaps"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterout.has_bandoverlaps</code></span></a>
      - <a
        href="#pymatgen.io.lobster.outputs.Lobsterout.has_density_of_energies"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterout.has_density_of_energies</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Lobsterout.has_fatbands"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterout.has_fatbands</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Lobsterout.has_grosspopulation"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterout.has_grosspopulation</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Lobsterout.has_polarization"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterout.has_polarization</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Lobsterout.info_lines"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterout.info_lines</code></span></a>
      - <a
        href="#pymatgen.io.lobster.outputs.Lobsterout.info_orthonormalization"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterout.info_orthonormalization</code></span></a>
      - <a
        href="#pymatgen.io.lobster.outputs.Lobsterout.is_restart_from_projection"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterout.is_restart_from_projection</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Lobsterout.lobster_version"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterout.lobster_version</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Lobsterout.number_of_spins"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterout.number_of_spins</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Lobsterout.number_of_threads"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterout.number_of_threads</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Lobsterout.timing"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterout.timing</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Lobsterout.total_spilling"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterout.total_spilling</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Lobsterout.warning_lines"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterout.warning_lines</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Lobsterout.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterout.as_dict()</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Lobsterout.get_doc"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Lobsterout.get_doc()</code></span></a>
    - <a href="#pymatgen.io.lobster.outputs.MadelungEnergies"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">MadelungEnergies</code></span></a>
      - <a
        href="#pymatgen.io.lobster.outputs.MadelungEnergies.madelungenergies_mulliken"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MadelungEnergies.madelungenergies_mulliken</code></span></a>
      - <a
        href="#pymatgen.io.lobster.outputs.MadelungEnergies.madelungenergies_loewdin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MadelungEnergies.madelungenergies_loewdin</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.MadelungEnergies.ewald_splitting"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MadelungEnergies.ewald_splitting</code></span></a>
      - <a
        href="#pymatgen.io.lobster.outputs.MadelungEnergies.madelungenergies_Loewdin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MadelungEnergies.madelungenergies_Loewdin</code></span></a>
      - <a
        href="#pymatgen.io.lobster.outputs.MadelungEnergies.madelungenergies_Mulliken"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MadelungEnergies.madelungenergies_Mulliken</code></span></a>
    - <a href="#pymatgen.io.lobster.outputs.NciCobiList"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">NciCobiList</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.NciCobiList.is_spin_polarized"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NciCobiList.is_spin_polarized</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.NciCobiList.NciCobiList"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NciCobiList.NciCobiList</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.NciCobiList.ncicobi_list"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NciCobiList.ncicobi_list</code></span></a>
    - <a href="#pymatgen.io.lobster.outputs.Polarization"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Polarization</code></span></a>
      - <a
        href="#pymatgen.io.lobster.outputs.Polarization.rel_mulliken_pol_vector"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Polarization.rel_mulliken_pol_vector</code></span></a>
      - <a
        href="#pymatgen.io.lobster.outputs.Polarization.rel_loewdin_pol_vector"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Polarization.rel_loewdin_pol_vector</code></span></a>
    - <a href="#pymatgen.io.lobster.outputs.SitePotential"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">SitePotential</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.SitePotential.atomlist"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SitePotential.atomlist</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.SitePotential.types"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SitePotential.types</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.SitePotential.num_atoms"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SitePotential.num_atoms</code></span></a>
      - <a
        href="#pymatgen.io.lobster.outputs.SitePotential.sitepotentials_mulliken"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SitePotential.sitepotentials_mulliken</code></span></a>
      - <a
        href="#pymatgen.io.lobster.outputs.SitePotential.sitepotentials_loewdin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SitePotential.sitepotentials_loewdin</code></span></a>
      - <a
        href="#pymatgen.io.lobster.outputs.SitePotential.madelungenergies_mulliken"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SitePotential.madelungenergies_mulliken</code></span></a>
      - <a
        href="#pymatgen.io.lobster.outputs.SitePotential.madelungenergies_loewdin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SitePotential.madelungenergies_loewdin</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.SitePotential.ewald_splitting"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SitePotential.ewald_splitting</code></span></a>
      - <a
        href="#pymatgen.io.lobster.outputs.SitePotential.get_structure_with_site_potentials"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SitePotential.get_structure_with_site_potentials()</code></span></a>
      - <a
        href="#pymatgen.io.lobster.outputs.SitePotential.madelungenergies_Loewdin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SitePotential.madelungenergies_Loewdin</code></span></a>
      - <a
        href="#pymatgen.io.lobster.outputs.SitePotential.madelungenergies_Mulliken"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SitePotential.madelungenergies_Mulliken</code></span></a>
      - <a
        href="#pymatgen.io.lobster.outputs.SitePotential.sitepotentials_Loewdin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SitePotential.sitepotentials_Loewdin</code></span></a>
      - <a
        href="#pymatgen.io.lobster.outputs.SitePotential.sitepotentials_Mulliken"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SitePotential.sitepotentials_Mulliken</code></span></a>
    - <a href="#pymatgen.io.lobster.outputs.Wavefunction"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Wavefunction</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Wavefunction.grid"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Wavefunction.grid</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Wavefunction.points"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Wavefunction.points</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Wavefunction.real"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Wavefunction.real</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Wavefunction.imaginary"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Wavefunction.imaginary</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Wavefunction.distance"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Wavefunction.distance</code></span></a>
      - <a
        href="#pymatgen.io.lobster.outputs.Wavefunction.get_volumetricdata_density"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Wavefunction.get_volumetricdata_density()</code></span></a>
      - <a
        href="#pymatgen.io.lobster.outputs.Wavefunction.get_volumetricdata_imaginary"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Wavefunction.get_volumetricdata_imaginary()</code></span></a>
      - <a
        href="#pymatgen.io.lobster.outputs.Wavefunction.get_volumetricdata_real"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Wavefunction.get_volumetricdata_real()</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Wavefunction.set_volumetric_data"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Wavefunction.set_volumetric_data()</code></span></a>
      - <a href="#pymatgen.io.lobster.outputs.Wavefunction.write_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Wavefunction.write_file()</code></span></a>
    - <a href="#pymatgen.io.lobster.outputs.get_orb_from_str"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">get_orb_from_str()</code></span></a>

</div>

</div>

</div>

<div class="section wy-nav-content-wrap" toggle="wy-nav-shift">

[pymatgen](index.html)

<div class="wy-nav-content">

<div class="rst-content style-external-links">

<div role="navigation" aria-label="Page navigation">

- <a href="index.html" class="icon icon-home" aria-label="Home"></a>
- pymatgen.io.lobster package
- <a
  href="https://github.com/materialsproject/pymatgen/blob/master/docs_rst/pymatgen.io.lobster.rst"
  class="fa fa-github">Edit on GitHub</a>

------------------------------------------------------------------------

</div>

<div class="document" role="main" itemscope="itemscope"
itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="module-pymatgen.io.lobster" class="section">

<span id="pymatgen-io-lobster-package"></span>

# pymatgen.io.lobster package<a href="#module-pymatgen.io.lobster" class="headerlink"
title="Link to this heading"></a>

This package implements modules for input and output to and from
LOBSTER. It imports the key classes form both lobster.inputs and
lobster.outputs to allow most classes to be simply called as
pymatgen.io.lobster.Lobsterin for example, to retain backwards
compatibility.

<div id="submodules" class="section">

## Submodules<a href="#submodules" class="headerlink"
title="Link to this heading"></a>

</div>

<div id="module-pymatgen.io.lobster.inputs" class="section">

<span id="pymatgen-io-lobster-inputs-module"></span>

## pymatgen.io.lobster.inputs module<a href="#module-pymatgen.io.lobster.inputs" class="headerlink"
title="Link to this heading"></a>

Module for reading LOBSTER input files. For more information on LOBSTER
see www.cohp.de.

If you use this module, please cite: J. George, G. Petretto, A. Naik, M.
Esters, A. J. Jackson, R. Nelson, R. Dronskowski, G.-M. Rignanese, G.
Hautier, “Automated Bonding Analysis with Crystal Orbital Hamilton
Populations”, ChemPlusChem 2022, e202200123, DOI:
10.1002/cplu.202200123.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Lobsterin</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">settingsdict</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/inputs.py#L57-L858"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.inputs.Lobsterin" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`UserDict`</span>, <span
class="pre">`MSONable`</span>

Handle and generate lobsterin files. Furthermore, it can also modify
INCAR files for LOBSTER, generate KPOINTS files for fatband calculations
in LOBSTER, and generate the standard primitive cells in a POSCAR file
that are needed for the fatband calculations. There are also several
standard lobsterin files that can be easily generated.

Reminder: lobsterin keywords are not case sensitive.

Parameters<span class="colon">:</span>  
**settingsdict** – dict to initialize Lobsterin.

<span class="sig-name descname"><span class="pre">AVAILABLE_KEYWORDS</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ClassVar</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">{'autorotate':</span> <span class="pre">'autoRotate',</span> <span class="pre">'bandwisespilling':</span> <span class="pre">'bandwiseSpilling',</span> <span class="pre">'basisfunctions':</span> <span class="pre">'basisfunctions',</span> <span class="pre">'basisrotation':</span> <span class="pre">'basisRotation',</span> <span class="pre">'basisset':</span> <span class="pre">'basisSet',</span> <span class="pre">'bwdf':</span> <span class="pre">'BWDF',</span> <span class="pre">'bwdfcohp':</span> <span class="pre">'BWDFCOHP',</span> <span class="pre">'cobibetween':</span> <span class="pre">'cobiBetween',</span> <span class="pre">'cohpbetween':</span> <span class="pre">'cohpbetween',</span> <span class="pre">'cohpendenergy':</span> <span class="pre">'COHPendEnergy',</span> <span class="pre">'cohpgenerator':</span> <span class="pre">'cohpGenerator',</span> <span class="pre">'cohpstartenergy':</span> <span class="pre">'COHPstartEnergy',</span> <span class="pre">'cohpsteps':</span> <span class="pre">'COHPSteps',</span> <span class="pre">'createfatband':</span> <span class="pre">'createFatband',</span> <span class="pre">'customstoforatom':</span> <span class="pre">'customSTOforAtom',</span> <span class="pre">'densityofenergy':</span> <span class="pre">'DensityOfEnergy',</span> <span class="pre">'donotignoreexcessivebands':</span> <span class="pre">'doNotIgnoreExcessiveBands',</span> <span class="pre">'donotorthogonalizebasis':</span> <span class="pre">'doNotOrthogonalizeBasis',</span> <span class="pre">'donotuseabsolutespilling':</span> <span class="pre">'doNotUseAbsoluteSpilling',</span> <span class="pre">'ewaldsum':</span> <span class="pre">'EwaldSum',</span> <span class="pre">'forceenergyrange':</span> <span class="pre">'forceEnergyRange',</span> <span class="pre">'forcev1hmatrix':</span> <span class="pre">'forceV1HMatrix',</span> <span class="pre">'gaussiansmearingwidth':</span> <span class="pre">'gaussianSmearingWidth',</span> <span class="pre">'gridbufferforprinting':</span> <span class="pre">'gridBufferForPrinting',</span> <span class="pre">'griddensityforprinting':</span> <span class="pre">'gridDensityForPrinting',</span> <span class="pre">'kpointwisespilling':</span> <span class="pre">'kpointwiseSpilling',</span> <span class="pre">'kspacecohp':</span> <span class="pre">'kSpaceCOHP',</span> <span class="pre">'loadprojectionfromfile':</span> <span class="pre">'loadProjectionFromFile',</span> <span class="pre">'lsodos':</span> <span class="pre">'LSODOS',</span> <span class="pre">'nofftforvisualization':</span> <span class="pre">'noFFTforVisualization',</span> <span class="pre">'nomemorymappedfiles':</span> <span class="pre">'noMemoryMappedFiles',</span> <span class="pre">'onlyreadvasprun.xml':</span> <span class="pre">'onlyReadVasprun.xml',</span> <span class="pre">'printlcaorealspacewavefunction':</span> <span class="pre">'printLCAORealSpaceWavefunction',</span> <span class="pre">'printlmosonatoms':</span> <span class="pre">'printLmosOnAtoms',</span> <span class="pre">'printlmosonatomswriteatomicdensities':</span> <span class="pre">'printLmosOnAtomswriteAtomicDensities',</span> <span class="pre">'printmofeatomwise':</span> <span class="pre">'printMofeAtomWise',</span> <span class="pre">'printmofemoleculewise':</span> <span class="pre">'printMofeMoleculeWise',</span> <span class="pre">'printpawrealspacewavefunction':</span> <span class="pre">'printPAWRealSpaceWavefunction',</span> <span class="pre">'printtotalspilling':</span> <span class="pre">'printTotalSpilling',</span> <span class="pre">'realspacehamiltonian':</span> <span class="pre">'realspaceHamiltonian',</span> <span class="pre">'realspaceoverlap':</span> <span class="pre">'realspaceOverlap',</span> <span class="pre">'rmsp':</span> <span class="pre">'RMSp',</span> <span class="pre">'saveprojectiontofile':</span> <span class="pre">'saveProjectionToFile',</span> <span class="pre">'skipcar':</span> <span class="pre">'skipCar',</span> <span class="pre">'skipcobi':</span> <span class="pre">'skipcobi',</span> <span class="pre">'skipcohp':</span> <span class="pre">'skipcohp',</span> <span class="pre">'skipcoop':</span> <span class="pre">'skipcoop',</span> <span class="pre">'skipdos':</span> <span class="pre">'skipdos',</span> <span class="pre">'skipgrosspopulation':</span> <span class="pre">'skipGrossPopulation',</span> <span class="pre">'skipmadelungenergy':</span> <span class="pre">'skipMadelungEnergy',</span> <span class="pre">'skipmofe':</span> <span class="pre">'skipMOFE',</span> <span class="pre">'skipmolecularorbitals':</span> <span class="pre">'skipMolecularOrbitals',</span> <span class="pre">'skippaworthonormalitytest':</span> <span class="pre">'skipPAWOrthonormalityTest',</span> <span class="pre">'skippopulationanalysis':</span> <span class="pre">'skipPopulationAnalysis',</span> <span class="pre">'skipprojection':</span> <span class="pre">'skipProjection',</span> <span class="pre">'skipreorthonormalization':</span> <span class="pre">'skipReOrthonormalization',</span> <span class="pre">'usedecimalplaces':</span> <span class="pre">'useDecimalPlaces',</span> <span class="pre">'useoriginaltetrahedronmethod':</span> <span class="pre">'useOriginalTetrahedronMethod',</span> <span class="pre">'userecommendedbasisfunctions':</span> <span class="pre">'userecommendedbasisfunctions',</span> <span class="pre">'writeatomicorbitals':</span> <span class="pre">'writeAtomicOrbitals',</span> <span class="pre">'writebasisfunctions':</span> <span class="pre">'writeBasisFunctions',</span> <span class="pre">'writematricestofile':</span> <span class="pre">'writeMatricesToFile'}</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.inputs.Lobsterin.AVAILABLE_KEYWORDS"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">BOOLEAN_KEYWORDS</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ClassVar</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">{'autorotate':</span> <span class="pre">'autoRotate',</span> <span class="pre">'bandwisespilling':</span> <span class="pre">'bandwiseSpilling',</span> <span class="pre">'bwdf':</span> <span class="pre">'BWDF',</span> <span class="pre">'bwdfcohp':</span> <span class="pre">'BWDFCOHP',</span> <span class="pre">'densityofenergy':</span> <span class="pre">'DensityOfEnergy',</span> <span class="pre">'donotignoreexcessivebands':</span> <span class="pre">'doNotIgnoreExcessiveBands',</span> <span class="pre">'donotorthogonalizebasis':</span> <span class="pre">'doNotOrthogonalizeBasis',</span> <span class="pre">'donotuseabsolutespilling':</span> <span class="pre">'doNotUseAbsoluteSpilling',</span> <span class="pre">'forceenergyrange':</span> <span class="pre">'forceEnergyRange',</span> <span class="pre">'forcev1hmatrix':</span> <span class="pre">'forceV1HMatrix',</span> <span class="pre">'kpointwisespilling':</span> <span class="pre">'kpointwiseSpilling',</span> <span class="pre">'loadprojectionfromfile':</span> <span class="pre">'loadProjectionFromFile',</span> <span class="pre">'lsodos':</span> <span class="pre">'LSODOS',</span> <span class="pre">'nofftforvisualization':</span> <span class="pre">'noFFTforVisualization',</span> <span class="pre">'nomemorymappedfiles':</span> <span class="pre">'noMemoryMappedFiles',</span> <span class="pre">'onlyreadvasprun.xml':</span> <span class="pre">'onlyReadVasprun.xml',</span> <span class="pre">'printlmosonatoms':</span> <span class="pre">'printLmosOnAtoms',</span> <span class="pre">'printmofeatomwise':</span> <span class="pre">'printMofeAtomWise',</span> <span class="pre">'printmofemoleculewise':</span> <span class="pre">'printMofeMoleculeWise',</span> <span class="pre">'printtotalspilling':</span> <span class="pre">'printTotalSpilling',</span> <span class="pre">'rmsp':</span> <span class="pre">'RMSp',</span> <span class="pre">'saveprojectiontofile':</span> <span class="pre">'saveProjectionToFile',</span> <span class="pre">'skipcar':</span> <span class="pre">'skipCar',</span> <span class="pre">'skipcobi':</span> <span class="pre">'skipcobi',</span> <span class="pre">'skipcohp':</span> <span class="pre">'skipcohp',</span> <span class="pre">'skipcoop':</span> <span class="pre">'skipcoop',</span> <span class="pre">'skipdos':</span> <span class="pre">'skipdos',</span> <span class="pre">'skipgrosspopulation':</span> <span class="pre">'skipGrossPopulation',</span> <span class="pre">'skipmadelungenergy':</span> <span class="pre">'skipMadelungEnergy',</span> <span class="pre">'skipmofe':</span> <span class="pre">'skipMOFE',</span> <span class="pre">'skipmolecularorbitals':</span> <span class="pre">'skipMolecularOrbitals',</span> <span class="pre">'skippaworthonormalitytest':</span> <span class="pre">'skipPAWOrthonormalityTest',</span> <span class="pre">'skippopulationanalysis':</span> <span class="pre">'skipPopulationAnalysis',</span> <span class="pre">'skipprojection':</span> <span class="pre">'skipProjection',</span> <span class="pre">'skipreorthonormalization':</span> <span class="pre">'skipReOrthonormalization',</span> <span class="pre">'useoriginaltetrahedronmethod':</span> <span class="pre">'useOriginalTetrahedronMethod',</span> <span class="pre">'userecommendedbasisfunctions':</span> <span class="pre">'userecommendedbasisfunctions',</span> <span class="pre">'writeatomicorbitals':</span> <span class="pre">'writeAtomicOrbitals',</span> <span class="pre">'writebasisfunctions':</span> <span class="pre">'writeBasisFunctions',</span> <span class="pre">'writematricestofile':</span> <span class="pre">'writeMatricesToFile'}</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.inputs.Lobsterin.BOOLEAN_KEYWORDS"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">FLOAT_KEYWORDS</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ClassVar</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">{'basisrotation':</span> <span class="pre">'basisRotation',</span> <span class="pre">'cohpendenergy':</span> <span class="pre">'COHPendEnergy',</span> <span class="pre">'cohpstartenergy':</span> <span class="pre">'COHPstartEnergy',</span> <span class="pre">'cohpsteps':</span> <span class="pre">'COHPSteps',</span> <span class="pre">'gaussiansmearingwidth':</span> <span class="pre">'gaussianSmearingWidth',</span> <span class="pre">'gridbufferforprinting':</span> <span class="pre">'gridBufferForPrinting',</span> <span class="pre">'griddensityforprinting':</span> <span class="pre">'gridDensityForPrinting',</span> <span class="pre">'usedecimalplaces':</span> <span class="pre">'useDecimalPlaces'}</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.inputs.Lobsterin.FLOAT_KEYWORDS"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">LIST_KEYWORDS</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ClassVar</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">{'basisfunctions':</span> <span class="pre">'basisfunctions',</span> <span class="pre">'cobibetween':</span> <span class="pre">'cobiBetween',</span> <span class="pre">'cohpbetween':</span> <span class="pre">'cohpbetween',</span> <span class="pre">'createfatband':</span> <span class="pre">'createFatband',</span> <span class="pre">'customstoforatom':</span> <span class="pre">'customSTOforAtom',</span> <span class="pre">'printlmosonatomswriteatomicdensities':</span> <span class="pre">'printLmosOnAtomswriteAtomicDensities'}</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.inputs.Lobsterin.LIST_KEYWORDS"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">STRING_KEYWORDS</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ClassVar</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">{'basisset':</span> <span class="pre">'basisSet',</span> <span class="pre">'cohpgenerator':</span> <span class="pre">'cohpGenerator',</span> <span class="pre">'ewaldsum':</span> <span class="pre">'EwaldSum',</span> <span class="pre">'kspacecohp':</span> <span class="pre">'kSpaceCOHP',</span> <span class="pre">'printlcaorealspacewavefunction':</span> <span class="pre">'printLCAORealSpaceWavefunction',</span> <span class="pre">'printpawrealspacewavefunction':</span> <span class="pre">'printPAWRealSpaceWavefunction',</span> <span class="pre">'realspacehamiltonian':</span> <span class="pre">'realspaceHamiltonian',</span> <span class="pre">'realspaceoverlap':</span> <span class="pre">'realspaceOverlap'}</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.inputs.Lobsterin.STRING_KEYWORDS"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/inputs.py#L276-L281"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.inputs.Lobsterin.as_dict"
class="headerlink" title="Link to this definition"></a>  
MSONable dict.

<span class="sig-name descname"><span class="pre">diff</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Self</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/inputs.py#L205-L248"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.inputs.Lobsterin.diff" class="headerlink"
title="Link to this definition"></a>  
Compare two Lobsterin and find which parameters are the same. Similar to
the diff method of Incar.

Parameters<span class="colon">:</span>  
**other** (<a href="#pymatgen.io.lobster.inputs.Lobsterin"
class="reference internal"
title="pymatgen.io.lobster.inputs.Lobsterin"><em>Lobsterin</em></a>) –
Lobsterin object to compare to.

Returns<span class="colon">:</span>  
{“Same”: same_params, “Different”: diff_params}

Return type<span class="colon">:</span>  
dict

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/inputs.py#L283-L292"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.inputs.Lobsterin.from_dict"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
**dct** (*dict*) – Dict representation.

Returns<span class="colon">:</span>  
Lobsterin

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">lobsterin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/inputs.py#L581-L630"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.inputs.Lobsterin.from_file"
class="headerlink" title="Link to this definition"></a>  
Create Lobsterin from lobsterin file.

Parameters<span class="colon">:</span>  
**lobsterin** (*PathLike*) – path to lobsterin.

Returns<span class="colon">:</span>  
Lobsterin object

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">get_all_possible_basis_functions</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.IStructure"
class="reference internal"
title="pymatgen.core.structure.IStructure"><span
class="pre">IStructure</span></a></span>*, *<span class="n"><span class="pre">potcar_symbols</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">address_basis_file_min</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">address_basis_file_max</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/inputs.py#L396-L433"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.inputs.Lobsterin.get_all_possible_basis_functions"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
- **structure** – Structure object

- **potcar_symbols** – list of the potcar symbols

- **address_basis_file_min** – path to file with the minimum required
  basis by the POTCAR

- **address_basis_file_max** – path to file with the largest possible
  basis of the POTCAR.

Returns<span class="colon">:</span>  
Can be used to create new Lobsterin objects in  
standard_calculations_from_vasp_files as dict_for_basis

Return type<span class="colon">:</span>  
list\[dict\]

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">get_basis</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.IStructure"
class="reference internal"
title="pymatgen.core.structure.IStructure"><span
class="pre">IStructure</span></a></span>*, *<span class="n"><span class="pre">potcar_symbols</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">address_basis_file</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/inputs.py#L359-L394"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.inputs.Lobsterin.get_basis"
class="headerlink" title="Link to this definition"></a>  
Get the basis functions from given potcar_symbols, e.g., \[“Fe_pv”,
“Si”\].

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  Structure object

- **potcar_symbols** – list of potcar symbols

- **address_basis_file** (*PathLike*) – path to the basis file

Returns<span class="colon">:</span>  
basis

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">standard_calculations_from_vasp_files</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">POSCAR_input</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'POSCAR'</span></span>*, *<span class="n"><span class="pre">INCAR_input</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'INCAR'</span></span>*, *<span class="n"><span class="pre">POTCAR_input</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">Vasprun_output</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'vasprun.xml'</span></span>*, *<span class="n"><span class="pre">dict_for_basis</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">option</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'standard'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/inputs.py#L669-L858"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.inputs.Lobsterin.standard_calculations_from_vasp_files"
class="headerlink" title="Link to this definition"></a>  
Generate lobsterin with standard settings.

Parameters<span class="colon">:</span>  
- **POSCAR_input** (*PathLike*) – path to POSCAR

- **INCAR_input** (*PathLike*) – path to INCAR

- **POTCAR_input** (*PathLike*) – path to POTCAR

- **Vasprun_output** (*PathLike*) – path to vasprun.xml

- **dict_for_basis** (*dict*) – can be provided: it should look the
  following: dict_for_basis={“Fe”:’3p 3d 4s 4f’, “C”: ‘2s 2p’} and will
  overwrite all settings from POTCAR_input

- **option** (*str*) – ‘standard’ will start a normal LOBSTER run where
  COHPs, COOPs, DOS, CHARGE etc. will be calculated
  ‘standard_with_energy_range_from_vasprun’ will start a normal LOBSTER
  run for entire energy range of VASP static run. vasprun.xml file needs
  to be in current directory. ‘standard_from_projection’ will start a
  normal LOBSTER run from a projection ‘standard_with_fatband’ will do a
  fatband calculation, run over all orbitals ‘onlyprojection’ will only
  do a projection ‘onlydos’ will only calculate a projected dos
  ‘onlycohp’ will only calculate cohp ‘onlycoop’ will only calculate
  coop ‘onlycohpcoop’ will only calculate cohp and coop

Returns<span class="colon">:</span>  
Lobsterin with standard settings

<span class="sig-name descname"><span class="pre">write_INCAR</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">incar_input</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'INCAR'</span></span>*, *<span class="n"><span class="pre">incar_output</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'INCAR.lobster'</span></span>*, *<span class="n"><span class="pre">poscar_input</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'POSCAR'</span></span>*, *<span class="n"><span class="pre">isym</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="p"><span class="pre">-</span></span><span class="m"><span class="pre">1</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="m"><span class="pre">0</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">further_settings</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/inputs.py#L320-L357"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.inputs.Lobsterin.write_INCAR"
class="headerlink" title="Link to this definition"></a>  
Write INCAR file. Will only make the run static, insert NBANDS, set
ISYM=0, LWAVE=True and you have to check for the rest.

Parameters<span class="colon">:</span>  
- **incar_input** (*PathLike*) – path to input INCAR

- **incar_output** (*PathLike*) – path to output INCAR

- **poscar_input** (*PathLike*) – path to input POSCAR

- **isym** (*-1* *\|* *0*) – ISYM value.

- **further_settings** (*dict*) – A dict can be used to include further
  settings, e.g. {“ISMEAR”:-5}

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">write_KPOINTS</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">POSCAR_input</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'POSCAR'</span></span>*, *<span class="n"><span class="pre">KPOINTS_output</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'KPOINTS.lobster'</span></span>*, *<span class="n"><span class="pre">reciprocal_density</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">100</span></span>*, *<span class="n"><span class="pre">isym</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="p"><span class="pre">-</span></span><span class="m"><span class="pre">1</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="m"><span class="pre">0</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">from_grid</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">input_grid</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">(5,</span> <span class="pre">5,</span> <span class="pre">5)</span></span>*, *<span class="n"><span class="pre">line_mode</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">kpoints_line_density</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">20</span></span>*, *<span class="n"><span class="pre">symprec</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.01</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/inputs.py#L454-L579"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.inputs.Lobsterin.write_KPOINTS"
class="headerlink" title="Link to this definition"></a>  
Write a gamma-centered KPOINTS file for LOBSTER.

Parameters<span class="colon">:</span>  
- **POSCAR_input** (*PathLike*) – path to POSCAR

- **KPOINTS_output** (*PathLike*) – path to output KPOINTS

- **reciprocal_density** (*int*) – Grid density

- **isym** (*-1* *\|* *0*) – ISYM value.

- **from_grid** (*bool*) – If True KPOINTS will be generated with the
  help of a grid given in input_grid. Otherwise, they will be generated
  from the reciprocal_density

- **input_grid** (*tuple*) – grid to generate the KPOINTS file

- **line_mode** (*bool*) – If True, band structure will be generated

- **kpoints_line_density** (*int*) – density of the lines in the band
  structure

- **symprec** (*float*) – precision to determine symmetry

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">write_POSCAR_with_standard_primitive</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">POSCAR_input</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'POSCAR'</span></span>*, *<span class="n"><span class="pre">POSCAR_output</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'POSCAR.lobster'</span></span>*, *<span class="n"><span class="pre">symprec</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.01</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/inputs.py#L435-L452"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.inputs.Lobsterin.write_POSCAR_with_standard_primitive"
class="headerlink" title="Link to this definition"></a>  
Write a POSCAR with the standard primitive cell. This is needed to
arrive at the correct kpath.

Parameters<span class="colon">:</span>  
- **POSCAR_input** (*PathLike*) – Input POSCAR file

- **POSCAR_output** (*PathLike*) – Output POSCAR file

- **symprec** (*float*) – precision to find symmetry

<span class="sig-name descname"><span class="pre">write_lobsterin</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">path</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'lobsterin'</span></span>*, *<span class="n"><span class="pre">overwritedict</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/inputs.py#L250-L274"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.inputs.Lobsterin.write_lobsterin"
class="headerlink" title="Link to this definition"></a>  
Write a lobsterin file, and recover keys to Camel case.

Parameters<span class="colon">:</span>  
- **path** (*str*) – filename of the output lobsterin file

- **overwritedict** (*dict*) – dict that can be used to update
  lobsterin, e.g. {“skipdos”: True}

<!-- -->

<span class="sig-name descname"><span class="pre">get_all_possible_basis_combinations</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">min_basis</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span>*, *<span class="n"><span class="pre">max_basis</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/inputs.py#L861-L902"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.inputs.get_all_possible_basis_combinations"
class="headerlink" title="Link to this definition"></a>  
Get all possible basis combinations.

Parameters<span class="colon">:</span>  
- **min_basis** – list of basis entries: e.g., \[“Si 3p 3s”\]

- **max_basis** – list of basis entries: e.g., \[“Si 3p 3s”\].

Returns<span class="colon">:</span>  
all possible combinations of basis functions, e.g. \[\[“Si 3p 3s”\]\]

Return type<span class="colon">:</span>  
list\[list\[str\]\]

</div>

<div id="module-pymatgen.io.lobster.lobsterenv" class="section">

<span id="pymatgen-io-lobster-lobsterenv-module"></span>

## pymatgen.io.lobster.lobsterenv module<a href="#module-pymatgen.io.lobster.lobsterenv" class="headerlink"
title="Link to this heading"></a>

This module provides classes to perform analyses of the local
environments (e.g., finding near neighbors) of single sites in molecules
and structures based on bonding analysis with LOBSTER.

If you use this module, please cite: J. George, G. Petretto, A. Naik, M.
Esters, A. J. Jackson, R. Nelson, R. Dronskowski, G.-M. Rignanese, G.
Hautier, “Automated Bonding Analysis with Crystal Orbital Hamilton
Populations”, ChemPlusChem 2022, e202200123, DOI:
10.1002/cplu.202200123.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ICOHPNeighborsInfo</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">total_icohp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">list_icohps</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">n_bonds</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">labels</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">atoms</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">central_isites</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/lobsterenv.py#L1505-L1524"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.lobsterenv.ICOHPNeighborsInfo"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`NamedTuple`</span>

Tuple to record information on relevant bonds.

Parameters<span class="colon">:</span>  
- **total_icohp** (*float*) – Sum of ICOHP values of neighbors to the
  selected sites (given by the index in structure).

- **list_icohps** (*list*) – Summed ICOHP values for all identified
  interactions with neighbors.

- **n_bonds** (*int*) – Number of identified bonds to the selected
  sites.

- **labels** (*list\[str\]*) – Labels (from ICOHPLIST) for all
  identified bonds.

- **atoms** (*list\[list\[str\]\]*) – Lists describing the species
  present (from ICOHPLIST) in the identified interactions , e.g.
  \[“Ag3”, “O5”\].

- **central_isites** (*list\[int\]*) – The central site indexes for each
  identified interaction.

Create new instance of ICOHPNeighborsInfo(total_icohp, list_icohps,
n_bonds, labels, atoms, central_isites)

<span class="sig-name descname"><span class="pre">atoms</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/lobsterenv.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.lobsterenv.ICOHPNeighborsInfo.atoms"
class="headerlink" title="Link to this definition"></a>  
Alias for field number 4

<span class="sig-name descname"><span class="pre">central_isites</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/lobsterenv.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.lobsterenv.ICOHPNeighborsInfo.central_isites"
class="headerlink" title="Link to this definition"></a>  
Alias for field number 5

<span class="sig-name descname"><span class="pre">labels</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/lobsterenv.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.lobsterenv.ICOHPNeighborsInfo.labels"
class="headerlink" title="Link to this definition"></a>  
Alias for field number 3

<span class="sig-name descname"><span class="pre">list_icohps</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/lobsterenv.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.lobsterenv.ICOHPNeighborsInfo.list_icohps"
class="headerlink" title="Link to this definition"></a>  
Alias for field number 1

<span class="sig-name descname"><span class="pre">n_bonds</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/lobsterenv.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.lobsterenv.ICOHPNeighborsInfo.n_bonds"
class="headerlink" title="Link to this definition"></a>  
Alias for field number 2

<span class="sig-name descname"><span class="pre">total_icohp</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/lobsterenv.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.lobsterenv.ICOHPNeighborsInfo.total_icohp"
class="headerlink" title="Link to this definition"></a>  
Alias for field number 0

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">LobsterLightStructureEnvironments</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">strategy</span></span>*, *<span class="n"><span class="pre">coordination_environments</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">all_nbs_sites</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">neighbors_sets</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">structure</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">valences</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">valences_origin</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/lobsterenv.py#L1369-L1502"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.lobsterenv.LobsterLightStructureEnvironments"
class="headerlink" title="Link to this definition"></a>  
Bases: <a
href="pymatgen.analysis.chemenv.coordination_environments.html#pymatgen.analysis.chemenv.coordination_environments.structure_environments.LightStructureEnvironments"
class="reference internal"
title="pymatgen.analysis.chemenv.coordination_environments.structure_environments.LightStructureEnvironments"><span
class="pre"><code
class="sourceCode python">LightStructureEnvironments</code></span></a>

Store LightStructureEnvironments based on LOBSTER outputs.

Constructor for the LightStructureEnvironments object.

Parameters<span class="colon">:</span>  
- **strategy** – ChemEnv strategy used to get the environments.

- **coordination_environments** – The coordination environments
  identified.

- **all_nbs_sites** – All the possible neighbors for each site in the
  structure.

- **neighbors_sets** – The neighbors sets of each site in the structure.

- **structure** – The structure.

- **valences** – The valences used to get the environments (if needed).

- **valences_origin** – How the valences were obtained (e.g. from the
  Bond-valence analysis or from the original structure).

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/lobsterenv.py#L1478-L1502"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.lobsterenv.LobsterLightStructureEnvironments.as_dict"
class="headerlink" title="Link to this definition"></a>  
Bson-serializable dict representation of the object.

Returns<span class="colon">:</span>  
Bson-serializable dict representation.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_Lobster</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">list_ce_symbol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">list_csm</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">list_permutation</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span>*, *<span class="n"><span class="pre">list_neighsite</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
class="reference internal"
title="pymatgen.core.sites.PeriodicSite"><span
class="pre">PeriodicSite</span></a><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">list_neighisite</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.IStructure"
class="reference internal"
title="pymatgen.core.structure.IStructure"><span
class="pre">IStructure</span></a></span>*, *<span class="n"><span class="pre">valences</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/lobsterenv.py#L1372-L1471"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.lobsterenv.LobsterLightStructureEnvironments.from_Lobster"
class="headerlink" title="Link to this definition"></a>  
Set up a LightStructureEnvironments from LOBSTER.

Parameters<span class="colon">:</span>  
- **list_ce_symbol** (*list\[str\]*) – Coordination environments
  symbols.

- **list_csm** (*list\[float\]*) – Continuous symmetry measures.

- **list_permutation** (*list*) – Permutations.

- **list_neighsite**
  (*list\[*<a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
  class="reference internal"
  title="pymatgen.core.sites.PeriodicSite"><em>PeriodicSite</em></a>*\]*)
  – Neighboring sites.

- **list_neighisite** (*list\[list\[int\]\]*) – Neighboring sites
  indexes.

- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  Structure object.

- **valences** (*list\[float\]*) – Valences.

Returns<span class="colon">:</span>  
LobsterLightStructureEnvironments

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">uniquely_determines_coordination_environments</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="k"><span class="pre">True</span></span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/lobsterenv.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.lobsterenv.LobsterLightStructureEnvironments.uniquely_determines_coordination_environments"
class="headerlink" title="Link to this definition"></a>  
Whether the coordination environments are uniquely determined.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">LobsterNeighbors</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.IStructure"
class="reference internal"
title="pymatgen.core.structure.IStructure"><span
class="pre">IStructure</span></a></span>*, *<span class="n"><span class="pre">filename_icohp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'ICOHPLIST.lobster'</span></span>*, *<span class="n"><span class="pre">obj_icohp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.lobster.outputs.Icohplist"
class="reference internal"
title="pymatgen.io.lobster.outputs.Icohplist"><span
class="pre">Icohplist</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">are_coops</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">are_cobis</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">valences</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">limits</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">additional_condition</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="m"><span class="pre">0</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="m"><span class="pre">1</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="m"><span class="pre">2</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="m"><span class="pre">3</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="m"><span class="pre">4</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="m"><span class="pre">5</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="m"><span class="pre">6</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">only_bonds_to</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">perc_strength_icohp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.15</span></span>*, *<span class="n"><span class="pre">noise_cutoff</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.1</span></span>*, *<span class="n"><span class="pre">valences_from_charges</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">filename_charge</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">obj_charge</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.lobster.outputs.Charge" class="reference internal"
title="pymatgen.io.lobster.outputs.Charge"><span
class="pre">Charge</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">which_charge</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'Mulliken'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'Loewdin'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'Mulliken'</span></span>*, *<span class="n"><span class="pre">adapt_extremum_to_add_cond</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">add_additional_data_sg</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">filename_blist_sg1</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">filename_blist_sg2</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">id_blist_sg1</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'icoop'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'icobi'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'icoop'</span></span>*, *<span class="n"><span class="pre">id_blist_sg2</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'icoop'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'icobi'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'icobi'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/lobsterenv.py#L60-L1366"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.lobsterenv.LobsterNeighbors"
class="headerlink" title="Link to this definition"></a>  
Bases: <a
href="pymatgen.analysis.html#pymatgen.analysis.local_env.NearNeighbors"
class="reference internal"
title="pymatgen.analysis.local_env.NearNeighbors"><span
class="pre"><code
class="sourceCode python">NearNeighbors</code></span></a>

This class combines capabilities from LocalEnv and ChemEnv to determine
coordination environments based on bonding analysis.

Parameters<span class="colon">:</span>  
- **filename_icohp** (*PathLike*) – Path to ICOHPLIST.lobster or
  ICOOPLIST.lobster or ICOBILIST.lobster.

- **obj_icohp** (<a href="#pymatgen.io.lobster.outputs.Icohplist"
  class="reference internal"
  title="pymatgen.io.lobster.outputs.Icohplist"><em>Icohplist</em></a>)
  – Icohplist object.

- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  Typically constructed by Structure.from_file(“POSCAR”).

- **are_coops** (*bool*) – Whether the file is a ICOOPLIST.lobster
  (True) or a ICOHPLIST.lobster (False). Only tested for
  ICOHPLIST.lobster so far.

- **are_cobis** (*bool*) – Whether the file is a ICOBILIST.lobster
  (True) or a ICOHPLIST.lobster (False).

- **valences** (*list\[float\]*) – Valence/charge for each element.

- **limits** (*tuple\[float,* *float\]*) – Range to decide which ICOHPs
  (ICOOP or ICOBI) should be considered.

- **additional_condition** (*int*) –

  Additional condition that decides which kind of bonds will be
  considered:

  > <div>
  >
  > 0 - NO_ADDITIONAL_CONDITION 1 - ONLY_ANION_CATION_BONDS 2 -
  > NO_ELEMENT_TO_SAME_ELEMENT_BONDS 3 -
  > ONLY_ANION_CATION_BONDS_AND_NO_ELEMENT_TO_SAME_ELEMENT_BONDS 4 -
  > ONLY_ELEMENT_TO_OXYGEN_BONDS 5 - DO_NOT_CONSIDER_ANION_CATION_BONDS
  > 6 - ONLY_CATION_CATION_BONDS
  >
  > </div>

- **only_bonds_to** (*list\[str\]*) – Only consider bonds to certain
  elements (e.g. \[“O”\] for oxygen).

- **perc_strength_icohp** (*float*) – If no “limits” are given, this
  will decide which ICOHPs will be considered (relative to the strongest
  ICOHP/ICOOP/ICOBI).

- **noise_cutoff** (*float*) – The lower limit of ICOHPs considered.

- **valences_from_charges** (*bool*) – If True and path to
  CHARGE.lobster is provided, will use LOBSTER charges (Mulliken)
  instead of valences.

- **filename_charge** (*PathLike*) – Path to Charge.lobster.

- **obj_charge**
  (<a href="#pymatgen.io.lobster.outputs.Charge" class="reference internal"
  title="pymatgen.io.lobster.outputs.Charge"><em>Charge</em></a>) –
  Charge object.

- **which_charge** (*"Mulliken"* *\|* *"Loewdin"*) – Source of charge.

- **adapt_extremum_to_add_cond** (*bool*) – Whether to adapt the limits
  to only focus on the bonds determined by the additional condition.

- **add_additional_data_sg** (*bool*) – Add the information from
  filename_add_bondinglist_sg1.

- **filename_blist_sg1** (*PathLike*) – Path to additional ICOOP, ICOBI
  data for structure graphs.

- **filename_blist_sg2** (*PathLike*) – Path to additional ICOOP, ICOBI
  data for structure graphs.

- **id_blist_sg1** (*"icoop"* *\|* *"icobi"*) – Identity of data in
  filename_blist_sg1.

- **id_blist_sg2** (*"icoop"* *\|* *"icobi"*) – Identity of data in
  filename_blist_sg2.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">anion_types</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">set</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.periodic_table.Element"
class="reference internal"
title="pymatgen.core.periodic_table.Element"><span
class="pre">Element</span></a><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/lobsterenv.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.lobsterenv.LobsterNeighbors.anion_types"
class="headerlink" title="Link to this definition"></a>  
The set of anion types in crystal structure.

Returns<span class="colon">:</span>  
Anions in the crystal structure.

Return type<span class="colon">:</span>  
set\[<a href="pymatgen.core.html#pymatgen.core.periodic_table.Element"
class="reference internal"
title="pymatgen.core.periodic_table.Element">Element</a>\]

<span class="sig-name descname"><span class="pre">get_anion_types</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">set</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.periodic_table.Element"
class="reference internal"
title="pymatgen.core.periodic_table.Element"><span
class="pre">Element</span></a><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../../../.venv/lib/python3.11/site-packages/monty/dev.py#L262-L264"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.lobsterenv.LobsterNeighbors.get_anion_types"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">get_info_cohps_to_neighbors</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">path_to_cohpcar</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'COHPCAR.lobster'</span></span>*, *<span class="n"><span class="pre">obj_cohpcar</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a
href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.cohp.CompleteCohp"
class="reference internal"
title="pymatgen.electronic_structure.cohp.CompleteCohp"><span
class="pre">CompleteCohp</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">isites</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">only_bonds_to</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">onlycation_isites</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">per_bond</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">summed_spin_channels</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><a
href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.cohp.CompleteCohp"
class="reference internal"
title="pymatgen.electronic_structure.cohp.CompleteCohp"><span
class="pre">CompleteCohp</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/lobsterenv.py#L505-L620"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.lobsterenv.LobsterNeighbors.get_info_cohps_to_neighbors"
class="headerlink" title="Link to this definition"></a>  
Get the COHPs (COOPs or COBIs) as a summed Cohp object and a label from
all sites mentioned in isites with neighbors.

Parameters<span class="colon">:</span>  
- **path_to_cohpcar** (*PathLike*) – Path to COHPCAR/COOPCAR/COBICAR.

- **obj_cohpcar** (<a
  href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.cohp.CompleteCohp"
  class="reference internal"
  title="pymatgen.electronic_structure.cohp.CompleteCohp"><em>CompleteCohp</em></a>)
  – CompleteCohp object.

- **isites** (*list\[int\]*) – The indexes of the sites.

- **only_bonds_to** (*list\[str\]*) – Only show COHPs to selected
  element, e.g. \[“O”\].

- **onlycation_isites** (*bool*) – If isites is None, only cation sites
  will be returned.

- **per_bond** (*bool*) – Whether to normalize per bond.

- **summed_spin_channels** (*bool*) – Whether to sum both spin channels.

Returns<span class="colon">:</span>  
Label for COHP. CompleteCohp: Describe all COHPs/COOPs/COBIs of the
sites

> <div>
>
> as given by isites and the other arguments.
>
> </div>

Return type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">get_info_icohps_between_neighbors</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">isites</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">onlycation_isites</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.lobster.lobsterenv.ICOHPNeighborsInfo"
class="reference internal"
title="pymatgen.io.lobster.lobsterenv.ICOHPNeighborsInfo"><span
class="pre">ICOHPNeighborsInfo</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/lobsterenv.py#L641-L749"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.lobsterenv.LobsterNeighbors.get_info_icohps_between_neighbors"
class="headerlink" title="Link to this definition"></a>  
Get interactions between neighbors of certain sites.

Parameters<span class="colon">:</span>  
- **isites** (*list\[int\]*) – Site IDs. If is None, all sites will be
  used.

- **onlycation_isites** (*bool*) – Only use cations, if isite is None.

Returns<span class="colon">:</span>  
ICOHPNeighborsInfo

<span class="sig-name descname"><span class="pre">get_info_icohps_to_neighbors</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">isites</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">onlycation_isites</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.lobster.lobsterenv.ICOHPNeighborsInfo"
class="reference internal"
title="pymatgen.io.lobster.lobsterenv.ICOHPNeighborsInfo"><span
class="pre">ICOHPNeighborsInfo</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/lobsterenv.py#L393-L449"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.lobsterenv.LobsterNeighbors.get_info_icohps_to_neighbors"
class="headerlink" title="Link to this definition"></a>  
Get information on the ICOHPs of neighbors for certain sites as
identified by their site id.

This is useful for plotting the COHPs (ICOOPLIST.lobster/
ICOHPLIST.lobster/ICOBILIST.lobster) of a site in the structure.

Parameters<span class="colon">:</span>  
- **isites** (*list\[int\]*) – Site IDs. If is None, all isites will be
  used to add the ICOHPs of the neighbors.

- **onlycation_isites** (*bool*) – If True and if isite is None, will
  only analyse the cations sites.

Returns<span class="colon">:</span>  
ICOHPNeighborsInfo

<span class="sig-name descname"><span class="pre">get_light_structure_environment</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">only_cation_environments</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">only_indices</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a
href="#pymatgen.io.lobster.lobsterenv.LobsterLightStructureEnvironments"
class="reference internal"
title="pymatgen.io.lobster.lobsterenv.LobsterLightStructureEnvironments"><span
class="pre">LobsterLightStructureEnvironments</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/lobsterenv.py#L298-L391"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.lobsterenv.LobsterNeighbors.get_light_structure_environment"
class="headerlink" title="Link to this definition"></a>  
Get a LobsterLightStructureEnvironments object if the structure only
contains coordination environments smaller 13.

Parameters<span class="colon">:</span>  
- **only_cation_environments** (*bool*) – Only return data for cations.

- **only_indices** (*list\[int\]*) – Only evaluate indexes in this list.

Returns<span class="colon">:</span>  
LobsterLightStructureEnvironments

<span class="sig-name descname"><span class="pre">get_nn_info</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.IStructure"
class="reference internal"
title="pymatgen.core.structure.IStructure"><span
class="pre">IStructure</span></a></span>*, *<span class="n"><span class="pre">n</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">use_weights</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/lobsterenv.py#L266-L296"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.lobsterenv.LobsterNeighbors.get_nn_info"
class="headerlink" title="Link to this definition"></a>  
Get coordination number (CN) of site by index.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  Input structure.

- **n** (*int*) – Index of site for which to determine CN.

- **use_weights** (*bool*) – Whether to use weights for computing the CN
  (True), or each coordinated site has equal weight (False). The former
  is not implemented yet.

Raises<span class="colon">:</span>  
**ValueError** – If use_weights is True, or if arg “structure” and
structure used to initialize LobsterNeighbors have different lengths.

Returns<span class="colon">:</span>  
coordination number and a list of nearest neighbors.

Return type<span class="colon">:</span>  
dict\[str, Any\]

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">molecules_allowed</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="k"><span class="pre">False</span></span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/lobsterenv.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.lobsterenv.LobsterNeighbors.molecules_allowed"
class="headerlink" title="Link to this definition"></a>  
Whether this LobsterNeighbors class can be used with Molecule objects.

<span class="sig-name descname"><span class="pre">plot_cohps_of_neighbors</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">path_to_cohpcar</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'COHPCAR.lobster'</span></span>*, *<span class="n"><span class="pre">obj_cohpcar</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a
href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.cohp.CompleteCohp"
class="reference internal"
title="pymatgen.electronic_structure.cohp.CompleteCohp"><span
class="pre">CompleteCohp</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">isites</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">onlycation_isites</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">only_bonds_to</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">per_bond</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">summed_spin_channels</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">xlim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ylim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">(-10,</span> <span class="pre">6)</span></span>*, *<span class="n"><span class="pre">integrated</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">mpl.axes.Axes</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/lobsterenv.py#L451-L503"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.lobsterenv.LobsterNeighbors.plot_cohps_of_neighbors"
class="headerlink" title="Link to this definition"></a>  
Plot summed COHPs or COBIs or COOPs.

Please be careful in the spin polarized case (plots might overlap).

Parameters<span class="colon">:</span>  
- **path_to_cohpcar** (*PathLike*) – Path to COHPCAR or COOPCAR or
  COBICAR.

- **obj_cohpcar** (<a
  href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.cohp.CompleteCohp"
  class="reference internal"
  title="pymatgen.electronic_structure.cohp.CompleteCohp"><em>CompleteCohp</em></a>)
  – CompleteCohp object

- **isites** (*list\[int\]*) – Site IDs. If empty, all sites will be
  used to add the ICOHPs of the neighbors.

- **onlycation_isites** (*bool*) – Only use cations, if isite is empty.

- **only_bonds_to** (*list\[str\]*) – Only anions in this list will be
  considered.

- **per_bond** (*bool*) – Whether to plot a normalization of the plotted
  COHP per number of bond (True), or the sum (False).

- **xlim** (*tuple\[float,* *float\]*) – Limits of x values.

- **ylim** (*tuple\[float,* *float\]*) – Limits of y values.

- **integrated** (*bool*) – Whether to show integrated COHP instead of
  COHP.

Returns<span class="colon">:</span>  
plt of the COHPs or COBIs or COOPs.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">structures_allowed</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="k"><span class="pre">True</span></span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/lobsterenv.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.lobsterenv.LobsterNeighbors.structures_allowed"
class="headerlink" title="Link to this definition"></a>  
Whether this LobsterNeighbors class can be used with Structure objects.

</div>

<div id="module-pymatgen.io.lobster.outputs" class="section">

<span id="pymatgen-io-lobster-outputs-module"></span>

## pymatgen.io.lobster.outputs module<a href="#module-pymatgen.io.lobster.outputs" class="headerlink"
title="Link to this heading"></a>

Module for reading Lobster output files. For more information on LOBSTER
see www.cohp.de.

If you use this module, please cite: J. George, G. Petretto, A. Naik, M.
Esters, A. J. Jackson, R. Nelson, R. Dronskowski, G.-M. Rignanese, G.
Hautier, “Automated Bonding Analysis with Crystal Orbital Hamilton
Populations”, ChemPlusChem 2022, e202200123, DOI:
10.1002/cplu.202200123.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Bandoverlaps</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'bandOverlaps.lobster'</span></span>*, *<span class="n"><span class="pre">band_overlaps_dict</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><a
href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">max_deviation</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/outputs.py#L1603-L1747"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Bandoverlaps" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Read bandOverlaps.lobster files, which are not created during every
LOBSTER run.

<span class="sig-name descname"><span class="pre">band_overlaps_dict</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Bandoverlaps.band_overlaps_dict"
class="headerlink" title="Link to this definition"></a>  
A dictionary containing the band overlap data of the form: {spin:
{“kpoint as string”: {“maxDeviation”: float that describes the max
deviation, “matrix”: 2D array of the size number of bands times number
of bands including the overlap matrices with}}}.

Type<span class="colon">:</span>  
dict\[<a
href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin">Spin</a>, Dict\[str,
Dict\[str, Union\[float, NDArray\]\]\]\]

<span class="sig-name descname"><span class="pre">max_deviation</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Bandoverlaps.max_deviation"
class="headerlink" title="Link to this definition"></a>  
The maximal deviation for each problematic kpoint.

Type<span class="colon">:</span>  
list\[float\]

Parameters<span class="colon">:</span>  
- **filename** (*PathLike*) – The “bandOverlaps.lobster” file.

- **band_overlaps_dict** –

  The band overlap data of the form: {

  > <div>
  >
  > spin: {  
  > “k_points” : list of k-point array, “max_deviations”: list of max
  > deviations associated with each k-point, “matrices”: list of the
  > overlap matrices associated with each k-point,
  >
  > }
  >
  > </div>

  }.

- **max_deviation** (*list\[float\]*) – The maximal deviations for each
  problematic k-point.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">bandoverlapsdict</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Bandoverlaps.bandoverlapsdict"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">has_good_quality_check_occupied_bands</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">number_occ_bands_spin_up</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">number_occ_bands_spin_down</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">spin_polarized</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">limit_deviation</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.1</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/outputs.py#L1706-L1742"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.outputs.Bandoverlaps.has_good_quality_check_occupied_bands"
class="headerlink" title="Link to this definition"></a>  
Check if the deviation from the ideal bandoverlap of all occupied bands
is smaller or equal to limit_deviation.

Parameters<span class="colon">:</span>  
- **number_occ_bands_spin_up** (*int*) – Number of occupied bands of
  spin up.

- **number_occ_bands_spin_down** (*int*) – Number of occupied bands of
  spin down.

- **spin_polarized** (*bool*) – Whether this is a spin polarized
  calculation.

- **limit_deviation** (*float*) – Upper limit of the maxDeviation.

Returns<span class="colon">:</span>  
True if the quality of the projection is good.

Return type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">has_good_quality_maxDeviation</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">limit_maxDeviation</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.1</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/outputs.py#L1694-L1704"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.outputs.Bandoverlaps.has_good_quality_maxDeviation"
class="headerlink" title="Link to this definition"></a>  
Check if the maxDeviation from the ideal bandoverlap is smaller or equal
to a limit.

Parameters<span class="colon">:</span>  
**limit_maxDeviation** (*float*) – Upper Limit of the maxDeviation.

Returns<span class="colon">:</span>  
Whether the ideal bandoverlap is smaller or equal to the limit.

Return type<span class="colon">:</span>  
bool

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Bwdf</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'BWDF.lobster'</span></span>*, *<span class="n"><span class="pre">centers</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">NDArray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">bwdf</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><a
href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">NDArray</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">bin_width</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/outputs.py#L2458-L2505"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Bwdf" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Read BWDF.lobster/BWDFCOHP.lobster file generated by LOBSTER.

<span class="sig-name descname"><span class="pre">centers</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Bwdf.centers" class="headerlink"
title="Link to this definition"></a>  
Bond length centers for the distribution.

Type<span class="colon">:</span>  
NDArray

<span class="sig-name descname"><span class="pre">bwdf</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Bwdf.bwdf" class="headerlink"
title="Link to this definition"></a>  
Bond weighted distribution function.

Type<span class="colon">:</span>  
dict\[<a
href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin">Spin</a>, NDArray\]

<span class="sig-name descname"><span class="pre">bin_width</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Bwdf.bin_width" class="headerlink"
title="Link to this definition"></a>  
Bin width used for computing the distribution by LOBSTER.

Type<span class="colon">:</span>  
float

Parameters<span class="colon">:</span>  
- **filename** (*PathLike*) – The “BWDF.lobster” file. Can also read
  BWDFCOHP.lobster.

- **centers** (*NDArray*) – Bond length centers for the distribution.

- **bwdf** (*dict\[*<a
  href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.core.Spin"
  class="reference internal"
  title="pymatgen.electronic_structure.core.Spin"><em>Spin</em></a>*,*
  *NDArray\]*) – Bond weighted distribution function.

- **bin_width** (*float*) – Bin width used for computing the
  distribution by LOBSTER.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Charge</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'CHARGE.lobster'</span></span>*, *<span class="n"><span class="pre">is_lcfo</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">num_atoms</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">atomlist</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">types</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">mulliken</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">loewdin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/outputs.py#L885-L968"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Charge" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Read CHARGE.lobster/ CHARGE.LCFO.lobster files generated by LOBSTER.

<span class="sig-name descname"><span class="pre">atomlist</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Charge.atomlist"
class="headerlink" title="Link to this definition"></a>  
List of atoms in CHARGE.lobster.

Type<span class="colon">:</span>  
list\[str\]

<span class="sig-name descname"><span class="pre">is_lcfo</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Charge.is_lcfo" class="headerlink"
title="Link to this definition"></a>  
Whether the CHARGE file is from LCFO analysis. Default is False.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">types</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Charge.types" class="headerlink"
title="Link to this definition"></a>  
List of types of atoms in CHARGE.lobster.

Type<span class="colon">:</span>  
list\[str\]

<span class="sig-name descname"><span class="pre">mulliken</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Charge.mulliken"
class="headerlink" title="Link to this definition"></a>  
List of Mulliken charges of atoms in CHARGE.lobster.

Type<span class="colon">:</span>  
list\[float\]

<span class="sig-name descname"><span class="pre">loewdin</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Charge.loewdin" class="headerlink"
title="Link to this definition"></a>  
List of Loewdin charges of atoms in CHARGE.Loewdin.

Type<span class="colon">:</span>  
list\[float\]

<span class="sig-name descname"><span class="pre">num_atoms</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Charge.num_atoms"
class="headerlink" title="Link to this definition"></a>  
Number of atoms in CHARGE.lobster.

Type<span class="colon">:</span>  
int

Parameters<span class="colon">:</span>  
- **filename** (*PathLike*) – The CHARGE file, typically
  “CHARGE.lobster”.

- **is_lcfo** (*bool*) – Whether the CHARGE file is from LCFO analysis.
  Default is False.

- **num_atoms** (*int*) – Number of atoms in the structure.

- **atomlist** (*list\[str\]*) – Atoms in the structure.

- **types** (*list\[str\]*) – Unique species in the structure.

- **mulliken** (*list\[float\]*) – Mulliken charges.

- **loewdin** (*list\[float\]*) – Loewdin charges.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Loewdin</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Charge.Loewdin" class="headerlink"
title="Link to this definition"></a>  

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Mulliken</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Charge.Mulliken"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">get_structure_with_charges</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure_filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/outputs.py#L941-L958"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Charge.get_structure_with_charges"
class="headerlink" title="Link to this definition"></a>  
Get a Structure with Mulliken and Loewdin charges as site properties

Parameters<span class="colon">:</span>  
**structure_filename** (*PathLike*) – The POSCAR file.

Returns<span class="colon">:</span>  
Structure Object with Mulliken and Loewdin charges as site properties.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Cohpcar</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">are_coops</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">are_cobis</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">are_multi_center_cobis</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">is_lcfo</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/outputs.py#L63-L341"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Cohpcar" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Read COXXCAR.lobster/COXXCAR.LCFO.lobster files generated by LOBSTER.

<span class="sig-name descname"><span class="pre">cohp_data</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Cohpcar.cohp_data"
class="headerlink" title="Link to this definition"></a>  
The COHP data of the form: {bond: {“COHP”: {Spin.up: cohps,
Spin.down:cohps},

> <div>
>
> “ICOHP”: {Spin.up: icohps, Spin.down: icohps}, “length”: bond length,
> “sites”: sites corresponding to the bond}
>
> </div>

Also contains an entry for the average, which does not have a “length”
key.

Type<span class="colon">:</span>  
dict\[str, Dict\[str, Any\]\]

<span class="sig-name descname"><span class="pre">efermi</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Cohpcar.efermi" class="headerlink"
title="Link to this definition"></a>  
The Fermi level in eV.

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">energies</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Cohpcar.energies"
class="headerlink" title="Link to this definition"></a>  
Sequence of energies in eV. Note that LOBSTER shifts the energies so
that the Fermi level is at zero.

Type<span class="colon">:</span>  
Sequence\[float\]

<span class="sig-name descname"><span class="pre">is_spin_polarized</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Cohpcar.is_spin_polarized"
class="headerlink" title="Link to this definition"></a>  
True if the calculation is spin polarized.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">orb_res_cohp</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Cohpcar.orb_res_cohp"
class="headerlink" title="Link to this definition"></a>  
The orbital-resolved COHPs of the form: orb_res_cohp\[label\] =
{bond_data\[“orb_label”\]: {

> <div>
>
> “COHP”: {Spin.up: cohps, Spin.down:cohps}, “ICOHP”: {Spin.up: icohps,
> Spin.down: icohps}, “orbitals”: orbitals, “length”: bond lengths,
> “sites”: sites corresponding to the bond},
>
> </div>

}

Type<span class="colon">:</span>  
dict\[str, Dict\[str, Dict\[str, Any\]\]\]

Parameters<span class="colon">:</span>  
- **are_coops** (*bool*) – Whether the file includes COOPs (True) or
  COHPs (False). Default is False.

- **are_cobis** (*bool*) – Whether the file is COBIs (True) or COHPs
  (False). Default is False.

- **are_multi_center_cobis** (*bool*) – Whether the file include
  multi-center COBIs (True) or two-center COBIs (False). Default is
  False.

- **is_lcfo** (*bool*) – Whether the COXXCAR file is from LCFO analysis.

- **filename** (*PathLike*) – The COHPCAR file. If it is None, the
  default file name will be chosen, depending on the value of are_coops.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Doscar</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">doscar</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'DOSCAR.lobster'</span></span>*, *<span class="n"><span class="pre">is_lcfo</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">structure_file</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'POSCAR'</span></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.IStructure"
class="reference internal"
title="pymatgen.core.structure.IStructure"><span
class="pre">IStructure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/outputs.py#L718-L882"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Doscar" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Store LOBSTER’s projected DOS and local projected DOS. The beforehand
quantum-chemical calculation was performed with VASP.

<span class="sig-name descname"><span class="pre">completedos</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Doscar.completedos"
class="headerlink" title="Link to this definition"></a>  
LobsterCompleteDos Object.

Type<span class="colon">:</span>  
<a
href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.dos.LobsterCompleteDos"
class="reference internal"
title="pymatgen.electronic_structure.dos.LobsterCompleteDos">LobsterCompleteDos</a>

<span class="sig-name descname"><span class="pre">pdos</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Doscar.pdos" class="headerlink"
title="Link to this definition"></a>  
List of Dict including NumPy arrays with pdos. Access as
pdos\[atomindex\]\[‘orbitalstring’\]\[‘Spin.up/Spin.down’\].

Type<span class="colon">:</span>  
list

<span class="sig-name descname"><span class="pre">tdos</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Doscar.tdos" class="headerlink"
title="Link to this definition"></a>  
Dos Object of the total density of states.

Type<span class="colon">:</span>  
<a
href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.dos.Dos"
class="reference internal"
title="pymatgen.electronic_structure.dos.Dos">Dos</a>

<span class="sig-name descname"><span class="pre">energies</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Doscar.energies"
class="headerlink" title="Link to this definition"></a>  
Numpy array of the energies at which the DOS was calculated (in eV,
relative to Efermi).

Type<span class="colon">:</span>  
NDArray

<span class="sig-name descname"><span class="pre">tdensities</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Doscar.tdensities"
class="headerlink" title="Link to this definition"></a>  
tdensities\[Spin.up\]: NumPy array of the total density of states for
the Spin.up contribution at each of the energies.
tdensities\[Spin.down\]: NumPy array of the total density of states for
the Spin.down contribution at each of the energies. If
is_spin_polarized=False, tdensities\[Spin.up\]: NumPy array of the total
density of states.

Type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">itdensities</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Doscar.itdensities"
class="headerlink" title="Link to this definition"></a>  
itdensities\[Spin.up\]: NumPy array of the total density of states for
the Spin.up contribution at each of the energies.
itdensities\[Spin.down\]: NumPy array of the total density of states for
the Spin.down contribution at each of the energies. If
is_spin_polarized=False, itdensities\[Spin.up\]: NumPy array of the
total density of states.

Type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">is_spin_polarized</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Doscar.is_spin_polarized"
class="headerlink" title="Link to this definition"></a>  
Whether the system is spin polarized.

Type<span class="colon">:</span>  
bool

Parameters<span class="colon">:</span>  
- **doscar** (*PathLike*) – The DOSCAR file, typically “DOSCAR.lobster”.

- **is_lcfo** (*bool*) – Whether the DOSCAR file is from LCFO analysis.

- **structure_file** (*PathLike*) – For VASP, this is typically
  “POSCAR”.

- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  Instead of a structure file (preferred), the Structure can be given
  directly.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">completedos</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a
href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.dos.LobsterCompleteDos"
class="reference internal"
title="pymatgen.electronic_structure.dos.LobsterCompleteDos"><span
class="pre">LobsterCompleteDos</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id0" class="headerlink" title="Link to this definition"></a>  
LobsterCompleteDos.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">energies</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">NDArray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id1" class="headerlink" title="Link to this definition"></a>  
Energies.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">is_spin_polarized</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id2" class="headerlink" title="Link to this definition"></a>  
Whether run is spin polarized.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">itdensities</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><a
href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">NDArray</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id3" class="headerlink" title="Link to this definition"></a>  
Integrated total DOS as a np.array.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">pdos</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id4" class="headerlink" title="Link to this definition"></a>  
Projected DOS (PDOS).

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">tdensities</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><a
href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">NDArray</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id5" class="headerlink" title="Link to this definition"></a>  
Total DOS as a np.array.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">tdos</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a
href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.dos.Dos"
class="reference internal"
title="pymatgen.electronic_structure.dos.Dos"><span
class="pre">Dos</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id6" class="headerlink" title="Link to this definition"></a>  
Total DOS (TDOS).

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Fatband</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filenames</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">PathLike</span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'.'</span></span>*, *<span class="n"><span class="pre">kpoints_file</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'KPOINTS'</span></span>*, *<span class="n"><span class="pre">vasprun_file</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'vasprun.xml'</span></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.IStructure"
class="reference internal"
title="pymatgen.core.structure.IStructure"><span
class="pre">IStructure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">efermi</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/outputs.py#L1366-L1600"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Fatband" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Read FATBAND_x\_y.lobster files.

<span class="sig-name descname"><span class="pre">efermi</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Fatband.efermi" class="headerlink"
title="Link to this definition"></a>  
Fermi level read from vasprun.xml.

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">eigenvals</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Fatband.eigenvals"
class="headerlink" title="Link to this definition"></a>  
Eigenvalues as a dictionary of NumPy arrays of shape (nbands, nkpoints).
The first index of the array refers to the band and the second to the
index of the kpoint. The kpoints are ordered according to the order of
the kpoints_array attribute. If the band structure is not spin
polarized, we only store one data set under Spin.up.

Type<span class="colon">:</span>  
dict\[<a
href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin">Spin</a>, NDArray\]

<span class="sig-name descname"><span class="pre">is_spin_polarized</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Fatband.is_spin_polarized"
class="headerlink" title="Link to this definition"></a>  
Whether this was a spin-polarized calculation.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">kpoints_array</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Fatband.kpoints_array"
class="headerlink" title="Link to this definition"></a>  
List of kpoints as NumPy arrays, in frac_coords of the given lattice by
default.

Type<span class="colon">:</span>  
list\[NDArray\]

<span class="sig-name descname"><span class="pre">label_dict</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Fatband.label_dict"
class="headerlink" title="Link to this definition"></a>  
Dictionary that links a kpoint (in frac coords or Cartesian coordinates
depending on the coords attribute) to a label.

Type<span class="colon">:</span>  
dict\[str, Union\[str, NDArray\]\]

<span class="sig-name descname"><span class="pre">lattice</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Fatband.lattice"
class="headerlink" title="Link to this definition"></a>  
Lattice object of reciprocal lattice as read from vasprun.xml.

Type<span class="colon">:</span>  
<a href="pymatgen.core.html#pymatgen.core.lattice.Lattice"
class="reference internal"
title="pymatgen.core.lattice.Lattice">Lattice</a>

<span class="sig-name descname"><span class="pre">nbands</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Fatband.nbands" class="headerlink"
title="Link to this definition"></a>  
Number of bands used in the calculation.

Type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">p_eigenvals</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Fatband.p_eigenvals"
class="headerlink" title="Link to this definition"></a>  
Dictionary of orbital projections as {spin: array of dict}. The indices
of the array are \[band_index, kpoint_index\]. The dict is then built
the following way: {“string of element”: “string of orbital as read in
from FATBAND file”}. If the band structure is not spin polarized, we
only store one data set under Spin.up.

Type<span class="colon">:</span>  
dict\[<a
href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin">Spin</a>, NDArray\]

<span class="sig-name descname"><span class="pre">structure</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Fatband.structure"
class="headerlink" title="Link to this definition"></a>  
Structure object.

Type<span class="colon">:</span>  
<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure">Structure</a>

Parameters<span class="colon">:</span>  
- **filenames** (*PathLike* *\|* *list\[PathLike\]*) – File names or
  path to a folder from which all “FATBAND\_\*” files will be read.

- **kpoints_file** (*PathLike*) – KPOINTS file for bandstructure
  calculation, typically “KPOINTS”.

- **vasprun_file** (*PathLike*) – Corresponding vasprun.xml file.
  Instead, the Fermi level from the DFT run can be provided. Then, this
  should be set to None.

- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  Structure object.

- **efermi** (*float*) – Fermi level in eV.

<span class="sig-name descname"><span class="pre">get_bandstructure</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a
href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.bandstructure.LobsterBandStructureSymmLine"
class="reference internal"
title="pymatgen.electronic_structure.bandstructure.LobsterBandStructureSymmLine"><span
class="pre">LobsterBandStructureSymmLine</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/outputs.py#L1590-L1600"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Fatband.get_bandstructure"
class="headerlink" title="Link to this definition"></a>  
Get a LobsterBandStructureSymmLine object which can be plotted with a
normal BSPlotter.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Grosspop</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'GROSSPOP.lobster'</span></span>*, *<span class="n"><span class="pre">is_lcfo</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">list_dict_grosspop</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/outputs.py#L1750-L1869"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Grosspop" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Read GROSSPOP.lobster/ GROSSPOP.LCFO.lobster files.

<span class="sig-name descname"><span class="pre">list_dict_grosspop</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Grosspop.list_dict_grosspop"
class="headerlink" title="Link to this definition"></a>  
List of dictionaries including all information about the
grosspopulations. Each dictionary contains the following keys: -
‘element’: The element symbol of the atom. - ‘Mulliken GP’: A dictionary
of Mulliken gross populations, where the keys are the orbital labels and
the

> <div>
>
> values are the corresponding gross populations as strings.
>
> </div>

- ‘Loewdin GP’: A dictionary of Loewdin gross populations, where the keys are the orbital labels and the  
  values are the corresponding gross populations as strings.

The 0th entry of the list refers to the first atom in GROSSPOP.lobster
and so on.

Type<span class="colon">:</span>  
list\[dict\[str, str\| dict\[str, str\]\]\]

Parameters<span class="colon">:</span>  
- **filename** (*PathLike*) – The “GROSSPOP.lobster” file.

- **is_lcfo** (*bool*) – Whether the GROSSPOP file is in LCFO format.

- **list_dict_grosspop** (*list\[dict\]*) – All information about the
  gross populations.

<span class="sig-name descname"><span class="pre">get_structure_with_total_grosspop</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure_filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/outputs.py#L1845-L1869"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.outputs.Grosspop.get_structure_with_total_grosspop"
class="headerlink" title="Link to this definition"></a>  
Get a Structure with Mulliken and Loewdin total grosspopulations as site
properties.

Parameters<span class="colon">:</span>  
**structure_filename** (*PathLike*) – The POSCAR file.

Returns<span class="colon">:</span>  
Structure Object with Mulliken and Loewdin total grosspopulations as
site properties.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Icohplist</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">is_lcfo</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">are_coops</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">are_cobis</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">is_spin_polarized</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">orbitalwise</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">icohpcollection</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a
href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.cohp.IcohpCollection"
class="reference internal"
title="pymatgen.electronic_structure.cohp.IcohpCollection"><span
class="pre">IcohpCollection</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/outputs.py#L344-L609"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Icohplist" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Read ICOXXLIST/ICOXXLIST.LCFO.lobster files generated by LOBSTER.

<span class="sig-name descname"><span class="pre">are_coops</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Icohplist.are_coops"
class="headerlink" title="Link to this definition"></a>  
Whether the file includes COOPs (True) or COHPs (False).

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">is_lcfo</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Icohplist.is_lcfo"
class="headerlink" title="Link to this definition"></a>  
Whether the ICOXXLIST file is from LCFO analysis.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">is_spin_polarized</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Icohplist.is_spin_polarized"
class="headerlink" title="Link to this definition"></a>  
Whether the calculation is spin polarized.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">Icohplist</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Icohplist.Icohplist"
class="headerlink" title="Link to this definition"></a>  
The listfile data of the form: {  
bond: {  
“length”: Bond length, “number_of_bonds”: Number of bonds, “icohp”:
{Spin.up: ICOHP(Ef)\_up, Spin.down: …}, }

}

Type<span class="colon">:</span>  
dict\[str, Dict\[str, Union\[float, int, Dict\[<a
href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin">Spin</a>, float\]\]\]\]

<span class="sig-name descname"><span class="pre">IcohpCollection</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Icohplist.IcohpCollection"
class="headerlink" title="Link to this definition"></a>  
IcohpCollection Object.

Type<span class="colon">:</span>  
<a
href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.cohp.IcohpCollection"
class="reference internal"
title="pymatgen.electronic_structure.cohp.IcohpCollection">IcohpCollection</a>

Parameters<span class="colon">:</span>  
- **is_lcfo** (*bool*) – Whether the ICOHPLIST file is from LCFO
  analysis.

- **are_coops** (*bool*) – Whether the file includes COOPs (True) or
  COHPs (False). Default is False.

- **are_cobis** (*bool*) – Whether the file is COBIs (True) or COHPs
  (False). Default is False.

- **filename** (*PathLike*) – The ICOHPLIST file. If it is None, the
  default file name will be chosen, depending on the value of are_coops

- **is_spin_polarized** (*bool*) – Whether the calculation is spin
  polarized.

- **orbitalwise** (*bool*) – Whether the calculation is orbitalwise.

- **icohpcollection** (<a
  href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.cohp.IcohpCollection"
  class="reference internal"
  title="pymatgen.electronic_structure.cohp.IcohpCollection"><em>IcohpCollection</em></a>)
  – IcohpCollection Object.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">icohpcollection</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a
href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.cohp.IcohpCollection"
class="reference internal"
title="pymatgen.electronic_structure.cohp.IcohpCollection"><span
class="pre">IcohpCollection</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Icohplist.icohpcollection"
class="headerlink" title="Link to this definition"></a>  
The IcohpCollection object.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">icohplist</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">Any</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Icohplist.icohplist"
class="headerlink" title="Link to this definition"></a>  
The ICOHP list compatible with older version of this class.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">LobsterMatrices</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">e_fermi</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'hamiltonMatrices.lobster'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/outputs.py#L2246-L2416"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.LobsterMatrices"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Read Matrices file generated by LOBSTER (e.g. hamiltonMatrices.lobster).

<span class="sig-name descname"><span class="pre">If</span> <span class="pre">filename</span> <span class="pre">==</span> <span class="pre">"hamiltonMatrices.lobster"</span></span>  
onsite_energies (list\[NDArray\]): Real parts of onsite energies from the  
matrices each k-point.

average_onsite_energies (dict): Average onsite elements energies for  
all k-points with keys as basis used in the LOBSTER computation (uses
only real part of matrix).

hamilton_matrices (dict\[Spin, NDArray\]): The complex Hamilton matrix at each  
k-point with k-point and spin as keys.

<span class="sig-name descname"><span class="pre">If</span> <span class="pre">filename</span> <span class="pre">==</span> <span class="pre">"coefficientMatrices.lobster"</span></span>  
onsite_coefficients (list\[NDArray\]): Real parts of onsite coefficients  
from the matrices each k-point.

average_onsite_coefficient (dict): Average onsite elements coefficients  
for all k-points with keys as basis used in the LOBSTER computation
(uses only real part of matrix).

coefficient_matrices (dict\[Spin, NDArray\]): The coefficients matrix  
at each k-point with k-point and spin as keys.

<span class="sig-name descname"><span class="pre">If</span> <span class="pre">filename</span> <span class="pre">==</span> <span class="pre">"transferMatrices.lobster"</span></span>  
onsite_transfer (list\[NDArray\]): Real parts of onsite transfer  
coefficients from the matrices at each k-point.

average_onsite_transfer (dict): Average onsite elements transfer  
coefficients for all k-points with keys as basis used in the LOBSTER
computation (uses only real part of matrix).

transfer_matrices (dict\[Spin, NDArray\]): The coefficients matrix at  
each k-point with k-point and spin as keys.

<span class="sig-name descname"><span class="pre">If</span> <span class="pre">filename</span> <span class="pre">==</span> <span class="pre">"overlapMatrices.lobster"</span></span>  
onsite_overlaps (list\[NDArray\]): Real parts of onsite overlaps  
from the matrices each k-point.

average_onsite_overlaps (dict): Average onsite elements overlaps  
for all k-points with keys as basis used in the LOBSTER computation
(uses only real part of matrix).

overlap_matrices (dict\[NDArray\]): The overlap matrix at  
each k-point with k-point as keys.

Parameters<span class="colon">:</span>  
- **e_fermi** (*float*) – Fermi level in eV for the structure only.
  Relevant if input file contains Hamilton matrices data.

- **filename** (*PathLike*) – The hamiltonMatrices file, typically
  “hamiltonMatrices.lobster”.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Lobsterout</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/outputs.py#L971-L1363"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Lobsterout" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Read the lobsterout and evaluate the spilling, save the basis, save
warnings, save info.

<span class="sig-name descname"><span class="pre">basis_functions</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Lobsterout.basis_functions"
class="headerlink" title="Link to this definition"></a>  
Basis functions that were used in lobster run as strings.

Type<span class="colon">:</span>  
list\[str\]

<span class="sig-name descname"><span class="pre">basis_type</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Lobsterout.basis_type"
class="headerlink" title="Link to this definition"></a>  
Basis types that were used in lobster run as strings.

Type<span class="colon">:</span>  
list\[str\]

<span class="sig-name descname"><span class="pre">charge_spilling</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Lobsterout.charge_spilling"
class="headerlink" title="Link to this definition"></a>  
Charge spilling (first entry: result for spin 1, second entry: result
for spin 2 or not present).

Type<span class="colon">:</span>  
list\[float\]

<span class="sig-name descname"><span class="pre">dft_program</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Lobsterout.dft_program"
class="headerlink" title="Link to this definition"></a>  
The DFT program used for the calculation of the wave function.

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">elements</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Lobsterout.elements"
class="headerlink" title="Link to this definition"></a>  
Elements that were present in LOBSTER calculation.

Type<span class="colon">:</span>  
list\[str\]

<span class="sig-name descname"><span class="pre">has_charge</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Lobsterout.has_charge"
class="headerlink" title="Link to this definition"></a>  
Whether CHARGE.lobster is present.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">has_cohpcar</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Lobsterout.has_cohpcar"
class="headerlink" title="Link to this definition"></a>  
Whether COHPCAR.lobster and ICOHPLIST.lobster are present.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">has_madelung</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Lobsterout.has_madelung"
class="headerlink" title="Link to this definition"></a>  
Whether SitePotentials.lobster and MadelungEnergies.lobster are present.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">has_coopcar</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Lobsterout.has_coopcar"
class="headerlink" title="Link to this definition"></a>  
Whether COOPCAR.lobster and ICOOPLIST.lobster are present.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">has_cobicar</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Lobsterout.has_cobicar"
class="headerlink" title="Link to this definition"></a>  
Whether COBICAR.lobster and ICOBILIST.lobster are present.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">has_doscar</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Lobsterout.has_doscar"
class="headerlink" title="Link to this definition"></a>  
Whether DOSCAR.lobster is present.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">has_doscar_lso</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Lobsterout.has_doscar_lso"
class="headerlink" title="Link to this definition"></a>  
Whether DOSCAR.LSO.lobster is present.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">has_projection</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Lobsterout.has_projection"
class="headerlink" title="Link to this definition"></a>  
Whether projectionData.lobster is present.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">has_bandoverlaps</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Lobsterout.has_bandoverlaps"
class="headerlink" title="Link to this definition"></a>  
Whether bandOverlaps.lobster is present.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">has_density_of_energies</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.outputs.Lobsterout.has_density_of_energies"
class="headerlink" title="Link to this definition"></a>  
Whether DensityOfEnergy.lobster is present.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">has_fatbands</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Lobsterout.has_fatbands"
class="headerlink" title="Link to this definition"></a>  
Whether fatband calculation was performed.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">has_grosspopulation</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Lobsterout.has_grosspopulation"
class="headerlink" title="Link to this definition"></a>  
Whether GROSSPOP.lobster is present.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">has_polarization</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Lobsterout.has_polarization"
class="headerlink" title="Link to this definition"></a>  
Whether POLARIZATION.lobster is present.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">info_lines</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Lobsterout.info_lines"
class="headerlink" title="Link to this definition"></a>  
Additional information on the run.

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">info_orthonormalization</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.outputs.Lobsterout.info_orthonormalization"
class="headerlink" title="Link to this definition"></a>  
Information on orthonormalization.

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">is_restart_from_projection</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.outputs.Lobsterout.is_restart_from_projection"
class="headerlink" title="Link to this definition"></a>  
Whether that calculation was restarted from an existing projection file.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">lobster_version</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Lobsterout.lobster_version"
class="headerlink" title="Link to this definition"></a>  
The LOBSTER version.

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">number_of_spins</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Lobsterout.number_of_spins"
class="headerlink" title="Link to this definition"></a>  
The number of spins.

Type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">number_of_threads</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Lobsterout.number_of_threads"
class="headerlink" title="Link to this definition"></a>  
How many threads were used.

Type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">timing</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Lobsterout.timing"
class="headerlink" title="Link to this definition"></a>  
Dict with infos on timing.

Type<span class="colon">:</span>  
dict\[str, float\]

<span class="sig-name descname"><span class="pre">total_spilling</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Lobsterout.total_spilling"
class="headerlink" title="Link to this definition"></a>  
The total spilling for spin channel 1 (and spin channel 2).

Type<span class="colon">:</span>  
list\[float\]

<span class="sig-name descname"><span class="pre">warning_lines</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Lobsterout.warning_lines"
class="headerlink" title="Link to this definition"></a>  
String with all warnings.

Type<span class="colon">:</span>  
str

Parameters<span class="colon">:</span>  
- **filename** (*PathLike*) – The lobsterout file.

- **\*\*kwargs** – dict to initialize Lobsterout instance

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/outputs.py#L1190-L1196"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Lobsterout.as_dict"
class="headerlink" title="Link to this definition"></a>  
MSONable dict.

<span class="sig-name descname"><span class="pre">get_doc</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/outputs.py#L1153-L1188"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Lobsterout.get_doc"
class="headerlink" title="Link to this definition"></a>  
Get a dict with all information stored in lobsterout.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">MadelungEnergies</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'MadelungEnergies.lobster'</span></span>*, *<span class="n"><span class="pre">ewald_splitting</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">madelungenergies_mulliken</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">madelungenergies_loewdin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/outputs.py#L2049-L2096"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.MadelungEnergies"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Read MadelungEnergies.lobster files generated by LOBSTER.

<span class="sig-name descname"><span class="pre">madelungenergies_mulliken</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.outputs.MadelungEnergies.madelungenergies_mulliken"
class="headerlink" title="Link to this definition"></a>  
The Madelung energy based on the Mulliken approach.

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">madelungenergies_loewdin</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.outputs.MadelungEnergies.madelungenergies_loewdin"
class="headerlink" title="Link to this definition"></a>  
The Madelung energy based on the Loewdin approach.

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">ewald_splitting</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.MadelungEnergies.ewald_splitting"
class="headerlink" title="Link to this definition"></a>  
The Ewald splitting parameter to compute SitePotentials.

Type<span class="colon">:</span>  
float

Parameters<span class="colon">:</span>  
- **filename** (*PathLike*) – The “MadelungEnergies.lobster” file.

- **ewald_splitting** (*float*) – The Ewald splitting parameter to
  compute SitePotentials.

- **madelungenergies_mulliken** (*float*) – The Madelung energy based on
  the Mulliken approach.

- **madelungenergies_loewdin** (*float*) – The Madelung energy based on
  the Loewdin approach.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">madelungenergies_Loewdin</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.outputs.MadelungEnergies.madelungenergies_Loewdin"
class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">madelungenergies_Mulliken</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.outputs.MadelungEnergies.madelungenergies_Mulliken"
class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">NciCobiList</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'NcICOBILIST.lobster'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/outputs.py#L612-L715"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.NciCobiList" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Read NcICOBILIST (multi-center ICOBI) files generated by LOBSTER.

<span class="sig-name descname"><span class="pre">is_spin_polarized</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.NciCobiList.is_spin_polarized"
class="headerlink" title="Link to this definition"></a>  
Whether the calculation is spin polarized.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">NciCobiList</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.NciCobiList.NciCobiList"
class="headerlink" title="Link to this definition"></a>  
The listfile data of the form: {

> <div>
>
> bond: {  
> “number_of_atoms”: Number of atoms involved in the multi-center
> interaction, “ncicobi”: {Spin.up: Nc-ICOBI(Ef)\_up, Spin.down: …},
> “interaction_type”: Type of the multi-center interaction, }
>
> </div>

}

Type<span class="colon">:</span>  
dict

LOBSTER \< 4.1.0: no COBI/ICOBI/NcICOBI

Parameters<span class="colon">:</span>  
**filename** – Name of the NcICOBILIST file.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ncicobi_list</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">Any</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.NciCobiList.ncicobi_list"
class="headerlink" title="Link to this definition"></a>  
Returns: dict: ncicobilist.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Polarization</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'POLARIZATION.lobster'</span></span>*, *<span class="n"><span class="pre">rel_mulliken_pol_vector</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">rel_loewdin_pol_vector</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/outputs.py#L2419-L2455"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Polarization" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Read POLARIZATION.lobster file generated by LOBSTER.

<span class="sig-name descname"><span class="pre">rel_mulliken_pol_vector</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.outputs.Polarization.rel_mulliken_pol_vector"
class="headerlink" title="Link to this definition"></a>  
Relative Mulliken polarization vector.

Type<span class="colon">:</span>  
dict\[str, float\]

<span class="sig-name descname"><span class="pre">rel_loewdin_pol_vector</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.outputs.Polarization.rel_loewdin_pol_vector"
class="headerlink" title="Link to this definition"></a>  
Relative Mulliken polarization vector.

Type<span class="colon">:</span>  
dict\[str, float\]

Parameters<span class="colon">:</span>  
- **filename** (*PathLike*) – The “POLARIZATION.lobster” file.

- **rel_mulliken_pol_vector** (*dict\[str,* *Union\[float,* *str\]\]*) –
  Relative Mulliken polarization vector.

- **rel_loewdin_pol_vector** (*dict\[str,* *Union\[float,* *str\]\]*) –
  Relative Loewdin polarization vector.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">SitePotential</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'SitePotentials.lobster'</span></span>*, *<span class="n"><span class="pre">ewald_splitting</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">num_atoms</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">atomlist</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">types</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sitepotentials_loewdin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sitepotentials_mulliken</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">madelungenergies_mulliken</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">madelungenergies_loewdin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/outputs.py#L2099-L2203"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.SitePotential" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Read SitePotentials.lobster files generated by LOBSTER.

<span class="sig-name descname"><span class="pre">atomlist</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.SitePotential.atomlist"
class="headerlink" title="Link to this definition"></a>  
Atoms in SitePotentials.lobster.

Type<span class="colon">:</span>  
list\[str\]

<span class="sig-name descname"><span class="pre">types</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.SitePotential.types"
class="headerlink" title="Link to this definition"></a>  
Types of atoms in SitePotentials.lobster.

Type<span class="colon">:</span>  
list\[str\]

<span class="sig-name descname"><span class="pre">num_atoms</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.SitePotential.num_atoms"
class="headerlink" title="Link to this definition"></a>  
Number of atoms in SitePotentials.lobster.

Type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">sitepotentials_mulliken</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.outputs.SitePotential.sitepotentials_mulliken"
class="headerlink" title="Link to this definition"></a>  
Mulliken potentials of sites in SitePotentials.lobster.

Type<span class="colon">:</span>  
list\[float\]

<span class="sig-name descname"><span class="pre">sitepotentials_loewdin</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.outputs.SitePotential.sitepotentials_loewdin"
class="headerlink" title="Link to this definition"></a>  
Loewdin potentials of sites in SitePotentials.lobster.

Type<span class="colon">:</span>  
list\[float\]

<span class="sig-name descname"><span class="pre">madelungenergies_mulliken</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.outputs.SitePotential.madelungenergies_mulliken"
class="headerlink" title="Link to this definition"></a>  
The Madelung energy based on the Mulliken approach.

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">madelungenergies_loewdin</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.outputs.SitePotential.madelungenergies_loewdin"
class="headerlink" title="Link to this definition"></a>  
The Madelung energy based on the Loewdin approach.

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">ewald_splitting</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.SitePotential.ewald_splitting"
class="headerlink" title="Link to this definition"></a>  
The Ewald Splitting parameter to compute SitePotentials.

Type<span class="colon">:</span>  
float

Parameters<span class="colon">:</span>  
- **filename** (*PathLike*) – The SitePotentials file, typically
  “SitePotentials.lobster”.

- **ewald_splitting** (*float*) – Ewald splitting parameter used for
  computing Madelung energies.

- **num_atoms** (*int*) – Number of atoms in the structure.

- **atomlist** (*list\[str\]*) – Atoms in the structure.

- **types** (*list\[str\]*) – Unique atom types in the structure.

- **sitepotentials_loewdin** (*list\[float\]*) – Loewdin site
  potentials.

- **sitepotentials_mulliken** (*list\[float\]*) – Mulliken site
  potentials.

- **madelungenergies_mulliken** (*float*) – Madelung energy based on the
  Mulliken approach.

- **madelungenergies_loewdin** (*float*) – Madelung energy based on the
  Loewdin approach.

<span class="sig-name descname"><span class="pre">get_structure_with_site_potentials</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure_filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/outputs.py#L2167-L2183"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.outputs.SitePotential.get_structure_with_site_potentials"
class="headerlink" title="Link to this definition"></a>  
Get a Structure with Mulliken and Loewdin charges as site properties.

Parameters<span class="colon">:</span>  
**structure_filename** (*PathLike*) – The POSCAR file.

Returns<span class="colon">:</span>  
Structure Object with Mulliken and Loewdin charges as site properties.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">madelungenergies_Loewdin</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.outputs.SitePotential.madelungenergies_Loewdin"
class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">madelungenergies_Mulliken</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.outputs.SitePotential.madelungenergies_Mulliken"
class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">sitepotentials_Loewdin</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.outputs.SitePotential.sitepotentials_Loewdin"
class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">sitepotentials_Mulliken</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.outputs.SitePotential.sitepotentials_Mulliken"
class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Wavefunction</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/outputs.py#L1872-L2045"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Wavefunction" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Read wave function files from LOBSTER and create an VolumetricData
object.

<span class="sig-name descname"><span class="pre">grid</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Wavefunction.grid"
class="headerlink" title="Link to this definition"></a>  
Grid for the wave function \[Nx+1, Ny+1, Nz+1\].

Type<span class="colon">:</span>  
tuple\[int, int, int\]

<span class="sig-name descname"><span class="pre">points</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Wavefunction.points"
class="headerlink" title="Link to this definition"></a>  
Points.

Type<span class="colon">:</span>  
list\[Tuple\[float, float, float\]\]

<span class="sig-name descname"><span class="pre">real</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Wavefunction.real"
class="headerlink" title="Link to this definition"></a>  
Real parts of wave function.

Type<span class="colon">:</span>  
list\[float\]

<span class="sig-name descname"><span class="pre">imaginary</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Wavefunction.imaginary"
class="headerlink" title="Link to this definition"></a>  
Imaginary parts of wave function.

Type<span class="colon">:</span>  
list\[float\]

<span class="sig-name descname"><span class="pre">distance</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/lobster/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Wavefunction.distance"
class="headerlink" title="Link to this definition"></a>  
Distances to the first point in wave function file.

Type<span class="colon">:</span>  
list\[float\]

Parameters<span class="colon">:</span>  
- **filename** (*PathLike*) – The wavecar file from LOBSTER.

- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  The Structure object.

<span class="sig-name descname"><span class="pre">get_volumetricdata_density</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="pymatgen.io.vasp.html#pymatgen.io.vasp.outputs.VolumetricData"
class="reference internal"
title="pymatgen.io.vasp.outputs.VolumetricData"><span
class="pre">VolumetricData</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/outputs.py#L2005-L2013"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.outputs.Wavefunction.get_volumetricdata_density"
class="headerlink" title="Link to this definition"></a>  
Get a VolumetricData object including the density part of the wave
function.

Returns<span class="colon">:</span>  
VolumetricData

<span class="sig-name descname"><span class="pre">get_volumetricdata_imaginary</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="pymatgen.io.vasp.html#pymatgen.io.vasp.outputs.VolumetricData"
class="reference internal"
title="pymatgen.io.vasp.outputs.VolumetricData"><span
class="pre">VolumetricData</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/outputs.py#L1995-L2003"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.outputs.Wavefunction.get_volumetricdata_imaginary"
class="headerlink" title="Link to this definition"></a>  
Get a VolumetricData object including the imaginary part of the wave
function.

Returns<span class="colon">:</span>  
VolumetricData

<span class="sig-name descname"><span class="pre">get_volumetricdata_real</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="pymatgen.io.vasp.html#pymatgen.io.vasp.outputs.VolumetricData"
class="reference internal"
title="pymatgen.io.vasp.outputs.VolumetricData"><span
class="pre">VolumetricData</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/outputs.py#L1985-L1993"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.lobster.outputs.Wavefunction.get_volumetricdata_real"
class="headerlink" title="Link to this definition"></a>  
Get a VolumetricData object including the real part of the wave
function.

Returns<span class="colon">:</span>  
VolumetricData

<span class="sig-name descname"><span class="pre">set_volumetric_data</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">grid</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/outputs.py#L1931-L1983"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Wavefunction.set_volumetric_data"
class="headerlink" title="Link to this definition"></a>  
Create the VolumetricData instances.

Parameters<span class="colon">:</span>  
- **grid** (*tuple\[int,* *int,* *int\]*) – Grid on which wavefunction
  was calculated, e.g. (1, 2, 2).

- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  The Structure object.

<span class="sig-name descname"><span class="pre">write_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'WAVECAR.vasp'</span></span>*, *<span class="n"><span class="pre">part</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'real'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'imaginary'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'density'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'real'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/outputs.py#L2015-L2045"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.Wavefunction.write_file"
class="headerlink" title="Link to this definition"></a>  
Save the wave function in a file that can be read by VESTA.

This will only work if the wavefunction from lobster is constructed with:  
“printLCAORealSpaceWavefunction kpoint 1 coordinates 0.0 0.0 0.0
coordinates 1.0 1.0 1.0 box bandlist 1 2 3 4 5 6 ” or similar (the whole
unit cell has to be covered!).

Parameters<span class="colon">:</span>  
- **filename** (*PathLike*) – The output file, e.g. “WAVECAR.vasp”.

- **part** (*"real"* *\|* *"imaginary"* *\|* *"density"\]*) – Part of
  the wavefunction to save.

<!-- -->

<span class="sig-name descname"><span class="pre">get_orb_from_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">orbs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><a
href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.core.Orbital"
class="reference internal"
title="pymatgen.electronic_structure.core.Orbital"><span
class="pre">Orbital</span></a><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/lobster/outputs.py#L2206-L2243"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.lobster.outputs.get_orb_from_str"
class="headerlink" title="Link to this definition"></a>  
Get Orbitals from string representations.

Parameters<span class="colon">:</span>  
**orbs** (*list\[str\]*) – Orbitals, e.g. \[“2p_x”, “3s”\].

Returns<span class="colon">:</span>  
Orbital label, orbitals.

Return type<span class="colon">:</span>  
tuple\[str, list\[tuple\[int, <a
href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.core.Orbital"
class="reference internal"
title="pymatgen.electronic_structure.core.Orbital">Orbital</a>\]\]\]

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
