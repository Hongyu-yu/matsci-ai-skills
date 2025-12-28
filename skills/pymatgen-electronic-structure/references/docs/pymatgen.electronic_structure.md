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

- <a href="#" class="reference internal">pymatgen.electronic_structure
  package</a>
  - <a href="#submodules" class="reference internal">Submodules</a>
  - <a href="#module-pymatgen.electronic_structure.bandstructure"
    class="reference internal">pymatgen.electronic_structure.bandstructure
    module</a>
    - <a href="#pymatgen.electronic_structure.bandstructure.BandStructure"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">BandStructure</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.BandStructure.kpoints"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructure.kpoints</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.BandStructure.lattice_rec"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructure.lattice_rec</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.BandStructure.efermi"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructure.efermi</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.BandStructure.is_spin_polarized"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructure.is_spin_polarized</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.BandStructure.bands"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructure.bands</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.BandStructure.nb_bands"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructure.nb_bands</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.BandStructure.structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructure.structure</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.BandStructure.projections"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructure.projections</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.BandStructure.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructure.as_dict()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.BandStructure.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructure.from_dict()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.BandStructure.from_old_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructure.from_old_dict()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.BandStructure.get_band_gap"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructure.get_band_gap()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.BandStructure.get_cbm"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructure.get_cbm()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.BandStructure.get_direct_band_gap"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructure.get_direct_band_gap()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.BandStructure.get_direct_band_gap_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructure.get_direct_band_gap_dict()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.BandStructure.get_kpoint_degeneracy"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructure.get_kpoint_degeneracy()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.BandStructure.get_projection_on_elements"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructure.get_projection_on_elements()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.BandStructure.get_projections_on_elements_and_orbitals"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructure.get_projections_on_elements_and_orbitals()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.BandStructure.get_sym_eq_kpoints"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructure.get_sym_eq_kpoints()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.BandStructure.get_vbm"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructure.get_vbm()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.BandStructure.is_metal"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructure.is_metal()</code></span></a>
    - <a
      href="#pymatgen.electronic_structure.bandstructure.BandStructureSymmLine"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">BandStructureSymmLine</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.BandStructureSymmLine.apply_scissor"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructureSymmLine.apply_scissor()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.BandStructureSymmLine.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructureSymmLine.as_dict()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.BandStructureSymmLine.get_branch"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructureSymmLine.get_branch()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.BandStructureSymmLine.get_equivalent_kpoints"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructureSymmLine.get_equivalent_kpoints()</code></span></a>
    - <a href="#pymatgen.electronic_structure.bandstructure.Kpoint"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Kpoint</code></span></a>
      - <a href="#pymatgen.electronic_structure.bandstructure.Kpoint.a"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Kpoint.a</code></span></a>
      - <a href="#pymatgen.electronic_structure.bandstructure.Kpoint.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Kpoint.as_dict()</code></span></a>
      - <a href="#pymatgen.electronic_structure.bandstructure.Kpoint.b"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Kpoint.b</code></span></a>
      - <a href="#pymatgen.electronic_structure.bandstructure.Kpoint.c"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Kpoint.c</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.Kpoint.cart_coords"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Kpoint.cart_coords</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.Kpoint.frac_coords"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Kpoint.frac_coords</code></span></a>
      - <a href="#pymatgen.electronic_structure.bandstructure.Kpoint.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Kpoint.from_dict()</code></span></a>
      - <a href="#pymatgen.electronic_structure.bandstructure.Kpoint.label"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Kpoint.label</code></span></a>
      - <a href="#pymatgen.electronic_structure.bandstructure.Kpoint.lattice"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Kpoint.lattice</code></span></a>
    - <a
      href="#pymatgen.electronic_structure.bandstructure.LobsterBandStructureSymmLine"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">LobsterBandStructureSymmLine</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.LobsterBandStructureSymmLine.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LobsterBandStructureSymmLine.as_dict()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.LobsterBandStructureSymmLine.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LobsterBandStructureSymmLine.from_dict()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.LobsterBandStructureSymmLine.from_old_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LobsterBandStructureSymmLine.from_old_dict()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.LobsterBandStructureSymmLine.get_projection_on_elements"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LobsterBandStructureSymmLine.get_projection_on_elements()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.bandstructure.LobsterBandStructureSymmLine.get_projections_on_elements_and_orbitals"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LobsterBandStructureSymmLine.get_projections_on_elements_and_orbitals()</code></span></a>
    - <a
      href="#pymatgen.electronic_structure.bandstructure.get_reconstructed_band_structure"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">get_reconstructed_band_structure()</code></span></a>
  - <a href="#module-pymatgen.electronic_structure.boltztrap"
    class="reference internal">pymatgen.electronic_structure.boltztrap
    module</a>
    - <a href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">BoltztrapAnalyzer</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapAnalyzer.as_dict()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.check_acc_bzt_bands"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapAnalyzer.check_acc_bzt_bands()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapAnalyzer.from_dict()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.from_files"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapAnalyzer.from_files()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.get_average_eff_mass"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapAnalyzer.get_average_eff_mass()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.get_carrier_concentration"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapAnalyzer.get_carrier_concentration()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.get_complete_dos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapAnalyzer.get_complete_dos()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.get_complexity_factor"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapAnalyzer.get_complexity_factor()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.get_conductivity"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapAnalyzer.get_conductivity()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.get_extreme"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapAnalyzer.get_extreme()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.get_hall_carrier_concentration"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapAnalyzer.get_hall_carrier_concentration()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.get_mu_bounds"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapAnalyzer.get_mu_bounds()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.get_power_factor"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapAnalyzer.get_power_factor()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.get_seebeck"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapAnalyzer.get_seebeck()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.get_seebeck_eff_mass"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapAnalyzer.get_seebeck_eff_mass()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.get_symm_bands"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapAnalyzer.get_symm_bands()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.get_thermal_conductivity"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapAnalyzer.get_thermal_conductivity()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.get_zt"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapAnalyzer.get_zt()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.parse_cond_and_hall"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapAnalyzer.parse_cond_and_hall()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.parse_intrans"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapAnalyzer.parse_intrans()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.parse_outputtrans"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapAnalyzer.parse_outputtrans()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.parse_struct"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapAnalyzer.parse_struct()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.parse_transdos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapAnalyzer.parse_transdos()</code></span></a>
    - <a href="#pymatgen.electronic_structure.boltztrap.BoltztrapError"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">BoltztrapError</code></span></a>
    - <a href="#pymatgen.electronic_structure.boltztrap.BoltztrapRunner"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">BoltztrapRunner</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapRunner.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapRunner.as_dict()</code></span></a>
      - <a href="#pymatgen.electronic_structure.boltztrap.BoltztrapRunner.bs"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapRunner.bs</code></span></a>
      - <a href="#pymatgen.electronic_structure.boltztrap.BoltztrapRunner.nelec"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapRunner.nelec</code></span></a>
      - <a href="#pymatgen.electronic_structure.boltztrap.BoltztrapRunner.run"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapRunner.run()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapRunner.write_def"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapRunner.write_def()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapRunner.write_energy"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapRunner.write_energy()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapRunner.write_input"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapRunner.write_input()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapRunner.write_intrans"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapRunner.write_intrans()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapRunner.write_proj"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapRunner.write_proj()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.boltztrap.BoltztrapRunner.write_struct"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapRunner.write_struct()</code></span></a>
    - <a href="#pymatgen.electronic_structure.boltztrap.compare_sym_bands"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">compare_sym_bands()</code></span></a>
    - <a href="#pymatgen.electronic_structure.boltztrap.eta_from_seebeck"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">eta_from_seebeck()</code></span></a>
    - <a href="#pymatgen.electronic_structure.boltztrap.read_cube_file"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">read_cube_file()</code></span></a>
    - <a
      href="#pymatgen.electronic_structure.boltztrap.seebeck_eff_mass_from_carr"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">seebeck_eff_mass_from_carr()</code></span></a>
    - <a
      href="#pymatgen.electronic_structure.boltztrap.seebeck_eff_mass_from_seebeck_carr"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">seebeck_eff_mass_from_seebeck_carr()</code></span></a>
    - <a href="#pymatgen.electronic_structure.boltztrap.seebeck_spb"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">seebeck_spb()</code></span></a>
  - <a href="#pymatgen-electronic-structure-boltztrap2-module"
    class="reference internal">pymatgen.electronic_structure.boltztrap2
    module</a>
  - <a href="#module-pymatgen.electronic_structure.cohp"
    class="reference internal">pymatgen.electronic_structure.cohp module</a>
    - <a href="#pymatgen.electronic_structure.cohp.Cohp"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Cohp</code></span></a>
      - <a href="#pymatgen.electronic_structure.cohp.Cohp.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cohp.as_dict()</code></span></a>
      - <a href="#pymatgen.electronic_structure.cohp.Cohp.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cohp.from_dict()</code></span></a>
      - <a href="#pymatgen.electronic_structure.cohp.Cohp.get_cohp"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cohp.get_cohp()</code></span></a>
      - <a href="#pymatgen.electronic_structure.cohp.Cohp.get_icohp"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cohp.get_icohp()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.cohp.Cohp.get_interpolated_value"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cohp.get_interpolated_value()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.cohp.Cohp.has_antibnd_states_below_efermi"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cohp.has_antibnd_states_below_efermi()</code></span></a>
    - <a href="#pymatgen.electronic_structure.cohp.CompleteCohp"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">CompleteCohp</code></span></a>
      - <a href="#pymatgen.electronic_structure.cohp.CompleteCohp.are_coops"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteCohp.are_coops</code></span></a>
      - <a href="#pymatgen.electronic_structure.cohp.CompleteCohp.are_cobis"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteCohp.are_cobis</code></span></a>
      - <a href="#pymatgen.electronic_structure.cohp.CompleteCohp.efermi"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteCohp.efermi</code></span></a>
      - <a href="#pymatgen.electronic_structure.cohp.CompleteCohp.energies"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteCohp.energies</code></span></a>
      - <a href="#pymatgen.electronic_structure.cohp.CompleteCohp.structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteCohp.structure</code></span></a>
      - <a href="#pymatgen.electronic_structure.cohp.CompleteCohp.cohp"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteCohp.cohp</code></span></a>
      - <a href="#pymatgen.electronic_structure.cohp.CompleteCohp.icohp"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteCohp.icohp</code></span></a>
      - <a href="#pymatgen.electronic_structure.cohp.CompleteCohp.all_cohps"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteCohp.all_cohps</code></span></a>
      - <a href="#pymatgen.electronic_structure.cohp.CompleteCohp.orb_res_cohp"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteCohp.orb_res_cohp</code></span></a>
      - <a href="#pymatgen.electronic_structure.cohp.CompleteCohp.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteCohp.as_dict()</code></span></a>
      - <a href="#pymatgen.electronic_structure.cohp.CompleteCohp.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteCohp.from_dict()</code></span></a>
      - <a href="#pymatgen.electronic_structure.cohp.CompleteCohp.from_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteCohp.from_file()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.cohp.CompleteCohp.get_cohp_by_label"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteCohp.get_cohp_by_label()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.cohp.CompleteCohp.get_orbital_resolved_cohp"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteCohp.get_orbital_resolved_cohp()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.cohp.CompleteCohp.get_summed_cohp_by_label_and_orbital_list"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteCohp.get_summed_cohp_by_label_and_orbital_list()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.cohp.CompleteCohp.get_summed_cohp_by_label_list"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteCohp.get_summed_cohp_by_label_list()</code></span></a>
    - <a href="#pymatgen.electronic_structure.cohp.IcohpCollection"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">IcohpCollection</code></span></a>
      - <a href="#pymatgen.electronic_structure.cohp.IcohpCollection.are_coops"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpCollection.are_coops</code></span></a>
      - <a href="#pymatgen.electronic_structure.cohp.IcohpCollection.are_cobis"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpCollection.are_cobis</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.cohp.IcohpCollection.is_spin_polarized"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpCollection.is_spin_polarized</code></span></a>
      - <a href="#id0" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpCollection.are_cobis</code></span></a>
      - <a href="#id1" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpCollection.are_coops</code></span></a>
      - <a href="#pymatgen.electronic_structure.cohp.IcohpCollection.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpCollection.as_dict()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.cohp.IcohpCollection.extremum_icohpvalue"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpCollection.extremum_icohpvalue()</code></span></a>
      - <a href="#pymatgen.electronic_structure.cohp.IcohpCollection.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpCollection.from_dict()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.cohp.IcohpCollection.get_icohp_by_label"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpCollection.get_icohp_by_label()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.cohp.IcohpCollection.get_icohp_dict_by_bondlengths"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpCollection.get_icohp_dict_by_bondlengths()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.cohp.IcohpCollection.get_icohp_dict_of_site"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpCollection.get_icohp_dict_of_site()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.cohp.IcohpCollection.get_summed_icohp_by_label_list"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpCollection.get_summed_icohp_by_label_list()</code></span></a>
      - <a href="#id2" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpCollection.is_spin_polarized</code></span></a>
    - <a href="#pymatgen.electronic_structure.cohp.IcohpValue"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">IcohpValue</code></span></a>
      - <a href="#pymatgen.electronic_structure.cohp.IcohpValue.energies"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpValue.energies</code></span></a>
      - <a href="#pymatgen.electronic_structure.cohp.IcohpValue.densities"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpValue.densities</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.cohp.IcohpValue.energies_are_cartesian"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpValue.energies_are_cartesian</code></span></a>
      - <a href="#pymatgen.electronic_structure.cohp.IcohpValue.are_coops"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpValue.are_coops</code></span></a>
      - <a href="#pymatgen.electronic_structure.cohp.IcohpValue.are_cobis"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpValue.are_cobis</code></span></a>
      - <a href="#pymatgen.electronic_structure.cohp.IcohpValue.icohp"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpValue.icohp</code></span></a>
      - <a href="#pymatgen.electronic_structure.cohp.IcohpValue.summed_icohp"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpValue.summed_icohp</code></span></a>
      - <a href="#pymatgen.electronic_structure.cohp.IcohpValue.num_bonds"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpValue.num_bonds</code></span></a>
      - <a href="#id3" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpValue.are_cobis</code></span></a>
      - <a href="#id4" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpValue.are_coops</code></span></a>
      - <a href="#id5" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpValue.icohp</code></span></a>
      - <a href="#pymatgen.electronic_structure.cohp.IcohpValue.icohpvalue"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpValue.icohpvalue()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.cohp.IcohpValue.icohpvalue_orbital"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpValue.icohpvalue_orbital()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.cohp.IcohpValue.is_spin_polarized"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpValue.is_spin_polarized</code></span></a>
      - <a href="#id6" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpValue.num_bonds</code></span></a>
      - <a href="#id7" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpValue.summed_icohp</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.cohp.IcohpValue.summed_orbital_icohp"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IcohpValue.summed_orbital_icohp</code></span></a>
    - <a
      href="#pymatgen.electronic_structure.cohp.get_integrated_cohp_in_energy_range"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">get_integrated_cohp_in_energy_range()</code></span></a>
  - <a href="#module-pymatgen.electronic_structure.core"
    class="reference internal">pymatgen.electronic_structure.core module</a>
    - <a href="#pymatgen.electronic_structure.core.Magmom"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Magmom</code></span></a>
      - <a href="#pymatgen.electronic_structure.core.Magmom.are_collinear"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Magmom.are_collinear()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.core.Magmom.from_global_moment_and_saxis"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Magmom.from_global_moment_and_saxis()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.core.Magmom.from_moment_relative_to_crystal_axes"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Magmom.from_moment_relative_to_crystal_axes()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.core.Magmom.get_00t_magmom_with_xyz_saxis"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Magmom.get_00t_magmom_with_xyz_saxis()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.core.Magmom.get_consistent_set_and_saxis"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Magmom.get_consistent_set_and_saxis()</code></span></a>
      - <a href="#pymatgen.electronic_structure.core.Magmom.get_moment"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Magmom.get_moment()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.core.Magmom.get_moment_relative_to_crystal_axes"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Magmom.get_moment_relative_to_crystal_axes()</code></span></a>
      - <a href="#pymatgen.electronic_structure.core.Magmom.get_suggested_saxis"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Magmom.get_suggested_saxis()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.core.Magmom.get_xyz_magmom_with_001_saxis"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Magmom.get_xyz_magmom_with_001_saxis()</code></span></a>
      - <a href="#pymatgen.electronic_structure.core.Magmom.global_moment"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Magmom.global_moment</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.core.Magmom.have_consistent_saxis"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Magmom.have_consistent_saxis()</code></span></a>
      - <a href="#pymatgen.electronic_structure.core.Magmom.projection"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Magmom.projection</code></span></a>
    - <a href="#pymatgen.electronic_structure.core.Orbital"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Orbital</code></span></a>
      - <a href="#pymatgen.electronic_structure.core.Orbital.dx2"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Orbital.dx2</code></span></a>
      - <a href="#pymatgen.electronic_structure.core.Orbital.dxy"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Orbital.dxy</code></span></a>
      - <a href="#pymatgen.electronic_structure.core.Orbital.dxz"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Orbital.dxz</code></span></a>
      - <a href="#pymatgen.electronic_structure.core.Orbital.dyz"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Orbital.dyz</code></span></a>
      - <a href="#pymatgen.electronic_structure.core.Orbital.dz2"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Orbital.dz2</code></span></a>
      - <a href="#pymatgen.electronic_structure.core.Orbital.f0"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Orbital.f0</code></span></a>
      - <a href="#pymatgen.electronic_structure.core.Orbital.f1"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Orbital.f1</code></span></a>
      - <a href="#pymatgen.electronic_structure.core.Orbital.f2"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Orbital.f2</code></span></a>
      - <a href="#pymatgen.electronic_structure.core.Orbital.f3"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Orbital.f3</code></span></a>
      - <a href="#pymatgen.electronic_structure.core.Orbital.f_1"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Orbital.f_1</code></span></a>
      - <a href="#pymatgen.electronic_structure.core.Orbital.f_2"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Orbital.f_2</code></span></a>
      - <a href="#pymatgen.electronic_structure.core.Orbital.f_3"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Orbital.f_3</code></span></a>
      - <a href="#pymatgen.electronic_structure.core.Orbital.orbital_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Orbital.orbital_type</code></span></a>
      - <a href="#pymatgen.electronic_structure.core.Orbital.px"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Orbital.px</code></span></a>
      - <a href="#pymatgen.electronic_structure.core.Orbital.py"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Orbital.py</code></span></a>
      - <a href="#pymatgen.electronic_structure.core.Orbital.pz"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Orbital.pz</code></span></a>
      - <a href="#pymatgen.electronic_structure.core.Orbital.s"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Orbital.s</code></span></a>
    - <a href="#pymatgen.electronic_structure.core.OrbitalType"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">OrbitalType</code></span></a>
      - <a href="#pymatgen.electronic_structure.core.OrbitalType.d"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">OrbitalType.d</code></span></a>
      - <a href="#pymatgen.electronic_structure.core.OrbitalType.f"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">OrbitalType.f</code></span></a>
      - <a href="#pymatgen.electronic_structure.core.OrbitalType.p"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">OrbitalType.p</code></span></a>
      - <a href="#pymatgen.electronic_structure.core.OrbitalType.s"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">OrbitalType.s</code></span></a>
    - <a href="#pymatgen.electronic_structure.core.Spin"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Spin</code></span></a>
      - <a href="#pymatgen.electronic_structure.core.Spin.down"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Spin.down</code></span></a>
      - <a href="#pymatgen.electronic_structure.core.Spin.up"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Spin.up</code></span></a>
  - <a href="#module-pymatgen.electronic_structure.dos"
    class="reference internal">pymatgen.electronic_structure.dos module</a>
    - <a href="#pymatgen.electronic_structure.dos.CompleteDos"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">CompleteDos</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.CompleteDos.structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteDos.structure</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.CompleteDos.pdos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteDos.pdos</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.CompleteDos.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteDos.as_dict()</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.CompleteDos.fp_to_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteDos.fp_to_dict()</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.CompleteDos.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteDos.from_dict()</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.CompleteDos.get_band_center"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteDos.get_band_center()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.dos.CompleteDos.get_band_filling"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteDos.get_band_filling()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.dos.CompleteDos.get_band_kurtosis"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteDos.get_band_kurtosis()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.dos.CompleteDos.get_band_skewness"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteDos.get_band_skewness()</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.CompleteDos.get_band_width"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteDos.get_band_width()</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.CompleteDos.get_dos_fp"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteDos.get_dos_fp()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.dos.CompleteDos.get_dos_fp_similarity"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteDos.get_dos_fp_similarity()</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.CompleteDos.get_element_dos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteDos.get_element_dos()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.dos.CompleteDos.get_element_spd_dos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteDos.get_element_spd_dos()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.dos.CompleteDos.get_hilbert_transform"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteDos.get_hilbert_transform()</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.CompleteDos.get_n_moment"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteDos.get_n_moment()</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.CompleteDos.get_normalized"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteDos.get_normalized()</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.CompleteDos.get_site_dos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteDos.get_site_dos()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.dos.CompleteDos.get_site_orbital_dos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteDos.get_site_orbital_dos()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.dos.CompleteDos.get_site_spd_dos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteDos.get_site_spd_dos()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.dos.CompleteDos.get_site_t2g_eg_resolved_dos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteDos.get_site_t2g_eg_resolved_dos()</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.CompleteDos.get_spd_dos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteDos.get_spd_dos()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.dos.CompleteDos.get_upper_band_edge"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteDos.get_upper_band_edge()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.dos.CompleteDos.spin_polarization"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompleteDos.spin_polarization</code></span></a>
    - <a href="#pymatgen.electronic_structure.dos.DOS"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">DOS</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.DOS.energies"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DOS.energies</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.DOS.densities"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DOS.densities</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.DOS.efermi"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DOS.efermi</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.DOS.XLABEL"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DOS.XLABEL</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.DOS.YLABEL"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DOS.YLABEL</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.DOS.get_cbm_vbm"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DOS.get_cbm_vbm()</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.DOS.get_gap"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DOS.get_gap()</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.DOS.get_interpolated_gap"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DOS.get_interpolated_gap()</code></span></a>
    - <a href="#pymatgen.electronic_structure.dos.Dos"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Dos</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.Dos.energies"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Dos.energies</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.Dos.densities"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Dos.densities</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.Dos.efermi"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Dos.efermi</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.Dos.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Dos.as_dict()</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.Dos.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Dos.from_dict()</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.Dos.get_cbm_vbm"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Dos.get_cbm_vbm()</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.Dos.get_densities"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Dos.get_densities()</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.Dos.get_gap"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Dos.get_gap()</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.Dos.get_interpolated_gap"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Dos.get_interpolated_gap()</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.Dos.get_interpolated_value"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Dos.get_interpolated_value()</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.Dos.get_smeared_densities"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Dos.get_smeared_densities()</code></span></a>
    - <a href="#pymatgen.electronic_structure.dos.DosFingerprint"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">DosFingerprint</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.DosFingerprint.bin_width"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DosFingerprint.bin_width</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.DosFingerprint.densities"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DosFingerprint.densities</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.DosFingerprint.energies"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DosFingerprint.energies</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.DosFingerprint.fp_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DosFingerprint.fp_type</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.DosFingerprint.n_bins"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DosFingerprint.n_bins</code></span></a>
    - <a href="#pymatgen.electronic_structure.dos.FermiDos"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">FermiDos</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.FermiDos.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">FermiDos.as_dict()</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.FermiDos.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">FermiDos.from_dict()</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.FermiDos.get_doping"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">FermiDos.get_doping()</code></span></a>
      - <a href="#pymatgen.electronic_structure.dos.FermiDos.get_fermi"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">FermiDos.get_fermi()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.dos.FermiDos.get_fermi_interextrapolated"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">FermiDos.get_fermi_interextrapolated()</code></span></a>
    - <a href="#pymatgen.electronic_structure.dos.LobsterCompleteDos"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">LobsterCompleteDos</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.dos.LobsterCompleteDos.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LobsterCompleteDos.from_dict()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.dos.LobsterCompleteDos.get_element_spd_dos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LobsterCompleteDos.get_element_spd_dos()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.dos.LobsterCompleteDos.get_site_orbital_dos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LobsterCompleteDos.get_site_orbital_dos()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.dos.LobsterCompleteDos.get_site_t2g_eg_resolved_dos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LobsterCompleteDos.get_site_t2g_eg_resolved_dos()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.dos.LobsterCompleteDos.get_spd_dos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">LobsterCompleteDos.get_spd_dos()</code></span></a>
    - <a href="#pymatgen.electronic_structure.dos.add_densities"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">add_densities()</code></span></a>
    - <a href="#pymatgen.electronic_structure.dos.f0"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">f0()</code></span></a>
  - <a href="#module-pymatgen.electronic_structure.plotter"
    class="reference internal">pymatgen.electronic_structure.plotter
    module</a>
    - <a href="#pymatgen.electronic_structure.plotter.BSDOSPlotter"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">BSDOSPlotter</code></span></a>
      - <a href="#pymatgen.electronic_structure.plotter.BSDOSPlotter.get_plot"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BSDOSPlotter.get_plot()</code></span></a>
    - <a href="#pymatgen.electronic_structure.plotter.BSPlotter"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">BSPlotter</code></span></a>
      - <a href="#pymatgen.electronic_structure.plotter.BSPlotter.add_bs"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BSPlotter.add_bs()</code></span></a>
      - <a href="#pymatgen.electronic_structure.plotter.BSPlotter.bs_plot_data"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BSPlotter.bs_plot_data()</code></span></a>
      - <a href="#pymatgen.electronic_structure.plotter.BSPlotter.get_plot"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BSPlotter.get_plot()</code></span></a>
      - <a href="#pymatgen.electronic_structure.plotter.BSPlotter.get_ticks"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BSPlotter.get_ticks()</code></span></a>
      - <a href="#pymatgen.electronic_structure.plotter.BSPlotter.get_ticks_old"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BSPlotter.get_ticks_old()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.plotter.BSPlotter.plot_brillouin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BSPlotter.plot_brillouin()</code></span></a>
      - <a href="#pymatgen.electronic_structure.plotter.BSPlotter.plot_compare"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BSPlotter.plot_compare()</code></span></a>
      - <a href="#pymatgen.electronic_structure.plotter.BSPlotter.save_plot"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BSPlotter.save_plot()</code></span></a>
      - <a href="#pymatgen.electronic_structure.plotter.BSPlotter.show"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BSPlotter.show()</code></span></a>
    - <a href="#pymatgen.electronic_structure.plotter.BSPlotterProjected"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">BSPlotterProjected</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.plotter.BSPlotterProjected.get_elt_projected_plots"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BSPlotterProjected.get_elt_projected_plots()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.plotter.BSPlotterProjected.get_elt_projected_plots_color"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BSPlotterProjected.get_elt_projected_plots_color()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.plotter.BSPlotterProjected.get_projected_plots_dots"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BSPlotterProjected.get_projected_plots_dots()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.plotter.BSPlotterProjected.get_projected_plots_dots_patom_pmorb"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BSPlotterProjected.get_projected_plots_dots_patom_pmorb()</code></span></a>
    - <a href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">BoltztrapPlotter</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_carriers"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapPlotter.plot_carriers()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_complexity_factor_mu"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapPlotter.plot_complexity_factor_mu()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_conductivity_dop"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapPlotter.plot_conductivity_dop()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_conductivity_mu"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapPlotter.plot_conductivity_mu()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_conductivity_temp"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapPlotter.plot_conductivity_temp()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_dos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapPlotter.plot_dos()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_eff_mass_dop"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapPlotter.plot_eff_mass_dop()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_eff_mass_temp"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapPlotter.plot_eff_mass_temp()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_hall_carriers"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapPlotter.plot_hall_carriers()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_power_factor_dop"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapPlotter.plot_power_factor_dop()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_power_factor_mu"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapPlotter.plot_power_factor_mu()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_power_factor_temp"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapPlotter.plot_power_factor_temp()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_seebeck_dop"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapPlotter.plot_seebeck_dop()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_seebeck_eff_mass_mu"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapPlotter.plot_seebeck_eff_mass_mu()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_seebeck_mu"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapPlotter.plot_seebeck_mu()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_seebeck_temp"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapPlotter.plot_seebeck_temp()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_zt_dop"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapPlotter.plot_zt_dop()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_zt_mu"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapPlotter.plot_zt_mu()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_zt_temp"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoltztrapPlotter.plot_zt_temp()</code></span></a>
    - <a href="#pymatgen.electronic_structure.plotter.CohpPlotter"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">CohpPlotter</code></span></a>
      - <a href="#pymatgen.electronic_structure.plotter.CohpPlotter.add_cohp"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CohpPlotter.add_cohp()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.plotter.CohpPlotter.add_cohp_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CohpPlotter.add_cohp_dict()</code></span></a>
      - <a
        href="#pymatgen.electronic_structure.plotter.CohpPlotter.get_cohp_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CohpPlotter.get_cohp_dict()</code></span></a>
      - <a href="#pymatgen.electronic_structure.plotter.CohpPlotter.get_plot"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CohpPlotter.get_plot()</code></span></a>
      - <a href="#pymatgen.electronic_structure.plotter.CohpPlotter.save_plot"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CohpPlotter.save_plot()</code></span></a>
      - <a href="#pymatgen.electronic_structure.plotter.CohpPlotter.show"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CohpPlotter.show()</code></span></a>
    - <a href="#pymatgen.electronic_structure.plotter.DosPlotter"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">DosPlotter</code></span></a>
      - <a href="#pymatgen.electronic_structure.plotter.DosPlotter.add_dos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DosPlotter.add_dos()</code></span></a>
      - <a href="#pymatgen.electronic_structure.plotter.DosPlotter.add_dos_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DosPlotter.add_dos_dict()</code></span></a>
      - <a href="#pymatgen.electronic_structure.plotter.DosPlotter.get_dos_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DosPlotter.get_dos_dict()</code></span></a>
      - <a href="#pymatgen.electronic_structure.plotter.DosPlotter.get_plot"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DosPlotter.get_plot()</code></span></a>
      - <a href="#pymatgen.electronic_structure.plotter.DosPlotter.save_plot"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DosPlotter.save_plot()</code></span></a>
      - <a href="#pymatgen.electronic_structure.plotter.DosPlotter.show"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DosPlotter.show()</code></span></a>
    - <a href="#pymatgen.electronic_structure.plotter.fold_point"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">fold_point()</code></span></a>
    - <a href="#pymatgen.electronic_structure.plotter.plot_brillouin_zone"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">plot_brillouin_zone()</code></span></a>
    - <a
      href="#pymatgen.electronic_structure.plotter.plot_brillouin_zone_from_kpath"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">plot_brillouin_zone_from_kpath()</code></span></a>
    - <a href="#pymatgen.electronic_structure.plotter.plot_ellipsoid"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">plot_ellipsoid()</code></span></a>
    - <a href="#pymatgen.electronic_structure.plotter.plot_fermi_surface"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">plot_fermi_surface()</code></span></a>
    - <a href="#pymatgen.electronic_structure.plotter.plot_labels"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">plot_labels()</code></span></a>
    - <a href="#pymatgen.electronic_structure.plotter.plot_lattice_vectors"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">plot_lattice_vectors()</code></span></a>
    - <a href="#pymatgen.electronic_structure.plotter.plot_path"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">plot_path()</code></span></a>
    - <a href="#pymatgen.electronic_structure.plotter.plot_points"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">plot_points()</code></span></a>
    - <a href="#pymatgen.electronic_structure.plotter.plot_wigner_seitz"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">plot_wigner_seitz()</code></span></a>

</div>

</div>

</div>

<div class="section wy-nav-content-wrap" toggle="wy-nav-shift">

[pymatgen](index.html)

<div class="wy-nav-content">

<div class="rst-content style-external-links">

<div role="navigation" aria-label="Page navigation">

