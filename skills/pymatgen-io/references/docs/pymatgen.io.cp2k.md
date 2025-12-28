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

- <a href="#" class="reference internal">pymatgen.io.cp2k package</a>
  - <a href="#submodules" class="reference internal">Submodules</a>
  - <a href="#module-pymatgen.io.cp2k.inputs"
    class="reference internal">pymatgen.io.cp2k.inputs module</a>
    - <a href="#pymatgen.io.cp2k.inputs.AtomicMetadata"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">AtomicMetadata</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.AtomicMetadata.info"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AtomicMetadata.info</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.AtomicMetadata.element"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AtomicMetadata.element</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.AtomicMetadata.potential"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AtomicMetadata.potential</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.AtomicMetadata.name"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AtomicMetadata.name</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.AtomicMetadata.alias_names"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AtomicMetadata.alias_names</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.AtomicMetadata.filename"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AtomicMetadata.filename</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.AtomicMetadata.version"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AtomicMetadata.version</code></span></a>
      - <a href="#id0" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AtomicMetadata.alias_names</code></span></a>
      - <a href="#id1" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AtomicMetadata.element</code></span></a>
      - <a href="#id2" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AtomicMetadata.filename</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.AtomicMetadata.get_hash"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AtomicMetadata.get_hash()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.AtomicMetadata.get_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AtomicMetadata.get_str()</code></span></a>
      - <a href="#id3" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AtomicMetadata.info</code></span></a>
      - <a href="#id4" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AtomicMetadata.name</code></span></a>
      - <a href="#id5" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AtomicMetadata.potential</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.AtomicMetadata.softmatch"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AtomicMetadata.softmatch()</code></span></a>
      - <a href="#id6" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AtomicMetadata.version</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.BandStructure"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">BandStructure</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.BandStructure.from_kpoints"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BandStructure.from_kpoints()</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.Band_Structure"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Band_Structure</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.BasisFile"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">BasisFile</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.BasisFile.from_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasisFile.from_str()</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.BasisInfo"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">BasisInfo</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.BasisInfo.electrons"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasisInfo.electrons</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.BasisInfo.core"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasisInfo.core</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.BasisInfo.valence"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasisInfo.valence</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.BasisInfo.polarization"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasisInfo.polarization</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.BasisInfo.diffuse"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasisInfo.diffuse</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.BasisInfo.cc"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasisInfo.cc</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.BasisInfo.pc"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasisInfo.pc</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.BasisInfo.sr"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasisInfo.sr</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.BasisInfo.molopt"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasisInfo.molopt</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.BasisInfo.admm"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasisInfo.admm</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.BasisInfo.lri"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasisInfo.lri</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.BasisInfo.contracted"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasisInfo.contracted</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.BasisInfo.xc"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasisInfo.xc</code></span></a>
      - <a href="#id7" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasisInfo.admm</code></span></a>
      - <a href="#id8" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasisInfo.cc</code></span></a>
      - <a href="#id9" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasisInfo.contracted</code></span></a>
      - <a href="#id10" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasisInfo.core</code></span></a>
      - <a href="#id11" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasisInfo.diffuse</code></span></a>
      - <a href="#id12" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasisInfo.electrons</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.BasisInfo.from_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasisInfo.from_str()</code></span></a>
      - <a href="#id13" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasisInfo.lri</code></span></a>
      - <a href="#id14" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasisInfo.molopt</code></span></a>
      - <a href="#id15" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasisInfo.pc</code></span></a>
      - <a href="#id16" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasisInfo.polarization</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.BasisInfo.softmatch"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasisInfo.softmatch()</code></span></a>
      - <a href="#id17" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasisInfo.sr</code></span></a>
      - <a href="#id18" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasisInfo.valence</code></span></a>
      - <a href="#id19" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BasisInfo.xc</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.BrokenSymmetry"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">BrokenSymmetry</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.BrokenSymmetry.from_el"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BrokenSymmetry.from_el()</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.Cell" class="reference internal"><span
      class="pre"><code
      class="docutils literal notranslate">Cell</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.Coord"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Coord</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.Cp2kInput"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Cp2kInput</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.Cp2kInput.from_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kInput.from_file()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.Cp2kInput.from_lines"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kInput.from_lines()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.Cp2kInput.from_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kInput.from_str()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.Cp2kInput.get_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kInput.get_str()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.Cp2kInput.write_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kInput.write_file()</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.DOS" class="reference internal"><span
      class="pre"><code
      class="docutils literal notranslate">DOS</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.DataFile"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">DataFile</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.DataFile.from_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DataFile.from_file()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.DataFile.from_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DataFile.from_str()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.DataFile.get_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DataFile.get_str()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.DataFile.objects"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DataFile.objects</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.DataFile.write_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DataFile.write_file()</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.Davidson"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Davidson</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.Dft" class="reference internal"><span
      class="pre"><code
      class="docutils literal notranslate">Dft</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.DftPlusU"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">DftPlusU</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.Diagonalization"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Diagonalization</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.EDensityCube"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">EDensityCube</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.E_Density_Cube"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">E_Density_Cube</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.ForceEval"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">ForceEval</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">GaussianTypeOrbitalBasisSet</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet.info"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GaussianTypeOrbitalBasisSet.info</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet.nset"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GaussianTypeOrbitalBasisSet.nset</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet.n"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GaussianTypeOrbitalBasisSet.n</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet.lmax"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GaussianTypeOrbitalBasisSet.lmax</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet.lmin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GaussianTypeOrbitalBasisSet.lmin</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet.nshell"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GaussianTypeOrbitalBasisSet.nshell</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet.exponents"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GaussianTypeOrbitalBasisSet.exponents</code></span></a>
      - <a
        href="#pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet.coefficients"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GaussianTypeOrbitalBasisSet.coefficients</code></span></a>
      - <a href="#id20" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GaussianTypeOrbitalBasisSet.coefficients</code></span></a>
      - <a href="#id21" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GaussianTypeOrbitalBasisSet.exponents</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet.from_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GaussianTypeOrbitalBasisSet.from_str()</code></span></a>
      - <a
        href="#pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet.get_keyword"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GaussianTypeOrbitalBasisSet.get_keyword()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet.get_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GaussianTypeOrbitalBasisSet.get_str()</code></span></a>
      - <a href="#id22" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GaussianTypeOrbitalBasisSet.info</code></span></a>
      - <a href="#id23" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GaussianTypeOrbitalBasisSet.lmax</code></span></a>
      - <a href="#id24" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GaussianTypeOrbitalBasisSet.lmin</code></span></a>
      - <a href="#id25" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GaussianTypeOrbitalBasisSet.n</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet.nexp"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GaussianTypeOrbitalBasisSet.nexp</code></span></a>
      - <a href="#id26" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GaussianTypeOrbitalBasisSet.nset</code></span></a>
      - <a href="#id27" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GaussianTypeOrbitalBasisSet.nshell</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.Global"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Global</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.GthPotential"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">GthPotential</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.GthPotential.info"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GthPotential.info</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.GthPotential.n_elecs"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GthPotential.n_elecs</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.GthPotential.r_loc"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GthPotential.r_loc</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.GthPotential.nexp_ppl"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GthPotential.nexp_ppl</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.GthPotential.c_exp_ppl"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GthPotential.c_exp_ppl</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.GthPotential.radii"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GthPotential.radii</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.GthPotential.nprj"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GthPotential.nprj</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.GthPotential.nprj_ppnl"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GthPotential.nprj_ppnl</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.GthPotential.hprj_ppnl"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GthPotential.hprj_ppnl</code></span></a>
      - <a href="#id28" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GthPotential.c_exp_ppl</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.GthPotential.from_section"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GthPotential.from_section()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.GthPotential.from_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GthPotential.from_str()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.GthPotential.get_keyword"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GthPotential.get_keyword()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.GthPotential.get_section"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GthPotential.get_section()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.GthPotential.get_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GthPotential.get_str()</code></span></a>
      - <a href="#id29" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GthPotential.hprj_ppnl</code></span></a>
      - <a href="#id30" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GthPotential.n_elecs</code></span></a>
      - <a href="#id31" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GthPotential.nexp_ppl</code></span></a>
      - <a href="#id32" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GthPotential.nprj</code></span></a>
      - <a href="#id33" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GthPotential.nprj_ppnl</code></span></a>
      - <a href="#id34" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GthPotential.r_loc</code></span></a>
      - <a href="#id35" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">GthPotential.radii</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.Keyword"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Keyword</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.Keyword.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Keyword.as_dict()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.Keyword.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Keyword.from_dict()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.Keyword.from_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Keyword.from_str()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.Keyword.get_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Keyword.get_str()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.Keyword.verbosity"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Keyword.verbosity()</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.KeywordList"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">KeywordList</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.KeywordList.append"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">KeywordList.append()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.KeywordList.extend"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">KeywordList.extend()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.KeywordList.get_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">KeywordList.get_str()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.KeywordList.verbosity"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">KeywordList.verbosity()</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.Kind" class="reference internal"><span
      class="pre"><code
      class="docutils literal notranslate">Kind</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.KpointSet"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">KpointSet</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.Kpoint_Set"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Kpoint_Set</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.Kpoints"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Kpoints</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.Kpoints.from_kpoints"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Kpoints.from_kpoints()</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.LDOS" class="reference internal"><span
      class="pre"><code
      class="docutils literal notranslate">LDOS</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.MOCubes"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">MOCubes</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.MO_Cubes"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">MO_Cubes</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.Mgrid"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Mgrid</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.OrbitalTransformation"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">OrbitalTransformation</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.PBE" class="reference internal"><span
      class="pre"><code
      class="docutils literal notranslate">PBE</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.PDOS" class="reference internal"><span
      class="pre"><code
      class="docutils literal notranslate">PDOS</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.PotentialFile"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">PotentialFile</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.PotentialFile.from_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PotentialFile.from_str()</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.PotentialInfo"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">PotentialInfo</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.PotentialInfo.electrons"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PotentialInfo.electrons</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.PotentialInfo.potential_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PotentialInfo.potential_type</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.PotentialInfo.nlcc"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PotentialInfo.nlcc</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.PotentialInfo.xc"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PotentialInfo.xc</code></span></a>
      - <a href="#id36" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PotentialInfo.electrons</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.PotentialInfo.from_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PotentialInfo.from_str()</code></span></a>
      - <a href="#id37" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PotentialInfo.nlcc</code></span></a>
      - <a href="#id38" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PotentialInfo.potential_type</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.PotentialInfo.softmatch"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PotentialInfo.softmatch()</code></span></a>
      - <a href="#id39" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">PotentialInfo.xc</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.QS" class="reference internal"><span
      class="pre"><code
      class="docutils literal notranslate">QS</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.Scf" class="reference internal"><span
      class="pre"><code
      class="docutils literal notranslate">Scf</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.Section"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Section</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.Section.add"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Section.add()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.Section.by_path"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Section.by_path()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.Section.check"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Section.check()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.Section.get"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Section.get()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.Section.get_keyword"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Section.get_keyword()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.Section.get_section"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Section.get_section()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.Section.get_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Section.get_str()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.Section.inc"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Section.inc()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.Section.insert"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Section.insert()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.Section.safeset"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Section.safeset()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.Section.set"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Section.set()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.Section.setitem"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Section.setitem()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.Section.silence"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Section.silence()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.Section.unset"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Section.unset()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.Section.update"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Section.update()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.Section.verbosity"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Section.verbosity()</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.SectionList"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">SectionList</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.SectionList.append"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SectionList.append()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.SectionList.extend"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SectionList.extend()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.SectionList.get"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SectionList.get()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.SectionList.get_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SectionList.get_str()</code></span></a>
      - <a href="#pymatgen.io.cp2k.inputs.SectionList.verbosity"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">SectionList.verbosity()</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.Smear"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Smear</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.Subsys"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Subsys</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.VHartreeCube"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">VHartreeCube</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.V_Hartree_Cube"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">V_Hartree_Cube</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.XCFunctional"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">XCFunctional</code></span></a>
    - <a href="#pymatgen.io.cp2k.inputs.Xc_Functional"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Xc_Functional</code></span></a>
  - <a href="#module-pymatgen.io.cp2k.outputs"
    class="reference internal">pymatgen.io.cp2k.outputs module</a>
    - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Cp2kOutput</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.as_dict()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.band_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.band_structure</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.calculation_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.calculation_type</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.charge"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.charge</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.complete_dos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.complete_dos</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.completed"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.completed</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.convergence"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.convergence()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.cp2k_version"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.cp2k_version</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.is_hubbard"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.is_hubbard</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.is_metal"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.is_metal</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.is_molecule"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.is_molecule</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.multiplicity"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.multiplicity</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.num_warnings"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.num_warnings</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_atomic_kind_info"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_atomic_kind_info()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_bandstructure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_bandstructure()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_cell_params"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_cell_params()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_chi_tensor"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_chi_tensor()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_cp2k_params"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_cp2k_params()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_dft_params"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_dft_params()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_dos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_dos()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_energies"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_energies()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_files"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_files()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_forces"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_forces()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_global_params"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_global_params()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_gtensor"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_gtensor()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_hirshfeld"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_hirshfeld()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_homo_lumo"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_homo_lumo()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_hyperfine"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_hyperfine()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_initial_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_initial_structure()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_input"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_input()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_ionic_steps"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_ionic_steps()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_mo_eigenvalues"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_mo_eigenvalues()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_mulliken"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_mulliken()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_nmr_shift"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_nmr_shift()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_opt_steps"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_opt_steps()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_overlap_condition"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_overlap_condition()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_plus_u_params"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_plus_u_params()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_qs_params"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_qs_params()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_raman"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_raman()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_scf_opt"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_scf_opt()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_scf_params"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_scf_params()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_stresses"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_stresses()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_structures"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_structures()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_tddfpt"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_tddfpt()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_timing"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_timing()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_total_numbers"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.parse_total_numbers()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.project_name"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.project_name</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.ran_successfully"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.ran_successfully()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.read_pattern"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.read_pattern()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.read_table_pattern"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.read_table_pattern()</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.run_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.run_type</code></span></a>
      - <a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.spin_polarized"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kOutput.spin_polarized</code></span></a>
    - <a href="#pymatgen.io.cp2k.outputs.parse_dos"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">parse_dos()</code></span></a>
    - <a href="#pymatgen.io.cp2k.outputs.parse_energy_file"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">parse_energy_file()</code></span></a>
    - <a href="#pymatgen.io.cp2k.outputs.parse_pdos"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">parse_pdos()</code></span></a>
  - <a href="#module-pymatgen.io.cp2k.sets"
    class="reference internal">pymatgen.io.cp2k.sets module</a>
    - <a href="#pymatgen.io.cp2k.sets.CellOptSet"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">CellOptSet</code></span></a>
    - <a href="#pymatgen.io.cp2k.sets.Cp2kValidationError"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">Cp2kValidationError</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.Cp2kValidationError.CP2K_VERSION"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">Cp2kValidationError.CP2K_VERSION</code></span></a>
    - <a href="#pymatgen.io.cp2k.sets.DftSet" class="reference internal"><span
      class="pre"><code
      class="docutils literal notranslate">DftSet</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.activate_epr"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.activate_epr()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.activate_fast_minimization"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.activate_fast_minimization()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.activate_hybrid"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.activate_hybrid()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.activate_hyperfine"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.activate_hyperfine()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.activate_localize"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.activate_localize()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.activate_motion"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.activate_motion()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.activate_nmr"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.activate_nmr()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.activate_nonperiodic"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.activate_nonperiodic()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.activate_polar"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.activate_polar()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.activate_robust_minimization"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.activate_robust_minimization()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.activate_spinspin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.activate_spinspin()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.activate_tddfpt"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.activate_tddfpt()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.activate_vdw_potential"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.activate_vdw_potential()</code></span></a>
      - <a
        href="#pymatgen.io.cp2k.sets.DftSet.activate_very_strict_minimization"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.activate_very_strict_minimization()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.create_subsys"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.create_subsys()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.get_basis_and_potential"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.get_basis_and_potential()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.get_cutoff_from_basis"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.get_cutoff_from_basis()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.get_xc_functionals"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.get_xc_functionals()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.modify_dft_print_iters"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.modify_dft_print_iters()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.print_bandstructure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.print_bandstructure()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.print_dos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.print_dos()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.print_e_density"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.print_e_density()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.print_forces"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.print_forces()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.print_hirshfeld"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.print_hirshfeld()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.print_ldos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.print_ldos()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.print_mo"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.print_mo()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.print_mo_cubes"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.print_mo_cubes()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.print_mulliken"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.print_mulliken()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.print_pdos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.print_pdos()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.print_v_hartree"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.print_v_hartree()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.set_charge"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.set_charge()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.validate"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.validate()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.write_basis_set_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.write_basis_set_file()</code></span></a>
      - <a href="#pymatgen.io.cp2k.sets.DftSet.write_potential_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DftSet.write_potential_file()</code></span></a>
    - <a href="#pymatgen.io.cp2k.sets.HybridCellOptSet"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">HybridCellOptSet</code></span></a>
    - <a href="#pymatgen.io.cp2k.sets.HybridRelaxSet"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">HybridRelaxSet</code></span></a>
    - <a href="#pymatgen.io.cp2k.sets.HybridStaticSet"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">HybridStaticSet</code></span></a>
    - <a href="#pymatgen.io.cp2k.sets.RelaxSet"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">RelaxSet</code></span></a>
    - <a href="#pymatgen.io.cp2k.sets.StaticSet"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">StaticSet</code></span></a>
  - <a href="#module-pymatgen.io.cp2k.utils"
    class="reference internal">pymatgen.io.cp2k.utils module</a>
    - <a href="#pymatgen.io.cp2k.utils.chunk" class="reference internal"><span
      class="pre"><code
      class="docutils literal notranslate">chunk()</code></span></a>
    - <a href="#pymatgen.io.cp2k.utils.get_truncated_coulomb_cutoff"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">get_truncated_coulomb_cutoff()</code></span></a>
    - <a href="#pymatgen.io.cp2k.utils.get_unique_site_indices"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">get_unique_site_indices()</code></span></a>
    - <a href="#pymatgen.io.cp2k.utils.natural_keys"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">natural_keys()</code></span></a>
    - <a href="#pymatgen.io.cp2k.utils.postprocessor"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">postprocessor()</code></span></a>
    - <a href="#pymatgen.io.cp2k.utils.preprocessor"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">preprocessor()</code></span></a>

</div>

</div>

</div>

<div class="section wy-nav-content-wrap" toggle="wy-nav-shift">

[pymatgen](index.html)

<div class="wy-nav-content">

<div class="rst-content style-external-links">

<div role="navigation" aria-label="Page navigation">

- <a href="index.html" class="icon icon-home" aria-label="Home"></a>
- pymatgen.io.cp2k package
- <a
  href="https://github.com/materialsproject/pymatgen/blob/master/docs_rst/pymatgen.io.cp2k.rst"
  class="fa fa-github">Edit on GitHub</a>

------------------------------------------------------------------------

</div>

<div class="document" role="main" itemscope="itemscope"
itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="module-pymatgen.io.cp2k" class="section">

<span id="pymatgen-io-cp2k-package"></span>

# pymatgen.io.cp2k package<a href="#module-pymatgen.io.cp2k" class="headerlink"
title="Link to this heading"></a>

Module for CP2K input/output parsing as well as sets for standard
calculations.

<div id="submodules" class="section">

## Submodules<a href="#submodules" class="headerlink"
title="Link to this heading"></a>

</div>

<div id="module-pymatgen.io.cp2k.inputs" class="section">

<span id="pymatgen-io-cp2k-inputs-module"></span>

## pymatgen.io.cp2k.inputs module<a href="#module-pymatgen.io.cp2k.inputs" class="headerlink"
title="Link to this heading"></a>

This module defines the building blocks of a CP2K input file. The CP2K
input structure is essentially a collection of “sections” which are
similar to dictionary objects that activate modules of the CP2K
executable, and then “keywords” which adjust variables inside of those
modules. For example, FORCE_EVAL section will activate CP2K’s ability to
calculate forces, and inside FORCE_EVAL, the Keyword “METHOD can be set
to “QS” to set the method of force evaluation to be the quickstep (DFT)
module.

A quick overview of the module:

– Section class defines the basis of CP2K input and contains methods for manipulating these  
objects similarly to Dicts.

– Keyword class defines the keywords used inside of Section objects that changes variables in  
CP2K programs.

– SectionList and KeywordList classes are lists of Section and Keyword objects that have  
the same dictionary key. This deals with repeated sections and keywords.

– Cp2kInput class is special instantiation of Section that is used to represent the full CP2K  
calculation input.

– The rest of the classes are children of Section intended to make initialization of common  
sections easier.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">AtomicMetadata</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">info:</span> <span class="pre">BasisInfo</span> <span class="pre">\|</span> <span class="pre">PotentialInfo</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">element:</span> <span class="pre">Element</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">potential:</span> <span class="pre">Literal\['All</span> <span class="pre">Electron'</span></span>*, *<span class="n"><span class="pre">'Pseudopotential'\]</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">name:</span> <span class="pre">str</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">alias_names:</span> <span class="pre">list</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">filename:</span> <span class="pre">str</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">version:</span> <span class="pre">str</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2285-L2340"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.AtomicMetadata" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Metadata for basis sets and potentials in CP2K.

<span class="sig-name descname"><span class="pre">info</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.AtomicMetadata.info"
class="headerlink" title="Link to this definition"></a>  
Info about this object

Type<span class="colon">:</span>  
<a href="#pymatgen.io.cp2k.inputs.BasisInfo" class="reference internal"
title="pymatgen.io.cp2k.inputs.BasisInfo">BasisInfo</a> \|
<a href="#pymatgen.io.cp2k.inputs.PotentialInfo"
class="reference internal"
title="pymatgen.io.cp2k.inputs.PotentialInfo">PotentialInfo</a> \| None

<span class="sig-name descname"><span class="pre">element</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.AtomicMetadata.element"
class="headerlink" title="Link to this definition"></a>  
Element for this object

Type<span class="colon">:</span>  
<a href="pymatgen.core.html#pymatgen.core.periodic_table.Element"
class="reference internal"
title="pymatgen.core.periodic_table.Element">Element</a> \| None

<span class="sig-name descname"><span class="pre">potential</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.AtomicMetadata.potential"
class="headerlink" title="Link to this definition"></a>  
The potential for this object

Type<span class="colon">:</span>  
Literal\[‘All Electron’, ‘Pseudopotential’\] \| None

<span class="sig-name descname"><span class="pre">name</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.AtomicMetadata.name"
class="headerlink" title="Link to this definition"></a>  
Name of the object

Type<span class="colon">:</span>  
str \| None

<span class="sig-name descname"><span class="pre">alias_names</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.AtomicMetadata.alias_names"
class="headerlink" title="Link to this definition"></a>  
Optional aliases

