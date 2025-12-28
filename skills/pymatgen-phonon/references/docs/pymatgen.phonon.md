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

- <a href="#" class="reference internal">pymatgen.phonon package</a>
  - <a href="#submodules" class="reference internal">Submodules</a>
  - <a href="#module-pymatgen.phonon.bandstructure"
    class="reference internal">pymatgen.phonon.bandstructure module</a>
    - <a href="#pymatgen.phonon.bandstructure.PhononBandStructure"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">PhononBandStructure</code></span></a>
      - <a href="#pymatgen.phonon.bandstructure.PhononBandStructure.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBandStructure.as_dict()</code></span></a>
      - <a
        href="#pymatgen.phonon.bandstructure.PhononBandStructure.asr_breaking"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBandStructure.asr_breaking()</code></span></a>
      - <a href="#pymatgen.phonon.bandstructure.PhononBandStructure.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBandStructure.from_dict()</code></span></a>
      - <a
        href="#pymatgen.phonon.bandstructure.PhononBandStructure.get_gamma_point"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBandStructure.get_gamma_point()</code></span></a>
      - <a
        href="#pymatgen.phonon.bandstructure.PhononBandStructure.get_nac_eigendisplacements_along_dir"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBandStructure.get_nac_eigendisplacements_along_dir()</code></span></a>
      - <a
        href="#pymatgen.phonon.bandstructure.PhononBandStructure.get_nac_frequencies_along_dir"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBandStructure.get_nac_frequencies_along_dir()</code></span></a>
      - <a
        href="#pymatgen.phonon.bandstructure.PhononBandStructure.has_eigendisplacements"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBandStructure.has_eigendisplacements</code></span></a>
      - <a
        href="#pymatgen.phonon.bandstructure.PhononBandStructure.has_imaginary_freq"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBandStructure.has_imaginary_freq()</code></span></a>
      - <a
        href="#pymatgen.phonon.bandstructure.PhononBandStructure.has_imaginary_gamma_freq"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBandStructure.has_imaginary_gamma_freq()</code></span></a>
      - <a href="#pymatgen.phonon.bandstructure.PhononBandStructure.has_nac"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBandStructure.has_nac</code></span></a>
      - <a href="#pymatgen.phonon.bandstructure.PhononBandStructure.max_freq"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBandStructure.max_freq()</code></span></a>
      - <a href="#pymatgen.phonon.bandstructure.PhononBandStructure.min_freq"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBandStructure.min_freq()</code></span></a>
      - <a href="#pymatgen.phonon.bandstructure.PhononBandStructure.width"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBandStructure.width()</code></span></a>
    - <a href="#pymatgen.phonon.bandstructure.PhononBandStructureSymmLine"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">PhononBandStructureSymmLine</code></span></a>
      - <a
        href="#pymatgen.phonon.bandstructure.PhononBandStructureSymmLine.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBandStructureSymmLine.as_dict()</code></span></a>
      - <a
        href="#pymatgen.phonon.bandstructure.PhononBandStructureSymmLine.as_phononwebsite"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBandStructureSymmLine.as_phononwebsite()</code></span></a>
      - <a
        href="#pymatgen.phonon.bandstructure.PhononBandStructureSymmLine.band_reorder"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBandStructureSymmLine.band_reorder()</code></span></a>
      - <a
        href="#pymatgen.phonon.bandstructure.PhononBandStructureSymmLine.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBandStructureSymmLine.from_dict()</code></span></a>
      - <a
        href="#pymatgen.phonon.bandstructure.PhononBandStructureSymmLine.get_branch"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBandStructureSymmLine.get_branch()</code></span></a>
      - <a
        href="#pymatgen.phonon.bandstructure.PhononBandStructureSymmLine.get_equivalent_qpoints"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBandStructureSymmLine.get_equivalent_qpoints()</code></span></a>
      - <a
        href="#pymatgen.phonon.bandstructure.PhononBandStructureSymmLine.write_phononwebsite"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBandStructureSymmLine.write_phononwebsite()</code></span></a>
    - <a href="#pymatgen.phonon.bandstructure.eigenvectors_from_displacements"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">eigenvectors_from_displacements()</code></span></a>
    - <a href="#pymatgen.phonon.bandstructure.estimate_band_connection"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">estimate_band_connection()</code></span></a>
    - <a href="#pymatgen.phonon.bandstructure.get_reasonable_repetitions"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">get_reasonable_repetitions()</code></span></a>
  - <a href="#module-pymatgen.phonon.dos"
    class="reference internal">pymatgen.phonon.dos module</a>
    - <a href="#pymatgen.phonon.dos.CompletePhononDos"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">CompletePhononDos</code></span></a>
      - <a href="#pymatgen.phonon.dos.CompletePhononDos.pdos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompletePhononDos.pdos</code></span></a>
      - <a href="#pymatgen.phonon.dos.CompletePhononDos.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompletePhononDos.as_dict()</code></span></a>
      - <a href="#pymatgen.phonon.dos.CompletePhononDos.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompletePhononDos.from_dict()</code></span></a>
      - <a href="#pymatgen.phonon.dos.CompletePhononDos.get_element_dos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompletePhononDos.get_element_dos()</code></span></a>
      - <a href="#pymatgen.phonon.dos.CompletePhononDos.get_site_dos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">CompletePhononDos.get_site_dos()</code></span></a>
    - <a href="#pymatgen.phonon.dos.PhononDos"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">PhononDos</code></span></a>
      - <a href="#pymatgen.phonon.dos.PhononDos.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononDos.as_dict()</code></span></a>
      - <a href="#pymatgen.phonon.dos.PhononDos.cv"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononDos.cv()</code></span></a>
      - <a href="#pymatgen.phonon.dos.PhononDos.entropy"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononDos.entropy()</code></span></a>
      - <a href="#pymatgen.phonon.dos.PhononDos.fp_to_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononDos.fp_to_dict()</code></span></a>
      - <a href="#pymatgen.phonon.dos.PhononDos.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononDos.from_dict()</code></span></a>
      - <a href="#pymatgen.phonon.dos.PhononDos.get_dos_fp"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononDos.get_dos_fp()</code></span></a>
      - <a href="#pymatgen.phonon.dos.PhononDos.get_dos_fp_similarity"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononDos.get_dos_fp_similarity()</code></span></a>
      - <a href="#pymatgen.phonon.dos.PhononDos.get_interpolated_value"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononDos.get_interpolated_value()</code></span></a>
      - <a href="#pymatgen.phonon.dos.PhononDos.get_last_peak"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononDos.get_last_peak()</code></span></a>
      - <a href="#pymatgen.phonon.dos.PhononDos.get_smeared_densities"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononDos.get_smeared_densities()</code></span></a>
      - <a href="#pymatgen.phonon.dos.PhononDos.helmholtz_free_energy"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononDos.helmholtz_free_energy()</code></span></a>
      - <a href="#pymatgen.phonon.dos.PhononDos.ind_zero_freq"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononDos.ind_zero_freq()</code></span></a>
      - <a href="#pymatgen.phonon.dos.PhononDos.internal_energy"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononDos.internal_energy()</code></span></a>
      - <a href="#pymatgen.phonon.dos.PhononDos.mae"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononDos.mae()</code></span></a>
      - <a href="#pymatgen.phonon.dos.PhononDos.r2_score"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononDos.r2_score()</code></span></a>
      - <a href="#pymatgen.phonon.dos.PhononDos.zero_point_energy"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononDos.zero_point_energy()</code></span></a>
    - <a href="#pymatgen.phonon.dos.PhononDosFingerprint"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">PhononDosFingerprint</code></span></a>
      - <a href="#pymatgen.phonon.dos.PhononDosFingerprint.bin_width"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononDosFingerprint.bin_width</code></span></a>
      - <a href="#pymatgen.phonon.dos.PhononDosFingerprint.densities"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononDosFingerprint.densities</code></span></a>
      - <a href="#pymatgen.phonon.dos.PhononDosFingerprint.frequencies"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononDosFingerprint.frequencies</code></span></a>
      - <a href="#pymatgen.phonon.dos.PhononDosFingerprint.n_bins"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononDosFingerprint.n_bins</code></span></a>
  - <a href="#module-pymatgen.phonon.gruneisen"
    class="reference internal">pymatgen.phonon.gruneisen module</a>
    - <a href="#pymatgen.phonon.gruneisen.GruneisenParameter"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">GruneisenParameter</code></span></a>
      - <a
        href="#pymatgen.phonon.gruneisen.GruneisenParameter.acoustic_debye_temp"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GruneisenParameter.acoustic_debye_temp</code></span></a>
      - <a
        href="#pymatgen.phonon.gruneisen.GruneisenParameter.average_gruneisen"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GruneisenParameter.average_gruneisen()</code></span></a>
      - <a href="#pymatgen.phonon.gruneisen.GruneisenParameter.debye_temp_limit"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GruneisenParameter.debye_temp_limit</code></span></a>
      - <a
        href="#pymatgen.phonon.gruneisen.GruneisenParameter.debye_temp_phonopy"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GruneisenParameter.debye_temp_phonopy()</code></span></a>
      - <a href="#pymatgen.phonon.gruneisen.GruneisenParameter.phdos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GruneisenParameter.phdos</code></span></a>
      - <a href="#pymatgen.phonon.gruneisen.GruneisenParameter.tdos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GruneisenParameter.tdos</code></span></a>
      - <a
        href="#pymatgen.phonon.gruneisen.GruneisenParameter.thermal_conductivity_slack"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GruneisenParameter.thermal_conductivity_slack()</code></span></a>
    - <a href="#pymatgen.phonon.gruneisen.GruneisenPhononBandStructure"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">GruneisenPhononBandStructure</code></span></a>
      - <a
        href="#pymatgen.phonon.gruneisen.GruneisenPhononBandStructure.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GruneisenPhononBandStructure.as_dict()</code></span></a>
      - <a
        href="#pymatgen.phonon.gruneisen.GruneisenPhononBandStructure.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GruneisenPhononBandStructure.from_dict()</code></span></a>
    - <a
      href="#pymatgen.phonon.gruneisen.GruneisenPhononBandStructureSymmLine"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">GruneisenPhononBandStructureSymmLine</code></span></a>
      - <a
        href="#pymatgen.phonon.gruneisen.GruneisenPhononBandStructureSymmLine.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GruneisenPhononBandStructureSymmLine.from_dict()</code></span></a>
  - <a href="#module-pymatgen.phonon.ir_spectra"
    class="reference internal">pymatgen.phonon.ir_spectra module</a>
    - <a href="#pymatgen.phonon.ir_spectra.IRDielectricTensor"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">IRDielectricTensor</code></span></a>
      - <a href="#pymatgen.phonon.ir_spectra.IRDielectricTensor.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IRDielectricTensor.as_dict()</code></span></a>
      - <a href="#pymatgen.phonon.ir_spectra.IRDielectricTensor.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IRDielectricTensor.from_dict()</code></span></a>
      - <a href="#pymatgen.phonon.ir_spectra.IRDielectricTensor.get_ir_spectra"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IRDielectricTensor.get_ir_spectra()</code></span></a>
      - <a href="#pymatgen.phonon.ir_spectra.IRDielectricTensor.get_plotter"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IRDielectricTensor.get_plotter()</code></span></a>
      - <a href="#pymatgen.phonon.ir_spectra.IRDielectricTensor.get_spectrum"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IRDielectricTensor.get_spectrum()</code></span></a>
      - <a href="#pymatgen.phonon.ir_spectra.IRDielectricTensor.max_phfreq"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IRDielectricTensor.max_phfreq</code></span></a>
      - <a href="#pymatgen.phonon.ir_spectra.IRDielectricTensor.nph_freqs"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IRDielectricTensor.nph_freqs</code></span></a>
      - <a href="#pymatgen.phonon.ir_spectra.IRDielectricTensor.plot"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IRDielectricTensor.plot()</code></span></a>
      - <a href="#pymatgen.phonon.ir_spectra.IRDielectricTensor.write_json"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IRDielectricTensor.write_json()</code></span></a>
  - <a href="#module-pymatgen.phonon.plotter"
    class="reference internal">pymatgen.phonon.plotter module</a>
    - <a href="#pymatgen.phonon.plotter.FreqUnits"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">FreqUnits</code></span></a>
      - <a href="#pymatgen.phonon.plotter.FreqUnits.factor"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">FreqUnits.factor</code></span></a>
      - <a href="#pymatgen.phonon.plotter.FreqUnits.label"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">FreqUnits.label</code></span></a>
    - <a href="#pymatgen.phonon.plotter.GruneisenPhononBSPlotter"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">GruneisenPhononBSPlotter</code></span></a>
      - <a href="#pymatgen.phonon.plotter.GruneisenPhononBSPlotter.bs_plot_data"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GruneisenPhononBSPlotter.bs_plot_data()</code></span></a>
      - <a href="#pymatgen.phonon.plotter.GruneisenPhononBSPlotter.get_plot_gs"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GruneisenPhononBSPlotter.get_plot_gs()</code></span></a>
      - <a
        href="#pymatgen.phonon.plotter.GruneisenPhononBSPlotter.plot_compare_gs"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GruneisenPhononBSPlotter.plot_compare_gs()</code></span></a>
      - <a href="#pymatgen.phonon.plotter.GruneisenPhononBSPlotter.save_plot_gs"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GruneisenPhononBSPlotter.save_plot_gs()</code></span></a>
      - <a href="#pymatgen.phonon.plotter.GruneisenPhononBSPlotter.show_gs"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GruneisenPhononBSPlotter.show_gs()</code></span></a>
    - <a href="#pymatgen.phonon.plotter.GruneisenPlotter"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">GruneisenPlotter</code></span></a>
      - <a href="#pymatgen.phonon.plotter.GruneisenPlotter.get_plot"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GruneisenPlotter.get_plot()</code></span></a>
      - <a href="#pymatgen.phonon.plotter.GruneisenPlotter.save_plot"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GruneisenPlotter.save_plot()</code></span></a>
      - <a href="#pymatgen.phonon.plotter.GruneisenPlotter.show"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GruneisenPlotter.show()</code></span></a>
    - <a href="#pymatgen.phonon.plotter.PhononBSPlotter"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">PhononBSPlotter</code></span></a>
      - <a href="#pymatgen.phonon.plotter.PhononBSPlotter.bs_plot_data"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBSPlotter.bs_plot_data()</code></span></a>
      - <a href="#pymatgen.phonon.plotter.PhononBSPlotter.get_plot"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBSPlotter.get_plot()</code></span></a>
      - <a href="#pymatgen.phonon.plotter.PhononBSPlotter.get_proj_plot"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBSPlotter.get_proj_plot()</code></span></a>
      - <a href="#pymatgen.phonon.plotter.PhononBSPlotter.get_ticks"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBSPlotter.get_ticks()</code></span></a>
      - <a href="#pymatgen.phonon.plotter.PhononBSPlotter.n_bands"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBSPlotter.n_bands</code></span></a>
      - <a href="#pymatgen.phonon.plotter.PhononBSPlotter.plot_brillouin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBSPlotter.plot_brillouin()</code></span></a>
      - <a href="#pymatgen.phonon.plotter.PhononBSPlotter.plot_compare"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBSPlotter.plot_compare()</code></span></a>
      - <a href="#pymatgen.phonon.plotter.PhononBSPlotter.save_plot"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBSPlotter.save_plot()</code></span></a>
      - <a href="#pymatgen.phonon.plotter.PhononBSPlotter.show"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBSPlotter.show()</code></span></a>
      - <a href="#pymatgen.phonon.plotter.PhononBSPlotter.show_proj"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononBSPlotter.show_proj()</code></span></a>
    - <a href="#pymatgen.phonon.plotter.PhononDosPlotter"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">PhononDosPlotter</code></span></a>
      - <a href="#pymatgen.phonon.plotter.PhononDosPlotter.add_dos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononDosPlotter.add_dos()</code></span></a>
      - <a href="#pymatgen.phonon.plotter.PhononDosPlotter.add_dos_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononDosPlotter.add_dos_dict()</code></span></a>
      - <a href="#pymatgen.phonon.plotter.PhononDosPlotter.get_dos_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononDosPlotter.get_dos_dict()</code></span></a>
      - <a href="#pymatgen.phonon.plotter.PhononDosPlotter.get_plot"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononDosPlotter.get_plot()</code></span></a>
      - <a href="#pymatgen.phonon.plotter.PhononDosPlotter.save_plot"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononDosPlotter.save_plot()</code></span></a>
      - <a href="#pymatgen.phonon.plotter.PhononDosPlotter.show"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PhononDosPlotter.show()</code></span></a>
    - <a href="#pymatgen.phonon.plotter.ThermoPlotter"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">ThermoPlotter</code></span></a>
      - <a href="#pymatgen.phonon.plotter.ThermoPlotter.plot_cv"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ThermoPlotter.plot_cv()</code></span></a>
      - <a href="#pymatgen.phonon.plotter.ThermoPlotter.plot_entropy"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ThermoPlotter.plot_entropy()</code></span></a>
      - <a
        href="#pymatgen.phonon.plotter.ThermoPlotter.plot_helmholtz_free_energy"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ThermoPlotter.plot_helmholtz_free_energy()</code></span></a>
      - <a href="#pymatgen.phonon.plotter.ThermoPlotter.plot_internal_energy"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ThermoPlotter.plot_internal_energy()</code></span></a>
      - <a
        href="#pymatgen.phonon.plotter.ThermoPlotter.plot_thermodynamic_properties"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ThermoPlotter.plot_thermodynamic_properties()</code></span></a>
    - <a href="#pymatgen.phonon.plotter.freq_units"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">freq_units()</code></span></a>
  - <a href="#module-pymatgen.phonon.thermal_displacements"
    class="reference internal">pymatgen.phonon.thermal_displacements
    module</a>
    - <a
      href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">ThermalDisplacementMatrices</code></span></a>
      - <a
        href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.B"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ThermalDisplacementMatrices.B</code></span></a>
      - <a
        href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.U1U2U3"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ThermalDisplacementMatrices.U1U2U3</code></span></a>
      - <a
        href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.Ucif"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ThermalDisplacementMatrices.Ucif</code></span></a>
      - <a
        href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.Ustar"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ThermalDisplacementMatrices.Ustar</code></span></a>
      - <a
        href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.beta"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ThermalDisplacementMatrices.beta</code></span></a>
      - <a
        href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.compute_directionality_quality_criterion"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ThermalDisplacementMatrices.compute_directionality_quality_criterion()</code></span></a>
      - <a
        href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.from_Ucif"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ThermalDisplacementMatrices.from_Ucif()</code></span></a>
      - <a
        href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.from_cif_P1"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ThermalDisplacementMatrices.from_cif_P1()</code></span></a>
      - <a
        href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.from_structure_with_site_properties_Ucif"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ThermalDisplacementMatrices.from_structure_with_site_properties_Ucif()</code></span></a>
      - <a
        href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.get_full_matrix"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ThermalDisplacementMatrices.get_full_matrix()</code></span></a>
      - <a
        href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.get_reduced_matrix"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ThermalDisplacementMatrices.get_reduced_matrix()</code></span></a>
      - <a
        href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.ratio_prolate"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ThermalDisplacementMatrices.ratio_prolate</code></span></a>
      - <a
        href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.to_structure_with_site_properties_Ucif"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ThermalDisplacementMatrices.to_structure_with_site_properties_Ucif()</code></span></a>
      - <a
        href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.visualize_directionality_quality_criterion"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ThermalDisplacementMatrices.visualize_directionality_quality_criterion()</code></span></a>
      - <a
        href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.write_cif"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ThermalDisplacementMatrices.write_cif()</code></span></a>