- <a href="index.html" class="icon icon-home" aria-label="Home"></a>
- pymatgen.electronic_structure package
- <a
  href="https://github.com/materialsproject/pymatgen/blob/master/docs_rst/pymatgen.electronic_structure.rst"
  class="fa fa-github">Edit on GitHub</a>

------------------------------------------------------------------------

</div>

<div class="document" role="main" itemscope="itemscope"
itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="module-pymatgen.electronic_structure" class="section">

<span id="pymatgen-electronic-structure-package"></span>

# pymatgen.electronic_structure package<a href="#module-pymatgen.electronic_structure" class="headerlink"
title="Link to this heading"></a>

This package contains electronic structure related tools and analyses.

<div id="submodules" class="section">

## Submodules<a href="#submodules" class="headerlink"
title="Link to this heading"></a>

</div>

<div id="module-pymatgen.electronic_structure.bandstructure"
class="section">

<span id="pymatgen-electronic-structure-bandstructure-module"></span>

## pymatgen.electronic_structure.bandstructure module<a href="#module-pymatgen.electronic_structure.bandstructure"
class="headerlink" title="Link to this heading"></a>

This module provides classes to define things related to band
structures.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">BandStructure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">kpoints</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">eigenvals</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Mapping</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">ArrayLike</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">lattice</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.lattice.Lattice"
class="reference internal" title="pymatgen.core.lattice.Lattice"><span
class="pre">Lattice</span></a></span>*, *<span class="n"><span class="pre">efermi</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">labels_dict</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Mapping</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><a href="#pymatgen.electronic_structure.bandstructure.Kpoint"
class="reference internal"
title="pymatgen.electronic_structure.bandstructure.Kpoint"><span
class="pre">Kpoint</span></a><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">coords_are_cartesian</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">projections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Mapping</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">NDArray</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/bandstructure.py#L157-L706"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.bandstructure.BandStructure"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Generic band structure data, defined by a list of Kpoints  
and corresponding energies for each of them.

<span class="sig-name descname"><span class="pre">kpoints</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/bandstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.BandStructure.kpoints"
class="headerlink" title="Link to this definition"></a>  
Kpoints in the band structure.

Type<span class="colon">:</span>  
list\[<a href="#pymatgen.electronic_structure.bandstructure.Kpoint"
class="reference internal"
title="pymatgen.electronic_structure.bandstructure.Kpoint">Kpoint</a>\]

<span class="sig-name descname"><span class="pre">lattice_rec</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/bandstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.BandStructure.lattice_rec"
class="headerlink" title="Link to this definition"></a>  
The reciprocal lattice of the band structure.

Type<span class="colon">:</span>  
<a href="pymatgen.core.html#pymatgen.core.lattice.Lattice"
class="reference internal"
title="pymatgen.core.lattice.Lattice">Lattice</a>

<span class="sig-name descname"><span class="pre">efermi</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/bandstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.BandStructure.efermi"
class="headerlink" title="Link to this definition"></a>  
The Fermi level.

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">is_spin_polarized</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/bandstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.BandStructure.is_spin_polarized"
class="headerlink" title="Link to this definition"></a>  
Whether the band structure is spin-polarized.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">bands</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/bandstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.BandStructure.bands"
class="headerlink" title="Link to this definition"></a>  
The energy eigenvalues. Note that the use of an array is necessary for
computational and memory efficiency due to the large amount of numerical
data. The indices of the array are (band_index, kpoint_index).

