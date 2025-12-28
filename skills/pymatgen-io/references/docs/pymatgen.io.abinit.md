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

- <a href="#" class="reference internal">pymatgen.io.abinit package</a>
  - <a href="#submodules" class="reference internal">Submodules</a>
  - <a href="#module-pymatgen.io.abinit.abiobjects"
    class="reference internal">pymatgen.io.abinit.abiobjects module</a>
    - <a href="#pymatgen.io.abinit.abiobjects.AbivarAble"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">AbivarAble</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.AbivarAble.to_abivars"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbivarAble.to_abivars()</code></span></a>
    - <a href="#pymatgen.io.abinit.abiobjects.Constraints"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Constraints</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.Constraints.to_abivars"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Constraints.to_abivars()</code></span></a>
    - <a href="#pymatgen.io.abinit.abiobjects.Electrons"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Electrons</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.Electrons.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Electrons.as_dict()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.Electrons.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Electrons.from_dict()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.Electrons.nspden"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Electrons.nspden</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.Electrons.nspinor"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Electrons.nspinor</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.Electrons.nsppol"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Electrons.nsppol</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.Electrons.to_abivars"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Electrons.to_abivars()</code></span></a>
    - <a href="#pymatgen.io.abinit.abiobjects.ElectronsAlgorithm"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">ElectronsAlgorithm</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.ElectronsAlgorithm.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElectronsAlgorithm.as_dict()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.ElectronsAlgorithm.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElectronsAlgorithm.from_dict()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.ElectronsAlgorithm.to_abivars"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ElectronsAlgorithm.to_abivars()</code></span></a>
    - <a href="#pymatgen.io.abinit.abiobjects.ExcHamiltonian"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">ExcHamiltonian</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.ExcHamiltonian.inclvkb"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ExcHamiltonian.inclvkb</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.ExcHamiltonian.to_abivars"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ExcHamiltonian.to_abivars()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.ExcHamiltonian.use_cg"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ExcHamiltonian.use_cg</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.ExcHamiltonian.use_direct_diago"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ExcHamiltonian.use_direct_diago</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.ExcHamiltonian.use_haydock"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ExcHamiltonian.use_haydock</code></span></a>
    - <a href="#pymatgen.io.abinit.abiobjects.HilbertTransform"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">HilbertTransform</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.HilbertTransform.to_abivars"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">HilbertTransform.to_abivars()</code></span></a>
    - <a href="#pymatgen.io.abinit.abiobjects.KSampling"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">KSampling</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.KSampling.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">KSampling.as_dict()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.KSampling.automatic_density"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">KSampling.automatic_density()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.KSampling.explicit_path"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">KSampling.explicit_path()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.KSampling.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">KSampling.from_dict()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.KSampling.gamma_centered"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">KSampling.gamma_centered()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.KSampling.gamma_only"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">KSampling.gamma_only()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.KSampling.is_homogeneous"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">KSampling.is_homogeneous</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.KSampling.monkhorst"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">KSampling.monkhorst()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.KSampling.monkhorst_automatic"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">KSampling.monkhorst_automatic()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.KSampling.path_from_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">KSampling.path_from_structure()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.KSampling.to_abivars"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">KSampling.to_abivars()</code></span></a>
    - <a href="#pymatgen.io.abinit.abiobjects.KSamplingModes"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">KSamplingModes</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.KSamplingModes.automatic"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">KSamplingModes.automatic</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.KSamplingModes.monkhorst"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">KSamplingModes.monkhorst</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.KSamplingModes.path"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">KSamplingModes.path</code></span></a>
    - <a href="#pymatgen.io.abinit.abiobjects.ModelDielectricFunction"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">ModelDielectricFunction</code></span></a>
      - <a
        href="#pymatgen.io.abinit.abiobjects.ModelDielectricFunction.to_abivars"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ModelDielectricFunction.to_abivars()</code></span></a>
    - <a href="#pymatgen.io.abinit.abiobjects.PPModel"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">PPModel</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.PPModel.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PPModel.as_dict()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.PPModel.as_ppmodel"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PPModel.as_ppmodel()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.PPModel.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PPModel.from_dict()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.PPModel.get_noppmodel"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PPModel.get_noppmodel()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.PPModel.to_abivars"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PPModel.to_abivars()</code></span></a>
    - <a href="#pymatgen.io.abinit.abiobjects.PPModelModes"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">PPModelModes</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.PPModelModes.farid"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PPModelModes.farid</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.PPModelModes.godby"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PPModelModes.godby</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.PPModelModes.hybersten"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PPModelModes.hybersten</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.PPModelModes.linden"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PPModelModes.linden</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.PPModelModes.noppmodel"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PPModelModes.noppmodel</code></span></a>
    - <a href="#pymatgen.io.abinit.abiobjects.RelaxationMethod"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">RelaxationMethod</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.RelaxationMethod.IONMOV_DEFAULT"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RelaxationMethod.IONMOV_DEFAULT</code></span></a>
      - <a
        href="#pymatgen.io.abinit.abiobjects.RelaxationMethod.OPTCELL_DEFAULT"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RelaxationMethod.OPTCELL_DEFAULT</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.RelaxationMethod.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RelaxationMethod.as_dict()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.RelaxationMethod.atoms_and_cell"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RelaxationMethod.atoms_and_cell()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.RelaxationMethod.atoms_only"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RelaxationMethod.atoms_only()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.RelaxationMethod.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RelaxationMethod.from_dict()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.RelaxationMethod.move_atoms"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RelaxationMethod.move_atoms</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.RelaxationMethod.move_cell"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RelaxationMethod.move_cell</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.RelaxationMethod.to_abivars"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RelaxationMethod.to_abivars()</code></span></a>
    - <a href="#pymatgen.io.abinit.abiobjects.Screening"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Screening</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.Screening.to_abivars"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Screening.to_abivars()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.Screening.use_hilbert"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Screening.use_hilbert</code></span></a>
    - <a href="#pymatgen.io.abinit.abiobjects.SelfEnergy"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">SelfEnergy</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.SelfEnergy.gwcalctyp"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SelfEnergy.gwcalctyp</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.SelfEnergy.symsigma"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SelfEnergy.symsigma</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.SelfEnergy.to_abivars"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SelfEnergy.to_abivars()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.SelfEnergy.use_ppmodel"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SelfEnergy.use_ppmodel</code></span></a>
    - <a href="#pymatgen.io.abinit.abiobjects.Smearing"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Smearing</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.Smearing.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Smearing.as_dict()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.Smearing.as_smearing"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Smearing.as_smearing()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.Smearing.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Smearing.from_dict()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.Smearing.mode"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Smearing.mode</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.Smearing.nosmearing"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Smearing.nosmearing()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.Smearing.to_abivars"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Smearing.to_abivars()</code></span></a>
    - <a href="#pymatgen.io.abinit.abiobjects.SpinMode"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">SpinMode</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.SpinMode.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SpinMode.as_dict()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.SpinMode.as_spinmode"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SpinMode.as_spinmode()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.SpinMode.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SpinMode.from_dict()</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.SpinMode.to_abivars"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SpinMode.to_abivars()</code></span></a>
    - <a href="#pymatgen.io.abinit.abiobjects.SpinModeTuple"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">SpinModeTuple</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.SpinModeTuple.mode"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SpinModeTuple.mode</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.SpinModeTuple.nspden"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SpinModeTuple.nspden</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.SpinModeTuple.nspinor"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SpinModeTuple.nspinor</code></span></a>
      - <a href="#pymatgen.io.abinit.abiobjects.SpinModeTuple.nsppol"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SpinModeTuple.nsppol</code></span></a>
    - <a href="#pymatgen.io.abinit.abiobjects.contract"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">contract()</code></span></a>
    - <a href="#pymatgen.io.abinit.abiobjects.lattice_from_abivars"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">lattice_from_abivars()</code></span></a>
    - <a href="#pymatgen.io.abinit.abiobjects.species_by_znucl"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">species_by_znucl()</code></span></a>
    - <a href="#pymatgen.io.abinit.abiobjects.structure_from_abivars"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">structure_from_abivars()</code></span></a>
    - <a href="#pymatgen.io.abinit.abiobjects.structure_to_abivars"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">structure_to_abivars()</code></span></a>
  - <a href="#module-pymatgen.io.abinit.abitimer"
    class="reference internal">pymatgen.io.abinit.abitimer module</a>
    - <a href="#pymatgen.io.abinit.abitimer.AbinitTimer"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">AbinitTimer</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimer.cpuwall_histogram"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimer.cpuwall_histogram()</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimer.get_dataframe"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimer.get_dataframe()</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimer.get_section"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimer.get_section()</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimer.get_values"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimer.get_values()</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimer.names_and_values"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimer.names_and_values()</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimer.ncpus"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimer.ncpus</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimer.order_sections"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimer.order_sections()</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimer.pie"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimer.pie()</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimer.scatter_hist"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimer.scatter_hist()</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimer.sum_sections"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimer.sum_sections()</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimer.to_csv"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimer.to_csv()</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimer.to_table"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimer.to_table()</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimer.totable"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimer.totable()</code></span></a>
    - <a href="#pymatgen.io.abinit.abitimer.AbinitTimerParseError"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">AbinitTimerParseError</code></span></a>
    - <a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">AbinitTimerParser</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.BEGIN_TAG"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimerParser.BEGIN_TAG</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.END_TAG"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimerParser.END_TAG</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.Error"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimerParser.Error</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.filenames"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimerParser.filenames</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.get_sections"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimerParser.get_sections()</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.parse"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimerParser.parse()</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.pefficiency"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimerParser.pefficiency()</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.plot_all"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimerParser.plot_all()</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.plot_efficiency"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimerParser.plot_efficiency()</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.plot_pie"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimerParser.plot_pie()</code></span></a>
      - <a
        href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.plot_stacked_hist"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimerParser.plot_stacked_hist()</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.section_names"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimerParser.section_names()</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.summarize"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimerParser.summarize()</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.timers"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimerParser.timers()</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.walk"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimerParser.walk()</code></span></a>
    - <a href="#pymatgen.io.abinit.abitimer.AbinitTimerSection"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">AbinitTimerSection</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimerSection.FIELDS"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimerSection.FIELDS</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimerSection.NUMERIC_FIELDS"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimerSection.NUMERIC_FIELDS</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimerSection.STR_FIELDS"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimerSection.STR_FIELDS</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimerSection.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimerSection.as_dict()</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimerSection.fake"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimerSection.fake()</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimerSection.to_csvline"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimerSection.to_csvline()</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimerSection.to_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimerSection.to_dict()</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.AbinitTimerSection.to_tuple"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitTimerSection.to_tuple()</code></span></a>
    - <a href="#pymatgen.io.abinit.abitimer.ParallelEfficiency"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">ParallelEfficiency</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.ParallelEfficiency.bad_sections"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ParallelEfficiency.bad_sections()</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.ParallelEfficiency.good_sections"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ParallelEfficiency.good_sections()</code></span></a>
      - <a href="#pymatgen.io.abinit.abitimer.ParallelEfficiency.totable"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ParallelEfficiency.totable()</code></span></a>
    - <a href="#pymatgen.io.abinit.abitimer.alternate"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">alternate()</code></span></a>
  - <a href="#module-pymatgen.io.abinit.inputs"
    class="reference internal">pymatgen.io.abinit.inputs module</a>
    - <a href="#pymatgen.io.abinit.inputs.AbstractInput"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">AbstractInput</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.AbstractInput.deepcopy"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractInput.deepcopy()</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.AbstractInput.pop_vars"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractInput.pop_vars()</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.AbstractInput.remove_vars"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractInput.remove_vars()</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.AbstractInput.set_vars"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractInput.set_vars()</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.AbstractInput.set_vars_ifnotin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractInput.set_vars_ifnotin()</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.AbstractInput.to_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractInput.to_str()</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.AbstractInput.vars"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractInput.vars</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.AbstractInput.write"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractInput.write()</code></span></a>
    - <a href="#pymatgen.io.abinit.inputs.BasicAbinitInput"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">BasicAbinitInput</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.Error"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicAbinitInput.Error</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.add_abiobjects"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicAbinitInput.add_abiobjects()</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicAbinitInput.as_dict()</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.comment"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicAbinitInput.comment</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicAbinitInput.from_dict()</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.isnc"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicAbinitInput.isnc</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.ispaw"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicAbinitInput.ispaw</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.new_with_vars"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicAbinitInput.new_with_vars()</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.pop_irdvars"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicAbinitInput.pop_irdvars()</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.pop_tolerances"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicAbinitInput.pop_tolerances()</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.pseudos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicAbinitInput.pseudos</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.set_comment"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicAbinitInput.set_comment()</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.set_gamma_sampling"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicAbinitInput.set_gamma_sampling()</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.set_kmesh"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicAbinitInput.set_kmesh()</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.set_kpath"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicAbinitInput.set_kpath()</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.set_spin_mode"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicAbinitInput.set_spin_mode()</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.set_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicAbinitInput.set_structure()</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicAbinitInput.structure</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.to_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicAbinitInput.to_str()</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.vars"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicAbinitInput.vars</code></span></a>
    - <a href="#pymatgen.io.abinit.inputs.BasicAbinitInputError"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">BasicAbinitInputError</code></span></a>
    - <a href="#pymatgen.io.abinit.inputs.BasicMultiDataset"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">BasicMultiDataset</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicMultiDataset.Error"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicMultiDataset.Error</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicMultiDataset.addnew_from"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicMultiDataset.addnew_from()</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicMultiDataset.append"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicMultiDataset.append()</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicMultiDataset.deepcopy"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicMultiDataset.deepcopy()</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicMultiDataset.extend"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicMultiDataset.extend()</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicMultiDataset.from_inputs"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicMultiDataset.from_inputs()</code></span></a>
      - <a
        href="#pymatgen.io.abinit.inputs.BasicMultiDataset.has_same_structures"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicMultiDataset.has_same_structures</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicMultiDataset.isnc"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicMultiDataset.isnc</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicMultiDataset.ispaw"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicMultiDataset.ispaw</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicMultiDataset.ndtset"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicMultiDataset.ndtset</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicMultiDataset.pseudos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicMultiDataset.pseudos</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicMultiDataset.replicate_input"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicMultiDataset.replicate_input()</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicMultiDataset.split_datasets"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicMultiDataset.split_datasets()</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicMultiDataset.to_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicMultiDataset.to_str()</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.BasicMultiDataset.write"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasicMultiDataset.write()</code></span></a>
    - <a href="#pymatgen.io.abinit.inputs.ShiftMode"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">ShiftMode</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.ShiftMode.GammaCentered"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ShiftMode.GammaCentered</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.ShiftMode.MonkhorstPack"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ShiftMode.MonkhorstPack</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.ShiftMode.OneSymmetric"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ShiftMode.OneSymmetric</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.ShiftMode.Symmetric"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ShiftMode.Symmetric</code></span></a>
      - <a href="#pymatgen.io.abinit.inputs.ShiftMode.from_object"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">ShiftMode.from_object()</code></span></a>
    - <a href="#pymatgen.io.abinit.inputs.as_structure"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">as_structure()</code></span></a>
    - <a href="#pymatgen.io.abinit.inputs.calc_shiftk"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">calc_shiftk()</code></span></a>
    - <a href="#pymatgen.io.abinit.inputs.ebands_input"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">ebands_input()</code></span></a>
    - <a href="#pymatgen.io.abinit.inputs.gs_input"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">gs_input()</code></span></a>
    - <a href="#pymatgen.io.abinit.inputs.ion_ioncell_relax_input"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">ion_ioncell_relax_input()</code></span></a>
    - <a href="#pymatgen.io.abinit.inputs.num_valence_electrons"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">num_valence_electrons()</code></span></a>
  - <a href="#module-pymatgen.io.abinit.netcdf"
    class="reference internal">pymatgen.io.abinit.netcdf module</a>
    - <a href="#pymatgen.io.abinit.netcdf.AbinitHeader"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">AbinitHeader</code></span></a>
      - <a href="#pymatgen.io.abinit.netcdf.AbinitHeader.to_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitHeader.to_str()</code></span></a>
      - <a href="#pymatgen.io.abinit.netcdf.AbinitHeader.to_string"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitHeader.to_string()</code></span></a>
    - <a href="#pymatgen.io.abinit.netcdf.EtsfReader"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">EtsfReader</code></span></a>
      - <a href="#pymatgen.io.abinit.netcdf.EtsfReader.chemical_symbols"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">EtsfReader.chemical_symbols()</code></span></a>
      - <a href="#pymatgen.io.abinit.netcdf.EtsfReader.read_abinit_hdr"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">EtsfReader.read_abinit_hdr()</code></span></a>
      - <a href="#pymatgen.io.abinit.netcdf.EtsfReader.read_abinit_xcfunc"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">EtsfReader.read_abinit_xcfunc()</code></span></a>
      - <a href="#pymatgen.io.abinit.netcdf.EtsfReader.read_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">EtsfReader.read_structure()</code></span></a>
      - <a href="#pymatgen.io.abinit.netcdf.EtsfReader.type_idx_from_symbol"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">EtsfReader.type_idx_from_symbol()</code></span></a>
    - <a href="#pymatgen.io.abinit.netcdf.NO_DEFAULT"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">NO_DEFAULT</code></span></a>
    - <a href="#pymatgen.io.abinit.netcdf.NetcdfReader"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">NetcdfReader</code></span></a>
      - <a href="#pymatgen.io.abinit.netcdf.NetcdfReader.Error"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NetcdfReader.Error</code></span></a>
      - <a href="#pymatgen.io.abinit.netcdf.NetcdfReader.close"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NetcdfReader.close()</code></span></a>
      - <a href="#pymatgen.io.abinit.netcdf.NetcdfReader.print_tree"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NetcdfReader.print_tree()</code></span></a>
      - <a href="#pymatgen.io.abinit.netcdf.NetcdfReader.read_dimvalue"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NetcdfReader.read_dimvalue()</code></span></a>
      - <a href="#pymatgen.io.abinit.netcdf.NetcdfReader.read_keys"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NetcdfReader.read_keys()</code></span></a>
      - <a href="#pymatgen.io.abinit.netcdf.NetcdfReader.read_value"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NetcdfReader.read_value()</code></span></a>
      - <a href="#pymatgen.io.abinit.netcdf.NetcdfReader.read_variable"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NetcdfReader.read_variable()</code></span></a>
      - <a href="#pymatgen.io.abinit.netcdf.NetcdfReader.read_varnames"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NetcdfReader.read_varnames()</code></span></a>
      - <a href="#pymatgen.io.abinit.netcdf.NetcdfReader.walk_tree"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NetcdfReader.walk_tree()</code></span></a>
    - <a href="#pymatgen.io.abinit.netcdf.NetcdfReaderError"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">NetcdfReaderError</code></span></a>
    - <a href="#pymatgen.io.abinit.netcdf.as_etsfreader"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">as_etsfreader()</code></span></a>
    - <a href="#pymatgen.io.abinit.netcdf.as_ncreader"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">as_ncreader()</code></span></a>
    - <a href="#pymatgen.io.abinit.netcdf.structure_from_ncdata"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">structure_from_ncdata()</code></span></a>
  - <a href="#module-pymatgen.io.abinit.pseudos"
    class="reference internal">pymatgen.io.abinit.pseudos module</a>
    - <a href="#pymatgen.io.abinit.pseudos.AbinitHeader"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">AbinitHeader</code></span></a>
    - <a href="#pymatgen.io.abinit.pseudos.AbinitPseudo"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">AbinitPseudo</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.AbinitPseudo.Z"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitPseudo.Z</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.AbinitPseudo.Z_val"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitPseudo.Z_val</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.AbinitPseudo.l_local"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitPseudo.l_local</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.AbinitPseudo.l_max"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitPseudo.l_max</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.AbinitPseudo.summary"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitPseudo.summary</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.AbinitPseudo.supports_soc"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbinitPseudo.supports_soc</code></span></a>
    - <a href="#pymatgen.io.abinit.pseudos.Hint"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Hint</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.Hint.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Hint.as_dict()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.Hint.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Hint.from_dict()</code></span></a>
    - <a href="#pymatgen.io.abinit.pseudos.NcAbinitHeader"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">NcAbinitHeader</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.NcAbinitHeader.fhi_header"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NcAbinitHeader.fhi_header()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.NcAbinitHeader.gth_header"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NcAbinitHeader.gth_header()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.NcAbinitHeader.hgh_header"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NcAbinitHeader.hgh_header()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.NcAbinitHeader.oncvpsp_header"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NcAbinitHeader.oncvpsp_header()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.NcAbinitHeader.tm_header"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NcAbinitHeader.tm_header()</code></span></a>
    - <a href="#pymatgen.io.abinit.pseudos.NcAbinitPseudo"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">NcAbinitPseudo</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.NcAbinitPseudo.Z"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NcAbinitPseudo.Z</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.NcAbinitPseudo.Z_val"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NcAbinitPseudo.Z_val</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.NcAbinitPseudo.l_local"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NcAbinitPseudo.l_local</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.NcAbinitPseudo.l_max"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NcAbinitPseudo.l_max</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.NcAbinitPseudo.nlcc_radius"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NcAbinitPseudo.nlcc_radius</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.NcAbinitPseudo.summary"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NcAbinitPseudo.summary</code></span></a>
    - <a href="#pymatgen.io.abinit.pseudos.NcPseudo"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">NcPseudo</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.NcPseudo.has_nlcc"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NcPseudo.has_nlcc</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.NcPseudo.nlcc_radius"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NcPseudo.nlcc_radius</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.NcPseudo.rcore"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">NcPseudo.rcore</code></span></a>
    - <a href="#pymatgen.io.abinit.pseudos.PawAbinitHeader"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">PawAbinitHeader</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PawAbinitHeader.paw_header"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PawAbinitHeader.paw_header()</code></span></a>
    - <a href="#pymatgen.io.abinit.pseudos.PawAbinitPseudo"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">PawAbinitPseudo</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PawAbinitPseudo.paw_radius"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PawAbinitPseudo.paw_radius</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PawAbinitPseudo.supports_soc"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PawAbinitPseudo.supports_soc</code></span></a>
    - <a href="#pymatgen.io.abinit.pseudos.PawPseudo"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">PawPseudo</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PawPseudo.paw_radius"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PawPseudo.paw_radius</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PawPseudo.rcore"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PawPseudo.rcore</code></span></a>
    - <a href="#pymatgen.io.abinit.pseudos.PawXmlSetup"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">PawXmlSetup</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.Z"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PawXmlSetup.Z</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.Z_val"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PawXmlSetup.Z_val</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.ae_core_density"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PawXmlSetup.ae_core_density()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.ae_partial_waves"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PawXmlSetup.ae_partial_waves()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.l_local"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PawXmlSetup.l_local</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.l_max"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PawXmlSetup.l_max</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.paw_radius"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PawXmlSetup.paw_radius</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.plot_densities"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PawXmlSetup.plot_densities()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.plot_projectors"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PawXmlSetup.plot_projectors()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.plot_waves"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PawXmlSetup.plot_waves()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.projector_functions"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PawXmlSetup.projector_functions()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.pseudo_core_density"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PawXmlSetup.pseudo_core_density()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.pseudo_partial_waves"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PawXmlSetup.pseudo_partial_waves</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.root"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PawXmlSetup.root()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.summary"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PawXmlSetup.summary</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.supports_soc"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PawXmlSetup.supports_soc</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.yield_figs"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PawXmlSetup.yield_figs()</code></span></a>
    - <a href="#pymatgen.io.abinit.pseudos.Pseudo"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Pseudo</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.Pseudo.Z"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Pseudo.Z</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.Pseudo.Z_val"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Pseudo.Z_val</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.Pseudo.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Pseudo.as_dict()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.Pseudo.as_pseudo"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Pseudo.as_pseudo()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.Pseudo.as_tmpfile"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Pseudo.as_tmpfile()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.Pseudo.basename"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Pseudo.basename</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.Pseudo.compute_md5"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Pseudo.compute_md5()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.Pseudo.djrepo_path"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Pseudo.djrepo_path</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.Pseudo.element"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Pseudo.element</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.Pseudo.filepath"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Pseudo.filepath</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.Pseudo.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Pseudo.from_dict()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.Pseudo.from_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Pseudo.from_file()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.Pseudo.has_dojo_report"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Pseudo.has_dojo_report</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.Pseudo.has_hints"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Pseudo.has_hints</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.Pseudo.hint_for_accuracy"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Pseudo.hint_for_accuracy()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.Pseudo.isnc"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Pseudo.isnc</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.Pseudo.ispaw"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Pseudo.ispaw</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.Pseudo.l_local"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Pseudo.l_local</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.Pseudo.l_max"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Pseudo.l_max</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.Pseudo.md5"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Pseudo.md5()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.Pseudo.open_pspsfile"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Pseudo.open_pspsfile()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.Pseudo.summary"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Pseudo.summary</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.Pseudo.supports_soc"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Pseudo.supports_soc</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.Pseudo.symbol"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Pseudo.symbol</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.Pseudo.to_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Pseudo.to_str()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.Pseudo.type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Pseudo.type</code></span></a>
    - <a href="#pymatgen.io.abinit.pseudos.PseudoParseError"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">PseudoParseError</code></span></a>
    - <a href="#pymatgen.io.abinit.pseudos.PseudoParser"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">PseudoParser</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PseudoParser.Error"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PseudoParser.Error</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PseudoParser.parse"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PseudoParser.parse()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PseudoParser.ppdesc"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PseudoParser.ppdesc</code></span></a>
        - <a href="#pymatgen.io.abinit.pseudos.PseudoParser.ppdesc.format"
          class="reference internal"><span class="pre"><code
          class="docutils literal notranslate">PseudoParser.ppdesc.format</code></span></a>
        - <a href="#pymatgen.io.abinit.pseudos.PseudoParser.ppdesc.name"
          class="reference internal"><span class="pre"><code
          class="docutils literal notranslate">PseudoParser.ppdesc.name</code></span></a>
        - <a href="#pymatgen.io.abinit.pseudos.PseudoParser.ppdesc.psp_type"
          class="reference internal"><span class="pre"><code
          class="docutils literal notranslate">PseudoParser.ppdesc.psp_type</code></span></a>
        - <a href="#pymatgen.io.abinit.pseudos.PseudoParser.ppdesc.pspcod"
          class="reference internal"><span class="pre"><code
          class="docutils literal notranslate">PseudoParser.ppdesc.pspcod</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PseudoParser.read_ppdesc"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PseudoParser.read_ppdesc()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PseudoParser.scan_directory"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PseudoParser.scan_directory()</code></span></a>
    - <a href="#pymatgen.io.abinit.pseudos.PseudoTable"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">PseudoTable</code></span></a>
      - <a
        href="#pymatgen.io.abinit.pseudos.PseudoTable.all_combinations_for_elements"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PseudoTable.all_combinations_for_elements()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PseudoTable.allnc"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PseudoTable.allnc</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PseudoTable.allpaw"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PseudoTable.allpaw</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PseudoTable.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PseudoTable.as_dict()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PseudoTable.as_table"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PseudoTable.as_table()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PseudoTable.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PseudoTable.from_dict()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PseudoTable.from_dir"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PseudoTable.from_dir()</code></span></a>
      - <a
        href="#pymatgen.io.abinit.pseudos.PseudoTable.get_pseudos_for_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PseudoTable.get_pseudos_for_structure()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PseudoTable.is_complete"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PseudoTable.is_complete()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PseudoTable.print_table"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PseudoTable.print_table()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PseudoTable.pseudo_with_symbol"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PseudoTable.pseudo_with_symbol()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PseudoTable.pseudos_with_symbols"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PseudoTable.pseudos_with_symbols()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PseudoTable.select"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PseudoTable.select()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PseudoTable.select_family"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PseudoTable.select_family()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PseudoTable.select_rows"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PseudoTable.select_rows()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PseudoTable.select_symbols"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PseudoTable.select_symbols()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PseudoTable.sort_by_z"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PseudoTable.sort_by_z()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PseudoTable.sorted"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PseudoTable.sorted()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PseudoTable.to_table"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PseudoTable.to_table()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PseudoTable.with_dojo_report"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PseudoTable.with_dojo_report()</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.PseudoTable.zlist"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PseudoTable.zlist</code></span></a>
    - <a href="#pymatgen.io.abinit.pseudos.RadialFunction"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">RadialFunction</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.RadialFunction.mesh"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RadialFunction.mesh</code></span></a>
      - <a href="#pymatgen.io.abinit.pseudos.RadialFunction.values"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">RadialFunction.values</code></span></a>
    - <a href="#pymatgen.io.abinit.pseudos.l2str"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">l2str()</code></span></a>
    - <a href="#pymatgen.io.abinit.pseudos.str2l"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">str2l()</code></span></a>
  - <a href="#module-pymatgen.io.abinit.variable"
    class="reference internal">pymatgen.io.abinit.variable module</a>
    - <a href="#pymatgen.io.abinit.variable.InputVariable"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">InputVariable</code></span></a>
      - <a href="#pymatgen.io.abinit.variable.InputVariable.basename"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">InputVariable.basename</code></span></a>
      - <a href="#pymatgen.io.abinit.variable.InputVariable.dataset"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">InputVariable.dataset</code></span></a>
      - <a href="#pymatgen.io.abinit.variable.InputVariable.format_list"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">InputVariable.format_list()</code></span></a>
      - <a href="#pymatgen.io.abinit.variable.InputVariable.format_list2d"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">InputVariable.format_list2d()</code></span></a>
      - <a href="#pymatgen.io.abinit.variable.InputVariable.format_scalar"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">InputVariable.format_scalar()</code></span></a>
      - <a href="#pymatgen.io.abinit.variable.InputVariable.get_value"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">InputVariable.get_value()</code></span></a>
      - <a href="#pymatgen.io.abinit.variable.InputVariable.name"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">InputVariable.name</code></span></a>
      - <a href="#pymatgen.io.abinit.variable.InputVariable.units"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">InputVariable.units</code></span></a>
    - <a href="#pymatgen.io.abinit.variable.flatten"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">flatten()</code></span></a>