</div>

</div>

</div>

<div class="section wy-nav-content-wrap" toggle="wy-nav-shift">

[pymatgen](index.html)

<div class="wy-nav-content">

<div class="rst-content style-external-links">

<div role="navigation" aria-label="Page navigation">

- <a href="index.html" class="icon icon-home" aria-label="Home"></a>
- pymatgen.phonon package
- <a
  href="https://github.com/materialsproject/pymatgen/blob/master/docs_rst/pymatgen.phonon.rst"
  class="fa fa-github">Edit on GitHub</a>

------------------------------------------------------------------------

</div>

<div class="document" role="main" itemscope="itemscope"
itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="module-pymatgen.phonon" class="section">

<span id="pymatgen-phonon-package"></span>

# pymatgen.phonon package<a href="#module-pymatgen.phonon" class="headerlink"
title="Link to this heading"></a>

pymatgen phonon package with functionality for phonon DOS +
bandstructure analysis and more.

<div id="submodules" class="section">

## Submodules<a href="#submodules" class="headerlink"
title="Link to this heading"></a>

</div>

<div id="module-pymatgen.phonon.bandstructure" class="section">

<span id="pymatgen-phonon-bandstructure-module"></span>

## pymatgen.phonon.bandstructure module<a href="#module-pymatgen.phonon.bandstructure" class="headerlink"
title="Link to this heading"></a>

This module provides classes to define a phonon band structure.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">PhononBandStructure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">qpoints</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">frequencies</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">lattice</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.lattice.Lattice"
class="reference internal" title="pymatgen.core.lattice.Lattice"><span
class="pre">Lattice</span></a></span>*, *<span class="n"><span class="pre">nac_frequencies</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">eigendisplacements</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">nac_eigendisplacements</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">labels_dict</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><a
href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.bandstructure.Kpoint"
class="reference internal"
title="pymatgen.electronic_structure.bandstructure.Kpoint"><span
class="pre">Kpoint</span></a><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">coords_are_cartesian</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/bandstructure.py#L62-L352"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.bandstructure.PhononBandStructure"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

This is the most generic phonon band structure data possible it’s
defined by a list of qpoints + frequencies for each of them. Additional
information may be given for frequencies at Gamma, where non-analytical
contribution may be taken into account.

Parameters<span class="colon">:</span>  
- **qpoints** – list of qpoint as numpy arrays, in frac_coords of the
  given lattice by default

- **frequencies** – list of phonon frequencies in THz as a numpy array
  with shape (3\*len(structure), len(qpoints)). The First index of the
  array refers to the band and the second to the index of the qpoint.

- **lattice** – The reciprocal lattice as a pymatgen Lattice object.
  Pymatgen uses the physics convention of reciprocal lattice vectors
  WITH a 2\*pi coefficient.

- **nac_frequencies** – Frequencies with non-analytical contributions at
  Gamma in THz. A list of tuples. The first element of each tuple should
  be a list defining the direction (not necessarily a versor, will be
  normalized internally). The second element containing the
  3\*len(structure) phonon frequencies with non-analytical correction
  for that direction.

- **eigendisplacements** – the phonon eigendisplacements associated to
  the frequencies in Cartesian coordinates. A numpy array of complex
  numbers with shape (3\*len(structure), len(qpoints), len(structure),
  3). The first index of the array refers to the band, the second to the
  index of the qpoint, the third to the atom in the structure and the
  fourth to the Cartesian coordinates.

- **nac_eigendisplacements** – the phonon eigendisplacements associated
  to the non-analytical frequencies in nac_frequencies in Cartesian
  coordinates. A list of tuples. The first element of each tuple should
  be a list defining the direction. The second element containing a
  numpy array of complex numbers with shape (3\*len(structure),
  len(structure), 3).

- **labels_dict** – (dict\[str, Kpoint\]): this links a qpoint (in frac
  coords or Cartesian coordinates depending on the coords) to a label.

- **coords_are_cartesian** (*bool*) – Whether the qpoint coordinates are
  Cartesian. Defaults to False.

- **structure** – The crystal structure (as a pymatgen Structure object)
  associated with the band structure. This is needed to calculate
  element/orbital projections of the band structure.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/bandstructure.py#L293-L322"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.bandstructure.PhononBandStructure.as_dict"
class="headerlink" title="Link to this definition"></a>  
MSONable dict.

<span class="sig-name descname"><span class="pre">asr_breaking</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tol_eigendisplacements</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-05</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/bandstructure.py#L266-L291"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.bandstructure.PhononBandStructure.asr_breaking"
class="headerlink" title="Link to this definition"></a>  
Get the breaking of the acoustic sum rule for the three acoustic modes,
if Gamma is present. None otherwise. If eigendisplacements are available
they are used to determine the acoustic modes: selects the bands
corresponding to the eigendisplacements that represent to a translation
within tol_eigendisplacements. If these are not identified or
eigendisplacements are missing the first 3 modes will be used (indices
\[:3\]).

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/bandstructure.py#L324-L352"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.bandstructure.PhononBandStructure.from_dict"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
**dct** (*dict*) – Dict representation of PhononBandStructure.

Returns<span class="colon">:</span>  
PhononBandStructure

<span class="sig-name descname"><span class="pre">get_gamma_point</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a
href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.bandstructure.Kpoint"
class="reference internal"
title="pymatgen.electronic_structure.bandstructure.Kpoint"><span
class="pre">Kpoint</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/bandstructure.py#L162-L168"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.bandstructure.PhononBandStructure.get_gamma_point"
class="headerlink" title="Link to this definition"></a>  
Get the Gamma q-point as a Kpoint object (or None if not found).

<span class="sig-name descname"><span class="pre">get_nac_eigendisplacements_along_dir</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">direction</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/bandstructure.py#L248-L264"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.bandstructure.PhononBandStructure.get_nac_eigendisplacements_along_dir"
class="headerlink" title="Link to this definition"></a>  
Get the nac_eigendisplacements for the given direction (not necessarily
a versor). None if the direction is not present or
nac_eigendisplacements has not been calculated.

Parameters<span class="colon">:</span>  
**direction** – the direction as a list of 3 elements

Returns<span class="colon">:</span>  
the eigendisplacements as a numpy array of complex numbers with shape
(3\*len(structure), len(structure), 3). None if not found.

<span class="sig-name descname"><span class="pre">get_nac_frequencies_along_dir</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">direction</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">np.ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/bandstructure.py#L230-L246"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.bandstructure.PhononBandStructure.get_nac_frequencies_along_dir"
class="headerlink" title="Link to this definition"></a>  
Get the nac_frequencies for the given direction (not necessarily a
versor). None if the direction is not present or nac_frequencies has not
been calculated.

Parameters<span class="colon">:</span>  
**direction** – the direction as a list of 3 elements

Returns<span class="colon">:</span>  
the frequencies as a numpy array o(3\*len(structure), len(qpoints)).
None if not found.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">has_eigendisplacements</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/phonon/bandstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.bandstructure.PhononBandStructure.has_eigendisplacements"
class="headerlink" title="Link to this definition"></a>  
True if eigendisplacements are present.

<span class="sig-name descname"><span class="pre">has_imaginary_freq</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.01</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/bandstructure.py#L192-L199"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.bandstructure.PhononBandStructure.has_imaginary_freq"
class="headerlink" title="Link to this definition"></a>  
True if imaginary frequencies are present anywhere in the band
structure. Always True if has_imaginary_gamma_freq is True.

Parameters<span class="colon">:</span>  
**tol** – Tolerance for determining if a frequency is imaginary.
Defaults to 0.01.

<span class="sig-name descname"><span class="pre">has_imaginary_gamma_freq</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.01</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/bandstructure.py#L201-L216"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.bandstructure.PhononBandStructure.has_imaginary_gamma_freq"
class="headerlink" title="Link to this definition"></a>  
Check if there are imaginary modes at the gamma point and all close
points.

Parameters<span class="colon">:</span>  
**tol** – Tolerance for determining if a frequency is imaginary.
Defaults to 0.01.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">has_nac</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/phonon/bandstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.bandstructure.PhononBandStructure.has_nac"
class="headerlink" title="Link to this definition"></a>  
True if nac_frequencies are present (i.e. the band structure has been
calculated taking into account Born-charge-derived non-analytical
corrections at Gamma).