Type<span class="colon">:</span>  
list

<span class="sig-name descname"><span class="pre">filename</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.AtomicMetadata.filename"
class="headerlink" title="Link to this definition"></a>  
Name of the file containing this object

Type<span class="colon">:</span>  
str \| None

<span class="sig-name descname"><span class="pre">version</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.AtomicMetadata.version"
class="headerlink" title="Link to this definition"></a>  
Version

Type<span class="colon">:</span>  
str \| None

<span class="sig-name descname"><span class="pre">alias_names</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id0" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">element</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.periodic_table.Element"
class="reference internal"
title="pymatgen.core.periodic_table.Element"><span
class="pre">Element</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id1" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">filename</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id2" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">get_hash</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2330-L2336"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.AtomicMetadata.get_hash"
class="headerlink" title="Link to this definition"></a>  
Get a hash of this object.

<span class="sig-name descname"><span class="pre">get_str</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2338-L2340"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.AtomicMetadata.get_str"
class="headerlink" title="Link to this definition"></a>  
Get string representation.

<span class="sig-name descname"><span class="pre">info</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="#pymatgen.io.cp2k.inputs.BasisInfo" class="reference internal"
title="pymatgen.io.cp2k.inputs.BasisInfo"><span
class="pre">BasisInfo</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="#pymatgen.io.cp2k.inputs.PotentialInfo"
class="reference internal"
title="pymatgen.io.cp2k.inputs.PotentialInfo"><span
class="pre">PotentialInfo</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id3" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">name</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id4" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">potential</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'All</span> <span class="pre">Electron'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'Pseudopotential'</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id5" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">softmatch</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2308-L2328"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.AtomicMetadata.softmatch"
class="headerlink" title="Link to this definition"></a>  
Soft matching to see if a desired basis/potential matches requirements.

Does soft matching on the “info” attribute first. Then soft matches
against the element and name/aliases.

<span class="sig-name descname"><span class="pre">version</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id6" class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">BandStructure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">kpoint_sets</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.io.cp2k.inputs.KpointSet" class="reference internal"
title="pymatgen.io.cp2k.inputs.KpointSet"><span
class="pre">KpointSet</span></a><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'BAND.bs'</span></span>*, *<span class="n"><span class="pre">added_mos</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">-1</span></span>*, *<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">subsections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2091-L2166"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.BandStructure" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span class="pre"><code
class="sourceCode python">Section</code></span></a>

Specify high symmetry paths for outputting the band structure in CP2K.

Parameters<span class="colon">:</span>  
- **kpoint_sets** – Sequence of KpointSet objects for the band structure
  calculation.

- **filename** – Filename for the band structure output

- **added_mos** – Added (unoccupied) molecular orbitals for the
  calculation.

- **keywords** – additional keywords

- **subsections** – additional subsections.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_kpoints</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">kpoints</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">VaspKpoints</span></span>*, *<span class="n"><span class="pre">kpoints_line_density</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">20</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2125-L2166"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.BandStructure.from_kpoints"
class="headerlink" title="Link to this definition"></a>  
Initialize band structure section from a line-mode Kpoint object.

Parameters<span class="colon">:</span>  
- **kpoints** – a kpoint object from the vasp module, which was
  constructed in line mode

- **kpoints_line_density** – Number of kpoints along each path

TODO: kpoints objects are defined in the vasp module instead of a code
agnostic module if this changes in the future as other codes are added,
then this will need to change

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Band_Structure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">kpoint_sets</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.io.cp2k.inputs.KpointSet" class="reference internal"
title="pymatgen.io.cp2k.inputs.KpointSet"><span
class="pre">KpointSet</span></a><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'BAND.bs'</span></span>*, *<span class="n"><span class="pre">added_mos</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">-1</span></span>*, *<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">subsections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2169-L2171"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Band_Structure" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.cp2k.inputs.BandStructure"
class="reference internal"
title="pymatgen.io.cp2k.inputs.BandStructure"><span class="pre"><code
class="sourceCode python">BandStructure</code></span></a>

Parameters<span class="colon">:</span>  
- **kpoint_sets** – Sequence of KpointSet objects for the band structure
  calculation.

- **filename** – Filename for the band structure output

- **added_mos** – Added (unoccupied) molecular orbitals for the
  calculation.

- **keywords** – additional keywords

- **subsections** – additional subsections.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">BasisFile</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">objects</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2779-L2787"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.BasisFile" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.DataFile" class="reference internal"
title="pymatgen.io.cp2k.inputs.DataFile"><span class="pre"><code
class="sourceCode python">DataFile</code></span></a>

Data file for basis sets only.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">string</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2783-L2787"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.BasisFile.from_str" class="headerlink"
title="Link to this definition"></a>  
Initialize from a string representation.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">BasisInfo</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">electrons</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">core</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">valence</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">polarization</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">diffuse</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">cc</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">pc</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">sr</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">molopt</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">admm</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">lri</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">contracted</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">xc</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2174-L2282"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.BasisInfo" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Summary info about a basis set.

<span class="sig-name descname"><span class="pre">electrons</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.BasisInfo.electrons"
class="headerlink" title="Link to this definition"></a>  
Number of electrons

Type<span class="colon">:</span>  
int \| None

<span class="sig-name descname"><span class="pre">core</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.BasisInfo.core" class="headerlink"
title="Link to this definition"></a>  
Number of basis functions per core electron

Type<span class="colon">:</span>  
int \| None

<span class="sig-name descname"><span class="pre">valence</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.BasisInfo.valence" class="headerlink"
title="Link to this definition"></a>  
Number of basis functions per valence electron OR number of exp if it is
a FIT formatted admm basis

Type<span class="colon">:</span>  
int \| None

<span class="sig-name descname"><span class="pre">polarization</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.BasisInfo.polarization"
class="headerlink" title="Link to this definition"></a>  
Number of polarization functions

Type<span class="colon">:</span>  
int \| None

<span class="sig-name descname"><span class="pre">diffuse</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.BasisInfo.diffuse" class="headerlink"
title="Link to this definition"></a>  
Number of added, diffuse/augmentation functions

Type<span class="colon">:</span>  
int \| None

<span class="sig-name descname"><span class="pre">cc</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.BasisInfo.cc" class="headerlink"
title="Link to this definition"></a>  
Correlation consistent

Type<span class="colon">:</span>  
bool \| None

<span class="sig-name descname"><span class="pre">pc</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.BasisInfo.pc" class="headerlink"
title="Link to this definition"></a>  
Polarization consistent

Type<span class="colon">:</span>  
bool \| None

<span class="sig-name descname"><span class="pre">sr</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.BasisInfo.sr" class="headerlink"
title="Link to this definition"></a>  
Short-range optimized

Type<span class="colon">:</span>  
bool \| None

<span class="sig-name descname"><span class="pre">molopt</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.BasisInfo.molopt" class="headerlink"
title="Link to this definition"></a>  
Optimized for molecules/solids

Type<span class="colon">:</span>  
bool \| None

<span class="sig-name descname"><span class="pre">admm</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.BasisInfo.admm" class="headerlink"
title="Link to this definition"></a>  
Whether this is an auxiliary basis set for ADMM

Type<span class="colon">:</span>  
bool \| None

<span class="sig-name descname"><span class="pre">lri</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.BasisInfo.lri" class="headerlink"
title="Link to this definition"></a>  
Whether this is a local resolution of identity auxiliary basis

Type<span class="colon">:</span>  
bool \| None

<span class="sig-name descname"><span class="pre">contracted</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.BasisInfo.contracted"
class="headerlink" title="Link to this definition"></a>  
Whether this basis set is contracted

Type<span class="colon">:</span>  
bool \| None

<span class="sig-name descname"><span class="pre">xc</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.BasisInfo.xc" class="headerlink"
title="Link to this definition"></a>  
Exchange correlation functional used for creating this potential

Type<span class="colon">:</span>  
str \| None

<span class="sig-name descname"><span class="pre">admm</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">False</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id7" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">cc</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">False</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id8" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">contracted</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id9" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">core</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id10" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">diffuse</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id11" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">electrons</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id12" class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">string</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2221-L2282"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.BasisInfo.from_str" class="headerlink"
title="Link to this definition"></a>  
Get summary info from a string.

<span class="sig-name descname"><span class="pre">lri</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">False</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id13" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">molopt</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">False</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id14" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">pc</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">False</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id15" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">polarization</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id16" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">softmatch</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2210-L2219"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.BasisInfo.softmatch"
class="headerlink" title="Link to this definition"></a>  
Soft matching to see if two basis sets match.

Will only match those attributes which *are* defined for this basis info
object (one way checking)

<span class="sig-name descname"><span class="pre">sr</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">False</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id17" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">valence</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id18" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">xc</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id19" class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">BrokenSymmetry</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">l_alpha</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">(-1,)</span></span>*, *<span class="n"><span class="pre">n_alpha</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">(0,)</span></span>*, *<span class="n"><span class="pre">nel_alpha</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">(-1,)</span></span>*, *<span class="n"><span class="pre">l_beta</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">(-1,)</span></span>*, *<span class="n"><span class="pre">n_beta</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">(0,)</span></span>*, *<span class="n"><span class="pre">nel_beta</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">(-1,)</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L1694-L1823"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.BrokenSymmetry" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span class="pre"><code
class="sourceCode python">Section</code></span></a>

Define the required atomic orbital occupation assigned in initialization
of the density matrix, by adding or subtracting electrons from specific
angular momentum channels. It works only with GUESS ATOMIC.

Initialize the broken symmetry section.

Parameters<span class="colon">:</span>  
- **l_alpha** – Angular momentum quantum number of the orbitals whose
  occupation is changed

- **n_alpha** – Principal quantum number of the orbitals whose
  occupation is changed. Default is the first not occupied

- **nel_alpha** – Orbital occupation change per angular momentum quantum
  number. In unrestricted calculations applied to spin alpha

- **l_beta** – Same as L_alpha for beta channel

- **n_beta** – Same as N_alpha for beta channel

- **nel_beta** – Same as NEL_alpha for beta channel

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_el</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">el</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.periodic_table.Element"
class="reference internal"
title="pymatgen.core.periodic_table.Element"><span
class="pre">Element</span></a></span>*, *<span class="n"><span class="pre">oxi_state</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L1757-L1823"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.BrokenSymmetry.from_el"
class="headerlink" title="Link to this definition"></a>  
Create section from element, oxidation state, and spin.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Cell</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">lattice</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.lattice.Lattice"
class="reference internal" title="pymatgen.core.lattice.Lattice"><span
class="pre">Lattice</span></a></span>*, *<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L1263-L1282"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Cell" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span class="pre"><code
class="sourceCode python">Section</code></span></a>

Controls the cell/lattice parameters for the simulation.

Initialize the cell section.

Parameters<span class="colon">:</span>  
- **lattice** – pymatgen lattice object

- **keywords** – additional keywords

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Coord</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">aliases</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">subsections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L1426-L1469"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Coord" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span class="pre"><code
class="sourceCode python">Section</code></span></a>

Specify the coordinates of the atoms using a pymatgen structure object.

Parameters<span class="colon">:</span>  
- **structure** – Pymatgen structure object

- **alias** (*bool*) – whether or not to identify the sites by Element +
  number so you can do things like assign unique magnetization do
  different elements.

- **keywords** – additional keywords

- **subsections** – additional subsections.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Cp2kInput</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'CP2K_INPUT'</span></span>*, *<span class="n"><span class="pre">subsections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L649-L779"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Cp2kInput" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span class="pre"><code
class="sourceCode python">Section</code></span></a>

Special instance of ‘Section’ class that is meant to represent the
overall CP2K input. Distinguishes itself from Section by overriding
get_str() to not print this section’s title and by implementing the file
i/o.

Initialize Cp2kInput by calling the super.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L685-L690"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Cp2kInput.from_file"
class="headerlink" title="Link to this definition"></a>  
Initialize from a file.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_lines</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">lines</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L698-L703"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Cp2kInput.from_lines"
class="headerlink" title="Link to this definition"></a>  
Helper method to read lines of file.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">s</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L692-L696"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Cp2kInput.from_str" class="headerlink"
title="Link to this definition"></a>  
Initialize from a string.

<span class="sig-name descname"><span class="pre">get_str</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L671-L673"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Cp2kInput.get_str" class="headerlink"
title="Link to this definition"></a>  
Get string representation of the Cp2kInput.

<span class="sig-name descname"><span class="pre">write_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">input_filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'cp2k.inp'</span></span>*, *<span class="n"><span class="pre">output_dir</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'.'</span></span>*, *<span class="n"><span class="pre">make_dir_if_not_present</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L762-L779"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Cp2kInput.write_file"
class="headerlink" title="Link to this definition"></a>  
Write input to a file.

Parameters<span class="colon">:</span>  
- **input_filename** (*PathLike,* *optional*) – Defaults to “cp2k.inp”.

- **output_dir** (*PathLike,* *optional*) – Defaults to “.”.

- **make_dir_if_not_present** (*bool,* *optional*) – Defaults to True.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">DOS</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">ndigits</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">6</span></span>*, *<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">subsections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L1472-L1500"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.DOS" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span class="pre"><code
class="sourceCode python">Section</code></span></a>

Controls printing of the density of states.

Initialize the DOS section.

Parameters<span class="colon">:</span>  
- **ndigits** – how many digits of precision to print. As of 2022.1,
  this is necessary to not lose information.

- **keywords** – additional keywords

- **subsections** – additional subsections

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">DataFile</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">objects</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2745-L2776"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.DataFile" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

A data file for a CP2K calc.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2754-L2761"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.DataFile.from_file" class="headerlink"
title="Link to this definition"></a>  
Load from a file, reserved for child classes.

*<span class="k"><span class="pre">abstractmethod</span></span><span class="w"> </span><span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">string</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2763-L2767"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.DataFile.from_str" class="headerlink"
title="Link to this definition"></a>  
Initialize from a string.

<span class="sig-name descname"><span class="pre">get_str</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2774-L2776"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.DataFile.get_str" class="headerlink"
title="Link to this definition"></a>  
Get string representation.

<span class="sig-name descname"><span class="pre">objects</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.DataFile.objects" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">write_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2769-L2772"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.DataFile.write_file"
class="headerlink" title="Link to this definition"></a>  
Write to a file.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Davidson</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">new_prec_each</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">20</span></span>*, *<span class="n"><span class="pre">preconditioner</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'FULL_SINGLE_INVERSE'</span></span>*, *<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">subsections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L1122-L1167"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Davidson" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span class="pre"><code
class="sourceCode python">Section</code></span></a>

Parameters for davidson diagonalization.

Parameters<span class="colon">:</span>  
- **new_prec_each** (*int*) – How often to recalculate the
  preconditioner.

- **preconditioner** (*str*) –

  Preconditioner to use. “FULL_ALL”: Most effective state selective
  preconditioner based on diagonalization,

  > <div>
  >
  > requires the ENERGY_GAP parameter to be an underestimate of the
  > HOMO-LUMO gap. This preconditioner is recommended for almost all
  > systems, except very large systems where make_preconditioner would
  > dominate the total computational cost.
  >
  > </div>

  ”FULL_KINETIC”: Cholesky inversion of S and T, fast construction, robust, use for  
  very large systems.

  ”FULL_SINGLE”: Based on H-eS diagonalization, not as good as FULL_ALL, but  
  somewhat cheaper to apply.

  ”FULL_SINGLE_INVERSE”: Based on H-eS cholesky inversion, similar to FULL_SINGLE  
  in preconditioning efficiency but cheaper to construct, might be
  somewhat less robust. Recommended for large systems.

  ”FULL_S\_INVERSE”: Cholesky inversion of S, not as good as FULL_KINETIC,  
  yet equally expensive.

  ”NONE”: skip preconditioning

- **keywords** – additional keywords

- **subsections** – additional subsections.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Dft</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">basis_set_filenames</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">('BASIS_MOLOPT',)</span></span>*, *<span class="n"><span class="pre">potential_filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'GTH_POTENTIALS'</span></span>*, *<span class="n"><span class="pre">uks</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">wfn_restart_file_name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">subsections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L839-L887"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Dft" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span class="pre"><code
class="sourceCode python">Section</code></span></a>

Controls the DFT parameters in CP2K.

Initialize the DFT section.

Parameters<span class="colon">:</span>  
- **basis_set_filenames** – Name of the file that contains the basis set
  information. Defaults to “BASIS_MOLOPT”.

- **potential_filename** – Name of the file that contains the
  pseudopotential information. Defaults to “GTH_POTENTIALS”.

- **uks** – Whether to run unrestricted Kohn Sham (spin polarized).
  Defaults to True.

- **wfn_restart_file_name** – Defaults to None.

- **keywords** – additional keywords to add.

- **subsections** – Any subsections to initialize with. Defaults to
  None.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">DftPlusU</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">eps_u\_ramping</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1e-05</span></span>*, *<span class="n"><span class="pre">init_u\_ramping_each_scf</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">l</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">-1</span></span>*, *<span class="n"><span class="pre">u_minus_j</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">u_ramping</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">subsections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L1376-L1423"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.DftPlusU" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span class="pre"><code
class="sourceCode python">Section</code></span></a>

Controls DFT+U for an atom kind.

Initialize the DftPlusU section.

Parameters<span class="colon">:</span>  
- **eps_u\_ramping** – (float) SCF convergence threshold at which to
  start ramping the U value

- **init_u\_ramping_each_scf** – (bool) Whether or not to do u_ramping
  each scf cycle

- **l** – (int) angular moment of the orbital to apply the +U correction

- **u_minus_j** – (float) the effective U parameter, Ueff = U-J

- **u_ramping** – (float) stepwise amount to increase during ramping
  until u_minus_j is reached

- **keywords** – additional keywords

- **subsections** – additional subsections

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Diagonalization</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">eps_adapt</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">eps_iter</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-08</span></span>*, *<span class="n"><span class="pre">eps_jacobi</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">jacobi_threshold</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-07</span></span>*, *<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">subsections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L1084-L1119"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Diagonalization" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span class="pre"><code
class="sourceCode python">Section</code></span></a>

Controls diagonalization settings (if using traditional
diagonalization).

Initialize the diagonalization section.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">EDensityCube</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">subsections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L1640-L1655"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.EDensityCube" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span class="pre"><code
class="sourceCode python">Section</code></span></a>

Controls printing of the electron density cube file.

Basic object representing a CP2K Section. Sections activate different
parts of the calculation. For example, FORCE_EVAL section will activate
CP2K’s ability to calculate forces.

Parameters<span class="colon">:</span>  
- **name** – The name of the section (must match name in CP2K)