</div>

</div>

</div>

<div class="section wy-nav-content-wrap" toggle="wy-nav-shift">

[pymatgen](index.html)

<div class="wy-nav-content">

<div class="rst-content style-external-links">

<div role="navigation" aria-label="Page navigation">

- <a href="index.html" class="icon icon-home" aria-label="Home"></a>
- pymatgen.io.abinit package
- <a
  href="https://github.com/materialsproject/pymatgen/blob/master/docs_rst/pymatgen.io.abinit.rst"
  class="fa fa-github">Edit on GitHub</a>

------------------------------------------------------------------------

</div>

<div class="document" role="main" itemscope="itemscope"
itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="module-pymatgen.io.abinit" class="section">

<span id="pymatgen-io-abinit-package"></span>

# pymatgen.io.abinit package<a href="#module-pymatgen.io.abinit" class="headerlink"
title="Link to this heading"></a>

This package implements basic input and output capabilities for Abinit.

<div id="submodules" class="section">

## Submodules<a href="#submodules" class="headerlink"
title="Link to this heading"></a>

</div>

<div id="module-pymatgen.io.abinit.abiobjects" class="section">

<span id="pymatgen-io-abinit-abiobjects-module"></span>

## pymatgen.io.abinit.abiobjects module<a href="#module-pymatgen.io.abinit.abiobjects" class="headerlink"
title="Link to this heading"></a>

Low-level classes and functions to work with Abinit input files.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">AbivarAble</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L310-L325"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.AbivarAble" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`ABC`</span>

An AbivarAble object provides a method to_abivars that returns a
dictionary with the abinit variables.

*<span class="k"><span class="pre">abstractmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">to_abivars</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L313-L315"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.AbivarAble.to_abivars"
class="headerlink" title="Link to this definition"></a>  
Get a dictionary with the abinit variables.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Constraints</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L1020-L1025"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.Constraints" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.abinit.abiobjects.AbivarAble"
class="reference internal"
title="pymatgen.io.abinit.abiobjects.AbivarAble"><span class="pre"><code
class="sourceCode python">AbivarAble</code></span></a>

Define the constraints for structural relaxation.

<span class="sig-name descname"><span class="pre">to_abivars</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L1023-L1025"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.Constraints.to_abivars"
class="headerlink" title="Link to this definition"></a>  
Dictionary with Abinit variables.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Electrons</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">spin_mode</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'polarized'</span></span>*, *<span class="n"><span class="pre">smearing</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'fermi_dirac:0.1</span> <span class="pre">eV'</span></span>*, *<span class="n"><span class="pre">algorithm</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">nband</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">fband</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">charge</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.0</span></span>*, *<span class="n"><span class="pre">comment</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L574-L657"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.Electrons" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.abinit.abiobjects.AbivarAble"
class="reference internal"
title="pymatgen.io.abinit.abiobjects.AbivarAble"><span class="pre"><code
class="sourceCode python">AbivarAble</code></span></a>, <span
class="pre">`MSONable`</span>

The electronic degrees of freedom.

Constructor for Electrons object.

Parameters<span class="colon">:</span>  
- **comment** – String comment for Electrons

- **charge** – Total charge of the system. Default is 0.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L619-L631"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.Electrons.as_dict"
class="headerlink" title="Link to this definition"></a>  
JSON friendly dict representation.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L633-L642"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.Electrons.from_dict"
class="headerlink" title="Link to this definition"></a>  
Build from dict.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">nspden</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abiobjects.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.Electrons.nspden"
class="headerlink" title="Link to this definition"></a>  
Number of independent density components.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">nspinor</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abiobjects.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.Electrons.nspinor"
class="headerlink" title="Link to this definition"></a>  
Number of independent spinor components.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">nsppol</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abiobjects.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.Electrons.nsppol"
class="headerlink" title="Link to this definition"></a>  
Number of independent spin polarizations.

<span class="sig-name descname"><span class="pre">to_abivars</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L644-L657"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.Electrons.to_abivars"
class="headerlink" title="Link to this definition"></a>  
Return dictionary with Abinit variables.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ElectronsAlgorithm</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*</span></span><span class="n"><span class="pre">args</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L516-L571"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.ElectronsAlgorithm"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`dict`</span>,
<a href="#pymatgen.io.abinit.abiobjects.AbivarAble"
class="reference internal"
title="pymatgen.io.abinit.abiobjects.AbivarAble"><span class="pre"><code
class="sourceCode python">AbivarAble</code></span></a>, <span
class="pre">`MSONable`</span>

Variables controlling the SCF/NSCF algorithm.

Parameters<span class="colon">:</span>  
- **iprcell** – 1 if the cell is fixed, 2 if the cell is relaxed.

- **iscf** – SCF algorithm.

- **diemac** – Macroscopic dielectric constant.

- **diemix** – Mixing parameter for the electric field.

- **diemixmag** – Mixing parameter for the magnetic field.

- **dielam** – Damping factor for the electric field.

- **diegap** – Energy gap for the dielectric function.

- **dielng** – Length of the electric field.

- **diecut** – Cutoff for the dielectric function.

- **nstep** – Maximum number of SCF iterations.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L557-L563"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.ElectronsAlgorithm.as_dict"
class="headerlink" title="Link to this definition"></a>  
Get JSON-able dict representation.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L565-L571"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.ElectronsAlgorithm.from_dict"
class="headerlink" title="Link to this definition"></a>  
Build from dict.

<span class="sig-name descname"><span class="pre">to_abivars</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L553-L555"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.ElectronsAlgorithm.to_abivars"
class="headerlink" title="Link to this definition"></a>  
Dictionary with Abinit input variables.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ExcHamiltonian</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">bs_loband</span></span>*, *<span class="n"><span class="pre">nband</span></span>*, *<span class="n"><span class="pre">mbpt_sciss</span></span>*, *<span class="n"><span class="pre">coulomb_mode</span></span>*, *<span class="n"><span class="pre">ecuteps</span></span>*, *<span class="n"><span class="pre">spin_mode</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'polarized'</span></span>*, *<span class="n"><span class="pre">mdf_epsinf</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">exc_type</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'TDA'</span></span>*, *<span class="n"><span class="pre">algo</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'haydock'</span></span>*, *<span class="n"><span class="pre">with_lf</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">bs_freq_mesh</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">zcut</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L1559-L1708"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.ExcHamiltonian"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.abinit.abiobjects.AbivarAble"
class="reference internal"
title="pymatgen.io.abinit.abiobjects.AbivarAble"><span class="pre"><code
class="sourceCode python">AbivarAble</code></span></a>

Contain parameters for the solution of the Bethe-Salpeter equation.

Parameters<span class="colon">:</span>  
- **bs_loband** – Lowest band index (Fortran convention) used in the e-h
  basis set. Can be scalar or array of shape (nsppol,). Must be \>= 1
  and \<= nband

- **nband** – Max band index used in the e-h basis set.

- **mbpt_sciss** – Scissors energy in Hartree.

- **coulomb_mode** – Treatment of the Coulomb term.

- **ecuteps** – Cutoff energy for W in Hartree.

- **mdf_epsinf** – Macroscopic dielectric function <span
  class="math notranslate nohighlight">\\(\\\epsilon\_\\\inf\\)</span>
  used in the model dielectric function.

- **exc_type** – Approximation used for the BSE Hamiltonian

- **with_lf** – True if local field effects are included \<==\> exchange
  term is included

- **bs_freq_mesh** – Frequency mesh for the macroscopic dielectric
  function (start, stop, step) in Ha.

- **zcut** – Broadening parameter in Ha.

- **\*\*kwargs** – Extra keywords.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">inclvkb</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abiobjects.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.ExcHamiltonian.inclvkb"
class="headerlink" title="Link to this definition"></a>  
Treatment of the dipole matrix element (NC pseudos, default is 2).

<span class="sig-name descname"><span class="pre">to_abivars</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L1673-L1708"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.ExcHamiltonian.to_abivars"
class="headerlink" title="Link to this definition"></a>  
Get a dictionary with the abinit variables.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">use_cg</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abiobjects.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.ExcHamiltonian.use_cg"
class="headerlink" title="Link to this definition"></a>  
True if we are using the conjugate gradient method.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">use_direct_diago</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abiobjects.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.ExcHamiltonian.use_direct_diago"
class="headerlink" title="Link to this definition"></a>  
True if we are performing the direct diagonalization of the BSE
Hamiltonian.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">use_haydock</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abiobjects.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.ExcHamiltonian.use_haydock"
class="headerlink" title="Link to this definition"></a>  
True if we are using the Haydock iterative technique.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">HilbertTransform</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">nomegasf</span></span>*, *<span class="n"><span class="pre">domegasf</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">spmeth</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1</span></span>*, *<span class="n"><span class="pre">nfreqre</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">freqremax</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">nfreqim</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">freqremin</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L1256-L1306"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.HilbertTransform"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.abinit.abiobjects.AbivarAble"
class="reference internal"
title="pymatgen.io.abinit.abiobjects.AbivarAble"><span class="pre"><code
class="sourceCode python">AbivarAble</code></span></a>

Parameters for the Hilbert-transform method (Screening code) i.e. the
parameters defining the frequency mesh used for the spectral function
and the frequency mesh used for the polarizability.