<span class="sig-name descname"><span class="pre">max_freq</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><a
href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.bandstructure.Kpoint"
class="reference internal"
title="pymatgen.electronic_structure.bandstructure.Kpoint"><span
class="pre">Kpoint</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/bandstructure.py#L176-L180"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.bandstructure.PhononBandStructure.max_freq"
class="headerlink" title="Link to this definition"></a>  
Get the q-point where the maximum frequency is reached and its value.

<span class="sig-name descname"><span class="pre">min_freq</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><a
href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.bandstructure.Kpoint"
class="reference internal"
title="pymatgen.electronic_structure.bandstructure.Kpoint"><span
class="pre">Kpoint</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/bandstructure.py#L170-L174"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.bandstructure.PhononBandStructure.min_freq"
class="headerlink" title="Link to this definition"></a>  
Get the q-point where the minimum frequency is reached and its value.

<span class="sig-name descname"><span class="pre">width</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">with_imaginary</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/bandstructure.py#L182-L190"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.bandstructure.PhononBandStructure.width"
class="headerlink" title="Link to this definition"></a>  
Get the difference between the maximum and minimum frequencies anywhere
in the band structure, not necessarily at identical same q-points. If
with_imaginary is False, only positive frequencies are considered.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">PhononBandStructureSymmLine</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">qpoints</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">frequencies</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">lattice</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.lattice.Lattice"
class="reference internal" title="pymatgen.core.lattice.Lattice"><span
class="pre">Lattice</span></a></span>*, *<span class="n"><span class="pre">has_nac</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">eigendisplacements</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">labels_dict</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">coords_are_cartesian</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/bandstructure.py#L355-L684"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.bandstructure.PhononBandStructureSymmLine"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.phonon.bandstructure.PhononBandStructure"
class="reference internal"
title="pymatgen.phonon.bandstructure.PhononBandStructure"><span
class="pre"><code
class="sourceCode python">PhononBandStructure</code></span></a>

Store phonon band structures along selected (symmetry) lines in the
Brillouin zone. We call the different symmetry lines (ex: \Gamma to Z)
“branches”.

Parameters<span class="colon">:</span>  
- **qpoints** – list of qpoints as numpy arrays, in frac_coords of the
  given lattice by default

- **frequencies** – list of phonon frequencies in eV as a numpy array
  with shape (3\*len(structure), len(qpoints))

- **lattice** – The reciprocal lattice as a pymatgen Lattice object.
  Pymatgen uses the physics convention of reciprocal lattice vectors
  WITH a 2\*pi coefficient

- **has_nac** – specify if the band structure has been produced taking
  into account non-analytical corrections at Gamma. If True frequencies
  at Gamma from different directions will be stored in naf. Default
  False.

- **eigendisplacements** – the phonon eigendisplacements associated to
  the frequencies in Cartesian coordinates. A numpy array of complex
  numbers with shape (3\*len(structure), len(qpoints), len(structure),
  3). he First index of the array refers to the band, the second to the
  index of the qpoint, the third to the atom in the structure and the
  fourth to the Cartesian coordinates.

- **labels_dict** – (dict) of {} this links a qpoint (in frac coords or
  Cartesian coordinates depending on the coords) to a label.

- **coords_are_cartesian** – Whether the qpoint coordinates are
  cartesian.

- **structure** – The crystal structure (as a pymatgen Structure object)
  associated with the band structure. This is needed if we provide
  projections to the band structure.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/bandstructure.py#L641-L649"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.bandstructure.PhononBandStructureSymmLine.as_dict"
class="headerlink" title="Link to this definition"></a>  
Get MSONable dict.

<span class="sig-name descname"><span class="pre">as_phononwebsite</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/bandstructure.py#L532-L608"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.bandstructure.PhononBandStructureSymmLine.as_phononwebsite"
class="headerlink" title="Link to this definition"></a>  
Return a dictionary with the phononwebsite format:
<a href="https://henriquemiranda.github.io/phononwebsite"
class="reference external">https://henriquemiranda.github.io/phononwebsite</a>.

<span class="sig-name descname"><span class="pre">band_reorder</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/bandstructure.py#L610-L639"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.bandstructure.PhononBandStructureSymmLine.band_reorder"
class="headerlink" title="Link to this definition"></a>  
Re-order the eigenvalues according to the similarity of the
eigenvectors.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/bandstructure.py#L651-L672"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.bandstructure.PhononBandStructureSymmLine.from_dict"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
**dct** (*dict*) – Dict representation.

Returns<span class="colon">:</span>  
PhononBandStructureSymmLine

<span class="sig-name descname"><span class="pre">get_branch</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">index</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/bandstructure.py#L499-L523"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.bandstructure.PhononBandStructureSymmLine.get_branch"
class="headerlink" title="Link to this definition"></a>  
Get in what branch(es) is the qpoint. There can be several branches.

Parameters<span class="colon">:</span>  
**index** (*int*) – the qpoint index

Returns<span class="colon">:</span>  
\[{“name”,”start_index”,”end_index”,”index”}\]  
indicating all branches in which the qpoint is. It takes into account
the fact that one qpoint (e.g., \Gamma) can be in several branches

Return type<span class="colon">:</span>  
list\[dict\[str, str \| int\]\]

<span class="sig-name descname"><span class="pre">get_equivalent_qpoints</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">index</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/bandstructure.py#L478-L497"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.bandstructure.PhononBandStructureSymmLine.get_equivalent_qpoints"
class="headerlink" title="Link to this definition"></a>  
Get the list of qpoint indices equivalent (meaning they are the same
frac coords) to the given one.

Parameters<span class="colon">:</span>  
**index** (*int*) – the qpoint index

Returns<span class="colon">:</span>  
equivalent indices

Return type<span class="colon">:</span>  
list\[int\]

TODO: now it uses the label we might want to use coordinates instead (in
case there was a mislabel)

<span class="sig-name descname"><span class="pre">write_phononwebsite</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/bandstructure.py#L525-L530"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.bandstructure.PhononBandStructureSymmLine.write_phononwebsite"
class="headerlink" title="Link to this definition"></a>  
Write a JSON file for the phononwebsite:
<a href="https://henriquemiranda.github.io/phononwebsite"
class="reference external">https://henriquemiranda.github.io/phononwebsite</a>.

<!-- -->

<span class="sig-name descname"><span class="pre">eigenvectors_from_displacements</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">disp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">masses</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">np.ndarray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/bandstructure.py#L39-L41"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.bandstructure.eigenvectors_from_displacements"
class="headerlink" title="Link to this definition"></a>  
Calculate the eigenvectors from the atomic displacements.

<!-- -->

<span class="sig-name descname"><span class="pre">estimate_band_connection</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">prev_eigvecs</span></span>*, *<span class="n"><span class="pre">eigvecs</span></span>*, *<span class="n"><span class="pre">prev_band_order</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/bandstructure.py#L44-L59"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.bandstructure.estimate_band_connection"
class="headerlink" title="Link to this definition"></a>  
A function to order the phonon eigenvectors taken from phonopy.

<!-- -->

<span class="sig-name descname"><span class="pre">get_reasonable_repetitions</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">n_atoms</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/bandstructure.py#L25-L36"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.bandstructure.get_reasonable_repetitions"
class="headerlink" title="Link to this definition"></a>  
Choose the number of repetitions in a supercell according to the number
of atoms in the system.

</div>

<div id="module-pymatgen.phonon.dos" class="section">

<span id="pymatgen-phonon-dos-module"></span>

## pymatgen.phonon.dos module<a href="#module-pymatgen.phonon.dos" class="headerlink"
title="Link to this heading"></a>

This module defines classes to represent the phonon density of states.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">CompletePhononDos</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">total_dos</span></span>*, *<span class="n"><span class="pre">ph_doses</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/dos.py#L587-L658"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.dos.CompletePhononDos" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.phonon.dos.PhononDos" class="reference internal"
title="pymatgen.phonon.dos.PhononDos"><span class="pre"><code
class="sourceCode python">PhononDos</code></span></a>

This wrapper class defines a total dos, and also provides a list of
PDos.

<span class="sig-name descname"><span class="pre">pdos</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/phonon/dos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.dos.CompletePhononDos.pdos" class="headerlink"
title="Link to this definition"></a>  
Dict of partial densities of the form {Site:Densities}. Densities are a
dict of {Orbital:Values} where Values are a list of floats. Site is a
pymatgen.core.sites.Site object.

Type<span class="colon">:</span>  
dict

Parameters<span class="colon">:</span>  
- **structure** – Structure associated with this particular DOS.

- **total_dos** – total Dos for structure

- **ph_doses** – The phonon DOSes are supplied as a dict of {Site:
  Densities}.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/dos.py#L642-L655"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.dos.CompletePhononDos.as_dict"
class="headerlink" title="Link to this definition"></a>  
JSON-serializable dict representation of CompletePhononDos.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/dos.py#L633-L640"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.dos.CompletePhononDos.from_dict"
class="headerlink" title="Link to this definition"></a>  
Get CompleteDos object from dict representation.

<span class="sig-name descname"><span class="pre">get_element_dos</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/dos.py#L618-L631"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.dos.CompletePhononDos.get_element_dos"
class="headerlink" title="Link to this definition"></a>  
Get element projected Dos.

Returns<span class="colon">:</span>  
Dos}