- **subsections** – A dictionary of subsections that are nested in this
  section. Format is {‘NAME’: Section(*args, \*\*kwargs). The name you
  chose for ‘NAME’ to index that subsection does not \*have* to be the
  same as the section’s true name, but we recommend matching them. You
  can specify a blank dictionary if there are no subsections, or if you
  want to insert the subsections later.

- **repeats** – Whether or not this section can be repeated. Most
  sections cannot. Default=False.

- **description** – Description of this section for easier readability

- **keywords** – the keywords to be set for this section. Each element
  should be a Keyword object. This can be more cumbersome than simply
  using kwargs for building a class in a script, but is more convenient
  for the class instantiations of CP2K sections (see below).

- **section_parameters** – the section parameters for this section.
  Section parameters are specialized keywords that modify the behavior
  of the section overall. Most sections do not have section parameters,
  but some do. Unlike normal Keywords, these are specified as strings
  and not as Keyword objects.

- **location** – the path to the section in the form
  ‘SECTION/SUBSECTION1/SUBSECTION3’, example for QS module:
  ‘FORCE_EVAL/DFT/QS’. This location is used to automatically determine
  if a subsection requires a supersection to be activated.

- **verbose** – Controls how much is printed to CP2K input files (Also
  see Keyword). If True, then a description of the section will be
  printed with it as a comment (if description is set). Default=True.

- **alias** – An alias for this class to use in place of the name.

- **keyword** (*kwargs are interpreted as*)

- **as** (*value pairs and added to the keywords array*)

- **objects**
  (<a href="#pymatgen.io.cp2k.inputs.Keyword" class="reference internal"
  title="pymatgen.io.cp2k.inputs.Keyword"><em>Keyword</em></a>)

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">E_Density_Cube</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">subsections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L1658-L1660"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.E_Density_Cube" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.cp2k.inputs.EDensityCube"
class="reference internal"
title="pymatgen.io.cp2k.inputs.EDensityCube"><span class="pre"><code
class="sourceCode python">EDensityCube</code></span></a>

Basic object representing a CP2K Section. Sections activate different
parts of the calculation. For example, FORCE_EVAL section will activate
CP2K’s ability to calculate forces.

Parameters<span class="colon">:</span>  
- **name** – The name of the section (must match name in CP2K)

- **subsections** – A dictionary of subsections that are nested in this
  section. Format is {‘NAME’: Section(*args, \*\*kwargs). The name you
  chose for ‘NAME’ to index that subsection does not \*have* to be the
  same as the section’s true name, but we recommend matching them. You
  can specify a blank dictionary if there are no subsections, or if you
  want to insert the subsections later.

- **repeats** – Whether or not this section can be repeated. Most
  sections cannot. Default=False.

- **description** – Description of this section for easier readability

- **keywords** – the keywords to be set for this section. Each element
  should be a Keyword object. This can be more cumbersome than simply
  using kwargs for building a class in a script, but is more convenient
  for the class instantiations of CP2K sections (see below).

- **section_parameters** – the section parameters for this section.
  Section parameters are specialized keywords that modify the behavior
  of the section overall. Most sections do not have section parameters,
  but some do. Unlike normal Keywords, these are specified as strings
  and not as Keyword objects.

- **location** – the path to the section in the form
  ‘SECTION/SUBSECTION1/SUBSECTION3’, example for QS module:
  ‘FORCE_EVAL/DFT/QS’. This location is used to automatically determine
  if a subsection requires a supersection to be activated.

- **verbose** – Controls how much is printed to CP2K input files (Also
  see Keyword). If True, then a description of the section will be
  printed with it as a comment (if description is set). Default=True.

- **alias** – An alias for this class to use in place of the name.

- **keyword** (*kwargs are interpreted as*)

- **as** (*value pairs and added to the keywords array*)

- **objects**
  (<a href="#pymatgen.io.cp2k.inputs.Keyword" class="reference internal"
  title="pymatgen.io.cp2k.inputs.Keyword"><em>Keyword</em></a>)

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ForceEval</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">subsections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L818-L836"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.ForceEval" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span class="pre"><code
class="sourceCode python">Section</code></span></a>

Controls the calculation of energy and forces in CP2K.

Initialize the ForceEval section.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">GaussianTypeOrbitalBasisSet</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">info:</span> <span class="pre">BasisInfo</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">element:</span> <span class="pre">Element</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">potential:</span> <span class="pre">Literal\['All</span> <span class="pre">Electron'</span></span>*, *<span class="n"><span class="pre">'Pseudopotential'\]</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">name:</span> <span class="pre">str</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">alias_names:</span> <span class="pre">list</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">filename:</span> <span class="pre">str</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">version:</span> <span class="pre">str</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">nset:</span> <span class="pre">int</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">n:</span> <span class="pre">list\[int\]</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">lmax:</span> <span class="pre">list\[int\]</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">lmin:</span> <span class="pre">list\[int\]</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">nshell:</span> <span class="pre">list\[dict\[int</span></span>*, *<span class="n"><span class="pre">int\]\]</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">exponents:</span> <span class="pre">list\[list\[float\]\]</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">coefficients:</span> <span class="pre">list\[dict\[int</span></span>*, *<span class="n"><span class="pre">dict\[int</span></span>*, *<span class="n"><span class="pre">dict\[int</span></span>*, *<span class="n"><span class="pre">float\]\]\]\]</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2343-L2499"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.cp2k.inputs.AtomicMetadata"
class="reference internal"
title="pymatgen.io.cp2k.inputs.AtomicMetadata"><span class="pre"><code
class="sourceCode python">AtomicMetadata</code></span></a>

Model definition of a GTO basis set.

<span class="sig-name descname"><span class="pre">info</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet.info"
class="headerlink" title="Link to this definition"></a>  
Cardinality of this basis

Type<span class="colon">:</span>  
<a href="#pymatgen.io.cp2k.inputs.BasisInfo" class="reference internal"
title="pymatgen.io.cp2k.inputs.BasisInfo">BasisInfo</a> \| None

<span class="sig-name descname"><span class="pre">nset</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet.nset"
class="headerlink" title="Link to this definition"></a>  
Number of exponent sets

Type<span class="colon">:</span>  
int \| None

<span class="sig-name descname"><span class="pre">n</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet.n"
class="headerlink" title="Link to this definition"></a>  
Principle quantum number for each set

Type<span class="colon">:</span>  
list\[int\] \| None

<span class="sig-name descname"><span class="pre">lmax</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet.lmax"
class="headerlink" title="Link to this definition"></a>  
Maximum angular momentum quantum number for each set

Type<span class="colon">:</span>  
list\[int\] \| None

<span class="sig-name descname"><span class="pre">lmin</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet.lmin"
class="headerlink" title="Link to this definition"></a>  
Minimum angular momentum quantum number for each set

Type<span class="colon">:</span>  
list\[int\] \| None

<span class="sig-name descname"><span class="pre">nshell</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet.nshell"
class="headerlink" title="Link to this definition"></a>  
Number of shells for angular momentum l for each set

Type<span class="colon">:</span>  
list\[dict\[int, int\]\] \| None

<span class="sig-name descname"><span class="pre">exponents</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet.exponents"
class="headerlink" title="Link to this definition"></a>  
Exponents for each set

Type<span class="colon">:</span>  
list\[list\[float\]\] \| None

<span class="sig-name descname"><span class="pre">coefficients</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet.coefficients"
class="headerlink" title="Link to this definition"></a>  
Contraction coefficients for each set. Dict\[exp-\>l-\>shell\]

Type<span class="colon">:</span>  
list\[dict\[int, dict\[int, dict\[int, float\]\]\]\] \| None

<span class="sig-name descname"><span class="pre">coefficients</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id20" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">exponents</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id21" class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">string</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2431-L2499"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet.from_str"
class="headerlink" title="Link to this definition"></a>  
Read from standard CP2K GTO formatted string.

<span class="sig-name descname"><span class="pre">get_keyword</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.cp2k.inputs.Keyword" class="reference internal"
title="pymatgen.io.cp2k.inputs.Keyword"><span
class="pre">Keyword</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2387-L2395"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet.get_keyword"
class="headerlink" title="Link to this definition"></a>  
Convert basis to keyword object.

<span class="sig-name descname"><span class="pre">get_str</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2402-L2429"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet.get_str"
class="headerlink" title="Link to this definition"></a>  
Get standard CP2K GTO formatted string.

<span class="sig-name descname"><span class="pre">info</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="#pymatgen.io.cp2k.inputs.BasisInfo" class="reference internal"
title="pymatgen.io.cp2k.inputs.BasisInfo"><span
class="pre">BasisInfo</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id22" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">lmax</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id23" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">lmin</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id24" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">n</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id25" class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">nexp</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet.nexp"
class="headerlink" title="Link to this definition"></a>  
Number of exponents.

<span class="sig-name descname"><span class="pre">nset</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id26" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">nshell</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id27" class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Global</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">project_name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'CP2K'</span></span>*, *<span class="n"><span class="pre">run_type</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'ENERGY_FORCE'</span></span>*, *<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L782-L815"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Global" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span class="pre"><code
class="sourceCode python">Section</code></span></a>

Controls ‘global’ settings for CP2K execution such as RUN_TYPE and
PROJECT_NAME.

Initialize the global section.

Parameters<span class="colon">:</span>  
- **project_name** – Defaults to “CP2K”.

- **run_type** – what type of calculation to run

- **keywords** – Additional keywords to add

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">GthPotential</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">info:</span> <span class="pre">PotentialInfo</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">element:</span> <span class="pre">Element</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">potential:</span> <span class="pre">Literal\['All</span> <span class="pre">Electron'</span></span>*, *<span class="n"><span class="pre">'Pseudopotential'\]</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">name:</span> <span class="pre">str</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">alias_names:</span> <span class="pre">list</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">filename:</span> <span class="pre">str</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">version:</span> <span class="pre">str</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">n_elecs:</span> <span class="pre">dict\[int</span></span>*, *<span class="n"><span class="pre">int\]</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">r_loc:</span> <span class="pre">float</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">nexp_ppl:</span> <span class="pre">int</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">c_exp_ppl:</span> <span class="pre">Sequence</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">radii:</span> <span class="pre">dict\[int</span></span>*, *<span class="n"><span class="pre">float\]</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">nprj:</span> <span class="pre">int</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">nprj_ppnl:</span> <span class="pre">dict\[int</span></span>*, *<span class="n"><span class="pre">int\]</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">hprj_ppnl:</span> <span class="pre">dict\[int</span></span>*, *<span class="n"><span class="pre">dict\[int</span></span>*, *<span class="n"><span class="pre">dict\[int</span></span>*, *<span class="n"><span class="pre">float\]\]\]</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2563-L2742"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.GthPotential" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.cp2k.inputs.AtomicMetadata"
class="reference internal"
title="pymatgen.io.cp2k.inputs.AtomicMetadata"><span class="pre"><code
class="sourceCode python">AtomicMetadata</code></span></a>

Representation of GTH-type (pseudo)potential.

<span class="sig-name descname"><span class="pre">info</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.GthPotential.info" class="headerlink"
title="Link to this definition"></a>  
Info about this potential

Type<span class="colon">:</span>  
<a href="#pymatgen.io.cp2k.inputs.PotentialInfo"
class="reference internal"
title="pymatgen.io.cp2k.inputs.PotentialInfo">PotentialInfo</a>

<span class="sig-name descname"><span class="pre">n_elecs</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.GthPotential.n_elecs"
class="headerlink" title="Link to this definition"></a>  
Number of electrons for each quantum number

Type<span class="colon">:</span>  
dict\[int, int\] \| None

<span class="sig-name descname"><span class="pre">r_loc</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.GthPotential.r_loc" class="headerlink"
title="Link to this definition"></a>  
Radius of local projectors

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">nexp_ppl</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.GthPotential.nexp_ppl"
class="headerlink" title="Link to this definition"></a>  
Number of the local pseudopotential functions

Type<span class="colon">:</span>  
int \| None

<span class="sig-name descname"><span class="pre">c_exp_ppl</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.GthPotential.c_exp_ppl"
class="headerlink" title="Link to this definition"></a>  
Sequence = field(None, description=”Coefficients of the local
pseudopotential functions

Type<span class="colon">:</span>  
Sequence \| None

<span class="sig-name descname"><span class="pre">radii</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.GthPotential.radii" class="headerlink"
title="Link to this definition"></a>  
Radius of the nonlocal part for angular momentum quantum number l
defined by the Gaussian function exponents alpha_prj_ppnl

Type<span class="colon">:</span>  
dict\[int, float\] \| None

<span class="sig-name descname"><span class="pre">nprj</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.GthPotential.nprj" class="headerlink"
title="Link to this definition"></a>  
Number of projectors

Type<span class="colon">:</span>  
int \| None

<span class="sig-name descname"><span class="pre">nprj_ppnl</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.GthPotential.nprj_ppnl"
class="headerlink" title="Link to this definition"></a>  
Number of the non-local projectors for the angular momentum quantum
number

Type<span class="colon">:</span>  
dict\[int, int\] \| None

<span class="sig-name descname"><span class="pre">hprj_ppnl</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.GthPotential.hprj_ppnl"
class="headerlink" title="Link to this definition"></a>  
Coefficients of the non-local projector functions. Coeff ij for ang
momentum l

Type<span class="colon">:</span>  
dict\[int, dict\[int, dict\[int, float\]\]\] \| None

<span class="sig-name descname"><span class="pre">)</span></span>  

<span class="sig-name descname"><span class="pre">c_exp_ppl</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id28" class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_section</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">section</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span
class="pre">Section</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2635-L2642"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.GthPotential.from_section"
class="headerlink" title="Link to this definition"></a>  
Extract GTH-formatted string from a section and convert it to model.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">string</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2677-L2742"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.GthPotential.from_str"
class="headerlink" title="Link to this definition"></a>  
Initialize model from a GTH formatted string.

<span class="sig-name descname"><span class="pre">get_keyword</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.cp2k.inputs.Keyword" class="reference internal"
title="pymatgen.io.cp2k.inputs.Keyword"><span
class="pre">Keyword</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2615-L2620"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.GthPotential.get_keyword"
class="headerlink" title="Link to this definition"></a>  
Get keyword object for the potential.

<span class="sig-name descname"><span class="pre">get_section</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span
class="pre">Section</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2622-L2633"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.GthPotential.get_section"
class="headerlink" title="Link to this definition"></a>  
Convert model to a GTH-formatted section object for input files.

<span class="sig-name descname"><span class="pre">get_str</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2644-L2675"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.GthPotential.get_str"
class="headerlink" title="Link to this definition"></a>  
Convert model to a GTH-formatted string.

<span class="sig-name descname"><span class="pre">hprj_ppnl</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id29" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">n_elecs</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id30" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">nexp_ppl</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id31" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">nprj</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id32" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">nprj_ppnl</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id33" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">r_loc</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id34" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">radii</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id35" class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Keyword</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="o"><span class="pre">\*</span></span><span class="n"><span class="pre">values</span></span>*, *<span class="n"><span class="pre">description</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">units</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">verbose</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">repeats</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L61-L174"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Keyword" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

A keyword argument in CP2K. Within CP2K Sections, which activate
features of the CP2K code, the keywords are arguments that control the
functionality of that feature. For example, the section “FORCE_EVAL”
activates the evaluation of forces/energies, but within “FORCE_EVAL” the
keyword “METHOD” controls whether or not this will be done with, say,
“Quickstep” (DFT) or “EIP” (empirical interatomic potential).

Initialize a keyword. These Keywords and the value passed to them are
sometimes as simple as KEYWORD VALUE, but can also be more elaborate
such as KEYWORD \[UNITS\] VALUE1 VALUE2, which is why this class exists:
to handle many values and control easy printing to an input file.

Parameters<span class="colon">:</span>  
- **name** – The name of this keyword. Must match an acceptable keyword
  from CP2K

- **values** – All non-keyword arguments after ‘name’ are interpreted as
  the values to set for this keyword. i.e: KEYWORD ARG1 ARG2 would
  provide two values to the keyword.

- **description** – The description for this keyword. This can make
  readability of input files easier for some. Default=None.

- **units** – The units for this keyword. If not specified, CP2K default
  units will be used. Consult manual for default units. Default=None.

- **verbose** – Whether the description should be printed with the
  string of this keyword

- **repeats** – Whether or not this keyword may be repeated.
  Default=False.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L124-L135"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Keyword.as_dict" class="headerlink"
title="Link to this definition"></a>  
Get a dictionary representation of the Keyword.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L141-L151"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Keyword.from_dict" class="headerlink"
title="Link to this definition"></a>  
Initialize from dictionary.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">s</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">description</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L153-L170"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Keyword.from_str" class="headerlink"
title="Link to this definition"></a>  
Initialize from a string.

Keywords must be labeled with strings. If the post-processor finds that
the keywords is a number, then None is return (used by the file reader).

Returns<span class="colon">:</span>  
Keyword or None

<span class="sig-name descname"><span class="pre">get_str</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L137-L139"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Keyword.get_str" class="headerlink"
title="Link to this definition"></a>  
String representation of Keyword.

<span class="sig-name descname"><span class="pre">verbosity</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">v</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L172-L174"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Keyword.verbosity" class="headerlink"
title="Link to this definition"></a>  
Change the printing of this keyword’s description.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">KeywordList</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.io.cp2k.inputs.Keyword" class="reference internal"
title="pymatgen.io.cp2k.inputs.Keyword"><span
class="pre">Keyword</span></a><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L177-L227"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.KeywordList" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Some keywords can be repeated, which makes accessing them via the normal
dictionary methods a little unnatural. This class deals with this by
defining a collection of same-named keywords that are accessed by one
name.

Initialize a keyword list given a sequence of keywords.

Parameters<span class="colon">:</span>  
**keywords** – A list of keywords. Must all have the same name
(case-insensitive)

<span class="sig-name descname"><span class="pre">append</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">item</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L212-L214"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.KeywordList.append" class="headerlink"
title="Link to this definition"></a>  
Append the keyword list.

<span class="sig-name descname"><span class="pre">extend</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">lst</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.io.cp2k.inputs.Keyword" class="reference internal"
title="pymatgen.io.cp2k.inputs.Keyword"><span
class="pre">Keyword</span></a><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L216-L218"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.KeywordList.extend" class="headerlink"
title="Link to this definition"></a>  
Extend the keyword list.

<span class="sig-name descname"><span class="pre">get_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">indent</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L220-L222"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.KeywordList.get_str"
class="headerlink" title="Link to this definition"></a>  
String representation of Keyword.

<span class="sig-name descname"><span class="pre">verbosity</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">verbosity</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L224-L227"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.KeywordList.verbosity"
class="headerlink" title="Link to this definition"></a>  
Silence all keywords in keyword list.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Kind</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">specie</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">alias</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">magnetization</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.0</span></span>*, *<span class="n"><span class="pre">basis_set</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet"
class="reference internal"
title="pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet"><span
class="pre">GaussianTypeOrbitalBasisSet</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'GTH_BASIS'</span></span>*, *<span class="n"><span class="pre">potential</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.cp2k.inputs.GthPotential"
class="reference internal"
title="pymatgen.io.cp2k.inputs.GthPotential"><span
class="pre">GthPotential</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'GTH_POTENTIALS'</span></span>*, *<span class="n"><span class="pre">ghost</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">aux_basis</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet"
class="reference internal"
title="pymatgen.io.cp2k.inputs.GaussianTypeOrbitalBasisSet"><span
class="pre">GaussianTypeOrbitalBasisSet</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">subsections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L1285-L1373"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Kind" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span class="pre"><code
class="sourceCode python">Section</code></span></a>

Specify the information for the different atom types being simulated.

Initialize a KIND section.

Parameters<span class="colon">:</span>  
- **specie** – Object representing the atom.

- **alias** – Alias for the atom, can be used for specifying
  modifications to certain atoms but not all, e.g. Mg_1 and Mg_2 to
  force difference oxidation states on the two atoms.

- **magnetization** – From the CP2K Manual: The magnetization used in
  the atomic initial guess. Adds magnetization/2 spin-alpha electrons
  and removes magnetization/2 spin-beta electrons.

- **basis_set** – Basis set for this atom, accessible from the basis set
  file specified

- **potential** – Pseudopotential for this atom, accessible from the
  potential file

- **ghost** – Turn this into ghost atom (disable the potential)

- **aux_basis** – Auxiliary basis to use with ADMM

- **keywords** – additional keywords

- **subsections** – additional subsections

- **kwargs** – Additional kwargs to pass to Section()

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">KpointSet</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">npoints</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">kpoints</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Iterable</span></span>*, *<span class="n"><span class="pre">units</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'B_VECTOR'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2045-L2083"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.KpointSet" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span class="pre"><code
class="sourceCode python">Section</code></span></a>

Specify a kpoint line to be calculated between special points.

Parameters<span class="colon">:</span>  
- **npoints** (*int*) – Number of kpoints along the line.

- **kpoints** – A dictionary of {label: kpoint} kpoints defining the
  path

- **units** (*str*) –

  Units for the kpoint coordinates. Options: “B_VECTOR” (reciprocal
  coordinates)

  > <div>
  >
  > ”CART_ANGSTROM” (units of 2\*Pi/Angstrom) “CART_BOHR” (units of
  > 2\*Pi/Bohr).
  >
  > </div>

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Kpoint_Set</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">npoints</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*, *<span class="n"><span class="pre">kpoints</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Iterable</span></span>*, *<span class="n"><span class="pre">units</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'B_VECTOR'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2086-L2088"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Kpoint_Set" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.KpointSet" class="reference internal"
title="pymatgen.io.cp2k.inputs.KpointSet"><span class="pre"><code
class="sourceCode python">KpointSet</code></span></a>

Parameters<span class="colon">:</span>  
- **npoints** (*int*) – Number of kpoints along the line.

- **kpoints** – A dictionary of {label: kpoint} kpoints defining the
  path

- **units** (*str*) –

  Units for the kpoint coordinates. Options: “B_VECTOR” (reciprocal
  coordinates)

  > <div>
  >
  > ”CART_ANGSTROM” (units of 2\*Pi/Angstrom) “CART_BOHR” (units of
  > 2\*Pi/Bohr).
  >
  > </div>

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Kpoints</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">kpts</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">weights</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">eps_geo</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-06</span></span>*, *<span class="n"><span class="pre">full_grid</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">parallel_group_size</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">-1</span></span>*, *<span class="n"><span class="pre">scheme</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'MONKHORST-PACK'</span></span>*, *<span class="n"><span class="pre">symmetry</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">units</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'B_VECTOR'</span></span>*, *<span class="n"><span class="pre">verbose</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">wavefunctions</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'COMPLEX'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L1900-L2042"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Kpoints" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span class="pre"><code
class="sourceCode python">Section</code></span></a>

Description of the k-points to use for the calculation.

Parameters<span class="colon">:</span>  
- **kpts** (*list,* *tuple*) – a 2D array for the kpoints of the form
  \[(1,1,1),\]. If len(kpts) == 1. Then it is taken as subdivisions for
  automatic kpoint scheme. If it has more entries, it is taken as manual
  entries for kpoints.

- **weights** (*list,* *tuple*) – a weight for each kpoint. Default is
  to weigh each by 1

- **eps_geo** (*float*) – tolerance for symmetry. Default=1e-6

- **full_grid** (*bool*) – use full (not reduced) kpoint grid.
  Default=False.

- **parallel_group_size** (*int*) – from CP2K manual: Number of
  processors to be used for a single kpoint. This number must divide the
  total number of processes. The number of groups must divide the total
  number of kpoints. Value=-1 (smallest possible number of processes per
  group, satisfying the constraints). Value=0 (all processes). Value=n
  (exactly n processes). Default=-1.

- **scheme** (*str*) – kpoint generation scheme.
  Default=’Monkhorst-Pack’

- **symmetry** (*bool*) – Use symmetry to reduce the number of kpoints.
  Default=False.

- **units** (*str*) – Units for the kpoint coordinates (reciprocal
  coordinates or cartesian). Default=’B_VECTOR’ (reciprocal)

- **verbose** (*bool*) – verbose output for kpoints. Default=False

- **wavefunctions** (*str*) – Whether to use complex or real valued
  wavefunctions (if available). Default=’complex’.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_kpoints</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">kpoints</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">VaspKpoints</span></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L1986-L2042"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Kpoints.from_kpoints"
class="headerlink" title="Link to this definition"></a>  
Initialize the section from a Kpoints object (pymatgen.io.vasp.inputs).
CP2K does not have an automatic gamma-point constructor, so this is
generally used to get the number of divisions from a kpoint static
constructor and then build a Monkhorst-Pack grid, which is sufficient
for gamma-recommended systems so long as the grid is fine enough.

Parameters<span class="colon">:</span>  
- **kpoints**
  (<a href="#pymatgen.io.cp2k.inputs.Kpoints" class="reference internal"
  title="pymatgen.io.cp2k.inputs.Kpoints"><em>Kpoints</em></a>) – A
  pymatgen kpoints object.

- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  Required for automatically performing symmetry analysis and reducing
  the kpoint grid.

- **reduce** – whether or not to reduce the grid using symmetry. CP2K
  itself cannot do this automatically without spglib present at
  execution time.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">LDOS</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">index</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1</span></span>*, *<span class="n"><span class="pre">alias</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">subsections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L1540-L1573"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.LDOS" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span class="pre"><code
class="sourceCode python">Section</code></span></a>

Controls printing of the LDOS (List-Density of states). i.e. projects
onto specific atoms.

Initialize the LDOS section.

Parameters<span class="colon">:</span>  
- **index** – Index of the atom to project onto

- **alias** – section alias

- **keywords** – additional keywords

- **subsections** – additional subsections

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">MOCubes</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">write_cube</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">nhomo</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1</span></span>*, *<span class="n"><span class="pre">nlumo</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1</span></span>*, *<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">subsections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L1599-L1632"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.MOCubes" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span class="pre"><code
class="sourceCode python">Section</code></span></a>

Controls printing of the molecular orbital eigenvalues.

Initialize the MO_CUBES section.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">MO_Cubes</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">write_cube</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">nhomo</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1</span></span>*, *<span class="n"><span class="pre">nlumo</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1</span></span>*, *<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">subsections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L1635-L1637"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.MO_Cubes" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.MOCubes" class="reference internal"
title="pymatgen.io.cp2k.inputs.MOCubes"><span class="pre"><code
class="sourceCode python">MOCubes</code></span></a>

Initialize the MO_CUBES section.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Mgrid</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">cutoff</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1200</span></span>*, *<span class="n"><span class="pre">rel_cutoff</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">80</span></span>*, *<span class="n"><span class="pre">ngrids</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">5</span></span>*, *<span class="n"><span class="pre">progression_factor</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">3</span></span>*, *<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">subsections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L1022-L1081"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Mgrid" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span class="pre"><code
class="sourceCode python">Section</code></span></a>

Controls the multigrid for numerical integration.

Initialize the MGRID section.

Parameters<span class="colon">:</span>  
- **cutoff** – Cutoff energy (in Rydbergs for historical reasons)
  defining how find of Gaussians will be used

- **rel_cutoff** – The relative cutoff energy, which defines how to map
  the Gaussians onto the multigrid. If the value is too low then, even
  if you have a high cutoff with sharp Gaussians, they will be mapped to
  the course part of the multigrid

- **ngrids** – number of grids to use

- **progression_factor** – divisor that decides how to map Gaussians the
  multigrid after the highest mapping is decided by rel_cutoff

- **keywords** – additional keywords

- **subsections** – additional subsections

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">OrbitalTransformation</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">minimizer</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'CG'</span></span>*, *<span class="n"><span class="pre">preconditioner</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'FULL_ALL'</span></span>*, *<span class="n"><span class="pre">algorithm</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'STRICT'</span></span>*, *<span class="n"><span class="pre">rotation</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">occupation_preconditioner</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">energy_gap</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">-1</span></span>*, *<span class="n"><span class="pre">linesearch</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'2PNT'</span></span>*, *<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">subsections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L1170-L1260"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.OrbitalTransformation"
class="headerlink" title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span class="pre"><code
class="sourceCode python">Section</code></span></a>

Turns on the Orbital Transformation scheme for diagonalizing the
Hamiltonian. Often faster and with guaranteed convergence compared to
normal diagonalization, but requires the system to have a band gap.

NOTE: OT has poor convergence for metallic systems and cannot use SCF
mixing or smearing. Therefore, you should not use it for metals or
systems with ‘small’ band gaps. In that case, use normal diagonalization

Initialize the OT section.

Parameters<span class="colon">:</span>  
- **minimizer** – The minimizer to use with the OT method. Default is
  conjugate gradient method, which is more robust, but more well-behaved
  systems should use DIIS, which can be as much as 50% faster.

- **preconditioner** – Preconditioner to use for OT, FULL_ALL tends to
  be most robust, but is not always most efficient. For difficult
  systems, FULL_SINGLE_INVERSE can be more robust, and is reasonably
  efficient with large systems. For huge, but well behaved, systems,
  where construction of the preconditioner can take a very long time,
  FULL_KINETIC can be a good choice.

- **algorithm** – What algorithm to use for OT. ‘Strict’: Taylor or
  diagonalization based algorithm. IRAC: Orbital Transformation based
  Iterative Refinement of the Approximate Congruence transformation
  (OT/IR).

- **rotation** – Introduce additional variables to allow subspace
  rotations (i.e fractional occupations)

- **occupation_preconditioner** – include the fractional occupation in
  the preconditioning

- **energy_gap** – Guess for the band gap. For FULL_ALL, should be
  smaller than the actual band gap, so simply using 0.01 is a robust
  value. Choosing a larger value will help if you start with a bad
  initial guess though. For FULL_SINGLE_INVERSE, energy_gap is treated
  as a lower bound. Values lower than 0.05 in this case can lead to
  stability issues.

- **linesearch** (*str*) – From the manual: 1D line search algorithm to
  be used with the OT minimizer, in increasing order of robustness and
  cost. MINIMIZER CG combined with LINESEARCH GOLD should always find an
  electronic minimum. Whereas the 2PNT minimizer is almost always OK,
  3PNT might be needed for systems in which successive OT CG steps do
  not decrease the total energy.

- **keywords** – additional keywords

- **subsections** – additional subsections

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">PBE</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">parameterization</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'ORIG'</span></span>*, *<span class="n"><span class="pre">scale_c</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1</span></span>*, *<span class="n"><span class="pre">scale_x</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1</span></span>*, *<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">subsections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L1857-L1897"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.PBE" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span class="pre"><code
class="sourceCode python">Section</code></span></a>

Info about the PBE functional.

Parameters<span class="colon">:</span>  
- **parameterization** (*str*) – ORIG: original PBE PBESOL: PBE for
  solids/surfaces REVPBE: revised PBE

- **scale_c** (*float*) – scales the correlation part of the functional.

- **scale_x** (*float*) – scales the exchange part of the functional.

- **keywords** – additional keywords

- **subsections** – additional subsections.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">PDOS</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">nlumo</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">-1</span></span>*, *<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">subsections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L1503-L1537"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.PDOS" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span class="pre"><code
class="sourceCode python">Section</code></span></a>

Controls printing of projected density of states onto the different atom
KINDS (elemental decomposed DOS).

Initialize the PDOS section.

Parameters<span class="colon">:</span>  
- **nlumo** – how many unoccupied orbitals to include (-1==ALL)

- **keywords** – additional keywords

- **subsections** – additional subsections

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">PotentialFile</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">objects</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2790-L2798"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.PotentialFile" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.DataFile" class="reference internal"
title="pymatgen.io.cp2k.inputs.DataFile"><span class="pre"><code
class="sourceCode python">DataFile</code></span></a>

Data file for potentials only.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">string</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2794-L2798"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.PotentialFile.from_str"
class="headerlink" title="Link to this definition"></a>  
Initialize from a string representation.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">PotentialInfo</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">electrons</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">potential_type</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">nlcc</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">xc</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2502-L2560"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.PotentialInfo" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Metadata for this potential.

<span class="sig-name descname"><span class="pre">electrons</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.PotentialInfo.electrons"
class="headerlink" title="Link to this definition"></a>  
Total number of electrons

Type<span class="colon">:</span>  
int \| None

<span class="sig-name descname"><span class="pre">potential_type</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.PotentialInfo.potential_type"
class="headerlink" title="Link to this definition"></a>  
Potential type (e.g. GTH)

Type<span class="colon">:</span>  
str \| None

<span class="sig-name descname"><span class="pre">nlcc</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.PotentialInfo.nlcc" class="headerlink"
title="Link to this definition"></a>  
Nonlinear core corrected potential

Type<span class="colon">:</span>  
bool \| None

<span class="sig-name descname"><span class="pre">xc</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.PotentialInfo.xc" class="headerlink"
title="Link to this definition"></a>  
Exchange correlation functional used for creating this potential

Type<span class="colon">:</span>  
str \| None

<span class="sig-name descname"><span class="pre">electrons</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id36" class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">string</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2530-L2560"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.PotentialInfo.from_str"
class="headerlink" title="Link to this definition"></a>  
Get a CP2K formatted string representation.

<span class="sig-name descname"><span class="pre">nlcc</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id37" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">potential_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id38" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">softmatch</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L2519-L2528"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.PotentialInfo.softmatch"
class="headerlink" title="Link to this definition"></a>  
Soft matching to see if two potentials match.

Will only match those attributes which *are* defined for this basis info
object (one way checking)

<span class="sig-name descname"><span class="pre">xc</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id39" class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">QS</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">method</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'GPW'</span></span>*, *<span class="n"><span class="pre">eps_default</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-10</span></span>*, *<span class="n"><span class="pre">eps_pgf_orb</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">extrapolation</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'ASPC'</span></span>*, *<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">subsections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L905-L963"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.QS" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span class="pre"><code
class="sourceCode python">Section</code></span></a>

Controls the quickstep settings (DFT driver).

Initialize the QS Section.

Parameters<span class="colon">:</span>  
- **method** (*"GPW"* *\|* *"GAPW"*) – What DFT methodology to use. GPW
  (Gaussian Plane Waves) for DFT with pseudopotentials or GAPW (Gaussian
  Augmented Plane Waves) for all electron calculations.

- **eps_default** (*float*) – The default level of convergence accuracy.
  NOTE: This is a global value for all the numerical value of all
  EPS\_\* values in QS module. It is not the same as EPS_SCF, which sets
  convergence accuracy of the SCF cycle alone.

- **eps_pgf_orb** – Precision for the overlap matrix. Default is to use
  sqrt(eps_default)

- **extrapolation** (*"PS"* *\|* *"ASPC"*) – Method use for
  extrapolation. If using gamma-point-only calculation, then one should
  either PS or ASPC (ASPC especially for MD runs). See the manual for
  other options.

- **keywords** – Additional keywords to add

- **subsections** – Subsections to initialize with.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Scf</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">max_scf</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">50</span></span>*, *<span class="n"><span class="pre">eps_scf</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-06</span></span>*, *<span class="n"><span class="pre">scf_guess</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'RESTART'</span></span>*, *<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">subsections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L966-L1019"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Scf" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span class="pre"><code
class="sourceCode python">Section</code></span></a>

Controls the self consistent field loop.

Initialize the Scf section.

Parameters<span class="colon">:</span>  
- **max_scf** (*int*) – Maximum number of SCF loops before terminating.
  Defaults to 50.

- **eps_scf** (*float*) – Convergence criteria for SCF loop. Defaults to
  1e-6.

- **scf_guess** –

  Initial guess for SCF loop. “ATOMIC”: Generate an atomic density using
  the atomic code “CORE”: Diagonalize the core Hamiltonian for an
  initial guess. “HISTORY_RESTART”: Extrapolated from previous RESTART
  files. “MOPAC”: Use same guess as MOPAC for semi-empirical methods or
  a simple

  > <div>
  >
  > diagonal density matrix for other methods.
  >
  > </div>

  ”NONE”: Skip initial guess (only for NON-SCC DFTB). “RANDOM”: Use
  random wavefunction coefficients. “RESTART”: Use the RESTART file as
  an initial guess (and ATOMIC if not present). “SPARSE”: Generate a
  sparse wavefunction using the atomic code (for OT based

  > <div>
  >
  > methods).
  >
  > </div>

- **keywords** – Additional keywords

- **subsections** – Additional subsections

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Section</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">subsections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">repeats</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">description</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">section_parameters</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">()</span></span>*, *<span class="n"><span class="pre">location</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">verbose</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">alias</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L230-L585"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Section" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Basic input representation of input to CP2K. Activates functionality
inside of the CP2K executable.

Basic object representing a CP2K Section. Sections activate different
parts of the calculation. For example, FORCE_EVAL section will activate
CP2K’s ability to calculate forces.

Parameters<span class="colon">:</span>  
- **name** – The name of the section (must match name in CP2K)

- **subsections** – A dictionary of subsections that are nested in this
  section. Format is {‘NAME’: Section(*args, \*\*kwargs). The name you
  chose for ‘NAME’ to index that subsection does not \*have* to be the
  same as the section’s true name, but we recommend matching them. You
  can specify a blank dictionary if there are no subsections, or if you
  want to insert the subsections later.

- **repeats** – Whether or not this section can be repeated. Most
  sections cannot. Default=False.

- **description** – Description of this section for easier readability

- **keywords** – the keywords to be set for this section. Each element
  should be a Keyword object. This can be more cumbersome than simply
  using kwargs for building a class in a script, but is more convenient
  for the class instantiations of CP2K sections (see below).

- **section_parameters** – the section parameters for this section.
  Section parameters are specialized keywords that modify the behavior
  of the section overall. Most sections do not have section parameters,
  but some do. Unlike normal Keywords, these are specified as strings
  and not as Keyword objects.

- **location** – the path to the section in the form
  ‘SECTION/SUBSECTION1/SUBSECTION3’, example for QS module:
  ‘FORCE_EVAL/DFT/QS’. This location is used to automatically determine
  if a subsection requires a supersection to be activated.

- **verbose** – Controls how much is printed to CP2K input files (Also
  see Keyword). If True, then a description of the section will be
  printed with it as a comment (if description is set). Default=True.

- **alias** – An alias for this class to use in place of the name.

- **keyword** (*kwargs are interpreted as*)

- **as** (*value pairs and added to the keywords array*)

- **objects**
  (<a href="#pymatgen.io.cp2k.inputs.Keyword" class="reference internal"
  title="pymatgen.io.cp2k.inputs.Keyword"><em>Keyword</em></a>)

<span class="sig-name descname"><span class="pre">add</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L370-L374"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Section.add" class="headerlink"
title="Link to this definition"></a>  
Add another keyword to the current section.

<span class="sig-name descname"><span class="pre">by_path</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">path</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L519-L532"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Section.by_path" class="headerlink"
title="Link to this definition"></a>  
Access a sub-section using a path. Used by the file parser.

Parameters<span class="colon">:</span>  
**path** (*str*) – Path to section of form
‘SUBSECTION1/SUBSECTION2/SUBSECTION_OF_INTEREST’

<span class="sig-name descname"><span class="pre">check</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">path</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L502-L517"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Section.check" class="headerlink"
title="Link to this definition"></a>  
Check if section exists within the current using a path. Can be useful
for cross-checking whether or not required dependencies have been
satisfied, which CP2K does not enforce.

Parameters<span class="colon">:</span>  
**path** (*str*) – Path to section of form
‘SUBSECTION1/SUBSECTION2/SUBSECTION_OF_INTEREST’

<span class="sig-name descname"><span class="pre">get</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">d</span></span>*, *<span class="n"><span class="pre">default</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L376-L388"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Section.get" class="headerlink"
title="Link to this definition"></a>  
Similar to get for dictionaries. This will attempt to retrieve the
section or keyword matching d. Will not raise an error if d does not
exist.

Parameters<span class="colon">:</span>  
- **d** – the key to retrieve, if present

- **default** – what to return if d is not found

<span class="sig-name descname"><span class="pre">get_keyword</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">d</span></span>*, *<span class="n"><span class="pre">default</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L402-L412"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Section.get_keyword"
class="headerlink" title="Link to this definition"></a>  
Get function, only for subsections.

Parameters<span class="colon">:</span>  
- **d** – Name of keyword to get

- **default** – return if d is not found in keyword list

<span class="sig-name descname"><span class="pre">get_section</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">d</span></span>*, *<span class="n"><span class="pre">default</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L390-L400"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Section.get_section"
class="headerlink" title="Link to this definition"></a>  
Get function, only for subsections.

Parameters<span class="colon">:</span>  
- **d** – Name of section to get

- **default** – return if d is not found in subsections

<span class="sig-name descname"><span class="pre">get_str</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L534-L536"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Section.get_str" class="headerlink"
title="Link to this definition"></a>  
Get string representation of Section.

<span class="sig-name descname"><span class="pre">inc</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L484-L494"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Section.inc" class="headerlink"
title="Link to this definition"></a>  
Mongo style dict modification. Include.

<span class="sig-name descname"><span class="pre">insert</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">d</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span
class="pre">Section</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="#pymatgen.io.cp2k.inputs.SectionList"
class="reference internal"
title="pymatgen.io.cp2k.inputs.SectionList"><span
class="pre">SectionList</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L496-L500"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Section.insert" class="headerlink"
title="Link to this definition"></a>  
Insert a new section as a subsection of the current one.

<span class="sig-name descname"><span class="pre">safeset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L468-L470"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Section.safeset" class="headerlink"
title="Link to this definition"></a>  
Alias for update with strict (no insertions). Used by custodian.

<span class="sig-name descname"><span class="pre">set</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L464-L466"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Section.set" class="headerlink"
title="Link to this definition"></a>  
Alias for update. Used by custodian.

<span class="sig-name descname"><span class="pre">setitem</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">key</span></span>*, *<span class="n"><span class="pre">value</span></span>*, *<span class="n"><span class="pre">strict</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L349-L368"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Section.setitem" class="headerlink"
title="Link to this definition"></a>  
Helper function for setting items. Kept separate from the
double-underscore function so that “strict” option can be made possible.

strict will only set values for items that already have a key entry (no
insertion).

<span class="sig-name descname"><span class="pre">silence</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L579-L585"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Section.silence" class="headerlink"
title="Link to this definition"></a>  
Recursively delete all print sections so that only defaults are printed
out.

<span class="sig-name descname"><span class="pre">unset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L472-L482"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Section.unset" class="headerlink"
title="Link to this definition"></a>  
Dict based deletion. Used by custodian.

<span class="sig-name descname"><span class="pre">update</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*, *<span class="n"><span class="pre">strict</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span
class="pre">Section</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L414-L439"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Section.update" class="headerlink"
title="Link to this definition"></a>  
Update the Section according to a dictionary argument. This is most
useful for providing user-override settings to default parameters. As
you pass a dictionary the class variables like “description”,
“location”, or “repeats” are not included. Therefore, it is recommended
that this be used to modify existing Section objects to a user’s needs,
but not used for the creation of new Section child-classes.

Parameters<span class="colon">:</span>  
- **dct** (*dict*) –

  A dictionary containing the update information. Should use nested
  dictionaries to specify the full path of the update. If a section or
  keyword does not exist, it will be created, but only with the values
  that are provided in “d”, not using default values from a Section
  object. Example: {

  > <div>
  >
  > ’SUBSECTION1’: {  
  > ‘SUBSEC2’: {‘NEW_KEYWORD’: ‘NEW_VAL’}, ‘NEW_SUBSEC’: {‘NEW_KWD’:
  > ‘NEW_VAL’} }
  >
  > }
  >
  > </div>

- **strict** (*bool*) – If true, only update existing sections and
  keywords. If false, allow new sections and keywords. Default: False

<span class="sig-name descname"><span class="pre">verbosity</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">verbosity</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L567-L577"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Section.verbosity" class="headerlink"
title="Link to this definition"></a>  
Change the section verbosity recursively by turning on/off the printing
of descriptions. Turning off descriptions may reduce the appealing
documentation of input files, but also helps de-clutter them.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">SectionList</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">sections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span
class="pre">Section</span></a><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L588-L646"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.SectionList" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Section list.

Initialize a SectionList object using a sequence of sections.

Parameters<span class="colon">:</span>  
**sections** – A list of keywords. Must all have the same name
(case-insensitive)

<span class="sig-name descname"><span class="pre">append</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">item</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L635-L637"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.SectionList.append" class="headerlink"
title="Link to this definition"></a>  
Append the section list.

<span class="sig-name descname"><span class="pre">extend</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">lst</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L639-L641"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.SectionList.extend" class="headerlink"
title="Link to this definition"></a>  
Extend the section list.

<span class="sig-name descname"><span class="pre">get</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">d</span></span>*, *<span class="n"><span class="pre">index</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">-1</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L629-L633"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.SectionList.get" class="headerlink"
title="Link to this definition"></a>  
Get for section list. If index is specified, return the section at that
index. Otherwise, return a get on the last section.

<span class="sig-name descname"><span class="pre">get_str</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L625-L627"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.SectionList.get_str"
class="headerlink" title="Link to this definition"></a>  
Return string representation of section list.

<span class="sig-name descname"><span class="pre">verbosity</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">verbosity</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L643-L646"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.SectionList.verbosity"
class="headerlink" title="Link to this definition"></a>  
Silence all sections in section list.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Smear</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">elec_temp</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">300</span></span>*, *<span class="n"><span class="pre">method</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'FERMI_DIRAC'</span></span>*, *<span class="n"><span class="pre">fixed_magnetic_moment</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">-100.0</span></span>*, *<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">subsections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L1663-L1691"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Smear" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span class="pre"><code
class="sourceCode python">Section</code></span></a>

Control electron smearing.

Basic object representing a CP2K Section. Sections activate different
parts of the calculation. For example, FORCE_EVAL section will activate
CP2K’s ability to calculate forces.

Parameters<span class="colon">:</span>  
- **name** – The name of the section (must match name in CP2K)

- **subsections** – A dictionary of subsections that are nested in this
  section. Format is {‘NAME’: Section(*args, \*\*kwargs). The name you
  chose for ‘NAME’ to index that subsection does not \*have* to be the
  same as the section’s true name, but we recommend matching them. You
  can specify a blank dictionary if there are no subsections, or if you
  want to insert the subsections later.

- **repeats** – Whether or not this section can be repeated. Most
  sections cannot. Default=False.

- **description** – Description of this section for easier readability

- **keywords** – the keywords to be set for this section. Each element
  should be a Keyword object. This can be more cumbersome than simply
  using kwargs for building a class in a script, but is more convenient
  for the class instantiations of CP2K sections (see below).

- **section_parameters** – the section parameters for this section.
  Section parameters are specialized keywords that modify the behavior
  of the section overall. Most sections do not have section parameters,
  but some do. Unlike normal Keywords, these are specified as strings
  and not as Keyword objects.

- **location** – the path to the section in the form
  ‘SECTION/SUBSECTION1/SUBSECTION3’, example for QS module:
  ‘FORCE_EVAL/DFT/QS’. This location is used to automatically determine
  if a subsection requires a supersection to be activated.

- **verbose** – Controls how much is printed to CP2K input files (Also
  see Keyword). If True, then a description of the section will be
  printed with it as a comment (if description is set). Default=True.

- **alias** – An alias for this class to use in place of the name.

- **keyword** (*kwargs are interpreted as*)

- **as** (*value pairs and added to the keywords array*)

- **objects**
  (<a href="#pymatgen.io.cp2k.inputs.Keyword" class="reference internal"
  title="pymatgen.io.cp2k.inputs.Keyword"><em>Keyword</em></a>)

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Subsys</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">subsections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L890-L902"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Subsys" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span class="pre"><code
class="sourceCode python">Section</code></span></a>

Controls the definition of the system to be simulated.

Initialize the subsys section.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">VHartreeCube</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">subsections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L1576-L1591"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.VHartreeCube" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span class="pre"><code
class="sourceCode python">Section</code></span></a>

Controls printing of the hartree potential as a cube file.

Basic object representing a CP2K Section. Sections activate different
parts of the calculation. For example, FORCE_EVAL section will activate
CP2K’s ability to calculate forces.

Parameters<span class="colon">:</span>  
- **name** – The name of the section (must match name in CP2K)

- **subsections** – A dictionary of subsections that are nested in this
  section. Format is {‘NAME’: Section(*args, \*\*kwargs). The name you
  chose for ‘NAME’ to index that subsection does not \*have* to be the
  same as the section’s true name, but we recommend matching them. You
  can specify a blank dictionary if there are no subsections, or if you
  want to insert the subsections later.

- **repeats** – Whether or not this section can be repeated. Most
  sections cannot. Default=False.

- **description** – Description of this section for easier readability

- **keywords** – the keywords to be set for this section. Each element
  should be a Keyword object. This can be more cumbersome than simply
  using kwargs for building a class in a script, but is more convenient
  for the class instantiations of CP2K sections (see below).

- **section_parameters** – the section parameters for this section.
  Section parameters are specialized keywords that modify the behavior
  of the section overall. Most sections do not have section parameters,
  but some do. Unlike normal Keywords, these are specified as strings
  and not as Keyword objects.

- **location** – the path to the section in the form
  ‘SECTION/SUBSECTION1/SUBSECTION3’, example for QS module:
  ‘FORCE_EVAL/DFT/QS’. This location is used to automatically determine
  if a subsection requires a supersection to be activated.

- **verbose** – Controls how much is printed to CP2K input files (Also
  see Keyword). If True, then a description of the section will be
  printed with it as a comment (if description is set). Default=True.

- **alias** – An alias for this class to use in place of the name.

- **keyword** (*kwargs are interpreted as*)

- **as** (*value pairs and added to the keywords array*)

- **objects**
  (<a href="#pymatgen.io.cp2k.inputs.Keyword" class="reference internal"
  title="pymatgen.io.cp2k.inputs.Keyword"><em>Keyword</em></a>)

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">V_Hartree_Cube</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">subsections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L1594-L1596"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.V_Hartree_Cube" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.cp2k.inputs.VHartreeCube"
class="reference internal"
title="pymatgen.io.cp2k.inputs.VHartreeCube"><span class="pre"><code
class="sourceCode python">VHartreeCube</code></span></a>

Basic object representing a CP2K Section. Sections activate different
parts of the calculation. For example, FORCE_EVAL section will activate
CP2K’s ability to calculate forces.

Parameters<span class="colon">:</span>  
- **name** – The name of the section (must match name in CP2K)

- **subsections** – A dictionary of subsections that are nested in this
  section. Format is {‘NAME’: Section(*args, \*\*kwargs). The name you
  chose for ‘NAME’ to index that subsection does not \*have* to be the
  same as the section’s true name, but we recommend matching them. You
  can specify a blank dictionary if there are no subsections, or if you
  want to insert the subsections later.

- **repeats** – Whether or not this section can be repeated. Most
  sections cannot. Default=False.

- **description** – Description of this section for easier readability

- **keywords** – the keywords to be set for this section. Each element
  should be a Keyword object. This can be more cumbersome than simply
  using kwargs for building a class in a script, but is more convenient
  for the class instantiations of CP2K sections (see below).

- **section_parameters** – the section parameters for this section.
  Section parameters are specialized keywords that modify the behavior
  of the section overall. Most sections do not have section parameters,
  but some do. Unlike normal Keywords, these are specified as strings
  and not as Keyword objects.

- **location** – the path to the section in the form
  ‘SECTION/SUBSECTION1/SUBSECTION3’, example for QS module:
  ‘FORCE_EVAL/DFT/QS’. This location is used to automatically determine
  if a subsection requires a supersection to be activated.

- **verbose** – Controls how much is printed to CP2K input files (Also
  see Keyword). If True, then a description of the section will be
  printed with it as a comment (if description is set). Default=True.

- **alias** – An alias for this class to use in place of the name.

- **keyword** (*kwargs are interpreted as*)

- **as** (*value pairs and added to the keywords array*)

- **objects**
  (<a href="#pymatgen.io.cp2k.inputs.Keyword" class="reference internal"
  title="pymatgen.io.cp2k.inputs.Keyword"><em>Keyword</em></a>)

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">XCFunctional</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">functionals</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">()</span></span>*, *<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">subsections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L1826-L1849"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.XCFunctional" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.Section" class="reference internal"
title="pymatgen.io.cp2k.inputs.Section"><span class="pre"><code
class="sourceCode python">Section</code></span></a>

Info about which XC functional to use.

Basic object representing a CP2K Section. Sections activate different
parts of the calculation. For example, FORCE_EVAL section will activate
CP2K’s ability to calculate forces.

Parameters<span class="colon">:</span>  
- **name** – The name of the section (must match name in CP2K)

- **subsections** – A dictionary of subsections that are nested in this
  section. Format is {‘NAME’: Section(*args, \*\*kwargs). The name you
  chose for ‘NAME’ to index that subsection does not \*have* to be the
  same as the section’s true name, but we recommend matching them. You
  can specify a blank dictionary if there are no subsections, or if you
  want to insert the subsections later.

- **repeats** – Whether or not this section can be repeated. Most
  sections cannot. Default=False.

- **description** – Description of this section for easier readability

- **keywords** – the keywords to be set for this section. Each element
  should be a Keyword object. This can be more cumbersome than simply
  using kwargs for building a class in a script, but is more convenient
  for the class instantiations of CP2K sections (see below).

- **section_parameters** – the section parameters for this section.
  Section parameters are specialized keywords that modify the behavior
  of the section overall. Most sections do not have section parameters,
  but some do. Unlike normal Keywords, these are specified as strings
  and not as Keyword objects.

- **location** – the path to the section in the form
  ‘SECTION/SUBSECTION1/SUBSECTION3’, example for QS module:
  ‘FORCE_EVAL/DFT/QS’. This location is used to automatically determine
  if a subsection requires a supersection to be activated.

- **verbose** – Controls how much is printed to CP2K input files (Also
  see Keyword). If True, then a description of the section will be
  printed with it as a comment (if description is set). Default=True.

- **alias** – An alias for this class to use in place of the name.

- **keyword** (*kwargs are interpreted as*)

- **as** (*value pairs and added to the keywords array*)

- **objects**
  (<a href="#pymatgen.io.cp2k.inputs.Keyword" class="reference internal"
  title="pymatgen.io.cp2k.inputs.Keyword"><em>Keyword</em></a>)

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Xc_Functional</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">functionals</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">()</span></span>*, *<span class="n"><span class="pre">keywords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">subsections</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/inputs.py#L1852-L1854"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.inputs.Xc_Functional" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.cp2k.inputs.XCFunctional"
class="reference internal"
title="pymatgen.io.cp2k.inputs.XCFunctional"><span class="pre"><code
class="sourceCode python">XCFunctional</code></span></a>

Basic object representing a CP2K Section. Sections activate different
parts of the calculation. For example, FORCE_EVAL section will activate
CP2K’s ability to calculate forces.

Parameters<span class="colon">:</span>  
- **name** – The name of the section (must match name in CP2K)

- **subsections** – A dictionary of subsections that are nested in this
  section. Format is {‘NAME’: Section(*args, \*\*kwargs). The name you
  chose for ‘NAME’ to index that subsection does not \*have* to be the
  same as the section’s true name, but we recommend matching them. You
  can specify a blank dictionary if there are no subsections, or if you
  want to insert the subsections later.

- **repeats** – Whether or not this section can be repeated. Most
  sections cannot. Default=False.

- **description** – Description of this section for easier readability

- **keywords** – the keywords to be set for this section. Each element
  should be a Keyword object. This can be more cumbersome than simply
  using kwargs for building a class in a script, but is more convenient
  for the class instantiations of CP2K sections (see below).

- **section_parameters** – the section parameters for this section.
  Section parameters are specialized keywords that modify the behavior
  of the section overall. Most sections do not have section parameters,
  but some do. Unlike normal Keywords, these are specified as strings
  and not as Keyword objects.

- **location** – the path to the section in the form
  ‘SECTION/SUBSECTION1/SUBSECTION3’, example for QS module:
  ‘FORCE_EVAL/DFT/QS’. This location is used to automatically determine
  if a subsection requires a supersection to be activated.

- **verbose** – Controls how much is printed to CP2K input files (Also
  see Keyword). If True, then a description of the section will be
  printed with it as a comment (if description is set). Default=True.

- **alias** – An alias for this class to use in place of the name.

- **keyword** (*kwargs are interpreted as*)

- **as** (*value pairs and added to the keywords array*)

- **objects**
  (<a href="#pymatgen.io.cp2k.inputs.Keyword" class="reference internal"
  title="pymatgen.io.cp2k.inputs.Keyword"><em>Keyword</em></a>)

</div>

<div id="module-pymatgen.io.cp2k.outputs" class="section">

<span id="pymatgen-io-cp2k-outputs-module"></span>

## pymatgen.io.cp2k.outputs module<a href="#module-pymatgen.io.cp2k.outputs" class="headerlink"
title="Link to this heading"></a>

This module defines the CP2K output parser along with a few other
functions for parsing CP2K-related outputs.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Cp2kOutput</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span>*, *<span class="n"><span class="pre">verbose</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">auto_load</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L39-L1638"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Parse output file from CP2K. The CP2K output file is very flexible in
the way that it is returned. This class will automatically parse
parameters that should always be present, but other parsing features may
be called depending on the run type.

Initialize the Cp2kOutput object.

Parameters<span class="colon">:</span>  
- **filename** – (str) Name of the CP2K output file to parse

- **verbose** – (bool) Whether or not to parse with verbosity (will
  parse lots of data that may not be useful)

- **auto_load** (*bool*) – Whether or not to automatically load basic
  info like energies and structures.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L1608-L1638"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.as_dict"
class="headerlink" title="Link to this definition"></a>  
Return dictionary representation of the output.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">band_structure</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a
href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.bandstructure.BandStructure"
class="reference internal"
title="pymatgen.electronic_structure.bandstructure.BandStructure"><span
class="pre">BandStructure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.band_structure"
class="headerlink" title="Link to this definition"></a>  
Band structure object if it has been parsed.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">calculation_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.calculation_type"
class="headerlink" title="Link to this definition"></a>  
The calculation type (what io.vasp.outputs calls run_type).

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">charge</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.charge" class="headerlink"
title="Link to this definition"></a>  
Charge from the input file.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">complete_dos</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a
href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.dos.CompleteDos"
class="reference internal"
title="pymatgen.electronic_structure.dos.CompleteDos"><span
class="pre">CompleteDos</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.complete_dos"
class="headerlink" title="Link to this definition"></a>  
Complete dos object if it has been parsed.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">completed</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.completed"
class="headerlink" title="Link to this definition"></a>  
Did the calculation complete.

<span class="sig-name descname"><span class="pre">convergence</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L402-L438"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.convergence"
class="headerlink" title="Link to this definition"></a>  
Check whether or not the SCF and geometry optimization cycles converged.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">cp2k_version</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.cp2k_version"
class="headerlink" title="Link to this definition"></a>  
The CP2K version used in the calculation.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">is_hubbard</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.is_hubbard"
class="headerlink" title="Link to this definition"></a>  
True if hubbard +U correction was used.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">is_metal</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.is_metal"
class="headerlink" title="Link to this definition"></a>  
Was a band gap found? i.e. is it a metal.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">is_molecule</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.is_molecule"
class="headerlink" title="Link to this definition"></a>  
True if the CP2K output was generated for a molecule (i.e. no
periodicity in the cell).

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">multiplicity</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.multiplicity"
class="headerlink" title="Link to this definition"></a>  
The spin multiplicity from input file.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">num_warnings</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.num_warnings"
class="headerlink" title="Link to this definition"></a>  
How many warnings showed up during the run.

<span class="sig-name descname"><span class="pre">parse_atomic_kind_info</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L735-L811"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_atomic_kind_info"
class="headerlink" title="Link to this definition"></a>  
Parse info on what atomic kinds are present and what
basis/pseudopotential is describing each of them.

<span class="sig-name descname"><span class="pre">parse_bandstructure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">bandstructure_filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L1268-L1352"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_bandstructure"
class="headerlink" title="Link to this definition"></a>  
Parse a CP2K bandstructure file.

Parameters<span class="colon">:</span>  
- **bandstructure_filename** – Filename containing bandstructure info.
  If

- **provided** (*not*)

- **by** (*then the pmg name* *of* *"BAND.bs" will be assumed*)

- **parser.** (*the filename*)

<span class="sig-name descname"><span class="pre">parse_cell_params</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L701-L733"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_cell_params"
class="headerlink" title="Link to this definition"></a>  
Parse the lattice parameters (initial) from the output file.

<span class="sig-name descname"><span class="pre">parse_chi_tensor</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">chi_filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L1412-L1456"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_chi_tensor"
class="headerlink" title="Link to this definition"></a>  
Parse the magnetic susceptibility tensor.

<span class="sig-name descname"><span class="pre">parse_cp2k_params</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L543-L552"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_cp2k_params"
class="headerlink" title="Link to this definition"></a>  
Parse the CP2K general parameters from CP2K output file into a
dictionary.

<span class="sig-name descname"><span class="pre">parse_dft_params</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L583-L655"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_dft_params"
class="headerlink" title="Link to this definition"></a>  
Parse the DFT parameters (as well as functional, HF, vdW params).

<span class="sig-name descname"><span class="pre">parse_dos</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dos_file</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">pdos_files</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ldos_files</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L1182-L1256"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_dos"
class="headerlink" title="Link to this definition"></a>  
Parse the dos files produced by CP2K calculation. CP2K produces
different files based on the input file rather than assimilating them
all into one file.

One file type is the overall DOS file, which is used for k-point
calculations. For non-kpoint calculation, the overall DOS is generally
not calculated, but the element-projected pDOS is. Separate files are
created for each spin channel and each atom kind. If requested, CP2K can
also do site/local projected dos (ldos). Each site requested will have a
separate file for each spin channel (if spin polarized calculation is
performed).

If possible, this function will assimilate the ldos files into a
CompleteDos object. Either provide a list of PDOS file paths, or use
glob to find the .pdos_ALPHA extension in the calculation directory.

Parameters<span class="colon">:</span>  
- **dos_file** (*str*) – Name of the dos file, otherwise will be
  inferred

- **pdos_files** (*list*) – list of pdos file paths, otherwise they will
  be inferred

- **ldos_files** (*list*) – list of ldos file paths, otherwise they will
  be inferred

<span class="sig-name descname"><span class="pre">parse_energies</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L440-L468"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_energies"
class="headerlink" title="Link to this definition"></a>  
Get the total energy from a CP2K calculation. Presently, the energy
reported in the trajectory (pos.xyz) file takes precedence over the
energy reported in the main output file. This is because the trajectory
file keeps track of energies in between restarts, while the main output
file may or may not depending on whether a particular machine overwrites
or appends it.

<span class="sig-name descname"><span class="pre">parse_files</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L216-L263"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_files"
class="headerlink" title="Link to this definition"></a>  
Identify files present in the directory with the CP2K output file. Looks
for trajectories, dos, and cubes.

<span class="sig-name descname"><span class="pre">parse_forces</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L470-L488"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_forces"
class="headerlink" title="Link to this definition"></a>  
Get the forces from the forces file, or from the main output file.

<span class="sig-name descname"><span class="pre">parse_global_params</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L575-L581"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_global_params"
class="headerlink" title="Link to this definition"></a>  
Parse the GLOBAL section parameters from CP2K output file into a
dictionary.

<span class="sig-name descname"><span class="pre">parse_gtensor</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">gtensor_filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L1375-L1410"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_gtensor"
class="headerlink" title="Link to this definition"></a>  
Parse a file containing g tensor.

<span class="sig-name descname"><span class="pre">parse_hirshfeld</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L955-L1004"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_hirshfeld"
class="headerlink" title="Link to this definition"></a>  
Parse the Hirshfeld population analysis for each step.

<span class="sig-name descname"><span class="pre">parse_homo_lumo</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L1158-L1180"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_homo_lumo"
class="headerlink" title="Link to this definition"></a>  
Find the HOMO - LUMO gap in \[eV\]. Returns the last value. For
gaps/eigenvalues decomposed by spin up/spin down channel and over many
ionic steps, see parse_mo_eigenvalues().

<span class="sig-name descname"><span class="pre">parse_hyperfine</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">hyperfine_filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L1354-L1373"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_hyperfine"
class="headerlink" title="Link to this definition"></a>  
Parse a file containing hyperfine coupling tensors for each atomic site.

<span class="sig-name descname"><span class="pre">parse_initial_structure</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L323-L377"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_initial_structure"
class="headerlink" title="Link to this definition"></a>  
Parse the initial structure from the main CP2K output file.

<span class="sig-name descname"><span class="pre">parse_input</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L564-L573"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_input"
class="headerlink" title="Link to this definition"></a>  
Load in the input set from the input file (if it can be found).

<span class="sig-name descname"><span class="pre">parse_ionic_steps</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L520-L541"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_ionic_steps"
class="headerlink" title="Link to this definition"></a>  
Parse the ionic step info. If already parsed, this will just assimilate.

<span class="sig-name descname"><span class="pre">parse_mo_eigenvalues</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L1006-L1156"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_mo_eigenvalues"
class="headerlink" title="Link to this definition"></a>  
Parse the MO eigenvalues from the CP2K output file. Will get the
eigenvalues (and band gap) at each ionic step (if more than one exist).

Everything is decomposed by spin channel. If calculation was performed
without spin polarization, then only Spin.up will be present, which
represents the average of up and down.

<span class="sig-name descname"><span class="pre">parse_mulliken</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L941-L953"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_mulliken"
class="headerlink" title="Link to this definition"></a>  
Parse the mulliken population analysis info for each step.

<span class="sig-name descname"><span class="pre">parse_nmr_shift</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L1458-L1460"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_nmr_shift"
class="headerlink" title="Link to this definition"></a>  
Parse NMR calculation.

<span class="sig-name descname"><span class="pre">parse_opt_steps</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L889-L939"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_opt_steps"
class="headerlink" title="Link to this definition"></a>  
Parse the geometry optimization information.

<span class="sig-name descname"><span class="pre">parse_overlap_condition</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L675-L683"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_overlap_condition"
class="headerlink" title="Link to this definition"></a>  
Retrieve the overlap condition number.

<span class="sig-name descname"><span class="pre">parse_plus_u\_params</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L554-L562"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_plus_u_params"
class="headerlink" title="Link to this definition"></a>  
Parse the DFT+U params.

<span class="sig-name descname"><span class="pre">parse_qs_params</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L657-L673"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_qs_params"
class="headerlink" title="Link to this definition"></a>  
Parse the DFT parameters (as well as functional, HF, vdW params).

<span class="sig-name descname"><span class="pre">parse_raman</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L1466-L1468"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_raman"
class="headerlink" title="Link to this definition"></a>  
Parse raman calculation.

<span class="sig-name descname"><span class="pre">parse_scf_opt</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L836-L865"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_scf_opt"
class="headerlink" title="Link to this definition"></a>  
Parse the SCF cycles (not usually important).

<span class="sig-name descname"><span class="pre">parse_scf_params</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L685-L699"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_scf_params"
class="headerlink" title="Link to this definition"></a>  
Retrieve the most import SCF parameters: the max number of scf cycles
(max_scf), the convergence cutoff for scf (eps_scf),.

<span class="sig-name descname"><span class="pre">parse_stresses</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L490-L518"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_stresses"
class="headerlink" title="Link to this definition"></a>  
Get the stresses from stress file, or from the main output file.

<span class="sig-name descname"><span class="pre">parse_structures</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">trajectory_file</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">lattice_file</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L265-L321"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_structures"
class="headerlink" title="Link to this definition"></a>  
Parse the structures from a CP2K calculation. Static calculations simply
use the initial structure. For calculations with ionic motion, the
function will look for the appropriate trajectory and lattice files
based on naming convention. If no file is given, and no file is found,
it is assumed that the lattice/structure remained constant, and the
initial lattice/structure is used. CP2K does not output the trajectory
in the main output file by default, so non static calculations have to
reference the trajectory file.

<span class="sig-name descname"><span class="pre">parse_tddfpt</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L1462-L1464"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_tddfpt"
class="headerlink" title="Link to this definition"></a>  
Parse TDDFPT calculation.

<span class="sig-name descname"><span class="pre">parse_timing</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L867-L887"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_timing"
class="headerlink" title="Link to this definition"></a>  
Parse the timing info (how long did the run take).

<span class="sig-name descname"><span class="pre">parse_total_numbers</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L813-L834"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.parse_total_numbers"
class="headerlink" title="Link to this definition"></a>  
Parse total numbers (not usually important).

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">project_name</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.project_name"
class="headerlink" title="Link to this definition"></a>  
What project name was used for this calculation.

<span class="sig-name descname"><span class="pre">ran_successfully</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L379-L400"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.ran_successfully"
class="headerlink" title="Link to this definition"></a>  
Sanity checks that the program ran successfully. Looks at the bottom of
the CP2K output file for the “PROGRAM ENDED” line, which is printed when
successfully ran. Also grabs the number of warnings issued.

<span class="sig-name descname"><span class="pre">read_pattern</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">patterns</span></span>*, *<span class="n"><span class="pre">reverse=False</span></span>*, *<span class="n"><span class="pre">terminate_on_match=False</span></span>*, *<span class="n"><span class="pre">postprocess=\<class</span> <span class="pre">'str'\></span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L1485-L1517"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.read_pattern"
class="headerlink" title="Link to this definition"></a>  
Originally from pymatgen.io.vasp.outputs.Outcar.

General pattern reading. Uses monty’s regrep method. Takes the same
arguments.

Parameters<span class="colon">:</span>  
- **patterns** (*dict*) – A dict of patterns, e.g. {“energy”:
  r”energy\\(sigma-\>0\\)\s+=\s+(\[\d\\-.\]+)”}.

- **reverse** (*bool*) – Read files in reverse. Defaults to false.
  Useful for large files, esp OUTCARs, especially when used with
  terminate_on_match.

- **terminate_on_match** (*bool*) – Whether to terminate when there is
  at least one match in each key in pattern.

- **postprocess** (*callable*) – A post processing function to convert
  all matches. Defaults to str, i.e., no change.

Renders accessible:  
Any attribute in patterns. For example, {“energy”:
r”energy\\(sigma-\>0\\)\s+=\s+(\[\d\\-.\]+)”} will set the value of
self.data\[“energy”\] = \[\[-1234\], \[-3453\], …\], to the results from
regex and postprocess. Note that the returned values are lists of lists,
because you can grep multiple items on one line.

<span class="sig-name descname"><span class="pre">read_table_pattern</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">header_pattern</span></span>*, *<span class="n"><span class="pre">row_pattern</span></span>*, *<span class="n"><span class="pre">footer_pattern</span></span>*, *<span class="n"><span class="pre">postprocess=\<class</span> <span class="pre">'str'\></span></span>*, *<span class="n"><span class="pre">attribute_name=None</span></span>*, *<span class="n"><span class="pre">last_one_only=True</span></span>*, *<span class="n"><span class="pre">strip=None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L1519-L1606"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.read_table_pattern"
class="headerlink" title="Link to this definition"></a>  
This function originated in pymatgen.io.vasp.outputs.Outcar.

Parse table-like data. A table composes of three parts: header, main
body, footer. All the data matches “row pattern” in the main body will
be returned.

Parameters<span class="colon">:</span>  
- **header_pattern** (*str*) – The regular expression pattern matches
  the table header. This pattern should match all the text immediately
  before the main body of the table. For multiple sections table match
  the text until the section of interest. MULTILINE and DOTALL options
  are enforced, as a result, the “.” meta-character will also match “n”
  in this section.

- **row_pattern** (*str*) – The regular expression matches a single line
  in the table. Capture interested field using regular expression
  groups.

- **footer_pattern** (*str*) – The regular expression matches the end of
  the table. E.g. a long dash line.

- **postprocess** (*callable*) – A post processing function to convert
  all matches. Defaults to str, i.e., no change.

- **attribute_name** (*str*) – Name of this table. If present the parsed
  data will be attached to “data. e.g. self.data\[“efg”\] = \[…\]

- **last_one_only** (*bool*) – All the tables will be parsed, if this
  option is set to True, only the last table will be returned. The
  enclosing list will be removed. i.e. Only a single table will be
  returned. Default to be True.

- **strip** (*list*) – Whether or not to strip contents out of the file
  before reading for a table pattern. This is mainly used by
  parse_scf_opt(), to strip HFX info out of the SCF loop start or DFT+U
  warnings out of the SCF loop iterations.

Returns<span class="colon">:</span>  
List of tables. 1) A table is a list of rows. 2) A row if either a list
of attribute values in case the the capturing group is defined without
name in row_pattern, or a dict in case that named capturing groups are
defined by row_pattern.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">run_type</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.run_type"
class="headerlink" title="Link to this definition"></a>  
What type of run (Energy, MD, etc.) was performed.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">spin_polarized</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.Cp2kOutput.spin_polarized"
class="headerlink" title="Link to this definition"></a>  
Was the calculation spin polarized.

<!-- -->

<span class="sig-name descname"><span class="pre">parse_dos</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dos_file</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L1661-L1677"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.parse_dos" class="headerlink"
title="Link to this definition"></a>  
Parse a dos file. This format is different from the pdos files.

<!-- -->

<span class="sig-name descname"><span class="pre">parse_energy_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">energy_file</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L1642-L1657"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.parse_energy_file" class="headerlink"
title="Link to this definition"></a>  
Parse energy file for calculations with multiple ionic steps.

<!-- -->

<span class="sig-name descname"><span class="pre">parse_pdos</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dos_file</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">spin_channel</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">total</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/outputs.py#L1680-L1787"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.outputs.parse_pdos" class="headerlink"
title="Link to this definition"></a>  
Parse a single DOS file created by CP2K. Must contain one PDOS snapshot.
i.e. you cannot use this cannot deal with multiple concatenated dos
files.

Parameters<span class="colon">:</span>  
- **dos_file** (*list*) – list of pdos_ALPHA file paths

- **spin_channel** (*int*) – Which spin channel the file corresponds to.
  By default, CP2K will write the file with ALPHA or BETA in the
  filename (for spin up or down), but you can specify this here, in case
  you have a manual file name. spin_channel == 1 –\> spin up,
  spin_channel == -1 –\> spin down.

- **total** (*bool*) – Whether to grab the total occupations, or the
  orbital decomposed ones.

- **sigma** (*float*) – width for gaussian smearing, if desired

Returns<span class="colon">:</span>  
> <div>
>
> 1.  orbital decomposed DOS dict: i.e. pdoss = {specie: {orbital.s:
>     {Spin.up: … }, orbital.px: {Spin.up: … } …}}
>
> 2.  energy levels of this dos file
>
> 3.  fermi energy (in eV).
>
> </div>

DOS object is not created here

Return type<span class="colon">:</span>  
Everything necessary to create a dos object, in dict format

</div>

<div id="module-pymatgen.io.cp2k.sets" class="section">

<span id="pymatgen-io-cp2k-sets-module"></span>

## pymatgen.io.cp2k.sets module<a href="#module-pymatgen.io.cp2k.sets" class="headerlink"
title="Link to this heading"></a>

This module defines input sets for CP2K and is a work in progress. The
structure/philosophy of this module is based on the Vasp input sets in
Pymatgen. These sets are meant to contain tested parameters that will
result in successful, reproducible, consistent calculations without need
for intervention 99% of the time. 99% of the time, you only need to
provide a pymatgen structure object and let the defaults take over from
there.

The sets are intended to be very general, e.g. a set for geometry
relaxation, and so most of the time, if you have specific needs, you can
simply specify them via the keyword argument override_default_params
(see Section.update() method). If you have the need to create a new
input set (say for a standardized high throughput calculation) then you
can create a new child of the Cp2kInputSet class.

In order to implement a new Set within the current code structure, follow this 3 step flow:  
1.  Inherit from Cp2kInputSet or one of its children and call the
    super() constructor

2.  Create the new sections and insert them into self and its
    subsections as needed

3.  Call self.update(override_default_params) in order to allow user
    settings.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">CellOptSet</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L1438-L1443"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.CellOptSet" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.sets.DftSet" class="reference internal"
title="pymatgen.io.cp2k.sets.DftSet"><span class="pre"><code
class="sourceCode python">DftSet</code></span></a>

Quick Constructor for cell optimization relaxation.

Parameters<span class="colon">:</span>  
- **structure** – Pymatgen structure or molecule object

- **basis_and_potential** (*dict*) – Basis set and pseudo-potential to
  use for each element. See DftSet.get_basis_and_potential for allowed
  formats.

- **element_defaults** (*dict*) – Default settings such as initial
  magnetization for each element. See DftSet.create_subsys for allowed
  formats.

- **ot** (*bool*) – Whether or not to use orbital transformation method
  for matrix diagonalization. OT is the flagship scf solver of CP2K, and
  will provide speed-ups for this part of the calculation, but the
  system must have a band gap for OT to be used (higher band-gap –\>
  faster convergence).

- **energy_gap** (*float*) – Estimate of energy gap for pre-conditioner.
  Default is -1, leaving it up to CP2K.

- **eps_default** (*float*) – Replaces all EPS_XX Keywords in the DFT
  section value, ensuring an overall accuracy of at least this much.

- **eps_scf** (*float*) –

  The convergence criteria for leaving the SCF loop. Default is 1e-6.
  Should ensure reasonable results, but is not applicable to all
  situations.

  > <div>
  >
  > Note: eps_scf is *not* in units of energy, as in most DFT codes. For
  > OT method, it is the largest gradient of the energy with respect to
  > changing any of the molecular orbital coefficients. For
  > diagonalization, it is the largest change in the density matrix from
  > the last step.
  >
  > </div>

- **max_scf** (*int*) – The max number of SCF cycles before terminating
  the solver. NOTE: With the OT solver, this corresponds to the max
  number of INNER scf loops, and then the outer loops are set with
  outer_max_scf, while with diagonalization it corresponds to the
  overall (INNER\*OUTER) number of SCF steps, with the inner loop limit
  set by

- **minimizer** (*str*) – The minimization scheme. DIIS can be as much
  as 50% faster than the more robust conjugate gradient method, and so
  it is chosen as default. Switch to CG if dealing with a difficult
  system.

- **preconditioner** (*str*) – Pre-conditioner for the OT method.
  FULL_SINGLE_INVERSE is very robust and compatible with non-integer
  occupations from IRAC+rotation. FULL_ALL is considered “best” but
  needs algorithm to be set to STRICT. Only change from these two when
  simulation cell gets to be VERY large, in which case FULL_KINETIC
  might be preferred.

- **algorithm** (*str*) – Algorithm for the OT method. STRICT assumes
  that the orbitals are strictly orthogonal to each other, which works
  well for wide gap ionic systems, but can diverge for systems with
  small gaps, fractional occupations, and some other cases. IRAC
  (iterative refinement of the approximate congruency) transformation is
  not analytically correct and uses a truncated polynomial expansion,
  but is robust to the problems with STRICT, and so is the default.

- **linesearch** (*str*) – Linesearch method for CG. 2PNT is the
  default, and is the fastest, but is not as robust as 3PNT. 2PNT is
  required as of CP2K v9.1 for compatibility with irac+rotation. This
  may be upgraded in the future. 3PNT can be good for wide gapped
  transition metal systems as an alternative.

- **rotation** (*bool*) – Whether or not to allow for rotation of the
  orbitals in the OT method. This equates to allowing for fractional
  occupations in the calculation.

- **occupation_preconditioner** (*bool*) – Whether or not to account for
  fractional occupations in the preconditioner. This method is not fully
  integrated as of CP2K v9.1 and is set to false by default.

- **cutoff** (*int*) – Cutoff energy (in Ry) for the finest level of the
  multigrid. A high cutoff will allow you to have very accurate
  calculations PROVIDED that REL_CUTOFF is appropriate. By default
  cutoff is set to 0, leaving it up to the set.

- **rel_cutoff** (*int*) – This cutoff decides how the Gaussians are
  mapped onto the different levels of the multigrid. If REL_CUTOFF is
  too low, then even if you have a high CUTOFF, all Gaussians will be
  mapped onto the coarsest level of the multi-grid, and thus the
  effective integration grid for the calculation may still be too
  coarse. By default 50Ry is chosen, which should be sufficient given
  the cutoff is large enough.

- **ngrids** (*int*) – number of multi-grids to use. CP2K default is 4,
  but the molopt basis files recommend 5.

- **progression_factor** (*int*) – Divisor of CUTOFF to get the cutoff
  for the next level of the multigrid.

- **wfn_restart_file_name** (*str*) – RESTART file for the initial
  wavefunction guess.

- **kpoints**
  (<a href="#pymatgen.io.cp2k.inputs.Kpoints" class="reference internal"
  title="pymatgen.io.cp2k.inputs.Kpoints"><em>Kpoints</em></a>) –
  kpoints object from pymatgen.io.vasp.inputs.Kpoints. By default, CP2K
  runs with gamma point only.

- **smearing** (*bool*) – whether or not to activate smearing (should be
  done for systems containing no (or a very small) band gap.

- **cell** (*dict\[str,* *Any\]*) – Keywords to add to the CELL section
  such as SYMMETRY. See <a
  href="https://manual.cp2k.org/trunk/CP2K_INPUT/FORCE_EVAL/SUBSYS/CELL.html#CP2K_INPUT.FORCE_EVAL.SUBSYS.CELL"
  class="reference external">https://manual.cp2k.org/trunk/CP2K_INPUT/FORCE_EVAL/SUBSYS/CELL.html#CP2K_INPUT.FORCE_EVAL.SUBSYS.CELL</a>

<!-- -->

*<span class="k"><span class="pre">exception</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">Cp2kValidationError</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">message</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L1470-L1481"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.Cp2kValidationError" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`Exception`</span>

CP2K validation exception. Not exhausted. May raise validation errors
for features which actually do work if using a newer version of CP2K.

<span class="sig-name descname"><span class="pre">CP2K_VERSION</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'v2022.1'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/cp2k/sets.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.Cp2kValidationError.CP2K_VERSION"
class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">DftSet</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*, *<span class="n"><span class="pre">project_name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'CP2K'</span></span>*, *<span class="n"><span class="pre">basis_and_potential</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">element_defaults</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">xc_functionals</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">multiplicity</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">ot</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">energy_gap</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">-1</span></span>*, *<span class="n"><span class="pre">qs_method</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'GPW'</span></span>*, *<span class="n"><span class="pre">eps_default</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-12</span></span>*, *<span class="n"><span class="pre">eps_scf</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-06</span></span>*, *<span class="n"><span class="pre">max_scf</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">minimizer</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'DIIS'</span></span>*, *<span class="n"><span class="pre">preconditioner</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'FULL_SINGLE_INVERSE'</span></span>*, *<span class="n"><span class="pre">algorithm</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'IRAC'</span></span>*, *<span class="n"><span class="pre">linesearch</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'2PNT'</span></span>*, *<span class="n"><span class="pre">rotation</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">occupation_preconditioner</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">cutoff</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">rel_cutoff</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">50</span></span>*, *<span class="n"><span class="pre">ngrids</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">5</span></span>*, *<span class="n"><span class="pre">progression_factor</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">3</span></span>*, *<span class="n"><span class="pre">override_default_params</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">wfn_restart_file_name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">kpoints</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.io.vasp.html#pymatgen.io.vasp.inputs.Kpoints"
class="reference internal" title="pymatgen.io.vasp.inputs.Kpoints"><span
class="pre">Kpoints</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">smearing</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">cell</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L83-L1420"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.inputs.Cp2kInput" class="reference internal"
title="pymatgen.io.cp2k.inputs.Cp2kInput"><span class="pre"><code
class="sourceCode python">Cp2kInput</code></span></a>

Base for an input set using the Quickstep module (i.e. a DFT
calculation). The DFT section is pretty vast in CP2K, so this set hopes
to make the DFT setup fairly simple. The provided parameters are pretty
conservative, and so they should not need to be changed very often.

Parameters<span class="colon">:</span>  
- **structure** – Pymatgen structure or molecule object

- **basis_and_potential** (*dict*) – Basis set and pseudo-potential to
  use for each element. See DftSet.get_basis_and_potential for allowed
  formats.

- **element_defaults** (*dict*) – Default settings such as initial
  magnetization for each element. See DftSet.create_subsys for allowed
  formats.

- **ot** (*bool*) – Whether or not to use orbital transformation method
  for matrix diagonalization. OT is the flagship scf solver of CP2K, and
  will provide speed-ups for this part of the calculation, but the
  system must have a band gap for OT to be used (higher band-gap –\>
  faster convergence).

- **energy_gap** (*float*) – Estimate of energy gap for pre-conditioner.
  Default is -1, leaving it up to CP2K.

- **eps_default** (*float*) – Replaces all EPS_XX Keywords in the DFT
  section value, ensuring an overall accuracy of at least this much.

- **eps_scf** (*float*) –

  The convergence criteria for leaving the SCF loop. Default is 1e-6.
  Should ensure reasonable results, but is not applicable to all
  situations.

  > <div>
  >
  > Note: eps_scf is *not* in units of energy, as in most DFT codes. For
  > OT method, it is the largest gradient of the energy with respect to
  > changing any of the molecular orbital coefficients. For
  > diagonalization, it is the largest change in the density matrix from
  > the last step.
  >
  > </div>

- **max_scf** (*int*) – The max number of SCF cycles before terminating
  the solver. NOTE: With the OT solver, this corresponds to the max
  number of INNER scf loops, and then the outer loops are set with
  outer_max_scf, while with diagonalization it corresponds to the
  overall (INNER\*OUTER) number of SCF steps, with the inner loop limit
  set by

- **minimizer** (*str*) – The minimization scheme. DIIS can be as much
  as 50% faster than the more robust conjugate gradient method, and so
  it is chosen as default. Switch to CG if dealing with a difficult
  system.

- **preconditioner** (*str*) – Pre-conditioner for the OT method.
  FULL_SINGLE_INVERSE is very robust and compatible with non-integer
  occupations from IRAC+rotation. FULL_ALL is considered “best” but
  needs algorithm to be set to STRICT. Only change from these two when
  simulation cell gets to be VERY large, in which case FULL_KINETIC
  might be preferred.

- **algorithm** (*str*) – Algorithm for the OT method. STRICT assumes
  that the orbitals are strictly orthogonal to each other, which works
  well for wide gap ionic systems, but can diverge for systems with
  small gaps, fractional occupations, and some other cases. IRAC
  (iterative refinement of the approximate congruency) transformation is
  not analytically correct and uses a truncated polynomial expansion,
  but is robust to the problems with STRICT, and so is the default.

- **linesearch** (*str*) – Linesearch method for CG. 2PNT is the
  default, and is the fastest, but is not as robust as 3PNT. 2PNT is
  required as of CP2K v9.1 for compatibility with irac+rotation. This
  may be upgraded in the future. 3PNT can be good for wide gapped
  transition metal systems as an alternative.

- **rotation** (*bool*) – Whether or not to allow for rotation of the
  orbitals in the OT method. This equates to allowing for fractional
  occupations in the calculation.

- **occupation_preconditioner** (*bool*) – Whether or not to account for
  fractional occupations in the preconditioner. This method is not fully
  integrated as of CP2K v9.1 and is set to false by default.

- **cutoff** (*int*) – Cutoff energy (in Ry) for the finest level of the
  multigrid. A high cutoff will allow you to have very accurate
  calculations PROVIDED that REL_CUTOFF is appropriate. By default
  cutoff is set to 0, leaving it up to the set.

- **rel_cutoff** (*int*) – This cutoff decides how the Gaussians are
  mapped onto the different levels of the multigrid. If REL_CUTOFF is
  too low, then even if you have a high CUTOFF, all Gaussians will be
  mapped onto the coarsest level of the multi-grid, and thus the
  effective integration grid for the calculation may still be too
  coarse. By default 50Ry is chosen, which should be sufficient given
  the cutoff is large enough.

- **ngrids** (*int*) – number of multi-grids to use. CP2K default is 4,
  but the molopt basis files recommend 5.

- **progression_factor** (*int*) – Divisor of CUTOFF to get the cutoff
  for the next level of the multigrid.

- **wfn_restart_file_name** (*str*) – RESTART file for the initial
  wavefunction guess.

- **kpoints**
  (<a href="#pymatgen.io.cp2k.inputs.Kpoints" class="reference internal"
  title="pymatgen.io.cp2k.inputs.Kpoints"><em>Kpoints</em></a>) –
  kpoints object from pymatgen.io.vasp.inputs.Kpoints. By default, CP2K
  runs with gamma point only.

- **smearing** (*bool*) – whether or not to activate smearing (should be
  done for systems containing no (or a very small) band gap.

- **cell** (*dict\[str,* *Any\]*) – Keywords to add to the CELL section
  such as SYMMETRY. See <a
  href="https://manual.cp2k.org/trunk/CP2K_INPUT/FORCE_EVAL/SUBSYS/CELL.html#CP2K_INPUT.FORCE_EVAL.SUBSYS.CELL"
  class="reference external">https://manual.cp2k.org/trunk/CP2K_INPUT/FORCE_EVAL/SUBSYS/CELL.html#CP2K_INPUT.FORCE_EVAL.SUBSYS.CELL</a>

<span class="sig-name descname"><span class="pre">activate_epr</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L1155-L1160"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.activate_epr" class="headerlink"
title="Link to this definition"></a>  
Calculate g-tensor. Requires localize. Suggested with GAPW.

<span class="sig-name descname"><span class="pre">activate_fast_minimization</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">on</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L1246-L1255"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.activate_fast_minimization"
class="headerlink" title="Link to this definition"></a>  
Modify the set to use fast SCF minimization.

<span class="sig-name descname"><span class="pre">activate_hybrid</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">hybrid_functional</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'PBE0'</span></span>*, *<span class="n"><span class="pre">hf_fraction</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.25</span></span>*, *<span class="n"><span class="pre">gga_x\_fraction</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.75</span></span>*, *<span class="n"><span class="pre">gga_c\_fraction</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1</span></span>*, *<span class="n"><span class="pre">max_memory</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">2000</span></span>*, *<span class="n"><span class="pre">cutoff_radius</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">8.0</span></span>*, *<span class="n"><span class="pre">potential_type</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">omega</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.11</span></span>*, *<span class="n"><span class="pre">scale_coulomb</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1</span></span>*, *<span class="n"><span class="pre">scale_gaussian</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1</span></span>*, *<span class="n"><span class="pre">scale_longrange</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1</span></span>*, *<span class="n"><span class="pre">admm</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">admm_method</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'BASIS_PROJECTION'</span></span>*, *<span class="n"><span class="pre">admm_purification_method</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'NONE'</span></span>*, *<span class="n"><span class="pre">admm_exch_correction_func</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'DEFAULT'</span></span>*, *<span class="n"><span class="pre">eps_schwarz</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-07</span></span>*, *<span class="n"><span class="pre">eps_schwarz_forces</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-06</span></span>*, *<span class="n"><span class="pre">screen_on_initial_p</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">screen_p\_forces</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L761-L1021"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.activate_hybrid"
class="headerlink" title="Link to this definition"></a>  
Basic set for activating hybrid DFT calculation using Auxiliary Density
Matrix Method.

Note 1: When running ADMM with CP2K, memory is very important. If the
memory requirements exceed what is available (see max_memory), then CP2K
will have to calculate the 4-electron integrals for HFX during each step
of the SCF cycle. ADMM provides a huge speed up by making the memory
requirements *feasible* to fit into RAM, which means you only need to
calculate the integrals once each SCF cycle. But, this only works if it
fits into memory. When setting up ADMM calculations, we recommend doing
whatever is possible to fit all the 4EI into memory.

Note 2: This set is designed for reliable high-throughput calculations,
NOT for extreme accuracy. Please review the in-line comments in this
method if you want more control.

Parameters<span class="colon">:</span>  
- **hybrid_functional** (*str*) – Type of hybrid functional. This set
  supports HSE (screened) and PBE0 (truncated). Default is PBE0, which
  converges easier in the GPW basis used by CP2K.

- **hf_fraction** (*float*) – fraction of exact HF exchange energy
  to mix. Default: 0.25

- **gga_x\_fraction** (*float*) – fraction of gga exchange energy to
  retain. Default: 0.75

- **gga_c\_fraction** (*float*) – fraction of gga correlation energy to
  retain. Default: 1.0

- **max_memory** (*int*) – Maximum memory available to each MPI process
  (in Mb) in the calculation. Most modern computing nodes will have
  \~2Gb per core, or 2048 Mb, but check for your specific system. This
  value should be as large as possible while still leaving some memory
  for the other parts of CP2K. Important: If this value is set larger
  than the memory limits, CP2K will likely seg-fault. Default: 2000

- **cutoff_radius** (*float*) – for truncated hybrid functional (i.e.
  PBE0), this is the cutoff radius. The default is selected as that
  which generally gives convergence, but maybe too low (if you want very
  high accuracy) or too high (if you want a quick screening). Default: 8
  angstroms

- **potential_type** (*str*) – what interaction potential to use for
  HFX. Available in CP2K are COULOMB, GAUSSIAN, IDENTITY, LOGRANGE,
  MIX_CL, MIX_CL_TRUNC, MIX_LG, SHORTRANGE, and TRUNCATED. Default is
  None, and it will be set automatically depending on the named
  hybrid_functional that you use, but setting it to one of the
  acceptable values will constitute a user-override.

- **omega** (*float*) – For HSE, this specifies the screening parameter.
  HSE06 sets this as 0.2, which is the default.

- **scale_coulomb** – Scale for the coulomb operator if using a range
  separated functional

- **scale_gaussian** – Scale for the gaussian operator (if applicable)

- **scale_longrange** – Scale for the coulomb operator if using a range
  separated functional

- **admm** – Whether or not to use the auxiliary density matrix method
  for the exact HF exchange contribution. Highly recommended. Speed ups
  between 10x and 1000x are possible when compared to non ADMM hybrid
  calculations.

- **admm_method** – Method for constructing the auxiliary basis

- **admm_purification_method** – Method for purifying the auxiliary
  density matrix so as to preserve properties, such as idempotency. May
  lead to shifts in the eigenvalues.

- **admm_exch_correction_func** – Which functional to use to calculate
  the exchange correction E_x(primary) - E_x(aux)

- **eps_schwarz** – Screening threshold for HFX, in Ha. Contributions
  smaller than this will be screened. The smaller the value, the more
  accurate, but also the more costly. Default value is 1e-7. 1e-6 works
  in a large number of cases, but is quite aggressive, which can lead to
  convergence issues.

- **eps_schwarz_forces** – Same as for eps_schwarz, but for screening
  contributions to forces. Convergence is not as sensitive with respect
  to eps_schwarz forces as compared to eps_schwarz, and so 1e-6 should
  be good default.

- **screen_on_initial_p** – If an initial density matrix is provided, in
  the form of a CP2K wfn restart file, then this initial density will be
  used for screening. This is generally very computationally efficient,
  but, as with eps_schwarz, can lead to instabilities if the initial
  density matrix is poor.

- **screen_p\_forces** – Same as screen_on_initial_p, but for screening
  of forces.

<span class="sig-name descname"><span class="pre">activate_hyperfine</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L1183-L1185"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.activate_hyperfine"
class="headerlink" title="Link to this definition"></a>  
Print the hyperfine coupling constants.

<span class="sig-name descname"><span class="pre">activate_localize</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">states</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'OCCUPIED'</span></span>*, *<span class="n"><span class="pre">preconditioner</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'FULL_ALL'</span></span>*, *<span class="n"><span class="pre">restart</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L1187-L1211"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.activate_localize"
class="headerlink" title="Link to this definition"></a>  
Activate calculation of the maximally localized wannier functions.

Parameters<span class="colon">:</span>  
- **states** – Which states to calculate. occupied, unoccupied, mixed
  states, or all states. At present, unoccupied orbitals are only
  implemented for GPW.

- **preconditioner** – Preconditioner to use for optimize

- **restart** – Initialize from the localization restart file

<span class="sig-name descname"><span class="pre">activate_motion</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">max_drift</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.003</span></span>*, *<span class="n"><span class="pre">rms_drift</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.0015</span></span>*, *<span class="n"><span class="pre">max_force</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.00045</span></span>*, *<span class="n"><span class="pre">rms_force</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.0003</span></span>*, *<span class="n"><span class="pre">max_iter</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">200</span></span>*, *<span class="n"><span class="pre">optimizer</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'BFGS'</span></span>*, *<span class="n"><span class="pre">trust_radius</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.25</span></span>*, *<span class="n"><span class="pre">line_search</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'2PNT'</span></span>*, *<span class="n"><span class="pre">ensemble</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'NVE'</span></span>*, *<span class="n"><span class="pre">temperature</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">300</span></span>*, *<span class="n"><span class="pre">timestep</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.5</span></span>*, *<span class="n"><span class="pre">nsteps</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">3</span></span>*, *<span class="n"><span class="pre">thermostat</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'NOSE'</span></span>*, *<span class="n"><span class="pre">nproc_rep</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L1023-L1147"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.activate_motion"
class="headerlink" title="Link to this definition"></a>  
Turns on the motion section for GEO_OPT, CELL_OPT, etc. calculations.
Will turn on the printing subsections and also bind any constraints to
their respective atoms.

<span class="sig-name descname"><span class="pre">activate_nmr</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L1162-L1167"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.activate_nmr" class="headerlink"
title="Link to this definition"></a>  
Calculate nmr shifts. Requires localize. Suggested with GAPW.

<span class="sig-name descname"><span class="pre">activate_nonperiodic</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">solver</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'ANALYTIC'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L1277-L1286"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.activate_nonperiodic"
class="headerlink" title="Link to this definition"></a>  
Activates a calculation with non-periodic calculations by turning of PBC
and changing the poisson solver. Still requires a CELL to put the atoms.

<span class="sig-name descname"><span class="pre">activate_polar</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L1175-L1181"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.activate_polar"
class="headerlink" title="Link to this definition"></a>  
Calculate polarizations (including raman).

<span class="sig-name descname"><span class="pre">activate_robust_minimization</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L1257-L1265"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.activate_robust_minimization"
class="headerlink" title="Link to this definition"></a>  
Modify the set to use more robust SCF minimization technique.

<span class="sig-name descname"><span class="pre">activate_spinspin</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L1169-L1173"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.activate_spinspin"
class="headerlink" title="Link to this definition"></a>  
Calculate spin-spin coupling tensor. Requires localize.

<span class="sig-name descname"><span class="pre">activate_tddfpt</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L1149-L1153"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.activate_tddfpt"
class="headerlink" title="Link to this definition"></a>  
Activate TDDFPT for calculating excited states. Only works with GPW.
Supports hfx.

<span class="sig-name descname"><span class="pre">activate_vdw_potential</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dispersion_functional</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">potential_type</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L1213-L1244"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.activate_vdw_potential"
class="headerlink" title="Link to this definition"></a>  
Activate van der Waals dispersion corrections.

Parameters<span class="colon">:</span>  
- **dispersion_functional** – Type of dispersion functional. Options:
  pair_potential or non_local

- **potential_type** – What type of potential to use, given a dispersion
  functional type Options: DFTD2, DFTD3, DFTD3(BJ), DRSLL, LMKLL, RVV10

<span class="sig-name descname"><span class="pre">activate_very_strict_minimization</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L1267-L1275"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.cp2k.sets.DftSet.activate_very_strict_minimization"
class="headerlink" title="Link to this definition"></a>  
Method to modify the set to use very strict SCF minimization scheme.

<span class="sig-name descname"><span class="pre">create_subsys</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L1288-L1362"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.create_subsys" class="headerlink"
title="Link to this definition"></a>  
Create the structure for the input.

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">get_basis_and_potential</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.IStructure"
class="reference internal"
title="pymatgen.core.structure.IStructure"><span
class="pre">IStructure</span></a></span>*, *<span class="n"><span class="pre">basis_and_potential</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">cp2k_data_dir</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L370-L596"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.get_basis_and_potential"
class="headerlink" title="Link to this definition"></a>  
Get a dictionary of basis and potential info for constructing the input
file.

data in basis_and_potential argument can be specified in several ways:

> <div>
>
> Strategy 1: Element-specific info (takes precedence)
>
> > <div>
> >
> > 1.  Provide a basis and potential object:
> >
> >     > <div>
> >     >
> >     > el: {‘basis’: obj, ‘potential’: obj}
> >     >
> >     > </div>
> >
> > 2.  Provide a hash of the object that matches the keys in the pmg
> >     configured CP2K data files.
> >
> >     > <div>
> >     >
> >     > el: {‘basis’: hash, ‘potential’: hash}
> >     >
> >     > </div>
> >
> > 3\. Provide the name of the basis and potential AND the
> > basis_filenames and potential_filename keywords specifying where to
> > find these objects
> >
> > > <div>
> > >
> > > el: {  
> > > ‘basis’: name, ‘potential’: name, ‘basis_filenames’:
> > > \[filenames\], ‘potential_filename’: filename
> > >
> > > }
> > >
> > > </div>
> >
> > </div>
>
> Strategy 2: global descriptors
>
> > <div>
> >
> > In this case, any elements not present in the argument will be dealt
> > with by searching the pmg configured CP2K data files to find a
> > objects matching your requirements.
> >
> > > <div>
> > >
> > > - functional: Find potential and basis that have been optimized for a specific functional like PBE.  
> > >   Can be None if you do not require them to match.
> > >
> > > - basis_type: type of basis to search for (e.g. DZVP-MOLOPT).
> > >
> > > - aux_basis_type: type of basis to search for (e.g. pFIT). Some elements do not have all aux types  
> > >   available. Use aux_basis_type that is universal to avoid issues,
> > >   or avoid using this strategy.
> > >
> > > - potential_type: “Pseudopotential” or “All Electron”
> > >
> > > </div>
> >
> > **\*BE WARNED\*** CP2K data objects can have the same name, this
> > will sort those and choose the first one that matches.
> >
> > </div>
>
> </div>

Will raise an error if no basis/potential info can be found according to
the input.

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">get_cutoff_from_basis</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">basis_sets</span></span>*, *<span class="n"><span class="pre">rel_cutoff</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L598-L616"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.get_cutoff_from_basis"
class="headerlink" title="Link to this definition"></a>  
Given a basis and a relative cutoff. Determine the ideal cutoff
variable.

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">get_xc_functionals</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">xc_functionals</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L618-L647"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.get_xc_functionals"
class="headerlink" title="Link to this definition"></a>  
Get XC functionals. If simplified names are provided in kwargs, they
will be expanded into their corresponding X and C names.

<span class="sig-name descname"><span class="pre">modify_dft_print_iters</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">iters</span></span>*, *<span class="n"><span class="pre">add_last</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Literal</span><span class="p"><span class="pre">\[</span></span><span class="s"><span class="pre">'no'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'numeric'</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="s"><span class="pre">'symbolic'</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'no'</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L1364-L1407"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.modify_dft_print_iters"
class="headerlink" title="Link to this definition"></a>  
Modify all DFT print iterations at once. Common use is to set iters to
the max number of iterations + 1 and then set add_last to numeric. This
would have the effect of printing only the first and last iteration,
which might be useful for speeding up/saving space on GEO_OPT or MD runs
where you don’t need the intermediate values.

Parameters<span class="colon">:</span>  
- **iters** (*int*) – print each “iters” iterations.

- **add_last** (*str*) – Whether to explicitly include the last
  iteration, and how to mark it. numeric: mark last iteration with the
  iteration number symbolic: mark last iteration with the letter “l” no:
  do not explicitly include the last iteration

<span class="sig-name descname"><span class="pre">print_bandstructure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">kpoints_line_density</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">20</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L729-L745"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.print_bandstructure"
class="headerlink" title="Link to this definition"></a>  
Attaches a non-scf band structure calc the end of an SCF loop.

This requires a kpoint calculation, which is not always default in CP2K.

Parameters<span class="colon">:</span>  
**kpoints_line_density** – number of kpoints along each branch in
line-mode calc.

<span class="sig-name descname"><span class="pre">print_dos</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">ndigits</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">6</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L663-L671"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.print_dos" class="headerlink"
title="Link to this definition"></a>  
Activate printing of the overall DOS file.

Note: As of 2022.1, ndigits needs to be set to a sufficient value to
ensure data is not lost. Note: As of 2022.1, can only be used with a
k-point calculation.

<span class="sig-name descname"><span class="pre">print_e\_density</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">stride</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(2,</span> <span class="pre">2,</span> <span class="pre">2)</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L724-L727"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.print_e_density"
class="headerlink" title="Link to this definition"></a>  
Controls the printing of cube files with electronic density and, for
UKS, the spin density.

<span class="sig-name descname"><span class="pre">print_forces</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L657-L661"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.print_forces" class="headerlink"
title="Link to this definition"></a>  
Print out the forces and stress during calculation.

<span class="sig-name descname"><span class="pre">print_hirshfeld</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">on</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L747-L750"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.print_hirshfeld"
class="headerlink" title="Link to this definition"></a>  
Activate or deactivate printing of Hirshfeld charges.

<span class="sig-name descname"><span class="pre">print_ldos</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">nlumo</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">-1</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L685-L697"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.print_ldos" class="headerlink"
title="Link to this definition"></a>  
Activate the printing of LDOS files, printing one for each atom kind by
default.

Parameters<span class="colon">:</span>  
**nlumo** (*int*) – Number of virtual orbitals to be added to the MO set
(-1=all). CAUTION: Setting this value to be higher than the number of
states present may cause a Cholesky error.

<span class="sig-name descname"><span class="pre">print_mo</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L711-L713"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.print_mo" class="headerlink"
title="Link to this definition"></a>  
Print molecular orbitals when running non-OT diagonalization.

<span class="sig-name descname"><span class="pre">print_mo_cubes</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">write_cube</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">nlumo</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">-1</span></span>*, *<span class="n"><span class="pre">nhomo</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">-1</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L699-L709"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.print_mo_cubes"
class="headerlink" title="Link to this definition"></a>  
Activate printing of molecular orbitals.

Parameters<span class="colon">:</span>  
- **write_cube** (*bool*) – whether to write cube file for the MOs
  instead of out file

- **nlumo** (*int*) – Controls the number of lumos printed and dumped as
  a cube (-1=all)

- **nhomo** (*int*) – Controls the number of homos printed and dumped as
  a cube (-1=all)

<span class="sig-name descname"><span class="pre">print_mulliken</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">on</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L752-L755"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.print_mulliken"
class="headerlink" title="Link to this definition"></a>  
Activate or deactivate printing of Mulliken charges.

<span class="sig-name descname"><span class="pre">print_pdos</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">nlumo</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">-1</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L673-L683"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.print_pdos" class="headerlink"
title="Link to this definition"></a>  
Activate creation of the PDOS file.

Parameters<span class="colon">:</span>  
**nlumo** (*int*) – Number of virtual orbitals to be added to the MO set
(-1=all). CAUTION: Setting this value to be higher than the number of
states present may cause a Cholesky error.

<span class="sig-name descname"><span class="pre">print_v\_hartree</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">stride</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(2,</span> <span class="pre">2,</span> <span class="pre">2)</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L715-L722"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.print_v_hartree"
class="headerlink" title="Link to this definition"></a>  
Controls the printing of a cube file with electrostatic potential generated by the  
total density (electrons+ions). It is valid only for QS with GPW
formalism.

Note that by convention the potential has opposite sign than the
expected physical one.

<span class="sig-name descname"><span class="pre">set_charge</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">charge</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L757-L759"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.set_charge" class="headerlink"
title="Link to this definition"></a>  
Set the overall charge of the simulation cell.

<span class="sig-name descname"><span class="pre">validate</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L1409-L1420"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.validate" class="headerlink"
title="Link to this definition"></a>  
Implements a few checks for a valid input set.

<span class="sig-name descname"><span class="pre">write_basis_set_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">basis_sets</span></span>*, *<span class="n"><span class="pre">fn</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'BASIS'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L649-L651"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.write_basis_set_file"
class="headerlink" title="Link to this definition"></a>  
Write the basis sets to a file.

<span class="sig-name descname"><span class="pre">write_potential_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">potentials</span></span>*, *<span class="n"><span class="pre">fn</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'POTENTIAL'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L653-L655"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.DftSet.write_potential_file"
class="headerlink" title="Link to this definition"></a>  
Write the potentials to a file.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">HybridCellOptSet</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L1462-L1467"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.HybridCellOptSet" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.sets.DftSet" class="reference internal"
title="pymatgen.io.cp2k.sets.DftSet"><span class="pre"><code
class="sourceCode python">DftSet</code></span></a>

Quick Constructor for hybrid cell optimization relaxation.

Parameters<span class="colon">:</span>  
- **structure** – Pymatgen structure or molecule object

- **basis_and_potential** (*dict*) – Basis set and pseudo-potential to
  use for each element. See DftSet.get_basis_and_potential for allowed
  formats.

- **element_defaults** (*dict*) – Default settings such as initial
  magnetization for each element. See DftSet.create_subsys for allowed
  formats.

- **ot** (*bool*) – Whether or not to use orbital transformation method
  for matrix diagonalization. OT is the flagship scf solver of CP2K, and
  will provide speed-ups for this part of the calculation, but the
  system must have a band gap for OT to be used (higher band-gap –\>
  faster convergence).

- **energy_gap** (*float*) – Estimate of energy gap for pre-conditioner.
  Default is -1, leaving it up to CP2K.

- **eps_default** (*float*) – Replaces all EPS_XX Keywords in the DFT
  section value, ensuring an overall accuracy of at least this much.

- **eps_scf** (*float*) –

  The convergence criteria for leaving the SCF loop. Default is 1e-6.
  Should ensure reasonable results, but is not applicable to all
  situations.

  > <div>
  >
  > Note: eps_scf is *not* in units of energy, as in most DFT codes. For
  > OT method, it is the largest gradient of the energy with respect to
  > changing any of the molecular orbital coefficients. For
  > diagonalization, it is the largest change in the density matrix from
  > the last step.
  >
  > </div>

- **max_scf** (*int*) – The max number of SCF cycles before terminating
  the solver. NOTE: With the OT solver, this corresponds to the max
  number of INNER scf loops, and then the outer loops are set with
  outer_max_scf, while with diagonalization it corresponds to the
  overall (INNER\*OUTER) number of SCF steps, with the inner loop limit
  set by

- **minimizer** (*str*) – The minimization scheme. DIIS can be as much
  as 50% faster than the more robust conjugate gradient method, and so
  it is chosen as default. Switch to CG if dealing with a difficult
  system.

- **preconditioner** (*str*) – Pre-conditioner for the OT method.
  FULL_SINGLE_INVERSE is very robust and compatible with non-integer
  occupations from IRAC+rotation. FULL_ALL is considered “best” but
  needs algorithm to be set to STRICT. Only change from these two when
  simulation cell gets to be VERY large, in which case FULL_KINETIC
  might be preferred.

- **algorithm** (*str*) – Algorithm for the OT method. STRICT assumes
  that the orbitals are strictly orthogonal to each other, which works
  well for wide gap ionic systems, but can diverge for systems with
  small gaps, fractional occupations, and some other cases. IRAC
  (iterative refinement of the approximate congruency) transformation is
  not analytically correct and uses a truncated polynomial expansion,
  but is robust to the problems with STRICT, and so is the default.

- **linesearch** (*str*) – Linesearch method for CG. 2PNT is the
  default, and is the fastest, but is not as robust as 3PNT. 2PNT is
  required as of CP2K v9.1 for compatibility with irac+rotation. This
  may be upgraded in the future. 3PNT can be good for wide gapped
  transition metal systems as an alternative.

- **rotation** (*bool*) – Whether or not to allow for rotation of the
  orbitals in the OT method. This equates to allowing for fractional
  occupations in the calculation.

- **occupation_preconditioner** (*bool*) – Whether or not to account for
  fractional occupations in the preconditioner. This method is not fully
  integrated as of CP2K v9.1 and is set to false by default.

- **cutoff** (*int*) – Cutoff energy (in Ry) for the finest level of the
  multigrid. A high cutoff will allow you to have very accurate
  calculations PROVIDED that REL_CUTOFF is appropriate. By default
  cutoff is set to 0, leaving it up to the set.

- **rel_cutoff** (*int*) – This cutoff decides how the Gaussians are
  mapped onto the different levels of the multigrid. If REL_CUTOFF is
  too low, then even if you have a high CUTOFF, all Gaussians will be
  mapped onto the coarsest level of the multi-grid, and thus the
  effective integration grid for the calculation may still be too
  coarse. By default 50Ry is chosen, which should be sufficient given
  the cutoff is large enough.

- **ngrids** (*int*) – number of multi-grids to use. CP2K default is 4,
  but the molopt basis files recommend 5.

- **progression_factor** (*int*) – Divisor of CUTOFF to get the cutoff
  for the next level of the multigrid.

- **wfn_restart_file_name** (*str*) – RESTART file for the initial
  wavefunction guess.

- **kpoints**
  (<a href="#pymatgen.io.cp2k.inputs.Kpoints" class="reference internal"
  title="pymatgen.io.cp2k.inputs.Kpoints"><em>Kpoints</em></a>) –
  kpoints object from pymatgen.io.vasp.inputs.Kpoints. By default, CP2K
  runs with gamma point only.

- **smearing** (*bool*) – whether or not to activate smearing (should be
  done for systems containing no (or a very small) band gap.

- **cell** (*dict\[str,* *Any\]*) – Keywords to add to the CELL section
  such as SYMMETRY. See <a
  href="https://manual.cp2k.org/trunk/CP2K_INPUT/FORCE_EVAL/SUBSYS/CELL.html#CP2K_INPUT.FORCE_EVAL.SUBSYS.CELL"
  class="reference external">https://manual.cp2k.org/trunk/CP2K_INPUT/FORCE_EVAL/SUBSYS/CELL.html#CP2K_INPUT.FORCE_EVAL.SUBSYS.CELL</a>

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">HybridRelaxSet</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L1454-L1459"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.HybridRelaxSet" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.sets.DftSet" class="reference internal"
title="pymatgen.io.cp2k.sets.DftSet"><span class="pre"><code
class="sourceCode python">DftSet</code></span></a>

Quick Constructor for hybrid geometry relaxation.

Parameters<span class="colon">:</span>  
- **structure** – Pymatgen structure or molecule object

- **basis_and_potential** (*dict*) – Basis set and pseudo-potential to
  use for each element. See DftSet.get_basis_and_potential for allowed
  formats.

- **element_defaults** (*dict*) – Default settings such as initial
  magnetization for each element. See DftSet.create_subsys for allowed
  formats.

- **ot** (*bool*) – Whether or not to use orbital transformation method
  for matrix diagonalization. OT is the flagship scf solver of CP2K, and
  will provide speed-ups for this part of the calculation, but the
  system must have a band gap for OT to be used (higher band-gap –\>
  faster convergence).

- **energy_gap** (*float*) – Estimate of energy gap for pre-conditioner.
  Default is -1, leaving it up to CP2K.

- **eps_default** (*float*) – Replaces all EPS_XX Keywords in the DFT
  section value, ensuring an overall accuracy of at least this much.

- **eps_scf** (*float*) –

  The convergence criteria for leaving the SCF loop. Default is 1e-6.
  Should ensure reasonable results, but is not applicable to all
  situations.

  > <div>
  >
  > Note: eps_scf is *not* in units of energy, as in most DFT codes. For
  > OT method, it is the largest gradient of the energy with respect to
  > changing any of the molecular orbital coefficients. For
  > diagonalization, it is the largest change in the density matrix from
  > the last step.
  >
  > </div>

- **max_scf** (*int*) – The max number of SCF cycles before terminating
  the solver. NOTE: With the OT solver, this corresponds to the max
  number of INNER scf loops, and then the outer loops are set with
  outer_max_scf, while with diagonalization it corresponds to the
  overall (INNER\*OUTER) number of SCF steps, with the inner loop limit
  set by

- **minimizer** (*str*) – The minimization scheme. DIIS can be as much
  as 50% faster than the more robust conjugate gradient method, and so
  it is chosen as default. Switch to CG if dealing with a difficult
  system.

- **preconditioner** (*str*) – Pre-conditioner for the OT method.
  FULL_SINGLE_INVERSE is very robust and compatible with non-integer
  occupations from IRAC+rotation. FULL_ALL is considered “best” but
  needs algorithm to be set to STRICT. Only change from these two when
  simulation cell gets to be VERY large, in which case FULL_KINETIC
  might be preferred.

- **algorithm** (*str*) – Algorithm for the OT method. STRICT assumes
  that the orbitals are strictly orthogonal to each other, which works
  well for wide gap ionic systems, but can diverge for systems with
  small gaps, fractional occupations, and some other cases. IRAC
  (iterative refinement of the approximate congruency) transformation is
  not analytically correct and uses a truncated polynomial expansion,
  but is robust to the problems with STRICT, and so is the default.

- **linesearch** (*str*) – Linesearch method for CG. 2PNT is the
  default, and is the fastest, but is not as robust as 3PNT. 2PNT is
  required as of CP2K v9.1 for compatibility with irac+rotation. This
  may be upgraded in the future. 3PNT can be good for wide gapped
  transition metal systems as an alternative.

- **rotation** (*bool*) – Whether or not to allow for rotation of the
  orbitals in the OT method. This equates to allowing for fractional
  occupations in the calculation.

- **occupation_preconditioner** (*bool*) – Whether or not to account for
  fractional occupations in the preconditioner. This method is not fully
  integrated as of CP2K v9.1 and is set to false by default.

- **cutoff** (*int*) – Cutoff energy (in Ry) for the finest level of the
  multigrid. A high cutoff will allow you to have very accurate
  calculations PROVIDED that REL_CUTOFF is appropriate. By default
  cutoff is set to 0, leaving it up to the set.

- **rel_cutoff** (*int*) – This cutoff decides how the Gaussians are
  mapped onto the different levels of the multigrid. If REL_CUTOFF is
  too low, then even if you have a high CUTOFF, all Gaussians will be
  mapped onto the coarsest level of the multi-grid, and thus the
  effective integration grid for the calculation may still be too
  coarse. By default 50Ry is chosen, which should be sufficient given
  the cutoff is large enough.

- **ngrids** (*int*) – number of multi-grids to use. CP2K default is 4,
  but the molopt basis files recommend 5.

- **progression_factor** (*int*) – Divisor of CUTOFF to get the cutoff
  for the next level of the multigrid.

- **wfn_restart_file_name** (*str*) – RESTART file for the initial
  wavefunction guess.

- **kpoints**
  (<a href="#pymatgen.io.cp2k.inputs.Kpoints" class="reference internal"
  title="pymatgen.io.cp2k.inputs.Kpoints"><em>Kpoints</em></a>) –
  kpoints object from pymatgen.io.vasp.inputs.Kpoints. By default, CP2K
  runs with gamma point only.

- **smearing** (*bool*) – whether or not to activate smearing (should be
  done for systems containing no (or a very small) band gap.

- **cell** (*dict\[str,* *Any\]*) – Keywords to add to the CELL section
  such as SYMMETRY. See <a
  href="https://manual.cp2k.org/trunk/CP2K_INPUT/FORCE_EVAL/SUBSYS/CELL.html#CP2K_INPUT.FORCE_EVAL.SUBSYS.CELL"
  class="reference external">https://manual.cp2k.org/trunk/CP2K_INPUT/FORCE_EVAL/SUBSYS/CELL.html#CP2K_INPUT.FORCE_EVAL.SUBSYS.CELL</a>

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">HybridStaticSet</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L1446-L1451"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.HybridStaticSet" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.sets.DftSet" class="reference internal"
title="pymatgen.io.cp2k.sets.DftSet"><span class="pre"><code
class="sourceCode python">DftSet</code></span></a>

Quick Constructor for static calculations.

Parameters<span class="colon">:</span>  
- **structure** – Pymatgen structure or molecule object

- **basis_and_potential** (*dict*) – Basis set and pseudo-potential to
  use for each element. See DftSet.get_basis_and_potential for allowed
  formats.

- **element_defaults** (*dict*) – Default settings such as initial
  magnetization for each element. See DftSet.create_subsys for allowed
  formats.

- **ot** (*bool*) – Whether or not to use orbital transformation method
  for matrix diagonalization. OT is the flagship scf solver of CP2K, and
  will provide speed-ups for this part of the calculation, but the
  system must have a band gap for OT to be used (higher band-gap –\>
  faster convergence).

- **energy_gap** (*float*) – Estimate of energy gap for pre-conditioner.
  Default is -1, leaving it up to CP2K.

- **eps_default** (*float*) – Replaces all EPS_XX Keywords in the DFT
  section value, ensuring an overall accuracy of at least this much.

- **eps_scf** (*float*) –

  The convergence criteria for leaving the SCF loop. Default is 1e-6.
  Should ensure reasonable results, but is not applicable to all
  situations.

  > <div>
  >
  > Note: eps_scf is *not* in units of energy, as in most DFT codes. For
  > OT method, it is the largest gradient of the energy with respect to
  > changing any of the molecular orbital coefficients. For
  > diagonalization, it is the largest change in the density matrix from
  > the last step.
  >
  > </div>

- **max_scf** (*int*) – The max number of SCF cycles before terminating
  the solver. NOTE: With the OT solver, this corresponds to the max
  number of INNER scf loops, and then the outer loops are set with
  outer_max_scf, while with diagonalization it corresponds to the
  overall (INNER\*OUTER) number of SCF steps, with the inner loop limit
  set by

- **minimizer** (*str*) – The minimization scheme. DIIS can be as much
  as 50% faster than the more robust conjugate gradient method, and so
  it is chosen as default. Switch to CG if dealing with a difficult
  system.

- **preconditioner** (*str*) – Pre-conditioner for the OT method.
  FULL_SINGLE_INVERSE is very robust and compatible with non-integer
  occupations from IRAC+rotation. FULL_ALL is considered “best” but
  needs algorithm to be set to STRICT. Only change from these two when
  simulation cell gets to be VERY large, in which case FULL_KINETIC
  might be preferred.

- **algorithm** (*str*) – Algorithm for the OT method. STRICT assumes
  that the orbitals are strictly orthogonal to each other, which works
  well for wide gap ionic systems, but can diverge for systems with
  small gaps, fractional occupations, and some other cases. IRAC
  (iterative refinement of the approximate congruency) transformation is
  not analytically correct and uses a truncated polynomial expansion,
  but is robust to the problems with STRICT, and so is the default.

- **linesearch** (*str*) – Linesearch method for CG. 2PNT is the
  default, and is the fastest, but is not as robust as 3PNT. 2PNT is
  required as of CP2K v9.1 for compatibility with irac+rotation. This
  may be upgraded in the future. 3PNT can be good for wide gapped
  transition metal systems as an alternative.

- **rotation** (*bool*) – Whether or not to allow for rotation of the
  orbitals in the OT method. This equates to allowing for fractional
  occupations in the calculation.

- **occupation_preconditioner** (*bool*) – Whether or not to account for
  fractional occupations in the preconditioner. This method is not fully
  integrated as of CP2K v9.1 and is set to false by default.

- **cutoff** (*int*) – Cutoff energy (in Ry) for the finest level of the
  multigrid. A high cutoff will allow you to have very accurate
  calculations PROVIDED that REL_CUTOFF is appropriate. By default
  cutoff is set to 0, leaving it up to the set.

- **rel_cutoff** (*int*) – This cutoff decides how the Gaussians are
  mapped onto the different levels of the multigrid. If REL_CUTOFF is
  too low, then even if you have a high CUTOFF, all Gaussians will be
  mapped onto the coarsest level of the multi-grid, and thus the
  effective integration grid for the calculation may still be too
  coarse. By default 50Ry is chosen, which should be sufficient given
  the cutoff is large enough.

- **ngrids** (*int*) – number of multi-grids to use. CP2K default is 4,
  but the molopt basis files recommend 5.

- **progression_factor** (*int*) – Divisor of CUTOFF to get the cutoff
  for the next level of the multigrid.

- **wfn_restart_file_name** (*str*) – RESTART file for the initial
  wavefunction guess.

- **kpoints**
  (<a href="#pymatgen.io.cp2k.inputs.Kpoints" class="reference internal"
  title="pymatgen.io.cp2k.inputs.Kpoints"><em>Kpoints</em></a>) –
  kpoints object from pymatgen.io.vasp.inputs.Kpoints. By default, CP2K
  runs with gamma point only.

- **smearing** (*bool*) – whether or not to activate smearing (should be
  done for systems containing no (or a very small) band gap.

- **cell** (*dict\[str,* *Any\]*) – Keywords to add to the CELL section
  such as SYMMETRY. See <a
  href="https://manual.cp2k.org/trunk/CP2K_INPUT/FORCE_EVAL/SUBSYS/CELL.html#CP2K_INPUT.FORCE_EVAL.SUBSYS.CELL"
  class="reference external">https://manual.cp2k.org/trunk/CP2K_INPUT/FORCE_EVAL/SUBSYS/CELL.html#CP2K_INPUT.FORCE_EVAL.SUBSYS.CELL</a>

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">RelaxSet</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L1430-L1435"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.RelaxSet" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.sets.DftSet" class="reference internal"
title="pymatgen.io.cp2k.sets.DftSet"><span class="pre"><code
class="sourceCode python">DftSet</code></span></a>

Quick Constructor for geometry relaxation.

Parameters<span class="colon">:</span>  
- **structure** – Pymatgen structure or molecule object

- **basis_and_potential** (*dict*) – Basis set and pseudo-potential to
  use for each element. See DftSet.get_basis_and_potential for allowed
  formats.

- **element_defaults** (*dict*) – Default settings such as initial
  magnetization for each element. See DftSet.create_subsys for allowed
  formats.

- **ot** (*bool*) – Whether or not to use orbital transformation method
  for matrix diagonalization. OT is the flagship scf solver of CP2K, and
  will provide speed-ups for this part of the calculation, but the
  system must have a band gap for OT to be used (higher band-gap –\>
  faster convergence).

- **energy_gap** (*float*) – Estimate of energy gap for pre-conditioner.
  Default is -1, leaving it up to CP2K.

- **eps_default** (*float*) – Replaces all EPS_XX Keywords in the DFT
  section value, ensuring an overall accuracy of at least this much.

- **eps_scf** (*float*) –

  The convergence criteria for leaving the SCF loop. Default is 1e-6.
  Should ensure reasonable results, but is not applicable to all
  situations.

  > <div>
  >
  > Note: eps_scf is *not* in units of energy, as in most DFT codes. For
  > OT method, it is the largest gradient of the energy with respect to
  > changing any of the molecular orbital coefficients. For
  > diagonalization, it is the largest change in the density matrix from
  > the last step.
  >
  > </div>

- **max_scf** (*int*) – The max number of SCF cycles before terminating
  the solver. NOTE: With the OT solver, this corresponds to the max
  number of INNER scf loops, and then the outer loops are set with
  outer_max_scf, while with diagonalization it corresponds to the
  overall (INNER\*OUTER) number of SCF steps, with the inner loop limit
  set by

- **minimizer** (*str*) – The minimization scheme. DIIS can be as much
  as 50% faster than the more robust conjugate gradient method, and so
  it is chosen as default. Switch to CG if dealing with a difficult
  system.

- **preconditioner** (*str*) – Pre-conditioner for the OT method.
  FULL_SINGLE_INVERSE is very robust and compatible with non-integer
  occupations from IRAC+rotation. FULL_ALL is considered “best” but
  needs algorithm to be set to STRICT. Only change from these two when
  simulation cell gets to be VERY large, in which case FULL_KINETIC
  might be preferred.

- **algorithm** (*str*) – Algorithm for the OT method. STRICT assumes
  that the orbitals are strictly orthogonal to each other, which works
  well for wide gap ionic systems, but can diverge for systems with
  small gaps, fractional occupations, and some other cases. IRAC
  (iterative refinement of the approximate congruency) transformation is
  not analytically correct and uses a truncated polynomial expansion,
  but is robust to the problems with STRICT, and so is the default.

- **linesearch** (*str*) – Linesearch method for CG. 2PNT is the
  default, and is the fastest, but is not as robust as 3PNT. 2PNT is
  required as of CP2K v9.1 for compatibility with irac+rotation. This
  may be upgraded in the future. 3PNT can be good for wide gapped
  transition metal systems as an alternative.

- **rotation** (*bool*) – Whether or not to allow for rotation of the
  orbitals in the OT method. This equates to allowing for fractional
  occupations in the calculation.

- **occupation_preconditioner** (*bool*) – Whether or not to account for
  fractional occupations in the preconditioner. This method is not fully
  integrated as of CP2K v9.1 and is set to false by default.

- **cutoff** (*int*) – Cutoff energy (in Ry) for the finest level of the
  multigrid. A high cutoff will allow you to have very accurate
  calculations PROVIDED that REL_CUTOFF is appropriate. By default
  cutoff is set to 0, leaving it up to the set.

- **rel_cutoff** (*int*) – This cutoff decides how the Gaussians are
  mapped onto the different levels of the multigrid. If REL_CUTOFF is
  too low, then even if you have a high CUTOFF, all Gaussians will be
  mapped onto the coarsest level of the multi-grid, and thus the
  effective integration grid for the calculation may still be too
  coarse. By default 50Ry is chosen, which should be sufficient given
  the cutoff is large enough.

- **ngrids** (*int*) – number of multi-grids to use. CP2K default is 4,
  but the molopt basis files recommend 5.

- **progression_factor** (*int*) – Divisor of CUTOFF to get the cutoff
  for the next level of the multigrid.

- **wfn_restart_file_name** (*str*) – RESTART file for the initial
  wavefunction guess.

- **kpoints**
  (<a href="#pymatgen.io.cp2k.inputs.Kpoints" class="reference internal"
  title="pymatgen.io.cp2k.inputs.Kpoints"><em>Kpoints</em></a>) –
  kpoints object from pymatgen.io.vasp.inputs.Kpoints. By default, CP2K
  runs with gamma point only.

- **smearing** (*bool*) – whether or not to activate smearing (should be
  done for systems containing no (or a very small) band gap.

- **cell** (*dict\[str,* *Any\]*) – Keywords to add to the CELL section
  such as SYMMETRY. See <a
  href="https://manual.cp2k.org/trunk/CP2K_INPUT/FORCE_EVAL/SUBSYS/CELL.html#CP2K_INPUT.FORCE_EVAL.SUBSYS.CELL"
  class="reference external">https://manual.cp2k.org/trunk/CP2K_INPUT/FORCE_EVAL/SUBSYS/CELL.html#CP2K_INPUT.FORCE_EVAL.SUBSYS.CELL</a>

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">StaticSet</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/sets.py#L1423-L1427"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.sets.StaticSet" class="headerlink"
title="Link to this definition"></a>  
Bases:
<a href="#pymatgen.io.cp2k.sets.DftSet" class="reference internal"
title="pymatgen.io.cp2k.sets.DftSet"><span class="pre"><code
class="sourceCode python">DftSet</code></span></a>

Quick Constructor for static calculations.

Parameters<span class="colon">:</span>  
- **structure** – Pymatgen structure or molecule object

- **basis_and_potential** (*dict*) – Basis set and pseudo-potential to
  use for each element. See DftSet.get_basis_and_potential for allowed
  formats.

- **element_defaults** (*dict*) – Default settings such as initial
  magnetization for each element. See DftSet.create_subsys for allowed
  formats.

- **ot** (*bool*) – Whether or not to use orbital transformation method
  for matrix diagonalization. OT is the flagship scf solver of CP2K, and
  will provide speed-ups for this part of the calculation, but the
  system must have a band gap for OT to be used (higher band-gap –\>
  faster convergence).

- **energy_gap** (*float*) – Estimate of energy gap for pre-conditioner.
  Default is -1, leaving it up to CP2K.

- **eps_default** (*float*) – Replaces all EPS_XX Keywords in the DFT
  section value, ensuring an overall accuracy of at least this much.

- **eps_scf** (*float*) –

  The convergence criteria for leaving the SCF loop. Default is 1e-6.
  Should ensure reasonable results, but is not applicable to all
  situations.

  > <div>
  >
  > Note: eps_scf is *not* in units of energy, as in most DFT codes. For
  > OT method, it is the largest gradient of the energy with respect to
  > changing any of the molecular orbital coefficients. For
  > diagonalization, it is the largest change in the density matrix from
  > the last step.
  >
  > </div>

- **max_scf** (*int*) – The max number of SCF cycles before terminating
  the solver. NOTE: With the OT solver, this corresponds to the max
  number of INNER scf loops, and then the outer loops are set with
  outer_max_scf, while with diagonalization it corresponds to the
  overall (INNER\*OUTER) number of SCF steps, with the inner loop limit
  set by

- **minimizer** (*str*) – The minimization scheme. DIIS can be as much
  as 50% faster than the more robust conjugate gradient method, and so
  it is chosen as default. Switch to CG if dealing with a difficult
  system.

- **preconditioner** (*str*) – Pre-conditioner for the OT method.
  FULL_SINGLE_INVERSE is very robust and compatible with non-integer
  occupations from IRAC+rotation. FULL_ALL is considered “best” but
  needs algorithm to be set to STRICT. Only change from these two when
  simulation cell gets to be VERY large, in which case FULL_KINETIC
  might be preferred.

- **algorithm** (*str*) – Algorithm for the OT method. STRICT assumes
  that the orbitals are strictly orthogonal to each other, which works
  well for wide gap ionic systems, but can diverge for systems with
  small gaps, fractional occupations, and some other cases. IRAC
  (iterative refinement of the approximate congruency) transformation is
  not analytically correct and uses a truncated polynomial expansion,
  but is robust to the problems with STRICT, and so is the default.

- **linesearch** (*str*) – Linesearch method for CG. 2PNT is the
  default, and is the fastest, but is not as robust as 3PNT. 2PNT is
  required as of CP2K v9.1 for compatibility with irac+rotation. This
  may be upgraded in the future. 3PNT can be good for wide gapped
  transition metal systems as an alternative.

- **rotation** (*bool*) – Whether or not to allow for rotation of the
  orbitals in the OT method. This equates to allowing for fractional
  occupations in the calculation.

- **occupation_preconditioner** (*bool*) – Whether or not to account for
  fractional occupations in the preconditioner. This method is not fully
  integrated as of CP2K v9.1 and is set to false by default.

- **cutoff** (*int*) – Cutoff energy (in Ry) for the finest level of the
  multigrid. A high cutoff will allow you to have very accurate
  calculations PROVIDED that REL_CUTOFF is appropriate. By default
  cutoff is set to 0, leaving it up to the set.

- **rel_cutoff** (*int*) – This cutoff decides how the Gaussians are
  mapped onto the different levels of the multigrid. If REL_CUTOFF is
  too low, then even if you have a high CUTOFF, all Gaussians will be
  mapped onto the coarsest level of the multi-grid, and thus the
  effective integration grid for the calculation may still be too
  coarse. By default 50Ry is chosen, which should be sufficient given
  the cutoff is large enough.

- **ngrids** (*int*) – number of multi-grids to use. CP2K default is 4,
  but the molopt basis files recommend 5.

- **progression_factor** (*int*) – Divisor of CUTOFF to get the cutoff
  for the next level of the multigrid.

- **wfn_restart_file_name** (*str*) – RESTART file for the initial
  wavefunction guess.

- **kpoints**
  (<a href="#pymatgen.io.cp2k.inputs.Kpoints" class="reference internal"
  title="pymatgen.io.cp2k.inputs.Kpoints"><em>Kpoints</em></a>) –
  kpoints object from pymatgen.io.vasp.inputs.Kpoints. By default, CP2K
  runs with gamma point only.

- **smearing** (*bool*) – whether or not to activate smearing (should be
  done for systems containing no (or a very small) band gap.

- **cell** (*dict\[str,* *Any\]*) – Keywords to add to the CELL section
  such as SYMMETRY. See <a
  href="https://manual.cp2k.org/trunk/CP2K_INPUT/FORCE_EVAL/SUBSYS/CELL.html#CP2K_INPUT.FORCE_EVAL.SUBSYS.CELL"
  class="reference external">https://manual.cp2k.org/trunk/CP2K_INPUT/FORCE_EVAL/SUBSYS/CELL.html#CP2K_INPUT.FORCE_EVAL.SUBSYS.CELL</a>

</div>

<div id="module-pymatgen.io.cp2k.utils" class="section">

<span id="pymatgen-io-cp2k-utils-module"></span>

## pymatgen.io.cp2k.utils module<a href="#module-pymatgen.io.cp2k.utils" class="headerlink"
title="Link to this heading"></a>

Utility functions for assisting with CP2K IO.

<span class="sig-name descname"><span class="pre">chunk</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">string</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/utils.py#L101-L109"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.utils.chunk" class="headerlink"
title="Link to this definition"></a>  
Chunk the string from a CP2K basis or potential file.

<!-- -->

<span class="sig-name descname"><span class="pre">get_truncated_coulomb_cutoff</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">inp_struct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/utils.py#L179-L187"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.utils.get_truncated_coulomb_cutoff"
class="headerlink" title="Link to this definition"></a>  
Get the truncated Coulomb cutoff for a given structure.

<!-- -->

<span class="sig-name descname"><span class="pre">get_unique_site_indices</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">struct</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Molecule"
class="reference internal"
title="pymatgen.core.structure.Molecule"><span
class="pre">Molecule</span></a></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/utils.py#L125-L176"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.utils.get_unique_site_indices"
class="headerlink" title="Link to this definition"></a>  
Get unique site indices for a structure according to site properties.
Whatever site-property has the most unique values is used for indexing.

For example, if you have magnetic CoO with half Co atoms having a
positive moment, and the other half having a negative moment. Then this
function will create a dict of sites for Co_1, Co_2, O. This function
also deals with “Species” properties like oxi_state and spin by pushing
them to site properties.

This creates unique sites, based on site properties, but does not have
anything to do with turning those site properties into CP2K input
parameters. This will only be done for properties which can be turned
into CP2K input parameters, which are stored in
parsable_site_properties.

<!-- -->

<span class="sig-name descname"><span class="pre">natural_keys</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">text</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/utils.py#L112-L122"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.utils.natural_keys" class="headerlink"
title="Link to this definition"></a>  
Sort text by numbers coming after an underscore with natural number
convention, Ex: \[file_1, file_12, file_2\] becomes \[file_1, file_2,
file_12\].

<!-- -->

<span class="sig-name descname"><span class="pre">postprocessor</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">data</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/utils.py#L16-L50"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.utils.postprocessor" class="headerlink"
title="Link to this definition"></a>  
Helper function to post process the results of the pattern matching
functions in Cp2kOutput and turn them to Python types.

Parameters<span class="colon">:</span>  
**data** (*str*) – The data to be post processed.

Raises<span class="colon">:</span>  
**ValueError** – If the data cannot be parsed.

Returns<span class="colon">:</span>  
The post processed data.

Return type<span class="colon">:</span>  
str \| float \| bool \| None

<!-- -->

<span class="sig-name descname"><span class="pre">preprocessor</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">data</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">dir</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'.'</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/cp2k/utils.py#L53-L98"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.cp2k.utils.preprocessor" class="headerlink"
title="Link to this definition"></a>  
CP2K contains internal preprocessor flags that are evaluated before
execution. This helper function recognizes those preprocessor flags and
replaces them with an equivalent CP2K input (this way everything is
contained neatly in the CP2K input structure, even if the user preferred
to use the flags.

CP2K preprocessor flags (with arguments) are:

> <div>
>
> @INCLUDE FILENAME: Insert the contents of FILENAME into the file at  
> this location.
>
> @SET VAR VALUE: set a variable, VAR, to have the value, VALUE. \$VAR
> or \${VAR}: replace these with the value of the variable, as set
>
> > <div>
> >
> > by the @SET flag.
> >
> > </div>
>
> @IF/@ELIF: Not implemented yet.
>
> </div>

Parameters<span class="colon">:</span>  
- **data** (*str*) – CP2K input to preprocess

- **dir** (*str,* *optional*) – Path for include files. Default is ‘.’
  (current directory).

Returns<span class="colon">:</span>  
Preprocessed string

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