Parameters<span class="colon">:</span>  
- **nomegasf** – Number of points for sampling the spectral function
  along the real axis.

- **domegasf** – Step in Ha for the linear mesh used for the spectral
  function.

- **spmeth** – Algorithm for the representation of the delta function.

- **nfreqre** – Number of points along the real axis (linear mesh).

- **freqremax** – Maximum frequency for W along the real axis (in
  hartree).

- **nfreqim** – Number of point along the imaginary axis (Gauss-Legendre
  mesh).

- **freqremin** – Minimum frequency for W along the real axis (in
  hartree).

<span class="sig-name descname"><span class="pre">to_abivars</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L1294-L1306"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.HilbertTransform.to_abivars"
class="headerlink" title="Link to this definition"></a>  
Get a dictionary with the abinit variables.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">KSampling</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">mode</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">KSamplingModes.monkhorst</span></span>*, *<span class="n"><span class="pre">num_kpts</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">kpts</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">((1,</span> <span class="pre">1,</span> <span class="pre">1),)</span></span>*, *<span class="n"><span class="pre">kpt_shifts</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0.5,</span> <span class="pre">0.5,</span> <span class="pre">0.5)</span></span>*, *<span class="n"><span class="pre">kpts_weights</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">use_symmetries</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">use_time_reversal</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">chksymbreak</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">comment</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L669-L1017"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.KSampling" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.abinit.abiobjects.AbivarAble"
class="reference internal"
title="pymatgen.io.abinit.abiobjects.AbivarAble"><span class="pre"><code
class="sourceCode python">AbivarAble</code></span></a>, <span
class="pre">`MSONable`</span>

Input variables defining the K-point sampling.

Highly flexible constructor for KSampling objects. The flexibility comes
at the cost of usability and in general, it is recommended that you use
the default constructor only if you know exactly what you are doing and
requires the flexibility. For most usage cases, the object be
constructed far more easily using the convenience static constructors:

> <div>
>
> 1.  gamma_only
>
> 2.  gamma_centered
>
> 3.  monkhorst
>
> 4.  monkhorst_automatic
>
> 5.  path
>
> </div>

and it is recommended that you use those.

Parameters<span class="colon">:</span>  
- **mode** – Mode for generating k-poits. Use one of the KSamplingModes
  enum types.

- **num_kpts** – Number of kpoints if mode is “automatic” Number of
  division for the sampling of the smallest segment if mode is “path”.
  Not used for the other modes

- **kpts** – Number of divisions. Even when only a single specification
  is required, e.g. in the automatic scheme, the kpts should still be
  specified as a 2D array. e.g. \[\[20\]\] or \[\[2,2,2\]\].

- **kpt_shifts** – Shifts for Kpoints.

- **use_symmetries** – False if spatial symmetries should not be used to
  reduce the number of independent k-points.

- **use_time_reversal** – False if time-reversal symmetry should not be
  used to reduce the number of independent k-points.

- **kpts_weights** – Optional weights for kpoints. For explicit kpoints.

- **chksymbreak** – Abinit input variable: check whether the BZ sampling
  preserves the symmetry of the crystal.

- **comment** – String comment for Kpoints

<div class="admonition note">

Note

The default behavior of the constructor is monkhorst.

</div>

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L993-L1008"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.KSampling.as_dict"
class="headerlink" title="Link to this definition"></a>  
Get JSON-able dict representation.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">automatic_density</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span>*, *<span class="n"><span class="pre">kppa</span></span>*, *<span class="n"><span class="pre">chksymbreak</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">use_symmetries</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">use_time_reversal</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">shifts</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0.5,</span> <span class="pre">0.5,</span> <span class="pre">0.5)</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L944-L987"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.KSampling.automatic_density"
class="headerlink" title="Link to this definition"></a>  
Get an automatic Kpoint object based on a structure and a kpoint
density. Uses Gamma centered meshes for hexagonal cells and
Monkhorst-Pack grids otherwise.

Algorithm:  
Uses a simple approach scaling the number of divisions along each
reciprocal lattice vector proportional to its length.

Parameters<span class="colon">:</span>  
- **structure** – Input structure

- **kppa** – Grid density

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">explicit_path</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">ndivsm</span></span>*, *<span class="n"><span class="pre">kpath_bounds</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L939-L942"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.KSampling.explicit_path"
class="headerlink" title="Link to this definition"></a>  
See \_path for the meaning of the variables.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L1010-L1017"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.KSampling.from_dict"
class="headerlink" title="Link to this definition"></a>  
Build from dict.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">gamma_centered</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">kpts</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(1,</span> <span class="pre">1,</span> <span class="pre">1)</span></span>*, *<span class="n"><span class="pre">use_symmetries</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">use_time_reversal</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L802-L823"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.KSampling.gamma_centered"
class="headerlink" title="Link to this definition"></a>  
Convenient static constructor for an automatic Gamma centered Kpoint
grid.

Parameters<span class="colon">:</span>  
- **kpts** – Subdivisions N_1, N_2 and N_3 along reciprocal lattice
  vectors.

- **use_symmetries** – False if spatial symmetries should not be used to
  reduce the number of independent k-points.

- **use_time_reversal** – False if time-reversal symmetry should not be
  used to reduce the number of independent k-points.

Returns<span class="colon">:</span>  
KSampling object.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">gamma_only</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L797-L800"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.KSampling.gamma_only"
class="headerlink" title="Link to this definition"></a>  
Gamma-only sampling.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">is_homogeneous</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abiobjects.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.KSampling.is_homogeneous"
class="headerlink" title="Link to this definition"></a>  
Homogeneous sampling.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">monkhorst</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">ngkpt</span></span>*, *<span class="n"><span class="pre">shiftk</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0.5,</span> <span class="pre">0.5,</span> <span class="pre">0.5)</span></span>*, *<span class="n"><span class="pre">chksymbreak</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">use_symmetries</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">use_time_reversal</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">comment</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L825-L854"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.KSampling.monkhorst"
class="headerlink" title="Link to this definition"></a>  
Convenient static constructor for a Monkhorst-Pack mesh.

Parameters<span class="colon">:</span>  
- **ngkpt** – Subdivisions N_1, N_2 and N_3 along reciprocal lattice
  vectors.

- **shiftk** – Shift to be applied to the kpoints.

- **use_symmetries** – Use spatial symmetries to reduce the number of
  k-points.

- **use_time_reversal** – Use time-reversal symmetry to reduce the
  number of k-points.

Returns<span class="colon">:</span>  
KSampling object.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">monkhorst_automatic</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span>*, *<span class="n"><span class="pre">ngkpt</span></span>*, *<span class="n"><span class="pre">use_symmetries</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">use_time_reversal</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">chksymbreak</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">comment</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L856-L892"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.KSampling.monkhorst_automatic"
class="headerlink" title="Link to this definition"></a>  
Convenient static constructor for an automatic Monkhorst-Pack mesh.

Parameters<span class="colon">:</span>  
- **structure** – Structure object.

- **ngkpt** – Subdivisions N_1, N_2 and N_3 along reciprocal lattice
  vectors.

- **use_symmetries** – Use spatial symmetries to reduce the number of
  k-points.

- **use_time_reversal** – Use time-reversal symmetry to reduce the
  number of k-points.

Returns<span class="colon">:</span>  
KSampling object.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">path_from_structure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">ndivsm</span></span>*, *<span class="n"><span class="pre">structure</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L930-L937"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.KSampling.path_from_structure"
class="headerlink" title="Link to this definition"></a>  
See \_path for the meaning of the variables.

<span class="sig-name descname"><span class="pre">to_abivars</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L989-L991"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.KSampling.to_abivars"
class="headerlink" title="Link to this definition"></a>  
Dictionary with Abinit variables.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">KSamplingModes</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">value</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L660-L666"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.KSamplingModes"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`Enum`</span>

Enum if the different samplings of the BZ.

<span class="sig-name descname"><span class="pre">automatic</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">3</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abiobjects.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.KSamplingModes.automatic"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">monkhorst</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">1</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abiobjects.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.KSamplingModes.monkhorst"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">path</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">2</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abiobjects.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.KSamplingModes.path"
class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ModelDielectricFunction</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">mdf_epsinf</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L1309-L1321"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.ModelDielectricFunction"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.abinit.abiobjects.AbivarAble"
class="reference internal"
title="pymatgen.io.abinit.abiobjects.AbivarAble"><span class="pre"><code
class="sourceCode python">AbivarAble</code></span></a>

Model dielectric function used for BSE calculation.

Parameters<span class="colon">:</span>  
**mdf_epsinf** – Value of epsilon_infinity.

<span class="sig-name descname"><span class="pre">to_abivars</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L1319-L1321"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.abinit.abiobjects.ModelDielectricFunction.to_abivars"
class="headerlink" title="Link to this definition"></a>  
Return dictionary with abinit variables.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">PPModel</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">mode</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'godby'</span></span>*, *<span class="n"><span class="pre">plasmon_freq</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L1167-L1253"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.PPModel" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.abinit.abiobjects.AbivarAble"
class="reference internal"
title="pymatgen.io.abinit.abiobjects.AbivarAble"><span class="pre"><code
class="sourceCode python">AbivarAble</code></span></a>, <span
class="pre">`MSONable`</span>

Parameters defining the plasmon-pole technique. The common way to
instantiate a PPModel object is via the class method
PPModel.as_ppmodel(string).

Parameters<span class="colon">:</span>  
- **mode** – ppmodel type

- **plasmon_freq** – Plasmon frequency in Ha.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L1241-L1248"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.PPModel.as_dict"
class="headerlink" title="Link to this definition"></a>  
Get JSON-able dict representation.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">as_ppmodel</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">obj</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L1173-L1197"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.PPModel.as_ppmodel"
class="headerlink" title="Link to this definition"></a>  
Constructs an instance of PPModel from obj.

Accepts obj in the form:  
- PPmodel instance

- string. e.g “godby:12.3 eV”, “linden”.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L1250-L1253"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.PPModel.from_dict"
class="headerlink" title="Link to this definition"></a>  
Build from dict.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">get_noppmodel</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L1236-L1239"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.PPModel.get_noppmodel"
class="headerlink" title="Link to this definition"></a>  
Calculation without plasmon-pole model.

<span class="sig-name descname"><span class="pre">to_abivars</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L1230-L1234"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.PPModel.to_abivars"
class="headerlink" title="Link to this definition"></a>  
Return dictionary with Abinit variables.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">PPModelModes</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">value</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L1156-L1164"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.PPModelModes" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`Enum`</span>

Different kind of plasmon-pole models.

<span class="sig-name descname"><span class="pre">farid</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">4</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abiobjects.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.PPModelModes.farid"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">godby</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">1</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abiobjects.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.PPModelModes.godby"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">hybersten</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">2</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abiobjects.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.PPModelModes.hybersten"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">linden</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">3</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abiobjects.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.PPModelModes.linden"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">noppmodel</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">0</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abiobjects.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.PPModelModes.noppmodel"
class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">RelaxationMethod</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*</span></span><span class="n"><span class="pre">args</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L1028-L1153"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.RelaxationMethod"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.abinit.abiobjects.AbivarAble"
class="reference internal"
title="pymatgen.io.abinit.abiobjects.AbivarAble"><span class="pre"><code
class="sourceCode python">AbivarAble</code></span></a>, <span
class="pre">`MSONable`</span>

This object stores the variables for the (constrained) structural
optimization ionmov and optcell specify the type of relaxation. The
other variables are optional and their use depend on ionmov and optcell.
A None value indicates that we use abinit default. Default values can be
modified by passing them to the constructor. The set of variables are
constructed in to_abivars depending on ionmov and optcell.

Parameters<span class="colon">:</span>  
- **ionmov** – The type of relaxation for the ions.

- **optcell** – The type of relaxation for the unit cell.

- **ntime** – Maximum number of iterations.

- **dilatmx** – Maximum allowed cell volume change.

- **ecutsm** – Energy convergence criterion.

- **strfact** – Stress convergence criterion.

- **tolmxf** – Force convergence criterion.

- **strtarget** – Target stress.

- **atoms_constraints** – Constraints for the atoms.

<span class="sig-name descname"><span class="pre">IONMOV_DEFAULT</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">3</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abiobjects.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.RelaxationMethod.IONMOV_DEFAULT"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">OPTCELL_DEFAULT</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">2</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abiobjects.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.abinit.abiobjects.RelaxationMethod.OPTCELL_DEFAULT"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L1139-L1144"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.RelaxationMethod.as_dict"
class="headerlink" title="Link to this definition"></a>  
Convert to dictionary.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">atoms_and_cell</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">atoms_constraints</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L1089-L1098"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.RelaxationMethod.atoms_and_cell"
class="headerlink" title="Link to this definition"></a>  
Relax atomic positions as well as unit cell.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">atoms_only</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">atoms_constraints</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L1082-L1087"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.RelaxationMethod.atoms_only"
class="headerlink" title="Link to this definition"></a>  
Relax atomic positions, keep unit cell fixed.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L1146-L1153"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.RelaxationMethod.from_dict"
class="headerlink" title="Link to this definition"></a>  
Build from dictionary.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">move_atoms</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abiobjects.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.RelaxationMethod.move_atoms"
class="headerlink" title="Link to this definition"></a>  
True if atoms must be moved.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">move_cell</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abiobjects.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.RelaxationMethod.move_cell"
class="headerlink" title="Link to this definition"></a>  
True if lattice parameters must be optimized.

<span class="sig-name descname"><span class="pre">to_abivars</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L1110-L1137"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.RelaxationMethod.to_abivars"
class="headerlink" title="Link to this definition"></a>  
Get a dictionary with the abinit variables.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Screening</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">ecuteps</span></span>*, *<span class="n"><span class="pre">nband</span></span>*, *<span class="n"><span class="pre">w_type</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'RPA'</span></span>*, *<span class="n"><span class="pre">sc_mode</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'one_shot'</span></span>*, *<span class="n"><span class="pre">hilbert</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ecutwfn</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">inclvkb</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">2</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L1329-L1421"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.Screening" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.abinit.abiobjects.AbivarAble"
class="reference internal"
title="pymatgen.io.abinit.abiobjects.AbivarAble"><span class="pre"><code
class="sourceCode python">AbivarAble</code></span></a>

This object defines the parameters used for the computation of the
screening function.

Parameters<span class="colon">:</span>  
- **ecuteps** – Cutoff energy for the screening (Ha units).