Return type<span class="colon">:</span>  
dict of {Element

<span class="sig-name descname"><span class="pre">get_site_dos</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">site</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.phonon.dos.PhononDos" class="reference internal"
title="pymatgen.phonon.dos.PhononDos"><span
class="pre">PhononDos</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/dos.py#L607-L616"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.dos.CompletePhononDos.get_site_dos"
class="headerlink" title="Link to this definition"></a>  
Get the Dos for a site.

Parameters<span class="colon">:</span>  
**site** – Site in Structure associated with CompletePhononDos.

Returns<span class="colon">:</span>  
containing summed orbital densities for site.

Return type<span class="colon">:</span>  
<a href="#pymatgen.phonon.dos.PhononDos" class="reference internal"
title="pymatgen.phonon.dos.PhononDos">PhononDos</a>

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">PhononDos</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">frequencies</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">densities</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/dos.py#L28-L564"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.dos.PhononDos" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Basic DOS object. All other DOS objects are extended versions of this
object.

Parameters<span class="colon">:</span>  
- **frequencies** – A sequence of frequencies in THz

- **densities** – A sequence representing the density of states.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/dos.py#L145-L152"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.dos.PhononDos.as_dict" class="headerlink"
title="Link to this definition"></a>  
JSON-serializable dict representation of PhononDos.

<span class="sig-name descname"><span class="pre">cv</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">temp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/dos.py#L172-L207"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.dos.PhononDos.cv" class="headerlink"
title="Link to this definition"></a>  
Constant volume specific heat C_v at temperature T obtained from the
integration of the DOS. Only positive frequencies will be used. Result
in J/(K\*mol-c). A mol-c is the abbreviation of a mole-cell, that is,
the number of Avogadro times the atoms in a unit cell. To compare with
experimental data the result should be divided by the number of unit
formulas in the cell. If the structure is provided the division is
performed internally and the result is in J/(K\*mol).

Parameters<span class="colon">:</span>  
- **temp** – a temperature in K

- **structure** – the structure of the system. If not None it will be
  used to determine the number of formula units

- **\*\*kwargs** – allows passing in deprecated t parameter for temp

Returns<span class="colon">:</span>  
Constant volume specific heat C_v

Return type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">entropy</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">temp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/dos.py#L209-L242"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.dos.PhononDos.entropy" class="headerlink"
title="Link to this definition"></a>  
Vibrational entropy at temperature T obtained from the integration of
the DOS. Only positive frequencies will be used. Result in J/(K\*mol-c).
A mol-c is the abbreviation of a mole-cell, that is, the number of
Avogadro times the atoms in a unit cell. To compare with experimental
data the result should be divided by the number of unit formulas in the
cell. If the structure is provided the division is performed internally
and the result is in J/(K\*mol).

Parameters<span class="colon">:</span>  
- **temp** – a temperature in K

- **structure** – the structure of the system. If not None it will be
  used to determine the number of formula units

- **\*\*kwargs** – allows passing in deprecated t parameter for temp

Returns<span class="colon">:</span>  
Vibrational entropy

Return type<span class="colon">:</span>  
float

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">fp_to_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">fp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.phonon.dos.PhononDosFingerprint"
class="reference internal"
title="pymatgen.phonon.dos.PhononDosFingerprint"><span
class="pre">PhononDosFingerprint</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/dos.py#L489-L502"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.dos.PhononDos.fp_to_dict" class="headerlink"
title="Link to this definition"></a>  
Convert a fingerprint into a dictionary.

Parameters<span class="colon">:</span>  
**fp** – The DOS fingerprint to be converted into a dictionary

Returns<span class="colon">:</span>  
A dict of the fingerprint Keys=type, Values=np.ndarray(frequencies,
densities)

Return type<span class="colon">:</span>  
dict

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">ArrayLike</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/dos.py#L140-L143"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.dos.PhononDos.from_dict" class="headerlink"
title="Link to this definition"></a>  
Get PhononDos object from dict representation of PhononDos.

<span class="sig-name descname"><span class="pre">get_dos_fp</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">binning</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">min_f</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">max_f</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">n_bins</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">256</span></span>*, *<span class="n"><span class="pre">normalize</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.phonon.dos.PhononDosFingerprint"
class="reference internal"
title="pymatgen.phonon.dos.PhononDosFingerprint"><span
class="pre">PhononDosFingerprint</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/dos.py#L418-L487"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.dos.PhononDos.get_dos_fp" class="headerlink"
title="Link to this definition"></a>  
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
- **binning** (*bool*) – If true, the DOS fingerprint is binned using
  np.linspace and n_bins. Default is True.

- **min_f** (*float*) – The minimum mode frequency to include in the
  fingerprint (default is None)

- **max_f** (*float*) – The maximum mode frequency to include in the
  fingerprint (default is None)

- **n_bins** (*int*) – Number of bins to be used in the fingerprint
  (default is 256)

- **normalize** (*bool*) – If true, normalizes the area under fp to
  equal to 1. Default is True.

Returns<span class="colon">:</span>  
The phonon density of states fingerprint  
of format (frequencies, densities, n_bins, bin_width)

Return type<span class="colon">:</span>  
<a href="#pymatgen.phonon.dos.PhononDosFingerprint"
class="reference internal"
title="pymatgen.phonon.dos.PhononDosFingerprint">PhononDosFingerprint</a>

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">get_dos_fp_similarity</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">fp1</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.phonon.dos.PhononDosFingerprint"
class="reference internal"
title="pymatgen.phonon.dos.PhononDosFingerprint"><span
class="pre">PhononDosFingerprint</span></a></span>*, *<span class="n"><span class="pre">fp2</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.phonon.dos.PhononDosFingerprint"
class="reference internal"
title="pymatgen.phonon.dos.PhononDosFingerprint"><span
class="pre">PhononDosFingerprint</span></a></span>*, *<span class="n"><span class="pre">col</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1</span></span>*, *<span class="n"><span class="pre">pt</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'All'</span></span>*, *<span class="n"><span class="pre">normalize</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">metric</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'tanimoto'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'wasserstein'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cosine-sim'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'tanimoto'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/dos.py#L504-L564"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.dos.PhononDos.get_dos_fp_similarity"
class="headerlink" title="Link to this definition"></a>  
Calculate the similarity index between two fingerprints.

Parameters<span class="colon">:</span>  
- **fp1** (<a href="#pymatgen.phonon.dos.PhononDosFingerprint"
  class="reference internal"
  title="pymatgen.phonon.dos.PhononDosFingerprint"><em>PhononDosFingerprint</em></a>)
  – The 1st dos fingerprint object

- **fp2** (<a href="#pymatgen.phonon.dos.PhononDosFingerprint"
  class="reference internal"
  title="pymatgen.phonon.dos.PhononDosFingerprint"><em>PhononDosFingerprint</em></a>)
  – The 2nd dos fingerprint object

- **col** (*int*) – The item in the fingerprints (0:frequencies,1:
  densities) to compute the similarity index of (default is 1)

- **pt** (*int* *or* *str*) – The index of the point that the dot
  product is to be taken (default is All)

- **normalize** (*bool*) – If True normalize the scalar product to 1
  (default is False)

- **metric** (*Literal*) – Metric used to compute similarity default is
  “tanimoto”.

Raises<span class="colon">:</span>  
- **ValueError** – If metric other than “tanimoto”, “wasserstein” and
  “cosine-sim” is requested.

- **ValueError** – If normalize is set to True along with the metric.

Returns<span class="colon">:</span>  
Similarity index given by the dot product

Return type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">get_interpolated_value</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">frequency</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/dos.py#L125-L131"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.dos.PhononDos.get_interpolated_value"
class="headerlink" title="Link to this definition"></a>  
Get interpolated density for a particular frequency.

Parameters<span class="colon">:</span>  
**frequency** – frequency to return the density for.

<span class="sig-name descname"><span class="pre">get_last_peak</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">threshold</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.05</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/dos.py#L377-L416"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.dos.PhononDos.get_last_peak"
class="headerlink" title="Link to this definition"></a>  
Find the last peak in the phonon DOS defined as the highest frequency
with a DOS value at least threshold \* height of the overall highest DOS
peak. A peak is any local maximum of the DOS as a function of frequency.
Use dos.get_interpolated_value(peak_freq) to get density at peak_freq.

TODO method added by @janosh on 2023-12-18. seems to work in most cases
but was not extensively tested. PRs with improvements welcome!

Parameters<span class="colon">:</span>  
**threshold** (*float,* *optional*) – Minimum ratio of the height of the
last peak to the height of the highest peak. Defaults to 0.05 = 5%. In
case no peaks are high enough to match, the threshold is reset to half
the height of the second-highest peak.

Returns<span class="colon">:</span>  
last DOS peak frequency (in THz)

Return type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">get_smeared_densities</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">sigma</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">ndarray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/dos.py#L40-L56"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.dos.PhononDos.get_smeared_densities"
class="headerlink" title="Link to this definition"></a>  
Get the densities, but with a Gaussian smearing of std dev sigma
applied.

Parameters<span class="colon">:</span>  
**sigma** – Std dev of Gaussian smearing function. In units of THz.
Common values are 0.01 - 0.1 THz.

Returns<span class="colon">:</span>  
Gaussian-smeared DOS densities.

Return type<span class="colon">:</span>  
np.array

<span class="sig-name descname"><span class="pre">helmholtz_free_energy</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">temp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/dos.py#L279-L312"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.dos.PhononDos.helmholtz_free_energy"
class="headerlink" title="Link to this definition"></a>  
Phonon contribution to the Helmholtz free energy at temperature T
obtained from the integration of the DOS. Only positive frequencies will
be used. Result in J/mol-c. A mol-c is the abbreviation of a mole-cell,
that is, the number of Avogadro times the atoms in a unit cell. To
compare with experimental data the result should be divided by the
number of unit formulas in the cell. If the structure is provided the
division is performed internally and the result is in J/mol.

Parameters<span class="colon">:</span>  
- **temp** – a temperature in K

- **structure** – the structure of the system. If not None it will be
  used to determine the number of formula units

- **\*\*kwargs** – allows passing in deprecated t parameter for temp

Returns<span class="colon">:</span>  
Phonon contribution to the Helmholtz free energy

Return type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">ind_zero_freq</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/phonon/dos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.dos.PhononDos.ind_zero_freq"
class="headerlink" title="Link to this definition"></a>  
Index of the first point for which the frequencies are \>= 0.

<span class="sig-name descname"><span class="pre">internal_energy</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">temp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/dos.py#L244-L277"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.dos.PhononDos.internal_energy"
class="headerlink" title="Link to this definition"></a>  
Phonon contribution to the internal energy at temperature T obtained
from the integration of the DOS. Only positive frequencies will be used.
Result in J/mol-c. A mol-c is the abbreviation of a mole-cell, that is,
the number of Avogadro times the atoms in a unit cell. To compare with
experimental data the result should be divided by the number of unit
formulas in the cell. If the structure is provided the division is
performed internally and the result is in J/mol.

Parameters<span class="colon">:</span>  
- **temp** – a temperature in K

- **structure** – the structure of the system. If not None it will be
  used to determine the number of formula units

- **\*\*kwargs** – allows passing in deprecated t parameter for temp

Returns<span class="colon">:</span>  
Phonon contribution to the internal energy

Return type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">mae</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.phonon.dos.PhononDos" class="reference internal"
title="pymatgen.phonon.dos.PhononDos"><span
class="pre">PhononDos</span></a></span>*, *<span class="n"><span class="pre">two_sided</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/dos.py#L340-L360"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.dos.PhononDos.mae" class="headerlink"
title="Link to this definition"></a>  
Mean absolute error between two DOSs.

Parameters<span class="colon">:</span>  
- **other**
  (<a href="#pymatgen.phonon.dos.PhononDos" class="reference internal"
  title="pymatgen.phonon.dos.PhononDos"><em>PhononDos</em></a>) –
  Another phonon DOS

- **two_sided** (*bool*) – Whether to calculate the two-sided MAE
  meaning interpolate each DOS to the other’s frequencies and averaging
  the two MAEs. Defaults to True.

Returns<span class="colon">:</span>  
Mean absolute error.

Return type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">r2_score</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.phonon.dos.PhononDos" class="reference internal"
title="pymatgen.phonon.dos.PhononDos"><span
class="pre">PhononDos</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/dos.py#L362-L375"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.dos.PhononDos.r2_score" class="headerlink"
title="Link to this definition"></a>  
R^2 score between two DOSs.

Parameters<span class="colon">:</span>  
**other**
(<a href="#pymatgen.phonon.dos.PhononDos" class="reference internal"
title="pymatgen.phonon.dos.PhononDos"><em>PhononDos</em></a>) – Another
phonon DOS

Returns<span class="colon">:</span>  
R^2 score

Return type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">zero_point_energy</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/dos.py#L314-L338"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.dos.PhononDos.zero_point_energy"
class="headerlink" title="Link to this definition"></a>  
Zero point energy of the system. Only positive frequencies will be used.
Result in J/mol-c. A mol-c is the abbreviation of a mole-cell, that is,
the number of Avogadro times the atoms in a unit cell. To compare with
experimental data the result should be divided by the number of unit
formulas in the cell. If the structure is provided the division is
performed internally and the result is in J/mol.

Parameters<span class="colon">:</span>  
**structure** – the structure of the system. If not None it will be used
to determine the number of formula units

Returns<span class="colon">:</span>  
Phonon contribution to the internal energy

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">PhononDosFingerprint</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">frequencies</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">NDArray</span></span>*, *<span class="n"><span class="pre">densities</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">NDArray</span></span>*, *<span class="n"><span class="pre">n_bins</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">bin_width</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/dos.py#L567-L584"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.dos.PhononDosFingerprint" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`NamedTuple`</span>

Represents a Phonon Density of States (DOS) fingerprint.

This named tuple is used to store information related to the Density of
States (DOS) in a material. It includes the frequencies, densities,
number of bins, and bin width.

Parameters<span class="colon">:</span>  
- **frequencies** – The frequency values associated with the DOS.

- **densities** – The corresponding density values for each energy.

- **n_bins** – The number of bins used in the fingerprint.

- **bin_width** – The width of each bin in the DOS fingerprint.

Create new instance of PhononDosFingerprint(frequencies, densities,
n_bins, bin_width)

<span class="sig-name descname"><span class="pre">bin_width</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/phonon/dos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.dos.PhononDosFingerprint.bin_width"
class="headerlink" title="Link to this definition"></a>  
Alias for field number 3

<span class="sig-name descname"><span class="pre">densities</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">NDArray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/phonon/dos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.dos.PhononDosFingerprint.densities"
class="headerlink" title="Link to this definition"></a>  
Alias for field number 1

<span class="sig-name descname"><span class="pre">frequencies</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">NDArray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/phonon/dos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.dos.PhononDosFingerprint.frequencies"
class="headerlink" title="Link to this definition"></a>  
Alias for field number 0

<span class="sig-name descname"><span class="pre">n_bins</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/phonon/dos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.dos.PhononDosFingerprint.n_bins"
class="headerlink" title="Link to this definition"></a>  
Alias for field number 2

</div>

<div id="module-pymatgen.phonon.gruneisen" class="section">

<span id="pymatgen-phonon-gruneisen-module"></span>

## pymatgen.phonon.gruneisen module<a href="#module-pymatgen.phonon.gruneisen" class="headerlink"
title="Link to this heading"></a>

This module provides classes to define a Grueneisen band structure.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">GruneisenParameter</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">qpoints</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">gruneisen</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">frequencies</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">multiplicities</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">lattice</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.lattice.Lattice"
class="reference internal" title="pymatgen.core.lattice.Lattice"><span
class="pre">Lattice</span></a></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/gruneisen.py#L41-L238"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.gruneisen.GruneisenParameter"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Store the Gruneisen parameter for a single q-point on a regular grid.

Parameters<span class="colon">:</span>  
- **qpoints** – list of qpoints as numpy arrays, in frac_coords of the
  given lattice by default

- **gruneisen** – list of gruneisen parameters as numpy arrays, shape:
  (3\*len(structure), len(qpoints))

- **frequencies** – list of phonon frequencies in THz as a numpy array
  with shape (3\*len(structure), len(qpoints))

- **multiplicities** – list of multiplicities

- **structure** – The crystal structure (as a pymatgen Structure object)
  associated with the gruneisen parameters.

- **lattice** – The reciprocal lattice as a pymatgen Lattice object.
  Pymatgen uses the physics convention of reciprocal lattice vectors
  WITH a 2\*pi coefficient.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">acoustic_debye_temp</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/phonon/gruneisen.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.gruneisen.GruneisenParameter.acoustic_debye_temp"
class="headerlink" title="Link to this definition"></a>  
Acoustic Debye temperature in K, i.e. the Debye temperature divided by
n_sites\*\*(1/3). Adapted from abipy.

<span class="sig-name descname"><span class="pre">average_gruneisen</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">t</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">squared</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">limit_frequencies</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'debye'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'acoustic'</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/gruneisen.py#L70-L132"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.gruneisen.GruneisenParameter.average_gruneisen"
class="headerlink" title="Link to this definition"></a>  
Calculate the average of the Gruneisen based on the values on the
regular grid. If squared is True, the average will use the squared value
of the Gruneisen and a squared root is performed on the final result.
Values associated with negative frequencies will be ignored. See Nath et
al. \_Scripta [<span id="id6"
class="problematic">Materialia\_</span>](#id5) **2017**, \_129\_, 88 for
the definitions. Adapted from classes in abipy that have been written by
Guido Petretto (UCLouvain).

Parameters<span class="colon">:</span>  
- **t** – the temperature at which the average Gruneisen will be
  evaluated. If None the acoustic Debye temperature is used (see
  acoustic_debye_temp).

- **squared** – if True the average is performed on the squared values
  of the Grueneisen.

- **limit_frequencies** – if None (default) no limit on the frequencies
  will be applied. Possible values are “debye” (only modes with
  frequencies lower than the acoustic Debye temperature) and “acoustic”
  (only the acoustic modes, i.e. the first three modes).

Returns<span class="colon">:</span>  
The average Gruneisen parameter

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">debye_temp_limit</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/phonon/gruneisen.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.gruneisen.GruneisenParameter.debye_temp_limit"
class="headerlink" title="Link to this definition"></a>  
Debye temperature in K. Adapted from apipy.

<span class="sig-name descname"><span class="pre">debye_temp_phonopy</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">freq_max_fit</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/gruneisen.py#L212-L229"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.gruneisen.GruneisenParameter.debye_temp_phonopy"
class="headerlink" title="Link to this definition"></a>  
Get Debye temperature in K as implemented in phonopy.

Parameters<span class="colon">:</span>  
**freq_max_fit** – Maximum frequency to include for fitting. Defaults to
include first quartile of frequencies.

Returns<span class="colon">:</span>  
Debye temperature in K.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">phdos</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="#pymatgen.phonon.dos.PhononDos" class="reference internal"
title="pymatgen.phonon.dos.PhononDos"><span
class="pre">PhononDos</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/phonon/gruneisen.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.gruneisen.GruneisenParameter.phdos"
class="headerlink" title="Link to this definition"></a>  
The phonon DOS (re)constructed from the gruneisen.yaml file.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">tdos</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/phonon/gruneisen.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.gruneisen.GruneisenParameter.tdos"
class="headerlink" title="Link to this definition"></a>  
The total DOS (re)constructed from the gruneisen.yaml file.

<span class="sig-name descname"><span class="pre">thermal_conductivity_slack</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">squared</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">limit_frequencies</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'debye'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'acoustic'</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">theta_d</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">t</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/gruneisen.py#L134-L175"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.gruneisen.GruneisenParameter.thermal_conductivity_slack"
class="headerlink" title="Link to this definition"></a>  
Calculate the thermal conductivity at the acoustic Debye temperature
with the Slack formula, using the average Gruneisen. Adapted from abipy.

Parameters<span class="colon">:</span>  
- **squared** (*bool*) – if True the average is performed on the squared
  values of the Gruneisen

- **limit_frequencies** – if None (default) no limit on the frequencies
  will be applied. Possible values are “debye” (only modes with
  frequencies lower than the acoustic Debye temperature) and “acoustic”
  (only the acoustic modes, i.e. the first three modes).

- **theta_d** – the temperature used to estimate the average of the
  Gruneisen used in the Slack formula. If None the acoustic Debye
  temperature is used (see acoustic_debye_temp). Will also be considered
  as the Debye temperature in the Slack formula.

- **t** – temperature at which the thermal conductivity is estimated. If
  None the value at the calculated acoustic Debye temperature is given.
  The value is obtained as a simple rescaling of the value at the Debye
  temperature.

Returns<span class="colon">:</span>  
The value of the thermal conductivity in W/(m\*K)

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">GruneisenPhononBandStructure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">qpoints</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">frequencies</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">gruneisenparameters</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">lattice</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.lattice.Lattice"
class="reference internal" title="pymatgen.core.lattice.Lattice"><span
class="pre">Lattice</span></a></span>*, *<span class="n"><span class="pre">eigendisplacements</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">labels_dict</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">coords_are_cartesian</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/gruneisen.py#L241-L343"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.gruneisen.GruneisenPhononBandStructure"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.phonon.bandstructure.PhononBandStructure"
class="reference internal"
title="pymatgen.phonon.bandstructure.PhononBandStructure"><span
class="pre"><code
class="sourceCode python">PhononBandStructure</code></span></a>

This is the most generic phonon band structure data possible it’s
defined by a list of qpoints + frequencies for each of them. Additional
information may be given for frequencies at Gamma, where non-analytical
contribution may be taken into account.

Parameters<span class="colon">:</span>  
- **qpoints** – list of qpoint as numpy arrays, in frac_coords of the
  given lattice by default

- **frequencies** – list of phonon frequencies in THz as a numpy array
  with shape (3\*len(structure), len(qpoints)). The First index of the
  array refers to the band and the second to the index of the qpoint.

- **gruneisenparameters** – list of Grueneisen parameters with the same
  structure frequencies.

- **lattice** – The reciprocal lattice as a pymatgen Lattice object.
  Pymatgen uses the physics convention of reciprocal lattice vectors
  WITH a 2\*pi coefficient.

- **eigendisplacements** – the phonon eigendisplacements associated to
  the frequencies in Cartesian coordinates. A numpy array of complex
  numbers with shape (3\*len(structure), len(qpoints), len(structure),
  3). The first index of the array refers to the band, the second to the
  index of the qpoint, the third to the atom in the structure and the
  fourth to the Cartesian coordinates.

- **labels_dict** – (dict) of {} this links a qpoint (in frac coords or
  Cartesian coordinates depending on the coords) to a label.

- **coords_are_cartesian** – Whether the qpoint coordinates are
  Cartesian.

- **structure** – The crystal structure (as a pymatgen Structure object)
  associated with the band structure. This is needed if we provide
  projections to the band structure.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/gruneisen.py#L298-L319"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.gruneisen.GruneisenPhononBandStructure.as_dict"
class="headerlink" title="Link to this definition"></a>  
Returns<span class="colon">:</span>  
MSONable dict.

Return type<span class="colon">:</span>  
dict\[str, Any\]

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/gruneisen.py#L321-L343"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.gruneisen.GruneisenPhononBandStructure.from_dict"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
**dct** (*dict*) – Dict representation.

Returns<span class="colon">:</span>  
Phonon band structure with Grueneisen parameters.

Return type<span class="colon">:</span>  
<a href="#pymatgen.phonon.gruneisen.GruneisenPhononBandStructure"
class="reference internal"
title="pymatgen.phonon.gruneisen.GruneisenPhononBandStructure">GruneisenPhononBandStructure</a>

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">GruneisenPhononBandStructureSymmLine</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">qpoints</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">frequencies</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">gruneisenparameters</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">lattice</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.lattice.Lattice"
class="reference internal" title="pymatgen.core.lattice.Lattice"><span
class="pre">Lattice</span></a></span>*, *<span class="n"><span class="pre">eigendisplacements</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">labels_dict</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">coords_are_cartesian</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/gruneisen.py#L346-L428"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.gruneisen.GruneisenPhononBandStructureSymmLine"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.phonon.gruneisen.GruneisenPhononBandStructure"
class="reference internal"
title="pymatgen.phonon.gruneisen.GruneisenPhononBandStructure"><span
class="pre"><code
class="sourceCode python">GruneisenPhononBandStructure</code></span></a>,
<a href="#pymatgen.phonon.bandstructure.PhononBandStructureSymmLine"
class="reference internal"
title="pymatgen.phonon.bandstructure.PhononBandStructureSymmLine"><span
class="pre"><code
class="sourceCode python">PhononBandStructureSymmLine</code></span></a>

Store a GruneisenPhononBandStructureSymmLine together with Grueneisen
parameters for every frequency.

Parameters<span class="colon">:</span>  
- **qpoints** – list of qpoints as numpy arrays, in frac_coords of the
  given lattice by default

- **frequencies** – list of phonon frequencies in eV as a numpy array
  with shape (3\*len(structure), len(qpoints))

- **gruneisenparameters** – list of Grueneisen parameters as a numpy
  array with the shape (3\*len(structure), len(qpoints))

- **lattice** – The reciprocal lattice as a pymatgen Lattice object.
  Pymatgen uses the physics convention of reciprocal lattice vectors
  WITH a 2\*pi coefficient

- **eigendisplacements** – the phonon eigendisplacements associated to
  the frequencies in Cartesian coordinates. A numpy array of complex
  numbers with shape (3\*len(structure), len(qpoints), len(structure),
  3). The first index of the array refers to the band, the second to the
  index of the qpoint, the third to the atom in the structure and the
  fourth to the Cartesian coordinates.

- **labels_dict** – (dict) of {} this links a qpoint (in frac coords or
  Cartesian coordinates depending on the coords) to a label.

- **coords_are_cartesian** – Whether the qpoint coordinates are
  cartesian.

- **structure** – The crystal structure (as a pymatgen Structure object)
  associated with the band structure. This is needed if we provide
  projections to the band structure.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/gruneisen.py#L406-L428"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.gruneisen.GruneisenPhononBandStructureSymmLine.from_dict"
class="headerlink" title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
**dct** (*dict*) – Dict representation.

Returns<span class="colon">:</span>  
GruneisenPhononBandStructureSymmLine

</div>

<div id="module-pymatgen.phonon.ir_spectra" class="section">

<span id="pymatgen-phonon-ir-spectra-module"></span>

## pymatgen.phonon.ir_spectra module<a href="#module-pymatgen.phonon.ir_spectra" class="headerlink"
title="Link to this heading"></a>

This module provides classes to handle the calculation of the IR spectra
This implementation is adapted from Abipy
<a href="https://github.com/abinit/abipy"
class="reference external">https://github.com/abinit/abipy</a> where it
was originally done by Guido Petretto and Matteo Giantomassi.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">IRDielectricTensor</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">oscillator_strength</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">ph_freqs_gamma</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">epsilon_infinity</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/ir_spectra.py#L37-L240"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.ir_spectra.IRDielectricTensor"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Handle the Ionic Dielectric Tensor The implementation is adapted from
Abipy See the definitions Eq.(53-54) in [<span id="id2"
class="problematic">:cite:\`Gonze1997\`</span>](#id1) PRB55, 10355
(1997).

Parameters<span class="colon">:</span>  
- **oscillator_strength** – IR oscillator strengths as defined in Eq. 54
  in [<span id="id4"
  class="problematic">:cite:\`Gonze1997\`</span>](#id3) PRB55, 10355
  (1997).

- **ph_freqs_gamma** – Phonon frequencies at the Gamma point

- **epsilon_infinity** – electronic susceptibility as defined in Eq. 29.

- **structure** – A Structure object corresponding to the structure used
  for the calculation.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/ir_spectra.py#L82-L91"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.ir_spectra.IRDielectricTensor.as_dict"
class="headerlink" title="Link to this definition"></a>  
JSON-serializable dict representation of IRDielectricTensor.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/ir_spectra.py#L63-L70"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.ir_spectra.IRDielectricTensor.from_dict"
class="headerlink" title="Link to this definition"></a>  
Get IRDielectricTensor from dict representation.

<span class="sig-name descname"><span class="pre">get_ir_spectra</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">broad</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">5e-05</span></span>*, *<span class="n"><span class="pre">emin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">emax</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">divs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">500</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/ir_spectra.py#L98-L136"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.ir_spectra.IRDielectricTensor.get_ir_spectra"
class="headerlink" title="Link to this definition"></a>  
The IR spectra is obtained for the different directions.

Parameters<span class="colon">:</span>  
- **broad** – a list of broadenings or a single broadening for the
  phonon peaks

- **emin** (*float*) – minimum energy in which to obtain the spectra.
  Defaults to 0.

- **emax** (*float*) – maximum energy in which to obtain the spectra.
  Defaults to None.

- **divs** – number of frequency samples between emin and emax

Returns<span class="colon">:</span>  
divs array with the frequencies at which the  
dielectric tensor is calculated

dielectric_tensor: divsx3x3 numpy array with the dielectric tensor  
for the range of frequencies

Return type<span class="colon">:</span>  
frequencies

<span class="sig-name descname"><span class="pre">get_plotter</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">components</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">('xx',)</span></span>*, *<span class="n"><span class="pre">reim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'reim'</span></span>*, *<span class="n"><span class="pre">broad</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">5e-05</span></span>*, *<span class="n"><span class="pre">emin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">emax</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">divs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">500</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="pymatgen.vis.html#pymatgen.vis.plotters.SpectrumPlotter"
class="reference internal"
title="pymatgen.vis.plotters.SpectrumPlotter"><span
class="pre">SpectrumPlotter</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/ir_spectra.py#L196-L240"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.ir_spectra.IRDielectricTensor.get_plotter"
class="headerlink" title="Link to this definition"></a>  
Return an instance of the Spectrum plotter containing the different
requested components.

Parameters<span class="colon">:</span>  
- **components** – A list with the components of the dielectric tensor
  to plot. Can be either two indexes or a string like ‘xx’ to plot the
  (0,0) component

- **reim** – If ‘re’ (im) is present in the string plots the real
  (imaginary) part of the dielectric tensor

- **broad** (*float*) – a list of broadenings or a single broadening for
  the phonon peaks. Defaults to 0.00005.

- **emin** (*float*) – minimum energy in which to obtain the spectra.
  Defaults to 0.

- **emax** (*float*) – maximum energy in which to obtain the spectra.
  Defaults to None.

- **divs** – number of frequency samples between emin and emax

- **\*\*kwargs** – Passed to IRDielectricTensor.get_spectrum()

<span class="sig-name descname"><span class="pre">get_spectrum</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">component</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">str</span></span>*, *<span class="n"><span class="pre">reim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">broad</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">5e-05</span></span>*, *<span class="n"><span class="pre">emin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">emax</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">divs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">500</span></span>*, *<span class="n"><span class="pre">label</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="pymatgen.core.html#pymatgen.core.spectrum.Spectrum"
class="reference internal" title="pymatgen.core.spectrum.Spectrum"><span
class="pre">Spectrum</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/ir_spectra.py#L169-L194"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.ir_spectra.IRDielectricTensor.get_spectrum"
class="headerlink" title="Link to this definition"></a>  
component: either two indexes or a string like ‘xx’ to plot the (0,0)
component reim: only “re” or “im” broad: a list of broadenings or a
single broadening for the phonon peaks.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">max_phfreq</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/phonon/ir_spectra.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.ir_spectra.IRDielectricTensor.max_phfreq"
class="headerlink" title="Link to this definition"></a>  
Maximum phonon frequency.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">nph_freqs</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/phonon/ir_spectra.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.ir_spectra.IRDielectricTensor.nph_freqs"
class="headerlink" title="Link to this definition"></a>  
Number of phonon frequencies.

<span class="sig-name descname"><span class="pre">plot</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">components</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">('xx',)</span></span>*, *<span class="n"><span class="pre">reim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'reim'</span></span>*, *<span class="n"><span class="pre">show_phonon_frequencies</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">xlim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ylim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Axes</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../util/plotting.py#L138-L167"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.ir_spectra.IRDielectricTensor.plot"
class="headerlink" title="Link to this definition"></a>  
Helper function to generate the Spectrum plotter and directly plot the
results.

Parameters<span class="colon">:</span>  
- **components** – A list with the components of the dielectric tensor
  to plot. Can be either two indexes or a string like ‘xx’ to plot the
  (0,0) component

- **reim** – If ‘re’ (im) is present in the string plots the real
  (imaginary) part of the dielectric tensor

- **show_phonon_frequencies** – plot a dot where the phonon frequencies
  are to help identify IR inactive modes

- **xlim** – x-limits of the plot. Defaults to None for automatic
  determination.

- **ylim** – y-limits of the plot. Defaults to None for automatic
  determination.

- **kwargs** – keyword arguments passed to the plotter

Keyword arguments controlling the display of the figure:

| kwargs       | Meaning                                                                                           |
|--------------|---------------------------------------------------------------------------------------------------|
| title        | Title of the plot (Default: None).                                                                |
| show         | True to show the figure (default: True).                                                          |
| savefig      | “abc.png” or “abc.eps” to save the figure to a file.                                              |
| size_kwargs  | Dictionary with options passed to fig.set_size_inches e.g. size_kwargs=dict(w=3, h=4)             |
| tight_layout | True to call fig.tight_layout (default: False)                                                    |
| ax_grid      | True (False) to add (remove) grid from all axes in fig. Default: None i.e. fig is left unchanged. |
| ax_annotate  | Add labels to subplots e.g. (a), (b). Default: False                                              |
| fig_close    | Close figure. Default: False.                                                                     |

<span class="sig-name descname"><span class="pre">write_json</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/ir_spectra.py#L93-L96"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.ir_spectra.IRDielectricTensor.write_json"
class="headerlink" title="Link to this definition"></a>  
Save a JSON file with this data.

</div>

<div id="module-pymatgen.phonon.plotter" class="section">

<span id="pymatgen-phonon-plotter-module"></span>

## pymatgen.phonon.plotter module<a href="#module-pymatgen.phonon.plotter" class="headerlink"
title="Link to this heading"></a>

This module implements plotter for DOS and band structure.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">FreqUnits</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">factor</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L37-L41"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.FreqUnits" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`NamedTuple`</span>

Conversion factor from THz to the required units and the label.

Create new instance of FreqUnits(factor, label)

<span class="sig-name descname"><span class="pre">factor</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/phonon/plotter.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.FreqUnits.factor" class="headerlink"
title="Link to this definition"></a>  
Alias for field number 0

<span class="sig-name descname"><span class="pre">label</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/phonon/plotter.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.FreqUnits.label" class="headerlink"
title="Link to this definition"></a>  
Alias for field number 1

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">GruneisenPhononBSPlotter</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">bs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a
href="#pymatgen.phonon.gruneisen.GruneisenPhononBandStructureSymmLine"
class="reference internal"
title="pymatgen.phonon.gruneisen.GruneisenPhononBandStructureSymmLine"><span
class="pre">GruneisenPhononBandStructureSymmLine</span></a></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L1072-L1296"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.GruneisenPhononBSPlotter"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.phonon.plotter.PhononBSPlotter"
class="reference internal"
title="pymatgen.phonon.plotter.PhononBSPlotter"><span class="pre"><code
class="sourceCode python">PhononBSPlotter</code></span></a>

Plot or get data to facilitate the plot of band structure objects.

Parameters<span class="colon">:</span>  
**bs** – A GruneisenPhononBandStructureSymmLine object.

<span class="sig-name descname"><span class="pre">bs_plot_data</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L1088-L1126"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.GruneisenPhononBSPlotter.bs_plot_data"
class="headerlink" title="Link to this definition"></a>  
Get the data nicely formatted for a plot.

Returns<span class="colon">:</span>  
ticks: A dict with the ‘distances’ at which there is a qpoint (the x
axis) and the labels (None if no label) frequencies: A list (one element
for each branch) of frequencies for each qpoint:
\[branch\]\[qpoint\]\[mode\]. The data is stored by branch to facilitate
the plotting gruneisen: GruneisenPhononBandStructureSymmLine lattice:
The reciprocal lattice.

Return type<span class="colon">:</span>  
A dict of the following format

<span class="sig-name descname"><span class="pre">get_plot_gs</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">ylim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">plot_ph_bs_with_gruneisen</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Axes</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L1128-L1218"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.GruneisenPhononBSPlotter.get_plot_gs"
class="headerlink" title="Link to this definition"></a>  
Get a matplotlib object for the Gruneisen bandstructure plot.

Parameters<span class="colon">:</span>  
- **ylim** – Specify the y-axis (gruneisen) limits; by default None let
  the code choose.

- **plot_ph_bs_with_gruneisen** (*bool*) – Plot phonon band-structure
  with bands coloured as per Gruneisen parameter values on a logarithmic
  scale

- **\*\*kwargs** – additional keywords passed to ax.plot().

<span class="sig-name descname"><span class="pre">plot_compare_gs</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other_plotter</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.phonon.plotter.GruneisenPhononBSPlotter"
class="reference internal"
title="pymatgen.phonon.plotter.GruneisenPhononBSPlotter"><span
class="pre">GruneisenPhononBSPlotter</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Axes</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L1259-L1296"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.plotter.GruneisenPhononBSPlotter.plot_compare_gs"
class="headerlink" title="Link to this definition"></a>  
Plot two band structure for comparison. One is in red the other in blue.
The two band structures need to be defined on the same symmetry lines!
and the distance between symmetry lines is the one of the band structure
used to build the PhononBSPlotter.

Parameters<span class="colon">:</span>  
**other_plotter**
(<a href="#pymatgen.phonon.plotter.GruneisenPhononBSPlotter"
class="reference internal"
title="pymatgen.phonon.plotter.GruneisenPhononBSPlotter"><em>GruneisenPhononBSPlotter</em></a>)
– another phonon DOS plotter defined along the same symmetry lines.

Raises<span class="colon">:</span>  
**ValueError** – if the two plotters are incompatible (due to different
data lengths)

Returns<span class="colon">:</span>  
with both band structures

Return type<span class="colon">:</span>  
plt.Axes

<span class="sig-name descname"><span class="pre">save_plot_gs</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*, *<span class="n"><span class="pre">img_format</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'eps'</span></span>*, *<span class="n"><span class="pre">ylim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">plot_ph_bs_with_gruneisen</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L1237-L1257"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.GruneisenPhononBSPlotter.save_plot_gs"
class="headerlink" title="Link to this definition"></a>  
Save matplotlib plot to a file.

Parameters<span class="colon">:</span>  
- **filename** – Filename to write to.

- **img_format** – Image format to use. Defaults to EPS.

- **ylim** – Specifies the y-axis limits.

- **plot_ph_bs_with_gruneisen** – Plot phonon band-structure with bands
  coloured as per Gruneisen parameter values on a logarithmic scale

- **\*\*kwargs** – kwargs passed to get_plot_gs

<span class="sig-name descname"><span class="pre">show_gs</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">ylim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">plot_ph_bs_with_gruneisen</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L1220-L1235"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.GruneisenPhononBSPlotter.show_gs"
class="headerlink" title="Link to this definition"></a>  
Show the plot using matplotlib.

Parameters<span class="colon">:</span>  
- **ylim** – Specifies the y-axis limits.

- **plot_ph_bs_with_gruneisen** – Plot phonon band-structure with bands
  coloured as per Gruneisen parameter values on a logarithmic scale

- **\*\*kwargs** – kwargs passed to get_plot_gs

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">GruneisenPlotter</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">gruneisen</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.phonon.gruneisen.GruneisenParameter"
class="reference internal"
title="pymatgen.phonon.gruneisen.GruneisenParameter"><span
class="pre">GruneisenParameter</span></a></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L999-L1069"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.GruneisenPlotter" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Plot GruneisenParameter.

Plot information from GruneisenParameter.

Parameters<span class="colon">:</span>  
**gruneisen** (<a href="#pymatgen.phonon.gruneisen.GruneisenParameter"
class="reference internal"
title="pymatgen.phonon.gruneisen.GruneisenParameter"><em>GruneisenParameter</em></a>)
– containing the data to plot.

<span class="sig-name descname"><span class="pre">get_plot</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">marker</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'o'</span></span>*, *<span class="n"><span class="pre">markersize</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">units</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'thz'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'ev'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'mev'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'ha'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cm-1'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cm^-1'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'thz'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Axes</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L1010-L1043"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.GruneisenPlotter.get_plot"
class="headerlink" title="Link to this definition"></a>  
Will produce a plot.

Parameters<span class="colon">:</span>  
- **marker** – marker for the depiction

- **markersize** – size of the marker

- **units** – unit for the plots, accepted units: thz, ev, mev, ha,
  cm-1, cm^-1.

Returns<span class="colon">:</span>  
matplotlib axes object

Return type<span class="colon">:</span>  
plt.Axes

<span class="sig-name descname"><span class="pre">save_plot</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*, *<span class="n"><span class="pre">img_format</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'pdf'</span></span>*, *<span class="n"><span class="pre">units</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'thz'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'ev'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'mev'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'ha'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cm-1'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cm^-1'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'thz'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L1054-L1069"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.GruneisenPlotter.save_plot"
class="headerlink" title="Link to this definition"></a>  
Will save the plot to a file.

Parameters<span class="colon">:</span>  
- **filename** – name of the filename

- **img_format** – format of the saved plot

- **units** – accepted units: thz, ev, mev, ha, cm-1, cm^-1.

<span class="sig-name descname"><span class="pre">show</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">units</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'thz'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'ev'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'mev'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'ha'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cm-1'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cm^-1'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'thz'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L1045-L1052"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.GruneisenPlotter.show"
class="headerlink" title="Link to this definition"></a>  
Will show the plot.

Parameters<span class="colon">:</span>  
**units** – units for the plot, accepted units: thz, ev, mev, ha, cm-1,
cm^-1.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">PhononBSPlotter</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">bs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.phonon.bandstructure.PhononBandStructureSymmLine"
class="reference internal"
title="pymatgen.phonon.bandstructure.PhononBandStructureSymmLine"><span
class="pre">PhononBandStructureSymmLine</span></a></span>*, *<span class="n"><span class="pre">label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L308-L777"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.PhononBSPlotter" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Plot or get data to facilitate the plot of band structure objects.

Parameters<span class="colon">:</span>  
- **bs** – A PhononBandStructureSymmLine object.

- **label** – A label for the plot. Defaults to None for no label. Esp.
  useful with the plot_compare method to distinguish the band
  structures.

<span class="sig-name descname"><span class="pre">bs_plot_data</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L347-L378"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.PhononBSPlotter.bs_plot_data"
class="headerlink" title="Link to this definition"></a>  
Get the data nicely formatted for a plot.

Returns<span class="colon">:</span>  
ticks: A dict with the ‘distances’ at which there is a qpoint (the x
axis) and the labels (None if no label) frequencies: A list (one element
for each branch) of frequencies for each qpoint:
\[branch\]\[qpoint\]\[mode\]. The data is stored by branch to facilitate
the plotting lattice: The reciprocal lattice.

Return type<span class="colon">:</span>  
A dict of the following format

<span class="sig-name descname"><span class="pre">get_plot</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">ylim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">units</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'thz'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'ev'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'mev'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'ha'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cm-1'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cm^-1'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'thz'</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Axes</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L380-L424"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.PhononBSPlotter.get_plot"
class="headerlink" title="Link to this definition"></a>  
Get a matplotlib object for the bandstructure plot.

Parameters<span class="colon">:</span>  
- **ylim** – Specify the y-axis (frequency) limits; by default None let
  the code choose.

- **units** – units for the frequencies. Accepted values thz, ev, mev,
  ha, cm-1, cm^-1. Defaults to “thz”.

- **\*\*kwargs** – passed to ax.plot function.

<span class="sig-name descname"><span class="pre">get_proj_plot</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">site_comb</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'element'</span></span>*, *<span class="n"><span class="pre">ylim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">units</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'thz'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'ev'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'mev'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'ha'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cm-1'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cm^-1'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'thz'</span></span>*, *<span class="n"><span class="pre">rgb_labels</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Axes</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L463-L562"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.PhononBSPlotter.get_proj_plot"
class="headerlink" title="Link to this definition"></a>  
Get a matplotlib object for the bandstructure plot projected along
atomic sites.

Parameters<span class="colon">:</span>  
- **site_comb** – a list of list, for example,
  \[\[0\],\[1\],\[2,3,4\]\]; the numbers in each sublist represents the
  indices of atoms; the atoms in a same sublist will be plotted in a
  same color; if not specified, unique elements are automatically
  grouped.

- **ylim** – Specify the y-axis (frequency) limits; by default None let
  the code choose.

- **units** – units for the frequencies. Accepted values thz, ev, mev,
  ha, cm-1, cm^-1. Defaults to “thz”.

- **rgb_labels** – a list of rgb colors for the labels; if not
  specified, the colors will be automatically generated.

<span class="sig-name descname"><span class="pre">get_ticks</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L619-L656"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.PhononBSPlotter.get_ticks"
class="headerlink" title="Link to this definition"></a>  
Get all ticks and labels for a band structure plot.

Returns<span class="colon">:</span>  
a list of distance at which ticks should be set and ‘label’: a list of
label for each of those ticks.

Return type<span class="colon">:</span>  
A dict with ‘distance’

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">n_bands</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/phonon/plotter.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.PhononBSPlotter.n_bands"
class="headerlink" title="Link to this definition"></a>  
Number of bands.

<span class="sig-name descname"><span class="pre">plot_brillouin</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L763-L777"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.PhononBSPlotter.plot_brillouin"
class="headerlink" title="Link to this definition"></a>  
Plot the Brillouin zone.

<span class="sig-name descname"><span class="pre">plot_compare</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other_plotter</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.phonon.plotter.PhononBSPlotter"
class="reference internal"
title="pymatgen.phonon.plotter.PhononBSPlotter"><span
class="pre">PhononBSPlotter</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><a href="#pymatgen.phonon.plotter.PhononBSPlotter"
class="reference internal"
title="pymatgen.phonon.plotter.PhononBSPlotter"><span
class="pre">PhononBSPlotter</span></a><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">units</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'thz'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'ev'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'mev'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'ha'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cm-1'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cm^-1'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'thz'</span></span>*, *<span class="n"><span class="pre">self_label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'self'</span></span>*, *<span class="n"><span class="pre">colors</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">legend_kwargs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">on_incompatible</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'raise'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'warn'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'ignore'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'raise'</span></span>*, *<span class="n"><span class="pre">other_kwargs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Axes</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L658-L761"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.PhononBSPlotter.plot_compare"
class="headerlink" title="Link to this definition"></a>  
Plot two band structure for comparison. self in blue, others in red,
green, … The band structures need to be defined on the same symmetry
lines! The distance between symmetry lines is determined by the band
structure used to initialize PhononBSPlotter (self).

Parameters<span class="colon">:</span>  
- **other_plotter** (<a href="#pymatgen.phonon.plotter.PhononBSPlotter"
  class="reference internal"
  title="pymatgen.phonon.plotter.PhononBSPlotter"><em>PhononBSPlotter</em></a>
  *\|* *dict\[str,* <a href="#pymatgen.phonon.plotter.PhononBSPlotter"
  class="reference internal"
  title="pymatgen.phonon.plotter.PhononBSPlotter"><em>PhononBSPlotter</em></a>*\]*)
  – Other PhononBSPlotter object(s) defined along the same symmetry
  lines

- **units** (*str*) – units for the frequencies. Accepted values thz,
  ev, mev, ha, cm-1, cm^-1. Defaults to ‘thz’.

- **self_label** (*str*) – label for the self band structure. Defaults
  to to the label passed to PhononBSPlotter.init or, if None, ‘self’.

- **colors** (*list\[str\]*) – list of colors for the other band
  structures. Defaults to None for automatic colors.

- **legend_kwargs** – dict\[str, Any\]: kwargs passed to ax.legend().

- **on_incompatible** (*'raise'* *\|* *'warn'* *\|* *'ignore'*) – What
  to do if the band structures are not compatible. Defaults to ‘raise’.

- **other_kwargs** – dict\[str, Any\]: kwargs passed to other_plotter
  ax.plot().

- **\*\*kwargs** – passed to ax.plot().

Returns<span class="colon">:</span>  
with two band structures.

Return type<span class="colon">:</span>  
plt.Axes

<span class="sig-name descname"><span class="pre">save_plot</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*, *<span class="n"><span class="pre">ylim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">units</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'thz'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'ev'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'mev'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'ha'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cm-1'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cm^-1'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'thz'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L578-L593"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.PhononBSPlotter.save_plot"
class="headerlink" title="Link to this definition"></a>  
Save matplotlib plot to a file.

Parameters<span class="colon">:</span>  
- **filename** (*str* *\|* *Path*) – Filename to write to.

- **ylim** (*float*) – Specifies the y-axis limits.

- **units** (*"thz"* *\|* *"ev"* *\|* *"mev"* *\|* *"ha"* *\|* *"cm-1"*
  *\|* *"cm^-1"*) – units for the frequencies.

<span class="sig-name descname"><span class="pre">show</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">ylim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">units</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'thz'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'ev'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'mev'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'ha'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cm-1'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cm^-1'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'thz'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L564-L576"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.PhononBSPlotter.show"
class="headerlink" title="Link to this definition"></a>  
Show the plot using matplotlib.

Parameters<span class="colon">:</span>  
- **ylim** (*float*) – Specifies the y-axis limits.

- **units** (*"thz"* *\|* *"ev"* *\|* *"mev"* *\|* *"ha"* *\|* *"cm-1"*
  *\|* *"cm^-1"*) – units for the frequencies.

<span class="sig-name descname"><span class="pre">show_proj</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">site_comb</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'element'</span></span>*, *<span class="n"><span class="pre">ylim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">units</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'thz'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'ev'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'mev'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'ha'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cm-1'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cm^-1'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'thz'</span></span>*, *<span class="n"><span class="pre">rgb_labels</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L595-L617"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.PhononBSPlotter.show_proj"
class="headerlink" title="Link to this definition"></a>  
Show the projected plot using matplotlib.

Parameters<span class="colon">:</span>  
- **site_comb** – A list of list of indices of sites to combine. For
  example, \[\[0, 1\], \[2, 3\]\] will combine the projections of sites
  0 and 1, and sites 2 and 3. Defaults to “element”, which will combine
  sites by element.

- **ylim** – Specify the y-axis (frequency) limits; by default None let
  the code choose.

- **units** – units for the frequencies. Accepted values thz, ev, mev,
  ha, cm-1, cm^-1. Defaults to “thz”.

- **rgb_labels** – A list of labels for the rgb triangle. Defaults to
  None, which will use the element symbols.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">PhononDosPlotter</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">stack</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">sigma</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L75-L305"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.PhononDosPlotter" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Plot phonon DOSs. The interface is very flexible to accommodate the many
different ways in which people want to view DOS. Typical usage is:

> <div>
>
> \# Initializes plotter with some optional args. Defaults are usually
> fine plotter = PhononDosPlotter().
>
> \# Add DOS with a label plotter.add_dos(“Total DOS”, dos)
>
> \# Alternatively, you can add a dict of DOSes. This is the typical
> form \# returned by CompletePhononDos.get_element_dos().
>
> </div>

Parameters<span class="colon">:</span>  
- **stack** – Whether to plot the DOS as a stacked area graph

- **sigma** – A float specifying a standard deviation for Gaussian
  smearing the DOS for nicer looking plots. Defaults to None for no
  smearing.

<span class="sig-name descname"><span class="pre">add_dos</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">dos</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.phonon.dos.PhononDos" class="reference internal"
title="pymatgen.phonon.dos.PhononDos"><span
class="pre">PhononDos</span></a></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L106-L119"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.PhononDosPlotter.add_dos"
class="headerlink" title="Link to this definition"></a>  
Add a dos for plotting.

Parameters<span class="colon">:</span>  
- **label** (*str*) – label for the DOS. Must be unique.

- **dos**
  (<a href="#pymatgen.phonon.dos.PhononDos" class="reference internal"
  title="pymatgen.phonon.dos.PhononDos"><em>PhononDos</em></a>) – DOS
  object

- **\*\*kwargs** – kwargs supported by matplotlib.pyplot.plot

<span class="sig-name descname"><span class="pre">add_dos_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dos_dict</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*, *<span class="n"><span class="pre">key_sort_func</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L121-L131"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.PhononDosPlotter.add_dos_dict"
class="headerlink" title="Link to this definition"></a>  
Add a dictionary of doses, with an optional sorting function for the
keys.

Parameters<span class="colon">:</span>  
- **dos_dict** – dict of {label: Dos}

- **key_sort_func** – function used to sort the dos_dict keys.

<span class="sig-name descname"><span class="pre">get_dos_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L133-L141"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.PhononDosPlotter.get_dos_dict"
class="headerlink" title="Link to this definition"></a>  
Get the added doses as a json-serializable dict. Note that if you have
specified smearing for the DOS plot, the densities returned will be the
smeared densities, not the original densities.

Returns<span class="colon">:</span>  
DOS data. Generally of the form {label: {‘frequencies’:.., ‘densities’:
…}}

Return type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">get_plot</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">xlim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ylim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">invert_axes</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">units</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'thz'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'ev'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'mev'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'ha'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cm-1'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cm^-1'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'thz'</span></span>*, *<span class="n"><span class="pre">legend</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ax</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Axes</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Axes</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L143-L260"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.PhononDosPlotter.get_plot"
class="headerlink" title="Link to this definition"></a>  
Get a matplotlib plot showing the DOS.

Parameters<span class="colon">:</span>  
- **xlim** – Specifies the x-axis limits. Set to None for automatic
  determination.

- **ylim** – Specifies the y-axis limits.

- **invert_axes** (*bool*) – Whether to invert the x and y axes. Enables
  chemist style DOS plotting. Defaults to False.

- **units** (*thz* *\|* *ev* *\|* *mev* *\|* *ha* *\|* *cm-1* *\|*
  *cm^-1*) – units for the frequencies. Defaults to “thz”.

- **legend** – dict with legend options. For example, {“loc”: “upper
  right”} will place the legend in the upper right corner. Defaults to
  {“fontsize”: 30}.

- **ax** (*Axes*) – An existing axes object onto which the plot will be
  added. If None, a new figure will be created.

<span class="sig-name descname"><span class="pre">save_plot</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*, *<span class="n"><span class="pre">img_format</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'eps'</span></span>*, *<span class="n"><span class="pre">xlim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ylim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">invert_axes</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">units</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'thz'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'ev'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'mev'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'ha'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cm-1'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cm^-1'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'thz'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L262-L285"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.PhononDosPlotter.save_plot"
class="headerlink" title="Link to this definition"></a>  
Save matplotlib plot to a file.

Parameters<span class="colon">:</span>  
- **filename** – Filename to write to.

- **img_format** – Image format to use. Defaults to EPS.

- **xlim** – Specifies the x-axis limits. Set to None for automatic
  determination.

- **ylim** – Specifies the y-axis limits.

- **invert_axes** – Whether to invert the x and y axes. Enables chemist
  style DOS plotting. Defaults to False.

- **units** – units for the frequencies. Accepted values thz, ev, mev,
  ha, cm-1, cm^-1

<span class="sig-name descname"><span class="pre">show</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">xlim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ylim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">invert_axes</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">units</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'thz'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'ev'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'mev'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'ha'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cm-1'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cm^-1'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'thz'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L287-L305"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.PhononDosPlotter.show"
class="headerlink" title="Link to this definition"></a>  
Show the plot using matplotlib.

Parameters<span class="colon">:</span>  
- **xlim** – Specifies the x-axis limits. Set to None for automatic
  determination.

- **ylim** – Specifies the y-axis limits.

- **invert_axes** – Whether to invert the x and y axes. Enables chemist
  style DOS plotting. Defaults to False.

- **units** – units for the frequencies. Accepted values thz, ev, mev,
  ha, cm-1, cm^-1.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ThermoPlotter</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dos</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.phonon.dos.PhononDos" class="reference internal"
title="pymatgen.phonon.dos.PhononDos"><span
class="pre">PhononDos</span></a></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L780-L996"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.ThermoPlotter" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Plotter for thermodynamic properties obtained from phonon DOS. If the
structure corresponding to the DOS, it will be used to extract the
formula unit and provide the plots in units of mol instead of mole-cell.

Parameters<span class="colon">:</span>  
- **dos** – A PhononDos object.

- **structure** – A Structure object corresponding to the structure used
  for the calculation.

<span class="sig-name descname"><span class="pre">plot_cv</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tmin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">tmax</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">ntemp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">ylim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Figure</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../util/plotting.py#L843-L861"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.ThermoPlotter.plot_cv"
class="headerlink" title="Link to this definition"></a>  
Plots the constant volume specific heat C_v in a temperature range.

Parameters<span class="colon">:</span>  
- **tmin** – minimum temperature

- **tmax** – maximum temperature

- **ntemp** – number of steps

- **ylim** – tuple specifying the y-axis limits.

- **kwargs** – kwargs passed to the matplotlib function ‘plot’.

Returns<span class="colon">:</span>  
matplotlib figure

Return type<span class="colon">:</span>  
plt.figure

Keyword arguments controlling the display of the figure:

| kwargs       | Meaning                                                                                           |
|--------------|---------------------------------------------------------------------------------------------------|
| title        | Title of the plot (Default: None).                                                                |
| show         | True to show the figure (default: True).                                                          |
| savefig      | “abc.png” or “abc.eps” to save the figure to a file.                                              |
| size_kwargs  | Dictionary with options passed to fig.set_size_inches e.g. size_kwargs=dict(w=3, h=4)             |
| tight_layout | True to call fig.tight_layout (default: False)                                                    |
| ax_grid      | True (False) to add (remove) grid from all axes in fig. Default: None i.e. fig is left unchanged. |
| ax_annotate  | Add labels to subplots e.g. (a), (b). Default: False                                              |
| fig_close    | Close figure. Default: False.                                                                     |

<span class="sig-name descname"><span class="pre">plot_entropy</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tmin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">tmax</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">ntemp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">ylim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Figure</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../util/plotting.py#L863-L881"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.ThermoPlotter.plot_entropy"
class="headerlink" title="Link to this definition"></a>  
Plots the vibrational entrpy in a temperature range.

Parameters<span class="colon">:</span>  
- **tmin** – minimum temperature

- **tmax** – maximum temperature

- **ntemp** – number of steps

- **ylim** – tuple specifying the y-axis limits.

- **kwargs** – kwargs passed to the matplotlib function ‘plot’.

Returns<span class="colon">:</span>  
matplotlib figure

Return type<span class="colon">:</span>  
plt.figure

Keyword arguments controlling the display of the figure:

| kwargs       | Meaning                                                                                           |
|--------------|---------------------------------------------------------------------------------------------------|
| title        | Title of the plot (Default: None).                                                                |
| show         | True to show the figure (default: True).                                                          |
| savefig      | “abc.png” or “abc.eps” to save the figure to a file.                                              |
| size_kwargs  | Dictionary with options passed to fig.set_size_inches e.g. size_kwargs=dict(w=3, h=4)             |
| tight_layout | True to call fig.tight_layout (default: False)                                                    |
| ax_grid      | True (False) to add (remove) grid from all axes in fig. Default: None i.e. fig is left unchanged. |
| ax_annotate  | Add labels to subplots e.g. (a), (b). Default: False                                              |
| fig_close    | Close figure. Default: False.                                                                     |

<span class="sig-name descname"><span class="pre">plot_helmholtz_free_energy</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tmin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">tmax</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">ntemp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">ylim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Figure</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../util/plotting.py#L910-L937"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.plotter.ThermoPlotter.plot_helmholtz_free_energy"
class="headerlink" title="Link to this definition"></a>  
Plots the vibrational contribution to the Helmoltz free energy in a
temperature range.

Parameters<span class="colon">:</span>  
- **tmin** – minimum temperature

- **tmax** – maximum temperature

- **ntemp** – number of steps

- **ylim** – tuple specifying the y-axis limits.

- **kwargs** – kwargs passed to the matplotlib function ‘plot’.

Returns<span class="colon">:</span>  
matplotlib figure

Return type<span class="colon">:</span>  
plt.figure

Keyword arguments controlling the display of the figure:

| kwargs       | Meaning                                                                                           |
|--------------|---------------------------------------------------------------------------------------------------|
| title        | Title of the plot (Default: None).                                                                |
| show         | True to show the figure (default: True).                                                          |
| savefig      | “abc.png” or “abc.eps” to save the figure to a file.                                              |
| size_kwargs  | Dictionary with options passed to fig.set_size_inches e.g. size_kwargs=dict(w=3, h=4)             |
| tight_layout | True to call fig.tight_layout (default: False)                                                    |
| ax_grid      | True (False) to add (remove) grid from all axes in fig. Default: None i.e. fig is left unchanged. |
| ax_annotate  | Add labels to subplots e.g. (a), (b). Default: False                                              |
| fig_close    | Close figure. Default: False.                                                                     |

<span class="sig-name descname"><span class="pre">plot_internal_energy</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tmin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">tmax</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">ntemp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">ylim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Figure</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../util/plotting.py#L883-L908"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.ThermoPlotter.plot_internal_energy"
class="headerlink" title="Link to this definition"></a>  
Plots the vibrational internal energy in a temperature range.

Parameters<span class="colon">:</span>  
- **tmin** – minimum temperature

- **tmax** – maximum temperature

- **ntemp** – number of steps

- **ylim** – tuple specifying the y-axis limits.

- **kwargs** – kwargs passed to the matplotlib function ‘plot’.

Returns<span class="colon">:</span>  
matplotlib figure

Return type<span class="colon">:</span>  
plt.figure

Keyword arguments controlling the display of the figure:

| kwargs       | Meaning                                                                                           |
|--------------|---------------------------------------------------------------------------------------------------|
| title        | Title of the plot (Default: None).                                                                |
| show         | True to show the figure (default: True).                                                          |
| savefig      | “abc.png” or “abc.eps” to save the figure to a file.                                              |
| size_kwargs  | Dictionary with options passed to fig.set_size_inches e.g. size_kwargs=dict(w=3, h=4)             |
| tight_layout | True to call fig.tight_layout (default: False)                                                    |
| ax_grid      | True (False) to add (remove) grid from all axes in fig. Default: None i.e. fig is left unchanged. |
| ax_annotate  | Add labels to subplots e.g. (a), (b). Default: False                                              |
| fig_close    | Close figure. Default: False.                                                                     |

<span class="sig-name descname"><span class="pre">plot_thermodynamic_properties</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tmin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">tmax</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*, *<span class="n"><span class="pre">ntemp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">ylim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Figure</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../util/plotting.py#L939-L996"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.plotter.ThermoPlotter.plot_thermodynamic_properties"
class="headerlink" title="Link to this definition"></a>  
Plots all the thermodynamic properties in a temperature range.

Parameters<span class="colon">:</span>  
- **tmin** – minimum temperature

- **tmax** – maximum temperature

- **ntemp** – number of steps

- **ylim** – tuple specifying the y-axis limits.

- **kwargs** – kwargs passed to the matplotlib function ‘plot’.

Returns<span class="colon">:</span>  
matplotlib figure

Return type<span class="colon">:</span>  
plt.figure

Keyword arguments controlling the display of the figure:

| kwargs       | Meaning                                                                                           |
|--------------|---------------------------------------------------------------------------------------------------|
| title        | Title of the plot (Default: None).                                                                |
| show         | True to show the figure (default: True).                                                          |
| savefig      | “abc.png” or “abc.eps” to save the figure to a file.                                              |
| size_kwargs  | Dictionary with options passed to fig.set_size_inches e.g. size_kwargs=dict(w=3, h=4)             |
| tight_layout | True to call fig.tight_layout (default: False)                                                    |
| ax_grid      | True (False) to add (remove) grid from all axes in fig. Default: None i.e. fig is left unchanged. |
| ax_annotate  | Add labels to subplots e.g. (a), (b). Default: False                                              |
| fig_close    | Close figure. Default: False.                                                                     |

<!-- -->

<span class="sig-name descname"><span class="pre">freq_units</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">units</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'thz'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'ev'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'mev'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'ha'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cm-1'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'cm^-1'</span></span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.phonon.plotter.FreqUnits" class="reference internal"
title="pymatgen.phonon.plotter.FreqUnits"><span
class="pre">FreqUnits</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/plotter.py#L44-L72"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.phonon.plotter.freq_units" class="headerlink"
title="Link to this definition"></a>  
Parameters<span class="colon">:</span>  
**units** – str, accepted values: thz, ev, mev, ha, cm-1, cm^-1.

Returns<span class="colon">:</span>  
Conversion factor from THz to the required units and the label in the
form of a namedtuple.

</div>

<div id="module-pymatgen.phonon.thermal_displacements" class="section">

<span id="pymatgen-phonon-thermal-displacements-module"></span>

## pymatgen.phonon.thermal_displacements module<a href="#module-pymatgen.phonon.thermal_displacements"
class="headerlink" title="Link to this heading"></a>

This module provides classes to handle thermal displacement matrices
(anisotropic displacement parameters).

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ThermalDisplacementMatrices</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">thermal_displacement_matrix_cart</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">temperature</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span>*, *<span class="n"><span class="pre">thermal_displacement_matrix_cif</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/thermal_displacements.py#L39-L571"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Handle thermal displacement matrices This class stores thermal
displacement matrices in Ucart format.

An earlier implementation based on Matlab can be found here:
<a href="https://github.com/JaGeo/MolecularToolbox"
class="reference external">https://github.com/JaGeo/MolecularToolbox</a>
( J. George, A. Wang, V. L. Deringer, R. Wang, R. Dronskowski, U.
Englert, CrystEngComm, 2015, 17, 7414-7422.)

Parameters<span class="colon">:</span>  
- **thermal_displacement_matrix_cart** – 2D numpy array including the
  thermal_displacement matrix Ucart 1st dimension atom types, then
  compressed thermal displacement matrix will follow U11, U22, U33, U23,
  U13, U12 (xx, yy, zz, yz, xz, xy) convention similar to
  “thermal_displacement_matrices.yaml” in phonopy

- **structure** – A pymatgen Structure object

- **temperature** – temperature at which thermal displacement matrix was
  determined

- **thermal_displacement_matrix_cif** – 2D numpy array including the
  thermal_displacement matrix Ucif format 1st dimension atom types, then
  compressed thermal displacement matrix will follow U11, U22, U33, U23,
  U13, U12 (xx, yy, zz, yz, xz, xy) convention similar to
  “thermal_displacement_matrices.yaml” in phonopy.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">B</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ndarray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/phonon/thermal_displacements.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.B"
class="headerlink" title="Link to this definition"></a>  
Computation as described in R. W. Grosse-Kunstleve, P. D. Adams, J Appl
Cryst 2002, 35, 477-480.

Returns<span class="colon">:</span>  
First dimension are the atoms in the structure.

Return type<span class="colon">:</span>  
np.array

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">U1U2U3</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/phonon/thermal_displacements.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.U1U2U3"
class="headerlink" title="Link to this definition"></a>  
Computation as described in R. W. Grosse-Kunstleve, P. D. Adams, J Appl
Cryst 2002, 35, 477-480.

Returns<span class="colon">:</span>  
eigenvalues of Ucart. First dimension are the atoms in the structure.

Return type<span class="colon">:</span>  
np.array

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Ucif</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ndarray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/phonon/thermal_displacements.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.Ucif"
class="headerlink" title="Link to this definition"></a>  
Computation as described in R. W. Grosse-Kunstleve, P. D. Adams, J Appl
Cryst 2002, 35, 477-480.

Returns<span class="colon">:</span>  
Ucif as array. First dimension are the atoms in the structure.

Return type<span class="colon">:</span>  
np.array

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Ustar</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ndarray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/phonon/thermal_displacements.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.Ustar"
class="headerlink" title="Link to this definition"></a>  
Computation as described in R. W. Grosse-Kunstleve, P. D. Adams, J Appl
Cryst 2002, 35, 477-480.

Returns<span class="colon">:</span>  
Ustar as array. First dimension are the atoms in the structure.

Return type<span class="colon">:</span>  
np.array

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">beta</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/phonon/thermal_displacements.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.beta"
class="headerlink" title="Link to this definition"></a>  
Computation as described in R. W. Grosse-Kunstleve, P. D. Adams, J Appl
Cryst 2002, 35, 477-480.

Returns<span class="colon">:</span>  
First dimension are the atoms in the structure.

Return type<span class="colon">:</span>  
np.array

<span class="sig-name descname"><span class="pre">compute_directionality_quality_criterion</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a
href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices"
class="reference internal"
title="pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices"><span
class="pre">ThermalDisplacementMatrices</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">ArrayLike</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/thermal_displacements.py#L246-L308"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.compute_directionality_quality_criterion"
class="headerlink" title="Link to this definition"></a>  
Will compute directionality of prolate displacement ellipsoids as
described in <a href="https://doi.org/10.1039/C9CE00794F"
class="reference external">https://doi.org/10.1039/C9CE00794F</a> with
the earlier implementation: <a href="https://github.com/damMroz/Angle/"
class="reference external">https://github.com/damMroz/Angle/</a>.

Parameters<span class="colon">:</span>  
- **other** – ThermalDisplacementMatrix

- **compared** (*please make sure that the order* *of* *the atoms in
  both objects that are*)

- **Otherwise** (*is the same.*)

- **results** (*this analysis will deliver wrong*)

Returns<span class="colon">:</span>  
will return a list including dicts for each atom that include “vector0”
(largest principal axes of self object),

> <div>
>
> ”vector1” (largest principal axes of the other object), “angle” between both axes,  
> These vectors can then, for example, be drawn into the structure with
> VESTA. Vectors are given in Cartesian coordinates
>
> </div>

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_Ucif</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">thermal_displacement_matrix_cif</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">temperature</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/thermal_displacements.py#L414-L458"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.from_Ucif"
class="headerlink" title="Link to this definition"></a>  
Starting from a numpy array, it will convert Ucif values into Ucart
values and initialize the class.

Parameters<span class="colon">:</span>  
- **thermal_displacement_matrix_cif** – np.array, first dimension are
  the atoms, then reduced form of thermal displacement matrix will
  follow Order as above: U11, U22, U33, U23, U13, U12

- **structure** – Structure object

- **temperature** – float Corresponding temperature

Returns<span class="colon">:</span>  
ThermalDisplacementMatrices

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_cif_P1</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a
href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices"
class="reference internal"
title="pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices"><span
class="pre">ThermalDisplacementMatrices</span></a><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/thermal_displacements.py#L511-L571"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.from_cif_P1"
class="headerlink" title="Link to this definition"></a>  
Reads a CIF with P1 symmetry including positions and ADPs. Currently, no
check of symmetry is performed as CifParser methods cannot be easily
reused.

Parameters<span class="colon">:</span>  
**filename** – Filename of the CIF.

Returns<span class="colon">:</span>  
ThermalDisplacementMatrices

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_structure_with_site_properties_Ucif</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">temperature</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/thermal_displacements.py#L494-L509"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.from_structure_with_site_properties_Ucif"
class="headerlink" title="Link to this definition"></a>  
Will create this object with the help of a structure with site
properties.

Parameters<span class="colon">:</span>  
- **structure** – Structure object including U11_cif, U22_cif, U33_cif,
  U23_cif, U13_cif, U12_cif as site

- **properties**

- **temperature** – temperature for Ucif data

Returns<span class="colon">:</span>  
ThermalDisplacementMatrices

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">get_full_matrix</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">thermal_displacement</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">np.ndarray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/thermal_displacements.py#L86-L111"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.get_full_matrix"
class="headerlink" title="Link to this definition"></a>  
Transfers the reduced matrix to the full matrix (order of reduced matrix
U11, U22, U33, U23, U13, U12).

Parameters<span class="colon">:</span>  
**thermal_displacement** – 2d numpy array, first dimension are the atoms

Returns<span class="colon">:</span>  
3d numpy array including thermal displacements, first dimensions are the
atoms

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">get_reduced_matrix</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">thermal_displacement</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">np.ndarray</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/thermal_displacements.py#L113-L135"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.get_reduced_matrix"
class="headerlink" title="Link to this definition"></a>  
Transfers the full matrix to reduced matrix (order of reduced matrix
U11, U22, U33, U23, U13, U12).

Parameters<span class="colon">:</span>  
**thermal_displacement** – 2d numpy array, first dimension are the atoms

Returns<span class="colon">:</span>  
3d numpy array including thermal displacements, first dimensions are the
atoms

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ratio_prolate</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ndarray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/phonon/thermal_displacements.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.ratio_prolate"
class="headerlink" title="Link to this definition"></a>  
This will compute ratio between largest and smallest eigenvalue of
Ucart.

<span class="sig-name descname"><span class="pre">to_structure_with_site_properties_Ucif</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/thermal_displacements.py#L460-L492"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.to_structure_with_site_properties_Ucif"
class="headerlink" title="Link to this definition"></a>  
Transfers this object into a structure with site properties (Ucif). This
is useful for sorting the atoms in the structure including site
properties. e.g. with code like this: def sort_order(site):

> <div>
>
> return \[site.specie.X, site.frac_coords\[0\], site.frac_coords\[1\],
> site.frac_coords\[2\]\]
>
> </div>

new_structure0 = Structure.from_sites(sorted(structure0,
key=sort_order)).

Returns<span class="colon">:</span>  
Structure

<span class="sig-name descname"><span class="pre">visualize_directionality_quality_criterion</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a
href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices"
class="reference internal"
title="pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices"><span
class="pre">ThermalDisplacementMatrices</span></a></span>*, *<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'visualization.vesta'</span></span>*, *<span class="n"><span class="pre">which_structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="m"><span class="pre">0</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="m"><span class="pre">1</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/thermal_displacements.py#L310-L407"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.visualize_directionality_quality_criterion"
class="headerlink" title="Link to this definition"></a>  
Will create a VESTA file for visualization of the directionality
criterion.

Parameters<span class="colon">:</span>  
- **other** – ThermalDisplacementMatrices

- **filename** – Filename of the VESTA file

- **which_structure** – 0 means structure of the self object will be
  used, 1 means structure of the other object will be used

<span class="sig-name descname"><span class="pre">write_cif</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../phonon/thermal_displacements.py#L211-L236"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.phonon.thermal_displacements.ThermalDisplacementMatrices.write_cif"
class="headerlink" title="Link to this definition"></a>  
Write a CIF including thermal displacements.

Parameters<span class="colon">:</span>  
**filename** – name of the CIF file

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