Type<span class="colon">:</span>  
dict\[<a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin">Spin</a>, NDArray\]

<span class="sig-name descname"><span class="pre">nb_bands</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/bandstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.BandStructure.nb_bands"
class="headerlink" title="Link to this definition"></a>  
The number of bands in the band structure.

Type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">structure</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/bandstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.BandStructure.structure"
class="headerlink" title="Link to this definition"></a>  
The structure.

Type<span class="colon">:</span>  
<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure">Structure</a>

<span class="sig-name descname"><span class="pre">projections</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/bandstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.BandStructure.projections"
class="headerlink" title="Link to this definition"></a>  
The projections. Note that the use of an array is necessary for
computational and memory efficiency due to the large amount of numerical
data. The indices of the array are (band_index, kpoint_index,
orbital_index, ion_index).

Type<span class="colon">:</span>  
dict\[<a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin">Spin</a>, NDArray\]

Parameters<span class="colon">:</span>  
- **kpoints** (*NDArray*) – Kpoint as NumPy array, in frac_coords of the
  given lattice by default.

- **eigenvals** (*dict*) – Energies for spin up and spin down as
  {Spin.up:\[\]\[\], Spin.down:\[\]\[\]}, the first index of the array
  \[\]\[\] refers to the band and the second to the index of the kpoint.
  The kpoints are ordered according to the kpoints array. If the band
  structure is not spin polarized, we only store one data set under
  Spin.up.

- **lattice**
  (<a href="pymatgen.core.html#pymatgen.core.lattice.Lattice"
  class="reference internal"
  title="pymatgen.core.lattice.Lattice"><em>Lattice</em></a>) – The
  reciprocal lattice. Pymatgen uses the physics convention of reciprocal
  lattice vectors with a 2\*pi coefficient.

- **efermi** (*float*) – The Fermi level.

- **labels_dict** (*dict\[str,*
  <a href="#pymatgen.electronic_structure.bandstructure.Kpoint"
  class="reference internal"
  title="pymatgen.electronic_structure.bandstructure.Kpoint"><em>Kpoint</em></a>*\]*)
  – Dict mapping label to Kpoint.

- **coords_are_cartesian** (*bool*) – Whether coordinates are cartesian.

- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  The crystal structure associated with the band structure. This is
  needed if we provide projections to the band structure.

- **projections**
  (*dict\[*<a href="#pymatgen.electronic_structure.core.Spin"
  class="reference internal"
  title="pymatgen.electronic_structure.core.Spin"><em>Spin</em></a>*,*
  *NDArray\]*) – Orbital projections. The indices of the array are
  (band_index, kpoint_index, orbital_index, ion_index). If the band
  structure is not spin polarized, we only store one data set under
  Spin.up.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/bandstructure.py#L569-L611"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.BandStructure.as_dict"
class="headerlink" title="Link to this definition"></a>  
JSON-serializable dict representation of BandStructure.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/bandstructure.py#L613-L661"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.BandStructure.from_dict"
class="headerlink" title="Link to this definition"></a>  
Create from a dict.

Parameters<span class="colon">:</span>  
**dct** – A dict with all data for a BandStructure.

Returns<span class="colon">:</span>  
BandStructure

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_old_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/bandstructure.py#L663-L706"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.BandStructure.from_old_dict"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
**dct** (*dict*) – A dict with all data for a BandStructure object.

Returns<span class="colon">:</span>  
BandStructure

<span class="sig-name descname"><span class="pre">get_band_gap</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/bandstructure.py#L444-L476"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.BandStructure.get_band_gap"
class="headerlink" title="Link to this definition"></a>  
Get band gap.

Returns<span class="colon">:</span>  
“energy” (float): Band gap energy. “direct” (bool): Whether the gap is
direct. “transition” (str): Kpoint labels of the transition (e.g.,
“\Gamma-X”).

Return type<span class="colon">:</span>  
dict with keys “energy”, “direct”, “transition”

<span class="sig-name descname"><span class="pre">get_cbm</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/bandstructure.py#L378-L442"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.BandStructure.get_cbm"
class="headerlink" title="Link to this definition"></a>  
Get data about the conduction band minimum (CBM).

Returns<span class="colon">:</span>  
- “band_index” (dict): A dict with spin keys pointing to a list of the

indices of the band containing the CBM (please note that you can have
several bands sharing the CBM) {Spin.up:\[\], Spin.down:\[\]}. -
“kpoint_index”: The list of indices in self.kpoints for the kpoint CBM.
Please note that there can be several kpoint_indices relating to the
same kpoint (e.g., Gamma can occur at different spots in the band
structure line plot). - “kpoint” (Kpoint): The kpoint. - “energy”
(float): The energy of the CBM. - “projections”: The projections along
sites and orbitals of the CBM if any projection data is available (else
it is an empty dictionary). The format is similar to the projections
field in BandStructure: {spin:{‘Orbital’: \[proj\]}} where the array
\[proj\] is ordered according to the sites in structure.

Return type<span class="colon">:</span>  
dict with keys “band_index”, “kpoint_index”, “kpoint”, “energy”

<span class="sig-name descname"><span class="pre">get_direct_band_gap</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/bandstructure.py#L507-L517"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.BandStructure.get_direct_band_gap"
class="headerlink" title="Link to this definition"></a>  
Get the direct band gap.

Returns<span class="colon">:</span>  
The direct band gap value.

Return type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">get_direct_band_gap_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/bandstructure.py#L478-L505"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.BandStructure.get_direct_band_gap_dict"
class="headerlink" title="Link to this definition"></a>  
Get information about the direct band gap.

Returns<span class="colon">:</span>  
The band gaps indexed by spin  
along with their band indices and kpoint index.

Return type<span class="colon">:</span>  
dict\[<a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin">Spin</a>, dict\[str,
Any\]\]

<span class="sig-name descname"><span class="pre">get_kpoint_degeneracy</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">kpoint</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">NDArray</span></span>*, *<span class="n"><span class="pre">cartesian</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.01</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/bandstructure.py#L550-L567"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.BandStructure.get_kpoint_degeneracy"
class="headerlink" title="Link to this definition"></a>  
Get degeneracy of a given kpoint based on structure symmetry.

Parameters<span class="colon">:</span>  
- **kpoint** (*1x3 NDArray*) – Coordinate of the k-point.

- **cartesian** (*bool*) – Whether kpoint is in Cartesian or fractional
  coordinates.

- **tol** (*float*) – Tolerance below which coordinates are considered
  equal.

Returns<span class="colon">:</span>  
Degeneracy, or None if structure is not available.

Return type<span class="colon">:</span>  
int \| None

<span class="sig-name descname"><span class="pre">get_projection_on_elements</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/bandstructure.py#L242-L261"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.BandStructure.get_projection_on_elements"
class="headerlink" title="Link to this definition"></a>  
Get projections on elements.

Returns<span class="colon">:</span>  
Dict in {Spin.up:\[\]\[{Element: \[values\]}\],  
Spin.down: \[\]\[{Element: \[values\]}\]} format. If there is no
projections in the band structure, return {}.

Return type<span class="colon">:</span>  
dict\[<a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin">Spin</a>, NDArray\]

<span class="sig-name descname"><span class="pre">get_projections_on_elements_and_orbitals</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">el_orb_spec</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/bandstructure.py#L263-L296"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.BandStructure.get_projections_on_elements_and_orbitals"
class="headerlink" title="Link to this definition"></a>  
Get projections on elements and specific orbitals.

Parameters<span class="colon">:</span>  
**el_orb_spec** (*dict\[str,* *list\[str\]\]*) – Elements and orbitals
to project onto. Format is {Element: \[orbitals\]}, e.g. {“Cu”: \[“d”,
“s”\]}.

Returns<span class="colon">:</span>  
Projections on elements in the  
{Spin.up: \[\]\[{Element: {orb: values}}\], Spin.down: \[\]\[{Element:
{orb: values}}\]} format. If there is no projections in the band
structure, return {}.

Return type<span class="colon">:</span>  
dict\[str, list\[str\]

<span class="sig-name descname"><span class="pre">get_sym_eq_kpoints</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">kpoint</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">NDArray</span></span>*, *<span class="n"><span class="pre">cartesian</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.01</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">NDArray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/bandstructure.py#L519-L548"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.BandStructure.get_sym_eq_kpoints"
class="headerlink" title="Link to this definition"></a>  
Get unique symmetrically equivalent Kpoints.

Parameters<span class="colon">:</span>  
- **kpoint** (*1x3 array*) – Coordinate of the Kpoint.

- **cartesian** (*bool*) – Whether kpoint is in Cartesian or fractional
  coordinates.

- **tol** (*float*) – Tolerance below which coordinates are considered
  equal.

Returns<span class="colon">:</span>  
None if structure is not available.

Return type<span class="colon">:</span>  
(1x3 NDArray) \| None

<span class="sig-name descname"><span class="pre">get_vbm</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/bandstructure.py#L311-L376"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.BandStructure.get_vbm"
class="headerlink" title="Link to this definition"></a>  
Get data about the valence band maximum (VBM).

Returns<span class="colon">:</span>  
- “band_index” (dict): A dict with spin keys pointing to a list of the

indices of the band containing the VBM (please note that you can have
several bands sharing the VBM) {Spin.up:\[\], Spin.down:\[\]}. -
“kpoint_index”: The list of indices in self.kpoints for the kpoint VBM.
Please note that there can be several kpoint_indices relating to the
same kpoint (e.g., Gamma can occur at different spots in the band
structure line plot). - “kpoint” (Kpoint): The kpoint. - “energy”
(float): The energy of the VBM. - “projections”: The projections along
sites and orbitals of the VBM if any projection data is available (else
it is an empty dictionary). The format is similar to the projections
field in BandStructure: {spin:{‘Orbital’: \[proj\]}} where the array
\[proj\] is ordered according to the sites in structure.

Return type<span class="colon">:</span>  
dict with keys “band_index”, “kpoint_index”, “kpoint”, “energy”

<span class="sig-name descname"><span class="pre">is_metal</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">efermi_tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.0001</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/bandstructure.py#L298-L309"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.BandStructure.is_metal"
class="headerlink" title="Link to this definition"></a>  
Check if the band structure indicates a metal, by looking at if the
fermi level crosses a band.

Returns<span class="colon">:</span>  
True if is metal.

Return type<span class="colon">:</span>  
bool

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">BandStructureSymmLine</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">kpoints</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">eigenvals</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Mapping</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">ArrayLike</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">lattice</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.lattice.Lattice"
class="reference internal" title="pymatgen.core.lattice.Lattice"><span
class="pre">Lattice</span></a></span>*, *<span class="n"><span class="pre">efermi</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">labels_dict</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Mapping</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><a href="#pymatgen.electronic_structure.bandstructure.Kpoint"
class="reference internal"
title="pymatgen.electronic_structure.bandstructure.Kpoint"><span
class="pre">Kpoint</span></a><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">coords_are_cartesian</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">projections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Mapping</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">NDArray</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/bandstructure.py#L709-L906"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.BandStructureSymmLine"
class="headerlink" title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.electronic_structure.bandstructure.BandStructure"
class="reference internal"
title="pymatgen.electronic_structure.bandstructure.BandStructure"><span
class="pre"><code
class="sourceCode python">BandStructure</code></span></a>, <span
class="pre">`MSONable`</span>

Store band structures along selected (symmetry) lines in the Brillouin
zone. We call the different symmetry lines (ex: \Gamma to Z) “branches”.

Parameters<span class="colon">:</span>  
- **kpoints** (*NDArray*) – Array of kpoint, in frac_coords of the given
  lattice by default

- **eigenvals**
  (*dict\[*<a href="#pymatgen.electronic_structure.core.Spin"
  class="reference internal"
  title="pymatgen.electronic_structure.core.Spin"><em>Spin</em></a>*,*
  *list\]*) – Energies for spin up and spin down
  {Spin.up:\[\]\[\],Spin.down:\[\]\[\]}, the first index of the array
  \[\]\[\] refers to the band and the second to the index of the kpoint.
  The kpoints are ordered according to the order of the kpoints array.
  If the band structure is not spin polarized, we only store one data
  set under Spin.up.

- **lattice**
  (<a href="pymatgen.core.html#pymatgen.core.lattice.Lattice"
  class="reference internal"
  title="pymatgen.core.lattice.Lattice"><em>Lattice</em></a>) – The
  reciprocal lattice. Pymatgen uses the physics convention of reciprocal
  lattice vectors with a 2\*pi coefficient.

- **efermi** (*float*) – The Fermi level.

- **labels_dict** (*dict\[str,*
  <a href="#pymatgen.electronic_structure.bandstructure.Kpoint"
  class="reference internal"
  title="pymatgen.electronic_structure.bandstructure.Kpoint"><em>Kpoint</em></a>*\]*)
  – Dict mapping label to Kpoint.

- **coords_are_cartesian** (*bool*) – Whether coordinates are cartesian.

- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  The crystal structure associated with the band structure. This is
  needed if we provide projections to the band structure.

- **projections**
  (*dict\[*<a href="#pymatgen.electronic_structure.core.Spin"
  class="reference internal"
  title="pymatgen.electronic_structure.core.Spin"><em>Spin</em></a>*,*
  *NDArray\]*) – Orbital projections as {spin: array}. The indices of
  the array are \[band_index, kpoint_index, orbital_index,
  ion_index\].If the band structure is not spin polarized, we only store
  one data set under Spin.up.

<span class="sig-name descname"><span class="pre">apply_scissor</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">new_band_gap</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/bandstructure.py#L847-L900"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.BandStructureSymmLine.apply_scissor"
class="headerlink" title="Link to this definition"></a>  
Apply a scissor operator (shift of the CBM) to fit the given band gap.
If it’s a metal, we look for the band crossing the Fermi level and shift
this one up. This will not work all the time for metals!

Parameters<span class="colon">:</span>  
**new_band_gap** (*float*) – The band gap the scissor band structure
need to have.

Returns<span class="colon">:</span>  
With the applied scissor shift.

Return type<span class="colon">:</span>  
<a
href="#pymatgen.electronic_structure.bandstructure.BandStructureSymmLine"
class="reference internal"
title="pymatgen.electronic_structure.bandstructure.BandStructureSymmLine">BandStructureSymmLine</a>

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/bandstructure.py#L902-L906"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.BandStructureSymmLine.as_dict"
class="headerlink" title="Link to this definition"></a>  
JSON-serializable dict representation of BandStructureSymmLine.

<span class="sig-name descname"><span class="pre">get_branch</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">index</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/bandstructure.py#L824-L845"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.BandStructureSymmLine.get_branch"
class="headerlink" title="Link to this definition"></a>  
Get what branch(es) is the kpoint. It takes into account the  
fact that one kpoint (e.g., Gamma) can be in several branches.

Parameters<span class="colon">:</span>  
**index** (*int*) – The kpoint index.

Returns<span class="colon">:</span>  
A list of dicts \[{“name”, “start_index”, “end_index”, “index”}\]  
indicating all branches in which the k_point is.

<span class="sig-name descname"><span class="pre">get_equivalent_kpoints</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">index</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/bandstructure.py#L800-L822"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.BandStructureSymmLine.get_equivalent_kpoints"
class="headerlink" title="Link to this definition"></a>  
Get kpoint indices equivalent (having the same coords) to the given one.

Parameters<span class="colon">:</span>  
**index** (*int*) – The kpoint index

Returns<span class="colon">:</span>  
Equivalent indices.

Return type<span class="colon">:</span>  
list\[int\]

TODO: now it uses the label, we might want to use coordinates instead in
case there was a mislabel.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Kpoint</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">coords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">lattice</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.lattice.Lattice"
class="reference internal" title="pymatgen.core.lattice.Lattice"><span
class="pre">Lattice</span></a></span>*, *<span class="n"><span class="pre">to_unit_cell</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">coords_are_cartesian</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/bandstructure.py#L38-L154"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.bandstructure.Kpoint"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

A kpoint defined with a lattice and frac or Cartesian coordinates,
similar to the Site object in pymatgen.core.structure.

Parameters<span class="colon">:</span>  
- **coords** (*NDArray*) – Coordinate of the Kpoint.

- **lattice**
  (<a href="pymatgen.core.html#pymatgen.core.lattice.Lattice"
  class="reference internal"
  title="pymatgen.core.lattice.Lattice"><em>Lattice</em></a>) – The
  reciprocal lattice of the kpoint.

- **to_unit_cell** (*bool*) – Translate fractional coordinate to the
  basic unit cell, i.e., all fractional coordinates satisfy 0 \<= a
  \< 1. Defaults to False.

- **coords_are_cartesian** (*bool*) – Whether the coordinates given are
  in Cartesian (True) or fractional coordinates (by default fractional).

- **label** (*str*) – The label of the Kpoint if any (None by default).

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">a</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/bandstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.bandstructure.Kpoint.a"
class="headerlink" title="Link to this definition"></a>  
Fractional a coordinate of the kpoint.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/bandstructure.py#L127-L136"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.bandstructure.Kpoint.as_dict"
class="headerlink" title="Link to this definition"></a>  
JSON-serializable dict representation of the kpoint.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">b</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/bandstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.bandstructure.Kpoint.b"
class="headerlink" title="Link to this definition"></a>  
Fractional b coordinate of the kpoint.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">c</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/bandstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.bandstructure.Kpoint.c"
class="headerlink" title="Link to this definition"></a>  
Fractional c coordinate of the kpoint.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">cart_coords</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">NDArray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/bandstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.Kpoint.cart_coords"
class="headerlink" title="Link to this definition"></a>  
The Cartesian coordinates of the kpoint as a NumPy array.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">frac_coords</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">NDArray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/bandstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.Kpoint.frac_coords"
class="headerlink" title="Link to this definition"></a>  
The fractional coordinates of the kpoint as a NumPy array.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/bandstructure.py#L138-L154"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.bandstructure.Kpoint.from_dict"
class="headerlink" title="Link to this definition"></a>  
Create from a dict.

Parameters<span class="colon">:</span>  
**dct** (*dict*) – A dict with all data for a kpoint object.

Returns<span class="colon">:</span>  
Kpoint

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">label</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/bandstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.bandstructure.Kpoint.label"
class="headerlink" title="Link to this definition"></a>  
The label associated with the kpoint.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">lattice</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.lattice.Lattice"
class="reference internal" title="pymatgen.core.lattice.Lattice"><span
class="pre">Lattice</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/bandstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.bandstructure.Kpoint.lattice"
class="headerlink" title="Link to this definition"></a>  
The lattice associated with the kpoint, as a Lattice object.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">LobsterBandStructureSymmLine</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">kpoints</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">eigenvals</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Mapping</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">ArrayLike</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">lattice</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.lattice.Lattice"
class="reference internal" title="pymatgen.core.lattice.Lattice"><span
class="pre">Lattice</span></a></span>*, *<span class="n"><span class="pre">efermi</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">labels_dict</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Mapping</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><a href="#pymatgen.electronic_structure.bandstructure.Kpoint"
class="reference internal"
title="pymatgen.electronic_structure.bandstructure.Kpoint"><span
class="pre">Kpoint</span></a><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">coords_are_cartesian</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">projections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Mapping</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">NDArray</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/bandstructure.py#L909-L1081"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.LobsterBandStructureSymmLine"
class="headerlink" title="Link to this definition"></a>  
Bases: <a
href="#pymatgen.electronic_structure.bandstructure.BandStructureSymmLine"
class="reference internal"
title="pymatgen.electronic_structure.bandstructure.BandStructureSymmLine"><span
class="pre"><code
class="sourceCode python">BandStructureSymmLine</code></span></a>

LOBSTER subclass of BandStructure with customized functions.

Parameters<span class="colon">:</span>  
- **kpoints** (*NDArray*) – Array of kpoint, in frac_coords of the given
  lattice by default

- **eigenvals**
  (*dict\[*<a href="#pymatgen.electronic_structure.core.Spin"
  class="reference internal"
  title="pymatgen.electronic_structure.core.Spin"><em>Spin</em></a>*,*
  *list\]*) – Energies for spin up and spin down
  {Spin.up:\[\]\[\],Spin.down:\[\]\[\]}, the first index of the array
  \[\]\[\] refers to the band and the second to the index of the kpoint.
  The kpoints are ordered according to the order of the kpoints array.
  If the band structure is not spin polarized, we only store one data
  set under Spin.up.

- **lattice**
  (<a href="pymatgen.core.html#pymatgen.core.lattice.Lattice"
  class="reference internal"
  title="pymatgen.core.lattice.Lattice"><em>Lattice</em></a>) – The
  reciprocal lattice. Pymatgen uses the physics convention of reciprocal
  lattice vectors with a 2\*pi coefficient.

- **efermi** (*float*) – The Fermi level.

- **labels_dict** (*dict\[str,*
  <a href="#pymatgen.electronic_structure.bandstructure.Kpoint"
  class="reference internal"
  title="pymatgen.electronic_structure.bandstructure.Kpoint"><em>Kpoint</em></a>*\]*)
  – Dict mapping label to Kpoint.

- **coords_are_cartesian** (*bool*) – Whether coordinates are cartesian.

- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  The crystal structure associated with the band structure. This is
  needed if we provide projections to the band structure.

- **projections**
  (*dict\[*<a href="#pymatgen.electronic_structure.core.Spin"
  class="reference internal"
  title="pymatgen.electronic_structure.core.Spin"><em>Spin</em></a>*,*
  *NDArray\]*) – Orbital projections as {spin: array}. The indices of
  the array are \[band_index, kpoint_index, orbital_index,
  ion_index\].If the band structure is not spin polarized, we only store
  one data set under Spin.up.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/bandstructure.py#L912-L953"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.LobsterBandStructureSymmLine.as_dict"
class="headerlink" title="Link to this definition"></a>  
JSON-serializable dict representation of BandStructureSymmLine.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/bandstructure.py#L955-L993"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.LobsterBandStructureSymmLine.from_dict"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
**dct** (*dict*) – All data for a LobsterBandStructureSymmLine object.

Returns<span class="colon">:</span>  
A LobsterBandStructureSymmLine object.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_old_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/bandstructure.py#L995-L1027"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.LobsterBandStructureSymmLine.from_old_dict"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
**dct** (*dict*) – All data for a LobsterBandStructureSymmLine object.

Returns<span class="colon">:</span>  
A LobsterBandStructureSymmLine object

<span class="sig-name descname"><span class="pre">get_projection_on_elements</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/bandstructure.py#L1029-L1046"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.LobsterBandStructureSymmLine.get_projection_on_elements"
class="headerlink" title="Link to this definition"></a>  
Get projections on elements. It sums over all available orbitals for
each element.

Returns<span class="colon">:</span>  
dict in the {Spin.up:\[\]\[{Element:values}\],  
Spin.down:\[\]\[{Element:values}\]} format. If there is no projections
in the band structure, return {}.

Return type<span class="colon">:</span>  
dict\[<a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin">Spin</a>, list\]

<span class="sig-name descname"><span class="pre">get_projections_on_elements_and_orbitals</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">el_orb_spec</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">SpeciesLike</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/bandstructure.py#L1048-L1081"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.LobsterBandStructureSymmLine.get_projections_on_elements_and_orbitals"
class="headerlink" title="Link to this definition"></a>  
Get projections on elements and specific orbitals.

Parameters<span class="colon">:</span>  
**el_orb_spec** (*dict*) – Elements and Orbitals for which we want to
project on. It is given as {Element: \[orbitals\]}, e.g. {“Si”: \[“3s”,
“3p”\]} or {“Si”: \[“3s”, “3p_x”, “3p_y”, “3p_z’\]} depending on input
files.

Returns<span class="colon">:</span>  
A dictionary of projections on elements in the
{Spin.up:\[\]\[{Element:{orb:values}}\],
Spin.down:\[\]\[{Element:{orb:values}}\]} format if there is no
projections in the band structure returns an empty dict.

<!-- -->

<span class="sig-name descname"><span class="pre">get_reconstructed_band_structure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">list_bs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.bandstructure.BandStructure"
class="reference internal"
title="pymatgen.electronic_structure.bandstructure.BandStructure"><span
class="pre">BandStructure</span></a><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">efermi</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.electronic_structure.bandstructure.BandStructure"
class="reference internal"
title="pymatgen.electronic_structure.bandstructure.BandStructure"><span
class="pre">BandStructure</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/bandstructure.py#L1100-L1160"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.bandstructure.get_reconstructed_band_structure"
class="headerlink" title="Link to this definition"></a>  
<span class="sig-name descname"><span class="pre">get_reconstructed_band_structure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">list_bs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a
href="#pymatgen.electronic_structure.bandstructure.BandStructureSymmLine"
class="reference internal"
title="pymatgen.electronic_structure.bandstructure.BandStructureSymmLine"><span
class="pre">BandStructureSymmLine</span></a><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">efermi</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a
href="#pymatgen.electronic_structure.bandstructure.BandStructureSymmLine"
class="reference internal"
title="pymatgen.electronic_structure.bandstructure.BandStructureSymmLine"><span
class="pre">BandStructureSymmLine</span></a></span></span>  
Merge multiple BandStructure(SymmLine) objects to a single one.

This is typically useful when you split non self-consistent band
structure runs to several independent jobs and want to merge the
results.

Parameters<span class="colon">:</span>  
- **list_bs** (*list*) – BandStructure or BandStructureSymmLine objects.

- **efermi** (*float*) – The Fermi level of the reconstructed band
  structure. If None, an average of all the Fermi levels in each object
  in the list_bs is used.

Returns<span class="colon">:</span>  
A BandStructure or BandStructureSymmLine object (depending on the type
of the objects in list_bs).

</div>

<div id="module-pymatgen.electronic_structure.boltztrap"
class="section">

<span id="pymatgen-electronic-structure-boltztrap-module"></span>

## pymatgen.electronic_structure.boltztrap module<a href="#module-pymatgen.electronic_structure.boltztrap"
class="headerlink" title="Link to this heading"></a>

This module provides classes to run and analyze BoltzTraP on pymatgen
band structure objects. BoltzTraP is a software developed by Georg
Madsen to interpolate band structures and compute materials properties
from this band structure using Boltzmann semi-classical transport
theory.

<a
href="https://www.tuwien.at/en/tch/tc/theoretical-materials-chemistry/boltztrap"
class="reference external">https://www.tuwien.at/en/tch/tc/theoretical-materials-chemistry/boltztrap</a>

You need version 1.2.3 or higher

References

Madsen, G. K. H., and Singh, D. J. (2006). BoltzTraP. A code for
calculating band-structure dependent quantities. Computer Physics
Communications, 175, 67-71

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">BoltztrapAnalyzer</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">gap</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">mu_steps</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">cond</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">seebeck</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">kappa</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">hall</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">doping</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">mu_doping</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">seebeck_doping</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">cond_doping</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">kappa_doping</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">hall_doping</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">intrans</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">dos</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">dos_partial</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">carrier_conc</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">vol</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">warning</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">bz_bands</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">bz_kpoints</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">fermi_surface_data</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L705-L2149"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Store all the data from a boltztrap run.

Constructor taking directly all the data generated by BoltzTraP. You
won’t probably use it directly but instead use the from_files and
from_dict methods.

Parameters<span class="colon">:</span>  
- **gap** – The gap after interpolation in eV

- **mu_steps** – The steps of electron chemical potential (or Fermi
  level) in eV.

- **cond** – The electronic conductivity tensor divided by a constant
  relaxation time (sigma/tau) at different temperature and fermi levels.
  The format is {temperature: \[array of 3x3 tensors at each Fermi level
  in mu_steps\]}. The units are 1/(Ohm\*m\*s).

- **seebeck** – The Seebeck tensor at different temperatures and fermi
  levels. The format is {temperature: \[array of 3x3 tensors at each
  Fermi level in mu_steps\]}. The units are V/K

- **kappa** – The electronic thermal conductivity tensor divided by a
  constant relaxation time (kappa/tau) at different temperature and
  fermi levels. The format is {temperature: \[array of 3x3 tensors at
  each Fermi level in mu_steps\]} The units are W/(m\*K\*s)

- **hall** – The hall tensor at different temperature and fermi levels
  The format is {temperature: \[array of 27 coefficients list at each
  Fermi level in mu_steps\]} The units are m^3/C

- **doping** – The different doping levels that have been given to
  BoltzTraP. The format is {‘p’:\[\],’n’:\[\]} with an array of doping
  levels. The units are cm^-3

- **mu_doping** – Gives the electron chemical potential (or Fermi level)
  for a given set of doping. Format is {‘p’:{temperature: \[fermi
  levels\],’n’:{temperature: \[fermi levels\]}} the Fermi level array is
  ordered according to the doping levels in doping units for doping are
  in cm^-3 and for Fermi level in eV

- **seebeck_doping** – The Seebeck tensor at different temperatures and
  doping levels. The format is {‘p’: {temperature: \[Seebeck tensors\]},
  ‘n’:{temperature: \[Seebeck tensors\]}} The \[Seebeck tensors\] array
  is ordered according to the doping levels in doping units for doping
  are in cm^-3 and for Seebeck in V/K

- **cond_doping** – The electronic conductivity tensor divided by a
  constant relaxation time (sigma/tau) at different temperatures and
  doping levels The format is {‘p’:{temperature: \[conductivity
  tensors\]}, ‘n’:{temperature: \[conductivity tensors\]}} The
  \[conductivity tensors\] array is ordered according to the doping
  levels in doping units for doping are in cm^-3 and for conductivity in
  1/(Ohm\*m\*s)

- **kappa_doping** – The thermal conductivity tensor divided by a
  constant relaxation time (kappa/tau) at different temperatures and
  doping levels. The format is {‘p’:{temperature: \[thermal conductivity
  tensors\]},’n’:{temperature: \[thermal conductivity tensors\]}} The
  \[thermal conductivity tensors\] array is ordered according to the
  doping levels in doping units for doping are in cm^-3 and for thermal
  conductivity in W/(m\*K\*s)

- **hall_doping** – The Hall tensor at different temperatures and doping
  levels. The format is {‘p’:{temperature: \[Hall tensors\]},
  ‘n’:{temperature: \[Hall tensors\]}} The \[Hall tensors\] array is
  ordered according to the doping levels in doping and each Hall tensor
  is represented by a 27 coefficients list. The units are m^3/C

- **intrans** – a dictionary of inputs e.g. {“scissor”: 0.0}

- **carrier_conc** – The concentration of carriers in electron (or hole)
  per unit cell

- **dos** – The dos computed by BoltzTraP given as a pymatgen Dos object

- **dos_partial** – Data for the partial DOS projected on sites and
  orbitals

- **vol** – Volume of the unit cell in angstrom cube (A^3)

- **warning** – string if BoltzTraP outputted a warning, else None

- **bz_bands** – Data for interpolated bands on a k-point line
  (run_type=BANDS)

- **bz_kpoints** – k-point in reciprocal coordinates for interpolated
  bands (run_type=BANDS)

- **fermi_surface_data** – energy values in a 3D grid imported from the
  output .cube file.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L1987-L2009"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.as_dict"
class="headerlink" title="Link to this definition"></a>  
MSONable dict.

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">check_acc_bzt_bands</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">sbs_bz</span></span>*, *<span class="n"><span class="pre">sbs_ref</span></span>*, *<span class="n"><span class="pre">warn_thr</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0.03,</span> <span class="pre">0.03)</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L888-L953"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.check_acc_bzt_bands"
class="headerlink" title="Link to this definition"></a>  
Compare sbs_bz BandStructureSymmLine calculated with boltztrap with the
sbs_ref BandStructureSymmLine as reference (from MP for instance),
computing correlation and energy difference for eight bands around the
gap (semiconductors) or Fermi level (metals). warn_thr is a threshold to
get a warning in the accuracy of Boltztap interpolated bands.

Return a dictionary with these keys: - “N”: the index of the band
compared; inside each there are:

> <div>
>
> - “Corr”: correlation coefficient for the 8 compared bands
>
> - “Dist”: energy distance for the 8 compared bands
>
> - “branch_name”: energy distance for that branch
>
> </div>

- “avg_corr”: average of correlation coefficient over the 8 bands

- “avg_dist”: average of energy distance over the 8 bands

- “nb_list”: list of indexes of the 8 compared bands

- “acc_thr”: list of two float corresponding to the two warning
  thresholds in input

- “acc_err”: list of two bools:  
  True if the avg_corr \> warn_thr\[0\], and True if the avg_dist \>
  warn_thr\[1\]

See also compare_sym_bands function doc.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">data</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L2011-L2149"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.from_dict"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
**data** – Dict representation.

Returns<span class="colon">:</span>  
BoltztrapAnalyzer

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_files</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">path_dir</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">dos_spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="p"><span class="pre">-</span></span><span class="m"><span class="pre">1</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="m"><span class="pre">1</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L1941-L1985"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.from_files"
class="headerlink" title="Link to this definition"></a>  
Get a BoltztrapAnalyzer object from a set of files.

Parameters<span class="colon">:</span>  
- **path_dir** – directory where the boltztrap files are

- **dos_spin** – in DOS mode, set to 1 for spin up and -1 for spin down

Returns<span class="colon">:</span>  
BoltztrapAnalyzer

<span class="sig-name descname"><span class="pre">get_average_eff_mass</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">output</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'eigs'</span></span>*, *<span class="n"><span class="pre">doping_levels</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L1220-L1296"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.get_average_eff_mass"
class="headerlink" title="Link to this definition"></a>  
Get the average effective mass tensor. We call it average because it
takes into account all the bands and regions in the Brillouin zone. This
is different than the standard textbook effective mass which relates
often to only one (parabolic) band. The average effective mass tensor is
defined as the integrated average of the second derivative of E(k) This
effective mass tensor takes into account: -non-parabolicity -multiple
extrema -multiple bands.

For more information about it. See:

Hautier, G., Miglio, A., Waroquiers, D., Rignanese, G., & Gonze, X.
(2014). How Does Chemistry Influence Electron Effective Mass in Oxides?
A High-Throughput Computational Analysis. Chemistry of Materials,
26(19), 5447-5458. doi:10.1021/cm404079a

or

Hautier, G., Miglio, A., Ceder, G., Rignanese, G.-M., & Gonze, X.
(2013). Identification and design principles of low hole effective mass
p-type transparent conducting oxides. Nature Communications, 4, 2292.
doi:10.1038/ncomms3292

Depending on the value of output, we have either the full 3x3 effective
mass tensor, its 3 eigenvalues or an average

Parameters<span class="colon">:</span>  
- **output** (*str*) – ‘eigs’ for eigenvalues, ‘tensor’ for the full

- **average** (*tensor and 'average' for an*)

- **doping_levels** (*bool*) – True for the results to be given at

- **levels** (*different doping*)

- **results** (*False for*)

- **potentials** (*at different electron chemical*)

Returns<span class="colon">:</span>  
{temp:\[\]},’n’:{temp:\[\]}} with an array of effective mass tensor,
eigenvalues of average value (depending on output) for each temperature
and for each doping level. The ‘p’ links to hole effective mass tensor
and ‘n’ to electron effective mass tensor.

Return type<span class="colon">:</span>  
If doping_levels=True,a dictionary {‘p’

<span class="sig-name descname"><span class="pre">get_carrier_concentration</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L1641-L1649"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.get_carrier_concentration"
class="headerlink" title="Link to this definition"></a>  
Get the carrier concentration (in cm^-3).

Returns<span class="colon">:</span>  
\[\]} with an array of carrier concentration (in cm^-3) at each
temperature The array relates to each step of electron chemical
potential

Return type<span class="colon">:</span>  
a dictionary {temp

<span class="sig-name descname"><span class="pre">get_complete_dos</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">analyzer_for_second_spin</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L1575-L1629"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.get_complete_dos"
class="headerlink" title="Link to this definition"></a>  
Get a CompleteDos object with the DOS from the interpolated projected
band structure.

Parameters<span class="colon">:</span>  
- **structure** – necessary to identify sites for projection

- **analyzer_for_second_spin** – must be specified to have a CompleteDos
  with both Spin components

Returns<span class="colon">:</span>  
from the interpolated projected band structure

Return type<span class="colon">:</span>  
<a href="#pymatgen.electronic_structure.dos.CompleteDos"
class="reference internal"
title="pymatgen.electronic_structure.dos.CompleteDos">CompleteDos</a>

Example of use in case of spin polarized case:

> <div>
>
> BoltztrapRunner(bs=bs,nelec=10,run_type=”DOS”,spin=1).run(path_dir=’dos_up/’)
> an_up=BoltztrapAnalyzer.from_files(“dos_up/boltztrap/”, dos_spin=1)
>
> BoltztrapRunner(bs=bs,nelec=10,run_type=”DOS”,spin=-1).run(path_dir=’dos_dw/’)
> an_dw=BoltztrapAnalyzer.from_files(“dos_dw/boltztrap/”, dos_spin=-1)
>
> cdos=an_up.get_complete_dos(bs.structure,an_dw)
>
> </div>

<span class="sig-name descname"><span class="pre">get_complexity_factor</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">output</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'average'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'tensor'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'average'</span></span>*, *<span class="n"><span class="pre">temp</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">300</span></span>*, *<span class="n"><span class="pre">doping_levels</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">Lambda</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.5</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L1356-L1419"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.get_complexity_factor"
class="headerlink" title="Link to this definition"></a>  
Fermi surface complexity factor respect to calculated as explained in
Ref. Gibbs, Z. M. et al., Effective mass and fermi surface complexity
factor from ab initio band structure calculations. npj Computational
Materials 3, 8 (2017).

Parameters<span class="colon">:</span>  
- **output** – ‘average’ returns the complexity factor calculated using
  the average of the three diagonal components of the seebeck and
  conductivity tensors. ‘tensor’ returns the complexity factor respect
  to the three diagonal components of seebeck and conductivity tensors.

- **doping_levels** – False means that the complexity factor is
  calculated for every value of the chemical potential True means that
  the complexity factor is calculated for every value of the doping
  levels for both n and p types

- **temp** – temperature of calculated seebeck and conductivity.

- **Lambda** – fitting parameter used to model the scattering (0.5 means
  constant relaxation time).

Returns<span class="colon">:</span>  
a list of values for the complexity factor w.r.t the chemical potential,
if doping_levels is set at False; a dict with n an p keys that contain a
list of values for the complexity factor w.r.t the doping levels, if
doping_levels is set at True; if ‘tensor’ is selected, each element of
the lists is a list containing the three components of the complexity
factor.

<span class="sig-name descname"><span class="pre">get_conductivity</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">output</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'eigs'</span></span>*, *<span class="n"><span class="pre">doping_levels</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">relaxation_time</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1e-14</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L986-L1019"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.get_conductivity"
class="headerlink" title="Link to this definition"></a>  
Get the conductivity (1/Ohm\*m) in either a full 3x3 tensor form, as 3
eigenvalues, or as the average value (trace/3.0) If doping_levels=True,
the results are given at different p and n doping levels (given by
self.doping), otherwise it is given as a series of electron chemical
potential values.

Parameters<span class="colon">:</span>  
- **output** (*str*) – the type of output. ‘tensor’ give the full

- **tensor** (*3x3*)

- **and** (*'eigs' its 3 eigenvalues*)

- **eigenvalues** (*'average' the average* *of* *the three*)

- **doping_levels** (*bool*) – True for the results to be given at

- **levels** (*different doping*)

- **results** (*False for*)

- **potentials** (*at different electron chemical*)

- **relaxation_time** (*float*) – constant relaxation time in secs

Returns<span class="colon">:</span>  
{‘p’:\[\],’n’:\[\]}}. The ‘p’ links to conductivity at p-type doping and
‘n’ to the conductivity at n-type doping. Otherwise, returns a
{temp:\[\]} dictionary. The result contains either the sorted three
eigenvalues of the symmetric conductivity tensor (format=’eigs’) or a
full tensor (3x3 array) (output=’tensor’) or as an average
(output=’average’). The result includes a given constant relaxation time

units are 1/Ohm\*m

Return type<span class="colon">:</span>  
If doping_levels=True, a dictionary {temp

<span class="sig-name descname"><span class="pre">get_extreme</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">target_prop</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'seebeck'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'power</span> <span class="pre">factor'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'conductivity'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'kappa'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'zt'</span></span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">maximize</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">min_temp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">max_temp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">min_doping</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">max_doping</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">isotropy_tolerance</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.05</span></span>*, *<span class="n"><span class="pre">use_average</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'p'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'n'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'best'</span></span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L1421-L1530"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.get_extreme"
class="headerlink" title="Link to this definition"></a>  
Use eigenvalues over a range of carriers, temperatures, and doping
levels, to estimate the “best” value that can be achieved for the given
target_property. Note that this method searches the doping dict only,
not the full mu dict.

Parameters<span class="colon">:</span>  
- **target_prop** (*"seebeck",* *"power factor",* *"conductivity",*
  *"kappa",* *"zt"*) – target property.

- **maximize** (*bool*) – True to maximize, False to minimize (e.g.
  kappa)

- **min_temp** (*float*) – minimum temperature allowed

- **max_temp** (*float*) – maximum temperature allowed

- **min_doping** (*float*) – minimum doping allowed (e.g., 1E18)

- **max_doping** (*float*) – maximum doping allowed (e.g., 1E20)

- **isotropy_tolerance** (*float*) – tolerance for isotropic (0.05 = 5%)

- **use_average** (*bool*) – True for average of eigenval, False for max
  eigenval.

Returns<span class="colon">:</span>  
{“p”, “n”, “best”}. Each key maps to a sub-dictionary with the following
keys:

> <div>
>
> {“value”, “temperature”, “doping”, “isotropic”, “carrier_type”}.
>
> </div>

Return type<span class="colon">:</span>  
A dictionary with the following keys

<span class="sig-name descname"><span class="pre">get_hall_carrier_concentration</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L1651-L1669"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.get_hall_carrier_concentration"
class="headerlink" title="Link to this definition"></a>  
Get the Hall carrier concentration (in cm^-3). This is the trace of the
Hall tensor (see BoltzTraP source code) Hall carrier concentration are
not always exactly the same than carrier concentration.

Returns<span class="colon">:</span>  
\[\]} with an array of Hall carrier concentration (in cm^-3) at each
temperature The array relates to each step of electron chemical
potential

Return type<span class="colon">:</span>  
a dictionary {temp

<span class="sig-name descname"><span class="pre">get_mu_bounds</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">temp</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">300</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L1631-L1639"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.get_mu_bounds"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
**temp** – Temperature.

Returns<span class="colon">:</span>  
The chemical potential bounds at that temperature.

<span class="sig-name descname"><span class="pre">get_power_factor</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">output</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'eigs'</span></span>*, *<span class="n"><span class="pre">doping_levels</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">relaxation_time</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1e-14</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L1021-L1081"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.get_power_factor"
class="headerlink" title="Link to this definition"></a>  
Get the power factor (Seebeck^2 \* conductivity) in units
microW/(m\*K^2) in either a full 3x3 tensor form, as 3 eigenvalues, or
as the average value (trace/3.0) If doping_levels=True, the results are
given at different p and n doping levels (given by self.doping),
otherwise it is given as a series of electron chemical potential values.

Parameters<span class="colon">:</span>  
- **output** (*str*) – the type of output. ‘tensor’ give the full 3x3

- **tensor**

- **and** (*'eigs' its 3 eigenvalues*)

- **eigenvalues** (*'average' the average* *of* *the three*)

- **doping_levels** (*bool*) – True for the results to be given at

- **levels** (*different doping*)

- **results** (*False for*)

- **potentials** (*at different electron chemical*)

- **relaxation_time** (*float*) – constant relaxation time in secs

Returns<span class="colon">:</span>  
{‘p’:\[\],’n’:\[\]}}. The ‘p’ links to power factor at p-type doping and
‘n’ to the conductivity at n-type doping. Otherwise, returns a
{temp:\[\]} dictionary. The result contains either the sorted three
eigenvalues of the symmetric power factor tensor (format=’eigs’) or a
full tensor (3x3 array) ( output=’tensor’) or as an average
(output=’average’). The result includes a given constant relaxation time

units are microW/(m K^2)

Return type<span class="colon">:</span>  
If doping_levels=True, a dictionary {temp

<span class="sig-name descname"><span class="pre">get_seebeck</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">output</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'eigs'</span></span>*, *<span class="n"><span class="pre">doping_levels</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L955-L984"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.get_seebeck"
class="headerlink" title="Link to this definition"></a>  
Get the seebeck coefficient (microV/K) in either a full 3x3 tensor form,
as 3 eigenvalues, or as the average value (trace/3.0) If
doping_levels=True, the results are given at different p and n doping
levels (given by self.doping), otherwise it is given as a series of
electron chemical potential values.

Parameters<span class="colon">:</span>  
- **output** (*str*) – the type of output. ‘tensor’ give the full

- **tensor** (*3x3*)

- **and** (*'eigs' its 3 eigenvalues*)

- **eigenvalues** (*'average' the average* *of* *the three*)

- **doping_levels** (*bool*) – True for the results to be given at

- **levels** (*different doping*)

- **results** (*False for*)

- **potentials** (*at different electron chemical*)

Returns<span class="colon">:</span>  
{‘p’:\[\],’n’:\[\]}}. The ‘p’ links to Seebeck at p-type doping and ‘n’
to the Seebeck at n-type doping. Otherwise, returns a {temp:\[\]}
dictionary The result contains either the sorted three eigenvalues of
the symmetric Seebeck tensor (output=’eigs’) or a full tensor (3x3
array) ( output=’tensor’) or as an average (output=’average’).

units are microV/K

Return type<span class="colon">:</span>  
If doping_levels=True, a dictionary {temp

<span class="sig-name descname"><span class="pre">get_seebeck_eff_mass</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">output</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'average'</span></span>*, *<span class="n"><span class="pre">temp</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">300</span></span>*, *<span class="n"><span class="pre">doping_levels</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">Lambda</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.5</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L1298-L1354"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.get_seebeck_eff_mass"
class="headerlink" title="Link to this definition"></a>  
Seebeck effective mass calculated as explained in Ref. Gibbs, Z. M. et
al., Effective mass and fermi surface complexity factor from ab initio
band structure calculations. npj Computational Materials 3, 8 (2017).

Parameters<span class="colon">:</span>  
- **output** – ‘average’ returns the seebeck effective mass calculated
  using the average of the three diagonal components of the seebeck
  tensor. ‘tensor’ returns the seebeck effective mass respect to the
  three diagonal components of the seebeck tensor.

- **doping_levels** – False means that the seebeck effective mass is
  calculated for every value of the chemical potential True means that
  the seebeck effective mass is calculated for every value of the doping
  levels for both n and p types

- **temp** – temperature of calculated seebeck.

- **Lambda** – fitting parameter used to model the scattering (0.5 means
  constant relaxation time).

Returns<span class="colon">:</span>  
a list of values for the seebeck effective mass w.r.t the chemical
potential, if doping_levels is set at False; a dict with n an p keys
that contain a list of values for the seebeck effective mass w.r.t the
doping levels, if doping_levels is set at True; if ‘tensor’ is selected,
each element of the lists is a list containing the three components of
the seebeck effective mass.

<span class="sig-name descname"><span class="pre">get_symm_bands</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">efermi</span></span>*, *<span class="n"><span class="pre">kpt_line</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">labels_dict</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L834-L886"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.get_symm_bands"
class="headerlink" title="Link to this definition"></a>  
Useful to read bands from BoltzTraP output and get a
BandStructureSymmLine object comparable with that one from a DFT
calculation (if the same kpt_line is provided). Default kpt_line and
labels_dict is the standard path of high symmetry k-point for the
specified structure. They could be extracted from the
BandStructureSymmLine object that you want to compare with. efermi
variable must be specified to create the BandStructureSymmLine object
(usually it comes from DFT or BoltzTraP calc).

<span class="sig-name descname"><span class="pre">get_thermal_conductivity</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">output</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'eigs'</span></span>*, *<span class="n"><span class="pre">doping_levels</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">k_el</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">relaxation_time</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1e-14</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L1083-L1146"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.get_thermal_conductivity"
class="headerlink" title="Link to this definition"></a>  
Get the electronic part of the thermal conductivity in either a full 3x3
tensor form, as 3 eigenvalues, or as the average value (trace/3.0) If
doping_levels=True, the results are given at different p and n doping
levels (given by self.doping), otherwise it is given as a series of
electron chemical potential values.

Parameters<span class="colon">:</span>  
- **output** (*str*) – the type of output. ‘tensor’ give the full 3x3

- **tensor**

- **and** (*'eigs' its 3 eigenvalues*)

- **eigenvalues** (*'average' the average* *of* *the three*)

- **doping_levels** (*bool*) – True for the results to be given at

- **levels** (*different doping*)

- **results** (*False for*)

- **potentials** (*at different electron chemical*)

- **k_el** (*bool*) – True for k_0-PF\*T, False for k_0

- **relaxation_time** (*float*) – constant relaxation time in secs

Returns<span class="colon">:</span>  
{‘p’:\[\],’n’:\[\]}}. The ‘p’ links to thermal conductivity at p-type
doping and ‘n’ to the thermal conductivity at n-type doping. Otherwise,
returns a {temp:\[\]} dictionary. The result contains either the sorted
three eigenvalues of the symmetric conductivity tensor (format=’eigs’)
or a full tensor (3x3 array) ( output=’tensor’) or as an average
(output=’average’). The result includes a given constant relaxation time

units are W/mK

Return type<span class="colon">:</span>  
If doping_levels=True, a dictionary {temp

<span class="sig-name descname"><span class="pre">get_zt</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">output</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'eigs'</span></span>*, *<span class="n"><span class="pre">doping_levels</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">relaxation_time</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1e-14</span></span>*, *<span class="n"><span class="pre">k_l</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L1148-L1218"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.get_zt"
class="headerlink" title="Link to this definition"></a>  
Get the ZT coefficient (S^2\*cond\*T/thermal cond) in either a full 3x3
tensor form, as 3 eigenvalues, or as the average value (trace/3.0) If
doping_levels=True, the results are given at different p and n doping
levels (given by self.doping), otherwise it is given as a series of
electron chemical potential values. We assume a constant relaxation time
and a constant lattice thermal conductivity.

Parameters<span class="colon">:</span>  
- **output** (*str*) – the type of output. ‘tensor’ give the full 3x3

- **tensor**

- **and** (*'eigs' its 3 eigenvalues*)

- **eigenvalues** (*'average' the average* *of* *the three*)

- **doping_levels** (*bool*) – True for the results to be given at

- **levels** (*different doping*)

- **results** (*False for*)

- **potentials** (*at different electron chemical*)

- **relaxation_time** (*float*) – constant relaxation time in secs

- **k_l** (*float*) – lattice thermal cond in W/(m\*K)

Returns<span class="colon">:</span>  
{‘p’:\[\],’n’:\[\]}}. The ‘p’ links to ZT at p-type doping and ‘n’ to
the ZT at n-type doping. Otherwise, returns a {temp:\[\]} dictionary.
The result contains either the sorted three eigenvalues of the symmetric
ZT tensor (format=’eigs’) or a full tensor (3x3 array) (
output=’tensor’) or as an average (output=’average’). The result
includes a given constant relaxation time and lattice thermal
conductivity

Return type<span class="colon">:</span>  
If doping_levels=True, a dictionary {temp

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">parse_cond_and_hall</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">path_dir</span></span>*, *<span class="n"><span class="pre">doping_levels</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L1810-L1939"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.parse_cond_and_hall"
class="headerlink" title="Link to this definition"></a>  
Parse the conductivity and Hall tensors.

Parameters<span class="colon">:</span>  
- **path_dir** – Path containing .condtens / .halltens files

- **doping_levels** – (\[float\]) - doping lvls, parse outtrans to get
  this.

Returns<span class="colon">:</span>  
mu_steps, cond, seebeck, kappa, hall, pn_doping_levels, mu_doping,
seebeck_doping, cond_doping, kappa_doping, hall_doping, carrier_conc

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">parse_intrans</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">path_dir</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L1774-L1792"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.parse_intrans"
class="headerlink" title="Link to this definition"></a>  
Parse boltztrap.intrans mainly to extract the value of scissor applied
to the bands or some other inputs.

Parameters<span class="colon">:</span>  
**path_dir** – (str) dir containing the boltztrap.intrans file

Returns<span class="colon">:</span>  
various inputs that had been used in the BoltzTraP run.

Return type<span class="colon">:</span>  
dict

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">parse_outputtrans</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">path_dir</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L1671-L1697"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.parse_outputtrans"
class="headerlink" title="Link to this definition"></a>  
Parse .outputtrans file.

Parameters<span class="colon">:</span>  
**path_dir** – dir containing boltztrap.outputtrans

Returns<span class="colon">:</span>  
tuple - (run_type, warning, efermi, gap, doping_levels)

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">parse_struct</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">path_dir</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L1794-L1808"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.parse_struct"
class="headerlink" title="Link to this definition"></a>  
Parse boltztrap.struct file (only the volume).

Parameters<span class="colon">:</span>  
**path_dir** – (str) dir containing the boltztrap.struct file

Returns<span class="colon">:</span>  
volume of the structure in Angstrom^3

Return type<span class="colon">:</span>  
float

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">parse_transdos</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">path_dir</span></span>*, *<span class="n"><span class="pre">efermi</span></span>*, *<span class="n"><span class="pre">dos_spin</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1</span></span>*, *<span class="n"><span class="pre">trim_dos</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L1699-L1772"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapAnalyzer.parse_transdos"
class="headerlink" title="Link to this definition"></a>  
Parse .transdos (total DOS) and .transdos_x\_y (partial DOS) files.

Parameters<span class="colon">:</span>  
- **path_dir** – (str) dir containing DOS files

- **efermi** – (float) Fermi energy

- **dos_spin** – (int) -1 for spin down, +1 for spin up

- **trim_dos** – (bool) whether to post-process / trim DOS.

Returns<span class="colon">:</span>  
tuple - (DOS, dict of partial DOS)

<!-- -->

*<span class="k"><span class="pre">exception</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">BoltztrapError</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L699-L702"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.boltztrap.BoltztrapError"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`Exception`</span>

Exception class for boltztrap. Raised when the boltztrap gives an error.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">BoltztrapRunner</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">bs</span></span>*, *<span class="n"><span class="pre">nelec</span></span>*, *<span class="n"><span class="pre">dos_type</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'HISTO'</span></span>*, *<span class="n"><span class="pre">energy_grid</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.005</span></span>*, *<span class="n"><span class="pre">lpfac</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">10</span></span>*, *<span class="n"><span class="pre">run_type</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'BOLTZ'</span></span>*, *<span class="n"><span class="pre">band_nb</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">tauref</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">tauexp</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">tauen</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">soc</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">doping</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">energy_span_around_fermi</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1.5</span></span>*, *<span class="n"><span class="pre">scissor</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.0</span></span>*, *<span class="n"><span class="pre">kpt_line</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">spin</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">cond_band</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">tmax</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1300</span></span>*, *<span class="n"><span class="pre">tgrid</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">50</span></span>*, *<span class="n"><span class="pre">symprec</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.001</span></span>*, *<span class="n"><span class="pre">cb_cut</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">10</span></span>*, *<span class="n"><span class="pre">timeout</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">7200</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L65-L696"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.boltztrap.BoltztrapRunner"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

This class is used to run BoltzTraP on a band structure object.

Parameters<span class="colon">:</span>  
- **bs** – A band structure object

- **nelec** – the number of electrons

- **dos_type** – two options for the band structure integration: “HISTO”
  (histogram) or “TETRA” using the tetrahedon method. TETRA typically
  gives better results (especially for DOSes) but takes more time

- **energy_grid** – the energy steps used for the integration (eV)

- **lpfac** – the number of interpolation points in the real space. By
  default 10 gives 10 time more points in the real space than the number
  of kpoints given in reciprocal space

- **run_type** – type of boltztrap usage. by default - BOLTZ: (default)
  compute transport coefficients - BANDS: interpolate all bands
  contained in the energy range specified in energy_span_around_fermi
  variable, along specified k-points - DOS: compute total and partial
  dos (custom BoltzTraP code needed!) - FERMI: compute fermi surface or
  more correctly to get certain bands interpolated

- **band_nb** – indicates a band number. Used for Fermi Surface
  interpolation (run_type=”FERMI”)

- **spin** – specific spin component (1: up, -1: down) of the band
  selected in FERMI mode (mandatory).

- **cond_band** – if a conduction band is specified in FERMI mode, set
  this variable as True

- **tauref** – reference relaxation time. Only set to a value different
  than zero if we want to model beyond the constant relaxation time.

- **tauexp** – exponent for the energy in the non-constant relaxation
  time approach

- **tauen** – reference energy for the non-constant relaxation time
  approach

- **soc** – results from spin-orbit coupling (soc) computations give
  typically non-polarized (no spin up or down) results but single
  electron occupations. If the band structure comes from a soc
  computation, you should set soc to True (default False)

- **doping** – the fixed doping levels you want to compute. BoltzTraP
  provides both transport values depending on electron chemical
  potential (fermi energy) and for a series of fixed carrier
  concentrations. By default, this is set to 1e16 to 1e22 in increments
  of factors of 10.

- **energy_span_around_fermi** – usually the interpolation is not needed
  on the entire energy range but on a specific range around the Fermi
  level. This energy gives this range in eV. by default it is 1.5 eV. If
  DOS or BANDS type are selected, this range is automatically set to
  cover the entire energy range.

- **scissor** – scissor to apply to the band gap (eV). This applies a
  scissor operation moving the band edges without changing the band
  shape. This is useful to correct the often underestimated band gap in
  DFT. Default is 0.0 (no scissor)

- **kpt_line** – list of fractional coordinates of kpoints as arrays or
  list of Kpoint objects for BANDS mode calculation (standard path of
  high symmetry k-points is automatically set as default)

- **tmax** – Maximum temperature (K) for calculation (default=1300)

- **tgrid** – Temperature interval for calculation (default=50)

- **symprec** – 1e-3 is the default in pymatgen. If the kmesh has been
  generated using a different symprec, it has to be specified to avoid a
  “factorization error” in BoltzTraP calculation. If a kmesh that spans
  the whole Brillouin zone has been used, or to disable all the
  symmetries, set symprec to None.

- **cb_cut** – by default 10% of the highest conduction bands are
  removed because they are often not accurate. Tune cb_cut to change the
  percentage (0-100) of bands that are removed.

- **timeout** – overall time limit (in seconds): mainly to avoid
  infinite loop when trying to find Fermi levels.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L671-L696"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapRunner.as_dict"
class="headerlink" title="Link to this definition"></a>  
MSONable dict.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">bs</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/boltztrap.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.boltztrap.BoltztrapRunner.bs"
class="headerlink" title="Link to this definition"></a>  
The BandStructure.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">nelec</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/boltztrap.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.boltztrap.BoltztrapRunner.nelec"
class="headerlink" title="Link to this definition"></a>  
Number of electrons.

<span class="sig-name descname"><span class="pre">run</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">path_dir</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">convergence</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">write_input</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">clear_dir</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">max_lpfac</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">150</span></span>*, *<span class="n"><span class="pre">min_egrid</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">5e-05</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L521-L669"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.boltztrap.BoltztrapRunner.run"
class="headerlink" title="Link to this definition"></a>  
Write inputs (optional), run BoltzTraP, and ensure convergence
(optional).

Parameters<span class="colon">:</span>  
- **path_dir** (*str*) – directory in which to run BoltzTraP

- **convergence** (*bool*) – whether to check convergence and make
  corrections if needed

- **write_input** – (bool) whether to write input files before the run
  (required for convergence mode)

- **clear_dir** – (bool) whether to remove all files in the path_dir
  before starting

- **max_lpfac** – (float) maximum lpfac value to try before reducing
  egrid in convergence mode

- **min_egrid** – (float) minimum egrid value to try before giving up in
  convergence mode

<span class="sig-name descname"><span class="pre">write_def</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">output_file</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L338-L365"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapRunner.write_def"
class="headerlink" title="Link to this definition"></a>  
Write the def to an output file.

Parameters<span class="colon">:</span>  
**output_file** – Filename

<span class="sig-name descname"><span class="pre">write_energy</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">output_file</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L257-L306"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapRunner.write_energy"
class="headerlink" title="Link to this definition"></a>  
Write the energy to an output file.

Parameters<span class="colon">:</span>  
**output_file** – Filename

<span class="sig-name descname"><span class="pre">write_input</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">output_dir</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L500-L519"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapRunner.write_input"
class="headerlink" title="Link to this definition"></a>  
Write the input files.

Parameters<span class="colon">:</span>  
**output_dir** – Directory to write the input files.

<span class="sig-name descname"><span class="pre">write_intrans</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">output_file</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L425-L498"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapRunner.write_intrans"
class="headerlink" title="Link to this definition"></a>  
Write the intrans to an output file.

Parameters<span class="colon">:</span>  
**output_file** – Filename

<span class="sig-name descname"><span class="pre">write_proj</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">output_file_proj</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">output_file_def</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L367-L423"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapRunner.write_proj"
class="headerlink" title="Link to this definition"></a>  
Write the projections to an output file.

Parameters<span class="colon">:</span>  
- **output_file_proj** – output file name

- **output_file_def** – output file name

<span class="sig-name descname"><span class="pre">write_struct</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">output_file</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L308-L336"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.BoltztrapRunner.write_struct"
class="headerlink" title="Link to this definition"></a>  
Write the structure to an output file.

Parameters<span class="colon">:</span>  
**output_file** – Filename

<!-- -->

<span class="sig-name descname"><span class="pre">compare_sym_bands</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">bands_obj</span></span>*, *<span class="n"><span class="pre">bands_ref_obj</span></span>*, *<span class="n"><span class="pre">nb</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L2199-L2259"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.boltztrap.compare_sym_bands"
class="headerlink" title="Link to this definition"></a>  
Compute the mean of correlation between bzt and vasp bandstructure on
sym line, for all bands and locally (for each branches) the difference
squared (%) if nb is specified.

<!-- -->

<span class="sig-name descname"><span class="pre">eta_from_seebeck</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">seeb</span></span>*, *<span class="n"><span class="pre">Lambda</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L2279-L2286"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.boltztrap.eta_from_seebeck"
class="headerlink" title="Link to this definition"></a>  
It takes a value of seebeck and adjusts the analytic seebeck until it’s
equal.

Returns<span class="colon">:</span>  
eta where the two seebeck coefficients are equal (reduced chemical
potential).

Return type<span class="colon">:</span>  
float

<!-- -->

<span class="sig-name descname"><span class="pre">read_cube_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L2152-L2196"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.boltztrap.read_cube_file"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
**filename** – Cube filename.

Returns<span class="colon">:</span>  
Energy data.

<!-- -->

<span class="sig-name descname"><span class="pre">seebeck_eff_mass_from_carr</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">eta</span></span>*, *<span class="n"><span class="pre">n</span></span>*, *<span class="n"><span class="pre">T</span></span>*, *<span class="n"><span class="pre">Lambda</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L2289-L2302"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.seebeck_eff_mass_from_carr"
class="headerlink" title="Link to this definition"></a>  
Calculate seebeck effective mass at a certain carrier concentration eta
in kB\*T units, n in cm-3, T in K, returns mass in m0 units.

<!-- -->

<span class="sig-name descname"><span class="pre">seebeck_eff_mass_from_seebeck_carr</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">seeb</span></span>*, *<span class="n"><span class="pre">n</span></span>*, *<span class="n"><span class="pre">T</span></span>*, *<span class="n"><span class="pre">Lambda</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L2305-L2311"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.boltztrap.seebeck_eff_mass_from_seebeck_carr"
class="headerlink" title="Link to this definition"></a>  
Find the chemical potential where analytic and calculated seebeck are
identical and then calculate the seebeck effective mass at that chemical
potential and a certain carrier concentration n.

<!-- -->

<span class="sig-name descname"><span class="pre">seebeck_spb</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">eta</span></span>*, *<span class="n"><span class="pre">Lambda</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.5</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/boltztrap.py#L2262-L2276"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.boltztrap.seebeck_spb"
class="headerlink" title="Link to this definition"></a>  
Seebeck analytic formula in the single parabolic model.

</div>

<div id="pymatgen-electronic-structure-boltztrap2-module"
class="section">

## pymatgen.electronic_structure.boltztrap2 module<a href="#pymatgen-electronic-structure-boltztrap2-module"
class="headerlink" title="Link to this heading"></a>

</div>

<div id="module-pymatgen.electronic_structure.cohp" class="section">

<span id="pymatgen-electronic-structure-cohp-module"></span>

## pymatgen.electronic_structure.cohp module<a href="#module-pymatgen.electronic_structure.cohp" class="headerlink"
title="Link to this heading"></a>

This module defines classes to represent:  
- Crystal orbital Hamilton population (COHP) and integrated COHP
  (ICOHP).

- Crystal orbital overlap population (COOP).

- Crystal orbital bond index (COBI).

If you use this module, please cite: J. George, G. Petretto, A. Naik, M.
Esters, A. J. Jackson, R. Nelson, R. Dronskowski, G.-M. Rignanese, G.
Hautier, “Automated Bonding Analysis with Crystal Orbital Hamilton
Populations”, ChemPlusChem 2022, e202200123, DOI:
10.1002/cplu.202200123.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Cohp</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">efermi</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">energies</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">cohp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Mapping</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">NDArray</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">are_coops</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">are_cobis</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">are_multi_center_cobis</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">icohp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Mapping</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">NDArray</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/cohp.py#L55-L229"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.Cohp" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Basic COHP object.

Parameters<span class="colon">:</span>  
- **efermi** (*float*) – The Fermi level.

- **energies** (*Sequence\[float\]*) – Energies.

- **({Spin** (*icohp*) – NDArrary}): The COHP for each spin.

- **are_coops** (*bool*) – Whether this object describes COOPs.

- **are_cobis** (*bool*) – Whether this object describes COBIs.

- **are_multi_center_cobis** (*bool*) – Whether this object describes
  multi-center COBIs.

- **({Spin** – NDArrary}): The ICOHP for each spin.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/cohp.py#L112-L126"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.Cohp.as_dict"
class="headerlink" title="Link to this definition"></a>  
JSON-serializable dict representation of COHP.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/cohp.py#L216-L229"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.Cohp.from_dict"
class="headerlink" title="Link to this definition"></a>  
Generate Cohp from a dict representation.

<span class="sig-name descname"><span class="pre">get_cohp</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">SpinLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">integrated</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">NDArray</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/cohp.py#L128-L153"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.Cohp.get_cohp"
class="headerlink" title="Link to this definition"></a>  
Get the COHP or ICOHP for a particular spin.

Parameters<span class="colon">:</span>  
- **spin** (*SpinLike*) – Selected spin. If is None and both spins are
  present, both will be returned.

- **integrated** – Return ICOHP (True) or COHP (False).

Returns<span class="colon">:</span>  
The COHP or ICOHP for the selected spin.

Return type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">get_icohp</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">SpinLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">NDArray</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/cohp.py#L155-L160"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.Cohp.get_icohp"
class="headerlink" title="Link to this definition"></a>  
Convenient wrapper to get the ICOHP for a particular spin.

<span class="sig-name descname"><span class="pre">get_interpolated_value</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">energy</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">integrated</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/cohp.py#L162-L181"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.cohp.Cohp.get_interpolated_value"
class="headerlink" title="Link to this definition"></a>  
Get the interpolated COHP for a particular energy.

Parameters<span class="colon">:</span>  
- **energy** (*float*) – Energy to get the COHP value for.

- **integrated** (*bool*) – Return ICOHP (True) or COHP (False).

<span class="sig-name descname"><span class="pre">has_antibnd_states_below_efermi</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">SpinLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">limit</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.01</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">bool</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/cohp.py#L183-L214"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.cohp.Cohp.has_antibnd_states_below_efermi"
class="headerlink" title="Link to this definition"></a>  
Get dict of antibonding states below the Fermi level for the spin.

Parameters<span class="colon">:</span>  
- **spin** (*SpinLike*) – Selected spin.

- **limit** (*float*) – Only COHP higher than this value will be
  considered.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">CompleteCohp</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">avg_cohp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.cohp.Cohp"
class="reference internal"
title="pymatgen.electronic_structure.cohp.Cohp"><span
class="pre">Cohp</span></a></span>*, *<span class="n"><span class="pre">cohp_dict</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><a href="#pymatgen.electronic_structure.cohp.Cohp"
class="reference internal"
title="pymatgen.electronic_structure.cohp.Cohp"><span
class="pre">Cohp</span></a><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">bonds</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">are_coops</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">are_cobis</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">are_multi_center_cobis</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">orb_res_cohp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/cohp.py#L232-L926"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.CompleteCohp"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.electronic_structure.cohp.Cohp"
class="reference internal"
title="pymatgen.electronic_structure.cohp.Cohp"><span class="pre"><code
class="sourceCode python">Cohp</code></span></a>

A wrapper that defines an average COHP, and individual COHPs.

<span class="sig-name descname"><span class="pre">are_coops</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.CompleteCohp.are_coops"
class="headerlink" title="Link to this definition"></a>  
Whether the object consists of COOPs.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">are_cobis</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.CompleteCohp.are_cobis"
class="headerlink" title="Link to this definition"></a>  
Whether the object consists of COBIs.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">efermi</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.CompleteCohp.efermi"
class="headerlink" title="Link to this definition"></a>  
The Fermi level.

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">energies</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.CompleteCohp.energies"
class="headerlink" title="Link to this definition"></a>  
Sequence of energies.

Type<span class="colon">:</span>  
Sequence\[float\]

<span class="sig-name descname"><span class="pre">structure</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.CompleteCohp.structure"
class="headerlink" title="Link to this definition"></a>  
Structure associated with the COHPs.

Type<span class="colon">:</span>  
<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure">Structure</a>

<span class="sig-name descname"><span class="pre">cohp</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.CompleteCohp.cohp"
class="headerlink" title="Link to this definition"></a>  
The average COHP.

Type<span class="colon">:</span>  
Sequence\[float\]

<span class="sig-name descname"><span class="pre">icohp</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.CompleteCohp.icohp"
class="headerlink" title="Link to this definition"></a>  
The average ICOHP.

Type<span class="colon">:</span>  
Sequence\[float\]

<span class="sig-name descname"><span class="pre">all_cohps</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.CompleteCohp.all_cohps"
class="headerlink" title="Link to this definition"></a>  
COHPs for individual bonds of the form {label: COHP}.

Type<span class="colon">:</span>  
dict\[str, Sequence\[float\]\]

<span class="sig-name descname"><span class="pre">orb_res_cohp</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.CompleteCohp.orb_res_cohp"
class="headerlink" title="Link to this definition"></a>  
Orbital-resolved COHPs.

Type<span class="colon">:</span>  
dict\[str, Dict\[str, Sequence\[float\]\]\]

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  Structure associated with this COHP.

- **avg_cohp** (<a href="#pymatgen.electronic_structure.cohp.Cohp"
  class="reference internal"
  title="pymatgen.electronic_structure.cohp.Cohp"><em>Cohp</em></a>) –
  The average COHP.

- **cohp_dict** (*dict\[str,*
  <a href="#pymatgen.electronic_structure.cohp.Cohp"
  class="reference internal"
  title="pymatgen.electronic_structure.cohp.Cohp"><em>Cohp</em></a>*\]*)
  – COHP for individual bonds of the form {label: COHP}.

- **bonds** (*dict\[str,* *Any\]*) – Information on the bonds of the
  form {label: {key: val}}. The value can be any information, but
  typically contains the sites, the bond length, and the number of
  bonds. If nothing is supplied, it will default to an empty dict.

- **are_coops** (*bool*) – Whether the Cohp objects are COOPs. Defaults
  to False for COHPs.

- **are_cobis** (*bool*) – Whether the Cohp objects are COBIs. Defaults
  to False for COHPs.

- **are_multi_center_cobis** (*bool*) – Whether the Cohp objects are
  multi-center COBIs. Defaults to False for COHPs.

- **orb_res_cohp** (*dict*) – Orbital-resolved COHPs.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/cohp.py#L311-L363"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.CompleteCohp.as_dict"
class="headerlink" title="Link to this definition"></a>  
JSON-serializable dict representation of CompleteCohp.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/cohp.py#L612-L728"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.CompleteCohp.from_dict"
class="headerlink" title="Link to this definition"></a>  
Get CompleteCohp object from a dict representation.

TODO: Clean this up.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">fmt</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'LMTO'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'LOBSTER'</span></span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">structure_file</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">are_coops</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">are_cobis</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">are_multi_center_cobis</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/cohp.py#L730-L926"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.CompleteCohp.from_file"
class="headerlink" title="Link to this definition"></a>  
Create CompleteCohp from an output file of a COHP calculation.

Parameters<span class="colon">:</span>  
- **fmt** (*Literal\["LMTO",* *"LOBSTER"\]*) – The code used to
  calculate COHPs.

- **filename** (*PathLike*) – The COHP output file. Defaults to “COPL”
  for LMTO and “COHPCAR.lobster/COOPCAR.lobster” for LOBSTER.

- **structure_file** (*PathLike*) – The file containing the structure.
  If None, use “CTRL” for LMTO and “POSCAR” for LOBSTER.

- **are_coops** (*bool*) – Whether the populations are COOPs or COHPs.
  Defaults to False for COHPs.

- **are_cobis** (*bool*) – Whether the populations are COBIs or COHPs.
  Defaults to False for COHPs.

- **are_multi_center_cobis** (*bool*) – Whether this file includes
  information on multi-center COBIs.

Returns<span class="colon">:</span>  
A CompleteCohp object.

<span class="sig-name descname"><span class="pre">get_cohp_by_label</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">summed_spin_channels</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.electronic_structure.cohp.Cohp"
class="reference internal"
title="pymatgen.electronic_structure.cohp.Cohp"><span
class="pre">Cohp</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/cohp.py#L365-L409"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.cohp.CompleteCohp.get_cohp_by_label"
class="headerlink" title="Link to this definition"></a>  
Get specific Cohp by the label, to simplify plotting.

Parameters<span class="colon">:</span>  
- **label** (*str*) – Label for the interaction.

- **summed_spin_channels** (*bool*) – Sum the spin channels and return
  the sum as Spin.up.

Returns<span class="colon">:</span>  
The Cohp.

<span class="sig-name descname"><span class="pre">get_orbital_resolved_cohp</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">orbitals</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><a href="#pymatgen.electronic_structure.core.Orbital"
class="reference internal"
title="pymatgen.electronic_structure.core.Orbital"><span
class="pre">Orbital</span></a><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><a href="#pymatgen.electronic_structure.core.Orbital"
class="reference internal"
title="pymatgen.electronic_structure.core.Orbital"><span
class="pre">Orbital</span></a><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="p"><span class="pre">...</span></span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">summed_spin_channels</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.electronic_structure.cohp.Cohp"
class="reference internal"
title="pymatgen.electronic_structure.cohp.Cohp"><span
class="pre">Cohp</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/cohp.py#L539-L610"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.cohp.CompleteCohp.get_orbital_resolved_cohp"
class="headerlink" title="Link to this definition"></a>  
Get orbital-resolved COHP.

Parameters<span class="colon">:</span>  
- **label** (*str*) – Bond labels as in ICOHPLIST/ICOOPLIST.lobster.

- **orbitals** – The orbitals as a label, or list/tuple of \[(n1,
  orbital1), (n2, orbital2), …\]. Where each orbital can either be str,
  int, or Orbital.

- **summed_spin_channels** (*bool*) – Sum the spin channels and return
  the sum as Spin.up.

Returns<span class="colon">:</span>  
A Cohp object if CompleteCohp contains orbital-resolved COHP,  
or None if it doesn’t.

Note: It currently assumes that orbitals are str if they aren’t the  
other valid types. This is not ideal, but is the easiest way to avoid
unicode issues between Python 2 and Python 3.

<span class="sig-name descname"><span class="pre">get_summed_cohp_by_label_and_orbital_list</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">label_list</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">orbital_list</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">divisor</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1</span></span>*, *<span class="n"><span class="pre">summed_spin_channels</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.electronic_structure.cohp.Cohp"
class="reference internal"
title="pymatgen.electronic_structure.cohp.Cohp"><span
class="pre">Cohp</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/cohp.py#L471-L537"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.cohp.CompleteCohp.get_summed_cohp_by_label_and_orbital_list"
class="headerlink" title="Link to this definition"></a>  
Get a Cohp object that includes a summed COHP divided by divisor.

Parameters<span class="colon">:</span>  
- **label_list** (*list\[str\]*) – Labels for the COHP that should be
  included.

- **orbital_list** (*list\[str\]*) – Orbitals for the COHPs that should
  be included (same order as label_list).

- **divisor** (*float*) – The summed COHP will be divided by this
  divisor.

- **summed_spin_channels** (*bool*) – Sum the spin channels and return
  the sum in Spin.up.

Returns<span class="colon">:</span>  
A Cohp object including the summed COHP.

<span class="sig-name descname"><span class="pre">get_summed_cohp_by_label_list</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">label_list</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">divisor</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1</span></span>*, *<span class="n"><span class="pre">summed_spin_channels</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.electronic_structure.cohp.Cohp"
class="reference internal"
title="pymatgen.electronic_structure.cohp.Cohp"><span
class="pre">Cohp</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/cohp.py#L411-L469"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.cohp.CompleteCohp.get_summed_cohp_by_label_list"
class="headerlink" title="Link to this definition"></a>  
Get a Cohp object that includes a summed COHP divided by divisor.

Parameters<span class="colon">:</span>  
- **label_list** (*list\[str\]*) – Labels for the COHP to include.

- **divisor** (*float*) – The summed COHP will be divided by this
  divisor.

- **summed_spin_channels** (*bool*) – Sum the spin channels and return
  the sum in Spin.up.

Returns<span class="colon">:</span>  
A Cohp object for the summed COHP.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">IcohpCollection</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">list_labels</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">list_atom1</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">list_atom2</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">list_length</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">list_translation</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">list_num</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">list_icohp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">is_spin_polarized</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span>*, *<span class="n"><span class="pre">list_orb_icohp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'icohp'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'orbitals'</span></span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">are_coops</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">are_cobis</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/cohp.py#L1118-L1456"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.IcohpCollection"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Collection of IcohpValues.

<span class="sig-name descname"><span class="pre">are_coops</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.IcohpCollection.are_coops"
class="headerlink" title="Link to this definition"></a>  
Whether these are ICOOPs.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">are_cobis</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.IcohpCollection.are_cobis"
class="headerlink" title="Link to this definition"></a>  
Whether these are ICOOPs.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">is_spin_polarized</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.cohp.IcohpCollection.is_spin_polarized"
class="headerlink" title="Link to this definition"></a>  
Whether the calculation is spin polarized.

Type<span class="colon">:</span>  
bool

Parameters<span class="colon">:</span>  
- **list_labels** (*list\[str\]*) – Labels for ICOHP/ICOOP values.

- **list_atom1** (*list\[str\]*) – Atom names, e.g. “O1”.

- **list_atom2** (*list\[str\]*) – Atom names, e.g. “O1”.

- **list_length** (*list\[float\]*) – Bond lengths in Angstrom.

- **list_translation** (*list\[tuple\[float,* *float,* *float\]\]*) –
  Cell translation vectors.

- **list_num** (*list\[int\]*) – Numbers of equivalent bonds, usually 1
  starting from LOBSTER 3.0.0.

- **list_icohp** (*list\[dict\]*) – Dicts as {Spin.up: ICOHP_up,
  Spin.down: ICOHP_down}.

- **is_spin_polarized** (*bool*) – Whether the calculation is spin
  polarized.

- **list_orb_icohp** (*list\[dict\]*) – Dicts as
  {\[str(Orbital1)-str(Orbital2)\]: { “icohp”: {Spin.up: IcohpValue for
  spin.up, Spin.down: IcohpValue for spin.down}, “orbitals”: \[Orbital1,
  Orbital2\]}.

- **are_coops** (*bool*) – Whether ICOOPs are stored.

- **are_cobis** (*bool*) – Whether ICOBIs are stored.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">are_cobis</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id0" class="headerlink" title="Link to this definition"></a>  
Whether this is COBI.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">are_coops</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id1" class="headerlink" title="Link to this definition"></a>  
Whether this is COOP.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/cohp.py#L1389-L1414"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.IcohpCollection.as_dict"
class="headerlink" title="Link to this definition"></a>  
JSON-serializable dict representation of COHP.

<span class="sig-name descname"><span class="pre">extremum_icohpvalue</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">summed_spin_channels</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Spin.up</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/cohp.py#L1336-L1372"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.cohp.IcohpCollection.extremum_icohpvalue"
class="headerlink" title="Link to this definition"></a>  
Get ICOHP/ICOOP of the strongest bond.

Parameters<span class="colon">:</span>  
- **summed_spin_channels** (*bool*) – Whether the ICOHPs/ICOOPs of both
  spin channels should be summed.

- **spin** (<a href="#pymatgen.electronic_structure.core.Spin"
  class="reference internal"
  title="pymatgen.electronic_structure.core.Spin"><em>Spin</em></a>) –
  If not summed_spin_channels, this indicates which spin channel should
  be returned.

Returns<span class="colon">:</span>  
Lowest ICOHP/largest ICOOP value (i.e. ICOHP/ICOOP value of strongest
bond).

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/cohp.py#L1416-L1456"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.IcohpCollection.from_dict"
class="headerlink" title="Link to this definition"></a>  
Generate IcohpCollection from a dict representation.

<span class="sig-name descname"><span class="pre">get_icohp_by_label</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">summed_spin_channels</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Spin.up</span></span>*, *<span class="n"><span class="pre">orbitals</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Orbital"
class="reference internal"
title="pymatgen.electronic_structure.core.Orbital"><span
class="pre">Orbital</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><a href="#pymatgen.electronic_structure.core.Orbital"
class="reference internal"
title="pymatgen.electronic_structure.core.Orbital"><span
class="pre">Orbital</span></a><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/cohp.py#L1192-L1224"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.cohp.IcohpCollection.get_icohp_by_label"
class="headerlink" title="Link to this definition"></a>  
Get an ICOHP value for a certain bond indicated by the label.

Parameters<span class="colon">:</span>  
- **label** (*str*) – The bond number in
  Icohplist.lobster/Icooplist.lobster, starting from “1”.

- **summed_spin_channels** (*bool*) – Whether the ICOHPs/ICOOPs of both
  spin channels should be summed.

- **spin** (<a href="#pymatgen.electronic_structure.core.Spin"
  class="reference internal"
  title="pymatgen.electronic_structure.core.Spin"><em>Spin</em></a>) –
  If not summed_spin_channels, indicate which spin channel should be
  returned.

- **orbitals** – List of Orbital or “str(Orbital1)-str(Orbital2)”.

Returns<span class="colon">:</span>  
ICOHP/ICOOP value.

Return type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">get_icohp_dict_by_bondlengths</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">minbondlength</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.0</span></span>*, *<span class="n"><span class="pre">maxbondlength</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">8.0</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><a href="#pymatgen.electronic_structure.cohp.IcohpValue"
class="reference internal"
title="pymatgen.electronic_structure.cohp.IcohpValue"><span
class="pre">IcohpValue</span></a><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/cohp.py#L1262-L1280"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.cohp.IcohpCollection.get_icohp_dict_by_bondlengths"
class="headerlink" title="Link to this definition"></a>  
Get IcohpValues within certain bond length range.

Parameters<span class="colon">:</span>  
- **minbondlength** (*float*) – The minimum bond length.

- **maxbondlength** (*float*) – The maximum bond length.

Returns<span class="colon">:</span>  
Keys are the labels from the initial list_labels.

Return type<span class="colon">:</span>  
dict\[str, <a href="#pymatgen.electronic_structure.cohp.IcohpValue"
class="reference internal"
title="pymatgen.electronic_structure.cohp.IcohpValue">IcohpValue</a>\]

<span class="sig-name descname"><span class="pre">get_icohp_dict_of_site</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">site</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">minsummedicohp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">maxsummedicohp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">minbondlength</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.0</span></span>*, *<span class="n"><span class="pre">maxbondlength</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">8.0</span></span>*, *<span class="n"><span class="pre">only_bonds_to</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><a href="#pymatgen.electronic_structure.cohp.IcohpValue"
class="reference internal"
title="pymatgen.electronic_structure.cohp.IcohpValue"><span
class="pre">IcohpValue</span></a><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/cohp.py#L1282-L1334"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.cohp.IcohpCollection.get_icohp_dict_of_site"
class="headerlink" title="Link to this definition"></a>  
Get IcohpValues for a certain site.

Parameters<span class="colon">:</span>  
- **site** (*int*) – The site of interest, ordered as in
  Icohplist.lobster/Icooplist.lobster, starts from 0.

- **minsummedicohp** (*float*) – Minimal ICOHP/ICOOP of the bonds that
  are considered. It is the summed ICOHP value from both spin channels
  for spin polarized cases

- **maxsummedicohp** (*float*) – Maximal ICOHP/ICOOP of the bonds that
  are considered. It is the summed ICOHP value from both spin channels
  for spin polarized cases

- **minbondlength** (*float*) – The minimum bond length.

- **maxbondlength** (*float*) – The maximum bond length.

- **only_bonds_to** (*list\[str\]*) – The bonding partners that are
  allowed, e.g. \[“O”\].

Returns<span class="colon">:</span>  
Dict of IcohpValues, the keys correspond to the values from the initial
list_labels.

<span class="sig-name descname"><span class="pre">get_summed_icohp_by_label_list</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">label_list</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">divisor</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1.0</span></span>*, *<span class="n"><span class="pre">summed_spin_channels</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Spin.up</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/cohp.py#L1226-L1260"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.cohp.IcohpCollection.get_summed_icohp_by_label_list"
class="headerlink" title="Link to this definition"></a>  
Get the sum of ICOHP values.

Parameters<span class="colon">:</span>  
- **label_list** (*list\[str\]*) – Labels of the ICOHPs/ICOOPs that
  should be summed, the same as in ICOHPLIST/ICOOPLIST.

- **divisor** (*float*) – Divisor used to divide the sum.

- **summed_spin_channels** (*bool*) – Whether the ICOHPs/ICOOPs of both
  spin channels should be summed.

- **spin** (<a href="#pymatgen.electronic_structure.core.Spin"
  class="reference internal"
  title="pymatgen.electronic_structure.core.Spin"><em>Spin</em></a>) –
  If not summed_spin_channels, indicate which spin channel should be
  returned.

Returns<span class="colon">:</span>  
Sum of ICOHPs selected with label_list.

Return type<span class="colon">:</span>  
float

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">is_spin_polarized</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id2" class="headerlink" title="Link to this definition"></a>  
Whether this is spin polarized.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">IcohpValue</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">atom1</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">atom2</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">length</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">translation</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">num</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">icohp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">are_coops</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">are_cobis</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">orbitals</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'icohp'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'orbitals'</span></span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/cohp.py#L929-L1115"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.IcohpValue"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Information for an ICOHP or ICOOP value.

<span class="sig-name descname"><span class="pre">energies</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.IcohpValue.energies"
class="headerlink" title="Link to this definition"></a>  
Energy values for the COHP/ICOHP/COOP/ICOOP.

Type<span class="colon">:</span>  
NDArray

<span class="sig-name descname"><span class="pre">densities</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.IcohpValue.densities"
class="headerlink" title="Link to this definition"></a>  
Density of states for the COHP/ICOHP/COOP/ICOOP.

Type<span class="colon">:</span>  
NDArray

<span class="sig-name descname"><span class="pre">energies_are_cartesian</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.cohp.IcohpValue.energies_are_cartesian"
class="headerlink" title="Link to this definition"></a>  
Whether the energies are cartesian.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">are_coops</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.IcohpValue.are_coops"
class="headerlink" title="Link to this definition"></a>  
Whether the object is COOP/ICOOP.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">are_cobis</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.IcohpValue.are_cobis"
class="headerlink" title="Link to this definition"></a>  
Whether the object is COBIS/ICOBIS.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">icohp</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.IcohpValue.icohp"
class="headerlink" title="Link to this definition"></a>  
The ICOHP/COHP values, whose keys are Spin.up and Spin.down.

Type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">summed_icohp</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.IcohpValue.summed_icohp"
class="headerlink" title="Link to this definition"></a>  
The summed ICOHP/COHP values.

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">num_bonds</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.IcohpValue.num_bonds"
class="headerlink" title="Link to this definition"></a>  
The number of bonds used for the average COHP (for LOBSTER versions
\<3.0).

Type<span class="colon">:</span>  
int

Parameters<span class="colon">:</span>  
- **label** (*str*) – Label for the ICOHP.

- **atom1** (*str*) – The first atom that contributes to the bond.

- **atom2** (*str*) – The second atom that contributes to the bond.

- **length** (*float*) – Bond length.

- **translation** (*tuple\[float,* *float,* *float\]*) – cell
  translation vector, e.g. (0, 0, 0).

- **num** (*int*) – The number of equivalent bonds.

- **icohp** (*dict\[*<a href="#pymatgen.electronic_structure.core.Spin"
  class="reference internal"
  title="pymatgen.electronic_structure.core.Spin"><em>Spin</em></a>*,*
  *float\]*) – {Spin.up: ICOHP_up, Spin.down: ICOHP_down}

- **are_coops** (*bool*) – Whether these are COOPs.

- **are_cobis** (*bool*) – Whether these are COBIs.

- **orbitals** (*dict*) –

  {\[str(Orbital1)-str(Orbital2)\]: { “icohp”: {

  > <div>
  >
  > > <div>
  > >
  > > Spin.up: IcohpValue for spin.up, Spin.down: IcohpValue for
  > > spin.down
  > >
  > > </div>
  >
  > },
  >
  > </div>

  ”orbitals”: \[Orbital1, Orbital2, …\]}.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">are_cobis</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id3" class="headerlink" title="Link to this definition"></a>  
Whether these are ICOBIs.

Returns<span class="colon">:</span>  
bool

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">are_coops</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id4" class="headerlink" title="Link to this definition"></a>  
Whether these are ICOOPs.

Returns<span class="colon">:</span>  
bool

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">icohp</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id5" class="headerlink" title="Link to this definition"></a>  
Dict with ICOHPs for spin up and spin down.

Returns<span class="colon">:</span>  
{Spin.up: ICOHP_up, Spin.down: ICOHP_down}.

Return type<span class="colon">:</span>  
dict\[<a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin">Spin</a>, float\]

<span class="sig-name descname"><span class="pre">icohpvalue</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Spin.up</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/cohp.py#L1046-L1057"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.cohp.IcohpValue.icohpvalue"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
**spin** – Spin.up or Spin.down.

Returns<span class="colon">:</span>  
ICOHP value corresponding to chosen spin.

Return type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">icohpvalue_orbital</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">orbitals</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Orbital"
class="reference internal"
title="pymatgen.electronic_structure.core.Orbital"><span
class="pre">Orbital</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><a href="#pymatgen.electronic_structure.core.Orbital"
class="reference internal"
title="pymatgen.electronic_structure.core.Orbital"><span
class="pre">Orbital</span></a><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">str</span></span>*, *<span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Spin.up</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/cohp.py#L1059-L1080"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.cohp.IcohpValue.icohpvalue_orbital"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
- **orbitals** – tuple\[Orbital, Orbital\] or
  “str(Orbital0)-str(Orbital1)”.

- **spin** (<a href="#pymatgen.electronic_structure.core.Spin"
  class="reference internal"
  title="pymatgen.electronic_structure.core.Spin"><em>Spin</em></a>) –
  Spin.up or Spin.down.

Returns<span class="colon">:</span>  
ICOHP value corresponding to chosen spin.

Return type<span class="colon">:</span>  
float

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">is_spin_polarized</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.cohp.IcohpValue.is_spin_polarized"
class="headerlink" title="Link to this definition"></a>  
Whether this is a spin polarized calculation.

Returns<span class="colon">:</span>  
bool

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">num_bonds</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id6" class="headerlink" title="Link to this definition"></a>  
The number of bonds for which the ICOHP value is an average.

Returns<span class="colon">:</span>  
int

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">summed_icohp</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id7" class="headerlink" title="Link to this definition"></a>  
Summed ICOHPs of both spin channels if spin polarized.

Returns<span class="colon">:</span>  
ICOHP value in eV.

Return type<span class="colon">:</span>  
float

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">summed_orbital_icohp</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/cohp.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.cohp.IcohpValue.summed_orbital_icohp"
class="headerlink" title="Link to this definition"></a>  
Summed orbital-resolved ICOHPs of both spin channels if spin-polarized.

Returns<span class="colon">:</span>  
“str(Orbital1)-str(Ortibal2)”: ICOHP value in eV.

Return type<span class="colon">:</span>  
dict\[str, float\]

<!-- -->

<span class="sig-name descname"><span class="pre">get_integrated_cohp_in_energy_range</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">cohp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.cohp.CompleteCohp"
class="reference internal"
title="pymatgen.electronic_structure.cohp.CompleteCohp"><span
class="pre">CompleteCohp</span></a></span>*, *<span class="n"><span class="pre">label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">orbital</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">energy_range</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">relative_E\_Fermi</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">summed_spin_channels</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/cohp.py#L1459-L1554"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.cohp.get_integrated_cohp_in_energy_range"
class="headerlink" title="Link to this definition"></a>  
Integrate CompleteCohps which include data of integrated COHPs (ICOHPs).

Parameters<span class="colon">:</span>  
- **cohp** (<a href="#pymatgen.electronic_structure.cohp.CompleteCohp"
  class="reference internal"
  title="pymatgen.electronic_structure.cohp.CompleteCohp"><em>CompleteCohp</em></a>)
  – CompleteCohp object.

- **label** (*str*) – Label of the COHP data.

- **orbital** (*str*) – If not None, a orbital resolved integrated COHP
  will be returned.

- **energy_range** – If None, return the ICOHP value at Fermi level. If
  float, integrate from this value up to Fermi level. If (float, float),
  integrate in between.

- **relative_E\_Fermi** (*bool*) – Whether energy scale with Fermi level
  at 0 eV is chosen.

- **summed_spin_channels** (*bool*) – Whether Spin channels will be
  summed.

Returns<span class="colon">:</span>  
float: the ICOHP. else:

> <div>
>
> dict: {Spin.up: float, Spin.down: float}
>
> </div>

Return type<span class="colon">:</span>  
If summed_spin_channels

</div>

<div id="module-pymatgen.electronic_structure.core" class="section">

<span id="pymatgen-electronic-structure-core-module"></span>

## pymatgen.electronic_structure.core module<a href="#module-pymatgen.electronic_structure.core" class="headerlink"
title="Link to this heading"></a>

This module provides core classes to define electronic structure,
including Spin, Orbital and Magmom.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Magmom</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">moment</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">MagMomentLike</span></span>*, *<span class="n"><span class="pre">saxis</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">(0,</span> <span class="pre">0,</span> <span class="pre">1)</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/core.py#L87-L490"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.Magmom" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

In active development. Use with caution, feedback is appreciated.

Class to handle magnetic moments. Define the magnetic moment of a site
or species relative to a spin quantization axis. Designed for use in
electronic structure calculations.

> <div>
>
> - For the general case, Magmom can be specified by a 3D vector,
>
> e.g. m = Magmom(\[1.0, 1.0, 2.0\]), and indexing will work as
> expected, e.g. m\[0\] gives 1.0.
>
> - For collinear calculations, Magmom can assumed to be float-like,
>
> e.g. m = Magmom(5.0) will work as expected, e.g. float(m) gives 5.0.
>
> </div>

Both cases should be safe and shouldn’t give any surprise, and more
advanced functionality is available if required.

There are also static methods for sequences of magmoms:

> <div>
>
> - Magmom.are_collinear(magmoms) - If True, a collinear electronic
>
> structure calculation can be safely initialized, with float(Magmom)
> giving the expected scalar magnetic moment value.
>
> - Magmom.get_consistent_set_and_saxis(magmoms) - For non-collinear
>
> electronic structure calculations, a global and consistent spin axis
> has to be used. This method returns a list of Magmoms which all share
> a common spin axis, along with the global spin axis.
>
> </div>

All methods that take sequence of magmoms will accept either Magmom
objects, or as scalars/lists and will automatically convert to Magmom
representations internally.

The following methods are also useful for VASP calculations:  
- Magmom.get_xyz_magmom_with_001_saxis()

- Magmom.get_00t_magmom_with_xyz_saxis()

See VASP documentation for more information:  
<a href="https://cms.mpi.univie.ac.at/wiki/index.php/SAXIS"
class="reference external">https://cms.mpi.univie.ac.at/wiki/index.php/SAXIS</a>

Parameters<span class="colon">:</span>  
- **moment** (*float* *\|* *Sequence\[float\]* *\|* *NDArray,*
  <a href="#pymatgen.electronic_structure.core.Magmom"
  class="reference internal"
  title="pymatgen.electronic_structure.core.Magmom"><em>Magmom</em></a>)
  – Magnetic moment.

- **saxis** (*tuple\[float,* *float,* *float\]*) – Spin axis, and will
  be converted to unit vector (default is (0, 0, 1)).

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">are_collinear</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">magmoms</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">MagMomentLike</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/core.py#L423-L447"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.Magmom.are_collinear"
class="headerlink" title="Link to this definition"></a>  
Check if a list of magnetic moments are collinear with each other.

Parameters<span class="colon">:</span>  
**magmoms** (*Sequence\[MagMomentLike\]*) – Magmoms, floats or vectors.

Returns<span class="colon">:</span>  
bool.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_global_moment_and_saxis</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">global_moment</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">MagMomentLike</span></span>*, *<span class="n"><span class="pre">saxis</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/core.py#L210-L227"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.core.Magmom.from_global_moment_and_saxis"
class="headerlink" title="Link to this definition"></a>  
Initialize Magmom from a given global magnetic moment, i.e. magnetic
moment with saxis=(0, 0, 1), and provided saxis.

Method is useful if you do not know the components of your magnetic
moment in frame of your desired spin axis.

Parameters<span class="colon">:</span>  
- **global_moment** (*MagMomentLike*) – Global magnetic moment.

- **saxis** (*tuple\[float,* *float,* *float\]*) – Spin axis.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_moment_relative_to_crystal_axes</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">moment</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">lattice</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.lattice.Lattice"
class="reference internal" title="pymatgen.core.lattice.Lattice"><span
class="pre">Lattice</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/core.py#L449-L472"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.core.Magmom.from_moment_relative_to_crystal_axes"
class="headerlink" title="Link to this definition"></a>  
Obtain a Magmom object from a magnetic moment provided relative to
crystal axes.

Used for obtaining moments from magCIF file.

Parameters<span class="colon">:</span>  
- **moment** (*tuple\[float,* *float,* *float\]*) – Magnetic moment.

- **lattice**
  (<a href="pymatgen.core.html#pymatgen.core.lattice.Lattice"
  class="reference internal"
  title="pymatgen.core.lattice.Lattice"><em>Lattice</em></a>) – Lattice.

Returns<span class="colon">:</span>  
Magmom

<span class="sig-name descname"><span class="pre">get_00t_magmom_with_xyz_saxis</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/core.py#L322-L355"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.core.Magmom.get_00t_magmom_with_xyz_saxis"
class="headerlink" title="Link to this definition"></a>  
For internal implementation reasons, the non-collinear calculations in
VASP prefer the following.

> <div>
>
> MAGMOM = 0 0 total_magnetic_moment SAXIS = x y z
>
> </div>

to an equivalent:

> <div>
>
> MAGMOM = x y z SAXIS = 0 0 1
>
> </div>

Returns<span class="colon">:</span>  
With magnetic moment (0, 0, t), where t is the total magnetic  
moment, and saxis rotated as required.

A consistent direction of saxis is applied such that t might be positive
or negative depending on the direction of the initial moment. This is
useful in the case of collinear structures, rather than assuming t is
always positive.

Return type<span class="colon">:</span>  
<a href="#pymatgen.electronic_structure.core.Magmom"
class="reference internal"
title="pymatgen.electronic_structure.core.Magmom">Magmom</a>

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">get_consistent_set_and_saxis</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">magmoms</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">MagMomentLike</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">saxis</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">NDArray</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">NDArray</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/core.py#L378-L395"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.core.Magmom.get_consistent_set_and_saxis"
class="headerlink" title="Link to this definition"></a>  
Ensure magmoms use the same spin axis.

Parameters<span class="colon">:</span>  
- **magmoms** (*Sequence\[MagMomentLike\]*) – Magmoms, floats or
  vectors.

- **saxis** (*tuple\[float,* *float,* *float\]*) – An optional global
  spin axis.

Returns<span class="colon">:</span>  
Magmoms and their global spin axes.

Return type<span class="colon">:</span>  
tuple\[list\[<a href="#pymatgen.electronic_structure.core.Magmom"
class="reference internal"
title="pymatgen.electronic_structure.core.Magmom">Magmom</a>\],
NDArray\]

<span class="sig-name descname"><span class="pre">get_moment</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">saxis</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">(0,</span> <span class="pre">0,</span> <span class="pre">1)</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">NDArray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/core.py#L229-L293"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.Magmom.get_moment"
class="headerlink" title="Link to this definition"></a>  
Get magnetic moment relative to a given spin quantization axis. If no
axis is provided, moment will be given relative to the Magmom’s internal
spin quantization axis, i.e. equivalent to Magmom.moment.

Parameters<span class="colon">:</span>  
**saxis** (*tuple\[float,* *float,* *float\]*) – Spin quantization axis.

Returns<span class="colon">:</span>  
NDArray of length 3.

<span class="sig-name descname"><span class="pre">get_moment_relative_to_crystal_axes</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">lattice</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.lattice.Lattice"
class="reference internal" title="pymatgen.core.lattice.Lattice"><span
class="pre">Lattice</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/core.py#L474-L490"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.core.Magmom.get_moment_relative_to_crystal_axes"
class="headerlink" title="Link to this definition"></a>  
If scalar magmoms, moments will be given arbitrarily along z.

Used for writing moments to magCIF file.

Parameters<span class="colon">:</span>  
**lattice** (<a href="pymatgen.core.html#pymatgen.core.lattice.Lattice"
class="reference internal"
title="pymatgen.core.lattice.Lattice"><em>Lattice</em></a>) – The
lattice.

Returns<span class="colon">:</span>  
tuple\[float, float, float\]

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">get_suggested_saxis</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">magmoms</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">MagMomentLike</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">NDArray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/core.py#L397-L421"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.Magmom.get_suggested_saxis"
class="headerlink" title="Link to this definition"></a>  
Get a suggested spin axis for magmoms, taking the largest magnetic
moment as the reference. For calculations with collinear spins, this
would give a sensible saxis for a NCL calculation.

Parameters<span class="colon">:</span>  
**magmoms** (*Sequence\[MagMomentLike\]*) – Magmoms, floats or vectors.

Returns<span class="colon">:</span>  
NDArray of length 3

<span class="sig-name descname"><span class="pre">get_xyz_magmom_with_001_saxis</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/core.py#L313-L320"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.core.Magmom.get_xyz_magmom_with_001_saxis"
class="headerlink" title="Link to this definition"></a>  
Get a Magmom in the default setting of saxis = (0, 0, 1) and the
magnetic moment rotated as required.

Returns<span class="colon">:</span>  
Magmom

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">global_moment</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">NDArray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.Magmom.global_moment"
class="headerlink" title="Link to this definition"></a>  
The magnetic moment defined in an arbitrary global reference frame, as a
np.array of length 3.

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">have_consistent_saxis</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">magmoms</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">MagMomentLike</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/core.py#L357-L376"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.core.Magmom.have_consistent_saxis"
class="headerlink" title="Link to this definition"></a>  
Check whether all Magmoms have a consistent spin quantization axis.

To write MAGMOM tags to a VASP INCAR, a consistent global SAXIS value
for all magmoms has to be used.

If spin axes are inconsistent, can create a consistent set with:  
Magmom.get_consistent_set(magmoms).

Parameters<span class="colon">:</span>  
**magmoms** (*Sequence\[MagMomentLike\]*) – Magmoms.

Returns<span class="colon">:</span>  
bool

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">projection</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.Magmom.projection"
class="headerlink" title="Link to this definition"></a>  
Project moment along spin quantization axis.

Useful for obtaining collinear approximation for slightly non-collinear
magmoms.

Returns<span class="colon">:</span>  
The projected moment.

Return type<span class="colon">:</span>  
float

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Orbital</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">value</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/core.py#L52-L84"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.Orbital" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`Enum`</span>

Enum type for specific orbitals. The indices are the order in which the
orbitals are reported in VASP and has no special meaning.

<span class="sig-name descname"><span class="pre">dx2</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">8</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.Orbital.dx2"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">dxy</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">4</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.Orbital.dxy"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">dxz</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">7</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.Orbital.dxz"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">dyz</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">5</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.Orbital.dyz"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">dz2</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">6</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.Orbital.dz2"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">f0</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">12</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.Orbital.f0"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">f1</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">13</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.Orbital.f1"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">f2</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">14</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.Orbital.f2"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">f3</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">15</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.Orbital.f3"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">f_1</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">11</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.Orbital.f_1"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">f_2</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">10</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.Orbital.f_2"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">f_3</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">9</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.Orbital.f_3"
class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">orbital_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="#pymatgen.electronic_structure.core.OrbitalType"
class="reference internal"
title="pymatgen.electronic_structure.core.OrbitalType"><span
class="pre">OrbitalType</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.Orbital.orbital_type"
class="headerlink" title="Link to this definition"></a>  
OrbitalType of an orbital.

<span class="sig-name descname"><span class="pre">px</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">3</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.Orbital.px"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">py</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">1</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.Orbital.py"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">pz</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">2</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.Orbital.pz"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">s</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">0</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.Orbital.s"
class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">OrbitalType</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">value</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/core.py#L39-L49"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.OrbitalType"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`Enum`</span>

Enum type for orbital type. Indices are the azimuthal quantum number l.

<span class="sig-name descname"><span class="pre">d</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">2</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.OrbitalType.d"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">f</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">3</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.OrbitalType.f"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">p</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">1</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.OrbitalType.p"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">s</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">0</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.OrbitalType.s"
class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Spin</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">value</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/core.py#L23-L36"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.Spin" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`Enum`</span>

Enum type for Spin. Only up and down. Usage: Spin.up, Spin.down.

<span class="sig-name descname"><span class="pre">down</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">-1</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.Spin.down"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">up</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">1</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/core.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.core.Spin.up" class="headerlink"
title="Link to this definition"></a>  

</div>

<div id="module-pymatgen.electronic_structure.dos" class="section">

<span id="pymatgen-electronic-structure-dos-module"></span>

## pymatgen.electronic_structure.dos module<a href="#module-pymatgen.electronic_structure.dos" class="headerlink"
title="Link to this heading"></a>

This module defines classes to represent the density of states (DOS),
etc.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">CompleteDos</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">total_dos</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.dos.Dos"
class="reference internal"
title="pymatgen.electronic_structure.dos.Dos"><span
class="pre">Dos</span></a></span>*, *<span class="n"><span class="pre">pdoss</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Mapping</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
class="reference internal"
title="pymatgen.core.sites.PeriodicSite"><span
class="pre">PeriodicSite</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Mapping</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Orbital"
class="reference internal"
title="pymatgen.electronic_structure.core.Orbital"><span
class="pre">Orbital</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Mapping</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">ArrayLike</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">normalize</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L646-L1392"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.CompleteDos"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.electronic_structure.dos.Dos"
class="reference internal"
title="pymatgen.electronic_structure.dos.Dos"><span class="pre"><code
class="sourceCode python">Dos</code></span></a>

Define total DOS, and projected DOS (PDOS).

Mainly used by pymatgen.io.vasp.Vasprun to create a complete DOS from a
vasprun.xml file. You are unlikely to generate this object manually.

<span class="sig-name descname"><span class="pre">structure</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/dos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.CompleteDos.structure"
class="headerlink" title="Link to this definition"></a>  
Structure associated with the CompleteDos.

Type<span class="colon">:</span>  
<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure">Structure</a>

<span class="sig-name descname"><span class="pre">pdos</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/dos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.CompleteDos.pdos"
class="headerlink" title="Link to this definition"></a>  
PDOS.

Type<span class="colon">:</span>  
dict\[<a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
class="reference internal"
title="pymatgen.core.sites.PeriodicSite">PeriodicSite</a>,
dict\[<a href="#pymatgen.electronic_structure.core.Orbital"
class="reference internal"
title="pymatgen.electronic_structure.core.Orbital">Orbital</a>,
dict\[<a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin">Spin</a>, NDArray\]\]\]

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  Structure associated with this DOS.

- **total_dos** (<a href="#pymatgen.electronic_structure.dos.Dos"
  class="reference internal"
  title="pymatgen.electronic_structure.dos.Dos"><em>Dos</em></a>) –
  Total DOS for the structure.

- **pdoss** (*dict*) – The PDOSs supplied as {Site: {Orbital: {Spin:
  Densities}}}.

- **normalize** (*bool*) – Whether to normalize the DOS by the volume of
  the structure. If True, the units of the DOS are states/eV/Angstrom^3.
  Otherwise, the units are states/eV.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L1373-L1392"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.CompleteDos.as_dict"
class="headerlink" title="Link to this definition"></a>  
JSON-serializable dict representation of CompleteDos.

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">fp_to_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">fp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.dos.DosFingerprint"
class="reference internal"
title="pymatgen.electronic_structure.dos.DosFingerprint"><span
class="pre">DosFingerprint</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">NDArray</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L1285-L1295"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.CompleteDos.fp_to_dict"
class="headerlink" title="Link to this definition"></a>  
Convert a DOS FingerPrint into a dict.

Parameters<span class="colon">:</span>  
**fp** (<a href="#pymatgen.electronic_structure.dos.DosFingerprint"
class="reference internal"
title="pymatgen.electronic_structure.dos.DosFingerprint"><em>DosFingerprint</em></a>)
– The DOS FingerPrint to convert.

Returns<span class="colon">:</span>  
The FingerPrint as dict.

Return type<span class="colon">:</span>  
dict(Keys=type, Values=np.array(energies, densities))

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L1358-L1371"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.CompleteDos.from_dict"
class="headerlink" title="Link to this definition"></a>  
Get CompleteDos object from dict representation.

<span class="sig-name descname"><span class="pre">get_band_center</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">band</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.core.OrbitalType"
class="reference internal"
title="pymatgen.electronic_structure.core.OrbitalType"><span
class="pre">OrbitalType</span></a></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">OrbitalType.d</span></span>*, *<span class="n"><span class="pre">elements</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">SpeciesLike</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sites</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
class="reference internal"
title="pymatgen.core.sites.PeriodicSite"><span
class="pre">PeriodicSite</span></a><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">erange</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L897-L935"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.CompleteDos.get_band_center"
class="headerlink" title="Link to this definition"></a>  
Compute the orbital-projected band center, defined as the first moment
relative to the Fermi level as:

> <div>
>
> int\_{-inf}^{+inf} rho(E)\*E dE/int\_{-inf}^{+inf} rho(E) dE.
>
> </div>

Note that the band center is often highly sensitive to the selected
energy range.

“elements” and “sites” cannot be used together.

References

Hammer and Norskov, Surf. Sci., 343 (1995).

Parameters<span class="colon">:</span>  
- **band** (<a href="#pymatgen.electronic_structure.core.OrbitalType"
  class="reference internal"
  title="pymatgen.electronic_structure.core.OrbitalType"><em>OrbitalType</em></a>)
  – Orbital to get the band center of (default is d-band)

- **elements** (*list\[SpeciesLike\]*) – Elements to get the band center
  of.

- **sites**
  (*list\[*<a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
  class="reference internal"
  title="pymatgen.core.sites.PeriodicSite"><em>PeriodicSite</em></a>*\]*)
  – Sites to get the band center of.

- **spin** (<a href="#pymatgen.electronic_structure.core.Spin"
  class="reference internal"
  title="pymatgen.electronic_structure.core.Spin"><em>Spin</em></a>) –
  Spin channel to use. If None, both spin channels will be combined.

- **erange** (*tuple(min,* *max)*) – The energy range to consider, with
  respect to the Fermi level. Default to None for all energies.

Returns<span class="colon">:</span>  
The band center in eV, often denoted epsilon_d for the d-band center.

Return type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">get_band_filling</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">band</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.core.OrbitalType"
class="reference internal"
title="pymatgen.electronic_structure.core.OrbitalType"><span
class="pre">OrbitalType</span></a></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">OrbitalType.d</span></span>*, *<span class="n"><span class="pre">elements</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">SpeciesLike</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sites</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
class="reference internal"
title="pymatgen.core.sites.PeriodicSite"><span
class="pre">PeriodicSite</span></a><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L845-L895"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.dos.CompleteDos.get_band_filling"
class="headerlink" title="Link to this definition"></a>  
Compute the orbital-projected band filling, defined as the zeroth moment
up to the Fermi level.

“elements” and “sites” cannot be used together.

Parameters<span class="colon">:</span>  
- **band** (<a href="#pymatgen.electronic_structure.core.OrbitalType"
  class="reference internal"
  title="pymatgen.electronic_structure.core.OrbitalType"><em>OrbitalType</em></a>)
  – Orbital to get the band center of (default is d-band).

- **elements** (*list\[SpeciesLike\]*) – Elements to get the band center
  of.

- **sites**
  (*list\[*<a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
  class="reference internal"
  title="pymatgen.core.sites.PeriodicSite"><em>PeriodicSite</em></a>*\]*)
  – Sites to get the band center of.

- **spin** (<a href="#pymatgen.electronic_structure.core.Spin"
  class="reference internal"
  title="pymatgen.electronic_structure.core.Spin"><em>Spin</em></a>) –
  Spin channel to use. If None, both spin channels will be combined.

Returns<span class="colon">:</span>  
Band filling in eV, often denoted f_d for the d-band.

Return type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">get_band_kurtosis</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">band</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.core.OrbitalType"
class="reference internal"
title="pymatgen.electronic_structure.core.OrbitalType"><span
class="pre">OrbitalType</span></a></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">OrbitalType.d</span></span>*, *<span class="n"><span class="pre">elements</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">SpeciesLike</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sites</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
class="reference internal"
title="pymatgen.core.sites.PeriodicSite"><span
class="pre">PeriodicSite</span></a><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">erange</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L999-L1029"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.dos.CompleteDos.get_band_kurtosis"
class="headerlink" title="Link to this definition"></a>  
Get the orbital-projected kurtosis, defined as the fourth standardized moment  
int\_{-inf}^{+inf} rho(E)\*(E-E_center)^4 dE/int\_{-inf}^{+inf} rho(E)
dE) / (int\_{-inf}^{+inf} rho(E)\*(E-E_center)^2 dE/int\_{-inf}^{+inf}
rho(E) dE))^2

where E_center is the orbital-projected band center.

Note that the kurtosis is often highly sensitive to the selected energy
range.

“elements” and “sites” cannot be used together.

Parameters<span class="colon">:</span>  
- **band** (<a href="#pymatgen.electronic_structure.core.OrbitalType"
  class="reference internal"
  title="pymatgen.electronic_structure.core.OrbitalType"><em>OrbitalType</em></a>)
  – Orbitals to get the band center of (default is d-band).

- **elements** (*list\[SpeciesLike\]*) – Elements to get the band center
  of.

- **sites**
  (*list\[*<a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
  class="reference internal"
  title="pymatgen.core.sites.PeriodicSite"><em>PeriodicSite</em></a>*\]*)
  – Sites to get the band center of.

- **spin** (<a href="#pymatgen.electronic_structure.core.Spin"
  class="reference internal"
  title="pymatgen.electronic_structure.core.Spin"><em>Spin</em></a>) –
  Spin channel to use. By default, both spin channels will be combined.

- **erange** (*tuple(min,* *max)*) – The energy range to consider, with
  respect to the Fermi level. Default to None for all energies.

Returns<span class="colon">:</span>  
The orbital-projected kurtosis (dimensionless).

Return type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">get_band_skewness</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">band</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.core.OrbitalType"
class="reference internal"
title="pymatgen.electronic_structure.core.OrbitalType"><span
class="pre">OrbitalType</span></a></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">OrbitalType.d</span></span>*, *<span class="n"><span class="pre">elements</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">SpeciesLike</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sites</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
class="reference internal"
title="pymatgen.core.sites.PeriodicSite"><span
class="pre">PeriodicSite</span></a><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">erange</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L967-L997"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.dos.CompleteDos.get_band_skewness"
class="headerlink" title="Link to this definition"></a>  
Get the orbital-projected skewness, defined as the third standardized moment:  
int\_{-inf}^{+inf} rho(E)\*(E-E_center)^3 dE/int\_{-inf}^{+inf} rho(E)
dE) / (int\_{-inf}^{+inf} rho(E)\*(E-E_center)^2 dE/int\_{-inf}^{+inf}
rho(E) dE))^(3/2)

where E_center is the orbital-projected band center.

Note that the skewness is often highly sensitive to the selected energy
range.

“elements” and “sites” cannot be used together.

Parameters<span class="colon">:</span>  
- **band** (<a href="#pymatgen.electronic_structure.core.OrbitalType"
  class="reference internal"
  title="pymatgen.electronic_structure.core.OrbitalType"><em>OrbitalType</em></a>)
  – Orbitals to get the band center of (default is d-band).

- **elements** (*list\[SpeciesLike\]*) – Elements to get the band center
  of.

- **sites**
  (*list\[*<a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
  class="reference internal"
  title="pymatgen.core.sites.PeriodicSite"><em>PeriodicSite</em></a>*\]*)
  – Sites to get the band center of.

- **spin** (<a href="#pymatgen.electronic_structure.core.Spin"
  class="reference internal"
  title="pymatgen.electronic_structure.core.Spin"><em>Spin</em></a>) –
  Spin channel to use. By default, both spin channels will be combined.

- **erange** (*tuple(min,* *max)*) – The energy range to consider, with
  respect to the Fermi level. Default to None for all energies.

Returns<span class="colon">:</span>  
The orbital-projected skewness (dimensionless).

Return type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">get_band_width</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">band</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.core.OrbitalType"
class="reference internal"
title="pymatgen.electronic_structure.core.OrbitalType"><span
class="pre">OrbitalType</span></a></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">OrbitalType.d</span></span>*, *<span class="n"><span class="pre">elements</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">SpeciesLike</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sites</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
class="reference internal"
title="pymatgen.core.sites.PeriodicSite"><span
class="pre">PeriodicSite</span></a><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">erange</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L937-L965"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.CompleteDos.get_band_width"
class="headerlink" title="Link to this definition"></a>  
Get the orbital-projected band width, defined as the square root of the
second moment:

> <div>
>
> sqrt(int\_{-inf}^{+inf} rho(E)\*(E-E_center)^2 dE/int\_{-inf}^{+inf}
> rho(E) dE)
>
> </div>

where E_center is the orbital-projected band center.

Note that the band width is often highly sensitive to the selected
energy range.

“elements” and “sites” cannot be used together.

Parameters<span class="colon">:</span>  
- **band** (<a href="#pymatgen.electronic_structure.core.OrbitalType"
  class="reference internal"
  title="pymatgen.electronic_structure.core.OrbitalType"><em>OrbitalType</em></a>)
  – Orbital to get the band center of (default is d-band).

- **elements** (*list\[SpeciesLike\]*) – Elements to get the band center
  of.

- **sites**
  (*list\[*<a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
  class="reference internal"
  title="pymatgen.core.sites.PeriodicSite"><em>PeriodicSite</em></a>*\]*)
  – Sites to get the band center of.

- **spin** (<a href="#pymatgen.electronic_structure.core.Spin"
  class="reference internal"
  title="pymatgen.electronic_structure.core.Spin"><em>Spin</em></a>) –
  Spin channel to use. By default, both spin channels will be combined.

- **erange** (*tuple(min,* *max)*) – The energy range to consider, with
  respect to the Fermi level. Default to None for all energies.

Returns<span class="colon">:</span>  
Orbital-projected band width in eV.

Return type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">get_dos_fp</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">fp_type</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'summed_pdos'</span></span>*, *<span class="n"><span class="pre">binning</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">min_e</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">max_e</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">n_bins</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">256</span></span>*, *<span class="n"><span class="pre">normalize</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.electronic_structure.dos.DosFingerprint"
class="reference internal"
title="pymatgen.electronic_structure.dos.DosFingerprint"><span
class="pre">DosFingerprint</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L1191-L1283"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.CompleteDos.get_dos_fp"
class="headerlink" title="Link to this definition"></a>  
Generate the DOS fingerprint.

Based on the work of:  
F. Knoop, T. A. r Purcell, M. Scheffler, C. Carbogno, J. Open Source
Softw. 2020, 5, 2671. Source - <a
href="https://gitlab.com/vibes-developers/vibes/-/tree/master/vibes/materials_fp"
class="reference external">https://gitlab.com/vibes-developers/vibes/-/tree/master/vibes/materials_fp</a>
Copyright (c) 2020 Florian Knoop, Thomas A.R.Purcell, Matthias
Scheffler, Christian Carbogno. Please also see and cite related work
by: M. Kuban, S. Rigamonti, C. Draxl, Digital Discovery 2024, 3, 2448.

Parameters<span class="colon">:</span>  
- **fp_type** (*str*) – The FingerPrint type, can be
  “{s/p/d/f/summed}\_{pdos/tdos}” (default is summed_pdos).

- **binning** (*bool*) – Whether to bin the DOS FingerPrint using
  np.linspace and n_bins. Default is True.

- **min_e** (*float*) – The minimum energy to include (default is None).

- **max_e** (*float*) – The maximum energy to include (default is None).

- **n_bins** (*int*) – Number of bins to be used, if binning (default is
  256).

- **normalize** (*bool*) – Whether to normalize the integrated DOS to 1.
  Default is True.

Raises<span class="colon">:</span>  
**ValueError** – If “fp_type” is not one of the accepted values.

Returns<span class="colon">:</span>  
The DOS fingerprint.

Return type<span class="colon">:</span>  
<a href="#pymatgen.electronic_structure.dos.DosFingerprint"
class="reference internal"
title="pymatgen.electronic_structure.dos.DosFingerprint">DosFingerprint</a>(energies,
densities, type, n_bins)

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">get_dos_fp_similarity</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">fp1</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.dos.DosFingerprint"
class="reference internal"
title="pymatgen.electronic_structure.dos.DosFingerprint"><span
class="pre">DosFingerprint</span></a></span>*, *<span class="n"><span class="pre">fp2</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.dos.DosFingerprint"
class="reference internal"
title="pymatgen.electronic_structure.dos.DosFingerprint"><span
class="pre">DosFingerprint</span></a></span>*, *<span class="n"><span class="pre">col</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1</span></span>*, *<span class="n"><span class="pre">pt</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'All'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'All'</span></span>*, *<span class="n"><span class="pre">normalize</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">metric</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'tanimoto'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'wasserstein'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cosine-sim'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'tanimoto'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L1297-L1356"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.dos.CompleteDos.get_dos_fp_similarity"
class="headerlink" title="Link to this definition"></a>  
Calculate the similarity index (dot product) of two DOS FingerPrints.

Parameters<span class="colon">:</span>  
- **fp1** (<a href="#pymatgen.electronic_structure.dos.DosFingerprint"
  class="reference internal"
  title="pymatgen.electronic_structure.dos.DosFingerprint"><em>DosFingerprint</em></a>)
  – The 1st dos fingerprint object

- **fp2** (<a href="#pymatgen.electronic_structure.dos.DosFingerprint"
  class="reference internal"
  title="pymatgen.electronic_structure.dos.DosFingerprint"><em>DosFingerprint</em></a>)
  – The 2nd dos fingerprint object

- **col** (*int*) – The item in the fingerprints (0:energies,1:
  densities) to compute the similarity index of (default is 1)

- **pt** (*int* *or* *str*) – The index of the point that the dot
  product is to be taken (default is All)

- **normalize** (*bool*) – If True normalize the scalar product to 1
  (default is False)

- **metric** (*Literal*) – Metric used to compute similarity default is
  “tanimoto”.

Raises<span class="colon">:</span>  
- **ValueError** – If metric other than tanimoto, wasserstein and
  “cosine-sim” is requested.

- **ValueError** – If normalize is set to True along with the metric.

Returns<span class="colon">:</span>  
Similarity index given by the dot product.

Return type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">get_element_dos</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">SpeciesLike</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><a href="#pymatgen.electronic_structure.dos.Dos"
class="reference internal"
title="pymatgen.electronic_structure.dos.Dos"><span
class="pre">Dos</span></a><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L782-L794"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.CompleteDos.get_element_dos"
class="headerlink" title="Link to this definition"></a>  
Get element projected DOS.

Returns<span class="colon">:</span>  
dict\[Element, Dos\]

<span class="sig-name descname"><span class="pre">get_element_spd_dos</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">el</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">SpeciesLike</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.OrbitalType"
class="reference internal"
title="pymatgen.electronic_structure.core.OrbitalType"><span
class="pre">OrbitalType</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><a href="#pymatgen.electronic_structure.dos.Dos"
class="reference internal"
title="pymatgen.electronic_structure.dos.Dos"><span
class="pre">Dos</span></a><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L796-L816"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.dos.CompleteDos.get_element_spd_dos"
class="headerlink" title="Link to this definition"></a>  
Get element and orbital (spd) projected DOS.

Parameters<span class="colon">:</span>  
**el** (*SpeciesLike*) – Element associated with CompleteDos.

Returns<span class="colon">:</span>  
dict\[OrbitalType, Dos\]

<span class="sig-name descname"><span class="pre">get_hilbert_transform</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">band</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.core.OrbitalType"
class="reference internal"
title="pymatgen.electronic_structure.core.OrbitalType"><span
class="pre">OrbitalType</span></a></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">OrbitalType.d</span></span>*, *<span class="n"><span class="pre">elements</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">SpeciesLike</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sites</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
class="reference internal"
title="pymatgen.core.sites.PeriodicSite"><span
class="pre">PeriodicSite</span></a><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.electronic_structure.dos.Dos"
class="reference internal"
title="pymatgen.electronic_structure.dos.Dos"><span
class="pre">Dos</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L1102-L1146"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.dos.CompleteDos.get_hilbert_transform"
class="headerlink" title="Link to this definition"></a>  
Get the Hilbert transform of the orbital-projected DOS, often plotted
for a Newns-Anderson analysis.

“elements” and “sites” cannot be used together.

Parameters<span class="colon">:</span>  
- **band** (<a href="#pymatgen.electronic_structure.core.OrbitalType"
  class="reference internal"
  title="pymatgen.electronic_structure.core.OrbitalType"><em>OrbitalType</em></a>)
  – Orbital to get the band center of (default is d-band).

- **elements** (*list\[SpeciesLike\]*) – Elements to get the band center
  of.

- **sites**
  (*list\[*<a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
  class="reference internal"
  title="pymatgen.core.sites.PeriodicSite"><em>PeriodicSite</em></a>*\]*)
  – Sites to get the band center of.

Returns<span class="colon">:</span>  
Hilbert transformation of the projected DOS.

Return type<span class="colon">:</span>  
<a href="#pymatgen.electronic_structure.dos.Dos"
class="reference internal"
title="pymatgen.electronic_structure.dos.Dos">Dos</a>

<span class="sig-name descname"><span class="pre">get_n\_moment</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">n</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">band</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.core.OrbitalType"
class="reference internal"
title="pymatgen.electronic_structure.core.OrbitalType"><span
class="pre">OrbitalType</span></a></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">OrbitalType.d</span></span>*, *<span class="n"><span class="pre">elements</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">SpeciesLike</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sites</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
class="reference internal"
title="pymatgen.core.sites.PeriodicSite"><span
class="pre">PeriodicSite</span></a><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">erange</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">center</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L1031-L1100"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.CompleteDos.get_n_moment"
class="headerlink" title="Link to this definition"></a>  
Get the nth moment of the DOS centered around the orbital-projected band
center, defined as:

> <div>
>
> int\_{-inf}^{+inf} rho(E)\*(E-E_center)^n dE/int\_{-inf}^{+inf} rho(E)
> dE
>
> </div>

where n is the order, E_center is the orbital-projected band center, and
E is the set of energies taken with respect to the Fermi level.

“elements” and “sites” cannot be used together.

Parameters<span class="colon">:</span>  
- **n** (*int*) – The order for the moment.

- **band** (<a href="#pymatgen.electronic_structure.core.OrbitalType"
  class="reference internal"
  title="pymatgen.electronic_structure.core.OrbitalType"><em>OrbitalType</em></a>)
  – Orbital to get the band center of (default is d-band).

- **elements**
  (*list\[*<a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
  class="reference internal"
  title="pymatgen.core.sites.PeriodicSite"><em>PeriodicSite</em></a>*\]*)
  – Elements to get the band center of.

- **sites**
  (*list\[*<a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
  class="reference internal"
  title="pymatgen.core.sites.PeriodicSite"><em>PeriodicSite</em></a>*\]*)
  – Sites to get the band center of.

- **spin** (<a href="#pymatgen.electronic_structure.core.Spin"
  class="reference internal"
  title="pymatgen.electronic_structure.core.Spin"><em>Spin</em></a>) –
  Spin channel to use. By default, both spin channels will be combined.

- **erange** (*tuple(min,* *max)*) – The energy range to consider, with
  respect to the Fermi level. Default to None for all energies.

- **center** (*bool*) – Take moments with respect to the band center.

Returns<span class="colon">:</span>  
Orbital-projected nth moment in eV

<span class="sig-name descname"><span class="pre">get_normalized</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L686-L696"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.CompleteDos.get_normalized"
class="headerlink" title="Link to this definition"></a>  
Get normalized CompleteDos.

<span class="sig-name descname"><span class="pre">get_site_dos</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">site</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
class="reference internal"
title="pymatgen.core.sites.PeriodicSite"><span
class="pre">PeriodicSite</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.electronic_structure.dos.Dos"
class="reference internal"
title="pymatgen.electronic_structure.dos.Dos"><span
class="pre">Dos</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L710-L720"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.CompleteDos.get_site_dos"
class="headerlink" title="Link to this definition"></a>  
Get the total DOS for a site with all orbitals.

Parameters<span class="colon">:</span>  
**site** (<a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
class="reference internal"
title="pymatgen.core.sites.PeriodicSite"><em>PeriodicSite</em></a>) –
Site in Structure associated with CompleteDos.

Returns<span class="colon">:</span>  
Total DOS for a site with all orbitals.

Return type<span class="colon">:</span>  
<a href="#pymatgen.electronic_structure.dos.Dos"
class="reference internal"
title="pymatgen.electronic_structure.dos.Dos">Dos</a>

<span class="sig-name descname"><span class="pre">get_site_orbital_dos</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">site</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
class="reference internal"
title="pymatgen.core.sites.PeriodicSite"><span
class="pre">PeriodicSite</span></a></span>*, *<span class="n"><span class="pre">orbital</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.core.Orbital"
class="reference internal"
title="pymatgen.electronic_structure.core.Orbital"><span
class="pre">Orbital</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.electronic_structure.dos.Dos"
class="reference internal"
title="pymatgen.electronic_structure.dos.Dos"><span
class="pre">Dos</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L698-L708"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.dos.CompleteDos.get_site_orbital_dos"
class="headerlink" title="Link to this definition"></a>  
Get the Dos for a particular orbital of a particular site.

Parameters<span class="colon">:</span>  
- **site** – Site in Structure associated with CompleteDos.

- **orbital** – Orbital in the site.

Returns<span class="colon">:</span>  
for a particular orbital of a particular site.

Return type<span class="colon">:</span>  
<a href="#pymatgen.electronic_structure.dos.Dos"
class="reference internal"
title="pymatgen.electronic_structure.dos.Dos">Dos</a>

<span class="sig-name descname"><span class="pre">get_site_spd_dos</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">site</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
class="reference internal"
title="pymatgen.core.sites.PeriodicSite"><span
class="pre">PeriodicSite</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.OrbitalType"
class="reference internal"
title="pymatgen.electronic_structure.core.OrbitalType"><span
class="pre">OrbitalType</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><a href="#pymatgen.electronic_structure.dos.Dos"
class="reference internal"
title="pymatgen.electronic_structure.dos.Dos"><span
class="pre">Dos</span></a><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L722-L738"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.dos.CompleteDos.get_site_spd_dos"
class="headerlink" title="Link to this definition"></a>  
Get orbital projected DOS of a particular site.

Parameters<span class="colon">:</span>  
**site** (<a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
class="reference internal"
title="pymatgen.core.sites.PeriodicSite"><em>PeriodicSite</em></a>) –
Site in Structure associated with CompleteDos.

Returns<span class="colon">:</span>  
dict\[OrbitalType, Dos\]

<span class="sig-name descname"><span class="pre">get_site_t2g_eg_resolved_dos</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">site</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
class="reference internal"
title="pymatgen.core.sites.PeriodicSite"><span
class="pre">PeriodicSite</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'e_g'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'t2g'</span></span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><a href="#pymatgen.electronic_structure.dos.Dos"
class="reference internal"
title="pymatgen.electronic_structure.dos.Dos"><span
class="pre">Dos</span></a><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L740-L764"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.dos.CompleteDos.get_site_t2g_eg_resolved_dos"
class="headerlink" title="Link to this definition"></a>  
Get the t2g/e_g projected DOS for a particular site.

Parameters<span class="colon">:</span>  
**site** (<a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
class="reference internal"
title="pymatgen.core.sites.PeriodicSite"><em>PeriodicSite</em></a>) –
Site in Structure associated with CompleteDos.

Returns<span class="colon">:</span>  
Summed e_g and t2g DOS for the site.

Return type<span class="colon">:</span>  
dict\[Literal\[“e_g”, “t2g”\], Dos\]

<span class="sig-name descname"><span class="pre">get_spd_dos</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.OrbitalType"
class="reference internal"
title="pymatgen.electronic_structure.core.OrbitalType"><span
class="pre">OrbitalType</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><a href="#pymatgen.electronic_structure.dos.Dos"
class="reference internal"
title="pymatgen.electronic_structure.dos.Dos"><span
class="pre">Dos</span></a><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L766-L780"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.CompleteDos.get_spd_dos"
class="headerlink" title="Link to this definition"></a>  
Get orbital projected DOS.

Returns<span class="colon">:</span>  
dict\[OrbitalType, Dos\]

<span class="sig-name descname"><span class="pre">get_upper_band_edge</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">band</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.core.OrbitalType"
class="reference internal"
title="pymatgen.electronic_structure.core.OrbitalType"><span
class="pre">OrbitalType</span></a></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">OrbitalType.d</span></span>*, *<span class="n"><span class="pre">elements</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">SpeciesLike</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sites</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
class="reference internal"
title="pymatgen.core.sites.PeriodicSite"><span
class="pre">PeriodicSite</span></a><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">erange</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L1148-L1189"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.dos.CompleteDos.get_upper_band_edge"
class="headerlink" title="Link to this definition"></a>  
Get the orbital-projected upper band edge.

The definition by Xin et al. Phys. Rev. B, 89, 115114 (2014) is used,
which is the highest peak position of the Hilbert transform of the
orbital-projected DOS.

“elements” and “sites” cannot be used together.

Parameters<span class="colon">:</span>  
- **band** (<a href="#pymatgen.electronic_structure.core.OrbitalType"
  class="reference internal"
  title="pymatgen.electronic_structure.core.OrbitalType"><em>OrbitalType</em></a>)
  – Orbital to get the band center of (default is d-band).

- **elements** (*list\[SpeciesLike\]*) – Elements to get the band center
  of.

- **sites**
  (*list\[*<a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
  class="reference internal"
  title="pymatgen.core.sites.PeriodicSite"><em>PeriodicSite</em></a>*\]*)
  – Sites to get the band center of.

- **spin** (<a href="#pymatgen.electronic_structure.core.Spin"
  class="reference internal"
  title="pymatgen.electronic_structure.core.Spin"><em>Spin</em></a>) –
  Spin channel to use. Both spin channels will be combined by default.

- **erange** (*tuple(min,* *max)*) – The energy range to consider, with
  respect to the Fermi level. Default to None for all energies.

Returns<span class="colon">:</span>  
Upper band edge in eV, often denoted epsilon_u.

Return type<span class="colon">:</span>  
float

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">spin_polarization</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/dos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.dos.CompleteDos.spin_polarization"
class="headerlink" title="Link to this definition"></a>  
Spin polarization at Fermi level.

Examples

See Sanvito et al., DOI: 10.1126/sciadv.1602241 for an example usage.

Returns<span class="colon">:</span>  
Spin polarization in range \[0, 1\], will return NaN  
if spin polarization is ill-defined (e.g. for insulator). None if the
calculation is not spin-polarized.

Return type<span class="colon">:</span>  
float \| None

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">DOS</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">energies</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">densities</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">efermi</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L39-L170"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.DOS" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="pymatgen.core.html#pymatgen.core.spectrum.Spectrum"
class="reference internal" title="pymatgen.core.spectrum.Spectrum"><span
class="pre"><code class="sourceCode python">Spectrum</code></span></a>

(Work in progress) Replacement of basic DOS object.  
All other DOS objects are extended versions of this.

<span class="sig-name descname"><span class="pre">energies</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/dos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.DOS.energies"
class="headerlink" title="Link to this definition"></a>  
Energies.

Type<span class="colon">:</span>  
Sequence\[float\]

<span class="sig-name descname"><span class="pre">densities</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/dos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.DOS.densities"
class="headerlink" title="Link to this definition"></a>  
Spin densities, e.g. {Spin.up: DOS_up, Spin.down: DOS_down}.

Type<span class="colon">:</span>  
dict\[<a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin">Spin</a>, NDArray\]

<span class="sig-name descname"><span class="pre">efermi</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/dos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.DOS.efermi"
class="headerlink" title="Link to this definition"></a>  
The Fermi level.

Type<span class="colon">:</span>  
float

Parameters<span class="colon">:</span>  
- **energies** (*Sequence\[float\]*) – The Energies.

- **densities** (*NDArray*) – A Nx1 or Nx2 array. If former, it is
  interpreted as a Spin.up only density. Otherwise, the first column is
  interpreted as Spin.up and the other Spin.down.

- **efermi** (*float*) – The Fermi level.

<span class="sig-name descname"><span class="pre">XLABEL</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'Energy'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/dos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.DOS.XLABEL"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">YLABEL</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'Density'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/dos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.DOS.YLABEL"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">get_cbm_vbm</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.0001</span></span>*, *<span class="n"><span class="pre">abs_tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L129-L149"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.DOS.get_cbm_vbm"
class="headerlink" title="Link to this definition"></a>  
Expects a DOS object and finds the CBM and VBM eigenvalues, using
interpolation to determine the points at which the DOS crosses the
threshold tol.

tol may need to be increased for systems with noise/disorder.

Parameters<span class="colon">:</span>  
- **tol** (*float*) – Tolerance in occupations for determining the gap.

- **abs_tol** (*bool*) – Use absolute (True) or relative (False)
  tolerance.

- **spin** (<a href="#pymatgen.electronic_structure.core.Spin"
  class="reference internal"
  title="pymatgen.electronic_structure.core.Spin"><em>Spin</em></a> *\|*
  *None*) – Find the gap: - None: In the summed DOS. - Up: In the spin
  up channel. - Down: In the spin down channel.

Returns<span class="colon">:</span>  
Energies in eV corresponding to the CBM and VBM.

Return type<span class="colon">:</span>  
tuple\[float, float\]

<span class="sig-name descname"><span class="pre">get_gap</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.0001</span></span>*, *<span class="n"><span class="pre">abs_tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L151-L170"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.DOS.get_gap"
class="headerlink" title="Link to this definition"></a>  
Expects a DOS object and finds the band gap, using the determined VBM
and CBM eigenvalues.

tol may need to be increased for systems with noise/disorder.

Parameters<span class="colon">:</span>  
- **tol** (*float*) – Tolerance in occupations for determining the gap.

- **abs_tol** (*bool*) – Use absolute (True) or relative (False)
  tolerance.

- **spin** (<a href="#pymatgen.electronic_structure.core.Spin"
  class="reference internal"
  title="pymatgen.electronic_structure.core.Spin"><em>Spin</em></a> *\|*
  *None*) – Find the gap: - None: In the summed DOS. - Up: In the spin
  up channel. - Down: In the spin down channel.

Returns<span class="colon">:</span>  
Gap in eV.

Return type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">get_interpolated_gap</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.0001</span></span>*, *<span class="n"><span class="pre">abs_tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L79-L127"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.DOS.get_interpolated_gap"
class="headerlink" title="Link to this definition"></a>  
Find the interpolated band gap.

Parameters<span class="colon">:</span>  
- **tol** (*float*) – Tolerance in occupations for determining the gap.

- **abs_tol** (*bool*) – Use absolute (True) or relative (False)
  tolerance.

- **spin** (<a href="#pymatgen.electronic_structure.core.Spin"
  class="reference internal"
  title="pymatgen.electronic_structure.core.Spin"><em>Spin</em></a> *\|*
  *None*) – Find the gap: - None: In the summed DOS. - Up: In the spin
  up channel. - Down: In the spin down channel.

Returns<span class="colon">:</span>  
Energies in eV corresponding to the  
band gap, CBM and VBM.

Return type<span class="colon">:</span>  
tuple\[float, float, float\]

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Dos</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">efermi</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">energies</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">densities</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Mapping</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">ArrayLike</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">norm_vol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L173-L394"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.Dos" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Basic DOS object. All other DOS objects are extended versions of this.

<span class="sig-name descname"><span class="pre">energies</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/dos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.Dos.energies"
class="headerlink" title="Link to this definition"></a>  
Energies.

Type<span class="colon">:</span>  
Sequence\[float\]

<span class="sig-name descname"><span class="pre">densities</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/dos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.Dos.densities"
class="headerlink" title="Link to this definition"></a>  
Spin densities, e.g. {Spin.up: DOS_up, Spin.down: DOS_down}.

Type<span class="colon">:</span>  
dict\[<a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin">Spin</a>, NDArray

<span class="sig-name descname"><span class="pre">efermi</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/dos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.Dos.efermi"
class="headerlink" title="Link to this definition"></a>  
The Fermi level.

Type<span class="colon">:</span>  
float

Parameters<span class="colon">:</span>  
- **efermi** (*float*) – The Fermi level.

- **energies** (*Sequence\[float\]*) – Energies.

- **densities**
  (*dict\[*<a href="#pymatgen.electronic_structure.core.Spin"
  class="reference internal"
  title="pymatgen.electronic_structure.core.Spin"><em>Spin</em></a>*,*
  *NDArray\]*) – The density of states for each Spin.

- **norm_vol** (*float* *\|* *None*) – The volume used to normalize the
  DOS. Defaults to 1 if None which will not perform any normalization.
  If None, the result will be in unit of states/eV, otherwise will be in
  states/eV/Angstrom^3.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L386-L394"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.Dos.as_dict"
class="headerlink" title="Link to this definition"></a>  
JSON-serializable dict representation of Dos.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L377-L384"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.Dos.from_dict"
class="headerlink" title="Link to this definition"></a>  
Get Dos from a dict representation.

<span class="sig-name descname"><span class="pre">get_cbm_vbm</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.0001</span></span>*, *<span class="n"><span class="pre">abs_tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L333-L353"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.Dos.get_cbm_vbm"
class="headerlink" title="Link to this definition"></a>  
Expects a DOS object and finds the CBM and VBM eigenvalues, using
interpolation to determine the points at which the DOS crosses the
threshold tol.

tol may need to be increased for systems with noise/disorder.

Parameters<span class="colon">:</span>  
- **tol** (*float*) – Tolerance in occupations for determining the gap.

- **abs_tol** (*bool*) – Use absolute (True) or relative (False)
  tolerance.

- **spin** (<a href="#pymatgen.electronic_structure.core.Spin"
  class="reference internal"
  title="pymatgen.electronic_structure.core.Spin"><em>Spin</em></a> *\|*
  *None*) – Find the gap: None - In the summed DOS. Up - In the spin up
  channel. Down - In the spin down channel.

Returns<span class="colon">:</span>  
Energies in eV corresponding to the CBM and VBM.

Return type<span class="colon">:</span>  
tuple\[float, float\]

<span class="sig-name descname"><span class="pre">get_densities</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">NDArray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L238-L257"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.Dos.get_densities"
class="headerlink" title="Link to this definition"></a>  
Get the DOS for a particular spin.

Parameters<span class="colon">:</span>  
**spin** (<a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><em>Spin</em></a>) –
Spin.

Returns<span class="colon">:</span>  
The DOS for the particular spin. Or the sum of both spins  
if Spin is None.

Return type<span class="colon">:</span>  
NDArray

<span class="sig-name descname"><span class="pre">get_gap</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.0001</span></span>*, *<span class="n"><span class="pre">abs_tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L355-L375"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.Dos.get_gap"
class="headerlink" title="Link to this definition"></a>  
Find the band gap.

Parameters<span class="colon">:</span>  
- **tol** (*float*) – Tolerance in occupations for determining the band
  gap.

- **abs_tol** (*bool*) – Use absolute (True) or relative (False)
  tolerance.

- **spin** (<a href="#pymatgen.electronic_structure.core.Spin"
  class="reference internal"
  title="pymatgen.electronic_structure.core.Spin"><em>Spin</em></a> *\|*
  *None*) – Find the band gap: None - In the summed DOS. Up - In the
  spin up channel. Down - In the spin down channel.

Returns<span class="colon">:</span>  
Band gap in eV.

Return type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">get_interpolated_gap</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.0001</span></span>*, *<span class="n"><span class="pre">abs_tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L285-L331"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.Dos.get_interpolated_gap"
class="headerlink" title="Link to this definition"></a>  
Find the interpolated band gap.

Parameters<span class="colon">:</span>  
- **tol** (*float*) – Tolerance in occupations for determining the band
  gap.

- **abs_tol** (*bool*) – Use absolute (True) or relative (False)
  tolerance.

- **spin** (<a href="#pymatgen.electronic_structure.core.Spin"
  class="reference internal"
  title="pymatgen.electronic_structure.core.Spin"><em>Spin</em></a> *\|*
  *None*) – Find the gap: None - In the summed DOS. Up - In the spin up
  channel. Down - In the spin down channel.

Returns<span class="colon">:</span>  
Energies in eV corresponding to the  
band gap, CBM and VBM.

Return type<span class="colon">:</span>  
tuple\[float, float, float\]

<span class="sig-name descname"><span class="pre">get_interpolated_value</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">energy</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L272-L283"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.Dos.get_interpolated_value"
class="headerlink" title="Link to this definition"></a>  
Get interpolated density for a particular energy.

Parameters<span class="colon">:</span>  
**energy** (*float*) – Energy to return the density for.

Returns<span class="colon">:</span>  
Density for energy for each spin.

Return type<span class="colon">:</span>  
dict\[<a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin">Spin</a>, float\]

<span class="sig-name descname"><span class="pre">get_smeared_densities</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">sigma</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">NDArray</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L259-L270"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.Dos.get_smeared_densities"
class="headerlink" title="Link to this definition"></a>  
Get the the DOS with a Gaussian smearing.

Parameters<span class="colon">:</span>  
**sigma** (*float*) – Standard deviation of Gaussian smearing.

Returns<span class="colon">:</span>  
NDArray}: Gaussian-smeared DOS by spin.

Return type<span class="colon">:</span>  
{Spin

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">DosFingerprint</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">energies</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">np.ndarray</span></span>*, *<span class="n"><span class="pre">densities</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">np.ndarray</span></span>*, *<span class="n"><span class="pre">fp_type</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">n_bins</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">bin_width</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L624-L643"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.DosFingerprint"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`NamedTuple`</span>

Represents a Density of States (DOS) fingerprint.

This named tuple is used to store information related to the Density of
States (DOS) in a material. It includes the energies, densities, type,
number of bins, and bin width.

Parameters<span class="colon">:</span>  
- **energies** – The energy values associated with the DOS.

- **densities** – The corresponding density values for each energy.

- **fp_type** – The type of DOS fingerprint.

- **n_bins** – The number of bins used in the fingerprint.

- **bin_width** – The width of each bin in the DOS fingerprint.

Create new instance of DosFingerprint(energies, densities, fp_type,
n_bins, bin_width)

<span class="sig-name descname"><span class="pre">bin_width</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/dos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.DosFingerprint.bin_width"
class="headerlink" title="Link to this definition"></a>  
Alias for field number 4

<span class="sig-name descname"><span class="pre">densities</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ndarray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/dos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.DosFingerprint.densities"
class="headerlink" title="Link to this definition"></a>  
Alias for field number 1

<span class="sig-name descname"><span class="pre">energies</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ndarray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/dos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.DosFingerprint.energies"
class="headerlink" title="Link to this definition"></a>  
Alias for field number 0

<span class="sig-name descname"><span class="pre">fp_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/dos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.DosFingerprint.fp_type"
class="headerlink" title="Link to this definition"></a>  
Alias for field number 2

<span class="sig-name descname"><span class="pre">n_bins</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/electronic_structure/dos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.DosFingerprint.n_bins"
class="headerlink" title="Link to this definition"></a>  
Alias for field number 3

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">FermiDos</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dos</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.dos.Dos"
class="reference internal"
title="pymatgen.electronic_structure.dos.Dos"><span
class="pre">Dos</span></a></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">nelecs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">bandgap</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L397-L621"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.FermiDos" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.electronic_structure.dos.Dos"
class="reference internal"
title="pymatgen.electronic_structure.dos.Dos"><span class="pre"><code
class="sourceCode python">Dos</code></span></a>, <span
class="pre">`MSONable`</span>

Relate the density of states, doping levels (i.e. carrier
concentrations) and corresponding Fermi levels.

A negative doping concentration indicates the majority carriers are
electrons (N-type); a positive doping concentration indicates holes are
the majority carriers (P-type).

Parameters<span class="colon">:</span>  
- **dos** (<a href="#pymatgen.electronic_structure.dos.Dos"
  class="reference internal"
  title="pymatgen.electronic_structure.dos.Dos"><em>Dos</em></a>) –
  Pymatgen Dos object.

- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) – A
  structure. If None, the Structure of the Dos will be used. If the Dos
  does not have an associated Structure, an ValueError will be raised.

- **nelecs** (*float*) – The number of electrons included in the energy
  range of Dos. It is used for normalizing the DOS. Default None to the
  total number of electrons in the structure.

- **bandgap** (*float*) – If not None, the energy values are scissored
  so that the electronic band gap matches this value.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L611-L621"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.FermiDos.as_dict"
class="headerlink" title="Link to this definition"></a>  
JSON-serializable dict representation of FermiDos.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L601-L609"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.FermiDos.from_dict"
class="headerlink" title="Link to this definition"></a>  
Get FermiDos object from a dict representation.

<span class="sig-name descname"><span class="pre">get_doping</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">fermi_level</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">temperature</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L466-L495"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.FermiDos.get_doping"
class="headerlink" title="Link to this definition"></a>  
Calculate the doping (majority carrier concentration) at a given Fermi
level and temperature. A simple Left Riemann sum is used for integrating
the density of states over energy & equilibrium Fermi-Dirac
distribution.

Parameters<span class="colon">:</span>  
- **fermi_level** (*float*) – The Fermi level in eV.

- **temperature** (*float*) – The temperature in Kelvin.

Returns<span class="colon">:</span>  
The doping concentration in units of 1/cm^3. Negative values  
indicate that the majority carriers are electrons (N-type), whereas
positive values indicates the majority carriers are holes (P-type).

Return type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">get_fermi</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">concentration</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">temperature</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">rtol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.01</span></span>*, *<span class="n"><span class="pre">nstep</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">50</span></span>*, *<span class="n"><span class="pre">step</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.1</span></span>*, *<span class="n"><span class="pre">precision</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">8</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L497-L538"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.FermiDos.get_fermi"
class="headerlink" title="Link to this definition"></a>  
Find the Fermi level at which the doping concentration at the given
temperature (T) is equal to concentration. An algorithm is used where
the relative error is minimized by calculating the doping at a grid
which continually becomes finer.

Parameters<span class="colon">:</span>  
- **concentration** (*float*) – The doping concentration in 1/cm^3.
  Negative values represent N-type doping and positive values represent
  P-type.

- **temperature** (*float*) – The temperature in Kelvin.

- **rtol** (*float*) – The maximum acceptable relative error.

- **nstep** (*int*) – The number of steps checked around a given Fermi
  level.

- **step** (*float*) – The initial Energy step length when searching.

- **precision** (*int*) – The decimal places of calculated Fermi level.

Raises<span class="colon">:</span>  
**ValueError** – If the Fermi level cannot be found.

Returns<span class="colon">:</span>  
The Fermi level in eV. Note that this is different from  
the default Dos.efermi.

Return type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">get_fermi_interextrapolated</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">concentration</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">temperature</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">warn</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">c_ref</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">10000000000.0</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L540-L599"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.dos.FermiDos.get_fermi_interextrapolated"
class="headerlink" title="Link to this definition"></a>  
Similar to get_fermi method except that when it fails to converge, an
interpolated or extrapolated Fermi level is returned, with the
assumption that the Fermi level changes linearly with
log(abs(concentration)), and therefore must be used with caution.

Parameters<span class="colon">:</span>  
- **concentration** (*float*) – The doping concentration in 1/cm^3.
  Negative value represents N-type doping and positive value represents
  P-type.

- **temperature** (*float*) – The temperature in Kelvin.

- **warn** (*bool*) – Whether to give a warning the first time the Fermi
  level cannot be found.

- **c_ref** (*float*) – A doping concentration where get_fermi returns a
  value without error for both c_ref and -c_ref.

- **\*\*kwargs** – Keyword arguments passed to the get_fermi function.

Returns<span class="colon">:</span>  
The possibly interpolated or extrapolated Fermi level.

Return type<span class="colon">:</span>  
float

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">LobsterCompleteDos</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">total_dos</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.dos.Dos"
class="reference internal"
title="pymatgen.electronic_structure.dos.Dos"><span
class="pre">Dos</span></a></span>*, *<span class="n"><span class="pre">pdoss</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Mapping</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
class="reference internal"
title="pymatgen.core.sites.PeriodicSite"><span
class="pre">PeriodicSite</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Mapping</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Orbital"
class="reference internal"
title="pymatgen.electronic_structure.core.Orbital"><span
class="pre">Orbital</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Mapping</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">ArrayLike</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">normalize</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L1415-L1524"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.LobsterCompleteDos"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.electronic_structure.dos.CompleteDos"
class="reference internal"
title="pymatgen.electronic_structure.dos.CompleteDos"><span
class="pre"><code
class="sourceCode python">CompleteDos</code></span></a>

Extended CompleteDos for LOBSTER.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  Structure associated with this DOS.

- **total_dos** (<a href="#pymatgen.electronic_structure.dos.Dos"
  class="reference internal"
  title="pymatgen.electronic_structure.dos.Dos"><em>Dos</em></a>) –
  Total DOS for the structure.

- **pdoss** (*dict*) – The PDOSs supplied as {Site: {Orbital: {Spin:
  Densities}}}.

- **normalize** (*bool*) – Whether to normalize the DOS by the volume of
  the structure. If True, the units of the DOS are states/eV/Angstrom^3.
  Otherwise, the units are states/eV.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L1513-L1524"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.dos.LobsterCompleteDos.from_dict"
class="headerlink" title="Link to this definition"></a>  
Get LobsterCompleteDos from a dict representation.

<span class="sig-name descname"><span class="pre">get_element_spd_dos</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">el</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">SpeciesLike</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><a href="#pymatgen.electronic_structure.dos.Dos"
class="reference internal"
title="pymatgen.electronic_structure.dos.Dos"><span
class="pre">Dos</span></a><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L1491-L1511"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.dos.LobsterCompleteDos.get_element_spd_dos"
class="headerlink" title="Link to this definition"></a>  
Get element and s/p/d projected DOS.

Parameters<span class="colon">:</span>  
**el** (*SpeciesLike*) – Element associated with LobsterCompleteDos.

Returns<span class="colon">:</span>  
Dos, OrbitalType.p: Dos, OrbitalType.d: Dos}

Return type<span class="colon">:</span>  
dict of {OrbitalType.s

<span class="sig-name descname"><span class="pre">get_site_orbital_dos</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">site</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
class="reference internal"
title="pymatgen.core.sites.PeriodicSite"><span
class="pre">PeriodicSite</span></a></span>*, *<span class="n"><span class="pre">orbital</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.electronic_structure.dos.Dos"
class="reference internal"
title="pymatgen.electronic_structure.dos.Dos"><span
class="pre">Dos</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L1418-L1436"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.dos.LobsterCompleteDos.get_site_orbital_dos"
class="headerlink" title="Link to this definition"></a>  
Get the DOS for a particular orbital of a particular site.

Parameters<span class="colon">:</span>  
- **site**
  (<a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
  class="reference internal"
  title="pymatgen.core.sites.PeriodicSite"><em>PeriodicSite</em></a>) –
  Site in Structure associated with LobsterCompleteDos.

- **orbital** (*str*) –

  Principal quantum number and orbital, e.g. “4s”. Possible orbitals
  are: “s”, “p_y”, “p_z”, “p_x”, “d_xy”, “d_yz”, “d_z^2”,

  > <div>
  >
  > ”d_xz”, “d_x^2-y^2”, “f_y(3x^2-y^2)”, “f_xyz”, “f_yz^2”, “f_z^3”,
  > “f_xz^2”, “f_z(x^2-y^2)”, “f_x(x^2-3y^2)”.
  >
  > </div>

  In contrast to the Cohpcar and the Cohplist objects,  
  the strings from the LOBSTER files are used.

Returns<span class="colon">:</span>  
DOS of an orbital of a specific site.

Return type<span class="colon">:</span>  
<a href="#pymatgen.electronic_structure.dos.Dos"
class="reference internal"
title="pymatgen.electronic_structure.dos.Dos">Dos</a>

<span class="sig-name descname"><span class="pre">get_site_t2g_eg_resolved_dos</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">site</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
class="reference internal"
title="pymatgen.core.sites.PeriodicSite"><span
class="pre">PeriodicSite</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'e_g'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'t2g'</span></span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><a href="#pymatgen.electronic_structure.dos.Dos"
class="reference internal"
title="pymatgen.electronic_structure.dos.Dos"><span
class="pre">Dos</span></a><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L1438-L1468"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.dos.LobsterCompleteDos.get_site_t2g_eg_resolved_dos"
class="headerlink" title="Link to this definition"></a>  
Get the t2g/e_g projected DOS for a particular site.

Parameters<span class="colon">:</span>  
**site** (<a href="pymatgen.core.html#pymatgen.core.sites.PeriodicSite"
class="reference internal"
title="pymatgen.core.sites.PeriodicSite"><em>PeriodicSite</em></a>) –
Site in Structure associated with LobsterCompleteDos.

Returns<span class="colon">:</span>  
Summed e_g and t2g DOS for the site.

Return type<span class="colon">:</span>  
dict\[Literal\[“e_g”, “t2g”\], Dos\]

<span class="sig-name descname"><span class="pre">get_spd_dos</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><a href="#pymatgen.electronic_structure.dos.Dos"
class="reference internal"
title="pymatgen.electronic_structure.dos.Dos"><span
class="pre">Dos</span></a><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L1470-L1489"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.dos.LobsterCompleteDos.get_spd_dos"
class="headerlink" title="Link to this definition"></a>  
Get orbital projected DOS.

For example, if 3s and 4s are included in the basis of some element,
they will be both summed in the orbital projected DOS.

Returns<span class="colon">:</span>  
Dos}

Return type<span class="colon">:</span>  
{orbital

<!-- -->

<span class="sig-name descname"><span class="pre">add_densities</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">density1</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Mapping</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">ArrayLike</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">density2</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Mapping</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">ArrayLike</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.electronic_structure.core.Spin"
class="reference internal"
title="pymatgen.electronic_structure.core.Spin"><span
class="pre">Spin</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">NDArray</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L1527-L1540"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.add_densities"
class="headerlink" title="Link to this definition"></a>  
Sum two DOS along each spin channel.

Parameters<span class="colon">:</span>  
- **density1**
  (*dict\[*<a href="#pymatgen.electronic_structure.core.Spin"
  class="reference internal"
  title="pymatgen.electronic_structure.core.Spin"><em>Spin</em></a>*,*
  *NDArray\]*) – First DOS.

- **density2**
  (*dict\[*<a href="#pymatgen.electronic_structure.core.Spin"
  class="reference internal"
  title="pymatgen.electronic_structure.core.Spin"><em>Spin</em></a>*,*
  *NDArray\]*) – Second DOS.

Returns<span class="colon">:</span>  
dict\[Spin, NDArray\]

<!-- -->

<span class="sig-name descname"><span class="pre">f0</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">E</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">NDArray</span></span>*, *<span class="n"><span class="pre">fermi</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">T</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/dos.py#L1551-L1563"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.dos.f0" class="headerlink"
title="Link to this definition"></a>  
Fermi-Dirac distribution function.

Parameters<span class="colon">:</span>  
- **E** (*float*) – Energy in eV.

- **fermi** (*float*) – The Fermi level in eV.

- **T** (*float*) – The temperature in kelvin.

Returns<span class="colon">:</span>  
The Fermi-Dirac occupation probability at energy E.

Return type<span class="colon">:</span>  
float

</div>

<div id="module-pymatgen.electronic_structure.plotter" class="section">

<span id="pymatgen-electronic-structure-plotter-module"></span>

## pymatgen.electronic_structure.plotter module<a href="#module-pymatgen.electronic_structure.plotter"
class="headerlink" title="Link to this heading"></a>

This module implements plotter for DOS and band structure.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">BSDOSPlotter</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">bs_projection</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'elements'</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'elements'</span></span>*, *<span class="n"><span class="pre">dos_projection</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'elements'</span></span>*, *<span class="n"><span class="pre">vb_energy_range</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">4</span></span>*, *<span class="n"><span class="pre">cb_energy_range</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">4</span></span>*, *<span class="n"><span class="pre">fixed_cb_energy</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">egrid_interval</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1</span></span>*, *<span class="n"><span class="pre">font</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'Times</span> <span class="pre">New</span> <span class="pre">Roman'</span></span>*, *<span class="n"><span class="pre">axis_fontsize</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">20</span></span>*, *<span class="n"><span class="pre">tick_fontsize</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">15</span></span>*, *<span class="n"><span class="pre">legend_fontsize</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">14</span></span>*, *<span class="n"><span class="pre">bs_legend</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'best'</span></span>*, *<span class="n"><span class="pre">dos_legend</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'best'</span></span>*, *<span class="n"><span class="pre">rgb_legend</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">fig_size</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">(11,</span> <span class="pre">8.5)</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L2259-L2845"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.BSDOSPlotter"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

A joint, aligned band structure and density of states plot.
Contributions from Jan Pohls as well as the online example from Germain
Salvato-Vallverdu: <a href="https://gvallver.perso.univ-pau.fr/?p=587"
class="reference external">https://gvallver.perso.univ-pau.fr/?p=587</a>.

Instantiate plotter settings.

Parameters<span class="colon">:</span>  
- **bs_projection** (*'elements'* *\|* *None*) – Whether to project the
  bands onto elements.

- **dos_projection** (*str*) – “elements”, “orbitals”, or None

- **vb_energy_range** (*float*) – energy in eV to show of valence bands

- **cb_energy_range** (*float*) – energy in eV to show of conduction
  bands

- **fixed_cb_energy** (*bool*) – If true, the cb_energy_range will be
  interpreted as constant (i.e., no gap correction for cb energy)

- **egrid_interval** (*float*) – interval for grid marks

- **font** (*str*) – font family

- **axis_fontsize** (*float*) – font size for axis

- **tick_fontsize** (*float*) – font size for axis tick labels

- **legend_fontsize** (*float*) – font size for legends

- **bs_legend** (*str*) – matplotlib string location for legend or None

- **dos_legend** (*str*) – matplotlib string location for legend or None

- **rgb_legend** (*bool*) – (T/F) whether to draw RGB triangle/bar for
  element proj.

- **fig_size** (*tuple*) – dimensions of figure size (width, height)

<span class="sig-name descname"><span class="pre">get_plot</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">bs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a
href="#pymatgen.electronic_structure.bandstructure.BandStructureSymmLine"
class="reference internal"
title="pymatgen.electronic_structure.bandstructure.BandStructureSymmLine"><span
class="pre">BandStructureSymmLine</span></a></span>*, *<span class="n"><span class="pre">dos</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.dos.Dos"
class="reference internal"
title="pymatgen.electronic_structure.dos.Dos"><span
class="pre">Dos</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="#pymatgen.electronic_structure.dos.CompleteDos"
class="reference internal"
title="pymatgen.electronic_structure.dos.CompleteDos"><span
class="pre">CompleteDos</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">plt.Axes</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">plt.Axes</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">plt.Axes</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L2316-L2589"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.BSDOSPlotter.get_plot"
class="headerlink" title="Link to this definition"></a>  
Get a matplotlib plot object.

Parameters<span class="colon">:</span>  
- **bs** (<a
  href="#pymatgen.electronic_structure.bandstructure.BandStructureSymmLine"
  class="reference internal"
  title="pymatgen.electronic_structure.bandstructure.BandStructureSymmLine"><em>BandStructureSymmLine</em></a>)
  – the bandstructure to plot. Projection data must exist for projected
  plots.

- **dos** (<a href="#pymatgen.electronic_structure.dos.Dos"
  class="reference internal"
  title="pymatgen.electronic_structure.dos.Dos"><em>Dos</em></a>) – the
  Dos to plot. Projection data must exist (i.e., CompleteDos) for
  projected plots.

Returns<span class="colon">:</span>  
matplotlib axes for the band structure and DOS, resp.

Return type<span class="colon">:</span>  
plt.Axes \| tuple\[plt.Axes, plt.Axes\]

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">BSPlotter</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">bs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a
href="#pymatgen.electronic_structure.bandstructure.BandStructureSymmLine"
class="reference internal"
title="pymatgen.electronic_structure.bandstructure.BandStructureSymmLine"><span
class="pre">BandStructureSymmLine</span></a></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L296-L915"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.BSPlotter"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Plot or get data to facilitate the plotting of band structure.

Parameters<span class="colon">:</span>  
**bs** – A BandStructureSymmLine object.

<span class="sig-name descname"><span class="pre">add_bs</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">bs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a
href="#pymatgen.electronic_structure.bandstructure.BandStructureSymmLine"
class="reference internal"
title="pymatgen.electronic_structure.bandstructure.BandStructureSymmLine"><span
class="pre">BandStructureSymmLine</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a
href="#pymatgen.electronic_structure.bandstructure.BandStructureSymmLine"
class="reference internal"
title="pymatgen.electronic_structure.bandstructure.BandStructureSymmLine"><span
class="pre">BandStructureSymmLine</span></a><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L341-L350"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.BSPlotter.add_bs"
class="headerlink" title="Link to this definition"></a>  
Add bands objects to the BSPlotter.

<span class="sig-name descname"><span class="pre">bs_plot_data</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">zero_to_efermi</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">bs</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">bs_ref</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">split_branches</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L423-L534"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.BSPlotter.bs_plot_data"
class="headerlink" title="Link to this definition"></a>  
Get the data nicely formatted for a plot.

Parameters<span class="colon">:</span>  
- **zero_to_efermi** – Automatically set the Fermi level as the plot’s
  origin (i.e. subtract E_f). Defaults to True.

- **bs** – the bandstructure to get the data from. If not provided, the
  first one in the self.\_bs list will be used.

- **bs_ref** – is the bandstructure of reference when a rescale of the
  distances is need to plot multiple bands

- **split_branches** – if True distances and energies are split
  according to the branches. If False distances and energies are split
  only where branches are discontinuous (reducing the number of lines to
  plot).

Returns<span class="colon">:</span>  
A dictionary of the following format: ticks: A dict with the ‘distances’
at which there is a kpoint (the x axis) and the labels (None if no
label). energy: A dict storing bands for spin up and spin down data
{Spin:\[np.array(nb_bands,kpoints),…\]} as a list of discontinuous kpath
of energies. The energy of multiple continuous branches are stored
together. vbm: A list of tuples (distance,energy) marking the vbms. The
energies are shifted with respect to the Fermi level is the option has
been selected. cbm: A list of tuples (distance,energy) marking the cbms.
The energies are shifted with respect to the Fermi level is the option
has been selected. lattice: The reciprocal lattice. zero_energy: This is
the energy used as zero for the plot. band_gap:A string indicating the
band gap and its nature (empty if it’s a metal). is_metal: True if the
band structure is metallic (i.e., there is at least one band crossing
the Fermi level).

Return type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">get_plot</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">zero_to_efermi</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">ylim</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">smooth</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">vbm_cbm_marker</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">smooth_tol</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">smooth_k</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">3</span></span>*, *<span class="n"><span class="pre">smooth_np</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">100</span></span>*, *<span class="n"><span class="pre">bs_labels</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L595-L742"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.BSPlotter.get_plot"
class="headerlink" title="Link to this definition"></a>  
Get a matplotlib object for the bandstructures plot. Multiple
bandstructure objs are plotted together if they have the same high symm
path.

Parameters<span class="colon">:</span>  
- **zero_to_efermi** – Automatically set the Fermi level as the plot’s
  origin (i.e. subtract E_f). Defaults to True.

- **ylim** – Specify the y-axis (energy) limits; by default None let the
  code choose. It is vbm-4 and cbm+4 if insulator efermi-10 and
  efermi+10 if metal

- **smooth** (*bool* *or* *list(bools)*) – interpolates the bands by a
  spline cubic. A single bool values means to interpolate all the
  bandstructure objs. A list of bools allows to select the bandstructure
  obs to interpolate.

- **vbm_cbm_marker** (*bool*) – if True, a marker is added to the vbm
  and cbm.

- **smooth_tol** (*float*) – tolerance for fitting spline to band data.
  Default is None such that no tolerance will be used.

- **smooth_k** (*int*) – degree of splines 1\<k\<5

- **smooth_np** (*int*) – number of interpolated points per each branch.

- **bs_labels** – labels for each band for the plot legend.

<span class="sig-name descname"><span class="pre">get_ticks</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L774-L810"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.BSPlotter.get_ticks"
class="headerlink" title="Link to this definition"></a>  
Get all ticks and labels for a band structure plot.

Returns<span class="colon">:</span>  
A dictionary with ‘distance’: a list of distance at which ticks should
be set and ‘label’: a list of label for each of those ticks.

Return type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">get_ticks_old</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L812-L849"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.BSPlotter.get_ticks_old"
class="headerlink" title="Link to this definition"></a>  
Get all ticks and labels for a band structure plot.

Returns<span class="colon">:</span>  
A dictionary with ‘distance’: a list of distance at which ticks should
be set and ‘label’: a list of label for each of those ticks.

Return type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">plot_brillouin</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L897-L915"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.plotter.BSPlotter.plot_brillouin"
class="headerlink" title="Link to this definition"></a>  
Plot the Brillouin zone.

Returns<span class="colon">:</span>  
A matplotlib figure object with the Brillouin zone.

Return type<span class="colon">:</span>  
plt.Figure

<span class="sig-name descname"><span class="pre">plot_compare</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other_plotter</span></span>*, *<span class="n"><span class="pre">legend</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Axes</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L851-L895"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.BSPlotter.plot_compare"
class="headerlink" title="Link to this definition"></a>  
Plot two band structure for comparison. One is in red the other in blue
(no difference in spins). The two band structures need to be defined on
the same symmetry lines! and the distance between symmetry lines is the
one of the band structure used to build the BSPlotter.

Parameters<span class="colon">:</span>  
- **other_plotter** – Another band structure object defined along the
  same symmetry lines

- **legend** – True to add a legend to the plot

Returns<span class="colon">:</span>  
matplotlib Axes object with both band structures

Return type<span class="colon">:</span>  
plt.Axes

<span class="sig-name descname"><span class="pre">save_plot</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">ylim</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">zero_to_efermi</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">smooth</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L760-L772"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.BSPlotter.save_plot"
class="headerlink" title="Link to this definition"></a>  
Save matplotlib plot to a file.

Parameters<span class="colon">:</span>  
- **filename** (*str*) – Filename to write to. Must include extension to
  specify image format.

- **ylim** – Specifies the y-axis limits.

- **zero_to_efermi** – Automatically set the Fermi level as the plot’s
  origin (i.e. subtract E - E_f). Defaults to True.

- **smooth** – Cubic spline interpolation of the bands.

<span class="sig-name descname"><span class="pre">show</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">zero_to_efermi</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">ylim</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">smooth</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">smooth_tol</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L744-L758"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.BSPlotter.show"
class="headerlink" title="Link to this definition"></a>  
Show the plot using matplotlib.

Parameters<span class="colon">:</span>  
- **zero_to_efermi** – Set the Fermi level as the plot’s origin (i.e.
  subtract E_f). Defaults to True.

- **ylim** – Specify the y-axis (energy) limits; by default None let the
  code choose. It is vbm-4 and cbm+4 if insulator efermi-10 and
  efermi+10 if metal

- **smooth** – interpolates the bands by a spline cubic

- **smooth_tol** (*float*) – tolerance for fitting spline to band data.
  Default is None such that no tolerance will be used.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">BSPlotterProjected</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">bs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a
href="#pymatgen.electronic_structure.bandstructure.BandStructureSymmLine"
class="reference internal"
title="pymatgen.electronic_structure.bandstructure.BandStructureSymmLine"><span
class="pre">BandStructureSymmLine</span></a></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L918-L2256"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.BSPlotterProjected"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.electronic_structure.plotter.BSPlotter"
class="reference internal"
title="pymatgen.electronic_structure.plotter.BSPlotter"><span
class="pre"><code class="sourceCode python">BSPlotter</code></span></a>

Plot or get data to facilitate plotting of projected band structure
along orbitals, elements or sites.

Parameters<span class="colon">:</span>  
- **bs** – A BandStructureSymmLine object with projections

- **calculation.** (*e.g. from a VASP*)

<span class="sig-name descname"><span class="pre">get_elt_projected_plots</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">zero_to_efermi</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">ylim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">vbm_cbm_marker</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">band_linewidth</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1.0</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Axes</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L1098-L1194"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.plotter.BSPlotterProjected.get_elt_projected_plots"
class="headerlink" title="Link to this definition"></a>  
Generate a plot with subplots for different elements.

The blue and red colors are for spin up and spin down The size of the
dot in the plot corresponds to the value for the specific point.

Returns<span class="colon">:</span>  
2x2 array of plt.Axes with different  
subplots for each projection.

Return type<span class="colon">:</span>  
np.ndarray\[plt.Axes\]

<span class="sig-name descname"><span class="pre">get_elt_projected_plots_color</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">zero_to_efermi</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">elt_ordered</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">band_linewidth</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">3</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Axes</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L1196-L1290"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.plotter.BSPlotterProjected.get_elt_projected_plots_color"
class="headerlink" title="Link to this definition"></a>  
Generate a pyplot plot where the band structure line color depends on
the element of the band. where each element is associated with red,
green or blue.

The method can only deal with binary and ternary compounds.

Spin up and spin down are differentiated by a ‘-’ and a ‘–’ line.

Parameters<span class="colon">:</span>  
- **zero_to_efermi** – set the Fermi level as the plot’s origin (i.e.
  subtract E_f). Defaults to True.

- **elt_ordered** – A list of ordered Elements. The first one is red,
  second green, last blue.

- **band_linewidth** (*float*) – width of the line.

Raises<span class="colon">:</span>  
- **RuntimeError** – if the band structure is None.

- **ValueError** – if the number of elements is not 2 or 3.

Returns<span class="colon">:</span>  
a pyplot object

<span class="sig-name descname"><span class="pre">get_projected_plots_dots</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dictio</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">zero_to_efermi</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">ylim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">vbm_cbm_marker</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">band_linewidth</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1.0</span></span>*, *<span class="n"><span class="pre">marker_size</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">15.0</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">Axes</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L977-L1096"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.plotter.BSPlotterProjected.get_projected_plots_dots"
class="headerlink" title="Link to this definition"></a>  
Generate a plot with subplots for each element-orbital pair.

The orbitals are named as in the FATBAND file, e.g. “2p” or “2p_x”.

he blue and red colors are for spin up and spin down The size of the dot
in the plot corresponds to the value for the specific point.

Parameters<span class="colon">:</span>  
- **dictio** – The element and orbitals you want a projection on. The
  format is {Element: \[[<span id="id9"
  class="problematic">\*</span>](#id8)Orbitals\]} for instance
  {“Cu”:\[“d”, “s”\], “O”:\[“p”\]} will yield projections for Cu on d
  and s orbitals and oxygen on p.

- **zero_to_efermi** – Set the Fermi level as the plot’s origin (i.e.
  subtract E_f). Defaults to True.

- **ylim** – The y-axis limits. Defaults to None.

- **vbm_cbm_marker** (*bool*) – Add markers for the VBM and CBM.
  Defaults to False.

- **band_linewidth** (*float*) – The width of the lines. Defaults to
  1.0.

- **marker_size** (*float*) – The size of the markers. Defaults to 15.0.

Returns<span class="colon">:</span>  
plt.Axes

<span class="sig-name descname"><span class="pre">get_projected_plots_dots_patom_pmorb</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dictio</span></span>*, *<span class="n"><span class="pre">dictpa</span></span>*, *<span class="n"><span class="pre">sum_atoms</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sum_morbs</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">zero_to_efermi</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">ylim</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">vbm_cbm_marker</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">selected_branches</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">w_h\_size</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(12,</span> <span class="pre">8)</span></span>*, *<span class="n"><span class="pre">num_column</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L1582-L1764"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.plotter.BSPlotterProjected.get_projected_plots_dots_patom_pmorb"
class="headerlink" title="Link to this definition"></a>  
Return a plot composed of subplots for different atoms and orbitals
(subshell orbitals such as ‘s’, ‘p’, ‘d’ and ‘f’ defined by azimuthal
quantum numbers l = 0, 1, 2 and 3, respectively or individual orbitals
like ‘px’, ‘py’ and ‘pz’ defined by magnetic quantum numbers m = -1, 1
and 0, respectively). This is an extension of “get_projected_plots_dots”
method.

Parameters<span class="colon">:</span>  
- **dictio** – The elements and the orbitals you need to project on. The
  format is {Element:\[Orbitals\]}, for instance:
  {‘Cu’:\[‘dxy’,’s’,’px’\],’O’:\[‘px’,’py’,’pz’\]} will give projections
  for Cu on orbitals dxy, s, px and for O on orbitals px, py, pz. If you
  want to sum over all individual orbitals of subshell orbitals, for
  example, ‘px’, ‘py’ and ‘pz’ of O, just simply set
  {‘Cu’:\[‘dxy’,’s’,’px’\],’O’:\[‘p’\]} and set sum_morbs (see
  explanations below) as {‘O’:\[p\],…}. Otherwise, you will get an
  error.

- **dictpa** – The elements and their sites (defined by site numbers)
  you need to project on. The format is {Element: \[Site numbers\]}, for
  instance: {‘Cu’:\[1,5\],’O’:\[3,4\]} will give projections for Cu on
  site-1 and on site-5, O on site-3 and on site-4 in the cell. The
  correct site numbers of atoms are consistent with themselves in the
  structure computed. Normally, the structure should be totally similar
  with POSCAR file, however, sometimes VASP can rotate or translate the
  cell. Thus, it would be safe if using Vasprun class to get the
  final_structure and as a result, correct index numbers of atoms.

- **sum_atoms** – Sum projection of the similar atoms together (e.g.: Cu
  on site-1 and Cu on site-5). The format is {Element: \[Site
  numbers\]}, for instance: {‘Cu’: \[1,5\], ‘O’: \[3,4\]} means summing
  projections over Cu on site-1 and Cu on site-5 and O on site-3 and on
  site-4. If you do not want to use this functional, just turn it off by
  setting sum_atoms = None.

- **sum_morbs** – Sum projections of individual orbitals of similar
  atoms together (e.g.: ‘dxy’ and ‘dxz’). The format is {Element:
  \[individual orbitals\]}, for instance: {‘Cu’: \[‘dxy’, ‘dxz’\], ‘O’:
  \[‘px’, ‘py’\]} means summing projections over ‘dxy’ and ‘dxz’ of Cu
  and ‘px’ and ‘py’ of O. If you do not want to use this functional,
  just turn it off by setting sum_morbs = None.

- **zero_to_efermi** – Automatically set the Fermi level as the plot’s
  origin (i.e. subtract E_f). Defaults to True.

- **ylim** – The y-axis limit. Defaults to None.

- **vbm_cbm_marker** – Whether to plot points to indicate valence band
  maxima and conduction band minima positions. Defaults to False.

- **selected_branches** – The index of symmetry lines you chose for
  plotting. This can be useful when the number of symmetry lines (in
  KPOINTS file) are manny while you only want to show for certain ones.
  The format is \[index of line\], for instance: \[1, 3, 4\] means you
  just need to do projection along lines number 1, 3 and 4 while
  neglecting lines number 2 and so on. By default, this is None type and
  all symmetry lines will be plotted.

- **w_h\_size** – This variable help you to control the width and height
  of figure. By default, width = 12 and height = 8 (inches). The
  width/height ratio is kept the same for subfigures and the size of
  each depends on how many number of subfigures are plotted.

- **num_column** – This variable help you to manage how the subfigures
  are arranged in the figure by setting up the number of columns of
  subfigures. The value should be an int number. For example, num_column
  = 3 means you want to plot subfigures in 3 columns. By default,
  num_column = None and subfigures are aligned in 2 columns.

Returns<span class="colon">:</span>  
A pyplot object with different subfigures for different projections. The
blue and red colors lines are bands for spin up and spin down. The green
and cyan dots are projections for spin up and spin down. The bigger the
green or cyan dots in the projected band structures, the higher
character for the corresponding elements and orbitals. List of
individual orbitals and their numbers (set up by VASP and no special
meaning): s = 0; py = 1 pz = 2 px = 3; dxy = 4 dyz = 5 dz2 = 6 dxz = 7
dx2 = 8; f_3 = 9 f_2 = 10 f_1 = 11 f0 = 12 f1 = 13 f2 = 14 f3 = 15

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">BoltztrapPlotter</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">bz</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L2848-L3760"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Plot Boltztrap data.

Parameters<span class="colon">:</span>  
**bz** – a BoltztrapAnalyzer object.

<span class="sig-name descname"><span class="pre">plot_carriers</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">temp</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">300</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L3716-L3737"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_carriers"
class="headerlink" title="Link to this definition"></a>  
Plot the carrier concentration in function of Fermi level.

Parameters<span class="colon">:</span>  
**temp** – the temperature

Returns<span class="colon">:</span>  
a matplotlib object

<span class="sig-name descname"><span class="pre">plot_complexity_factor_mu</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">temps</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(300,)</span></span>*, *<span class="n"><span class="pre">output</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'average'</span></span>*, *<span class="n"><span class="pre">Lambda</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.5</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L2955-L3012"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_complexity_factor_mu"
class="headerlink" title="Link to this definition"></a>  
Plot respect to the chemical potential of the Fermi surface complexity
factor calculated as explained in Ref. Gibbs, Z. M. et al., Effective
mass and fermi surface complexity factor from ab initio band structure
calculations. npj Computational Materials 3, 8 (2017).

Parameters<span class="colon">:</span>  
- **output** – ‘average’ returns the complexity factor calculated using
  the average of the three diagonal components of the seebeck and
  conductivity tensors. ‘tensor’ returns the complexity factor respect
  to the three diagonal components of seebeck and conductivity tensors.

- **temps** – list of temperatures of calculated seebeck and
  conductivity.

- **Lambda** – fitting parameter used to model the scattering (0.5 means
  constant relaxation time).

Returns<span class="colon">:</span>  
a matplotlib object

<span class="sig-name descname"><span class="pre">plot_conductivity_dop</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">temps</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'all'</span></span>*, *<span class="n"><span class="pre">output</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'average'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'eigs'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'average'</span></span>*, *<span class="n"><span class="pre">relaxation_time</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1e-14</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L3474-L3530"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_conductivity_dop"
class="headerlink" title="Link to this definition"></a>  
Plot the conductivity in function of doping levels for different
temperatures.

Parameters<span class="colon">:</span>  
- **temps** – the default ‘all’ plots all the temperatures in the
  analyzer. Specify a list of temperatures if you want to plot only
  some.

- **output** – with ‘average’ you get an average of the three directions
  with ‘eigs’ you get all the three directions.

- **relaxation_time** – specify a constant relaxation time value

Returns<span class="colon">:</span>  
a matplotlib object

<span class="sig-name descname"><span class="pre">plot_conductivity_mu</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">temp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">600</span></span>*, *<span class="n"><span class="pre">output</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'eig'</span></span>*, *<span class="n"><span class="pre">relaxation_time</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-14</span></span>*, *<span class="n"><span class="pre">xlim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L3049-L3085"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_conductivity_mu"
class="headerlink" title="Link to this definition"></a>  
Plot the conductivity in function of Fermi level. Semi-log plot.

Parameters<span class="colon">:</span>  
- **temp** (*float*) – the temperature

- **output** (*str*) – “eig” or “average”

- **relaxation_time** (*float*) – A relaxation time in s. Defaults to
  1e-14 and the plot is in units of relaxation time

- **xlim** (*tuple\[float,* *float\]*) – a 2-tuple of min and max fermi
  energy. Defaults to (0, band gap)

Returns<span class="colon">:</span>  
a matplotlib object

<span class="sig-name descname"><span class="pre">plot_conductivity_temp</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">doping</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'all'</span></span>*, *<span class="n"><span class="pre">output</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'average'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'eigs'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'average'</span></span>*, *<span class="n"><span class="pre">relaxation_time</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1e-14</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L3210-L3264"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_conductivity_temp"
class="headerlink" title="Link to this definition"></a>  
Plot the conductivity in function of temperature for different doping
levels.

Parameters<span class="colon">:</span>  
- **doping** (*str*) – the default ‘all’ plots all the doping levels in
  the analyzer. Specify a list of doping levels if you want to plot only
  some.

- **output** – with ‘average’ you get an average of the three directions
  with ‘eigs’ you get all the three directions.

- **relaxation_time** – specify a constant relaxation time value

Returns<span class="colon">:</span>  
a matplotlib object

<span class="sig-name descname"><span class="pre">plot_dos</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">sigma</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.05</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L3703-L3714"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_dos"
class="headerlink" title="Link to this definition"></a>  
Plot dos.

Parameters<span class="colon">:</span>  
**sigma** – a smearing

Returns<span class="colon">:</span>  
a matplotlib object

<span class="sig-name descname"><span class="pre">plot_eff_mass_dop</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">temps</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'all'</span></span>*, *<span class="n"><span class="pre">output</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'average'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'eigs'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'average'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L3649-L3701"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_eff_mass_dop"
class="headerlink" title="Link to this definition"></a>  
Plot the average effective mass in function of doping levels for
different temperatures.

Parameters<span class="colon">:</span>  
- **temps** – the default ‘all’ plots all the temperatures in the
  analyzer. Specify a list of temperatures if you want to plot only
  some.

- **output** – with ‘average’ you get an average of the three directions
  with ‘eigs’ you get all the three directions.

- **relaxation_time** – specify a constant relaxation time value

Returns<span class="colon">:</span>  
a matplotlib object

<span class="sig-name descname"><span class="pre">plot_eff_mass_temp</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">doping</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'all'</span></span>*, *<span class="n"><span class="pre">output</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'average'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'eigs'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'average'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L3377-L3423"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_eff_mass_temp"
class="headerlink" title="Link to this definition"></a>  
Plot the average effective mass in function of temperature for different
doping levels.

Parameters<span class="colon">:</span>  
- **doping** (*str*) – the default ‘all’ plots all the doping levels in
  the analyzer. Specify a list of doping levels if you want to plot only
  some.

- **output** (*'average'* *\|* *'eigs'*) – with ‘average’ you get an
  average of the three directions with ‘eigs’ you get all the three
  directions.

Returns<span class="colon">:</span>  
a matplotlib Axes object

<span class="sig-name descname"><span class="pre">plot_hall_carriers</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">temp</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">300</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L3739-L3760"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_hall_carriers"
class="headerlink" title="Link to this definition"></a>  
Plot the Hall carrier concentration in function of Fermi level.

Parameters<span class="colon">:</span>  
**temp** – the temperature

Returns<span class="colon">:</span>  
a matplotlib object

<span class="sig-name descname"><span class="pre">plot_power_factor_dop</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">temps</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'all'</span></span>*, *<span class="n"><span class="pre">output</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'average'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'eigs'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'average'</span></span>*, *<span class="n"><span class="pre">relaxation_time</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1e-14</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L3532-L3588"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_power_factor_dop"
class="headerlink" title="Link to this definition"></a>  
Plot the Power Factor in function of doping levels for different
temperatures.

Parameters<span class="colon">:</span>  
- **temps** – the default ‘all’ plots all the temperatures in the
  analyzer. Specify a list of temperatures if you want to plot only
  some.

- **output** – with ‘average’ you get an average of the three directions
  with ‘eigs’ you get all the three directions.

- **relaxation_time** – specify a constant relaxation time value

Returns<span class="colon">:</span>  
a matplotlib object

<span class="sig-name descname"><span class="pre">plot_power_factor_mu</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">temp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">600</span></span>*, *<span class="n"><span class="pre">output</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'eig'</span></span>*, *<span class="n"><span class="pre">relaxation_time</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-14</span></span>*, *<span class="n"><span class="pre">xlim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L3087-L3124"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_power_factor_mu"
class="headerlink" title="Link to this definition"></a>  
Plot the power factor in function of Fermi level. Semi-log plot.

Parameters<span class="colon">:</span>  
- **temp** (*float*) – the temperature

- **output** (*str*) – “eig” or “average”

- **relaxation_time** (*float*) – A relaxation time in s. Defaults to
  1e-14 and the plot is in units of relaxation time

- **xlim** (*tuple\[float,* *float\]*) – a 2-tuple of min and max fermi
  energy. Defaults to (0, band gap)

Returns<span class="colon">:</span>  
a matplotlib object

<span class="sig-name descname"><span class="pre">plot_power_factor_temp</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">doping</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'all'</span></span>*, *<span class="n"><span class="pre">output</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'average'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'eigs'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'average'</span></span>*, *<span class="n"><span class="pre">relaxation_time</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1e-14</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L3266-L3319"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_power_factor_temp"
class="headerlink" title="Link to this definition"></a>  
Plot the Power Factor in function of temperature for different doping
levels.

Parameters<span class="colon">:</span>  
- **doping** (*str*) – the default ‘all’ plots all the doping levels in
  the analyzer. Specify a list of doping levels if you want to plot only
  some.

- **output** – with ‘average’ you get an average of the three directions
  with ‘eigs’ you get all the three directions.

- **relaxation_time** – specify a constant relaxation time value

Returns<span class="colon">:</span>  
a matplotlib object

<span class="sig-name descname"><span class="pre">plot_seebeck_dop</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">temps</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'all'</span></span>*, *<span class="n"><span class="pre">output</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'average'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'eigs'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'average'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L3425-L3472"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_seebeck_dop"
class="headerlink" title="Link to this definition"></a>  
Plot the Seebeck in function of doping levels for different
temperatures.

Parameters<span class="colon">:</span>  
- **temps** – the default ‘all’ plots all the temperatures in the
  analyzer. Specify a list of temperatures if you want to plot only
  some.

- **output** – with ‘average’ you get an average of the three directions
  with ‘eigs’ you get all the three directions.

Returns<span class="colon">:</span>  
a matplotlib object

<span class="sig-name descname"><span class="pre">plot_seebeck_eff_mass_mu</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">temps</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(300,)</span></span>*, *<span class="n"><span class="pre">output</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'average'</span></span>*, *<span class="n"><span class="pre">Lambda</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.5</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L2895-L2953"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_seebeck_eff_mass_mu"
class="headerlink" title="Link to this definition"></a>  
Plot respect to the chemical potential of the Seebeck effective mass
calculated as explained in Ref. Gibbs, Z. M. et al., Effective mass and
fermi surface complexity factor from ab initio band structure
calculations. npj Computational Materials 3, 8 (2017).

Parameters<span class="colon">:</span>  
- **output** – ‘average’ returns the seebeck effective mass calculated
  using the average of the three diagonal components of the seebeck
  tensor. ‘tensor’ returns the seebeck effective mass respect to the
  three diagonal components of the seebeck tensor.

- **temps** – list of temperatures of calculated seebeck.

- **Lambda** – fitting parameter used to model the scattering (0.5 means
  constant relaxation time).

Returns<span class="colon">:</span>  
a matplotlib object

<span class="sig-name descname"><span class="pre">plot_seebeck_mu</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">temp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">600</span></span>*, *<span class="n"><span class="pre">output</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'eig'</span></span>*, *<span class="n"><span class="pre">xlim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L3014-L3047"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_seebeck_mu"
class="headerlink" title="Link to this definition"></a>  
Plot the seebeck coefficient in function of Fermi level.

Parameters<span class="colon">:</span>  
- **temp** (*float*) – the temperature

- **output** (*str*) – “eig” or “average”

- **xlim** (*tuple\[float,* *float\]*) – a 2-tuple of min and max fermi
  energy. Defaults to (0, band gap)

Returns<span class="colon">:</span>  
a matplotlib object

<span class="sig-name descname"><span class="pre">plot_seebeck_temp</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">doping</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'all'</span></span>*, *<span class="n"><span class="pre">output</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'average'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'eigs'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'average'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L3163-L3208"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_seebeck_temp"
class="headerlink" title="Link to this definition"></a>  
Plot the Seebeck coefficient in function of temperature for different
doping levels.

Parameters<span class="colon">:</span>  
- **doping** (*str*) – the default ‘all’ plots all the doping levels in
  the analyzer. Specify a list of doping levels if you want to plot only
  some.

- **output** – with ‘average’ you get an average of the three directions
  with ‘eigs’ you get all the three directions.

Returns<span class="colon">:</span>  
a matplotlib object

<span class="sig-name descname"><span class="pre">plot_zt_dop</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">temps</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'all'</span></span>*, *<span class="n"><span class="pre">output</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'average'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'eigs'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'average'</span></span>*, *<span class="n"><span class="pre">relaxation_time</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1e-14</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L3590-L3647"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_zt_dop"
class="headerlink" title="Link to this definition"></a>  
Plot the figure of merit zT in function of doping levels for different
temperatures.

Parameters<span class="colon">:</span>  
- **temps** – the default ‘all’ plots all the temperatures in the
  analyzer. Specify a list of temperatures if you want to plot only
  some.

- **output** – with ‘average’ you get an average of the three directions
  with ‘eigs’ you get all the three directions.

- **relaxation_time** – specify a constant relaxation time value

Returns<span class="colon">:</span>  
a matplotlib object

<span class="sig-name descname"><span class="pre">plot_zt_mu</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">temp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">600</span></span>*, *<span class="n"><span class="pre">output</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'eig'</span></span>*, *<span class="n"><span class="pre">relaxation_time</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-14</span></span>*, *<span class="n"><span class="pre">xlim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Axes</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L3126-L3161"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_zt_mu"
class="headerlink" title="Link to this definition"></a>  
Plot the ZT as function of Fermi level.

Parameters<span class="colon">:</span>  
- **temp** (*float*) – the temperature

- **output** (*str*) – “eig” or “average”

- **relaxation_time** (*float*) – A relaxation time in s. Defaults to
  1e-14 and the plot is in units of relaxation time

- **xlim** (*tuple\[float,* *float\]*) – a 2-tuple of min and max fermi
  energy. Defaults to (0, band gap)

Returns<span class="colon">:</span>  
matplotlib axes object

Return type<span class="colon">:</span>  
plt.Axes

<span class="sig-name descname"><span class="pre">plot_zt_temp</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">doping</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'all'</span></span>*, *<span class="n"><span class="pre">output</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'average'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'eigs'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'average'</span></span>*, *<span class="n"><span class="pre">relaxation_time</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1e-14</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L3321-L3375"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.plotter.BoltztrapPlotter.plot_zt_temp"
class="headerlink" title="Link to this definition"></a>  
Plot the figure of merit zT in function of temperature for different
doping levels.

Parameters<span class="colon">:</span>  
- **doping** (*str*) – the default ‘all’ plots all the doping levels in
  the analyzer. Specify a list of doping levels if you want to plot only
  some.

- **output** – with ‘average’ you get an average of the three directions
  with ‘eigs’ you get all the three directions.

- **relaxation_time** – specify a constant relaxation time value

Raises<span class="colon">:</span>  
**ValueError** – if output is not ‘average’ or ‘eigs’

Returns<span class="colon">:</span>  
a matplotlib object

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">CohpPlotter</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">zero_at_efermi</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">are_coops</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">are_cobis</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L3763-L3990"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.CohpPlotter"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Plot crystal orbital Hamilton populations (COHPs) or crystal orbital
overlap populations (COOPs). It is modeled after the DosPlotter object.

Parameters<span class="colon">:</span>  
- **zero_at_efermi** – Whether to shift all populations to have zero
  energy at the Fermi level. Defaults to True.

- **are_coops** – Switch to indicate that these are COOPs, not COHPs.
  Defaults to False for COHPs.

- **are_cobis** – Switch to indicate that these are COBIs or
  multi-center COBIs, not COHPs/COOPs. Defaults to False for COHPs.

<span class="sig-name descname"><span class="pre">add_cohp</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">label</span></span>*, *<span class="n"><span class="pre">cohp</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L3783-L3799"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.CohpPlotter.add_cohp"
class="headerlink" title="Link to this definition"></a>  
Add a COHP for plotting.

Parameters<span class="colon">:</span>  
- **label** – Label for the COHP. Must be unique.

- **cohp** – COHP object.

<span class="sig-name descname"><span class="pre">add_cohp_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">cohp_dict</span></span>*, *<span class="n"><span class="pre">key_sort_func</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L3801-L3812"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.plotter.CohpPlotter.add_cohp_dict"
class="headerlink" title="Link to this definition"></a>  
Add a dictionary of COHPs with an optional sorting function for the
keys.

Parameters<span class="colon">:</span>  
- **cohp_dict** – dict of the form {label: Cohp}

- **key_sort_func** – function used to sort the cohp_dict keys.

<span class="sig-name descname"><span class="pre">get_cohp_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L3814-L3823"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.plotter.CohpPlotter.get_cohp_dict"
class="headerlink" title="Link to this definition"></a>  
Get the added COHPs as a json-serializable dict. Note that if you have
specified smearing for the COHP plot, the populations returned will be
the smeared and not the original populations.

Returns<span class="colon">:</span>  
Dict of COHP data of the form {label: {“efermi”: efermi, “energies”: …,
“COHP”: {Spin.up: …}, “ICOHP”: …}}.

Return type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">get_plot</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">xlim</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ylim</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">plot_negative</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">integrated</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">invert_axes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L3825-L3965"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.CohpPlotter.get_plot"
class="headerlink" title="Link to this definition"></a>  
Get a matplotlib plot showing the COHP.

Parameters<span class="colon">:</span>  
- **xlim** – Specifies the x-axis limits. Defaults to None for automatic
  determination.

- **ylim** – Specifies the y-axis limits. Defaults to None for automatic
  determination.

- **plot_negative** – It is common to plot -COHP(E) so that the sign
  means the same for COOPs and COHPs. Defaults to None for automatic
  determination: If are_coops is True, this will be set to False, else
  it will be set to True.

- **integrated** – Switch to plot ICOHPs. Defaults to False.

- **invert_axes** – Put the energies onto the y-axis, which is common in
  chemistry.

Returns<span class="colon">:</span>  
A matplotlib object.

<span class="sig-name descname"><span class="pre">save_plot</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">xlim</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ylim</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L3967-L3978"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.CohpPlotter.save_plot"
class="headerlink" title="Link to this definition"></a>  
Save matplotlib plot to a file.

Parameters<span class="colon">:</span>  
- **filename** (*str*) – File name to write to. Must include extension
  to specify image format.

- **xlim** – Specifies the x-axis limits. Defaults to None for automatic
  determination.

- **ylim** – Specifies the y-axis limits. Defaults to None for automatic
  determination.

<span class="sig-name descname"><span class="pre">show</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">xlim</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ylim</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L3980-L3990"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.CohpPlotter.show"
class="headerlink" title="Link to this definition"></a>  
Show the plot using matplotlib.

Parameters<span class="colon">:</span>  
- **xlim** – Specifies the x-axis limits. Defaults to None for automatic
  determination.

- **ylim** – Specifies the y-axis limits. Defaults to None for automatic
  determination.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">DosPlotter</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">zero_at_efermi</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">stack</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">sigma</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L52-L293"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.DosPlotter"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Plot DOS. The interface is extremely flexible given there are many
different ways in which people want to view DOS. Typical usage is:

> <div>
>
> \# Initialize plotter with some optional args. Defaults are usually
> fine plotter = PhononDosPlotter().
>
> \# Add DOS with a label plotter.add_dos(“Total DOS”, dos)
>
> \# Alternatively, you can add a dict of DOS. This is the typical form
> \# returned by CompletePhononDos.get_element_dos().
> plotter.add_dos_dict({“dos1”: dos1, “dos2”: dos2})
> plotter.add_dos_dict(complete_dos.get_spd_dos())
>
> </div>

Parameters<span class="colon">:</span>  
- **zero_at_efermi** (*bool*) – Whether to shift all Dos to have zero
  energy at the fermi energy. Defaults to True.

- **stack** (*bool*) – Whether to plot the DOS as a stacked area graph

- **sigma** (*float*) – Specify a standard deviation for Gaussian
  smearing the DOS for nicer looking plots. Defaults to None for no
  smearing.

<span class="sig-name descname"><span class="pre">add_dos</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">dos</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.electronic_structure.dos.Dos"
class="reference internal"
title="pymatgen.electronic_structure.dos.Dos"><span
class="pre">Dos</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L95-L111"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.DosPlotter.add_dos"
class="headerlink" title="Link to this definition"></a>  
Add a DOS for plotting.

Parameters<span class="colon">:</span>  
- **label** – a unique label for the DOS.

- **dos** – Dos object

<span class="sig-name descname"><span class="pre">add_dos_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dos_dict</span></span>*, *<span class="n"><span class="pre">key_sort_func</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L113-L123"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.DosPlotter.add_dos_dict"
class="headerlink" title="Link to this definition"></a>  
Add a dictionary of DOSs, with an optional sorting function for the
keys.

Parameters<span class="colon">:</span>  
- **dos_dict** – dict of {label: Dos}

- **key_sort_func** – function used to sort the dos_dict keys.

<span class="sig-name descname"><span class="pre">get_dos_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L125-L134"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.DosPlotter.get_dos_dict"
class="headerlink" title="Link to this definition"></a>  
Get the added doses as a json-serializable dict. Note that if you have
specified smearing for the DOS plot, the densities returned will be the
smeared densities, not the original densities.

Returns<span class="colon">:</span>  
Dict of dos data. Generally of the form {label: {‘energies’:…,
‘densities’: {‘up’:…}, ‘efermi’:efermi}}

Return type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">get_plot</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">xlim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ylim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">invert_axes</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">beta_dashed</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Axes</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L136-L264"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.DosPlotter.get_plot"
class="headerlink" title="Link to this definition"></a>  
Get a matplotlib plot showing the DOS.

Parameters<span class="colon">:</span>  
- **xlim** (*tuple\[float,* *float\]*) – The energy axis limits.
  Defaults to None for automatic determination.

- **ylim** (*tuple\[float,* *float\]*) – The y-axis limits. Defaults to
  None for automatic determination.

- **invert_axes** (*bool*) – Whether to invert the x and y axes. Enables
  chemist style DOS plotting. Defaults to False.

- **beta_dashed** (*bool*) – Plots the beta spin channel with a dashed
  line. Defaults to False.

Returns<span class="colon">:</span>  
matplotlib Axes object.

Return type<span class="colon">:</span>  
plt.Axes

<span class="sig-name descname"><span class="pre">save_plot</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">xlim</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ylim</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">invert_axes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">beta_dashed</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L266-L279"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.DosPlotter.save_plot"
class="headerlink" title="Link to this definition"></a>  
Save matplotlib plot to a file.

Parameters<span class="colon">:</span>  
- **filename** (*str*) – Filename to write to. Must include extension to
  specify image format.

- **xlim** – Specifies the x-axis limits. Set to None for automatic
  determination.

- **ylim** – Specifies the y-axis limits.

- **invert_axes** (*bool*) – Whether to invert the x and y axes. Enables
  chemist style DOS plotting. Defaults to False.

- **beta_dashed** (*bool*) – Plots the beta spin channel with a dashed
  line. Defaults to False.

<span class="sig-name descname"><span class="pre">show</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">xlim</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ylim</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">invert_axes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">beta_dashed</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L281-L293"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.DosPlotter.show"
class="headerlink" title="Link to this definition"></a>  
Show the plot using matplotlib.

Parameters<span class="colon">:</span>  
- **xlim** – Specifies the x-axis limits. Set to None for automatic
  determination.

- **ylim** – Specifies the y-axis limits.

- **invert_axes** (*bool*) – Whether to invert the x and y axes. Enables
  chemist style DOS plotting. Defaults to False.

- **beta_dashed** (*bool*) – Plots the beta spin channel with a dashed
  line. Defaults to False.

<!-- -->

<span class="sig-name descname"><span class="pre">fold_point</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">p</span></span>*, *<span class="n"><span class="pre">lattice</span></span>*, *<span class="n"><span class="pre">coords_are_cartesian</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L4324-L4355"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.fold_point"
class="headerlink" title="Link to this definition"></a>  
Folds a point with coordinates p inside the first Brillouin zone of the
lattice.

Parameters<span class="colon">:</span>  
- **p** – coordinates of one point

- **lattice** – Lattice object used to convert from reciprocal to
  Cartesian coordinates

- **coords_are_cartesian** – Set to True if you are providing
  coordinates in Cartesian coordinates. Defaults to False.

Returns<span class="colon">:</span>  
The Cartesian coordinates folded inside the first Brillouin zone

<!-- -->

<span class="sig-name descname"><span class="pre">plot_brillouin_zone</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">bz_lattice</span></span>*, *<span class="n"><span class="pre">lines</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">labels</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">kpoints</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">fold</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">coords_are_cartesian</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">ax</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Axes</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../util/plotting.py#L4425-L4486"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.plot_brillouin_zone"
class="headerlink" title="Link to this definition"></a>  
Plots a 3D representation of the Brillouin zone of the structure. Can
add to the plot paths, labels and kpoints.

Parameters<span class="colon">:</span>  
- **bz_lattice** – Lattice object of the Brillouin zone

- **lines** – list of lists of coordinates. Each list represent a
  different path

- **labels** – dict containing the label as a key and the coordinates as
  value.

- **kpoints** – list of coordinates

- **fold** – whether the points should be folded inside the first
  Brillouin Zone. Defaults to False. Requires lattice if True.

- **coords_are_cartesian** – Set to True if you are providing
  coordinates in Cartesian coordinates. Defaults to False.

- **ax** – matplotlib Axes or None if a new figure should be created.

- **kwargs** – provided by add_fig_kwargs decorator

Returns<span class="colon">:</span>  
matplotlib figure

Keyword arguments controlling the display of the figure:

| kwargs       | Meaning                                                                                           |
|--------------|---------------------------------------------------------------------------------------------------|
| title        | Title of the plot (Default: None).                                                                |
| show         | True to show the figure (default: True).                                                          |
| savefig      | ”abc.png” or “abc.eps” to save the figure to a file.                                              |
| size_kwargs  | Dictionary with options passed to fig.set_size_inches e.g. size_kwargs=dict(w=3, h=4)             |
| tight_layout | True to call fig.tight_layout (default: False)                                                    |
| ax_grid      | True (False) to add (remove) grid from all axes in fig. Default: None i.e. fig is left unchanged. |
| ax_annotate  | Add labels to subplots e.g. (a), (b). Default: False                                              |
| fig_close    | Close figure. Default: False.                                                                     |

<!-- -->

<span class="sig-name descname"><span class="pre">plot_brillouin_zone_from_kpath</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">kpath</span></span>*, *<span class="n"><span class="pre">ax</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Axes</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Axes</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../util/plotting.py#L4402-L4422"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.electronic_structure.plotter.plot_brillouin_zone_from_kpath"
class="headerlink" title="Link to this definition"></a>  
Get the plot (as a matplotlib object) of the symmetry line path in  
the Brillouin Zone.

Parameters<span class="colon">:</span>  
- **kpath** (<a
  href="pymatgen.symmetry.html#pymatgen.symmetry.bandstructure.HighSymmKpath"
  class="reference internal"
  title="pymatgen.symmetry.bandstructure.HighSymmKpath"><em>HighSymmKpath</em></a>)
  – a HighSymmKPath object

- **ax** – matplotlib Axes or None if a new figure should be created.

- **\*\*kwargs** – provided by add_fig_kwargs decorator

Returns<span class="colon">:</span>  
matplotlib Axes

Keyword arguments controlling the display of the figure:

| kwargs       | Meaning                                                                                           |
|--------------|---------------------------------------------------------------------------------------------------|
| title        | Title of the plot (Default: None).                                                                |
| show         | True to show the figure (default: True).                                                          |
| savefig      | ”abc.png” or “abc.eps” to save the figure to a file.                                              |
| size_kwargs  | Dictionary with options passed to fig.set_size_inches e.g. size_kwargs=dict(w=3, h=4)             |
| tight_layout | True to call fig.tight_layout (default: False)                                                    |
| ax_grid      | True (False) to add (remove) grid from all axes in fig. Default: None i.e. fig is left unchanged. |
| ax_annotate  | Add labels to subplots e.g. (a), (b). Default: False                                              |
| fig_close    | Close figure. Default: False.                                                                     |

Return type<span class="colon">:</span>  
plt.Axes

<!-- -->

<span class="sig-name descname"><span class="pre">plot_ellipsoid</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">hessian</span></span>*, *<span class="n"><span class="pre">center</span></span>*, *<span class="n"><span class="pre">lattice</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">rescale</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1.0</span></span>*, *<span class="n"><span class="pre">ax</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Axes</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">coords_are_cartesian</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">arrows</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L4489-L4576"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.plot_ellipsoid"
class="headerlink" title="Link to this definition"></a>  
Plots a 3D ellipsoid rappresenting the Hessian matrix in input. Useful
to get a graphical visualization of the effective mass of a band in a
single k-point.

Parameters<span class="colon">:</span>  
- **hessian** – the Hessian matrix

- **center** – the center of the ellipsoid in reciprocal coords
  (Default)

- **lattice** – Lattice object of the Brillouin zone

- **rescale** – factor for size scaling of the ellipsoid

- **ax** – matplotlib Axes or None if a new figure should be created.

- **coords_are_cartesian** – Set to True if you are providing a center
  in Cartesian coordinates. Defaults to False.

- **arrows** – whether to plot arrows for the principal axes of the
  ellipsoid. Defaults to False.

- **\*\*kwargs** – passed to the matplotlib function ‘plot_wireframe’.
  Color defaults to blue, rstride and cstride default to 4, alpha
  defaults to 0.2.

Returns<span class="colon">:</span>  
matplotlib figure and matplotlib ax

Example of use:  
fig,ax=plot_wigner_seitz(struct.reciprocal_lattice)
plot_ellipsoid(hessian,\[0.0,0.0,0.0\], struct.reciprocal_lattice,ax=ax)

<!-- -->

<span class="sig-name descname"><span class="pre">plot_fermi_surface</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">data</span></span>*, *<span class="n"><span class="pre">structure</span></span>*, *<span class="n"><span class="pre">cbm</span></span>*, *<span class="n"><span class="pre">energy_levels</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">multiple_figure</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">mlab_figure</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">kpoints_dict</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">colors</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">transparency_factor</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">labels_scale_factor</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.05</span></span>*, *<span class="n"><span class="pre">points_scale_factor</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.02</span></span>*, *<span class="n"><span class="pre">interactive</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../../../.venv/lib/python3.11/site-packages/monty/dev.py#L3993-L4178"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.plot_fermi_surface"
class="headerlink" title="Link to this definition"></a>  
Plot the Fermi surface at specific energy value using Boltztrap 1 FERMI
mode.

The easiest way to use this plotter is:

> <div>
>
> 1.  Run boltztrap in ‘FERMI’ mode using BoltztrapRunner,
>
> 2.  Load BoltztrapAnalyzer using your method of choice (e.g.,
>     from_files)
>
> 3.  Pass in your BoltztrapAnalyzer’s fermi_surface_data as this  
>     function’s data argument.
>
> </div>

Parameters<span class="colon">:</span>  
- **data** – energy values in a 3D grid from a CUBE file via
  read_cube_file function, or from a
  BoltztrapAnalyzer.fermi_surface_data

- **structure** – structure object of the material

- **energy_levels** (*\[float\]*) – Energy values for plotting the fermi
  surface(s) By default 0 eV correspond to the VBM, as in the plot of
  band structure along symmetry line. Default: One surface, with max
  energy value + 0.01 eV

- **cbm** (*bool*) – True if the considered band is a conduction band or
  not.

- **multiple_figure** (*bool*) – If True a figure for each energy level
  will be shown. If False all the surfaces will be shown in the same
  figure. In this last case, tune the transparency factor.

- **mlab_figure** (*mayavi.mlab.figure*) – A previous figure to plot a
  new surface on.

- **kpoints_dict** (*dict*) – dictionary of kpoints to label in the
  plot. Example: {“K”:\[0.5,0.0,0.5\]}, coords are fractional

- **colors** (*\[tuple\]*) – Iterable of 3-tuples (r,g,b) of integers to
  define the colors of each surface (one per energy level). Should be
  the same length as the number of surfaces being plotted. Example (3
  surfaces): colors=\[(1,0,0), (0,1,0), (0,0,1)\] Example (2 surfaces):
  colors=\[(0, 0.5, 0.5)\]

- **transparency_factor** (*float*) – Values in the range \[0,1\] to
  tune the opacity of each surface. Should be one transparency_factor
  per surface.

- **labels_scale_factor** (*float*) – factor to tune size of the kpoint
  labels

- **points_scale_factor** (*float*) – factor to tune size of the kpoint
  points

- **interactive** (*bool*) – if True an interactive figure will be
  shown. If False a non interactive figure will be shown, but it is
  possible to plot other surfaces on the same figure. To make it
  interactive, run mlab.show().

Returns<span class="colon">:</span>  
The mlab plotter and an interactive  
figure to control the plot.

Return type<span class="colon">:</span>  
tuple\[mlab.figure, mlab\]

Note: Experimental.  
Please, double check the surface shown by using some other software and
report issues.

<!-- -->

<span class="sig-name descname"><span class="pre">plot_labels</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">labels</span></span>*, *<span class="n"><span class="pre">lattice</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">coords_are_cartesian</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">ax</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Axes</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L4278-L4321"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.plot_labels"
class="headerlink" title="Link to this definition"></a>  
Add labels to a matplotlib Axes.

Parameters<span class="colon">:</span>  
- **labels** – dict containing the label as a key and the coordinates as
  value.

- **lattice** – Lattice object used to convert from reciprocal to
  Cartesian coordinates

- **coords_are_cartesian** – Set to True if you are providing.
  coordinates in Cartesian coordinates. Defaults to False. Requires
  lattice if False.

- **ax** – matplotlib Axes or None if a new figure should be created.

- **kwargs** – kwargs passed to the matplotlib function ‘text’. Color
  defaults to blue and size to 25.

Returns<span class="colon">:</span>  
matplotlib figure and matplotlib ax

<!-- -->

<span class="sig-name descname"><span class="pre">plot_lattice_vectors</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">lattice</span></span>*, *<span class="n"><span class="pre">ax</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Axes</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L4212-L4239"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.plot_lattice_vectors"
class="headerlink" title="Link to this definition"></a>  
Add the basis vectors of the lattice provided to a matplotlib Axes.

Parameters<span class="colon">:</span>  
- **lattice** – Lattice object

- **ax** – matplotlib Axes or None if a new figure should be created.

- **kwargs** – kwargs passed to the matplotlib function ‘plot’. Color
  defaults to green and linewidth to 3.

Returns<span class="colon">:</span>  
matplotlib figure and matplotlib ax

<!-- -->

<span class="sig-name descname"><span class="pre">plot_path</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">line</span></span>*, *<span class="n"><span class="pre">lattice</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">coords_are_cartesian</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">ax</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Axes</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L4242-L4275"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.plot_path"
class="headerlink" title="Link to this definition"></a>  
Add a line passing through the coordinates listed in ‘line’ to a
matplotlib Axes.

Parameters<span class="colon">:</span>  
- **line** – list of coordinates.

- **lattice** – Lattice object used to convert from reciprocal to
  Cartesian coordinates

- **coords_are_cartesian** – Set to True if you are providing
  coordinates in Cartesian coordinates. Defaults to False. Requires
  lattice if False.

- **ax** – matplotlib Axes or None if a new figure should be created.

- **kwargs** – kwargs passed to the matplotlib function ‘plot’. Color
  defaults to red and linewidth to 3.

Returns<span class="colon">:</span>  
matplotlib figure and matplotlib ax

<!-- -->

<span class="sig-name descname"><span class="pre">plot_points</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">points</span></span>*, *<span class="n"><span class="pre">lattice</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">coords_are_cartesian</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">fold</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">ax</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Axes</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L4358-L4399"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.plot_points"
class="headerlink" title="Link to this definition"></a>  
Add Points to a matplotlib Axes.

Parameters<span class="colon">:</span>  
- **points** – list of coordinates

- **lattice** – Lattice object used to convert from reciprocal to
  Cartesian coordinates

- **coords_are_cartesian** – Set to True if you are providing
  coordinates in Cartesian coordinates. Defaults to False. Requires
  lattice if False.

- **fold** – whether the points should be folded inside the first
  Brillouin Zone. Defaults to False. Requires lattice if True.

- **ax** – matplotlib Axes or None if a new figure should be created.

- **kwargs** – kwargs passed to the matplotlib function ‘scatter’. Color
  defaults to blue

Returns<span class="colon">:</span>  
matplotlib figure and matplotlib ax

<!-- -->

<span class="sig-name descname"><span class="pre">plot_wigner_seitz</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">lattice</span></span>*, *<span class="n"><span class="pre">ax</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Axes</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../electronic_structure/plotter.py#L4181-L4209"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.electronic_structure.plotter.plot_wigner_seitz"
class="headerlink" title="Link to this definition"></a>  
Add the skeleton of the Wigner-Seitz cell of the lattice to a matplotlib
Axes.

Parameters<span class="colon">:</span>  
- **lattice** – Lattice object

- **ax** – matplotlib Axes or None if a new figure should be created.

- **kwargs** – kwargs passed to the matplotlib function ‘plot’. Color
  defaults to black and linewidth to 1.

Returns<span class="colon">:</span>  
matplotlib figure and matplotlib ax

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