- **function** (*nband Number* *of* *bands for the Green's*)

- **w_type** – Screening type

- **sc_mode** – Self-consistency mode.

- **hilbert** – Instance of HilbertTransform defining the parameters for
  the Hilber transform method.

- **ecutwfn** – Cutoff energy for the wavefunctions (Default: ecutwfn ==
  ecut).

- **inclvkb** – Option for the treatment of the dipole matrix elements
  (NC pseudos).

<span class="sig-name descname"><span class="pre">to_abivars</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L1402-L1421"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.Screening.to_abivars"
class="headerlink" title="Link to this definition"></a>  
Get a dictionary with the abinit variables.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">use_hilbert</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abiobjects.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.Screening.use_hilbert"
class="headerlink" title="Link to this definition"></a>  
True if we are using the Hilbert transform method.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">SelfEnergy</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">se_type</span></span>*, *<span class="n"><span class="pre">sc_mode</span></span>*, *<span class="n"><span class="pre">nband</span></span>*, *<span class="n"><span class="pre">ecutsigx</span></span>*, *<span class="n"><span class="pre">screening</span></span>*, *<span class="n"><span class="pre">gw_qprange</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1</span></span>*, *<span class="n"><span class="pre">ppmodel</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ecuteps</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ecutwfn</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">gwpara</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">2</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L1424-L1556"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.SelfEnergy" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.abinit.abiobjects.AbivarAble"
class="reference internal"
title="pymatgen.io.abinit.abiobjects.AbivarAble"><span class="pre"><code
class="sourceCode python">AbivarAble</code></span></a>

Define the parameters used for the computation of the self-energy.

Parameters<span class="colon">:</span>  
- **se_type** – Type of self-energy (str)

- **sc_mode** – Self-consistency mode.

- **nband** – Number of bands for the Green’s function

- **ecutsigx** – Cutoff energy for the exchange part of the self-energy
  (Ha units).

- **screening** – Screening instance.

- **gw_qprange** – Option for the automatic selection of k-points and
  bands for GW corrections. See Abinit docs for more detail. The default
  value makes the code computie the QP energies for all the point in the
  IBZ and one band above and one band below the Fermi level.

- **ppmodel** – PPModel instance with the parameters used for the
  plasmon-pole technique.

- **ecuteps** – Cutoff energy for the screening (Ha units).

- **ecutwfn** – Cutoff energy for the wavefunctions (Default: ecutwfn ==
  ecut).

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">gwcalctyp</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abiobjects.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.SelfEnergy.gwcalctyp"
class="headerlink" title="Link to this definition"></a>  
The value of the gwcalctyp input variable.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">symsigma</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abiobjects.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.SelfEnergy.symsigma"
class="headerlink" title="Link to this definition"></a>  
1 if symmetries can be used to reduce the number of q-points.

<span class="sig-name descname"><span class="pre">to_abivars</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L1531-L1556"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.SelfEnergy.to_abivars"
class="headerlink" title="Link to this definition"></a>  
Get a dictionary with the abinit variables.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">use_ppmodel</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abiobjects.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.SelfEnergy.use_ppmodel"
class="headerlink" title="Link to this definition"></a>  
True if we are using the plasmon-pole approximation.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Smearing</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">occopt</span></span>*, *<span class="n"><span class="pre">tsmear</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L407-L513"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.Smearing" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.abinit.abiobjects.AbivarAble"
class="reference internal"
title="pymatgen.io.abinit.abiobjects.AbivarAble"><span class="pre"><code
class="sourceCode python">AbivarAble</code></span></a>, <span
class="pre">`MSONable`</span>

Variables defining the smearing technique. The preferred way to
instantiate a Smearing object is via the class method
Smearing.as_smearing(string).

Parameters<span class="colon">:</span>  
- **occopt** – Integer specifying the smearing technique.

- **tsmear** – Smearing parameter in Hartree units.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L501-L508"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.Smearing.as_dict"
class="headerlink" title="Link to this definition"></a>  
JSON-friendly dict representation of Smearing.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">as_smearing</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">obj</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L450-L480"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.Smearing.as_smearing"
class="headerlink" title="Link to this definition"></a>  
Constructs an instance of Smearing from obj. Accepts obj in the form:

> <div>
>
> - Smearing instance
>
> - “name:tsmear” e.g. “gaussian:0.004” (Hartree units)
>
> - “name:tsmear units” e.g. “gaussian:0.1 eV”
>
> - None –\> no smearing
>
> </div>

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L510-L513"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.Smearing.from_dict"
class="headerlink" title="Link to this definition"></a>  
Build from dict.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">mode</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abiobjects.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.Smearing.mode"
class="headerlink" title="Link to this definition"></a>  
String with smearing technique.

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">nosmearing</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L490-L493"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.Smearing.nosmearing"
class="headerlink" title="Link to this definition"></a>  
For calculations without smearing.

<span class="sig-name descname"><span class="pre">to_abivars</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L495-L499"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.Smearing.to_abivars"
class="headerlink" title="Link to this definition"></a>  
Return dictionary with Abinit variables.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">SpinMode</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">mode</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">nsppol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">nspinor</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">nspden</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L355-L395"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.SpinMode" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.abinit.abiobjects.SpinModeTuple"
class="reference internal"
title="pymatgen.io.abinit.abiobjects.SpinModeTuple"><span
class="pre"><code
class="sourceCode python">SpinModeTuple</code></span></a>,
<a href="#pymatgen.io.abinit.abiobjects.AbivarAble"
class="reference internal"
title="pymatgen.io.abinit.abiobjects.AbivarAble"><span class="pre"><code
class="sourceCode python">AbivarAble</code></span></a>, <span
class="pre">`MSONable`</span>

Different configurations of the electron density as implemented in
abinit: One can use as_spinmode to construct the object via
SpinMode.as_spinmode (string) where string can assume the values:

> <div>
>
> - polarized
>
> - unpolarized
>
> - afm (anti-ferromagnetic)
>
> - spinor (non-collinear magnetism)
>
> - spinor_nomag (non-collinear, no magnetism)
>
> </div>

Create new instance of SpinModeTuple(mode, nsppol, nspinor, nspden)

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L386-L390"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.SpinMode.as_dict"
class="headerlink" title="Link to this definition"></a>  
JSON-friendly dict representation of SpinMode.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">as_spinmode</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">obj</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L370-L380"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.SpinMode.as_spinmode"
class="headerlink" title="Link to this definition"></a>  
Convert obj into a SpinMode instance.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L392-L395"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.SpinMode.from_dict"
class="headerlink" title="Link to this definition"></a>  
Build from dict.

<span class="sig-name descname"><span class="pre">to_abivars</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L382-L384"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.SpinMode.to_abivars"
class="headerlink" title="Link to this definition"></a>  
Dictionary with Abinit input variables.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">SpinModeTuple</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">mode</span></span>*, *<span class="n"><span class="pre">nsppol</span></span>*, *<span class="n"><span class="pre">nspinor</span></span>*, *<span class="n"><span class="pre">nspden</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L348-L352"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.SpinModeTuple"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`NamedTuple`</span>

Create new instance of SpinModeTuple(mode, nsppol, nspinor, nspden)

<span class="sig-name descname"><span class="pre">mode</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abiobjects.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.SpinModeTuple.mode"
class="headerlink" title="Link to this definition"></a>  
Alias for field number 0

<span class="sig-name descname"><span class="pre">nspden</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abiobjects.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.SpinModeTuple.nspden"
class="headerlink" title="Link to this definition"></a>  
Alias for field number 3

<span class="sig-name descname"><span class="pre">nspinor</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abiobjects.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.SpinModeTuple.nspinor"
class="headerlink" title="Link to this definition"></a>  
Alias for field number 2

<span class="sig-name descname"><span class="pre">nsppol</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abiobjects.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.SpinModeTuple.nsppol"
class="headerlink" title="Link to this definition"></a>  
Alias for field number 1

<!-- -->

<span class="sig-name descname"><span class="pre">contract</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">string</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L287-L307"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.contract" class="headerlink"
title="Link to this definition"></a>  
Examples

assert contract(“1 1 1 2 2 3”) == “3\*1 2\*2 1\*3” assert contract(“1 1
3 2 3”) == “2\*1 1\*3 1\*2 1\*3”.

<!-- -->

<span class="sig-name descname"><span class="pre">lattice_from_abivars</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">cls</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*</span></span><span class="n"><span class="pre">args</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L27-L99"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.lattice_from_abivars"
class="headerlink" title="Link to this definition"></a>  
Get a Lattice object from a dictionary with the Abinit variables acell
and either rprim in Bohr or angdeg. If acell is not given, the Abinit
default of \[1, 1, 1\] Bohr is used.

Parameters<span class="colon">:</span>  
**cls** – Lattice class to be instantiated. Defaults to
pymatgen.core.Lattice.

Example

lattice_from_abivars(acell=3\*\[10\], rprim=np.eye(3))

<!-- -->

<span class="sig-name descname"><span class="pre">species_by_znucl</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.IStructure"
class="reference internal"
title="pymatgen.core.structure.IStructure"><span
class="pre">IStructure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.periodic_table.Species"
class="reference internal"
title="pymatgen.core.periodic_table.Species"><span
class="pre">Species</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.periodic_table.Element"
class="reference internal"
title="pymatgen.core.periodic_table.Element"><span
class="pre">Element</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.periodic_table.DummySpecies"
class="reference internal"
title="pymatgen.core.periodic_table.DummySpecies"><span
class="pre">DummySpecies</span></a><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L168-L187"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.species_by_znucl"
class="headerlink" title="Link to this definition"></a>  
Get list of unique specie found in structure **ordered according to
sites**.

Example

Site0: 0.5 0 0 O Site1: 0 0 0 Si

produces \[Specie_O, Specie_Si\] and not set(\[Specie_O, Specie_Si\]) as
in types_of_specie

<!-- -->

<span class="sig-name descname"><span class="pre">structure_from_abivars</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">cls</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*</span></span><span class="n"><span class="pre">args</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L102-L165"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.structure_from_abivars"
class="headerlink" title="Link to this definition"></a>  
Build a Structure object from a dictionary with ABINIT variables.

Parameters<span class="colon">:</span>  
**cls** – Structure class to be instantiated. Defaults to Structure.

Example

al_structure = structure_from_abivars(  
acell=3\*\[7.5\], rprim=\[0.0, 0.5, 0.5, 0.5, 0.0, 0.5, 0.5, 0.5, 0.0\],
typat=1, xred=\[0.0, 0.0, 0.0\], ntypat=1, znucl=13,

)

xred can be replaced with xcart or xangst.

<!-- -->

<span class="sig-name descname"><span class="pre">structure_to_abivars</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.IStructure"
class="reference internal"
title="pymatgen.core.structure.IStructure"><span
class="pre">IStructure</span></a></span>*, *<span class="n"><span class="pre">enforce_znucl</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">enforce_typat</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abiobjects.py#L190-L284"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abiobjects.structure_to_abivars"
class="headerlink" title="Link to this definition"></a>  
Receives a structure and returns a dictionary with ABINIT variables.

Parameters<span class="colon">:</span>  
- **enforce_znucl** (*list*) – ntypat entries with the value of Z for
  each type of atom. Used to change the default ordering. Defaults to
  None.

- **enforce_typat** (*list*) – natom entries with the type index.
  Fortran conventions: start to count from 1. Used to change the default
  ordering.

</div>

<div id="module-pymatgen.io.abinit.abitimer" class="section">

<span id="pymatgen-io-abinit-abitimer-module"></span>

## pymatgen.io.abinit.abitimer module<a href="#module-pymatgen.io.abinit.abitimer" class="headerlink"
title="Link to this heading"></a>

This module provides objects for extracting timing data from the ABINIT
output files It also provides tools to analyze and to visualize the
parallel efficiency.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">AbinitTimer</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">sections</span></span>*, *<span class="n"><span class="pre">info</span></span>*, *<span class="n"><span class="pre">cpu_time</span></span>*, *<span class="n"><span class="pre">wall_time</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L644-L914"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimer" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Container class storing the timing results.

Parameters<span class="colon">:</span>  
- **sections** – List of sections

- **info** – Dictionary with extra info.

- **cpu_time** – Cpu-time in seconds.

- **wall_time** – Wall-time in seconds.

<span class="sig-name descname"><span class="pre">cpuwall_histogram</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">ax</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Axes</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../util/plotting.py#L804-L836"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimer.cpuwall_histogram"
class="headerlink" title="Link to this definition"></a>  
Plot histogram with cpu- and wall-time on axis ax.

Parameters<span class="colon">:</span>  
**ax** – matplotlib Axes or None if a new figure should be created.

Returns<span class="colon">:</span>  
matplotlib figure

Return type<span class="colon">:</span>  
plt.Figure

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

<span class="sig-name descname"><span class="pre">get_dataframe</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">sort_key</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'wall_time'</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L720-L732"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimer.get_dataframe"
class="headerlink" title="Link to this definition"></a>  
Return a pandas DataFrame with entries sorted according to sort_key.

<span class="sig-name descname"><span class="pre">get_section</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">section_name</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L681-L687"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimer.get_section"
class="headerlink" title="Link to this definition"></a>  
Return section associated to section_name.

<span class="sig-name descname"><span class="pre">get_values</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">keys</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L734-L739"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimer.get_values"
class="headerlink" title="Link to this definition"></a>  
Return a list of values associated to a particular list of keys.

<span class="sig-name descname"><span class="pre">names_and_values</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">key</span></span>*, *<span class="n"><span class="pre">minval</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">minfract</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sorted</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L741-L791"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimer.names_and_values"
class="headerlink" title="Link to this definition"></a>  
Select the entries whose value\[key\] is \>= minval or whose
fraction\[key\] is \>= minfract Return the names of the sections and the
corresponding values.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ncpus</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abitimer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimer.ncpus"
class="headerlink" title="Link to this definition"></a>  
Total number of CPUs employed.

<span class="sig-name descname"><span class="pre">order_sections</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">key</span></span>*, *<span class="n"><span class="pre">reverse</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L800-L802"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimer.order_sections"
class="headerlink" title="Link to this definition"></a>  
Sort sections according to the value of key.

<span class="sig-name descname"><span class="pre">pie</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">key</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'wall_time'</span></span>*, *<span class="n"><span class="pre">minfract</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.05</span></span>*, *<span class="n"><span class="pre">ax</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Axes</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../util/plotting.py#L838-L857"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimer.pie"
class="headerlink" title="Link to this definition"></a>  
Plot pie chart for this timer.

Parameters<span class="colon">:</span>  
- **key** – Keyword used to extract data from the timer.

- **minfract** – Don’t show sections whose relative weight is less that
  minfract.

- **ax** – matplotlib Axes or None if a new figure should be created.

Returns<span class="colon">:</span>  
matplotlib figure

Return type<span class="colon">:</span>  
plt.Figure

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

<span class="sig-name descname"><span class="pre">scatter_hist</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">ax</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Axes</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../util/plotting.py#L859-L914"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimer.scatter_hist"
class="headerlink" title="Link to this definition"></a>  
Scatter plot + histogram.

Parameters<span class="colon">:</span>  
**ax** – matplotlib Axes or None if a new figure should be created.

Returns<span class="colon">:</span>  
matplotlib figure

Return type<span class="colon">:</span>  
plt.Figure

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

<span class="sig-name descname"><span class="pre">sum_sections</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">keys</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L796-L798"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimer.sum_sections"
class="headerlink" title="Link to this definition"></a>  
Sum value of keys.

<span class="sig-name descname"><span class="pre">to_csv</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">fileobj=\<\_io.TextIOWrapper</span> <span class="pre">name='\<stdout\>'</span> <span class="pre">mode='w'</span> <span class="pre">encoding='utf-8'\></span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L689-L700"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimer.to_csv"
class="headerlink" title="Link to this definition"></a>  
Write data on file fileobj using CSV format.

<span class="sig-name descname"><span class="pre">to_table</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">sort_key</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'wall_time'</span></span>*, *<span class="n"><span class="pre">stop</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L702-L714"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimer.to_table"
class="headerlink" title="Link to this definition"></a>  
Return a table (list of lists) with timer data.

<span class="sig-name descname"><span class="pre">totable</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*</span></span><span class="n"><span class="pre">args</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../../../.venv/lib/python3.11/site-packages/monty/dev.py#L716-L718"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimer.totable"
class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">exception</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">AbinitTimerParseError</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L38-L39"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimerParseError"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="pymatgen.io.html#pymatgen.io.core.ParseError"
class="reference internal" title="pymatgen.io.core.ParseError"><span
class="pre"><code class="sourceCode python">ParseError</code></span></a>

Errors raised by AbinitTimerParser.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">AbinitTimerParser</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L42-L503"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`Iterable`</span>

Responsible for parsing a list of output files, extracting the timing
results and analyzing the results. Assume the Abinit output files have
been produced with timopt -1.

Example

parser = AbinitTimerParser() parser.parse(list_of_files)

To analyze all [<span id="id2" class="problematic">\*</span>](#id1).abo
files within top, use:

> <div>
>
> parser, paths, okfiles = AbinitTimerParser.walk(top=”.”, ext=”.abo”)
>
> </div>

<span class="sig-name descname"><span class="pre">BEGIN_TAG</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'-\<BEGIN_TIMER'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abitimer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.BEGIN_TAG"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">END_TAG</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'-\<END_TIMER\>'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abitimer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.END_TAG"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">Error</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L38-L39"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.Error"
class="headerlink" title="Link to this definition"></a>  
alias of <a href="#pymatgen.io.abinit.abitimer.AbinitTimerParseError"
class="reference internal"
title="pymatgen.io.abinit.abitimer.AbinitTimerParseError"><span
class="pre"><code
class="sourceCode python">AbinitTimerParseError</code></span></a>

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">filenames</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abitimer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.filenames"
class="headerlink" title="Link to this definition"></a>  
List of files that have been parsed successfully.

<span class="sig-name descname"><span class="pre">get_sections</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">section_name</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L236-L249"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.get_sections"
class="headerlink" title="Link to this definition"></a>  
Get the list of sections stored in self.timers() given section_name A
fake section is returned if the timer does not have section_name.

<span class="sig-name descname"><span class="pre">parse</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filenames</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L103-L135"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.parse"
class="headerlink" title="Link to this definition"></a>  
Read and parse a filename or a list of filenames. Files that cannot be
opened are ignored. A single filename may also be given.

Returns<span class="colon">:</span>  
list of successfully read files.

<span class="sig-name descname"><span class="pre">pefficiency</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L251-L308"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.pefficiency"
class="headerlink" title="Link to this definition"></a>  
Analyze the parallel efficiency.

Returns<span class="colon">:</span>  
ParallelEfficiency object.

<span class="sig-name descname"><span class="pre">plot_all</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">show</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L496-L503"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.plot_all"
class="headerlink" title="Link to this definition"></a>  
Call all plot methods provided by the parser.

<span class="sig-name descname"><span class="pre">plot_efficiency</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">key</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'wall_time'</span></span>*, *<span class="n"><span class="pre">what</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'good+bad'</span></span>*, *<span class="n"><span class="pre">nmax</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">5</span></span>*, *<span class="n"><span class="pre">ax</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Axes</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../util/plotting.py#L334-L407"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.plot_efficiency"
class="headerlink" title="Link to this definition"></a>  
Plot the parallel efficiency.

Parameters<span class="colon">:</span>  
- **key** – Parallel efficiency is computed using the wall_time.

- **what** – Specifies what to plot: good for sections with good
  parallel efficiency. bad for sections with bad efficiency. Options can
  be concatenated with +.

- **nmax** – Maximum number of entries in plot

- **ax** – matplotlib Axes or None if a new figure should be created.

| kwargs     | Meaning                            |
|------------|------------------------------------|
| linewidth  | matplotlib linewidth. Default: 2.0 |
| markersize | matplotlib markersize. Default: 10 |

Returns<span class="colon">:</span>  
matplotlib figure

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

<span class="sig-name descname"><span class="pre">plot_pie</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">key</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'wall_time'</span></span>*, *<span class="n"><span class="pre">minfract</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.05</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../util/plotting.py#L409-L432"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.plot_pie"
class="headerlink" title="Link to this definition"></a>  
Plot pie charts of the different timers.

Parameters<span class="colon">:</span>  
- **key** – Keyword used to extract data from timers.

- **minfract** – Don’t show sections whose relative weight is less that
  minfract.

Returns<span class="colon">:</span>  
matplotlib figure

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

<span class="sig-name descname"><span class="pre">plot_stacked_hist</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">key</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'wall_time'</span></span>*, *<span class="n"><span class="pre">nmax</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">5</span></span>*, *<span class="n"><span class="pre">ax</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Axes</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../util/plotting.py#L434-L494"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.plot_stacked_hist"
class="headerlink" title="Link to this definition"></a>  
Plot stacked histogram of the different timers.

Parameters<span class="colon">:</span>  
- **key** – Keyword used to extract data from the timers. Only the first
  nmax sections with largest value are show.

- **nmax** – Maximum number of sections to show. Other entries are
  grouped together in the others section.

- **ax** – matplotlib Axes or None if a new figure should be created.

Returns<span class="colon">:</span>  
matplotlib figure

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

<span class="sig-name descname"><span class="pre">section_names</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">ordkey</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'wall_time'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L220-L234"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.section_names"
class="headerlink" title="Link to this definition"></a>  
Get the names of sections ordered by ordkey. For the time being, the
values are taken from the first timer.

<span class="sig-name descname"><span class="pre">summarize</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L310-L332"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.summarize"
class="headerlink" title="Link to this definition"></a>  
Return pandas DataFrame with the most important results stored in the
timers.

<span class="sig-name descname"><span class="pre">timers</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">mpi_rank</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'0'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L214-L218"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.timers"
class="headerlink" title="Link to this definition"></a>  
Return the list of timers associated to the given filename and MPI rank
mpi_rank.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">walk</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">top</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'.'</span></span>*, *<span class="n"><span class="pre">ext</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'.abo'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L65-L82"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimerParser.walk"
class="headerlink" title="Link to this definition"></a>  
Scan directory tree starting from top, look for files with extension ext
and parse timing data.

Returns<span class="colon">:</span>  
the new object paths: the list of files found ok_files: list of files
that have been parsed successfully.

> <div>
>
> (ok_files == paths) if all files have been parsed.
>
> </div>

Return type<span class="colon">:</span>  
parser

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">AbinitTimerSection</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">name</span></span>*, *<span class="n"><span class="pre">cpu_time</span></span>*, *<span class="n"><span class="pre">cpu_fract</span></span>*, *<span class="n"><span class="pre">wall_time</span></span>*, *<span class="n"><span class="pre">wall_fract</span></span>*, *<span class="n"><span class="pre">ncalls</span></span>*, *<span class="n"><span class="pre">gflops</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L574-L641"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimerSection"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Record with the timing results associated to a section of code.

Parameters<span class="colon">:</span>  
- **name** – Name of the sections.

- **cpu_time** – CPU time in seconds.

- **cpu_fract** – Percentage of CPU time.

- **wall_time** – Wall-time in seconds.

- **wall_fract** – Percentage of wall-time.

- **ncalls** – Number of calls

- **gflops** – Gigaflops.

<span class="sig-name descname"><span class="pre">FIELDS</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">('name',</span> <span class="pre">'wall_time',</span> <span class="pre">'wall_fract',</span> <span class="pre">'cpu_time',</span> <span class="pre">'cpu_fract',</span> <span class="pre">'ncalls',</span> <span class="pre">'gflops')</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abitimer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimerSection.FIELDS"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">NUMERIC_FIELDS</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">('wall_time',</span> <span class="pre">'wall_fract',</span> <span class="pre">'cpu_time',</span> <span class="pre">'cpu_fract',</span> <span class="pre">'ncalls',</span> <span class="pre">'gflops')</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abitimer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimerSection.NUMERIC_FIELDS"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">STR_FIELDS</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">('name',)</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/abitimer.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimerSection.STR_FIELDS"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L618-L620"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimerSection.as_dict"
class="headerlink" title="Link to this definition"></a>  
Get the values as a dictionary.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">fake</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L590-L593"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimerSection.fake"
class="headerlink" title="Link to this definition"></a>  
Return a fake section. Mainly used to fill missing entries if needed.

<span class="sig-name descname"><span class="pre">to_csvline</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">with_header</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L626-L634"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimerSection.to_csvline"
class="headerlink" title="Link to this definition"></a>  
Return a string with data in CSV format. Add header if with_header.

<span class="sig-name descname"><span class="pre">to_dict</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*</span></span><span class="n"><span class="pre">args</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../../../.venv/lib/python3.11/site-packages/monty/dev.py#L622-L624"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimerSection.to_dict"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">to_tuple</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L614-L616"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.AbinitTimerSection.to_tuple"
class="headerlink" title="Link to this definition"></a>  
Get the values as a tuple.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ParallelEfficiency</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filenames</span></span>*, *<span class="n"><span class="pre">ref_idx</span></span>*, *<span class="o"><span class="pre">\*</span></span><span class="n"><span class="pre">args</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L506-L571"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.ParallelEfficiency"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`dict`</span>

Store results concerning the parallel efficiency of the job.

Parameters<span class="colon">:</span>  
- **filenames** – List of filenames

- **ref_idx** – Index of the Reference time (calculation done with the
  smallest number of cpus).

<span class="sig-name descname"><span class="pre">bad_sections</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">key</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'wall_time'</span></span>*, *<span class="n"><span class="pre">criterion</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'mean'</span></span>*, *<span class="n"><span class="pre">nmax</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">5</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L568-L571"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.ParallelEfficiency.bad_sections"
class="headerlink" title="Link to this definition"></a>  
Return first nmax sections with worst value of key key using criterion
criterion.

<span class="sig-name descname"><span class="pre">good_sections</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">key</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'wall_time'</span></span>*, *<span class="n"><span class="pre">criterion</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'mean'</span></span>*, *<span class="n"><span class="pre">nmax</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">5</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L563-L566"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.ParallelEfficiency.good_sections"
class="headerlink" title="Link to this definition"></a>  
Return first nmax sections with best value of key key using criterion
criterion.

<span class="sig-name descname"><span class="pre">totable</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">stop</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">reverse</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L541-L561"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.ParallelEfficiency.totable"
class="headerlink" title="Link to this definition"></a>  
Get table (list of lists) with timing results.

Parameters<span class="colon">:</span>  
- **stop** – Include results up to stop. None for all

- **reverse** – Put items with highest wall_time in first positions if
  True.

<!-- -->

<span class="sig-name descname"><span class="pre">alternate</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*</span></span><span class="n"><span class="pre">iterables</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/abitimer.py#L26-L35"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.abitimer.alternate" class="headerlink"
title="Link to this definition"></a>  
\[a\[0\], b\[0\], … , a\[1\], b\[1\], …, a\[n\], b\[n\] …\] \>\>\>
alternate(\[1, 4\], \[2, 5\], \[3, 6\]) \[1, 2, 3, 4, 5, 6\].

</div>

<div id="module-pymatgen.io.abinit.inputs" class="section">

<span id="pymatgen-io-abinit-inputs-module"></span>

## pymatgen.io.abinit.inputs module<a href="#module-pymatgen.io.abinit.inputs" class="headerlink"
title="Link to this heading"></a>

This module defines a simplified interface for generating ABINIT input
files. Note that not all the features of Abinit are supported by
BasicAbinitInput. For a more comprehensive implementation, use the
AbinitInput object provided by AbiPy.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">AbstractInput</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L588-L699"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.AbstractInput" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MutableMapping`</span>, <span
class="pre">`ABC`</span>

Abstract class defining the methods that must be implemented by Input
objects.

<span class="sig-name descname"><span class="pre">deepcopy</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L623-L625"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.AbstractInput.deepcopy"
class="headerlink" title="Link to this definition"></a>  
Deep copy of the input.

<span class="sig-name descname"><span class="pre">pop_vars</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">keys</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L654-L666"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.AbstractInput.pop_vars"
class="headerlink" title="Link to this definition"></a>  
Remove the variables listed in keys. Return dictionary with the
variables that have been removed. Unlike remove_vars, no exception is
raised if the variables are not in the input.

Parameters<span class="colon">:</span>  
**keys** – string or list of strings with variable names.

Example

inp.pop_vars(\[“ionmov”, “optcell”, “ntime”, “dilatmx”\])

<span class="sig-name descname"><span class="pre">remove_vars</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">keys</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">strict</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><a href="#pymatgen.io.abinit.variable.InputVariable"
class="reference internal"
title="pymatgen.io.abinit.variable.InputVariable"><span
class="pre">InputVariable</span></a><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L668-L686"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.AbstractInput.remove_vars"
class="headerlink" title="Link to this definition"></a>  
Remove the variables listed in keys. Return dictionary with the
variables that have been removed.

Parameters<span class="colon">:</span>  
- **keys** – string or list of strings with variable names.

- **strict** – If True, KeyError is raised if at least one variable is
  not present.

<span class="sig-name descname"><span class="pre">set_vars</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*</span></span><span class="n"><span class="pre">args</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L627-L637"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.AbstractInput.set_vars"
class="headerlink" title="Link to this definition"></a>  
Set the value of the variables. Return dict with the variables added to
the input.

Example

input.set_vars(ecut=10, ionmov=3)

<span class="sig-name descname"><span class="pre">set_vars_ifnotin</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*</span></span><span class="n"><span class="pre">args</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L639-L652"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.AbstractInput.set_vars_ifnotin"
class="headerlink" title="Link to this definition"></a>  
Set the value of the variables but only if the variable is not already
present. Return dict with the variables added to the input.

Example

input.set_vars(ecut=10, ionmov=3)

*<span class="k"><span class="pre">abstractmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">to_str</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L697-L699"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.AbstractInput.to_str"
class="headerlink" title="Link to this definition"></a>  
Get a string with the input.

*<span class="k"><span class="pre">abstract</span></span><span class="w"> </span><span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">vars</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.AbstractInput.vars"
class="headerlink" title="Link to this definition"></a>  
Dictionary with the input variables. Used to implement dict-like
interface.

<span class="sig-name descname"><span class="pre">write</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filepath</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'run.abi'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L614-L621"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.AbstractInput.write"
class="headerlink" title="Link to this definition"></a>  
Write the input file to file to filepath.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">BasicAbinitInput</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span>*, *<span class="n"><span class="pre">pseudos</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.io.abinit.pseudos.Pseudo" class="reference internal"
title="pymatgen.io.abinit.pseudos.Pseudo"><span
class="pre">Pseudo</span></a><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="#pymatgen.io.abinit.pseudos.PseudoTable"
class="reference internal"
title="pymatgen.io.abinit.pseudos.PseudoTable"><span
class="pre">PseudoTable</span></a></span>*, *<span class="n"><span class="pre">pseudo_dir</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">comment</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">abi_args</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">abi_kwargs</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L706-L997"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicAbinitInput" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.abinit.inputs.AbstractInput"
class="reference internal"
title="pymatgen.io.abinit.inputs.AbstractInput"><span class="pre"><code
class="sourceCode python">AbstractInput</code></span></a>, <span
class="pre">`MSONable`</span>

Store the ABINIT variables for a single dataset.

Parameters<span class="colon">:</span>  
- **structure** (*file with*) – Parameters defining the crystalline
  structure. Accepts [<span id="id4"
  class="problematic">\|Structure\|</span>](#id3) object

- **structure**

- **pseudos** – Pseudopotentials to be used for the calculation.
  Accepts: string or list of strings with the name of the
  pseudopotential files, list of [<span id="id6"
  class="problematic">\|Pseudo\|</span>](#id5) objects or [<span
  id="id8" class="problematic">\|PseudoTable\|</span>](#id7) object.

- **pseudo_dir** – Name of the directory where the pseudopotential files
  are located.

- **ndtset** – Number of datasets.

- **comment** – Optional string with a comment that will be placed at
  the beginning of the file.

- **abi_args** – list of tuples (key, value) with the initial set of
  variables. Default: Empty

- **abi_kwargs** – Dictionary with the initial set of variables.
  Default: Empty.

<span class="sig-name descname"><span class="pre">Error</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L702-L703"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.Error"
class="headerlink" title="Link to this definition"></a>  
alias of <a href="#pymatgen.io.abinit.inputs.BasicAbinitInputError"
class="reference internal"
title="pymatgen.io.abinit.inputs.BasicAbinitInputError"><span
class="pre"><code
class="sourceCode python">BasicAbinitInputError</code></span></a>

<span class="sig-name descname"><span class="pre">add_abiobjects</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*</span></span><span class="n"><span class="pre">abi_objects</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L795-L802"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.add_abiobjects"
class="headerlink" title="Link to this definition"></a>  
For a list of AbiVarable objects, add the corresponding variables to the
input.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L766-L782"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.as_dict"
class="headerlink" title="Link to this definition"></a>  
JSON interface used in pymatgen for easier serialization.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">comment</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.comment"
class="headerlink" title="Link to this definition"></a>  
Optional string with comment. None if comment is not set.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L789-L793"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.from_dict"
class="headerlink" title="Link to this definition"></a>  
JSON interface used in pymatgen for easier serialization.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">isnc</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.isnc"
class="headerlink" title="Link to this definition"></a>  
True if norm-conserving calculation.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ispaw</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.ispaw"
class="headerlink" title="Link to this definition"></a>  
True if PAW calculation.

<span class="sig-name descname"><span class="pre">new_with_vars</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*</span></span><span class="n"><span class="pre">args</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L974-L983"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.new_with_vars"
class="headerlink" title="Link to this definition"></a>  
Get a new input with the given variables.

Example

new = input.new_with_vars(ecut=20)

<span class="sig-name descname"><span class="pre">pop_irdvars</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L992-L997"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.pop_irdvars"
class="headerlink" title="Link to this definition"></a>  
Remove all the ird\* variables present in self. Return dictionary with
the variables that have been removed.

<span class="sig-name descname"><span class="pre">pop_tolerances</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L985-L990"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.pop_tolerances"
class="headerlink" title="Link to this definition"></a>  
Remove all the tolerance variables present in self. Return dictionary
with the variables that have been removed.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">pseudos</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.pseudos"
class="headerlink" title="Link to this definition"></a>  
List of [<span id="id10" class="problematic">\|Pseudo\|</span>](#id9)
objects.

<span class="sig-name descname"><span class="pre">set_comment</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">comment</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L878-L880"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.set_comment"
class="headerlink" title="Link to this definition"></a>  
Set a comment to be included at the top of the file.

<span class="sig-name descname"><span class="pre">set_gamma_sampling</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L910-L912"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.set_gamma_sampling"
class="headerlink" title="Link to this definition"></a>  
Gamma-only sampling of the BZ.

<span class="sig-name descname"><span class="pre">set_kmesh</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">ngkpt</span></span>*, *<span class="n"><span class="pre">shiftk</span></span>*, *<span class="n"><span class="pre">kptopt</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L899-L908"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.set_kmesh"
class="headerlink" title="Link to this definition"></a>  
Set the variables for the sampling of the BZ.

Parameters<span class="colon">:</span>  
- **ngkpt** – Monkhorst-Pack divisions

- **shiftk** – List of shifts.

- **kptopt** – Option for the generation of the mesh.

<span class="sig-name descname"><span class="pre">set_kpath</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">ndivsm</span></span>*, *<span class="n"><span class="pre">kptbounds</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">iscf</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">-2</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L914-L939"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.set_kpath"
class="headerlink" title="Link to this definition"></a>  
Set the variables for the computation of the electronic band structure.

Parameters<span class="colon">:</span>  
- **ndivsm** – Number of divisions for the smallest segment.

- **kptbounds** – k-points defining the path in k-space. If None, we use
  the default high-symmetry k-path defined in the pymatgen database.

<span class="sig-name descname"><span class="pre">set_spin_mode</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">spin_mode</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L941-L957"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.set_spin_mode"
class="headerlink" title="Link to this definition"></a>  
Set the variables used to the treat the spin degree of freedom. Return
dictionary with the variables that have been removed.

Parameters<span class="colon">:</span>  
- **spin_mode** – SpinMode object or string. Possible values for string
  are:

- **polarized** (*-*)

- **unpolarized** (*-*)

- **afm** (*-*)

- **spinor** (*-*)

- **spinor_nomag** (*-*)

<span class="sig-name descname"><span class="pre">set_structure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L887-L896"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.set_structure"
class="headerlink" title="Link to this definition"></a>  
Set structure.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">structure</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.structure"
class="headerlink" title="Link to this definition"></a>  
The [<span id="id12" class="problematic">\|Structure\|</span>](#id11)
object associated to this input.

<span class="sig-name descname"><span class="pre">to_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">post</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">with_structure</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">with_pseudos</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">exclude</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L821-L868"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.to_str"
class="headerlink" title="Link to this definition"></a>  
String representation.

Parameters<span class="colon">:</span>  
- **post** – String that will be appended to the name of the variables
  Note that post is usually autodetected when we have multiple
  datatasets It is mainly used when we have an input file with a single
  dataset so that we can prevent the code from adding “1” to the name of
  the variables (In this case, indeed, Abinit complains if ndtset=1 is
  not specified and we don’t want ndtset=1 simply because the code will
  start to add \_DS1\_ to all the input and output files.

- **with_structure** – False if section with structure variables should
  not be printed.

- **with_pseudos** – False if JSON section with pseudo data should not
  be added.

- **exclude** – List of variable names that should be ignored.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">vars</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicAbinitInput.vars"
class="headerlink" title="Link to this definition"></a>  
Dictionary with variables.

<!-- -->

*<span class="k"><span class="pre">exception</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">BasicAbinitInputError</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L702-L703"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicAbinitInputError"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`Exception`</span>

Base error class for exceptions raised by BasicAbinitInput.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">BasicMultiDataset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">pseudos</span></span>*, *<span class="n"><span class="pre">pseudo_dir</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">''</span></span>*, *<span class="n"><span class="pre">ndtset</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L1000-L1302"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicMultiDataset"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

This object is essentially a list of BasicAbinitInputs. that provides an
easy-to-use interface to apply global changes to the the inputs stored
in the objects.

Let’s assume for example that multi contains two BasicAbinitInputs and
we want to set ecut to 1 in both dictionaries. The direct approach would
be:

> <div>
>
> for inp in multi:  
> inp.set_vars(ecut=1)
>
> </div>

or alternatively:

> <div>
>
> for i in range(multi.ndtset):  
> multi\[i\].set_vars(ecut=1)
>
> </div>

BasicMultiDataset provides its own implementation of \_\_getattr\_\_ so
that one can simply use:

> <div>
>
> multi.set_vars(ecut=1)
>
> multi.get(“ecut”) returns a list of values. It’s equivalent to:
>
> > <div>
> >
> > \[inp\[“ecut”\] for inp in multi\]
> >
> > </div>
>
> Note that if “ecut” is not present in one of the input of multi, the
> corresponding entry is set to None. A default value can be specified
> with:
>
> > <div>
> >
> > multi.get(“paral_kgb”, 0)
> >
> > </div>
>
> </div>

<div class="admonition warning">

Warning

BasicMultiDataset does not support calculations done with different sets
of pseudopotentials. The inputs can have different crystalline
structures (as long as the atom types are equal) but each input in
BasicMultiDataset must have the same set of pseudopotentials.

</div>

Parameters<span class="colon">:</span>  
- **structure** – file with the structure, [<span id="id14"
  class="problematic">\|Structure\|</span>](#id13) object or dictionary
  with ABINIT geo variable Accepts also list of objects that can be
  converted to Structure object. In this case, however, ndtset must be
  equal to the length of the list.

- **pseudos** – String or list of string with the name of the
  pseudopotential files.

- **pseudo_dir** – Name of the directory where the pseudopotential files
  are located.

- **ndtset** – Number of datasets.

<span class="sig-name descname"><span class="pre">Error</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L702-L703"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicMultiDataset.Error"
class="headerlink" title="Link to this definition"></a>  
alias of <a href="#pymatgen.io.abinit.inputs.BasicAbinitInputError"
class="reference internal"
title="pymatgen.io.abinit.inputs.BasicAbinitInputError"><span
class="pre"><code
class="sourceCode python">BasicAbinitInputError</code></span></a>

<span class="sig-name descname"><span class="pre">addnew_from</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dtindex</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L1208-L1210"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicMultiDataset.addnew_from"
class="headerlink" title="Link to this definition"></a>  
Add a new entry in the multidataset by copying the input with index
dtindex.

<span class="sig-name descname"><span class="pre">append</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">abinit_input</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L1191-L1197"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicMultiDataset.append"
class="headerlink" title="Link to this definition"></a>  
Add a BasicAbinitInput to the list.

<span class="sig-name descname"><span class="pre">deepcopy</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L1216-L1218"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicMultiDataset.deepcopy"
class="headerlink" title="Link to this definition"></a>  
Deep copy of the BasicMultiDataset.

<span class="sig-name descname"><span class="pre">extend</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">abinit_inputs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L1199-L1206"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicMultiDataset.extend"
class="headerlink" title="Link to this definition"></a>  
Extends self with a list of BasicAbinitInputs.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_inputs</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">inputs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.io.abinit.inputs.BasicAbinitInput"
class="reference internal"
title="pymatgen.io.abinit.inputs.BasicAbinitInput"><span
class="pre">BasicAbinitInput</span></a><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L1084-L1102"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicMultiDataset.from_inputs"
class="headerlink" title="Link to this definition"></a>  
Construct a multidataset from a list of BasicAbinitInputs.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">has_same_structures</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.abinit.inputs.BasicMultiDataset.has_same_structures"
class="headerlink" title="Link to this definition"></a>  
True if all inputs in BasicMultiDataset are equal.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">isnc</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicMultiDataset.isnc"
class="headerlink" title="Link to this definition"></a>  
True if norm-conserving calculation.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ispaw</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicMultiDataset.ispaw"
class="headerlink" title="Link to this definition"></a>  
True if PAW calculation.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ndtset</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicMultiDataset.ndtset"
class="headerlink" title="Link to this definition"></a>  
Number of inputs in self.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">pseudos</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicMultiDataset.pseudos"
class="headerlink" title="Link to this definition"></a>  
Abinit pseudopotentials.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">replicate_input</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">input</span></span>*, *<span class="n"><span class="pre">ndtset</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L1104-L1112"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicMultiDataset.replicate_input"
class="headerlink" title="Link to this definition"></a>  
Construct a multidataset with ndtset from the BasicAbinitInput input.

<span class="sig-name descname"><span class="pre">split_datasets</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L1212-L1214"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicMultiDataset.split_datasets"
class="headerlink" title="Link to this definition"></a>  
Return list of BasicAbinitInputs.

<span class="sig-name descname"><span class="pre">to_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">with_pseudos</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L1228-L1293"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicMultiDataset.to_str"
class="headerlink" title="Link to this definition"></a>  
String representation i.e. the input file read by Abinit.

Parameters<span class="colon">:</span>  
**with_pseudos** – False if JSON section with pseudo data should not be
added.

<span class="sig-name descname"><span class="pre">write</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filepath</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'run.abi'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L1295-L1302"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.BasicMultiDataset.write"
class="headerlink" title="Link to this definition"></a>  
Write ndset input files to disk. The name of the file is constructed
from the dataset index e.g. run0.abi.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ShiftMode</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">value</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L135-L161"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.ShiftMode" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`Enum`</span>

Mode used to generate the shifts for the k-point sampling. G: Gamma
centered M: Monkhorst-Pack ((0.5, 0.5, 0.5)) S: Symmetric. Respects the
chksymbreak with multiple shifts O: OneSymmetric. Respects the
chksymbreak with a single shift (as in ‘S’ if a single shift is given,
gamma

> <div>
>
> centered otherwise.
>
> </div>

<span class="sig-name descname"><span class="pre">GammaCentered</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'G'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.ShiftMode.GammaCentered"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">MonkhorstPack</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'M'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.ShiftMode.MonkhorstPack"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">OneSymmetric</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'O'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.ShiftMode.OneSymmetric"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">Symmetric</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'S'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.ShiftMode.Symmetric"
class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_object</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">obj</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L150-L161"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.ShiftMode.from_object"
class="headerlink" title="Link to this definition"></a>  
Get an instance of ShiftMode based on the type of object passed.
Converts strings to ShiftMode depending on the initial letter of the
string. G for GammaCentered, M for MonkhorstPack, S for Symmetric, O for
OneSymmetric. Case insensitive.

<!-- -->

<span class="sig-name descname"><span class="pre">as_structure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">obj</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L113-L132"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.as_structure" class="headerlink"
title="Link to this definition"></a>  
Convert obj into a Structure. Accepts:

> <div>
>
> - Structure object.
>
> - Filename
>
> - Dictionaries (MSONable format or dictionaries with abinit
>   variables).
>
> </div>

<!-- -->

<span class="sig-name descname"><span class="pre">calc_shiftk</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span>*, *<span class="n"><span class="pre">symprec</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.01</span></span>*, *<span class="n"><span class="pre">angle_tolerance</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">5</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L479-L571"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.calc_shiftk" class="headerlink"
title="Link to this definition"></a>  
Find the values of shiftk and nshiftk appropriated for the sampling of
the Brillouin zone.

When the primitive vectors of the lattice do NOT form a FCC or a BCC
lattice, the usual (shifted) Monkhorst-Pack grids are formed by using
nshiftk=1 and shiftk 0.5 0.5 0.5 . This is often the preferred k point
sampling. For a non-shifted Monkhorst-Pack grid, use nshiftk=1 and
shiftk 0.0 0.0 0.0, but there is little reason to do that.

When the primitive vectors of the lattice form a FCC lattice, with
rprim:

> <div>
>
> 0.0 0.5 0.5 0.5 0.0 0.5 0.5 0.5 0.0
>
> </div>

the (very efficient) usual Monkhorst-Pack sampling will be generated by
using nshiftk= 4 and shiftk:

> <div>
>
> 0.5 0.5 0.5 0.5 0.0 0.0 0.0 0.5 0.0 0.0 0.0 0.5
>
> </div>

When the primitive vectors of the lattice form a BCC lattice, with
rprim:

> <div>
>
> -0.5 0.5 0.5  
> 0.5 -0.5 0.5 0.5 0.5 -0.5
>
> </div>

the usual Monkhorst-Pack sampling will be generated by using nshiftk= 2
and shiftk:

> <div>
>
> > <div>
> >
> > 0.25 0.25 0.25
> >
> > </div>
>
> -0.25 -0.25 -0.25
>
> </div>

However, the simple sampling nshiftk=1 and shiftk 0.5 0.5 0.5 is
excellent.

For hexagonal lattices with hexagonal axes, e.g. rprim:

> <div>
>
> > <div>
> >
> > 1.0 0.0 0.0
> >
> > </div>
>
> -0.5 sqrt(3)/2 0.0  
> 0.0 0.0 1.0
>
> </div>

one can use nshiftk= 1 and shiftk 0.0 0.0 0.5 In rhombohedral axes, e.g.
using angdeg 3\*60., this corresponds to shiftk 0.5 0.5 0.5, to keep the
shift along the symmetry axis.

Returns<span class="colon">:</span>  
Suggested value of shiftk.

<!-- -->

<span class="sig-name descname"><span class="pre">ebands_input</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span>*, *<span class="n"><span class="pre">pseudos</span></span>*, *<span class="n"><span class="pre">kppa</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">nscf_nband</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ndivsm</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">15</span></span>*, *<span class="n"><span class="pre">ecut</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">pawecutdg</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">scf_nband</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">accuracy</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'normal'</span></span>*, *<span class="n"><span class="pre">spin_mode</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'polarized'</span></span>*, *<span class="n"><span class="pre">smearing</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'fermi_dirac:0.1</span> <span class="pre">eV'</span></span>*, *<span class="n"><span class="pre">charge</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.0</span></span>*, *<span class="n"><span class="pre">scf_algorithm</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">dos_kppa</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L308-L410"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.ebands_input" class="headerlink"
title="Link to this definition"></a>  
Get a [<span id="id16"
class="problematic">\|BasicMultiDataset\|</span>](#id15) object for band
structure calculations.

Parameters<span class="colon">:</span>  
- **structure** – [<span id="id18"
  class="problematic">\|Structure\|</span>](#id17) object.

- **pseudos** – List of filenames or list of [<span id="id20"
  class="problematic">\|Pseudo\|</span>](#id19) objects or [<span
  id="id22" class="problematic">\|PseudoTable\|</span>](#id21) object.

- **kppa** – Defines the sampling used for the SCF run. Defaults to 1000
  if not given.

- **nscf_nband** – Number of bands included in the NSCF run. Set to
  scf_nband + 10 if None.

- **ndivsm** – Number of divisions used to sample the smallest segment
  of the k-path. if 0, only the GS input is returned in multi\[0\].

- **ecut** – cutoff energy in Ha (if None, ecut is initialized from the
  pseudos according to accuracy)

- **pawecutdg** – cutoff energy in Ha for PAW double-grid (if None,
  pawecutdg is initialized from the pseudos according to accuracy)

- **scf_nband** – Number of bands for SCF run. If scf_nband is None,
  nband is automatically initialized from the list of pseudos, the
  structure and the smearing option.

- **accuracy** – Accuracy of the calculation.

- **spin_mode** – Spin polarization.

- **smearing** – Smearing technique.

- **charge** – Electronic charge added to the unit cell.

- **scf_algorithm** – Algorithm used for solving of the SCF cycle.

- **dos_kppa** – Scalar or List of integers with the number of k-points
  per atom to be used for the computation of the DOS (None if DOS is not
  wanted).

<!-- -->

<span class="sig-name descname"><span class="pre">gs_input</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span>*, *<span class="n"><span class="pre">pseudos</span></span>*, *<span class="n"><span class="pre">kppa</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ecut</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">pawecutdg</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">scf_nband</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">accuracy</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'normal'</span></span>*, *<span class="n"><span class="pre">spin_mode</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'polarized'</span></span>*, *<span class="n"><span class="pre">smearing</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'fermi_dirac:0.1</span> <span class="pre">eV'</span></span>*, *<span class="n"><span class="pre">charge</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.0</span></span>*, *<span class="n"><span class="pre">scf_algorithm</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L260-L305"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.gs_input" class="headerlink"
title="Link to this definition"></a>  
Get a BasicAbinitInput for ground-state calculation.

Parameters<span class="colon">:</span>  
- **structure** – [<span id="id24"
  class="problematic">\|Structure\|</span>](#id23) object.

- **pseudos** – List of filenames or list of [<span id="id26"
  class="problematic">\|Pseudo\|</span>](#id25) objects or [<span
  id="id28" class="problematic">\|PseudoTable\|</span>](#id27) object.

- **kppa** – Defines the sampling used for the SCF run. Defaults to 1000
  if not given.

- **ecut** – cutoff energy in Ha (if None, ecut is initialized from the
  pseudos according to accuracy)

- **pawecutdg** – cutoff energy in Ha for PAW double-grid (if None,
  pawecutdg is initialized from the pseudos according to accuracy)

- **scf_nband** – Number of bands for SCF run. If scf_nband is None,
  nband is automatically initialized from the list of pseudos, the
  structure and the smearing option.

- **accuracy** – Accuracy of the calculation.

- **spin_mode** – Spin polarization.

- **smearing** – Smearing technique.

- **charge** – Electronic charge added to the unit cell.

- **scf_algorithm** – Algorithm used for solving of the SCF cycle.

<!-- -->

<span class="sig-name descname"><span class="pre">ion_ioncell_relax_input</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span>*, *<span class="n"><span class="pre">pseudos</span></span>*, *<span class="n"><span class="pre">kppa</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">nband</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ecut</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">pawecutdg</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">accuracy</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'normal'</span></span>*, *<span class="n"><span class="pre">spin_mode</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'polarized'</span></span>*, *<span class="n"><span class="pre">smearing</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'fermi_dirac:0.1</span> <span class="pre">eV'</span></span>*, *<span class="n"><span class="pre">charge</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.0</span></span>*, *<span class="n"><span class="pre">scf_algorithm</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">shift_mode</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'Monkhorst-pack'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L413-L476"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.ion_ioncell_relax_input"
class="headerlink" title="Link to this definition"></a>  
Get a [<span id="id30"
class="problematic">\|BasicMultiDataset\|</span>](#id29) for a
structural relaxation. The first dataset optimizes the atomic positions
at fixed unit cell. The second datasets optimizes both ions and unit
cell parameters.

Parameters<span class="colon">:</span>  
- **structure** – [<span id="id32"
  class="problematic">\|Structure\|</span>](#id31) object.

- **pseudos** – List of filenames or list of [<span id="id34"
  class="problematic">\|Pseudo\|</span>](#id33) objects or [<span
  id="id36" class="problematic">\|PseudoTable\|</span>](#id35) object.

- **kppa** – Defines the sampling used for the Brillouin zone.

- **nband** – Number of bands included in the SCF run.

- **accuracy** – Accuracy of the calculation.

- **spin_mode** – Spin polarization.

- **smearing** – Smearing technique.

- **charge** – Electronic charge added to the unit cell.

- **scf_algorithm** – Algorithm used for the solution of the SCF cycle.

<!-- -->

<span class="sig-name descname"><span class="pre">num_valence_electrons</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span>*, *<span class="n"><span class="pre">pseudos</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/inputs.py#L574-L585"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.inputs.num_valence_electrons"
class="headerlink" title="Link to this definition"></a>  
Get the number of valence electrons.

Parameters<span class="colon">:</span>  
**pseudos** – List of [<span id="id38"
class="problematic">\|Pseudo\|</span>](#id37) objects or list of
filenames.

</div>

<div id="module-pymatgen.io.abinit.netcdf" class="section">

<span id="pymatgen-io-abinit-netcdf-module"></span>

## pymatgen.io.abinit.netcdf module<a href="#module-pymatgen.io.abinit.netcdf" class="headerlink"
title="Link to this heading"></a>

Wrapper for netCDF readers.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">AbinitHeader</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*</span></span><span class="n"><span class="pre">args</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/netcdf.py#L474-L503"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.netcdf.AbinitHeader" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`AttrDict`</span>

Stores the values reported in the Abinit header.

<span class="sig-name descname"><span class="pre">to_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">verbose</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">title</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/netcdf.py#L485-L497"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.netcdf.AbinitHeader.to_str"
class="headerlink" title="Link to this definition"></a>  
String representation. kwargs are passed to pprint.pformat.

Parameters<span class="colon">:</span>  
- **verbose** – Verbosity level

- **title** – Title string.

<span class="sig-name descname"><span class="pre">to_string</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*</span></span><span class="n"><span class="pre">args</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../../../.venv/lib/python3.11/site-packages/monty/dev.py#L501-L503"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.netcdf.AbinitHeader.to_string"
class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">EtsfReader</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">path</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/netcdf.py#L241-L299"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.netcdf.EtsfReader" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.abinit.netcdf.NetcdfReader"
class="reference internal"
title="pymatgen.io.abinit.netcdf.NetcdfReader"><span class="pre"><code
class="sourceCode python">NetcdfReader</code></span></a>

This object reads data from a file written according to the ETSF-IO
specifications.

We assume that the netcdf file contains at least the crystallographic
section.

Open the Netcdf file specified by path (read mode).

<span class="sig-name descname"><span class="pre">chemical_symbols</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/netcdf.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.netcdf.EtsfReader.chemical_symbols"
class="headerlink" title="Link to this definition"></a>  
Chemical symbols char \[number of atom species\]\[symbol length\].

<span class="sig-name descname"><span class="pre">read_abinit_hdr</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/netcdf.py#L272-L299"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.netcdf.EtsfReader.read_abinit_hdr"
class="headerlink" title="Link to this definition"></a>  
Read the variables associated to the Abinit header.

Return AbinitHeader

<span class="sig-name descname"><span class="pre">read_abinit_xcfunc</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/netcdf.py#L267-L270"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.netcdf.EtsfReader.read_abinit_xcfunc"
class="headerlink" title="Link to this definition"></a>  
Read ixc from an Abinit file. Return XcFunc object.

<span class="sig-name descname"><span class="pre">read_structure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">cls=\<class</span> <span class="pre">'pymatgen.core.structure.Structure'\></span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/netcdf.py#L263-L265"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.netcdf.EtsfReader.read_structure"
class="headerlink" title="Link to this definition"></a>  
Get the crystalline structure stored in the rootgrp.

<span class="sig-name descname"><span class="pre">type_idx_from_symbol</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">symbol</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/netcdf.py#L259-L261"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.netcdf.EtsfReader.type_idx_from_symbol"
class="headerlink" title="Link to this definition"></a>  
Get the type index from the chemical symbol. Note python convention.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">NO_DEFAULT</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/netcdf.py#L70-L71"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.netcdf.NO_DEFAULT" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Signal that read_value should raise an Error.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">NetcdfReader</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">path</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/netcdf.py#L74-L238"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.netcdf.NetcdfReader" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Wraps and extends netCDF4.Dataset. Read only mode. Supports with
statements.

Additional documentation available at:  
<a href="https://unidata.github.io/netcdf4-python/"
class="reference external">https://unidata.github.io/netcdf4-python/</a>

Open the Netcdf file specified by path (read mode).

<span class="sig-name descname"><span class="pre">Error</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/netcdf.py#L66-L67"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.netcdf.NetcdfReader.Error"
class="headerlink" title="Link to this definition"></a>  
alias of <a href="#pymatgen.io.abinit.netcdf.NetcdfReaderError"
class="reference internal"
title="pymatgen.io.abinit.netcdf.NetcdfReaderError"><span
class="pre"><code
class="sourceCode python">NetcdfReaderError</code></span></a>

<span class="sig-name descname"><span class="pre">close</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/netcdf.py#L110-L115"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.netcdf.NetcdfReader.close"
class="headerlink" title="Link to this definition"></a>  
Close the file.

<span class="sig-name descname"><span class="pre">print_tree</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/netcdf.py#L130-L134"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.netcdf.NetcdfReader.print_tree"
class="headerlink" title="Link to this definition"></a>  
Print all the groups in the file.

<span class="sig-name descname"><span class="pre">read_dimvalue</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dimname</span></span>*, *<span class="n"><span class="pre">path='/'</span></span>*, *<span class="n"><span class="pre">default=\<class</span> <span class="pre">'pymatgen.io.abinit.netcdf.NO_DEFAULT'\></span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/netcdf.py#L136-L151"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.netcdf.NetcdfReader.read_dimvalue"
class="headerlink" title="Link to this definition"></a>  
Get the value of a dimension.

Parameters<span class="colon">:</span>  
- **dimname** – Name of the variable

- **path** – path to the group.

- **default** – return default if dimname is not present and default is
  not NO_DEFAULT else raise self.Error.

<span class="sig-name descname"><span class="pre">read_keys</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">keys</span></span>*, *<span class="n"><span class="pre">dict_cls=\<class</span> <span class="pre">'monty.collections.AttrDict'\></span></span>*, *<span class="n"><span class="pre">path='/'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/netcdf.py#L221-L238"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.netcdf.NetcdfReader.read_keys"
class="headerlink" title="Link to this definition"></a>  
Read a list of variables/dimensions from file. If a key is not present
the corresponding entry in the output dictionary is set to None.

<span class="sig-name descname"><span class="pre">read_value</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">varname</span></span>*, *<span class="n"><span class="pre">path='/'</span></span>*, *<span class="n"><span class="pre">cmode=None</span></span>*, *<span class="n"><span class="pre">default=\<class</span> <span class="pre">'pymatgen.io.abinit.netcdf.NO_DEFAULT'\></span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/netcdf.py#L160-L193"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.netcdf.NetcdfReader.read_value"
class="headerlink" title="Link to this definition"></a>  
Get the values of variable with name varname in the group specified by
path.

Parameters<span class="colon">:</span>  
- **varname** – Name of the variable

- **path** – path to the group.

- **cmode** – if cmode==”c”, a complex ndarrays is constructed and
  returned (netcdf does not provide native support from complex
  datatype).

- **default** – returns default if varname is not present. self.Error is
  raised if default is set to NO_DEFAULT

Returns<span class="colon">:</span>  
numpy array if varname represents an array, scalar otherwise.

<span class="sig-name descname"><span class="pre">read_variable</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">varname</span></span>*, *<span class="n"><span class="pre">path</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'/'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/netcdf.py#L195-L197"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.netcdf.NetcdfReader.read_variable"
class="headerlink" title="Link to this definition"></a>  
Get the variable with name varname in the group specified by path.

<span class="sig-name descname"><span class="pre">read_varnames</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">path</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'/'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/netcdf.py#L153-L158"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.netcdf.NetcdfReader.read_varnames"
class="headerlink" title="Link to this definition"></a>  
List of variable names stored in the group specified by path.

<span class="sig-name descname"><span class="pre">walk_tree</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">top</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/netcdf.py#L117-L128"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.netcdf.NetcdfReader.walk_tree"
class="headerlink" title="Link to this definition"></a>  
Navigate all the groups in the file starting from top. If top is None,
the root group is used.

<!-- -->

*<span class="k"><span class="pre">exception</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">NetcdfReaderError</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/netcdf.py#L66-L67"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.netcdf.NetcdfReaderError"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`Exception`</span>

Base error class for NetcdfReader.

<!-- -->

<span class="sig-name descname"><span class="pre">as_etsfreader</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">file</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/netcdf.py#L61-L63"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.netcdf.as_etsfreader" class="headerlink"
title="Link to this definition"></a>  
Return an EtsfReader. Accepts filename or EtsfReader.

<!-- -->

<span class="sig-name descname"><span class="pre">as_ncreader</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">file</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/netcdf.py#L52-L58"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.netcdf.as_ncreader" class="headerlink"
title="Link to this definition"></a>  
Convert file into a NetcdfReader instance. Returns reader, close_it
where close_it is set to True if we have to close the file before
leaving the procedure.

<!-- -->

<span class="sig-name descname"><span class="pre">structure_from_ncdata</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">ncdata</span></span>*, *<span class="n"><span class="pre">site_properties=None</span></span>*, *<span class="n"><span class="pre">cls=\<class</span> <span class="pre">'pymatgen.core.structure.Structure'\></span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/netcdf.py#L302-L368"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.netcdf.structure_from_ncdata"
class="headerlink" title="Link to this definition"></a>  
Read and return a pymatgen structure from a NetCDF file containing
crystallographic data in the ETSF-IO format.

Parameters<span class="colon">:</span>  
- **ncdata** – filename or NetcdfReader instance.

- **site_properties** – Dictionary with site properties.

- **cls** – The Structure class to instantiate.

</div>

<div id="module-pymatgen.io.abinit.pseudos" class="section">

<span id="pymatgen-io-abinit-pseudos-module"></span>

## pymatgen.io.abinit.pseudos module<a href="#module-pymatgen.io.abinit.pseudos" class="headerlink"
title="Link to this heading"></a>

This module provides objects describing the basic parameters of the
pseudopotentials used in Abinit, and a parser to instantiate
pseudopotential objects..

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">AbinitHeader</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L632-L642"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.AbinitHeader" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`dict`</span>

Dictionary whose keys can be also accessed as attributes.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">AbinitPseudo</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">path</span></span>*, *<span class="n"><span class="pre">header</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L445-L503"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.AbinitPseudo" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.abinit.pseudos.Pseudo" class="reference internal"
title="pymatgen.io.abinit.pseudos.Pseudo"><span class="pre"><code
class="sourceCode python">Pseudo</code></span></a>

An AbinitPseudo is a pseudopotential whose file contains an abinit
header.

Parameters<span class="colon">:</span>  
- **path** – Filename.

- **header** – AbinitHeader instance.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Z</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.AbinitPseudo.Z" class="headerlink"
title="Link to this definition"></a>  
The atomic number of the atom.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Z_val</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.AbinitPseudo.Z_val"
class="headerlink" title="Link to this definition"></a>  
Valence charge.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">l_local</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.AbinitPseudo.l_local"
class="headerlink" title="Link to this definition"></a>  
Angular momentum used for the local part.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">l_max</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.AbinitPseudo.l_max"
class="headerlink" title="Link to this definition"></a>  
Maximum angular momentum.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">summary</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.AbinitPseudo.summary"
class="headerlink" title="Link to this definition"></a>  
Summary line reported in the ABINIT header.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">supports_soc</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.AbinitPseudo.supports_soc"
class="headerlink" title="Link to this definition"></a>  
True if the pseudo can be used in a calculation with spin-orbit
coupling. Base classes should provide a concrete implementation that
computes this value.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Hint</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">ecut</span></span>*, *<span class="n"><span class="pre">pawecutdg</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L549-L576"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Hint" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Suggested value for the cutoff energy \[Hartree units\] and the cutoff
energy for the dense grid (only for PAW pseudos).

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L564-L571"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Hint.as_dict" class="headerlink"
title="Link to this definition"></a>  
Return dictionary for MSONable protocol.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L573-L576"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Hint.from_dict" class="headerlink"
title="Link to this definition"></a>  
Build instance from dictionary (MSONable protocol).

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">NcAbinitHeader</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">summary</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L662-L850"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.NcAbinitHeader" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.abinit.pseudos.AbinitHeader"
class="reference internal"
title="pymatgen.io.abinit.pseudos.AbinitHeader"><span class="pre"><code
class="sourceCode python">AbinitHeader</code></span></a>

The abinit header found in the NC pseudopotential files.

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">fhi_header</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span>*, *<span class="n"><span class="pre">ppdesc</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L709-L728"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.NcAbinitHeader.fhi_header"
class="headerlink" title="Link to this definition"></a>  
Parse the FHI abinit header. Example:

Troullier-Martins psp for element Sc Thu Oct 27 17:33:22 EDT 1994  
21.00000 3.00000 940714 zatom, zion, pspdat 1 1 2 0 2001 .00000
pspcod,pspxc,lmax,lloc,mmax,r2well 1.80626423934776 .22824404341771
1.17378968127746 rchrg,fchrg,qchrg

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">gth_header</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span>*, *<span class="n"><span class="pre">ppdesc</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L745-L762"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.NcAbinitHeader.gth_header"
class="headerlink" title="Link to this definition"></a>  
Parse the GTH abinit header. Example:

Goedecker-Teter-Hutter Wed May 8 14:27:44 EDT 1996 1 1 960508
zatom,zion,pspdat 2 1 0 0 2001 0. pspcod,pspxc,lmax,lloc,mmax,r2well
0.2000000 -4.0663326 0.6778322 0 0 rloc, c1, c2, c3, c4 0 0 0 rs, h1s,
h2s 0 0 rp, h1p

> <div>
>
> 1.36 .2 0.6 rcutoff, rloc
>
> </div>

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">hgh_header</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span>*, *<span class="n"><span class="pre">ppdesc</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L730-L743"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.NcAbinitHeader.hgh_header"
class="headerlink" title="Link to this definition"></a>  
Parse the HGH abinit header. Example:

Hartwigsen-Goedecker-Hutter psp for Ne, from PRB58, 3641 (1998)  
10 8 010605 zatom,zion,pspdat 3 1 1 0 2001 0
pspcod,pspxc,lmax,lloc,mmax,r2well

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">oncvpsp_header</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span>*, *<span class="n"><span class="pre">ppdesc</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L764-L790"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.NcAbinitHeader.oncvpsp_header"
class="headerlink" title="Link to this definition"></a>  
Parse the ONCVPSP abinit header. Example:

Li ONCVPSP r_core= 2.01 3.02  
> <div>
>
> > <div>
> >
> > 3.0000 3.0000 140504 zatom,zion,pspd
> >
> > </div>
>
> 8 2 1 4 600 0 pspcod,pspxc,lmax,lloc,mmax,r2well
>
> </div>

5.99000000 0.00000000 0.00000000 rchrg fchrg qchrg  
> <div>
>
> 2 2 0 0 0 nproj 0 extension_switch
>
> </div>

0 -2.5000025868368D+00 -1.2006906995331D+00  
1 0.0000000000000D+00 0.0000000000000D+00 0.0000000000000D+00 2
1.0000000000000D-02 4.4140499497377D-02 1.9909081701712D-02

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">tm_header</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span>*, *<span class="n"><span class="pre">ppdesc</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L792-L850"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.NcAbinitHeader.tm_header"
class="headerlink" title="Link to this definition"></a>  
Parse the TM abinit header. Example:

Troullier-Martins psp for element Fm Thu Oct 27 17:28:39 EDT 1994
100.00000 14.00000 940714 zatom, zion, pspdat

> <div>
>
> 1 1 3 0 2001 .00000 pspcod,pspxc,lmax,lloc,mmax,r2well 0 4.085 6.246 0
> 2.8786493 l,e99.0,e99.9,nproj,rcpsp .00000000 .0000000000 .0000000000
> .00000000 rms,ekb1,ekb2,epsatm 1 3.116 4.632 1 3.4291849
> l,e99.0,e99.9,nproj,rcpsp .00000000 .0000000000 .0000000000 .00000000
> rms,ekb1,ekb2,epsatm 2 4.557 6.308 1 2.1865358
> l,e99.0,e99.9,nproj,rcpsp .00000000 .0000000000 .0000000000 .00000000
> rms,ekb1,ekb2,epsatm 3 23.251 29.387 1 2.4776730
> l,e99.0,e99.9,nproj,rcpsp .00000000 .0000000000 .0000000000 .00000000
> rms,ekb1,ekb2,epsatm 3.62474762267880 .07409391739104 3.07937699839200
> rchrg,fchrg,qchrg
>
> </div>

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">NcAbinitPseudo</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">path</span></span>*, *<span class="n"><span class="pre">header</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L506-L532"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.NcAbinitPseudo" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.abinit.pseudos.NcPseudo"
class="reference internal"
title="pymatgen.io.abinit.pseudos.NcPseudo"><span class="pre"><code
class="sourceCode python">NcPseudo</code></span></a>,
<a href="#pymatgen.io.abinit.pseudos.AbinitPseudo"
class="reference internal"
title="pymatgen.io.abinit.pseudos.AbinitPseudo"><span class="pre"><code
class="sourceCode python">AbinitPseudo</code></span></a>

Norm-conserving pseudopotential in the Abinit format.

Parameters<span class="colon">:</span>  
- **path** – Filename.

- **header** – AbinitHeader instance.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Z</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.NcAbinitPseudo.Z"
class="headerlink" title="Link to this definition"></a>  
The atomic number of the atom.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Z_val</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.NcAbinitPseudo.Z_val"
class="headerlink" title="Link to this definition"></a>  
Number of valence electrons.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">l_local</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.NcAbinitPseudo.l_local"
class="headerlink" title="Link to this definition"></a>  
Angular momentum used for the local part.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">l_max</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.NcAbinitPseudo.l_max"
class="headerlink" title="Link to this definition"></a>  
Maximum angular momentum.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">nlcc_radius</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.NcAbinitPseudo.nlcc_radius"
class="headerlink" title="Link to this definition"></a>  
Radius at which the core charge vanish (i.e. cut-off in a.u.). Returns
0.0 if nlcc is not used.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">summary</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.NcAbinitPseudo.summary"
class="headerlink" title="Link to this definition"></a>  
Summary line reported in the ABINIT header.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">NcPseudo</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L387-L412"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.NcPseudo" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`ABC`</span>

Abstract class defining the methods that must be implemented by the
concrete classes representing norm-conserving pseudopotentials.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">has_nlcc</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.NcPseudo.has_nlcc"
class="headerlink" title="Link to this definition"></a>  
True if the pseudo is generated with non-linear core correction.

*<span class="k"><span class="pre">abstract</span></span><span class="w"> </span><span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">nlcc_radius</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.NcPseudo.nlcc_radius"
class="headerlink" title="Link to this definition"></a>  
Radius at which the core charge vanish (i.e. cut-off in a.u.). Returns
0.0 if nlcc is not used.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">rcore</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.NcPseudo.rcore" class="headerlink"
title="Link to this definition"></a>  
Radius of the pseudization sphere in a.u.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">PawAbinitHeader</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">summary</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L853-L976"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PawAbinitHeader" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.abinit.pseudos.AbinitHeader"
class="reference internal"
title="pymatgen.io.abinit.pseudos.AbinitHeader"><span class="pre"><code
class="sourceCode python">AbinitHeader</code></span></a>

The abinit header found in the PAW pseudopotential files.

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">paw_header</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span>*, *<span class="n"><span class="pre">ppdesc</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L902-L976"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PawAbinitHeader.paw_header"
class="headerlink" title="Link to this definition"></a>  
Parse the PAW abinit header. Examples:

Paw atomic data for element Ni - Generated by AtomPAW (N. Holzwarth) + AtomPAW2Abinit v3.0.5  
> <div>
>
> 28.000 18.000 20061204 : zatom,zion,pspdat 7 7 2 0 350 0. :
> pspcod,pspxc,lmax,lloc,mmax,r2well
>
> </div>

paw3 1305<span class="classifier">pspfmt,creatorID</span>  
5 13 : basis_size,lmn_size

0 0 1 1 2 : orbitals 3 : number_of_meshes 1 3 350 1.1803778368E-05
3.5000000000E-02 : mesh 1, type,size,rad_step\[,log_step\] 2 1 921
2.500000000000E-03 : mesh 2, type,size,rad_step\[,log_step\] 3 3 391
1.1803778368E-05 3.5000000000E-02 : mesh 3,
type,size,rad_step\[,log_step\]

> <div>
>
> 2.3000000000 : r_cut(SPH)
>
> </div>

2 0.

Another format:

C (US d-loc) - PAW data extracted from US-psp (D.Vanderbilt) - generated by USpp2Abinit v2.3.0  
> <div>
>
> > <div>
> >
> > 6.000 4.000 20090106 : zatom,zion,pspdat
> >
> > </div>
>
> 7 11 1 0 560 0. : pspcod,pspxc,lmax,lloc,mmax,r2well
>
> </div>

paw4 2230<span class="classifier">pspfmt,creatorID</span>  
4 8 : basis_size,lmn_size

0 0 1 1 : orbitals 5 : number_of_meshes 1 2 560 1.5198032759E-04
1.6666666667E-02 : mesh 1, type,size,rad_step\[,log_step\] 2 2 556
1.5198032759E-04 1.6666666667E-02 : mesh 2,
type,size,rad_step\[,log_step\] 3 2 576 1.5198032759E-04
1.6666666667E-02 : mesh 3, type,size,rad_step\[,log_step\] 4 2 666
1.5198032759E-04 1.6666666667E-02 : mesh 4,
type,size,rad_step\[,log_step\] 5 2 673 1.5198032759E-04
1.6666666667E-02 : mesh 5, type,size,rad_step\[,log_step\]

> <div>
>
> 1.5550009124 : r_cut(PAW)
>
> </div>

3 0. : shape_type,rshape

Yet nnother one:

Paw atomic data for element Si - Generated by atompaw v3.0.1.3 & AtomPAW2Abinit v3.3.1  
> <div>
>
> 14.000 4.000 20120814 : zatom,zion,pspdat 7 11 1 0 663 0. :
> pspcod,pspxc,lmax,lloc,mmax,r2well
>
> </div>

paw5 1331<span class="classifier">pspfmt,creatorID</span>  
4 8 : basis_size,lmn_size

0 0 1 1 : orbitals 5 : number_of_meshes 1 2 663 8.2129718540404674E-04
1.1498160595656655E-02 : mesh 1, type,size,rad_step\[,log_step\] 2 2 658
8.2129718540404674E-04 1.1498160595656655E-02 : mesh 2,
type,size,rad_step\[,log_step\] 3 2 740 8.2129718540404674E-04
1.1498160595656655E-02 : mesh 3, type,size,rad_step\[,log_step\] 4 2 819
8.2129718540404674E-04 1.1498160595656655E-02 : mesh 4,
type,size,rad_step\[,log_step\] 5 2 870 8.2129718540404674E-04
1.1498160595656655E-02 : mesh 5, type,size,rad_step\[,log_step\]

> <div>
>
> 1.5669671236 : r_cut(PAW)
>
> </div>

2 0. : shape_type,rshape

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">PawAbinitPseudo</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">path</span></span>*, *<span class="n"><span class="pre">header</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L535-L546"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PawAbinitPseudo" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.abinit.pseudos.PawPseudo"
class="reference internal"
title="pymatgen.io.abinit.pseudos.PawPseudo"><span class="pre"><code
class="sourceCode python">PawPseudo</code></span></a>,
<a href="#pymatgen.io.abinit.pseudos.AbinitPseudo"
class="reference internal"
title="pymatgen.io.abinit.pseudos.AbinitPseudo"><span class="pre"><code
class="sourceCode python">AbinitPseudo</code></span></a>

Paw pseudopotential in the Abinit format.

Parameters<span class="colon">:</span>  
- **path** – Filename.

- **header** – AbinitHeader instance.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">paw_radius</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PawAbinitPseudo.paw_radius"
class="headerlink" title="Link to this definition"></a>  
Radius of the PAW sphere in a.u.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">supports_soc</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PawAbinitPseudo.supports_soc"
class="headerlink" title="Link to this definition"></a>  
True if the pseudo can be used in a calculation with spin-orbit
coupling. Base classes should provide a concrete implementation that
computes this value.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">PawPseudo</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L415-L442"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PawPseudo" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`ABC`</span>

Abstract class that defines the methods that must be implemented by the
concrete classes representing PAW pseudopotentials.

*<span class="k"><span class="pre">abstract</span></span><span class="w"> </span><span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">paw_radius</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PawPseudo.paw_radius"
class="headerlink" title="Link to this definition"></a>  
Radius of the PAW sphere in a.u.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">rcore</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PawPseudo.rcore" class="headerlink"
title="Link to this definition"></a>  
Alias of paw_radius.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">PawXmlSetup</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filepath</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L1169-L1505"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PawXmlSetup" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.abinit.pseudos.Pseudo" class="reference internal"
title="pymatgen.io.abinit.pseudos.Pseudo"><span class="pre"><code
class="sourceCode python">Pseudo</code></span></a>,
<a href="#pymatgen.io.abinit.pseudos.PawPseudo"
class="reference internal"
title="pymatgen.io.abinit.pseudos.PawPseudo"><span class="pre"><code
class="sourceCode python">PawPseudo</code></span></a>

Setup class for PawXml.

Parameters<span class="colon">:</span>  
**filepath** (*str*) – Path to the XML file.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Z</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.Z" class="headerlink"
title="Link to this definition"></a>  
The atomic number of the atom.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Z_val</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.Z_val"
class="headerlink" title="Link to this definition"></a>  
Number of valence electrons.

<span class="sig-name descname"><span class="pre">ae_core_density</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.ae_core_density"
class="headerlink" title="Link to this definition"></a>  
The all-electron radial density.

<span class="sig-name descname"><span class="pre">ae_partial_waves</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.ae_partial_waves"
class="headerlink" title="Link to this definition"></a>  
Dictionary with the AE partial waves indexed by state.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">l_local</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.l_local"
class="headerlink" title="Link to this definition"></a>  
Angular momentum used for the local part.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">l_max</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.l_max"
class="headerlink" title="Link to this definition"></a>  
Maximum angular momentum.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">paw_radius</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.paw_radius"
class="headerlink" title="Link to this definition"></a>  
Radius of the PAW sphere in a.u.

<span class="sig-name descname"><span class="pre">plot_densities</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">ax</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">plt.Axes</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../util/plotting.py#L1387-L1411"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.plot_densities"
class="headerlink" title="Link to this definition"></a>  
Plot the PAW densities.

Parameters<span class="colon">:</span>  
**ax** – matplotlib Axes or None if a new figure should be created.

Returns<span class="colon">:</span>  
matplotlib figure

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

<span class="sig-name descname"><span class="pre">plot_projectors</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">ax</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">plt.Axes</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">fontsize</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">12</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../util/plotting.py#L1444-L1468"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.plot_projectors"
class="headerlink" title="Link to this definition"></a>  
Plot the PAW projectors.

Parameters<span class="colon">:</span>  
**ax** – matplotlib Axes or None if a new figure should be created.

Returns<span class="colon">:</span>  
matplotlib figure

Return type<span class="colon">:</span>  
plt.Figure

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

<span class="sig-name descname"><span class="pre">plot_waves</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">ax</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">plt.Axes</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">fontsize</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">12</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../util/plotting.py#L1413-L1442"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.plot_waves"
class="headerlink" title="Link to this definition"></a>  
Plot the AE and the pseudo partial waves.

Parameters<span class="colon">:</span>  
- **ax** – matplotlib Axes or None if a new figure should be created.

- **fontsize** – fontsize for legends and titles

Returns<span class="colon">:</span>  
matplotlib figure

Return type<span class="colon">:</span>  
plt.Figure

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

<span class="sig-name descname"><span class="pre">projector_functions</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.projector_functions"
class="headerlink" title="Link to this definition"></a>  
Dictionary with the PAW projectors indexed by state.

<span class="sig-name descname"><span class="pre">pseudo_core_density</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.pseudo_core_density"
class="headerlink" title="Link to this definition"></a>  
The pseudized radial density.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">pseudo_partial_waves</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.pseudo_partial_waves"
class="headerlink" title="Link to this definition"></a>  
Dictionary with the pseudo partial waves indexed by state.

<span class="sig-name descname"><span class="pre">root</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.root"
class="headerlink" title="Link to this definition"></a>  
Root tree of XML.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">summary</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.summary"
class="headerlink" title="Link to this definition"></a>  
String summarizing the most important properties.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">supports_soc</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.supports_soc"
class="headerlink" title="Link to this definition"></a>  
Here I assume that the ab-initio code can treat the SOC within the
on-site approximation.

<span class="sig-name descname"><span class="pre">yield_figs</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L1380-L1385"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PawXmlSetup.yield_figs"
class="headerlink" title="Link to this definition"></a>  
This function *generates* a predefined list of matplotlib figures with
minimal input from the user.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Pseudo</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L88-L384"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Pseudo" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>, <span
class="pre">`ABC`</span>

Abstract base class defining the methods that must be implemented by the
concrete pseudo-potential sub-classes.

*<span class="k"><span class="pre">abstract</span></span><span class="w"> </span><span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Z</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Pseudo.Z" class="headerlink"
title="Link to this definition"></a>  
The atomic number of the atom.

*<span class="k"><span class="pre">abstract</span></span><span class="w"> </span><span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Z_val</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Pseudo.Z_val" class="headerlink"
title="Link to this definition"></a>  
Valence charge.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L241-L255"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Pseudo.as_dict" class="headerlink"
title="Link to this definition"></a>  
Return dictionary for MSONable protocol.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">as_pseudo</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">obj</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.abinit.pseudos.Pseudo" class="reference internal"
title="pymatgen.io.abinit.pseudos.Pseudo"><span
class="pre">Pseudo</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.abinit.pseudos.Pseudo" class="reference internal"
title="pymatgen.io.abinit.pseudos.Pseudo"><span
class="pre">Pseudo</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L94-L101"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Pseudo.as_pseudo"
class="headerlink" title="Link to this definition"></a>  
Convert obj into a Pseudo.

Parameters<span class="colon">:</span>  
**obj** (*str* *\|*
<a href="#pymatgen.io.abinit.pseudos.Pseudo" class="reference internal"
title="pymatgen.io.abinit.pseudos.Pseudo"><em>Pseudo</em></a>) – Path to
the pseudo file or a Pseudo object.

<span class="sig-name descname"><span class="pre">as_tmpfile</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tmpdir</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L270-L294"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Pseudo.as_tmpfile"
class="headerlink" title="Link to this definition"></a>  
Copy the pseudopotential to a temporary a file and returns a new
pseudopotential object. Useful for unit tests in which we have to change
the content of the file.

Parameters<span class="colon">:</span>  
**tmpdir** – If None, a new temporary directory is created and files are
copied here else tmpdir is used.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">basename</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Pseudo.basename" class="headerlink"
title="Link to this definition"></a>  
File basename.

<span class="sig-name descname"><span class="pre">compute_md5</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L223-L231"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Pseudo.compute_md5"
class="headerlink" title="Link to this definition"></a>  
Compute and return MD5 hash value.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">djrepo_path</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Pseudo.djrepo_path"
class="headerlink" title="Link to this definition"></a>  
The path of the djrepo file. None if file does not exist.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">element</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.periodic_table.Element"
class="reference internal"
title="pymatgen.core.periodic_table.Element"><span
class="pre">Element</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Pseudo.element" class="headerlink"
title="Link to this definition"></a>  
Pymatgen Element.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">filepath</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Pseudo.filepath" class="headerlink"
title="Link to this definition"></a>  
Absolute path to pseudopotential file.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L257-L268"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Pseudo.from_dict"
class="headerlink" title="Link to this definition"></a>  
Build instance from dictionary (MSONable protocol).

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L103-L110"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Pseudo.from_file"
class="headerlink" title="Link to this definition"></a>  
Build an instance of a concrete Pseudo subclass from filename. Note: the
parser knows the concrete class that should be instantiated Client code
should rely on the abstract interface provided by Pseudo.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">has_dojo_report</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Pseudo.has_dojo_report"
class="headerlink" title="Link to this definition"></a>  
True if the pseudo has an associated DOJO_REPORT section.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">has_hints</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Pseudo.has_hints"
class="headerlink" title="Link to this definition"></a>  
True if self provides hints on the cutoff energy.

<span class="sig-name descname"><span class="pre">hint_for_accuracy</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">accuracy</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'normal'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L309-L325"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Pseudo.hint_for_accuracy"
class="headerlink" title="Link to this definition"></a>  
Get a Hint object with the suggested value of ecut \[Ha\] and pawecutdg
\[Ha\] for the given accuracy. ecut and pawecutdg are set to zero if no
hint is available.

Parameters<span class="colon">:</span>  
**accuracy** – \[“low”, “normal”, “high”\]

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">isnc</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Pseudo.isnc" class="headerlink"
title="Link to this definition"></a>  
True if norm-conserving pseudopotential.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ispaw</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Pseudo.ispaw" class="headerlink"
title="Link to this definition"></a>  
True if PAW pseudopotential.

*<span class="k"><span class="pre">abstract</span></span><span class="w"> </span><span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">l_local</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Pseudo.l_local" class="headerlink"
title="Link to this definition"></a>  
Angular momentum used for the local part.

*<span class="k"><span class="pre">abstract</span></span><span class="w"> </span><span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">l_max</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Pseudo.l_max" class="headerlink"
title="Link to this definition"></a>  
Maximum angular momentum.

<span class="sig-name descname"><span class="pre">md5</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Pseudo.md5" class="headerlink"
title="Link to this definition"></a>  
MD5 hash value.

<span class="sig-name descname"><span class="pre">open_pspsfile</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">ecut</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">20</span></span>*, *<span class="n"><span class="pre">pawecutdg</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L338-L384"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Pseudo.open_pspsfile"
class="headerlink" title="Link to this definition"></a>  
Calls Abinit to compute the internal tables for the application of the
pseudopotential part. Returns PspsFile object providing methods to plot
and analyze the data or None if file is not found or it’s not readable.

Parameters<span class="colon">:</span>  
- **ecut** – Cutoff energy in Hartree.

- **pawecutdg** – Cutoff energy for the PAW double grid.

*<span class="k"><span class="pre">abstract</span></span><span class="w"> </span><span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">summary</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Pseudo.summary" class="headerlink"
title="Link to this definition"></a>  
String summarizing the most important properties.

*<span class="k"><span class="pre">abstract</span></span><span class="w"> </span><span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">supports_soc</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Pseudo.supports_soc"
class="headerlink" title="Link to this definition"></a>  
True if the pseudo can be used in a calculation with spin-orbit
coupling. Base classes should provide a concrete implementation that
computes this value.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">symbol</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Pseudo.symbol" class="headerlink"
title="Link to this definition"></a>  
Element symbol.

<span class="sig-name descname"><span class="pre">to_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">verbose</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L131-L152"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Pseudo.to_str" class="headerlink"
title="Link to this definition"></a>  
String representation.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.Pseudo.type" class="headerlink"
title="Link to this definition"></a>  
Type of pseudo.

<!-- -->

*<span class="k"><span class="pre">exception</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">PseudoParseError</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L979-L980"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoParseError"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="pymatgen.io.html#pymatgen.io.core.ParseError"
class="reference internal" title="pymatgen.io.core.ParseError"><span
class="pre"><code class="sourceCode python">ParseError</code></span></a>

Base Error class for the exceptions raised by PseudoParser.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">PseudoParser</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L983-L1156"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoParser" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Responsible for parsing pseudopotential files and returning
pseudopotential objects.

Usage:  
pseudo = PseudoParser().parse(“filename”)

<span class="sig-name descname"><span class="pre">Error</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L979-L980"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoParser.Error"
class="headerlink" title="Link to this definition"></a>  
alias of <a href="#pymatgen.io.abinit.pseudos.PseudoParseError"
class="reference internal"
title="pymatgen.io.abinit.pseudos.PseudoParseError"><span
class="pre"><code
class="sourceCode python">PseudoParseError</code></span></a>

<span class="sig-name descname"><span class="pre">parse</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L1110-L1156"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoParser.parse"
class="headerlink" title="Link to this definition"></a>  
Read and parse a pseudopotential file. Main entry point for client code.

Returns<span class="colon">:</span>  
pseudopotential object or None if filename is not a valid
pseudopotential file.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ppdesc</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">pspcod</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">psp_type</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">format</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L993-L999"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoParser.ppdesc"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`NamedTuple`</span>

Supported values of pspcod.

Create new instance of ppdesc(pspcod, name, psp_type, format)

<span class="sig-name descname"><span class="pre">format</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoParser.ppdesc.format"
class="headerlink" title="Link to this definition"></a>  
Alias for field number 3

<span class="sig-name descname"><span class="pre">name</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoParser.ppdesc.name"
class="headerlink" title="Link to this definition"></a>  
Alias for field number 1

<span class="sig-name descname"><span class="pre">psp_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoParser.ppdesc.psp_type"
class="headerlink" title="Link to this definition"></a>  
Alias for field number 2

<span class="sig-name descname"><span class="pre">pspcod</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoParser.ppdesc.pspcod"
class="headerlink" title="Link to this definition"></a>  
Alias for field number 0

<span class="sig-name descname"><span class="pre">read_ppdesc</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L1068-L1108"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoParser.read_ppdesc"
class="headerlink" title="Link to this definition"></a>  
Read the pseudopotential descriptor from filename.

Returns<span class="colon">:</span>  
Pseudopotential descriptor. None if filename is not a valid
pseudopotential file.

Raises<span class="colon">:</span>  
<a href="#pymatgen.io.abinit.pseudos.PseudoParseError"
class="reference internal"
title="pymatgen.io.abinit.pseudos.PseudoParseError"><strong>PseudoParseError</strong></a>
–

<span class="sig-name descname"><span class="pre">scan_directory</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dirname</span></span>*, *<span class="n"><span class="pre">exclude_exts</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">()</span></span>*, *<span class="n"><span class="pre">exclude_fnames</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">()</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L1027-L1066"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoParser.scan_directory"
class="headerlink" title="Link to this definition"></a>  
Analyze the files contained in directory dirname.

Parameters<span class="colon">:</span>  
- **dirname** – directory path

- **exclude_exts** – list of file extensions that should be skipped.

- **exclude_fnames** – list of file names that should be skipped.

Returns<span class="colon">:</span>  
List of pseudopotential objects.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">PseudoTable</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">pseudos</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.io.abinit.pseudos.Pseudo" class="reference internal"
title="pymatgen.io.abinit.pseudos.Pseudo"><span
class="pre">Pseudo</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L1508-L1842"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoTable" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`Sequence`</span>, <span
class="pre">`MSONable`</span>

Define the pseudopotentials from the element table. Individidual
elements are accessed by name, symbol or atomic number.

For example, the following all retrieve iron: - elements\[26\] -
elements.Fe - elements.symbol(‘Fe’) - elements.name(‘iron’) -
elements.isotope(‘Fe’)

Parameters<span class="colon">:</span>  
**pseudos** – List of pseudopotentials or filepaths.

<span class="sig-name descname"><span class="pre">all_combinations_for_elements</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">element_symbols</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L1673-L1687"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.abinit.pseudos.PseudoTable.all_combinations_for_elements"
class="headerlink" title="Link to this definition"></a>  
Get a list with all the possible combination of pseudos for the given
list of element_symbols. Each item is a list of pseudopotential objects.

Example

table.all_combinations_for_elements(\[“Li”, “F”\])

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">allnc</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoTable.allnc"
class="headerlink" title="Link to this definition"></a>  
True if all pseudos are norm-conserving.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">allpaw</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoTable.allpaw"
class="headerlink" title="Link to this definition"></a>  
True if all pseudos are PAW.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L1645-L1658"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoTable.as_dict"
class="headerlink" title="Link to this definition"></a>  
Return dictionary for MSONable protocol.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">as_table</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">items</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L1521-L1524"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoTable.as_table"
class="headerlink" title="Link to this definition"></a>  
Return an instance of PseudoTable from the iterable items.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L1660-L1667"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoTable.from_dict"
class="headerlink" title="Link to this definition"></a>  
Build instance from dictionary (MSONable protocol).

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dir</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">top</span></span>*, *<span class="n"><span class="pre">exts</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">exclude_dirs</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'\_\*'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L1526-L1566"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoTable.from_dir"
class="headerlink" title="Link to this definition"></a>  
Find all pseudos in the directory tree starting from top.

Parameters<span class="colon">:</span>  
- **top** – Top of the directory tree

- **exts** – List of files extensions. if exts == “all_files” we try to
  open all files in top

- **exclude_dirs** – Wildcard used to exclude directories.

Returns<span class="colon">:</span>  
PseudoTable sorted by atomic number Z.

<span class="sig-name descname"><span class="pre">get_pseudos_for_structure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L1756-L1766"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.abinit.pseudos.PseudoTable.get_pseudos_for_structure"
class="headerlink" title="Link to this definition"></a>  
Get the list of Pseudo objects to be used for this Structure.

Parameters<span class="colon">:</span>  
**structure** – pymatgen Structure.

Raises<span class="colon">:</span>  
- **ValueError** –

- **multiple occurrences are present in the table.** –

<span class="sig-name descname"><span class="pre">is_complete</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">zmax</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">118</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L1669-L1671"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoTable.is_complete"
class="headerlink" title="Link to this definition"></a>  
True if table is complete i.e. all elements with Z \< zmax have at least
on pseudopotential.

<span class="sig-name descname"><span class="pre">print_table</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">stream=\<\_io.TextIOWrapper</span> <span class="pre">name='\<stdout\>'</span> <span class="pre">mode='w'</span> <span class="pre">encoding='utf-8'\></span></span>*, *<span class="n"><span class="pre">filter_function=None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L1768-L1779"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoTable.print_table"
class="headerlink" title="Link to this definition"></a>  
A pretty ASCII printer for the periodic table, based on some
filter_function.

Parameters<span class="colon">:</span>  
- **stream** – file-like object

- **filter_function** – A filtering function that take a Pseudo as input
  and returns a boolean. For example, setting filter_function = lambda
  p: p.Z_val \> 2 will print a periodic table containing only pseudos
  with Z_val \> 2.

<span class="sig-name descname"><span class="pre">pseudo_with_symbol</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">symbol</span></span>*, *<span class="n"><span class="pre">allow_multi</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L1689-L1704"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoTable.pseudo_with_symbol"
class="headerlink" title="Link to this definition"></a>  
Get the pseudo with the given chemical symbol.

Parameters<span class="colon">:</span>  
- **symbols** – String with the chemical symbol of the element

- **allow_multi** – By default, the method raises ValueError if multiple
  occurrences are found. Use allow_multi to prevent this.

Raises<span class="colon">:</span>  
**ValueError if symbol is not found** **or** **multiple occurrences are
present and not allow_multi** –

<span class="sig-name descname"><span class="pre">pseudos_with_symbols</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">symbols</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L1706-L1721"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoTable.pseudos_with_symbols"
class="headerlink" title="Link to this definition"></a>  
Get the pseudos with the given chemical symbols.

Raises<span class="colon">:</span>  
**ValueError if one** **of** **the symbols is not found** **or**
**multiple occurrences are present.** –

<span class="sig-name descname"><span class="pre">select</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">condition</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.abinit.pseudos.PseudoTable"
class="reference internal"
title="pymatgen.io.abinit.pseudos.PseudoTable"><span
class="pre">PseudoTable</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L1815-L1825"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoTable.select"
class="headerlink" title="Link to this definition"></a>  
Select only those pseudopotentials for which condition is True.

Parameters<span class="colon">:</span>  
**condition** – Function that accepts a Pseudo object and returns True
or False.

Returns<span class="colon">:</span>  
New PseudoTable instance with pseudos for which condition is True.

Return type<span class="colon">:</span>  
<a href="#pymatgen.io.abinit.pseudos.PseudoTable"
class="reference internal"
title="pymatgen.io.abinit.pseudos.PseudoTable">PseudoTable</a>

<span class="sig-name descname"><span class="pre">select_family</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">family</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L1839-L1842"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoTable.select_family"
class="headerlink" title="Link to this definition"></a>  
Return PseudoTable with element belonging to the specified family, e.g.
family=”alkaline”.

<span class="sig-name descname"><span class="pre">select_rows</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">rows</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L1831-L1837"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoTable.select_rows"
class="headerlink" title="Link to this definition"></a>  
Get new class:PseudoTable object with pseudos in the given rows of the
periodic table. rows can be either a int or a list of integers.

<span class="sig-name descname"><span class="pre">select_symbols</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">symbols</span></span>*, *<span class="n"><span class="pre">ret_list</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L1723-L1754"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoTable.select_symbols"
class="headerlink" title="Link to this definition"></a>  
Get a PseudoTable with the pseudopotentials with the given list of
chemical symbols.

Parameters<span class="colon">:</span>  
- **symbols** – str or list of symbols Prepend the symbol string with
  “-”, to exclude pseudos.

- **ret_list** – if True a list of pseudos is returned instead of a
  PseudoTable

<span class="sig-name descname"><span class="pre">sort_by_z</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L1811-L1813"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoTable.sort_by_z"
class="headerlink" title="Link to this definition"></a>  
Return a new PseudoTable with pseudos sorted by Z.

<span class="sig-name descname"><span class="pre">sorted</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attrname</span></span>*, *<span class="n"><span class="pre">reverse</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L1794-L1809"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoTable.sorted"
class="headerlink" title="Link to this definition"></a>  
Sort the table according to the value of attribute attrname.

Returns<span class="colon">:</span>  
PseudoTable object

Return type<span class="colon">:</span>  
New class

<span class="sig-name descname"><span class="pre">to_table</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filter_function</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L1781-L1792"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoTable.to_table"
class="headerlink" title="Link to this definition"></a>  
Return string with data in tabular form.

<span class="sig-name descname"><span class="pre">with_dojo_report</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L1827-L1829"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoTable.with_dojo_report"
class="headerlink" title="Link to this definition"></a>  
Select pseudos containing the DOJO_REPORT section. Return new
class:PseudoTable object.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">zlist</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.PseudoTable.zlist"
class="headerlink" title="Link to this definition"></a>  
Ordered list with the atomic numbers available in the table.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">RadialFunction</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">mesh</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span></span>*, *<span class="n"><span class="pre">values</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">NDArray</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L1159-L1166"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.RadialFunction" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`NamedTuple`</span>

Radial Function class.

TODO: use RadialFunction from pseudo_dojo.

Create new instance of RadialFunction(mesh, values)

<span class="sig-name descname"><span class="pre">mesh</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Any</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.RadialFunction.mesh"
class="headerlink" title="Link to this definition"></a>  
Alias for field number 0

<span class="sig-name descname"><span class="pre">values</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">NDArray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/pseudos.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.RadialFunction.values"
class="headerlink" title="Link to this definition"></a>  
Alias for field number 1

<!-- -->

<span class="sig-name descname"><span class="pre">l2str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">l_ang_mom</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L75-L80"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.l2str" class="headerlink"
title="Link to this definition"></a>  
Convert the angular momentum l (int) to string.

<!-- -->

<span class="sig-name descname"><span class="pre">str2l</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">s</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/pseudos.py#L83-L85"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.pseudos.str2l" class="headerlink"
title="Link to this definition"></a>  
Convert a string to the angular momentum l (int).

</div>

<div id="module-pymatgen.io.abinit.variable" class="section">

<span id="pymatgen-io-abinit-variable-module"></span>

## pymatgen.io.abinit.variable module<a href="#module-pymatgen.io.abinit.variable" class="headerlink"
title="Link to this heading"></a>

Support for Abinit input variables.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">InputVariable</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span>*, *<span class="n"><span class="pre">units</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">''</span></span>*, *<span class="n"><span class="pre">valperline</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">3</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/variable.py#L23-L199"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.variable.InputVariable" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

An Abinit input variable.

Parameters<span class="colon">:</span>  
- **name** – Name of the variable.

- **value** – Value of the variable.

- **units** – String specifying one of the units supported by Abinit.
  Default: atomic units.

- **valperline** – Number of items printed per line.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">basename</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/variable.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.variable.InputVariable.basename"
class="headerlink" title="Link to this definition"></a>  
The name trimmed of any dataset index.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">dataset</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/variable.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.variable.InputVariable.dataset"
class="headerlink" title="Link to this definition"></a>  
The dataset index in string form.

<span class="sig-name descname"><span class="pre">format_list</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">values</span></span>*, *<span class="n"><span class="pre">float_decimal</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/variable.py#L183-L199"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.variable.InputVariable.format_list"
class="headerlink" title="Link to this definition"></a>  
Format a list of values into a string. The result might be spread among
several lines.

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">format_list2d</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">values</span></span>*, *<span class="n"><span class="pre">float_decimal</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/variable.py#L143-L181"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.variable.InputVariable.format_list2d"
class="headerlink" title="Link to this definition"></a>  
Format a list of lists.

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">format_scalar</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">float_decimal</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/variable.py#L115-L141"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.variable.InputVariable.format_scalar"
class="headerlink" title="Link to this definition"></a>  
Format a single numerical value into a string with the appropriate
number of decimal.

<span class="sig-name descname"><span class="pre">get_value</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/variable.py#L46-L50"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.variable.InputVariable.get_value"
class="headerlink" title="Link to this definition"></a>  
Return the value.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">name</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/variable.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.variable.InputVariable.name"
class="headerlink" title="Link to this definition"></a>  
Name of the variable.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">units</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/abinit/variable.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.variable.InputVariable.units"
class="headerlink" title="Link to this definition"></a>  
The units.

<!-- -->

<span class="sig-name descname"><span class="pre">flatten</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">iterable</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/abinit/variable.py#L202-L218"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.abinit.variable.flatten" class="headerlink"
title="Link to this definition"></a>  
Make an iterable flat, i.e. a 1d iterable object.

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
