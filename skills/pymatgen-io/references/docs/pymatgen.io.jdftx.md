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

- <a href="#" class="reference internal">pymatgen.io.jdftx package</a>
  - <a href="#submodules" class="reference internal">Submodules</a>
  - <a href="#module-pymatgen.io.jdftx.generic_tags"
    class="reference internal">pymatgen.io.jdftx.generic_tags module</a>
    - <a href="#pymatgen.io.jdftx.generic_tags.AbstractNumericTag"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">AbstractNumericTag</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.AbstractNumericTag.eq_atol"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractNumericTag.eq_atol</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.AbstractNumericTag.eq_rtol"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractNumericTag.eq_rtol</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.generic_tags.AbstractNumericTag.get_invalid_value_error_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractNumericTag.get_invalid_value_error_str()</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.AbstractNumericTag.lb"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractNumericTag.lb</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.AbstractNumericTag.lb_incl"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractNumericTag.lb_incl</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.AbstractNumericTag.ub"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractNumericTag.ub</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.AbstractNumericTag.ub_incl"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractNumericTag.ub_incl</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.generic_tags.AbstractNumericTag.val_is_within_bounds"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractNumericTag.val_is_within_bounds()</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.generic_tags.AbstractNumericTag.validate_value_bounds"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractNumericTag.validate_value_bounds()</code></span></a>
    - <a href="#pymatgen.io.jdftx.generic_tags.AbstractTag"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">AbstractTag</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.generic_tags.AbstractTag.allow_list_representation"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractTag.allow_list_representation</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.AbstractTag.can_repeat"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractTag.can_repeat</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.AbstractTag.defer_until_struc"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractTag.defer_until_struc</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.generic_tags.AbstractTag.get_dict_representation"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractTag.get_dict_representation()</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.generic_tags.AbstractTag.get_list_representation"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractTag.get_list_representation()</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.AbstractTag.get_token_len"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractTag.get_token_len()</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.AbstractTag.is_equal_to"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractTag.is_equal_to()</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.AbstractTag.is_tag_container"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractTag.is_tag_container</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.AbstractTag.multiline_tag"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractTag.multiline_tag</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.AbstractTag.optional"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractTag.optional</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.AbstractTag.read"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractTag.read()</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.generic_tags.AbstractTag.validate_value_bounds"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractTag.validate_value_bounds()</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.generic_tags.AbstractTag.validate_value_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractTag.validate_value_type()</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.AbstractTag.write"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractTag.write()</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.AbstractTag.write_tagname"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractTag.write_tagname</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.AbstractTag.write_value"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">AbstractTag.write_value</code></span></a>
    - <a href="#pymatgen.io.jdftx.generic_tags.BoolTag"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">BoolTag</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.BoolTag.get_token_len"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoolTag.get_token_len()</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.BoolTag.raise_value_error"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoolTag.raise_value_error()</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.BoolTag.read"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoolTag.read()</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.BoolTag.validate_value_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoolTag.validate_value_type()</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.BoolTag.write"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoolTag.write()</code></span></a>
    - <a href="#pymatgen.io.jdftx.generic_tags.BoolTagContainer"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">BoolTagContainer</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.BoolTagContainer.read"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">BoolTagContainer.read()</code></span></a>
    - <a href="#pymatgen.io.jdftx.generic_tags.ClassPrintFormatter"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">ClassPrintFormatter</code></span></a>
    - <a href="#pymatgen.io.jdftx.generic_tags.DumpTagContainer"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">DumpTagContainer</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.DumpTagContainer.read"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">DumpTagContainer.read()</code></span></a>
    - <a href="#pymatgen.io.jdftx.generic_tags.FloatTag"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">FloatTag</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.FloatTag.get_token_len"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">FloatTag.get_token_len()</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.FloatTag.prec"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">FloatTag.prec</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.FloatTag.read"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">FloatTag.read()</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.FloatTag.validate_value_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">FloatTag.validate_value_type()</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.FloatTag.write"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">FloatTag.write()</code></span></a>
    - <a href="#pymatgen.io.jdftx.generic_tags.InitMagMomTag"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">InitMagMomTag</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.InitMagMomTag.get_token_len"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">InitMagMomTag.get_token_len()</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.InitMagMomTag.read"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">InitMagMomTag.read()</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.generic_tags.InitMagMomTag.validate_value_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">InitMagMomTag.validate_value_type()</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.InitMagMomTag.write"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">InitMagMomTag.write()</code></span></a>
    - <a href="#pymatgen.io.jdftx.generic_tags.IntTag"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">IntTag</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.IntTag.get_token_len"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IntTag.get_token_len()</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.IntTag.read"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IntTag.read()</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.IntTag.validate_value_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IntTag.validate_value_type()</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.IntTag.write"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">IntTag.write()</code></span></a>
    - <a href="#pymatgen.io.jdftx.generic_tags.MultiformatTag"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">MultiformatTag</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.MultiformatTag.format_options"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MultiformatTag.format_options</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.generic_tags.MultiformatTag.get_format_index_for_str_value"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MultiformatTag.get_format_index_for_str_value()</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.MultiformatTag.get_token_len"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MultiformatTag.get_token_len()</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.generic_tags.MultiformatTag.raise_invalid_format_option_error"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MultiformatTag.raise_invalid_format_option_error()</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.MultiformatTag.read"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MultiformatTag.read()</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.generic_tags.MultiformatTag.validate_value_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MultiformatTag.validate_value_type()</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.MultiformatTag.write"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">MultiformatTag.write()</code></span></a>
    - <a href="#pymatgen.io.jdftx.generic_tags.StrTag"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">StrTag</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.StrTag.get_token_len"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">StrTag.get_token_len()</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.StrTag.options"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">StrTag.options</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.StrTag.read"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">StrTag.read()</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.StrTag.validate_value_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">StrTag.validate_value_type()</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.StrTag.write"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">StrTag.write()</code></span></a>
    - <a href="#pymatgen.io.jdftx.generic_tags.TagContainer"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">TagContainer</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.generic_tags.TagContainer.get_dict_representation"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TagContainer.get_dict_representation()</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.generic_tags.TagContainer.get_list_representation"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TagContainer.get_list_representation()</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.TagContainer.get_token_len"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TagContainer.get_token_len()</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.TagContainer.is_tag_container"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TagContainer.is_tag_container</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.generic_tags.TagContainer.linebreak_nth_entry"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TagContainer.linebreak_nth_entry</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.TagContainer.read"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TagContainer.read()</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.TagContainer.subtags"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TagContainer.subtags</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.generic_tags.TagContainer.validate_value_bounds"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TagContainer.validate_value_bounds()</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.generic_tags.TagContainer.validate_value_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TagContainer.validate_value_type()</code></span></a>
      - <a href="#pymatgen.io.jdftx.generic_tags.TagContainer.write"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">TagContainer.write()</code></span></a>
  - <a href="#module-pymatgen.io.jdftx.inputs"
    class="reference internal">pymatgen.io.jdftx.inputs module</a>
    - <a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">JDFTXInfile</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.append_tag"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXInfile.append_tag()</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXInfile.as_dict()</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.copy"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXInfile.copy()</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXInfile.from_dict()</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.from_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXInfile.from_file()</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.from_jdftxstructure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXInfile.from_jdftxstructure()</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.from_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXInfile.from_str()</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.from_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXInfile.from_structure()</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.get_dict_representation"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXInfile.get_dict_representation()</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.get_differing_tags"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXInfile.get_differing_tags()</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.get_differing_tags_from"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXInfile.get_differing_tags_from()</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.inputs.JDFTXInfile.get_filtered_differing_tags"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXInfile.get_filtered_differing_tags()</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.get_list_representation"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXInfile.get_list_representation()</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.get_text_list"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXInfile.get_text_list()</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.is_comparable_to"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXInfile.is_comparable_to()</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.path_parent"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXInfile.path_parent</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.strip_structure_tags"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXInfile.strip_structure_tags()</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXInfile.structure</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.to_jdftxstructure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXInfile.to_jdftxstructure()</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.to_pmg_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXInfile.to_pmg_structure()</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.validate_boundaries"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXInfile.validate_boundaries()</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.validate_tags"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXInfile.validate_tags()</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.write_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXInfile.write_file()</code></span></a>
    - <a href="#pymatgen.io.jdftx.inputs.JDFTXStructure"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">JDFTXStructure</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXStructure.structure</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.selective_dynamics"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXStructure.selective_dynamics</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.sort_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXStructure.sort_structure</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.write_cart_coords"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXStructure.write_cart_coords</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.velocities"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXStructure.velocities</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.constraint_types"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXStructure.constraint_types</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.constraint_vectors"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXStructure.constraint_vectors</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.inputs.JDFTXStructure.hyperplane_group_names"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXStructure.hyperplane_group_names</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXStructure.as_dict()</code></span></a>
      - <a href="#id0" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXStructure.constraint_types</code></span></a>
      - <a href="#id1" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXStructure.constraint_vectors</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.from_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXStructure.from_dict()</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.from_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXStructure.from_file()</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.from_jdftxinfile"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXStructure.from_jdftxinfile()</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.from_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXStructure.from_str()</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.get_str"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXStructure.get_str()</code></span></a>
      - <a href="#id2" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXStructure.hyperplane_group_names</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.natoms"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXStructure.natoms</code></span></a>
      - <a href="#id3" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXStructure.selective_dynamics</code></span></a>
      - <a href="#id4" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXStructure.sort_structure</code></span></a>
      - <a href="#id5" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXStructure.structure</code></span></a>
      - <a href="#id6" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXStructure.velocities</code></span></a>
      - <a href="#id7" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXStructure.write_cart_coords</code></span></a>
      - <a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.write_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXStructure.write_file()</code></span></a>
    - <a
      href="#pymatgen.io.jdftx.inputs.selective_dynamics_site_prop_to_jdftx_interpretable"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">selective_dynamics_site_prop_to_jdftx_interpretable()</code></span></a>
  - <a href="#module-pymatgen.io.jdftx.jdftxinfile_default_inputs"
    class="reference internal">pymatgen.io.jdftx.jdftxinfile_default_inputs
    module</a>
  - <a href="#module-pymatgen.io.jdftx.jdftxinfile_master_format"
    class="reference internal">pymatgen.io.jdftx.jdftxinfile_master_format
    module</a>
    - <a
      href="#pymatgen.io.jdftx.jdftxinfile_master_format.get_dump_tag_container"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">get_dump_tag_container()</code></span></a>
    - <a href="#pymatgen.io.jdftx.jdftxinfile_master_format.get_tag_object"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">get_tag_object()</code></span></a>
    - <a
      href="#pymatgen.io.jdftx.jdftxinfile_master_format.get_tag_object_on_val"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">get_tag_object_on_val()</code></span></a>
  - <a href="#module-pymatgen.io.jdftx.jdftxinfile_ref_options"
    class="reference internal">pymatgen.io.jdftx.jdftxinfile_ref_options
    module</a>
  - <a href="#module-pymatgen.io.jdftx.jdftxoutfileslice"
    class="reference internal">pymatgen.io.jdftx.jdftxoutfileslice
    module</a>
    - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">JDFTXOutfileSlice</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.prefix"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.prefix</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.jstrucs"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.jstrucs</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.jsettings_fluid"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.jsettings_fluid</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.jsettings_electronic"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.jsettings_electronic</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.jsettings_lattice"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.jsettings_lattice</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.jsettings_ionic"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.jsettings_ionic</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.xc_func"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.xc_func</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.lattice_initial"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.lattice_initial</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.lattice_final"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.lattice_final</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.lattice"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.lattice</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.a"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.a</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.b"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.b</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.c"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.c</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.fftgrid"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.fftgrid</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.geom_opt"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.geom_opt</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.geom_opt_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.geom_opt_type</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.efermi"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.efermi</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.egap"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.egap</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.emin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.emin</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.emax"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.emax</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.homo"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.homo</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.lumo"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.lumo</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.homo_filling"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.homo_filling</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.lumo_filling"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.lumo_filling</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.is_metal"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.is_metal</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.etype"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.etype</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.broadening_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.broadening_type</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.broadening"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.broadening</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.kgrid"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.kgrid</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.truncation_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.truncation_type</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.truncation_radius"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.truncation_radius</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.pwcut"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.pwcut</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.rhocut"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.rhocut</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.pp_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.pp_type</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.total_electrons"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.total_electrons</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.semicore_electrons"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.semicore_electrons</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.valence_electrons"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.valence_electrons</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.total_electrons_uncharged"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.total_electrons_uncharged</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.semicore_electrons_uncharged"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.semicore_electrons_uncharged</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.valence_electrons_uncharged"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.valence_electrons_uncharged</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.nbands"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.nbands</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.atom_elements"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.atom_elements</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.atom_elements_int"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.atom_elements_int</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.atom_types"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.atom_types</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.spintype"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.spintype</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.nspin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.nspin</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.nat"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.nat</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.atom_coords_initial"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.atom_coords_initial</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.atom_coords_final"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.atom_coords_final</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.atom_coords"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.atom_coords</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.has_solvation"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.has_solvation</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.fluid"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.fluid</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.is_gc"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.is_gc</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.is_bgw"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.is_bgw</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.has_eigstats"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.has_eigstats</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.has_parsable_pseudo"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.has_parsable_pseudo</code></span></a>
      - <a href="#id12" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.a</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.abs_magneticmoment"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.abs_magneticmoment</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.alpha"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.alpha</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.as_dict()</code></span></a>
      - <a href="#id13" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.atom_coords</code></span></a>
      - <a href="#id14" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.atom_coords_final</code></span></a>
      - <a href="#id15" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.atom_coords_initial</code></span></a>
      - <a href="#id16" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.atom_elements</code></span></a>
      - <a href="#id17" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.atom_elements_int</code></span></a>
      - <a href="#id18" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.atom_types</code></span></a>
      - <a href="#id19" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.b</code></span></a>
      - <a href="#id20" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.broadening</code></span></a>
      - <a href="#id21" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.broadening_type</code></span></a>
      - <a href="#id22" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.c</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.constant_lattice"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.constant_lattice</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.converged"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.converged</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.determine_is_metal"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.determine_is_metal()</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.e"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.e</code></span></a>
      - <a href="#id23" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.efermi</code></span></a>
      - <a href="#id24" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.egap</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.elec_alpha"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.elec_alpha</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.elec_e"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.elec_e</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.elec_grad_k"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.elec_grad_k</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.elec_linmin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.elec_linmin</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.elec_nstep"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.elec_nstep</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.elecmindata"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.elecmindata</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.electronic_output"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.electronic_output</code></span></a>
      - <a href="#id25" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.emax</code></span></a>
      - <a href="#id26" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.emin</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.eopt_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.eopt_type</code></span></a>
      - <a href="#id27" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.etype</code></span></a>
      - <a href="#id28" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.fftgrid</code></span></a>
      - <a href="#id29" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.fluid</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.forces"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.forces</code></span></a>
      - <a href="#id30" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.geom_opt</code></span></a>
      - <a href="#id31" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.geom_opt_type</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.grad_k"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.grad_k</code></span></a>
      - <a href="#id32" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.has_eigstats</code></span></a>
      - <a href="#id33" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.has_parsable_pseudo</code></span></a>
      - <a href="#id34" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.has_solvation</code></span></a>
      - <a href="#id35" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.homo</code></span></a>
      - <a href="#id36" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.homo_filling</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.initial_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.initial_structure</code></span></a>
      - <a href="#id37" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.is_bgw</code></span></a>
      - <a href="#id38" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.is_gc</code></span></a>
      - <a href="#id39" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.is_metal</code></span></a>
      - <a href="#id40" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.jsettings_electronic</code></span></a>
      - <a href="#id41" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.jsettings_fluid</code></span></a>
      - <a href="#id42" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.jsettings_ionic</code></span></a>
      - <a href="#id43" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.jsettings_lattice</code></span></a>
      - <a href="#id44" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.jstrucs</code></span></a>
      - <a href="#id45" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.kgrid</code></span></a>
      - <a href="#id46" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.lattice</code></span></a>
      - <a href="#id47" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.lattice_final</code></span></a>
      - <a href="#id48" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.lattice_initial</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.linmin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.linmin</code></span></a>
      - <a href="#id49" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.lumo</code></span></a>
      - <a href="#id50" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.lumo_filling</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.mu"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.mu</code></span></a>
      - <a href="#id51" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.nat</code></span></a>
      - <a href="#id52" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.nbands</code></span></a>
      - <a href="#id53" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.nspin</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.nstep"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.nstep</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.optical_egap"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.optical_egap</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.parsable_pseudos"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.parsable_pseudos</code></span></a>
      - <a href="#id54" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.pp_type</code></span></a>
      - <a href="#id55" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.prefix</code></span></a>
      - <a href="#id56" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.pwcut</code></span></a>
      - <a href="#id57" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.rhocut</code></span></a>
      - <a href="#id58" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.semicore_electrons</code></span></a>
      - <a href="#id59" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.semicore_electrons_uncharged</code></span></a>
      - <a href="#id60" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.spintype</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.strain"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.strain</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.stress"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.stress</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.structure</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.t_s"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.t_s</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.to_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.to_dict()</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.to_jdftxinfile"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.to_jdftxinfile()</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.tot_magneticmoment"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.tot_magneticmoment</code></span></a>
      - <a href="#id61" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.total_electrons</code></span></a>
      - <a href="#id62" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.total_electrons_uncharged</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.trajectory"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.trajectory</code></span></a>
      - <a href="#id63" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.truncation_radius</code></span></a>
      - <a href="#id64" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.truncation_type</code></span></a>
      - <a href="#id65" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.valence_electrons</code></span></a>
      - <a href="#id66" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.valence_electrons_uncharged</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.vibrational_energy_components"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.vibrational_energy_components</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.vibrational_modes"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.vibrational_modes</code></span></a>
      - <a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.write"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.write()</code></span></a>
      - <a href="#id67" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfileSlice.xc_func</code></span></a>
    - <a
      href="#pymatgen.io.jdftx.jdftxoutfileslice.get_pseudo_read_section_bounds"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">get_pseudo_read_section_bounds()</code></span></a>
  - <a href="#module-pymatgen.io.jdftx.jelstep"
    class="reference internal">pymatgen.io.jdftx.jelstep module</a>
    - <a href="#pymatgen.io.jdftx.jelstep.JElStep"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">JElStep</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElStep.opt_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.opt_type</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElStep.etype"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.etype</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElStep.nstep"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.nstep</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElStep.e"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.e</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElStep.grad_k"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.grad_k</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElStep.alpha"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.alpha</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElStep.linmin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.linmin</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElStep.t_s"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.t_s</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElStep.mu"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.mu</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElStep.nelectrons"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.nelectrons</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElStep.abs_magneticmoment"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.abs_magneticmoment</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElStep.tot_magneticmoment"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.tot_magneticmoment</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElStep.subspacerotationadjust"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.subspacerotationadjust</code></span></a>
      - <a href="#id68" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.abs_magneticmoment</code></span></a>
      - <a href="#id69" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.alpha</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElStep.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.as_dict()</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElStep.converged"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.converged</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElStep.converged_reason"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.converged_reason</code></span></a>
      - <a href="#id70" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.e</code></span></a>
      - <a href="#id71" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.etype</code></span></a>
      - <a href="#id72" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.grad_k</code></span></a>
      - <a href="#id73" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.linmin</code></span></a>
      - <a href="#id74" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.mu</code></span></a>
      - <a href="#id75" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.nelectrons</code></span></a>
      - <a href="#id76" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.nstep</code></span></a>
      - <a href="#id77" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.opt_type</code></span></a>
      - <a href="#id78" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.subspacerotationadjust</code></span></a>
      - <a href="#id79" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.t_s</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElStep.to_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.to_dict()</code></span></a>
      - <a href="#id80" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElStep.tot_magneticmoment</code></span></a>
    - <a href="#pymatgen.io.jdftx.jelstep.JElSteps"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">JElSteps</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElSteps.opt_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.opt_type</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElSteps.etype"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.etype</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElSteps.iter_flag"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.iter_flag</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElSteps.converged"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.converged</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElSteps.converged_reason"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.converged_reason</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElSteps.slices"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.slices</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElSteps.e"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.e</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElSteps.grad_k"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.grad_k</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElSteps.alpha"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.alpha</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElSteps.linmin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.linmin</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElSteps.t_s"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.t_s</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElSteps.mu"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.mu</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElSteps.nelectrons"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.nelectrons</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElSteps.abs_magneticmoment"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.abs_magneticmoment</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElSteps.tot_magneticmoment"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.tot_magneticmoment</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElSteps.subspacerotationadjust"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.subspacerotationadjust</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElSteps.nstep"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.nstep</code></span></a>
      - <a href="#id81" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.abs_magneticmoment</code></span></a>
      - <a href="#id82" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.alpha</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElSteps.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.as_dict()</code></span></a>
      - <a href="#id83" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.converged</code></span></a>
      - <a href="#id84" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.converged_reason</code></span></a>
      - <a href="#id85" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.e</code></span></a>
      - <a href="#id86" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.etype</code></span></a>
      - <a href="#id87" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.grad_k</code></span></a>
      - <a href="#id88" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.iter_flag</code></span></a>
      - <a href="#id89" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.linmin</code></span></a>
      - <a href="#id90" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.mu</code></span></a>
      - <a href="#id91" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.nelectrons</code></span></a>
      - <a href="#id92" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.nstep</code></span></a>
      - <a href="#id93" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.opt_type</code></span></a>
      - <a href="#id94" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.slices</code></span></a>
      - <a href="#id95" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.subspacerotationadjust</code></span></a>
      - <a href="#id96" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.t_s</code></span></a>
      - <a href="#pymatgen.io.jdftx.jelstep.JElSteps.to_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.to_dict()</code></span></a>
      - <a href="#id97" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JElSteps.tot_magneticmoment</code></span></a>
  - <a href="#module-pymatgen.io.jdftx.jminsettings"
    class="reference internal">pymatgen.io.jdftx.jminsettings module</a>
    - <a href="#pymatgen.io.jdftx.jminsettings.JMinSettings"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">JMinSettings</code></span></a>
      - <a href="#pymatgen.io.jdftx.jminsettings.JMinSettings.params"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JMinSettings.params</code></span></a>
    - <a href="#pymatgen.io.jdftx.jminsettings.JMinSettingsElectronic"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">JMinSettingsElectronic</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.jminsettings.JMinSettingsElectronic.start_flag"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JMinSettingsElectronic.start_flag</code></span></a>
    - <a href="#pymatgen.io.jdftx.jminsettings.JMinSettingsFluid"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">JMinSettingsFluid</code></span></a>
      - <a href="#pymatgen.io.jdftx.jminsettings.JMinSettingsFluid.start_flag"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JMinSettingsFluid.start_flag</code></span></a>
    - <a href="#pymatgen.io.jdftx.jminsettings.JMinSettingsIonic"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">JMinSettingsIonic</code></span></a>
      - <a href="#pymatgen.io.jdftx.jminsettings.JMinSettingsIonic.start_flag"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JMinSettingsIonic.start_flag</code></span></a>
    - <a href="#pymatgen.io.jdftx.jminsettings.JMinSettingsLattice"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">JMinSettingsLattice</code></span></a>
      - <a href="#pymatgen.io.jdftx.jminsettings.JMinSettingsLattice.start_flag"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JMinSettingsLattice.start_flag</code></span></a>
  - <a href="#module-pymatgen.io.jdftx.joutstructure"
    class="reference internal">pymatgen.io.jdftx.joutstructure module</a>
    - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">JOutStructure</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.opt_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.opt_type</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.etype"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.etype</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.eopt_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.eopt_type</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.emin_flag"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.emin_flag</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.ecomponents"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.ecomponents</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.elecmindata"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.elecmindata</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.stress"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.stress</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.strain"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.strain</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.nstep"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.nstep</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.e"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.e</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.grad_k"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.grad_k</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.alpha"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.alpha</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.linmin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.linmin</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.t_s"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.t_s</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.geom_converged"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.geom_converged</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.joutstructure.JOutStructure.geom_converged_reason"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.geom_converged_reason</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.line_types"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.line_types</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.joutstructure.JOutStructure.selective_dynamics"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.selective_dynamics</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.mu"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.mu</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.nelectrons"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.nelectrons</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.joutstructure.JOutStructure.abs_magneticmoment"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.abs_magneticmoment</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.joutstructure.JOutStructure.tot_magneticmoment"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.tot_magneticmoment</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.elec_nstep"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.elec_nstep</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.elec_e"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.elec_e</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.elec_grad_k"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.elec_grad_k</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.elec_alpha"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.elec_alpha</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.elec_linmin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.elec_linmin</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.structure</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.is_md"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.is_md</code></span></a>
      - <a href="#id98" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.abs_magneticmoment</code></span></a>
      - <a href="#id99" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.alpha</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.as_dict()</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.charges"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.charges</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.joutstructure.JOutStructure.constraint_types"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.constraint_types</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.joutstructure.JOutStructure.constraint_vectors"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.constraint_vectors</code></span></a>
      - <a href="#id100" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.e</code></span></a>
      - <a href="#id101" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.ecomponents</code></span></a>
      - <a href="#id102" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.elec_alpha</code></span></a>
      - <a href="#id103" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.elec_e</code></span></a>
      - <a href="#id104" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.elec_grad_k</code></span></a>
      - <a href="#id105" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.elec_linmin</code></span></a>
      - <a href="#id106" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.elec_nstep</code></span></a>
      - <a href="#id107" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.elecmindata</code></span></a>
      - <a href="#id108" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.emin_flag</code></span></a>
      - <a href="#id109" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.eopt_type</code></span></a>
      - <a href="#id110" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.etype</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.forces"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.forces</code></span></a>
      - <a href="#id111" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.geom_converged</code></span></a>
      - <a href="#id112" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.geom_converged_reason</code></span></a>
      - <a href="#id113" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.grad_k</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.group_names"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.group_names</code></span></a>
      - <a href="#id114" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.is_md</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.kinetic_stress"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.kinetic_stress</code></span></a>
      - <a href="#id115" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.line_types</code></span></a>
      - <a href="#id116" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.linmin</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.joutstructure.JOutStructure.magnetic_moments"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.magnetic_moments</code></span></a>
      - <a href="#id117" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.mu</code></span></a>
      - <a href="#id118" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.nelectrons</code></span></a>
      - <a href="#id119" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.nstep</code></span></a>
      - <a href="#id120" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.opt_type</code></span></a>
      - <a href="#id121" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.selective_dynamics</code></span></a>
      - <a href="#id122" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.strain</code></span></a>
      - <a href="#id123" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.stress</code></span></a>
      - <a href="#id124" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.structure</code></span></a>
      - <a href="#id125" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.t_s</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.joutstructure.JOutStructure.thermostat_velocity"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.thermostat_velocity</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.to_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.to_dict()</code></span></a>
      - <a href="#id126" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.tot_magneticmoment</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.velocities"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructure.velocities</code></span></a>
  - <a href="#module-pymatgen.io.jdftx.joutstructures"
    class="reference internal">pymatgen.io.jdftx.joutstructures module</a>
    - <a href="#pymatgen.io.jdftx.joutstructures.JOutStructures"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">JOutStructures</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.joutstructures.JOutStructures.out_slice_start_flag"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.out_slice_start_flag</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.opt_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.opt_type</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.joutstructures.JOutStructures.geom_converged"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.geom_converged</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.joutstructures.JOutStructures.geom_converged_reason"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.geom_converged_reason</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.joutstructures.JOutStructures.elec_converged"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.elec_converged</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.joutstructures.JOutStructures.elec_converged_reason"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.elec_converged_reason</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.slices"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.slices</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.eopt_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.eopt_type</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.etype"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.etype</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.emin_flag"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.emin_flag</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.ecomponents"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.ecomponents</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.elecmindata"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.elecmindata</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.stress"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.stress</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.strain"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.strain</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.nstep"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.nstep</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.e"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.e</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.grad_k"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.grad_k</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.alpha"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.alpha</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.linmin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.linmin</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.joutstructures.JOutStructures.abs_magneticmoment"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.abs_magneticmoment</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.joutstructures.JOutStructures.tot_magneticmoment"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.tot_magneticmoment</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.mu"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.mu</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.elec_e"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.elec_e</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.elec_nstep"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.elec_nstep</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.elec_grad_k"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.elec_grad_k</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.elec_alpha"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.elec_alpha</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.elec_linmin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.elec_linmin</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.charges"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.charges</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.joutstructures.JOutStructures.magnetic_moments"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.magnetic_moments</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.joutstructures.JOutStructures.selective_dynamics"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.selective_dynamics</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.structure</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.joutstructures.JOutStructures.initial_structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.initial_structure</code></span></a>
      - <a href="#id131" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.abs_magneticmoment</code></span></a>
      - <a href="#id132" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.alpha</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.as_dict()</code></span></a>
      - <a href="#id133" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.charges</code></span></a>
      - <a href="#id134" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.e</code></span></a>
      - <a href="#id135" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.ecomponents</code></span></a>
      - <a href="#id136" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.elec_alpha</code></span></a>
      - <a href="#id137" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.elec_converged</code></span></a>
      - <a href="#id138" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.elec_converged_reason</code></span></a>
      - <a href="#id139" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.elec_e</code></span></a>
      - <a href="#id140" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.elec_grad_k</code></span></a>
      - <a href="#id141" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.elec_linmin</code></span></a>
      - <a href="#id142" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.elec_nstep</code></span></a>
      - <a href="#id143" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.elecmindata</code></span></a>
      - <a href="#id144" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.emin_flag</code></span></a>
      - <a href="#id145" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.eopt_type</code></span></a>
      - <a href="#id146" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.etype</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.forces"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.forces</code></span></a>
      - <a href="#id147" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.geom_converged</code></span></a>
      - <a href="#id148" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.geom_converged_reason</code></span></a>
      - <a href="#id149" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.grad_k</code></span></a>
      - <a href="#id150" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.initial_structure</code></span></a>
      - <a href="#id151" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.linmin</code></span></a>
      - <a href="#id152" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.magnetic_moments</code></span></a>
      - <a href="#id153" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.mu</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.nelectrons"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.nelectrons</code></span></a>
      - <a href="#id154" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.nstep</code></span></a>
      - <a href="#id155" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.opt_type</code></span></a>
      - <a href="#id156" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.out_slice_start_flag</code></span></a>
      - <a href="#id157" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.selective_dynamics</code></span></a>
      - <a href="#id158" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.slices</code></span></a>
      - <a href="#id159" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.strain</code></span></a>
      - <a href="#id160" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.stress</code></span></a>
      - <a href="#id161" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.structure</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.t_s"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.t_s</code></span></a>
      - <a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.to_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.to_dict()</code></span></a>
      - <a href="#id162" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JOutStructures.tot_magneticmoment</code></span></a>
  - <a href="#module-pymatgen.io.jdftx.outputs"
    class="reference internal">pymatgen.io.jdftx.outputs module</a>
    - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">JDFTXOutfile</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.slices"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.slices</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.prefix"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.prefix</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.jstrucs"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.jstrucs</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.jsettings_fluid"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.jsettings_fluid</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.jsettings_electronic"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.jsettings_electronic</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.jsettings_lattice"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.jsettings_lattice</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.jsettings_ionic"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.jsettings_ionic</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.xc_func"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.xc_func</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.lattice_initial"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.lattice_initial</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.lattice_final"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.lattice_final</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.lattice"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.lattice</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.a"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.a</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.b"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.b</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.c"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.c</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.fftgrid"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.fftgrid</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.geom_opt"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.geom_opt</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.geom_opt_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.geom_opt_type</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.ecomponents"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.ecomponents</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.efermi"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.efermi</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.egap"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.egap</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.emin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.emin</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.emax"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.emax</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.homo"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.homo</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.lumo"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.lumo</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.homo_filling"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.homo_filling</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.lumo_filling"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.lumo_filling</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.is_metal"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.is_metal</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.converged"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.converged</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.etype"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.etype</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.broadening_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.broadening_type</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.broadening"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.broadening</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.kgrid"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.kgrid</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.truncation_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.truncation_type</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.truncation_radius"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.truncation_radius</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.pwcut"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.pwcut</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.rhocut"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.rhocut</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.pp_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.pp_type</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.total_electrons"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.total_electrons</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.semicore_electrons"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.semicore_electrons</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.valence_electrons"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.valence_electrons</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.total_electrons_uncharged"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.total_electrons_uncharged</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.semicore_electrons_uncharged"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.semicore_electrons_uncharged</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.valence_electrons_uncharged"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.valence_electrons_uncharged</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.nbands"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.nbands</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.atom_elements"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.atom_elements</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.atom_elements_int"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.atom_elements_int</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.atom_types"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.atom_types</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.spintype"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.spintype</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.nspin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.nspin</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.nat"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.nat</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.atom_coords_initial"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.atom_coords_initial</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.atom_coords_final"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.atom_coords_final</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.atom_coords"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.atom_coords</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.structure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.structure</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.trajectory"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.trajectory</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.has_solvation"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.has_solvation</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.fluid"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.fluid</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.is_gc"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.is_gc</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.eopt_type"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.eopt_type</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.elecmindata"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.elecmindata</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.stress"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.stress</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.strain"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.strain</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.nstep"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.nstep</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.e"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.e</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.grad_k"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.grad_k</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.alpha"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.alpha</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.linmin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.linmin</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.abs_magneticmoment"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.abs_magneticmoment</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.tot_magneticmoment"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.tot_magneticmoment</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.mu"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.mu</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.elec_e"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.elec_e</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.elec_nstep"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.elec_nstep</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.elec_grad_k"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.elec_grad_k</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.elec_alpha"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.elec_alpha</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.elec_linmin"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.elec_linmin</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.infile"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.infile</code></span></a>
      - <a href="#id167" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.a</code></span></a>
      - <a href="#id168" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.abs_magneticmoment</code></span></a>
      - <a href="#id169" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.alpha</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.as_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.as_dict()</code></span></a>
      - <a href="#id170" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.atom_coords</code></span></a>
      - <a href="#id171" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.atom_coords_final</code></span></a>
      - <a href="#id172" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.atom_coords_initial</code></span></a>
      - <a href="#id173" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.atom_elements</code></span></a>
      - <a href="#id174" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.atom_elements_int</code></span></a>
      - <a href="#id175" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.atom_types</code></span></a>
      - <a href="#id176" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.b</code></span></a>
      - <a href="#id177" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.broadening</code></span></a>
      - <a href="#id178" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.broadening_type</code></span></a>
      - <a href="#id179" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.c</code></span></a>
      - <a href="#id180" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.converged</code></span></a>
      - <a href="#id181" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.e</code></span></a>
      - <a href="#id182" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.efermi</code></span></a>
      - <a href="#id183" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.egap</code></span></a>
      - <a href="#id184" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.elec_alpha</code></span></a>
      - <a href="#id185" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.elec_e</code></span></a>
      - <a href="#id186" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.elec_grad_k</code></span></a>
      - <a href="#id187" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.elec_linmin</code></span></a>
      - <a href="#id188" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.elec_nstep</code></span></a>
      - <a href="#id189" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.elecmindata</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.electronic_output"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.electronic_output</code></span></a>
      - <a href="#id190" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.emax</code></span></a>
      - <a href="#id191" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.emin</code></span></a>
      - <a href="#id192" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.eopt_type</code></span></a>
      - <a href="#id193" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.etype</code></span></a>
      - <a href="#id194" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.fftgrid</code></span></a>
      - <a href="#id195" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.fluid</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.forces"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.forces</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.from_calc_dir"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.from_calc_dir()</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.from_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.from_file()</code></span></a>
      - <a href="#id196" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.geom_opt</code></span></a>
      - <a href="#id197" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.geom_opt_type</code></span></a>
      - <a href="#id198" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.grad_k</code></span></a>
      - <a href="#id199" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.has_solvation</code></span></a>
      - <a href="#id200" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.homo</code></span></a>
      - <a href="#id201" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.homo_filling</code></span></a>
      - <a href="#id202" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.infile</code></span></a>
      - <a href="#id203" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.is_gc</code></span></a>
      - <a href="#id204" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.is_metal</code></span></a>
      - <a href="#id205" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.jsettings_electronic</code></span></a>
      - <a href="#id206" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.jsettings_fluid</code></span></a>
      - <a href="#id207" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.jsettings_ionic</code></span></a>
      - <a href="#id208" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.jsettings_lattice</code></span></a>
      - <a href="#id209" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.jstrucs</code></span></a>
      - <a href="#id210" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.kgrid</code></span></a>
      - <a href="#id211" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.lattice</code></span></a>
      - <a href="#id212" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.lattice_final</code></span></a>
      - <a href="#id213" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.lattice_initial</code></span></a>
      - <a href="#id214" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.linmin</code></span></a>
      - <a href="#id215" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.lumo</code></span></a>
      - <a href="#id216" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.lumo_filling</code></span></a>
      - <a href="#id217" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.mu</code></span></a>
      - <a href="#id218" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.nat</code></span></a>
      - <a href="#id219" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.nbands</code></span></a>
      - <a href="#id220" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.nspin</code></span></a>
      - <a href="#id221" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.nstep</code></span></a>
      - <a href="#id222" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.pp_type</code></span></a>
      - <a href="#id223" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.prefix</code></span></a>
      - <a href="#id224" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.pwcut</code></span></a>
      - <a href="#id225" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.rhocut</code></span></a>
      - <a href="#id226" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.semicore_electrons</code></span></a>
      - <a href="#id227" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.semicore_electrons_uncharged</code></span></a>
      - <a href="#id228" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.slices</code></span></a>
      - <a href="#id229" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.spintype</code></span></a>
      - <a href="#id230" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.strain</code></span></a>
      - <a href="#id231" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.stress</code></span></a>
      - <a href="#id232" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.structure</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.to_dict"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.to_dict()</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.to_jdftxinfile"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.to_jdftxinfile()</code></span></a>
      - <a href="#id233" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.tot_magneticmoment</code></span></a>
      - <a href="#id234" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.total_electrons</code></span></a>
      - <a href="#id235" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.total_electrons_uncharged</code></span></a>
      - <a href="#id236" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.trajectory</code></span></a>
      - <a href="#id237" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.truncation_radius</code></span></a>
      - <a href="#id238" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.truncation_type</code></span></a>
      - <a href="#id239" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.valence_electrons</code></span></a>
      - <a href="#id240" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.valence_electrons_uncharged</code></span></a>
      - <a
        href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.vibrational_energy_components"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.vibrational_energy_components</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.vibrational_modes"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.vibrational_modes</code></span></a>
      - <a href="#id241" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutfile.xc_func</code></span></a>
    - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutputs"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">JDFTXOutputs</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutputs.calc_dir"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutputs.calc_dir</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutputs.store_vars"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutputs.store_vars</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutputs.paths"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutputs.paths</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutputs.outfile"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutputs.outfile</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutputs.bandProjections"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutputs.bandProjections</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutputs.eigenvals"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutputs.eigenvals</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutputs.orb_label_list"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutputs.orb_label_list</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutputs.kpts"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutputs.kpts</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutputs.wk_list"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutputs.wk_list</code></span></a>
      - <a href="#id242" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutputs.bandProjections</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutputs.bandstructure"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutputs.bandstructure</code></span></a>
      - <a href="#id243" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutputs.calc_dir</code></span></a>
      - <a href="#id244" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutputs.eigenvals</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutputs.from_calc_dir"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutputs.from_calc_dir()</code></span></a>
      - <a href="#id245" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutputs.kpts</code></span></a>
      - <a href="#id246" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutputs.orb_label_list</code></span></a>
      - <a href="#id247" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutputs.outfile</code></span></a>
      - <a href="#pymatgen.io.jdftx.outputs.JDFTXOutputs.outfile_name"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutputs.outfile_name</code></span></a>
      - <a href="#id248" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutputs.paths</code></span></a>
      - <a href="#id249" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutputs.store_vars</code></span></a>
      - <a href="#id250" class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JDFTXOutputs.wk_list</code></span></a>
  - <a href="#module-pymatgen.io.jdftx.sets"
    class="reference internal">pymatgen.io.jdftx.sets module</a>
    - <a href="#pymatgen.io.jdftx.sets.JdftxInputSet"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">JdftxInputSet</code></span></a>
      - <a href="#pymatgen.io.jdftx.sets.JdftxInputSet.from_file"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JdftxInputSet.from_file()</code></span></a>
      - <a href="#pymatgen.io.jdftx.sets.JdftxInputSet.write_input"
        class="reference internal"><span class="pre"><code
        class="docutils literal notranslate">JdftxInputSet.write_input()</code></span></a>
    - <a href="#pymatgen.io.jdftx.sets.condense_jdftxinputs"
      class="reference internal"><span class="pre"><code
      class="docutils literal notranslate">condense_jdftxinputs()</code></span></a>

</div>

</div>

</div>

<div class="section wy-nav-content-wrap" toggle="wy-nav-shift">

[pymatgen](index.html)

<div class="wy-nav-content">

<div class="rst-content style-external-links">

<div role="navigation" aria-label="Page navigation">

- <a href="index.html" class="icon icon-home" aria-label="Home"></a>
- pymatgen.io.jdftx package
- <a
  href="https://github.com/materialsproject/pymatgen/blob/master/docs_rst/pymatgen.io.jdftx.rst"
  class="fa fa-github">Edit on GitHub</a>

------------------------------------------------------------------------

</div>

<div class="document" role="main" itemscope="itemscope"
itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="module-pymatgen.io.jdftx" class="section">

<span id="pymatgen-io-jdftx-package"></span>

# pymatgen.io.jdftx package<a href="#module-pymatgen.io.jdftx" class="headerlink"
title="Link to this heading"></a>

<div id="submodules" class="section">

## Submodules<a href="#submodules" class="headerlink"
title="Link to this heading"></a>

</div>

<div id="module-pymatgen.io.jdftx.generic_tags" class="section">

<span id="pymatgen-io-jdftx-generic-tags-module"></span>

## pymatgen.io.jdftx.generic_tags module<a href="#module-pymatgen.io.jdftx.generic_tags" class="headerlink"
title="Link to this heading"></a>

Module for class objects for containing JDFTx tags.

This module contains class objects for containing JDFTx tags. These
class objects are used to validate the type of the value for the tag,
read the value string for the tag, write the tag and its value as a
string, and get the token length of the tag.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">AbstractNumericTag</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">multiline_tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">can_repeat</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">write_tagname</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">write_value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">optional</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">defer_until_struc</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">is_tag_container</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">allow_list_representation</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">lb</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ub</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">lb_incl</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">ub_incl</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">eq_atol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-08</span></span>*, *<span class="n"><span class="pre">eq_rtol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-05</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L452-L522"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.AbstractNumericTag"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.jdftx.generic_tags.AbstractTag"
class="reference internal"
title="pymatgen.io.jdftx.generic_tags.AbstractTag"><span
class="pre"><code
class="sourceCode python">AbstractTag</code></span></a>

Abstract base class for numeric tags.

<span class="sig-name descname"><span class="pre">eq_atol</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">1e-08</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/generic_tags.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.AbstractNumericTag.eq_atol"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">eq_rtol</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">1e-05</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/generic_tags.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.AbstractNumericTag.eq_rtol"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">get_invalid_value_error_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L479-L497"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.generic_tags.AbstractNumericTag.get_invalid_value_error_str"
class="headerlink" title="Link to this definition"></a>  
Raise a ValueError for the invalid value.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to raise the ValueError for.

- **value** (*float* *\|* *int*) – The value to raise the ValueError
  for.

<span class="sig-name descname"><span class="pre">lb</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/generic_tags.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.AbstractNumericTag.lb"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">lb_incl</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">True</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/generic_tags.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.AbstractNumericTag.lb_incl"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">ub</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/generic_tags.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.AbstractNumericTag.ub"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">ub_incl</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">True</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/generic_tags.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.AbstractNumericTag.ub_incl"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">val_is_within_bounds</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L463-L477"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.generic_tags.AbstractNumericTag.val_is_within_bounds"
class="headerlink" title="Link to this definition"></a>  
Check if the value is within the bounds.

Parameters<span class="colon">:</span>  
**value** (*float* *\|* *int*) – The value to check.

Returns<span class="colon">:</span>  
True if the value is within the bounds, False otherwise.

Return type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">validate_value_bounds</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">bool</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L499-L506"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.generic_tags.AbstractNumericTag.validate_value_bounds"
class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">AbstractTag</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">multiline_tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">can_repeat</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">write_tagname</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">write_value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">optional</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">defer_until_struc</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">is_tag_container</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">allow_list_representation</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L39-L271"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.AbstractTag" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.jdftx.generic_tags.ClassPrintFormatter"
class="reference internal"
title="pymatgen.io.jdftx.generic_tags.ClassPrintFormatter"><span
class="pre"><code
class="sourceCode python">ClassPrintFormatter</code></span></a>, <span
class="pre">`ABC`</span>

Abstract base class for all tags.

<span class="sig-name descname"><span class="pre">allow_list_representation</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">False</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/generic_tags.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.generic_tags.AbstractTag.allow_list_representation"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">can_repeat</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">False</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/generic_tags.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.AbstractTag.can_repeat"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">defer_until_struc</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">False</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/generic_tags.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.AbstractTag.defer_until_struc"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">get_dict_representation</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L261-L271"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.generic_tags.AbstractTag.get_dict_representation"
class="headerlink" title="Link to this definition"></a>  
Convert the value to a dict representation.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to convert the value to a dict
  representation for.

- **value** (*Any*) – The value to convert to a dict representation.

Returns<span class="colon">:</span>  
The value converted to a dict representation.

Return type<span class="colon">:</span>  
dict \| list\[dict\]

<span class="sig-name descname"><span class="pre">get_list_representation</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L249-L259"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.generic_tags.AbstractTag.get_list_representation"
class="headerlink" title="Link to this definition"></a>  
Convert the value to a list representation.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to convert the value to a list
  representation for.

- **value** (*Any*) – The value to convert to a list representation.

Returns<span class="colon">:</span>  
The value converted to a list representation.

Return type<span class="colon">:</span>  
list \| list\[list\]

*<span class="k"><span class="pre">abstractmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">get_token_len</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">int</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L227-L233"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.AbstractTag.get_token_len"
class="headerlink" title="Link to this definition"></a>  
Get the token length of the tag.

Returns<span class="colon">:</span>  
The token length of the tag.

Return type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">is_equal_to</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">val1</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">obj2</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.jdftx.generic_tags.AbstractTag"
class="reference internal"
title="pymatgen.io.jdftx.generic_tags.AbstractTag"><span
class="pre">AbstractTag</span></a></span>*, *<span class="n"><span class="pre">val2</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L71-L90"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.AbstractTag.is_equal_to"
class="headerlink" title="Link to this definition"></a>  
Check if the two values are equal.

Parameters<span class="colon">:</span>  
- **val1** (*Any*) – The value of this tag object.

- **obj2** (<a href="#pymatgen.io.jdftx.generic_tags.AbstractTag"
  class="reference internal"
  title="pymatgen.io.jdftx.generic_tags.AbstractTag"><em>AbstractTag</em></a>)
  – The other tag object.

- **val2** (*Any*) – The value of the other tag object.

Returns<span class="colon">:</span>  
True if the two tag object/value pairs are equal, False otherwise.

Return type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">is_tag_container</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">False</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/generic_tags.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.AbstractTag.is_tag_container"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">multiline_tag</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">False</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/generic_tags.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.AbstractTag.multiline_tag"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">optional</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">True</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/generic_tags.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.AbstractTag.optional"
class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">abstractmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">read</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value_str</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Any</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L170-L180"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.AbstractTag.read"
class="headerlink" title="Link to this definition"></a>  
Read and parse the value string for this tag.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to read the value string for.

- **value_str** (*str*) – The value string to read.

Returns<span class="colon">:</span>  
The parsed value.

Return type<span class="colon">:</span>  
Any

<span class="sig-name descname"><span class="pre">validate_value_bounds</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">bool</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L163-L168"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.generic_tags.AbstractTag.validate_value_bounds"
class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">abstractmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">validate_value_type</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span></span>*, *<span class="n"><span class="pre">try_auto_type_fix</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">bool</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L57-L69"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.generic_tags.AbstractTag.validate_value_type"
class="headerlink" title="Link to this definition"></a>  
Validate the type of the value for this tag.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to validate the type of the value for.

- **value** (*Any*) – The value to validate the type of.

- **try_auto_type_fix** (*bool,* *optional*) – Whether to try to
  automatically fix the type of the value.

- **False.** (*Defaults to*)

Returns<span class="colon">:</span>  
The tag, whether the value is of the correct type, and the possibly
fixed value.

Return type<span class="colon">:</span>  
tuple\[str, bool, Any\]

*<span class="k"><span class="pre">abstractmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">write</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L215-L225"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.AbstractTag.write"
class="headerlink" title="Link to this definition"></a>  
Write the tag and its value as a string.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to write.

- **value** (*Any*) – The value to write.

Returns<span class="colon">:</span>  
The tag and its value as a string.

Return type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">write_tagname</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">True</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/generic_tags.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.AbstractTag.write_tagname"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">write_value</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">True</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/generic_tags.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.AbstractTag.write_value"
class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">BoolTag</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">multiline_tag:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">can_repeat:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">write_tagname:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">True</span></span>*, *<span class="n"><span class="pre">write_value:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">True</span></span>*, *<span class="n"><span class="pre">optional:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">True</span></span>*, *<span class="n"><span class="pre">defer_until_struc:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">is_tag_container:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">allow_list_representation:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">\_TF_read_options:</span> <span class="pre">dict\[str</span></span>*, *<span class="n"><span class="pre">bool\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">\_TF_write_options:</span> <span class="pre">dict\[bool</span></span>*, *<span class="n"><span class="pre">str\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L274-L373"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.BoolTag" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.jdftx.generic_tags.AbstractTag"
class="reference internal"
title="pymatgen.io.jdftx.generic_tags.AbstractTag"><span
class="pre"><code
class="sourceCode python">AbstractTag</code></span></a>

Tag for boolean values in JDFTx input files.

Tag for boolean values in JDFTx input files.

<span class="sig-name descname"><span class="pre">get_token_len</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">int</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L367-L373"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.BoolTag.get_token_len"
class="headerlink" title="Link to this definition"></a>  
Get the token length of the tag.

Returns<span class="colon">:</span>  
The token length of the tag.

Return type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">raise_value_error</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L322-L329"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.BoolTag.raise_value_error"
class="headerlink" title="Link to this definition"></a>  
Raise a ValueError for the value string.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to raise the ValueError for.

- **value** (*str*) – The value string to raise the ValueError for.

<span class="sig-name descname"><span class="pre">read</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L331-L352"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.BoolTag.read"
class="headerlink" title="Link to this definition"></a>  
Read the value string for this tag.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to read the value string for.

- **value** (*str*) – The value string to read.

Returns<span class="colon">:</span>  
The parsed boolean value.

Return type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">validate_value_type</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span></span>*, *<span class="n"><span class="pre">try_auto_type_fix</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">bool</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L295-L307"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.BoolTag.validate_value_type"
class="headerlink" title="Link to this definition"></a>  
Validate the type of the value for this tag.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to validate the type of the value for.

- **value** (*Any*) – The value to validate the type of.

- **try_auto_type_fix** (*bool,* *optional*) – Whether to try to
  automatically fix the type of the value.

- **False.** (*Defaults to*)

Returns<span class="colon">:</span>  
The tag, whether the value is of the correct type, and the possibly
fixed value.

Return type<span class="colon">:</span>  
tuple\[str, bool, Any\]

<span class="sig-name descname"><span class="pre">write</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L354-L365"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.BoolTag.write"
class="headerlink" title="Link to this definition"></a>  
Write the tag and its value as a string.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to write.

- **value** (*Any*) – The value to write.

Returns<span class="colon">:</span>  
The tag and its value as a string.

Return type<span class="colon">:</span>  
str

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">BoolTagContainer</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">multiline_tag:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">can_repeat:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">write_tagname:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">True</span></span>*, *<span class="n"><span class="pre">write_value:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">True</span></span>*, *<span class="n"><span class="pre">optional:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">True</span></span>*, *<span class="n"><span class="pre">defer_until_struc:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">is_tag_container:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">True</span></span>*, *<span class="n"><span class="pre">allow_list_representation:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">linebreak_nth_entry:</span> <span class="pre">int</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">subtags:</span> <span class="pre">dict\[str</span></span>*, *<span class="n"><span class="pre">\~pymatgen.io.jdftx.generic_tags.AbstractTag\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L1291-L1325"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.BoolTagContainer"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.jdftx.generic_tags.TagContainer"
class="reference internal"
title="pymatgen.io.jdftx.generic_tags.TagContainer"><span
class="pre"><code
class="sourceCode python">TagContainer</code></span></a>

BoolTagContainer class for handling the subtags to the “dump” tag.

This class is used to handle the subtags to the “dump” tag. All subtags
are freqs for dump, and all values for these tags are boolean values
that are read given the existence of their “var” name.

<span class="sig-name descname"><span class="pre">read</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value_str</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L1299-L1325"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.BoolTagContainer.read"
class="headerlink" title="Link to this definition"></a>  
Read the value string for this tag.

This method reads the value string for this tag. It is used to parse the
value string for the tag and return the parsed value.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to read the value string for.

- **value_str** (*str*) – The value string to read.

Returns<span class="colon">:</span>  
The parsed value.

Return type<span class="colon">:</span>  
dict

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">ClassPrintFormatter</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L24-L36"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.ClassPrintFormatter"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Generic class for printing to command line in readable format.

Generic class for printing to command line in readable format.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">DumpTagContainer</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">multiline_tag:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">can_repeat:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">write_tagname:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">True</span></span>*, *<span class="n"><span class="pre">write_value:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">True</span></span>*, *<span class="n"><span class="pre">optional:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">True</span></span>*, *<span class="n"><span class="pre">defer_until_struc:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">is_tag_container:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">True</span></span>*, *<span class="n"><span class="pre">allow_list_representation:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">linebreak_nth_entry:</span> <span class="pre">int</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">subtags:</span> <span class="pre">dict\[str</span></span>*, *<span class="n"><span class="pre">\~pymatgen.io.jdftx.generic_tags.AbstractTag\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L1328-L1362"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.DumpTagContainer"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.jdftx.generic_tags.TagContainer"
class="reference internal"
title="pymatgen.io.jdftx.generic_tags.TagContainer"><span
class="pre"><code
class="sourceCode python">TagContainer</code></span></a>

DumpTagContainer class for handling the “dump” tag.

This class is used to handle the “dump” tag.

<span class="sig-name descname"><span class="pre">read</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value_str</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L1335-L1362"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.DumpTagContainer.read"
class="headerlink" title="Link to this definition"></a>  
Read the value string for this tag.

This method reads the value string for this tag. It is used to parse the
value string for the tag and return the parsed value.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to read the value string for.

- **value_str** (*str*) – The value string to read.

Returns<span class="colon">:</span>  
The parsed value.

Return type<span class="colon">:</span>  
dict

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">FloatTag</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">multiline_tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">can_repeat</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">write_tagname</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">write_value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">optional</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">defer_until_struc</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">is_tag_container</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">allow_list_representation</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">lb</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ub</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">lb_incl</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">ub_incl</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">eq_atol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-08</span></span>*, *<span class="n"><span class="pre">eq_rtol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-05</span></span>*, *<span class="n"><span class="pre">prec</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L585-L650"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.FloatTag" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.jdftx.generic_tags.AbstractNumericTag"
class="reference internal"
title="pymatgen.io.jdftx.generic_tags.AbstractNumericTag"><span
class="pre"><code
class="sourceCode python">AbstractNumericTag</code></span></a>

Tag for float values in JDFTx input files.

Tag for float values in JDFTx input files.

<span class="sig-name descname"><span class="pre">get_token_len</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">int</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L644-L650"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.FloatTag.get_token_len"
class="headerlink" title="Link to this definition"></a>  
Get the token length of the tag.

Returns<span class="colon">:</span>  
The token length of the tag.

Return type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">prec</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/generic_tags.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.FloatTag.prec"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">read</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L608-L623"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.FloatTag.read"
class="headerlink" title="Link to this definition"></a>  
Read the value string for this tag.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to read the value string for.

- **value** (*str*) – The value string to read.

Returns<span class="colon">:</span>  
The parsed float value.

Return type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">validate_value_type</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span></span>*, *<span class="n"><span class="pre">try_auto_type_fix</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">bool</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L594-L606"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.FloatTag.validate_value_type"
class="headerlink" title="Link to this definition"></a>  
Validate the type of the value for this tag.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to validate the type of the value for.

- **value** (*Any*) – The value to validate the type of.

- **try_auto_type_fix** (*bool,* *optional*) – Whether to try to
  automatically fix the type of the value, by default False.

Returns<span class="colon">:</span>  
The tag, whether the value is of the correct type, and the possibly
fixed value.

Return type<span class="colon">:</span>  
tuple\[str, bool, Any\]

<span class="sig-name descname"><span class="pre">write</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L625-L642"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.FloatTag.write"
class="headerlink" title="Link to this definition"></a>  
Write the tag and its value as a string.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to write.

- **value** (*Any*) – The value to write.

Returns<span class="colon">:</span>  
The tag and its value as a string.

Return type<span class="colon">:</span>  
str

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">InitMagMomTag</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">multiline_tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">can_repeat</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">write_tagname</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">write_value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">optional</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">defer_until_struc</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">is_tag_container</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">allow_list_representation</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L653-L721"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.InitMagMomTag"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.jdftx.generic_tags.AbstractTag"
class="reference internal"
title="pymatgen.io.jdftx.generic_tags.AbstractTag"><span
class="pre"><code
class="sourceCode python">AbstractTag</code></span></a>

Tag for initial-magnetic-moments tag in JDFTx input files.

Tag for initial-magnetic-moments tag in JDFTx input files.

<span class="sig-name descname"><span class="pre">get_token_len</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">int</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L711-L717"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.InitMagMomTag.get_token_len"
class="headerlink" title="Link to this definition"></a>  
Get the token length of the tag.

Returns<span class="colon">:</span>  
The token length of the tag.

Return type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">read</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L686-L697"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.InitMagMomTag.read"
class="headerlink" title="Link to this definition"></a>  
Read the value string for this tag.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to read the value string for.

- **value** (*str*) – The value string to read.

Returns<span class="colon">:</span>  
The parsed string value.

Return type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">validate_value_type</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span></span>*, *<span class="n"><span class="pre">try_auto_type_fix</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">bool</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L672-L684"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.generic_tags.InitMagMomTag.validate_value_type"
class="headerlink" title="Link to this definition"></a>  
Validate the type of the value for this tag.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to validate the type of the value for.

- **value** (*Any*) – The value to validate the type of.

- **try_auto_type_fix** (*bool,* *optional*) – Whether to try to
  automatically fix the type of the value, by default False.

Returns<span class="colon">:</span>  
The tag, whether the value is of the correct type, and the possibly
fixed value.

Return type<span class="colon">:</span>  
tuple\[str, bool, Any\]

<span class="sig-name descname"><span class="pre">write</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L699-L709"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.InitMagMomTag.write"
class="headerlink" title="Link to this definition"></a>  
Write the tag and its value as a string.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to write.

- **value** (*Any*) – The value to write.

Returns<span class="colon">:</span>  
The tag and its value as a string.

Return type<span class="colon">:</span>  
str

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">IntTag</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">multiline_tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">can_repeat</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">write_tagname</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">write_value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">optional</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">defer_until_struc</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">is_tag_container</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">allow_list_representation</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">lb</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ub</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">lb_incl</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">ub_incl</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">eq_atol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-08</span></span>*, *<span class="n"><span class="pre">eq_rtol</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1e-05</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L525-L582"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.IntTag" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.jdftx.generic_tags.AbstractNumericTag"
class="reference internal"
title="pymatgen.io.jdftx.generic_tags.AbstractNumericTag"><span
class="pre"><code
class="sourceCode python">AbstractNumericTag</code></span></a>

Tag for integer values in JDFTx input files.

Tag for integer values in JDFTx input files.

<span class="sig-name descname"><span class="pre">get_token_len</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">int</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L576-L582"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.IntTag.get_token_len"
class="headerlink" title="Link to this definition"></a>  
Get the token length of the tag.

Returns<span class="colon">:</span>  
The token length of the tag.

Return type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">read</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">int</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L546-L560"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.IntTag.read" class="headerlink"
title="Link to this definition"></a>  
Read the value string for this tag.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to read the value string for.

- **value** (*str*) – The value string to read.

Returns<span class="colon">:</span>  
The parsed integer value.

Return type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">validate_value_type</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span></span>*, *<span class="n"><span class="pre">try_auto_type_fix</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">bool</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L532-L544"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.IntTag.validate_value_type"
class="headerlink" title="Link to this definition"></a>  
Validate the type of the value for this tag.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to validate the type of the value for.

- **value** (*Any*) – The value to validate the type of.

- **try_auto_type_fix** (*bool,* *optional*) – Whether to try to
  automatically fix the type of the value, by default False.

Returns<span class="colon">:</span>  
The tag, whether the value is of the correct type, and the possibly
fixed value.

Return type<span class="colon">:</span>  
tuple\[str, bool, Any\]

<span class="sig-name descname"><span class="pre">write</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L562-L574"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.IntTag.write"
class="headerlink" title="Link to this definition"></a>  
Write the tag and its value as a string.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to write.

- **value** (*Any*) – The value to write.

Returns<span class="colon">:</span>  
The tag and its value as a string.

Return type<span class="colon">:</span>  
str

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">MultiformatTag</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">multiline_tag:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">can_repeat:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">write_tagname:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">True</span></span>*, *<span class="n"><span class="pre">write_value:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">True</span></span>*, *<span class="n"><span class="pre">optional:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">True</span></span>*, *<span class="n"><span class="pre">defer_until_struc:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">is_tag_container:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">allow_list_representation:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">format_options:</span> <span class="pre">list\[\~pymatgen.io.jdftx.generic_tags.AbstractTag\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L1143-L1288"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.MultiformatTag"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.jdftx.generic_tags.AbstractTag"
class="reference internal"
title="pymatgen.io.jdftx.generic_tags.AbstractTag"><span
class="pre"><code
class="sourceCode python">AbstractTag</code></span></a>

Class for tags with multiple format options.

Class for tags that could have different types of input values given to
them or tags where different subtag options directly impact how many
expected arguments are provided e.g. the coulomb-truncation or
van-der-waals tags.

This class should not be used for tags with simply some combination of
mandatory and optional args because the TagContainer class can handle
those cases by itself.

<span class="sig-name descname"><span class="pre">format_options</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.io.jdftx.generic_tags.AbstractTag"
class="reference internal"
title="pymatgen.io.jdftx.generic_tags.AbstractTag"><span
class="pre">AbstractTag</span></a><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/generic_tags.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.MultiformatTag.format_options"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">get_format_index_for_str_value</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">int</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L1203-L1226"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.generic_tags.MultiformatTag.get_format_index_for_str_value"
class="headerlink" title="Link to this definition"></a>  
Get the format index from string representation of value.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to read the value string for.

- **value** (*str*) – The value string to read.

Returns<span class="colon">:</span>  
The index of the format option for the value of this tag.

Return type<span class="colon">:</span>  
int

Raises<span class="colon">:</span>  
**ValueError** – If no valid read format is found for the tag.

<span class="sig-name descname"><span class="pre">get_token_len</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">int</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L1276-L1285"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.MultiformatTag.get_token_len"
class="headerlink" title="Link to this definition"></a>  
Get the token length of the tag.

Returns<span class="colon">:</span>  
The token length of the tag.

Return type<span class="colon">:</span>  
int

Raises<span class="colon">:</span>  
**NotImplementedError** – If the method is called directly on
MultiformatTag objects.

<span class="sig-name descname"><span class="pre">raise_invalid_format_option_error</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">i</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L1228-L1238"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.generic_tags.MultiformatTag.raise_invalid_format_option_error"
class="headerlink" title="Link to this definition"></a>  
Raise an error for an invalid format option.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to raise the error for.

- **i** (*int*) – The index of the format option to raise the error for.

Raises<span class="colon">:</span>  
**ValueError** – If the format option is invalid.

<span class="sig-name descname"><span class="pre">read</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L1172-L1184"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.MultiformatTag.read"
class="headerlink" title="Link to this definition"></a>  
Read the value string for this tag.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to read the value string for.

- **value** (*str*) – The value string to read.

Raises<span class="colon">:</span>  
**RuntimeError** – If the method is called directly on MultiformatTag.

<span class="sig-name descname"><span class="pre">validate_value_type</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span></span>*, *<span class="n"><span class="pre">try_auto_type_fix</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">bool</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L1156-L1170"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.generic_tags.MultiformatTag.validate_value_type"
class="headerlink" title="Link to this definition"></a>  
Validate the type of the value for this tag.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to validate the value type for.

- **value** (*Any*) – The value to validate the type of.

- **try_auto_type_fix** (*bool,* *optional*) – Whether to try to
  automatically fix the type of the value. Defaults to False.

Returns<span class="colon">:</span>  
The tag, whether the value is of the correct type, and the possibly
fixed value.

Return type<span class="colon">:</span>  
tuple\[str, bool, Any\]

<span class="sig-name descname"><span class="pre">write</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L1186-L1201"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.MultiformatTag.write"
class="headerlink" title="Link to this definition"></a>  
Write the tag and its value as a string.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to write.

- **value** (*Any*) – The value to write.

Returns<span class="colon">:</span>  
The tag and its value as a string.

Return type<span class="colon">:</span>  
str

Raises<span class="colon">:</span>  
**RuntimeError** – If the method is called directly on MultiformatTag.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">StrTag</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">multiline_tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">can_repeat</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">write_tagname</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">write_value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">optional</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">defer_until_struc</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">is_tag_container</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">allow_list_representation</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">options</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L376-L449"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.StrTag" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.jdftx.generic_tags.AbstractTag"
class="reference internal"
title="pymatgen.io.jdftx.generic_tags.AbstractTag"><span
class="pre"><code
class="sourceCode python">AbstractTag</code></span></a>

Tag for string values in JDFTx input files.

Tag for string values in JDFTx input files.

<span class="sig-name descname"><span class="pre">get_token_len</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">int</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L443-L449"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.StrTag.get_token_len"
class="headerlink" title="Link to this definition"></a>  
Get the token length of the tag.

Returns<span class="colon">:</span>  
The token length of the tag.

Return type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">options</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/generic_tags.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.StrTag.options"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">read</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L416-L429"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.StrTag.read" class="headerlink"
title="Link to this definition"></a>  
Read the value string for this tag.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to read the value string for.

- **value** (*str*) – The value string to read.

Returns<span class="colon">:</span>  
The parsed string value.

Return type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">validate_value_type</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span></span>*, *<span class="n"><span class="pre">try_auto_type_fix</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">bool</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L385-L397"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.StrTag.validate_value_type"
class="headerlink" title="Link to this definition"></a>  
Validate the type of the value for this tag.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to validate the type of the value for.

- **value** (*Any*) – The value to validate the type of.

- **try_auto_type_fix** (*bool,* *optional*) – Whether to try to
  automatically fix the type of the value. Defaults to False.

Returns<span class="colon">:</span>  
The tag, whether the value is of the correct type, and the possibly
fixed value.

Return type<span class="colon">:</span>  
tuple\[str, bool, Any\]

<span class="sig-name descname"><span class="pre">write</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L431-L441"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.StrTag.write"
class="headerlink" title="Link to this definition"></a>  
Write the tag and its value as a string.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to write.

- **value** (*Any*) – The value to write.

Returns<span class="colon">:</span>  
The tag and its value as a string.

Return type<span class="colon">:</span>  
str

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">TagContainer</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">multiline_tag:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">can_repeat:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">write_tagname:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">True</span></span>*, *<span class="n"><span class="pre">write_value:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">True</span></span>*, *<span class="n"><span class="pre">optional:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">True</span></span>*, *<span class="n"><span class="pre">defer_until_struc:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">is_tag_container:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">True</span></span>*, *<span class="n"><span class="pre">allow_list_representation:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">linebreak_nth_entry:</span> <span class="pre">int</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">subtags:</span> <span class="pre">dict\[str</span></span>*, *<span class="n"><span class="pre">\~pymatgen.io.jdftx.generic_tags.AbstractTag\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L724-L1136"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.TagContainer"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.jdftx.generic_tags.AbstractTag"
class="reference internal"
title="pymatgen.io.jdftx.generic_tags.AbstractTag"><span
class="pre"><code
class="sourceCode python">AbstractTag</code></span></a>

TagContainer class for handling tags that contain other tags.

This class is used to handle tags that contain other tags. It is used to
validate the type of the value for the tag, read the value string for
the tag, write the tag and its value as a string, and get the token
length of the tag.

Note: When constructing a TagContainer, all subtags must be able to
return the correct token length without any information about the value.
\# TODO: Remove this assumption by changing the signature of
get_token_len to take the value as an argument.

<span class="sig-name descname"><span class="pre">get_dict_representation</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L1074-L1114"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.generic_tags.TagContainer.get_dict_representation"
class="headerlink" title="Link to this definition"></a>  
Convert the value to a dict representation.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to convert the value to a dict
  representation for.

- **value** (*list*) – The value to convert to a dict representation.

Returns<span class="colon">:</span>  
The value converted to a dict representation.

Return type<span class="colon">:</span>  
dict \| list\[dict\]

<span class="sig-name descname"><span class="pre">get_list_representation</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L1009-L1041"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.generic_tags.TagContainer.get_list_representation"
class="headerlink" title="Link to this definition"></a>  
Convert the value to a list representation.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to convert the value to a list
  representation for.

- **value** (*Any*) – The value to convert to a list representation.

Returns<span class="colon">:</span>  
The value converted to a list representation.

Return type<span class="colon">:</span>  
list

<span class="sig-name descname"><span class="pre">get_token_len</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">int</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L963-L974"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.TagContainer.get_token_len"
class="headerlink" title="Link to this definition"></a>  
Get the token length of the tag.

Returns<span class="colon">:</span>  
The token length of the tag.

Return type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">is_tag_container</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">True</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/generic_tags.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.TagContainer.is_tag_container"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">linebreak_nth_entry</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/generic_tags.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.generic_tags.TagContainer.linebreak_nth_entry"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">read</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L848-L913"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.TagContainer.read"
class="headerlink" title="Link to this definition"></a>  
Read the value string for this tag.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to read the value string for.

- **value** (*str*) – The value string to read.

Returns<span class="colon">:</span>  
The parsed value.

Return type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">subtags</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><a href="#pymatgen.io.jdftx.generic_tags.AbstractTag"
class="reference internal"
title="pymatgen.io.jdftx.generic_tags.AbstractTag"><span
class="pre">AbstractTag</span></a><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/generic_tags.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.TagContainer.subtags"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">validate_value_bounds</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">bool</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L775-L803"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.generic_tags.TagContainer.validate_value_bounds"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">validate_value_type</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span></span>*, *<span class="n"><span class="pre">try_auto_type_fix</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">bool</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L805-L846"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.generic_tags.TagContainer.validate_value_type"
class="headerlink" title="Link to this definition"></a>  
Validate the type of the value for this tag.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to validate the type of the value for.

- **value** (*Any*) – The value to validate the type of.

- **try_auto_type_fix** (*bool,* *optional*) – Whether to try to
  automatically fix the type of the value, by default False.

Returns<span class="colon">:</span>  
The tag, whether the value is of the correct type, and the possibly
fixed value.

Return type<span class="colon">:</span>  
tuple\[str, bool, Any\]

<span class="sig-name descname"><span class="pre">write</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/generic_tags.py#L915-L961"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.generic_tags.TagContainer.write"
class="headerlink" title="Link to this definition"></a>  
Write the tag and its value as a string.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – The tag to write.

- **value** (*Any*) – The value to write.

Returns<span class="colon">:</span>  
The tag and its value as a string.

Return type<span class="colon">:</span>  
str

</div>

<div id="module-pymatgen.io.jdftx.inputs" class="section">

<span id="pymatgen-io-jdftx-inputs-module"></span>

## pymatgen.io.jdftx.inputs module<a href="#module-pymatgen.io.jdftx.inputs" class="headerlink"
title="Link to this heading"></a>

Classes for reading/manipulating/writing JDFTx input files.

Classes for reading/manipulating/writing JDFTx input files.

Note: JDFTXInfile will be moved back to its own module once a more broad
inputs class is written.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">JDFTXInfile</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">params</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L59-L838"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`dict`</span>, <span
class="pre">`MSONable`</span>

Class for reading/writing JDFtx input files.

JDFTxInfile object for reading and writing JDFTx input files.
Essentially a dictionary with some helper functions.

Create a JDFTXInfile object.

Parameters<span class="colon">:</span>  
**params** (*dict*) – Input parameters as a dictionary.

<span class="sig-name descname"><span class="pre">append_tag</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L475-L497"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.append_tag"
class="headerlink" title="Link to this definition"></a>  
Append a value to a tag.

Append a value to a tag. Use this method instead of directly appending
the list contained in the tag, such that the value is properly
processed.

Parameters<span class="colon">:</span>  
- **tag** (*str*) – Tag to append to.

- **value** (*Any*) – Value to append.

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">sort_tags</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">skip_module_keys</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L360-L376"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.as_dict"
class="headerlink" title="Link to this definition"></a>  
Return JDFTXInfile as MSONable dict.

Parameters<span class="colon">:</span>  
- **sort_tags** (*bool,* *optional*) – Whether to sort the tags.
  Defaults to True.

- **skip_module_keys** (*bool,* *optional*) – Whether to skip the module
  keys. Defaults to False.

Returns<span class="colon">:</span>  
JDFTXInfile as MSONable dict.

Return type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">copy</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile"><span
class="pre">JDFTXInfile</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L378-L384"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.copy" class="headerlink"
title="Link to this definition"></a>  
Return a copy of the JDFTXInfile object.

Returns<span class="colon">:</span>  
Copy of the JDFTXInfile object.

Return type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile">JDFTXInfile</a>

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">d</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">validate_value_boundaries</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile"><span
class="pre">JDFTXInfile</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L169-L185"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.from_dict"
class="headerlink" title="Link to this definition"></a>  
Create JDFTXInfile from a dictionary.

Parameters<span class="colon">:</span>  
**d** (*dict*) – Dictionary to create JDFTXInfile from.

Returns<span class="colon">:</span>  
The created JDFTXInfile object.

Return type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile">JDFTXInfile</a>

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*, *<span class="n"><span class="pre">dont_require_structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">sort_tags</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">assign_path_parent</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">validate_value_boundaries</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile"><span
class="pre">JDFTXInfile</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L187-L218"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.from_file"
class="headerlink" title="Link to this definition"></a>  
Read a JDFTXInfile object from a file.

Parameters<span class="colon">:</span>  
- **filename** (*PathLike*) – Filename to read from.

- **dont_require_structure** (*bool,* *optional*) – Whether to require
  structure tags. Defaults to False.

- **sort_tags** (*bool,* *optional*) – Whether to sort the tags.
  Defaults to True.

- **assign_path_parent** (*bool,* *optional*) – Whether to assign the
  parent directory of the input file for include tags. Defaults to True.

Returns<span class="colon">:</span>  
The created JDFTXInfile object.

Return type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile">JDFTXInfile</a>

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_jdftxstructure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">jdftxstructure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.jdftx.inputs.JDFTXStructure"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXStructure"><span
class="pre">JDFTXStructure</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile"><span
class="pre">JDFTXInfile</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L241-L255"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.from_jdftxstructure"
class="headerlink" title="Link to this definition"></a>  
Create a JDFTXInfile object from a JDFTXStructure object.

Parameters<span class="colon">:</span>  
**jdftxstructure** (<a href="#pymatgen.io.jdftx.inputs.JDFTXStructure"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXStructure"><em>JDFTXStructure</em></a>)
– JDFTXStructure object to convert.

Returns<span class="colon">:</span>  
The created JDFTXInfile object.

Return type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile">JDFTXInfile</a>

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">string</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">dont_require_structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">sort_tags</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">path_parent</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Path</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">validate_value_boundaries</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile"><span
class="pre">JDFTXInfile</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L257-L312"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.from_str"
class="headerlink" title="Link to this definition"></a>  
Read a JDFTXInfile object from a string.

Parameters<span class="colon">:</span>  
- **string** (*str*) – String to read from.

- **dont_require_structure** (*bool,* *optional*) – Whether to require
  structure tags. Defaults to False.

- **sort_tags** (*bool,* *optional*) – Whether to sort the tags.
  Defaults to True.

- **path_parent** (*Path,* *optional*) – Path to the parent directory of
  the input file for include tags. Defaults to None.

- **validate_value_boundaries** (*bool,* *optional*) – Whether to
  validate the value boundaries. Defaults to True.

Returns<span class="colon">:</span>  
The created JDFTXInfile object.

Return type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile">JDFTXInfile</a>

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_structure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*, *<span class="n"><span class="pre">selective_dynamics</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">write_cart_coords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile"><span
class="pre">JDFTXInfile</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L220-L239"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.from_structure"
class="headerlink" title="Link to this definition"></a>  
Create a JDFTXInfile object from a pymatgen Structure.

Parameters<span class="colon">:</span>  
- **structure**
  (<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
  class="reference internal"
  title="pymatgen.core.structure.Structure"><em>Structure</em></a>) –
  Structure to convert.

- **selective_dynamics** (*ArrayLike,* *optional*) – Selective dynamics
  attribute for each site if available. Shape Nx1, by default None.

Returns<span class="colon">:</span>  
The created JDFTXInfile object.

Return type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile">JDFTXInfile</a>

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">get_dict_representation</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">jdftxinfile</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile"><span
class="pre">JDFTXInfile</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile"><span
class="pre">JDFTXInfile</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L336-L358"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.get_dict_representation"
class="headerlink" title="Link to this definition"></a>  
Convert JDFTXInfile object properties into dict representation.

Parameters<span class="colon">:</span>  
**jdftxinfile** (<a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile"><em>JDFTXInfile</em></a>) –
JDFTXInfile object to convert.

<span class="sig-name descname"><span class="pre">get_differing_tags</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile"><span
class="pre">JDFTXInfile</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L634-L645"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.get_differing_tags"
class="headerlink" title="Link to this definition"></a>  
Return which tags differ between self and other JDFTXInfile.

Parameters<span class="colon">:</span>  
**other** (<a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile"><em>JDFTXInfile</em></a>) –
Other JDFTXInfile object to compare to.

Returns<span class="colon">:</span>  
Tags that differ between the two JDFTXInfile objects.

Return type<span class="colon">:</span>  
list\[str\]

<span class="sig-name descname"><span class="pre">get_differing_tags_from</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile"><span
class="pre">JDFTXInfile</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L648-L681"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.get_differing_tags_from"
class="headerlink" title="Link to this definition"></a>  
Return which self-contained tags differ from other JDFTXInfile.

Parameters<span class="colon">:</span>  
**other** (<a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile"><em>JDFTXInfile</em></a>) –
Other JDFTXInfile object to compare to.

Returns<span class="colon">:</span>  
Tags from this JDFTXInfile that differ from the other JDFTXInfile.

Return type<span class="colon">:</span>  
list\[str\]

<span class="sig-name descname"><span class="pre">get_filtered_differing_tags</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile"><span
class="pre">JDFTXInfile</span></a></span>*, *<span class="n"><span class="pre">exclude_tags</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">exclude_tag_categories</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ensure_include_tags</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L592-L631"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.inputs.JDFTXInfile.get_filtered_differing_tags"
class="headerlink" title="Link to this definition"></a>  
Return which tags differ between self and other JDFTXInfile.

Returns a list of tags that differ between the two JDFTXInfile objects,
excluding any tags specified in exclude_tags or exclude_tag_categories.
This is useful for comparing two JDFTXInfile objects while ignoring
certain tags that are expected to differ.

Parameters<span class="colon">:</span>  
- **other** (<a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
  class="reference internal"
  title="pymatgen.io.jdftx.inputs.JDFTXInfile"><em>JDFTXInfile</em></a>)
  – Other JDFTXInfile object to compare to.

- **exclude_tags** (*list\[str\],* *optional*) – Tags to exclude from
  comparison. Defaults to None. Set to contain tags you are already
  accounting for being different to exclude them.

- **exclude_tag_categories** (*list\[str\],* *optional*) – Tag
  categories to exclude from comparison. Defaults to None. Add all tags
  of specified tag categories to be excluded in the comparison.

- **ensure_include_tags** (*list\[str\],* *optional*) – Tags to ensure
  are included in the comparison. Defaults to None. Helpful for tags in
  categories you want to exclude but want to ensure are included in the
  comparison.

Returns<span class="colon">:</span>  
Tags that differ between the two JDFTXInfile objects.

Return type<span class="colon">:</span>  
list\[str\]

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">get_list_representation</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">jdftxinfile</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile"><span
class="pre">JDFTXInfile</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile"><span
class="pre">JDFTXInfile</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L314-L334"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.get_list_representation"
class="headerlink" title="Link to this definition"></a>  
Convert JDFTXInfile object properties into list representation.

Parameters<span class="colon">:</span>  
**jdftxinfile** (<a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile"><em>JDFTXInfile</em></a>) –
JDFTXInfile object to convert.

<span class="sig-name descname"><span class="pre">get_text_list</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L386-L411"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.get_text_list"
class="headerlink" title="Link to this definition"></a>  
Get a list of strings representation of the JDFTXInfile.

Returns<span class="colon">:</span>  
List of strings representation of the JDFTXInfile.

Return type<span class="colon">:</span>  
list\[str\]

<span class="sig-name descname"><span class="pre">is_comparable_to</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile"><span
class="pre">JDFTXInfile</span></a></span>*, *<span class="n"><span class="pre">exclude_tags</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">exclude_tag_categories</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ensure_include_tags</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L557-L590"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.is_comparable_to"
class="headerlink" title="Link to this definition"></a>  
Check if two JDFTXInfile objects are comparable.

Parameters<span class="colon">:</span>  
- **other** (<a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
  class="reference internal"
  title="pymatgen.io.jdftx.inputs.JDFTXInfile"><em>JDFTXInfile</em></a>)
  – Other JDFTXInfile object to compare to.

- **exclude_tags** (*list\[str\],* *optional*) – Tags to exclude from
  comparison. Defaults to None. Set to contain tags you are already
  accounting for being different to exclude them.

- **exclude_tag_categories** (*list\[str\],* *optional*) – Tag
  categories to exclude from comparison. Defaults to None. If left as
  None, will exclude all tags in the “export”, “restart”, and
  “structure” categories. Add all tags of specified tag categories to be
  excluded in the comparison.

- **ensure_include_tags** (*list\[str\],* *optional*) – Tags to ensure
  are included in the comparison. Defaults to None. If left as None,
  will make sure ‘ion-species’ is included in comparison. Helpful for
  tags in categories you want to exclude but want to ensure are included
  in the comparison.

Returns<span class="colon">:</span>  
Whether the two JDFTXInfile objects are comparable.

Return type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">path_parent</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.path_parent"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">strip_structure_tags</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L464-L473"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.strip_structure_tags"
class="headerlink" title="Link to this definition"></a>  
Strip all structural tags from the JDFTXInfile.

Strip all structural tags from the JDFTXInfile. This is useful for
preparing a JDFTXInfile object from a pre-existing calculation for a new
structure.

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">structure</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.structure"
class="headerlink" title="Link to this definition"></a>  
Return a pymatgen Structure object.

Returns<span class="colon">:</span>  
Pymatgen structure object.

Return type<span class="colon">:</span>  
<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure">Structure</a>

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">to_jdftxstructure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">jdftxinfile</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile"><span
class="pre">JDFTXInfile</span></a></span>*, *<span class="n"><span class="pre">sort_structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.jdftx.inputs.JDFTXStructure"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXStructure"><span
class="pre">JDFTXStructure</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L422-L436"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.to_jdftxstructure"
class="headerlink" title="Link to this definition"></a>  
Convert JDFTXInfile to JDFTXStructure object.

Converts JDFTx lattice, lattice-scale, ion tags into JDFTXStructure,
with Pymatgen structure as attribute.

Parameters<span class="colon">:</span>  
- **jdftxinfile** (<a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
  class="reference internal"
  title="pymatgen.io.jdftx.inputs.JDFTXInfile"><em>JDFTXInfile</em></a>)
  – JDFTXInfile object to convert.

- **sort_structure** (*bool,* *optional*) – Whether to sort the
  structure. Useful if species are not grouped properly together.
  Defaults to False.

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">to_pmg_structure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">jdftxinfile</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile"><span
class="pre">JDFTXInfile</span></a></span>*, *<span class="n"><span class="pre">sort_structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L438-L462"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.to_pmg_structure"
class="headerlink" title="Link to this definition"></a>  
Convert JDFTXInfile to pymatgen Structure object.

Converts JDFTx lattice, lattice-scale, ion tags into pymatgen Structure.

Parameters<span class="colon">:</span>  
- **jdftxinfile** (<a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
  class="reference internal"
  title="pymatgen.io.jdftx.inputs.JDFTXInfile"><em>JDFTXInfile</em></a>)
  – JDFTXInfile object to convert.

- **sort_structure** (*bool,* *optional*) – Whether to sort the
  structure. Useful if species are not grouped properly together.
  Defaults to False.

Returns<span class="colon">:</span>  
The created pymatgen Structure object.

Return type<span class="colon">:</span>  
<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure">Structure</a>

<span class="sig-name descname"><span class="pre">validate_boundaries</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L537-L554"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.validate_boundaries"
class="headerlink" title="Link to this definition"></a>  
Validate the boundaries of the JDFTXInfile.

Validate the boundaries of the JDFTXInfile. This is a placeholder for
future functionality.

<span class="sig-name descname"><span class="pre">validate_tags</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">try_auto_type_fix</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">error_on_failed_fix</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">return_list_rep</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L501-L535"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.validate_tags"
class="headerlink" title="Link to this definition"></a>  
Validate the tags in the JDFTXInfile.

Validate the tags in the JDFTXInfile. If try_auto_type_fix is True, will
attempt to fix the tags. If error_on_failed_fix is True, will raise an
error if the tags cannot be fixed. If return_list_rep is True, will
return the tags in list representation.

Parameters<span class="colon">:</span>  
- **try_auto_type_fix** (*bool,* *optional*) – Whether to attempt to fix
  the tags. Defaults to False.

- **error_on_failed_fix** (*bool,* *optional*) – Whether to raise an
  error if the tags cannot be fixed. Defaults to True.

- **return_list_rep** (*bool,* *optional*) – Whether to return the tags
  in list representation. Defaults to False.

<span class="sig-name descname"><span class="pre">write_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L413-L420"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile.write_file"
class="headerlink" title="Link to this definition"></a>  
Write JDFTXInfile to an in file.

Parameters<span class="colon">:</span>  
**filename** (*PathLike*) – Filename to write to.

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">JDFTXStructure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">selective_dynamics</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sort_structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">write_cart_coords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">velocities</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">constraint_types</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">constraint_vectors</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">hyperplane_group_names</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L879-L1196"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXStructure" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`MSONable`</span>

Object for representing the data in JDFTXStructure tags.

<span class="sig-name descname"><span class="pre">structure</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.structure"
class="headerlink" title="Link to this definition"></a>  
Associated Structure.

Type<span class="colon">:</span>  
<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure">Structure</a>

<span class="sig-name descname"><span class="pre">selective_dynamics</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.selective_dynamics"
class="headerlink" title="Link to this definition"></a>  
Selective dynamics attribute for each site if available. Shape Nx1.

Type<span class="colon">:</span>  
ArrayLike

<span class="sig-name descname"><span class="pre">sort_structure</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.sort_structure"
class="headerlink" title="Link to this definition"></a>  
Whether to sort the structure. Useful if species are not grouped
properly together. Defaults to False.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">write_cart_coords</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.write_cart_coords"
class="headerlink" title="Link to this definition"></a>  
Whether to write cartesian coordinates. Defaults to False.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">velocities</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.velocities"
class="headerlink" title="Link to this definition"></a>  
Velocities for each site if available. Kept separate from
structure.site_properties\[“velocities”\] to allow inhomogeneous
shaping.

Type<span class="colon">:</span>  
list\[np.ndarray \| list\[float\] \| None\]

<span class="sig-name descname"><span class="pre">constraint_types</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.constraint_types"
class="headerlink" title="Link to this definition"></a>  
Constraint types for each site if available. Kept separate from
structure.site_properties\[“constraint_types”\] to allow inhomogeneous
shaping.

Type<span class="colon">:</span>  
list\[str \| None\]

<span class="sig-name descname"><span class="pre">constraint_vectors</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.constraint_vectors"
class="headerlink" title="Link to this definition"></a>  
Constraint vectors for each site if available. Kept separate from
structure.site_properties\[“constraint_vectors”\] to allow inhomogeneous
shaping. i’th entry must be a list of vectors if the i’th
constraint_type is “HyperPlane”. Otherwise, a single vector is expected.

Type<span class="colon">:</span>  
list\[np.ndarray \| list\[np.ndarray\] \| None\]

<span class="sig-name descname"><span class="pre">hyperplane_group_names</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.inputs.JDFTXStructure.hyperplane_group_names"
class="headerlink" title="Link to this definition"></a>  
Group names for each site if available. Kept separate from
structure.site_properties\[“group_names”\] to allow inhomogeneous
shaping. i’th entry must be a list of group names if the i’th
constraint_type is “HyperPlane”. Otherwise, None is expected.

Type<span class="colon">:</span>  
list\[list\[str\] \| None\]

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L1166-L1181"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.as_dict"
class="headerlink" title="Link to this definition"></a>  
MSONable dict.

Returns<span class="colon">:</span>  
MSONable dictionary representation of the JDFTXStructure.

Return type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">constraint_types</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id0" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">constraint_vectors</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id1" class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">params</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">Self</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L1183-L1196"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.from_dict"
class="headerlink" title="Link to this definition"></a>  
Get JDFTXStructure from dict.

Parameters<span class="colon">:</span>  
**params** (*dict*) – Serialized JDFTXStructure.

Returns<span class="colon">:</span>  
The created JDFTXStructure object.

Return type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.inputs.JDFTXStructure"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXStructure">JDFTXStructure</a>

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.jdftx.inputs.JDFTXStructure"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXStructure"><span
class="pre">JDFTXStructure</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L999-L1009"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.from_file"
class="headerlink" title="Link to this definition"></a>  
Read JDFTXStructure from file.

Parameters<span class="colon">:</span>  
**filename** (*str*) – Filename to read from.

Returns<span class="colon">:</span>  
The created JDFTXStructure object.

Return type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.inputs.JDFTXStructure"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXStructure">JDFTXStructure</a>

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_jdftxinfile</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">jdftxinfile</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile"><span
class="pre">JDFTXInfile</span></a></span>*, *<span class="n"><span class="pre">sort_structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.jdftx.inputs.JDFTXStructure"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXStructure"><span
class="pre">JDFTXStructure</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L1011-L1072"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.from_jdftxinfile"
class="headerlink" title="Link to this definition"></a>  
Get JDFTXStructure from JDFTXInfile.

Parameters<span class="colon">:</span>  
- **jdftxinfile** (<a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
  class="reference internal"
  title="pymatgen.io.jdftx.inputs.JDFTXInfile"><em>JDFTXInfile</em></a>)
  – JDFTXInfile object.

- **sort_structure** (*bool,* *optional*) – Whether to sort the
  structure. Useful if species are not grouped properly together as
  JDFTx output will have species sorted.

Returns<span class="colon">:</span>  
The created JDFTXStructure object.

Return type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.inputs.JDFTXStructure"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXStructure">JDFTXStructure</a>

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">data</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.jdftx.inputs.JDFTXStructure"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXStructure"><span
class="pre">JDFTXStructure</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L987-L997"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.from_str"
class="headerlink" title="Link to this definition"></a>  
Read JDFTXStructure from string.

Parameters<span class="colon">:</span>  
**data** (*str*) – String to read from.

Returns<span class="colon">:</span>  
The created JDFTXStructure object.

Return type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.inputs.JDFTXStructure"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXStructure">JDFTXStructure</a>

<span class="sig-name descname"><span class="pre">get_str</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">in_cart_coords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L1074-L1151"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.get_str"
class="headerlink" title="Link to this definition"></a>  
Return a string to be written as JDFTXInfile tags.

Allows extra options as compared to calling str(JDFTXStructure)
directly.

Parameters<span class="colon">:</span>  
**in_cart_coords** (*bool,* *optional*) – Whether coordinates are output
in direct or Cartesian.

Returns<span class="colon">:</span>  
Representation of JDFTXInfile structure tags.

Return type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">hyperplane_group_names</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id2" class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">natoms</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.natoms"
class="headerlink" title="Link to this definition"></a>  
Return number of atoms.

Returns<span class="colon">:</span>  
Number of sites.

Return type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">selective_dynamics</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ArrayLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id3" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">sort_structure</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">False</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id4" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">structure</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id5" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">velocities</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id6" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">write_cart_coords</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">False</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/inputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id7" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">write_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">filename</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L1153-L1164"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.inputs.JDFTXStructure.write_file"
class="headerlink" title="Link to this definition"></a>  
Write JDFTXStructure to a file.

The supported kwargs are the same as those for the
JDFTXStructure.get_str method and are passed through directly.

Parameters<span class="colon">:</span>  
- **filename** (*PathLike*) – Filename to write to.

- **\*\*kwargs** – Kwargs to pass to JDFTXStructure.get_str.

<!-- -->

<span class="sig-name descname"><span class="pre">selective_dynamics_site_prop_to_jdftx_interpretable</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">selective_dynamics</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">ArrayLike</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/inputs.py#L860-L876"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.inputs.selective_dynamics_site_prop_to_jdftx_interpretable"
class="headerlink" title="Link to this definition"></a>  
Convert selective dynamics site property to JDFTX interpretable format.

Parameters<span class="colon">:</span>  
**selective_dynamics** (*list\[list\[bool\]\]*) – Selective dynamics
site property.

Returns<span class="colon">:</span>  
JDFTX interpretable format of selective dynamics.

Return type<span class="colon">:</span>  
ArrayLike

</div>

<div id="module-pymatgen.io.jdftx.jdftxinfile_default_inputs"
class="section">

<span id="pymatgen-io-jdftx-jdftxinfile-default-inputs-module"></span>

## pymatgen.io.jdftx.jdftxinfile_default_inputs module<a href="#module-pymatgen.io.jdftx.jdftxinfile_default_inputs"
class="headerlink" title="Link to this heading"></a>

</div>

<div id="module-pymatgen.io.jdftx.jdftxinfile_master_format"
class="section">

<span id="pymatgen-io-jdftx-jdftxinfile-master-format-module"></span>

## pymatgen.io.jdftx.jdftxinfile_master_format module<a href="#module-pymatgen.io.jdftx.jdftxinfile_master_format"
class="headerlink" title="Link to this heading"></a>

Master list of AbstractTag-type objects for JDFTx input file generation.

This module contains; - MASTER_TAG_LIST: a dictionary mapping tag
categories to dictionaries mapping

> <div>
>
> tag names to AbstractTag-type objects.
>
> </div>

- get_tag_object: a function that returns an AbstractTag-type object from  
  MASTER_TAG_LIST given a tag name.

<span class="sig-name descname"><span class="pre">get_dump_tag_container</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.jdftx.generic_tags.DumpTagContainer"
class="reference internal"
title="pymatgen.io.jdftx.generic_tags.DumpTagContainer"><span
class="pre">DumpTagContainer</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/jdftxinfile_master_format.py#L1394-L1407"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxinfile_master_format.get_dump_tag_container"
class="headerlink" title="Link to this definition"></a>  
Initialize a dump tag container.

Returns<span class="colon">:</span>  
The dump tag container.

Return type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.generic_tags.DumpTagContainer"
class="reference internal"
title="pymatgen.io.jdftx.generic_tags.DumpTagContainer">DumpTagContainer</a>

<!-- -->

<span class="sig-name descname"><span class="pre">get_tag_object</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.jdftx.generic_tags.AbstractTag"
class="reference internal"
title="pymatgen.io.jdftx.generic_tags.AbstractTag"><span
class="pre">AbstractTag</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/jdftxinfile_master_format.py#L1426-L1435"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxinfile_master_format.get_tag_object"
class="headerlink" title="Link to this definition"></a>  
Get the tag object for a given tag name.

Parameters<span class="colon">:</span>  
**tag** (*str*) – The tag name.

Returns<span class="colon">:</span>  
The tag object.

Return type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.generic_tags.AbstractTag"
class="reference internal"
title="pymatgen.io.jdftx.generic_tags.AbstractTag">AbstractTag</a>

<!-- -->

<span class="sig-name descname"><span class="pre">get_tag_object_on_val</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span>*, *<span class="n"><span class="pre">val</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.jdftx.generic_tags.AbstractTag"
class="reference internal"
title="pymatgen.io.jdftx.generic_tags.AbstractTag"><span
class="pre">AbstractTag</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/jdftxinfile_master_format.py#L1438-L1454"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxinfile_master_format.get_tag_object_on_val"
class="headerlink" title="Link to this definition"></a>  
Get the tag object for a given tag name.

Parameters<span class="colon">:</span>  
**tag** (*str*) – The tag name.

Returns<span class="colon">:</span>  
The tag object.

Return type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.generic_tags.AbstractTag"
class="reference internal"
title="pymatgen.io.jdftx.generic_tags.AbstractTag">AbstractTag</a>

</div>

<div id="module-pymatgen.io.jdftx.jdftxinfile_ref_options"
class="section">

<span id="pymatgen-io-jdftx-jdftxinfile-ref-options-module"></span>

## pymatgen.io.jdftx.jdftxinfile_ref_options module<a href="#module-pymatgen.io.jdftx.jdftxinfile_ref_options"
class="headerlink" title="Link to this heading"></a>

Module for containing reference data for JDFTx tags.

This module contains reference data for JDFTx tags, such as valid
options for functionals, pseudopotentials, etc.

</div>

<div id="module-pymatgen.io.jdftx.jdftxoutfileslice" class="section">

<span id="pymatgen-io-jdftx-jdftxoutfileslice-module"></span>

## pymatgen.io.jdftx.jdftxoutfileslice module<a href="#module-pymatgen.io.jdftx.jdftxoutfileslice" class="headerlink"
title="Link to this heading"></a>

JDFTx Outfile Slice Class.

This module defines the JDFTxOutfileSlice class, which is used to read
and process a JDFTx out file.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">JDFTXOutfileSlice</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">prefix</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">jstrucs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures"
class="reference internal"
title="pymatgen.io.jdftx.joutstructures.JOutStructures"><span
class="pre">JOutStructures</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">jsettings_fluid</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.jdftx.jminsettings.JMinSettings"
class="reference internal"
title="pymatgen.io.jdftx.jminsettings.JMinSettings"><span
class="pre">JMinSettings</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">jsettings_electronic</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.jdftx.jminsettings.JMinSettings"
class="reference internal"
title="pymatgen.io.jdftx.jminsettings.JMinSettings"><span
class="pre">JMinSettings</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">jsettings_lattice</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.jdftx.jminsettings.JMinSettings"
class="reference internal"
title="pymatgen.io.jdftx.jminsettings.JMinSettings"><span
class="pre">JMinSettings</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">jsettings_ionic</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.jdftx.jminsettings.JMinSettings"
class="reference internal"
title="pymatgen.io.jdftx.jminsettings.JMinSettings"><span
class="pre">JMinSettings</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">constant_lattice</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">xc_func</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">lattice_initial</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">np.ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">lattice_final</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">np.ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">lattice</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">np.ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">a</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">b</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">c</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">fftgrid</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">geom_opt</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">geom_opt_type</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">efermi</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">egap</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">optical_egap</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">emin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">emax</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">homo</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">lumo</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">homo_filling</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">lumo_filling</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">is_metal</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">etype</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">broadening_type</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">broadening</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">kgrid</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">truncation_type</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">truncation_radius</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">pwcut</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">rhocut</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">pp_type</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">semicore_electrons</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">valence_electrons</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">total_electrons_uncharged</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">semicore_electrons_uncharged</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">valence_electrons_uncharged</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">nbands</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">atom_elements</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">atom_elements_int</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">atom_types</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">spintype</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">nspin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">nat</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">atom_coords_initial</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">np.ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">atom_coords_final</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">np.ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">atom_coords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">np.ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">has_solvation</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">fluid</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">is_gc</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">is_bgw</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">has_eigstats</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">has_parsable_pseudo</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">\_total_electrons_backup</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">total_electrons</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">\_mu_backup</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">t_s</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">converged</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">initial_structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">trajectory</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.trajectory.Trajectory"
class="reference internal"
title="pymatgen.core.trajectory.Trajectory"><span
class="pre">Trajectory</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">electronic_output</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">eopt_type</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">elecmindata</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.jdftx.jelstep.JElSteps" class="reference internal"
title="pymatgen.io.jdftx.jelstep.JElSteps"><span
class="pre">JElSteps</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">stress</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">np.ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">strain</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">np.ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">forces</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">np.ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">nstep</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">e</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grad_k</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">alpha</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">linmin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">abs_magneticmoment</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">tot_magneticmoment</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">mu</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">elec_nstep</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">elec_e</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">elec_grad_k</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">elec_alpha</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">elec_linmin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">vibrational_modes</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">vibrational_energy_components</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/jdftxoutfileslice.py#L64-L1330"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

A class to read and process a slice of a JDFTx out file.

A class to read and process a slice of a JDFTx out file, where a “slice”
is a segment of an out file corresponding to a single call of JDFTx.

<span class="sig-name descname"><span class="pre">from_out_slice(text</span></span>  
list\[str\]): Read slice of out file into a JDFTXOutfileSlice instance.

<span class="sig-name descname"><span class="pre">prefix</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.prefix"
class="headerlink" title="Link to this definition"></a>  
Prefix of dump files for JDFTx calculation.

Type<span class="colon">:</span>  
str \| None

<span class="sig-name descname"><span class="pre">jstrucs</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.jstrucs"
class="headerlink" title="Link to this definition"></a>  
JOutStructures instance containing intermediate structures. Holds a
“slices” attribute, which is a list of JOutStructure instances. (A
JOutStructure instance functions as a Structure object, along with a
JElSteps instance (stored as elecmindata) and other
JDFTx-calculation-specific data.)

Type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.joutstructures.JOutStructures"
class="reference internal"
title="pymatgen.io.jdftx.joutstructures.JOutStructures">JOutStructures</a>
\| None

<span class="sig-name descname"><span class="pre">jsettings_fluid</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.jsettings_fluid"
class="headerlink" title="Link to this definition"></a>  
JMinSettings instance containing fluid optimization settings.

Type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.jminsettings.JMinSettings"
class="reference internal"
title="pymatgen.io.jdftx.jminsettings.JMinSettings">JMinSettings</a> \|
None

<span class="sig-name descname"><span class="pre">jsettings_electronic</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.jsettings_electronic"
class="headerlink" title="Link to this definition"></a>  
JMinSettings instance containing electronic optimization settings.

Type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.jminsettings.JMinSettings"
class="reference internal"
title="pymatgen.io.jdftx.jminsettings.JMinSettings">JMinSettings</a> \|
None

<span class="sig-name descname"><span class="pre">jsettings_lattice</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.jsettings_lattice"
class="headerlink" title="Link to this definition"></a>  
JMinSettings instance containing lattice optimization settings.

Type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.jminsettings.JMinSettings"
class="reference internal"
title="pymatgen.io.jdftx.jminsettings.JMinSettings">JMinSettings</a> \|
None

<span class="sig-name descname"><span class="pre">jsettings_ionic</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.jsettings_ionic"
class="headerlink" title="Link to this definition"></a>  
JMinSettings instance containing ionic optimization settings.

Type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.jminsettings.JMinSettings"
class="reference internal"
title="pymatgen.io.jdftx.jminsettings.JMinSettings">JMinSettings</a> \|
None

<span class="sig-name descname"><span class="pre">xc_func</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.xc_func"
class="headerlink" title="Link to this definition"></a>  
Exchange-correlation functional used in the calculation.

Type<span class="colon">:</span>  
str \| None

<span class="sig-name descname"><span class="pre">lattice_initial</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.lattice_initial"
class="headerlink" title="Link to this definition"></a>  
Initial lattice matrix in Angstroms.

Type<span class="colon">:</span>  
np.ndarray \| None

<span class="sig-name descname"><span class="pre">lattice_final</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.lattice_final"
class="headerlink" title="Link to this definition"></a>  
Final lattice matrix in Angstroms.

Type<span class="colon">:</span>  
np.ndarray \| None

<span class="sig-name descname"><span class="pre">lattice</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.lattice"
class="headerlink" title="Link to this definition"></a>  
Current lattice matrix in Angstroms.

Type<span class="colon">:</span>  
np.ndarray \| None

<span class="sig-name descname"><span class="pre">a</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.a"
class="headerlink" title="Link to this definition"></a>  
Lattice parameter a in Angstroms.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">b</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.b"
class="headerlink" title="Link to this definition"></a>  
Lattice parameter b in Angstroms.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">c</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.c"
class="headerlink" title="Link to this definition"></a>  
Lattice parameter c in Angstroms.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">fftgrid</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.fftgrid"
class="headerlink" title="Link to this definition"></a>  
Shape of FFT grid used in calculation (3 integers).

Type<span class="colon">:</span>  
list\[int\] \| None

<span class="sig-name descname"><span class="pre">geom_opt</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.geom_opt"
class="headerlink" title="Link to this definition"></a>  
True if geometric (lattice or ionic) optimization was performed.

Type<span class="colon">:</span>  
bool \| None

<span class="sig-name descname"><span class="pre">geom_opt_type</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.geom_opt_type"
class="headerlink" title="Link to this definition"></a>  
Type of geometric optimization performed (lattice or ionic, where
lattice implies ionic as well unless geometry was given in direct
coordinates).

Type<span class="colon">:</span>  
str \| None

<span class="sig-name descname"><span class="pre">efermi</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.efermi"
class="headerlink" title="Link to this definition"></a>  
Fermi energy in eV (may be None if eigstats are not dumped).

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">egap</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.egap"
class="headerlink" title="Link to this definition"></a>  
Band gap in eV (None if eigstats are not dumped).

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">emin</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.emin"
class="headerlink" title="Link to this definition"></a>  
Minimum energy in eV (None if eigstats are not dumped).

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">emax</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.emax"
class="headerlink" title="Link to this definition"></a>  
Maximum energy in eV (None if eigstats are not dumped).

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">homo</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.homo"
class="headerlink" title="Link to this definition"></a>  
Energy of last band-state before Fermi level (acronym for Highest
Occupied Molecular Orbital, even though these are not molecular orbitals
and this state may not be entirely occupied) (None if eigstats are not
dumped).

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">lumo</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.lumo"
class="headerlink" title="Link to this definition"></a>  
Energy of first band-state after Fermi level (acronym for Lowest
Unoccupied Molecular Orbital, even though these are not molecular
orbitals, and this state may not be entirely unoccupied) (None if
eigstats are not dumped).

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">homo_filling</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.homo_filling"
class="headerlink" title="Link to this definition"></a>  
Filling of “homo” band-state as calculated within this class object from
the homo energy, Fermi level, electronic broadening type and electronic
broadening parameter. (None if eigstats are not dumped).

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">lumo_filling</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.lumo_filling"
class="headerlink" title="Link to this definition"></a>  
Filling of “lumo” band-state as calculated within this class object from
the homo energy, Fermi level, electronic broadening type and electronic
broadening parameter. (None if eigstats are not dumped).

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">is_metal</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.is_metal"
class="headerlink" title="Link to this definition"></a>  
True if fillings of homo and lumo band-states are off-set by 1 and 0 by
at least an arbitrary tolerance of 0.01 (ie 1 - 0.015 and 0.012 for
homo/lumo fillings would be metallic, while 1-0.001 and 0 would not be).
(Only available if eigstats was dumped).

Type<span class="colon">:</span>  
bool \| None

<span class="sig-name descname"><span class="pre">etype</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.etype"
class="headerlink" title="Link to this definition"></a>  
String representation of total energy-type of system. Commonly “G”
(grand-canonical potential) for GC calculations, and “F” for canonical
(fixed electron count) calculations.

Type<span class="colon">:</span>  
str \| None

<span class="sig-name descname"><span class="pre">broadening_type</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.broadening_type"
class="headerlink" title="Link to this definition"></a>  
Type of broadening for electronic filling about Fermi-level requested.
Either “Fermi”, “Cold”, “MP1”, or “Gauss”.

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">broadening</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.broadening"
class="headerlink" title="Link to this definition"></a>  
Magnitude of broadening for electronic filling.

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">kgrid</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.kgrid"
class="headerlink" title="Link to this definition"></a>  
Shape of k-point grid used in calculation. (equivalent to k-point
folding).

Type<span class="colon">:</span>  
list\[int\]

<span class="sig-name descname"><span class="pre">truncation_type</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.truncation_type"
class="headerlink" title="Link to this definition"></a>  
Type of coulomb truncation used to prevent interaction between periodic
images along certain directions. “periodic” means no coulomb truncation
was used.

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">truncation_radius</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.truncation_radius"
class="headerlink" title="Link to this definition"></a>  
If spherical truncation_type, this is the radius of the coulomb
truncation sphere.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">pwcut</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.pwcut"
class="headerlink" title="Link to this definition"></a>  
The plane-wave cutoff energy in Hartrees used in the most recent JDFTx
call.

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">rhocut</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.rhocut"
class="headerlink" title="Link to this definition"></a>  
The density cutoff energy in Hartrees used in the most recent JDFTx
call.

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">pp_type</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.pp_type"
class="headerlink" title="Link to this definition"></a>  
The pseudopotential library used in the most recent JDFTx call.
Currently only “GBRV” and “SG15” are supported by this output parser.

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">total_electrons</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.total_electrons"
class="headerlink" title="Link to this definition"></a>  
The total number of electrons in the most recent JDFTx call (redundant
to nelectrons).

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">semicore_electrons</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.semicore_electrons"
class="headerlink" title="Link to this definition"></a>  
The number of semicore electrons in the most recent JDFTx call.

Type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">valence_electrons</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.valence_electrons"
class="headerlink" title="Link to this definition"></a>  
The number of valence electrons in the most recent JDFTx call.

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">total_electrons_uncharged</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.total_electrons_uncharged"
class="headerlink" title="Link to this definition"></a>  
The total number of electrons in the most recent JDFTx call, uncorrected
for charge. (ie total_electrons + charge).

Type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">semicore_electrons_uncharged</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.semicore_electrons_uncharged"
class="headerlink" title="Link to this definition"></a>  
The number of semicore electrons in the most recent JDFTx call,
uncorrected for charge. (ie semicore_electrons + charge).

Type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">valence_electrons_uncharged</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.valence_electrons_uncharged"
class="headerlink" title="Link to this definition"></a>  
The number of valence electrons in the most recent JDFTx call,
uncorrected for charge. (ie valence_electrons + charge).

Type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">nbands</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.nbands"
class="headerlink" title="Link to this definition"></a>  
The number of bands used in the most recent JDFTx call.

Type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">atom_elements</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.atom_elements"
class="headerlink" title="Link to this definition"></a>  
The list of each ion’s element symbol in the most recent JDFTx call.

Type<span class="colon">:</span>  
list\[str\]

<span class="sig-name descname"><span class="pre">atom_elements_int</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.atom_elements_int"
class="headerlink" title="Link to this definition"></a>  
The list of ion’s atomic numbers in the most recent JDFTx call.

Type<span class="colon">:</span>  
list\[int\]

<span class="sig-name descname"><span class="pre">atom_types</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.atom_types"
class="headerlink" title="Link to this definition"></a>  
Non-repeating list of each ion’s element symbol in the most recent JDFTx
call.

Type<span class="colon">:</span>  
list\[str\]

<span class="sig-name descname"><span class="pre">spintype</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.spintype"
class="headerlink" title="Link to this definition"></a>  
The spin type used in the most recent JDFTx call. Options are “none”,
“collinear”.

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">nspin</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.nspin"
class="headerlink" title="Link to this definition"></a>  
The number of spins used in the most recent JDFTx call.

Type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">nat</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.nat"
class="headerlink" title="Link to this definition"></a>  
The number of atoms in the most recent JDFTx call.

Type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">atom_coords_initial</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.atom_coords_initial"
class="headerlink" title="Link to this definition"></a>  
The initial atomic coordinates of the most recent JDFTx call.

Type<span class="colon">:</span>  
list\[list\[float\]\]

<span class="sig-name descname"><span class="pre">atom_coords_final</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.atom_coords_final"
class="headerlink" title="Link to this definition"></a>  
The final atomic coordinates of the most recent JDFTx call.

Type<span class="colon">:</span>  
list\[list\[float\]\]

<span class="sig-name descname"><span class="pre">atom_coords</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.atom_coords"
class="headerlink" title="Link to this definition"></a>  
The atomic coordinates of the most recent JDFTx call.

Type<span class="colon">:</span>  
list\[list\[float\]\]

<span class="sig-name descname"><span class="pre">has_solvation</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.has_solvation"
class="headerlink" title="Link to this definition"></a>  
True if the most recent JDFTx call included a solvation calculation.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">fluid</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.fluid"
class="headerlink" title="Link to this definition"></a>  
The fluid used in the most recent JDFTx call.

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">is_gc</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.is_gc"
class="headerlink" title="Link to this definition"></a>  
True if the most recent slice is a grand canonical calculation.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">is_bgw</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.is_bgw"
class="headerlink" title="Link to this definition"></a>  
True if data must be usable for a BerkeleyGW calculation (user-set).

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">has_eigstats</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.has_eigstats"
class="headerlink" title="Link to this definition"></a>  
True if eigstats were dumped in the most recent JDFTx call.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">has_parsable_pseudo</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.has_parsable_pseudo"
class="headerlink" title="Link to this definition"></a>  
True if the most recent JDFTx call used a pseudopotential that can be
parsed by this output parser. Options are currently “GBRV” and “SG15”.

Type<span class="colon">:</span>  
bool

Properties:  
t_s (float \| None): The total time in seconds for the calculation.
converged (bool \| None): True if calculation converged. trajectory
(Trajectory): pymatgen Trajectory object containing intermediate
Structure’s of outfile slice

> <div>
>
> calculation.
>
> </div>

electronic_output (dict): Dictionary with all relevant electronic
information dumped from an eigstats log. structure (Structure):
Calculation result as pymatgen Structure. initial_structure (Structure):
Initial structure of the calculation, as read from inputs portion of out
file. eopt_type (str \| None): eopt_type from most recent JOutStructure.
elecmindata (JElSteps): elecmindata from most recent JOutStructure.
stress (np.ndarray \| None): Stress tensor from most recent
JOutStructure in units eV/Ang^3. strain (np.ndarray \| None): Strain
tensor from most recent JOutStructure (unitless). nstep (int \| None):
(geometric) nstep from most recent JOutStructure. e (float \| None):
Energy of system “etype” from most recent JOutStructure. grad_k (float):
The final norm of the preconditioned gradient for geometric optimization
of the most recent

> <div>
>
> JDFTx call (evaluated as dot(g, Kg), where g is the gradient and Kg is
> the preconditioned gradient). (written as “[<span id="id9"
> class="problematic">\|</span>](#id8)grad\|\_K” in JDFTx output).
>
> </div>

alpha (float): The step size of the final geometric step in the most
recent JDFTx call. linmin (float): The final normalized projection of
the geometric step direction onto the gradient for the most

> <div>
>
> recent JDFTx call.
>
> </div>

abs_magneticmoment (float \| None): The absolute magnetic moment of the
most recent JDFTx call. tot_magneticmoment (float \| None): The total
magnetic moment of the most recent JDFTx call. mu (float): The Fermi
energy of the most recent JDFTx call. elec_e (float): The final energy
of the most recent electronic optimization step. elec_nstep (int): The
number of electronic optimization steps in the most recent JDFTx call.
elec_grad_k (float): The final norm of the preconditioned gradient for
electronic optimization of the most

> <div>
>
> recent JDFTx call (evaluated as dot(g, Kg), where g is the gradient
> and Kg is the preconditioned gradient). (written as “[<span id="id11"
> class="problematic">\|</span>](#id10)grad\|\_K” in JDFTx output).
>
> </div>

elec_alpha (float): The step size of the final electronic step in the
most recent JDFTx call. elec_linmin (float): The final normalized
projection of the electronic step direction onto the gradient for the

> <div>
>
> most recent JDFTx call.
>
> </div>

Magic Methods:  
\_\_getattr\_\_(name: str) -\> Any: Overwrite of default \_\_getattr\_\_ method to allow for reference of un-defined  
attributes to the “jstrucs” class field. This referring behavior is
ideally never used as (currently) all referrable attributes are defined
properties, but is included to prevent errors in the case of future
changes.

\_\_str\_\_() -\> str: Return a string representation of the class
instance using pprint module. \_\_repr\_\_() -\> str: Create string
representation of the class instance. Overwritten from default behavior
for

> <div>
>
> dataclass so that properties are included in the string, and verbose
> attributes with redundant information are trimmed.
>
> </div>

<span class="sig-name descname"><span class="pre">a</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id12" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">abs_magneticmoment</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.abs_magneticmoment"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">alpha</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.alpha"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/jdftxoutfileslice.py#L1283-L1296"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.as_dict"
class="headerlink" title="Link to this definition"></a>  
Convert dataclass to dictionary representation.

Returns<span class="colon">:</span>  
JDFTXOutfileSlice in dictionary format.

Return type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">atom_coords</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">np.ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id13" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">atom_coords_final</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">np.ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id14" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">atom_coords_initial</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">np.ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id15" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">atom_elements</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id16" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">atom_elements_int</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id17" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">atom_types</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id18" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">b</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id19" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">broadening</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id20" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">broadening_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id21" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">c</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id22" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">constant_lattice</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.constant_lattice"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">converged</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.converged"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">determine_is_metal</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/jdftxoutfileslice.py#L1149-L1164"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.determine_is_metal"
class="headerlink" title="Link to this definition"></a>  
Determine if the system is a metal based on the fillings of homo and
lumo.

Returns<span class="colon">:</span>  
True if system is metallic.

Return type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">e</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.e"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">efermi</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id23" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">egap</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id24" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">elec_alpha</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.elec_alpha"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">elec_e</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.elec_e"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">elec_grad_k</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.elec_grad_k"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">elec_linmin</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.elec_linmin"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">elec_nstep</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.elec_nstep"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">elecmindata</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="#pymatgen.io.jdftx.jelstep.JElSteps" class="reference internal"
title="pymatgen.io.jdftx.jelstep.JElSteps"><span
class="pre">JElSteps</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.elecmindata"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">electronic_output</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.electronic_output"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">emax</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id25" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">emin</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id26" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">eopt_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.eopt_type"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">etype</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id27" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">fftgrid</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id28" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">fluid</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id29" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">forces</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">np.ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.forces"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">geom_opt</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id30" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">geom_opt_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id31" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">grad_k</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.grad_k"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">has_eigstats</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">False</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id32" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">has_parsable_pseudo</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">False</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id33" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">has_solvation</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">False</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id34" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">homo</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id35" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">homo_filling</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id36" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">initial_structure</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.initial_structure"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">is_bgw</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">False</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id37" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">is_gc</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id38" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">is_metal</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id39" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">jsettings_electronic</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="#pymatgen.io.jdftx.jminsettings.JMinSettings"
class="reference internal"
title="pymatgen.io.jdftx.jminsettings.JMinSettings"><span
class="pre">JMinSettings</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id40" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">jsettings_fluid</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="#pymatgen.io.jdftx.jminsettings.JMinSettings"
class="reference internal"
title="pymatgen.io.jdftx.jminsettings.JMinSettings"><span
class="pre">JMinSettings</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id41" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">jsettings_ionic</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="#pymatgen.io.jdftx.jminsettings.JMinSettings"
class="reference internal"
title="pymatgen.io.jdftx.jminsettings.JMinSettings"><span
class="pre">JMinSettings</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id42" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">jsettings_lattice</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="#pymatgen.io.jdftx.jminsettings.JMinSettings"
class="reference internal"
title="pymatgen.io.jdftx.jminsettings.JMinSettings"><span
class="pre">JMinSettings</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id43" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">jstrucs</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures"
class="reference internal"
title="pymatgen.io.jdftx.joutstructures.JOutStructures"><span
class="pre">JOutStructures</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id44" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">kgrid</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id45" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">lattice</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">np.ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id46" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">lattice_final</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">np.ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id47" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">lattice_initial</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">np.ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id48" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">linmin</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.linmin"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">lumo</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id49" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">lumo_filling</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id50" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">mu</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.mu"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">nat</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id51" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">nbands</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id52" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">nspin</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id53" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">nstep</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.nstep"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">optical_egap</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.optical_egap"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">parsable_pseudos</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ClassVar</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">\['GBRV',</span> <span class="pre">'SG15'\]</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.parsable_pseudos"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">pp_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id54" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">prefix</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id55" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">pwcut</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id56" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">rhocut</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id57" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">semicore_electrons</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id58" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">semicore_electrons_uncharged</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id59" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">spintype</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id60" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">strain</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">np.ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.strain"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">stress</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">np.ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.stress"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">structure</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.structure"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">t_s</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.t_s"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">to_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../../../.venv/lib/python3.11/site-packages/monty/dev.py#L1298-L1300"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.to_dict"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">to_jdftxinfile</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile"><span
class="pre">JDFTXInfile</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/jdftxoutfileslice.py#L1249-L1265"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.to_jdftxinfile"
class="headerlink" title="Link to this definition"></a>  
Convert the JDFTXOutfile object to a JDFTXInfile object with the most
recent structure. If the input structure is desired, simply fetch
JDFTXOutfile.infile

Returns<span class="colon">:</span>  
A JDFTXInfile object representing the input parameters of the
JDFTXOutfile.

Return type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile">JDFTXInfile</a>

<span class="sig-name descname"><span class="pre">tot_magneticmoment</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.tot_magneticmoment"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">total_electrons</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id61" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">total_electrons_uncharged</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id62" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">trajectory</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.trajectory.Trajectory"
class="reference internal"
title="pymatgen.core.trajectory.Trajectory"><span
class="pre">Trajectory</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.trajectory"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">truncation_radius</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id63" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">truncation_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id64" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">valence_electrons</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id65" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">valence_electrons_uncharged</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id66" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">vibrational_energy_components</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.vibrational_energy_components"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">vibrational_modes</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.vibrational_modes"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">write</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/jdftxoutfileslice.py#L1275-L1281"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice.write"
class="headerlink" title="Link to this definition"></a>  
Return an error.

Raises<span class="colon">:</span>  
**NotImplementedError** – There is no need to write a JDFTx out file.

<span class="sig-name descname"><span class="pre">xc_func</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jdftxoutfileslice.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id67" class="headerlink" title="Link to this definition"></a>  

<!-- -->

<span class="sig-name descname"><span class="pre">get_pseudo_read_section_bounds</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">text</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/jdftxoutfileslice.py#L1344-L1362"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jdftxoutfileslice.get_pseudo_read_section_bounds"
class="headerlink" title="Link to this definition"></a>  
Get the boundary line numbers for the pseudopotential read section.

Parameters<span class="colon">:</span>  
**text** (*list\[str\]*) – Output of read_file for out file.

Returns<span class="colon">:</span>  
List of line numbers for the pseudopotential read sections.

Return type<span class="colon">:</span>  
list\[list\[int\]\]

</div>

<div id="module-pymatgen.io.jdftx.jelstep" class="section">

<span id="pymatgen-io-jdftx-jelstep-module"></span>

## pymatgen.io.jdftx.jelstep module<a href="#module-pymatgen.io.jdftx.jelstep" class="headerlink"
title="Link to this heading"></a>

Module for parsing single SCF step from JDFTx.

This module contains the JElStep class for parsing single SCF step from
a JDFTx out file.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">JElStep</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">opt_type</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">etype</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">nstep</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">e</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grad_k</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">alpha</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">linmin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">t_s</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">mu</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">nelectrons</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">abs_magneticmoment</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">tot_magneticmoment</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">subspacerotationadjust</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">converged</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">converged_reason</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/jelstep.py#L24-L250"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElStep" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Electronic minimization data for a single SCF step.

Class object for storing logged electronic minimization data for a
single SCF step.

<span class="sig-name descname"><span class="pre">opt_type</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElStep.opt_type" class="headerlink"
title="Link to this definition"></a>  
The type of electronic minimization step (almost always ElecMinimize).

Type<span class="colon">:</span>  
str \| None

<span class="sig-name descname"><span class="pre">etype</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElStep.etype" class="headerlink"
title="Link to this definition"></a>  
The type of energy component (G, F, or Etot).

Type<span class="colon">:</span>  
str \| None

<span class="sig-name descname"><span class="pre">nstep</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElStep.nstep" class="headerlink"
title="Link to this definition"></a>  
The SCF step number.

Type<span class="colon">:</span>  
int \| None

<span class="sig-name descname"><span class="pre">e</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElStep.e" class="headerlink"
title="Link to this definition"></a>  
The total electronic energy in eV.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">grad_k</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElStep.grad_k" class="headerlink"
title="Link to this definition"></a>  
The gradient of the Kohn-Sham energy (along the line minimization
direction).

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">alpha</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElStep.alpha" class="headerlink"
title="Link to this definition"></a>  
The step length.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">linmin</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElStep.linmin" class="headerlink"
title="Link to this definition"></a>  
Normalized line minimization direction / energy gradient projection (-1
for perfectly opposite, 1 for perfectly aligned).

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">t_s</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElStep.t_s" class="headerlink"
title="Link to this definition"></a>  
Time elapsed from beginning of JDFTx calculation.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">mu</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElStep.mu" class="headerlink"
title="Link to this definition"></a>  
The chemical potential in eV.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">nelectrons</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElStep.nelectrons"
class="headerlink" title="Link to this definition"></a>  
The number of electrons.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">abs_magneticmoment</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElStep.abs_magneticmoment"
class="headerlink" title="Link to this definition"></a>  
The absolute magnetic moment.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">tot_magneticmoment</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElStep.tot_magneticmoment"
class="headerlink" title="Link to this definition"></a>  
The total magnetic moment.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">subspacerotationadjust</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElStep.subspacerotationadjust"
class="headerlink" title="Link to this definition"></a>  
The subspace rotation adjustment factor.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">abs_magneticmoment</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id68" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">alpha</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id69" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/jelstep.py#L224-L237"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElStep.as_dict" class="headerlink"
title="Link to this definition"></a>  
Return dictionary representation of JElStep object.

Returns<span class="colon">:</span>  
Dictionary representation of JElStep object.

Return type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">converged</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">False</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElStep.converged"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">converged_reason</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElStep.converged_reason"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">e</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id70" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">etype</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id71" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">grad_k</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id72" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">linmin</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id73" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">mu</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id74" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">nelectrons</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id75" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">nstep</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id76" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">opt_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id77" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">subspacerotationadjust</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id78" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">t_s</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id79" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">to_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../../../.venv/lib/python3.11/site-packages/monty/dev.py#L239-L241"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElStep.to_dict" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">tot_magneticmoment</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id80" class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">JElSteps</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">opt_type:</span> <span class="pre">str</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">etype:</span> <span class="pre">str</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">iter_flag:</span> <span class="pre">str</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">converged:</span> <span class="pre">bool</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">converged_reason:</span> <span class="pre">str</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">slices:</span> <span class="pre">list\[\~pymatgen.io.jdftx.jelstep.JElStep\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/jelstep.py#L267-L493"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElSteps" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Class object for series of SCF steps.

Class object for collecting and storing a series of SCF steps done
between geometric optimization steps.

<span class="sig-name descname"><span class="pre">opt_type</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElSteps.opt_type"
class="headerlink" title="Link to this definition"></a>  
The type of electronic minimization step.

Type<span class="colon">:</span>  
str \| None

<span class="sig-name descname"><span class="pre">etype</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElSteps.etype" class="headerlink"
title="Link to this definition"></a>  
The type of energy component.

Type<span class="colon">:</span>  
str \| None

<span class="sig-name descname"><span class="pre">iter_flag</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElSteps.iter_flag"
class="headerlink" title="Link to this definition"></a>  
The flag that indicates the start of a log message for a JDFTx
optimization step.

Type<span class="colon">:</span>  
str \| None

<span class="sig-name descname"><span class="pre">converged</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElSteps.converged"
class="headerlink" title="Link to this definition"></a>  
True if the SCF steps converged.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">converged_reason</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElSteps.converged_reason"
class="headerlink" title="Link to this definition"></a>  
The reason for convergence.

Type<span class="colon">:</span>  
str \| None

<span class="sig-name descname"><span class="pre">slices</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElSteps.slices" class="headerlink"
title="Link to this definition"></a>  
A list of JElStep objects.

Type<span class="colon">:</span>  
list\[<a href="#pymatgen.io.jdftx.jelstep.JElStep" class="reference internal"
title="pymatgen.io.jdftx.jelstep.JElStep">JElStep</a>\]

<span class="sig-name descname"><span class="pre">e</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElSteps.e" class="headerlink"
title="Link to this definition"></a>  
The total electronic energy in eV.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">grad_k</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElSteps.grad_k" class="headerlink"
title="Link to this definition"></a>  
The gradient of the Kohn-Sham energy (along the line minimization
direction).

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">alpha</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElSteps.alpha" class="headerlink"
title="Link to this definition"></a>  
The step length.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">linmin</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElSteps.linmin" class="headerlink"
title="Link to this definition"></a>  
Normalized line minimization direction / energy gradient projection (-1
for perfectly opposite, 1 for perfectly aligned).

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">t_s</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElSteps.t_s" class="headerlink"
title="Link to this definition"></a>  
Time elapsed from beginning of JDFTx calculation.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">mu</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElSteps.mu" class="headerlink"
title="Link to this definition"></a>  
The chemical potential in eV.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">nelectrons</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElSteps.nelectrons"
class="headerlink" title="Link to this definition"></a>  
The number of electrons.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">abs_magneticmoment</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElSteps.abs_magneticmoment"
class="headerlink" title="Link to this definition"></a>  
The absolute magnetic moment.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">tot_magneticmoment</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElSteps.tot_magneticmoment"
class="headerlink" title="Link to this definition"></a>  
The total magnetic moment.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">subspacerotationadjust</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElSteps.subspacerotationadjust"
class="headerlink" title="Link to this definition"></a>  
The subspace rotation adjustment factor.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">nstep</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElSteps.nstep" class="headerlink"
title="Link to this definition"></a>  
The SCF step number.

Type<span class="colon">:</span>  
int \| None

<span class="sig-name descname"><span class="pre">abs_magneticmoment</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id81" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">alpha</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id82" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/jelstep.py#L395-L411"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElSteps.as_dict" class="headerlink"
title="Link to this definition"></a>  
Return dictionary representation of JElSteps object.

Returns<span class="colon">:</span>  
Dictionary representation of JElSteps object.

Return type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">converged</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id83" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">converged_reason</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id84" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">e</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id85" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">etype</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id86" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">grad_k</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id87" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">iter_flag</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id88" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">linmin</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id89" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">mu</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id90" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">nelectrons</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id91" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">nstep</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id92" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">opt_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id93" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">slices</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.io.jdftx.jelstep.JElStep" class="reference internal"
title="pymatgen.io.jdftx.jelstep.JElStep"><span
class="pre">JElStep</span></a><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id94" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">subspacerotationadjust</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id95" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">t_s</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id96" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">to_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../../../.venv/lib/python3.11/site-packages/monty/dev.py#L413-L415"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jelstep.JElSteps.to_dict" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">tot_magneticmoment</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jelstep.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id97" class="headerlink" title="Link to this definition"></a>  

</div>

<div id="module-pymatgen.io.jdftx.jminsettings" class="section">

<span id="pymatgen-io-jdftx-jminsettings-module"></span>

## pymatgen.io.jdftx.jminsettings module<a href="#module-pymatgen.io.jdftx.jminsettings" class="headerlink"
title="Link to this heading"></a>

Store generic minimization settings read from a JDFTx out file.

This module contains the JMinSettings class for storing generic
minimization and mutants for storing specific minimization settings read
from a JDFTx out file.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">JMinSettings</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">params</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/jminsettings.py#L15-L37"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jminsettings.JMinSettings"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Store generic minimization settings read from a JDFTx out file.

Store generic minimization settings read from a JDFTx out file.

Initialize a generic JMinSettings class.

Parameters<span class="colon">:</span>  
**params** (*dict\[str,* *Any\]* *\|* *None*) – A dictionary of
minimization settings.

<span class="sig-name descname"><span class="pre">params</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jminsettings.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jminsettings.JMinSettings.params"
class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">JMinSettingsElectronic</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">params</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/jminsettings.py#L40-L53"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jminsettings.JMinSettingsElectronic"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.jdftx.jminsettings.JMinSettings"
class="reference internal"
title="pymatgen.io.jdftx.jminsettings.JMinSettings"><span
class="pre"><code
class="sourceCode python">JMinSettings</code></span></a>

JMInSettings mutant for electronic minimization settings.

A class for storing electronic minimization settings read from a JDFTx
out file.

Initialize a generic JMinSettings class.

Parameters<span class="colon">:</span>  
**params** (*dict\[str,* *Any\]* *\|* *None*) – A dictionary of
minimization settings.

<span class="sig-name descname"><span class="pre">start_flag</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'electronic-minimize'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jminsettings.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.jminsettings.JMinSettingsElectronic.start_flag"
class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">JMinSettingsFluid</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">params</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/jminsettings.py#L56-L69"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jminsettings.JMinSettingsFluid"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.jdftx.jminsettings.JMinSettings"
class="reference internal"
title="pymatgen.io.jdftx.jminsettings.JMinSettings"><span
class="pre"><code
class="sourceCode python">JMinSettings</code></span></a>

JMInSettings mutant for fluid minimization settings.

A class for storing fluid minimization settings read from a JDFTx out
file.

Initialize a generic JMinSettings class.

Parameters<span class="colon">:</span>  
**params** (*dict\[str,* *Any\]* *\|* *None*) – A dictionary of
minimization settings.

<span class="sig-name descname"><span class="pre">start_flag</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'fluid-minimize'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jminsettings.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jminsettings.JMinSettingsFluid.start_flag"
class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">JMinSettingsIonic</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">params</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/jminsettings.py#L88-L101"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jminsettings.JMinSettingsIonic"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.jdftx.jminsettings.JMinSettings"
class="reference internal"
title="pymatgen.io.jdftx.jminsettings.JMinSettings"><span
class="pre"><code
class="sourceCode python">JMinSettings</code></span></a>

JMInSettings mutant for ionic minimization settings.

A class for storing ionic minimization settings read from a JDFTx out
file.

Initialize a generic JMinSettings class.

Parameters<span class="colon">:</span>  
**params** (*dict\[str,* *Any\]* *\|* *None*) – A dictionary of
minimization settings.

<span class="sig-name descname"><span class="pre">start_flag</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'ionic-minimize'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jminsettings.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jminsettings.JMinSettingsIonic.start_flag"
class="headerlink" title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">JMinSettingsLattice</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">params</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/jminsettings.py#L72-L85"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jminsettings.JMinSettingsLattice"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="#pymatgen.io.jdftx.jminsettings.JMinSettings"
class="reference internal"
title="pymatgen.io.jdftx.jminsettings.JMinSettings"><span
class="pre"><code
class="sourceCode python">JMinSettings</code></span></a>

JMInSettings mutant for lattice minimization settings.

A class for storing lattice minimization settings read from a JDFTx out
file.

Initialize a generic JMinSettings class.

Parameters<span class="colon">:</span>  
**params** (*dict\[str,* *Any\]* *\|* *None*) – A dictionary of
minimization settings.

<span class="sig-name descname"><span class="pre">start_flag</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'lattice-minimize'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/jminsettings.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.jminsettings.JMinSettingsLattice.start_flag"
class="headerlink" title="Link to this definition"></a>  

</div>

<div id="module-pymatgen.io.jdftx.joutstructure" class="section">

<span id="pymatgen-io-jdftx-joutstructure-module"></span>

## pymatgen.io.jdftx.joutstructure module<a href="#module-pymatgen.io.jdftx.joutstructure" class="headerlink"
title="Link to this heading"></a>

Class object for storing a single JDFTx geometric optimization step.

A mutant of the pymatgen Structure class for flexibility in holding
JDFTx.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">JOutStructure</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">lattice</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.lattice.Lattice"
class="reference internal" title="pymatgen.core.lattice.Lattice"><span
class="pre">Lattice</span></a></span>*, *<span class="n"><span class="pre">species</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">CompositionLike</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">coords</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ArrayLike</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="p"><span class="pre">\[</span></span><span class="pre">ArrayLike</span><span class="p"><span class="pre">\]</span></span></span>*, *<span class="n"><span class="pre">site_properties</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/joutstructure.py#L47-L1020"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure"
class="headerlink" title="Link to this definition"></a>  
Bases: <a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span class="pre"><code
class="sourceCode python">Structure</code></span></a>

Class object for storing a single JDFTx optimization step.

A mutant of the pymatgen Structure class for flexibility in holding
JDFTx optimization data.

Properties:  
charges (np.ndarray \| None): The Lowdin charges of the atoms in the
system. magnetic_moments (np.ndarray \| None): The magnetic moments of
the atoms in the system.

<span class="sig-name descname"><span class="pre">opt_type</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.opt_type"
class="headerlink" title="Link to this definition"></a>  
The type of optimization step.

Type<span class="colon">:</span>  
str \| None

<span class="sig-name descname"><span class="pre">etype</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.etype"
class="headerlink" title="Link to this definition"></a>  
The type of energy from the electronic minimization data.

Type<span class="colon">:</span>  
str \| None

<span class="sig-name descname"><span class="pre">eopt_type</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.eopt_type"
class="headerlink" title="Link to this definition"></a>  
The type of electronic minimization step.

Type<span class="colon">:</span>  
str \| None

<span class="sig-name descname"><span class="pre">emin_flag</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.emin_flag"
class="headerlink" title="Link to this definition"></a>  
The flag that indicates the start of a log message for a JDFTx
optimization step.

Type<span class="colon">:</span>  
str \| None

<span class="sig-name descname"><span class="pre">ecomponents</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.ecomponents"
class="headerlink" title="Link to this definition"></a>  
The energy components of the system.

Type<span class="colon">:</span>  
dict \| None

<span class="sig-name descname"><span class="pre">elecmindata</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.elecmindata"
class="headerlink" title="Link to this definition"></a>  
The electronic minimization data.

Type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.jelstep.JElSteps" class="reference internal"
title="pymatgen.io.jdftx.jelstep.JElSteps">JElSteps</a> \| None

<span class="sig-name descname"><span class="pre">stress</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.stress"
class="headerlink" title="Link to this definition"></a>  
The stress tensor.

Type<span class="colon">:</span>  
np.ndarray \| None

<span class="sig-name descname"><span class="pre">strain</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.strain"
class="headerlink" title="Link to this definition"></a>  
The strain tensor.

Type<span class="colon">:</span>  
np.ndarray \| None

<span class="sig-name descname"><span class="pre">nstep</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.nstep"
class="headerlink" title="Link to this definition"></a>  
The most recent step number.

Type<span class="colon">:</span>  
int \| None

<span class="sig-name descname"><span class="pre">e</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.e"
class="headerlink" title="Link to this definition"></a>  
The total energy of the system.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">grad_k</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.grad_k"
class="headerlink" title="Link to this definition"></a>  
The gradient of the electronic density along the most recent line
minimization.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">alpha</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.alpha"
class="headerlink" title="Link to this definition"></a>  
The step size of the most recent SCF step along the line minimization.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">linmin</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.linmin"
class="headerlink" title="Link to this definition"></a>  
The normalized alignment projection of the electronic energy gradient to
the line minimization direction.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">t_s</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.t_s"
class="headerlink" title="Link to this definition"></a>  
The time in seconds for the optimization step.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">geom_converged</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.geom_converged"
class="headerlink" title="Link to this definition"></a>  
Whether the geometry optimization has converged.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">geom_converged_reason</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.joutstructure.JOutStructure.geom_converged_reason"
class="headerlink" title="Link to this definition"></a>  
The reason for geometry optimization convergence.

Type<span class="colon">:</span>  
str \| None

<span class="sig-name descname"><span class="pre">line_types</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.line_types"
class="headerlink" title="Link to this definition"></a>  
The types of lines in a JDFTx out file.

Type<span class="colon">:</span>  
ClassVar\[list\[str\]\]

<span class="sig-name descname"><span class="pre">selective_dynamics</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.joutstructure.JOutStructure.selective_dynamics"
class="headerlink" title="Link to this definition"></a>  
The selective dynamics flags for the atoms in the system.

Type<span class="colon">:</span>  
list\[int\] \| None

<span class="sig-name descname"><span class="pre">mu</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.mu"
class="headerlink" title="Link to this definition"></a>  
The chemical potential (Fermi level) in eV.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">nelectrons</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.nelectrons"
class="headerlink" title="Link to this definition"></a>  
The total number of electrons in the electron density.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">abs_magneticmoment</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.joutstructure.JOutStructure.abs_magneticmoment"
class="headerlink" title="Link to this definition"></a>  
The absolute magnetic moment of the electron density.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">tot_magneticmoment</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.joutstructure.JOutStructure.tot_magneticmoment"
class="headerlink" title="Link to this definition"></a>  
The total magnetic moment of the electron density.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">elec_nstep</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.elec_nstep"
class="headerlink" title="Link to this definition"></a>  
The most recent electronic step number.

Type<span class="colon">:</span>  
int \| None

<span class="sig-name descname"><span class="pre">elec_e</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.elec_e"
class="headerlink" title="Link to this definition"></a>  
The most recent electronic energy.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">elec_grad_k</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.elec_grad_k"
class="headerlink" title="Link to this definition"></a>  
The most recent electronic grad_k.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">elec_alpha</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.elec_alpha"
class="headerlink" title="Link to this definition"></a>  
The most recent electronic alpha.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">elec_linmin</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.elec_linmin"
class="headerlink" title="Link to this definition"></a>  
The most recent electronic linmin.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">structure</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.structure"
class="headerlink" title="Link to this definition"></a>  
The Structure object of the system. (helpful for uses where the
JOutStructure metadata causes issues)

Type<span class="colon">:</span>  
<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure">Structure</a> \| None

<span class="sig-name descname"><span class="pre">is_md</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.is_md"
class="headerlink" title="Link to this definition"></a>  
Whether the optimization step is a molecular dynamics step.

Type<span class="colon">:</span>  
bool

Create a periodic structure.

Parameters<span class="colon">:</span>  
- **lattice** – The lattice, either as a pymatgen.core.Lattice or simply
  as any 2D array. Each row should correspond to a lattice vector. e.g.
  \[\[10,0,0\], \[20,10,0\], \[0,0,30\]\] specifies a lattice with
  lattice vectors \[10,0,0\], \[20,10,0\] and \[0,0,30\].

- **species** –

  List of species on each site. Can take in flexible input, including:

  1.  A sequence of element / species specified either as string
      symbols, e.g. \[“Li”, “Fe2+”, “P”, …\] or atomic numbers, e.g. (3,
      56, …) or actual Element or Species objects.

  2.  List of dict of elements/species and occupancies, e.g. \[{“Fe” :
      0.5, “Mn”:0.5}, …\]. This allows the setup of disordered
      structures.

- **coords** (*Nx3 array*) – list of fractional/cartesian coordinates of
  each species.

- **charge** (*float*) – overall charge of the structure. Defaults to
  behavior in SiteCollection where total charge is the sum of the
  oxidation states.

- **validate_proximity** (*bool*) – Whether to check if there are sites
  that are less than 0.01 Ang apart. Defaults to False.

- **to_unit_cell** (*bool*) – Whether to map all sites into the unit
  cell, i.e., fractional coords between 0 and 1. Defaults to False.

- **coords_are_cartesian** (*bool*) – Set to True if you are providing
  coordinates in Cartesian coordinates. Defaults to False.

- **site_properties** (*dict*) – Properties associated with the sites as
  a dict of sequences, e.g. {“magmom”:\[5,5,5,5\]}. The sequences have
  to be the same length as the atomic species and fractional_coords.
  Defaults to None for no properties.

- **labels** (*list\[str\]*) – Labels associated with the sites as a
  list of strings, e.g. \[‘Li1’, ‘Li2’\]. Must have the same length as
  the species and fractional coords. Defaults to None for no labels.

- **properties** (*dict*) – Properties associated with the whole
  structure. Will be serialized when writing the structure to JSON or
  YAML but is lost when converting to other formats.

<span class="sig-name descname"><span class="pre">abs_magneticmoment</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id98" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">alpha</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id99" class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/joutstructure.py#L991-L1005"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.as_dict"
class="headerlink" title="Link to this definition"></a>  
Convert the JOutStructure object to a dictionary.

Returns<span class="colon">:</span>  
A dictionary representation of the JOutStructure object.

Return type<span class="colon">:</span>  
dict

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">charges</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">NDArray</span><span class="p"><span class="pre">\[</span></span><span class="pre">np.float64</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.charges"
class="headerlink" title="Link to this definition"></a>  
Return the Lowdin charges.

Returns<span class="colon">:</span>  
The Lowdin charges of the atoms in the system.

Return type<span class="colon">:</span>  
np.ndarray

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">constraint_types</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.joutstructure.JOutStructure.constraint_types"
class="headerlink" title="Link to this definition"></a>  
Return the constraint_types.

Returns<span class="colon">:</span>  
The constraint_types of the atoms in the system.

Return type<span class="colon">:</span>  
list\[str \| None\] \| None

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">constraint_vectors</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">np.ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">np.ndarray</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.joutstructure.JOutStructure.constraint_vectors"
class="headerlink" title="Link to this definition"></a>  
Return the velocities.

Returns<span class="colon">:</span>  
The constraint_vectors of the atoms in the system.

Return type<span class="colon">:</span>  
list\[np.ndarray \| list\[np.ndarray\] \| None\] \| None

<span class="sig-name descname"><span class="pre">e</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id100" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">ecomponents</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id101" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">elec_alpha</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id102" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">elec_e</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id103" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">elec_grad_k</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id104" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">elec_linmin</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id105" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">elec_nstep</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id106" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">elecmindata</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="#pymatgen.io.jdftx.jelstep.JElSteps" class="reference internal"
title="pymatgen.io.jdftx.jelstep.JElSteps"><span
class="pre">JElSteps</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id107" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">emin_flag</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id108" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">eopt_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id109" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">etype</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id110" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">forces</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">NDArray</span><span class="p"><span class="pre">\[</span></span><span class="pre">np.float64</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.forces"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">geom_converged</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">False</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id111" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">geom_converged_reason</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id112" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">grad_k</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id113" class="headerlink"
title="Link to this definition"></a>  

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">group_names</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.group_names"
class="headerlink" title="Link to this definition"></a>  
Return the group_names.

Returns<span class="colon">:</span>  
The group_names of the atoms in the system.

Return type<span class="colon">:</span>  
list\[list\[str\] \| None\] \| None

<span class="sig-name descname"><span class="pre">is_md</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">False</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id114" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">kinetic_stress</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">NDArray</span><span class="p"><span class="pre">\[</span></span><span class="pre">np.float64</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.kinetic_stress"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">line_types</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">ClassVar</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">\['emin',</span> <span class="pre">'lattice',</span> <span class="pre">'strain',</span> <span class="pre">'kinetic_stress',</span> <span class="pre">'stress',</span> <span class="pre">'posns',</span> <span class="pre">'forces',</span> <span class="pre">'ecomp',</span> <span class="pre">'lowdin',</span> <span class="pre">'opt'\]</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id115" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">linmin</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id116" class="headerlink"
title="Link to this definition"></a>  

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">magnetic_moments</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">NDArray</span><span class="p"><span class="pre">\[</span></span><span class="pre">np.float64</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.joutstructure.JOutStructure.magnetic_moments"
class="headerlink" title="Link to this definition"></a>  
Return the magnetic moments.

Returns<span class="colon">:</span>  
The magnetic moments of the atoms in the system.

Return type<span class="colon">:</span>  
np.ndarray

<span class="sig-name descname"><span class="pre">mu</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id117" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">nelectrons</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id118" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">nstep</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id119" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">opt_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id120" class="headerlink"
title="Link to this definition"></a>  

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">selective_dynamics</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id121" class="headerlink"
title="Link to this definition"></a>  
Return the selective dynamics.

Returns<span class="colon">:</span>  
The selective dynamics of the atoms in the system.

Return type<span class="colon">:</span>  
list\[list\[int\]\]

<span class="sig-name descname"><span class="pre">strain</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">NDArray</span><span class="p"><span class="pre">\[</span></span><span class="pre">np.float64</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id122" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">stress</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">NDArray</span><span class="p"><span class="pre">\[</span></span><span class="pre">np.float64</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id123" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">structure</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id124" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">t_s</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id125" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">thermostat_velocity</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">np.ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.joutstructure.JOutStructure.thermostat_velocity"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">to_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../../../.venv/lib/python3.11/site-packages/monty/dev.py#L1007-L1009"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.to_dict"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">tot_magneticmoment</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">np.float64</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id126" class="headerlink"
title="Link to this definition"></a>  

*<span class="k"><span class="pre">property</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">velocities</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Sequence</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">np.ndarray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructure.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure.velocities"
class="headerlink" title="Link to this definition"></a>  
Return the velocities.

Returns<span class="colon">:</span>  
The velocities of the atoms in the system.

Return type<span class="colon">:</span>  
list\[np.ndarray \| None\] \| None

</div>

<div id="module-pymatgen.io.jdftx.joutstructures" class="section">

<span id="pymatgen-io-jdftx-joutstructures-module"></span>

## pymatgen.io.jdftx.joutstructures module<a href="#module-pymatgen.io.jdftx.joutstructures" class="headerlink"
title="Link to this heading"></a>

Module for JOutStructures class.

This module contains the JOutStructures class for storing a series of
JOutStructure.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">JOutStructures</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">opt_type:</span> <span class="pre">str</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">geom_converged:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">geom_converged_reason:</span> <span class="pre">str</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">elec_converged:</span> <span class="pre">bool</span> <span class="pre">=</span> <span class="pre">False</span></span>*, *<span class="n"><span class="pre">elec_converged_reason:</span> <span class="pre">str</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">t_s:</span> <span class="pre">float</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">slices:</span> <span class="pre">list\[JOutStructure\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">eopt_type:</span> <span class="pre">str</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">etype:</span> <span class="pre">str</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">emin_flag:</span> <span class="pre">str</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">ecomponents:</span> <span class="pre">list\[str\]</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">elecmindata:</span> <span class="pre">JElSteps</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">stress:</span> <span class="pre">NDArray\[np.float64\]</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">strain:</span> <span class="pre">NDArray\[np.float64\]</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">forces:</span> <span class="pre">NDArray\[np.float64\]</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">nstep:</span> <span class="pre">int</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">e:</span> <span class="pre">float</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">grad_k:</span> <span class="pre">float</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">alpha:</span> <span class="pre">float</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">linmin:</span> <span class="pre">float</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">nelectrons:</span> <span class="pre">float</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">abs_magneticmoment:</span> <span class="pre">float</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">tot_magneticmoment:</span> <span class="pre">float</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">mu:</span> <span class="pre">float</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">elec_nstep:</span> <span class="pre">int</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">elec_e:</span> <span class="pre">float</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">elec_grad_k:</span> <span class="pre">float</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">elec_alpha:</span> <span class="pre">float</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">elec_linmin:</span> <span class="pre">float</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">charges:</span> <span class="pre">NDArray\[np.float64\]</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">magnetic_moments:</span> <span class="pre">NDArray\[np.float64\]</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">selective_dynamics:</span> <span class="pre">list\[int\]</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">structure:</span> <span class="pre">Structure</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">initial_structure:</span> <span class="pre">Structure</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/joutstructures.py#L60-L300"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures"
class="headerlink" title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

Class for storing a series of JStructure objects.

A class for storing a series of JStructure objects.

<span class="sig-name descname"><span class="pre">out_slice_start_flag</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.joutstructures.JOutStructures.out_slice_start_flag"
class="headerlink" title="Link to this definition"></a>  
The string that marks the beginning of the portion of an out file slice
that contains data for a JOutStructures object.

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">opt_type</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.opt_type"
class="headerlink" title="Link to this definition"></a>  
The type of optimization performed on the structures in the
JOutStructures object.

Type<span class="colon">:</span>  
str \| None

<span class="sig-name descname"><span class="pre">geom_converged</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.joutstructures.JOutStructures.geom_converged"
class="headerlink" title="Link to this definition"></a>  
Whether the geometry of the last structure in the list has converged.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">geom_converged_reason</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.joutstructures.JOutStructures.geom_converged_reason"
class="headerlink" title="Link to this definition"></a>  
The reason the geometry of the last structure in the list has converged.

Type<span class="colon">:</span>  
str \| None

<span class="sig-name descname"><span class="pre">elec_converged</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.joutstructures.JOutStructures.elec_converged"
class="headerlink" title="Link to this definition"></a>  
Whether the electronic density of the last structure in the list has
converged.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">elec_converged_reason</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.joutstructures.JOutStructures.elec_converged_reason"
class="headerlink" title="Link to this definition"></a>  
The reason the electronic density of the last structure in the list has
converged.

Type<span class="colon">:</span>  
str \| None

<span class="sig-name descname"><span class="pre">slices</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.slices"
class="headerlink" title="Link to this definition"></a>  
A list of JOutStructure objects.

Type<span class="colon">:</span>  
list\[<a href="#pymatgen.io.jdftx.joutstructure.JOutStructure"
class="reference internal"
title="pymatgen.io.jdftx.joutstructure.JOutStructure">JOutStructure</a>\]

<span class="sig-name descname"><span class="pre">eopt_type</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.eopt_type"
class="headerlink" title="Link to this definition"></a>  
The type of electronic optimization performed on the last structure in
the list.

Type<span class="colon">:</span>  
str \| None

<span class="sig-name descname"><span class="pre">etype</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.etype"
class="headerlink" title="Link to this definition"></a>  
String representation of total energy-type of system. Commonly “G”

Type<span class="colon">:</span>  
str \| None

<span class="sig-name descname"><span class="pre">(grand-canonical</span> <span class="pre">potential)</span> <span class="pre">for</span> <span class="pre">GC</span> <span class="pre">calculations,</span> <span class="pre">and</span> <span class="pre">"F"</span> <span class="pre">for</span> <span class="pre">canonical</span></span>  
Type<span class="colon">:</span>  
fixed electron count

<span class="sig-name descname"><span class="pre">emin_flag</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.emin_flag"
class="headerlink" title="Link to this definition"></a>  
The flag for the electronic minimization.

Type<span class="colon">:</span>  
str \| None

<span class="sig-name descname"><span class="pre">ecomponents</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.ecomponents"
class="headerlink" title="Link to this definition"></a>  
The components of the electronic minimization.

Type<span class="colon">:</span>  
list\[str\] \| None

<span class="sig-name descname"><span class="pre">elecmindata</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.elecmindata"
class="headerlink" title="Link to this definition"></a>  
The electronic minimization data.

Type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.jelstep.JElSteps" class="reference internal"
title="pymatgen.io.jdftx.jelstep.JElSteps">JElSteps</a>

<span class="sig-name descname"><span class="pre">stress</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.stress"
class="headerlink" title="Link to this definition"></a>  
The stress tensor.

Type<span class="colon">:</span>  
np.ndarray \| None

<span class="sig-name descname"><span class="pre">strain</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.strain"
class="headerlink" title="Link to this definition"></a>  
The strain tensor.

Type<span class="colon">:</span>  
np.ndarray \| None

<span class="sig-name descname"><span class="pre">nstep</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.nstep"
class="headerlink" title="Link to this definition"></a>  
The number of steps in the optimization.

Type<span class="colon">:</span>  
int \| None

<span class="sig-name descname"><span class="pre">e</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.e"
class="headerlink" title="Link to this definition"></a>  
The total energy.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">grad_k</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.grad_k"
class="headerlink" title="Link to this definition"></a>  
The final norm of the preconditioned gradient for geometric optimization
of the most recent JDFTx call (evaluated as dot(g, Kg), where g is the
gradient and Kg is the preconditioned gradient). (written as “[<span
id="id128" class="problematic">\|</span>](#id127)grad\|\_K” in JDFTx
output).

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">alpha</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.alpha"
class="headerlink" title="Link to this definition"></a>  
The step size of the final geometric step in the most recent JDFTx call.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">linmin</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.linmin"
class="headerlink" title="Link to this definition"></a>  
The final normalized projection of the geometric step direction onto the
gradient for the most recent JDFTx call.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">abs_magneticmoment</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.joutstructures.JOutStructures.abs_magneticmoment"
class="headerlink" title="Link to this definition"></a>  
The absolute magnetic moment of the most recent JDFTx call.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">tot_magneticmoment</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.joutstructures.JOutStructures.tot_magneticmoment"
class="headerlink" title="Link to this definition"></a>  
The total magnetic moment of the most recent JDFTx call.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">mu</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.mu"
class="headerlink" title="Link to this definition"></a>  
The Fermi energy of the most recent JDFTx call.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">elec_e</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.elec_e"
class="headerlink" title="Link to this definition"></a>  
The final energy of the most recent electronic optimization step.

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">elec_nstep</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.elec_nstep"
class="headerlink" title="Link to this definition"></a>  
The number of electronic optimization steps in the most recent JDFTx
call.

Type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">elec_grad_k</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.elec_grad_k"
class="headerlink" title="Link to this definition"></a>  
The final norm of the preconditioned gradient for electronic
optimization of the most recent JDFTx call (evaluated as dot(g, Kg),
where g is the gradient and Kg is the preconditioned gradient). (written
as “[<span id="id130" class="problematic">\|</span>](#id129)grad\|\_K”
in JDFTx output).

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">elec_alpha</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.elec_alpha"
class="headerlink" title="Link to this definition"></a>  
The step size of the final electronic step in the most recent JDFTx
call.

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">elec_linmin</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.elec_linmin"
class="headerlink" title="Link to this definition"></a>  
The final normalized projection of the electronic step direction onto
the gradient for the most recent JDFTx call.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">charges</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.charges"
class="headerlink" title="Link to this definition"></a>  
The most recent Lowdin-charges.

Type<span class="colon">:</span>  
np.ndarray\[float\] \| None

<span class="sig-name descname"><span class="pre">magnetic_moments</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.joutstructures.JOutStructures.magnetic_moments"
class="headerlink" title="Link to this definition"></a>  
The most recent Lowdin-magnetic moments.

Type<span class="colon">:</span>  
np.ndarray\[float\] \| None

<span class="sig-name descname"><span class="pre">selective_dynamics</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.joutstructures.JOutStructures.selective_dynamics"
class="headerlink" title="Link to this definition"></a>  
The selective dynamics flags for the most recent JDFTx call.

Type<span class="colon">:</span>  
list\[int\] \| None

<span class="sig-name descname"><span class="pre">structure</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.structure"
class="headerlink" title="Link to this definition"></a>  
Cleaned pymatgen Structure object of final JOutStructure

Type<span class="colon">:</span>  
<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure">Structure</a> \| None

<span class="sig-name descname"><span class="pre">initial_structure</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.joutstructures.JOutStructures.initial_structure"
class="headerlink" title="Link to this definition"></a>  
Cleaned pymatgen Structure object of initial JOutStructure

Type<span class="colon">:</span>  
<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure">Structure</a> \| None

<span class="sig-name descname"><span class="pre">abs_magneticmoment</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id131" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">alpha</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id132" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/joutstructures.py#L225-L242"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.as_dict"
class="headerlink" title="Link to this definition"></a>  
Convert the JOutStructures object to a dictionary.

Returns<span class="colon">:</span>  
A dictionary representation of the JOutStructures object.

Return type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">charges</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">NDArray</span><span class="p"><span class="pre">\[</span></span><span class="pre">np.float64</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id133" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">e</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id134" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">ecomponents</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id135" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">elec_alpha</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id136" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">elec_converged</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">False</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id137" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">elec_converged_reason</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id138" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">elec_e</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id139" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">elec_grad_k</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id140" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">elec_linmin</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id141" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">elec_nstep</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id142" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">elecmindata</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="#pymatgen.io.jdftx.jelstep.JElSteps" class="reference internal"
title="pymatgen.io.jdftx.jelstep.JElSteps"><span
class="pre">JElSteps</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id143" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">emin_flag</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id144" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">eopt_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id145" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">etype</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id146" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">forces</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">NDArray</span><span class="p"><span class="pre">\[</span></span><span class="pre">np.float64</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.forces"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">geom_converged</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">False</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id147" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">geom_converged_reason</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id148" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">grad_k</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id149" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">initial_structure</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id150" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">linmin</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id151" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">magnetic_moments</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">NDArray</span><span class="p"><span class="pre">\[</span></span><span class="pre">np.float64</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id152" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">mu</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id153" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">nelectrons</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.nelectrons"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">nstep</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id154" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">opt_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id155" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">out_slice_start_flag</span></span>*<span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'--------</span> <span class="pre">Electronic</span> <span class="pre">minimization</span> <span class="pre">-----------'</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id156" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">selective_dynamics</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id157" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">slices</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.io.jdftx.joutstructure.JOutStructure"
class="reference internal"
title="pymatgen.io.jdftx.joutstructure.JOutStructure"><span
class="pre">JOutStructure</span></a><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id158" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">strain</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">NDArray</span><span class="p"><span class="pre">\[</span></span><span class="pre">np.float64</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id159" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">stress</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">NDArray</span><span class="p"><span class="pre">\[</span></span><span class="pre">np.float64</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id160" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">structure</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id161" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">t_s</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.t_s"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">to_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../../../.venv/lib/python3.11/site-packages/monty/dev.py#L244-L246"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures.to_dict"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">tot_magneticmoment</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/joutstructures.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id162" class="headerlink"
title="Link to this definition"></a>  

</div>

<div id="module-pymatgen.io.jdftx.outputs" class="section">

<span id="pymatgen-io-jdftx-outputs-module"></span>

## pymatgen.io.jdftx.outputs module<a href="#module-pymatgen.io.jdftx.outputs" class="headerlink"
title="Link to this heading"></a>

JDFTx outputs parsing module.

Module for parsing outputs of JDFTx.

Note: JDFTXOutfile will be moved back to its own module once a more
broad outputs class is written.

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">JDFTXOutfile</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">slices:</span> <span class="pre">list\[\~pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice</span> <span class="pre">\|</span> <span class="pre">None\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*, *<span class="n"><span class="pre">vibrational_modes:</span> <span class="pre">list\[dict\[str</span></span>*, *<span class="n"><span class="pre">\~typing.Any\]\]</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">vibrational_energy_components:</span> <span class="pre">dict\[str</span></span>*, *<span class="n"><span class="pre">float\]</span> <span class="pre">\|</span> <span class="pre">None</span> <span class="pre">=</span> <span class="pre">None</span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/outputs.py#L451-L815"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

JDFTx out file parsing class.

A class to read and process a JDFTx out file.

<span class="sig-name descname"><span class="pre">from_file(file_path</span></span>  
str \| Path) -\> JDFTXOutfile: Return JDFTXOutfile object from the path
to a JDFTx out file.

<span class="sig-name descname"><span class="pre">slices</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.slices"
class="headerlink" title="Link to this definition"></a>  
A list of JDFTXOutfileSlice objects. Each slice corresponds to an
individual call of the JDFTx executable. Subsequent JDFTx calls within
the same directory and prefix will append outputs to the same out file.
More than one slice may correspond to restarted calculations, geom +
single point calculations, or optimizations done with 3rd-party wrappers
like ASE.

Type<span class="colon">:</span>  
list\[<a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice"
class="reference internal"
title="pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice">JDFTXOutfileSlice</a>\]

<span class="sig-name descname"><span class="pre">prefix</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.prefix"
class="headerlink" title="Link to this definition"></a>  
The prefix of the most recent JDFTx call.

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">jstrucs</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.jstrucs"
class="headerlink" title="Link to this definition"></a>  
The JOutStructures object from the most recent JDFTx call. This object
contains a series of JOutStructure objects in its ‘slices’ attribute,
each corresponding to a single structure (multiple iff performing a
geometric optimization) as well as convergence data for the structures
as a series.

Type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.joutstructures.JOutStructures"
class="reference internal"
title="pymatgen.io.jdftx.joutstructures.JOutStructures">JOutStructures</a>

<span class="sig-name descname"><span class="pre">jsettings_fluid</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.jsettings_fluid"
class="headerlink" title="Link to this definition"></a>  
The JMinSettingsFluid object from the most recent JDFTx call. This
object contains only a ‘params’ attribute, which is a dictionary of the
input parameters for the fluid optimization.

Type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.jminsettings.JMinSettingsFluid"
class="reference internal"
title="pymatgen.io.jdftx.jminsettings.JMinSettingsFluid">JMinSettingsFluid</a>

<span class="sig-name descname"><span class="pre">jsettings_electronic</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.jsettings_electronic"
class="headerlink" title="Link to this definition"></a>  
The JMinSettingsElectronic object from the most recent JDFTx call. This
object contains only a ‘params’ attribute, which is a dictionary of the
input parameters for the electronic optimization.

Type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.jminsettings.JMinSettingsElectronic"
class="reference internal"
title="pymatgen.io.jdftx.jminsettings.JMinSettingsElectronic">JMinSettingsElectronic</a>

<span class="sig-name descname"><span class="pre">jsettings_lattice</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.jsettings_lattice"
class="headerlink" title="Link to this definition"></a>  
The JMinSettingsLattice object from the most recent JDFTx call. This
object contains only a ‘params’ attribute, which is a dictionary of the
input parameters for the lattice optimization.

Type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.jminsettings.JMinSettingsLattice"
class="reference internal"
title="pymatgen.io.jdftx.jminsettings.JMinSettingsLattice">JMinSettingsLattice</a>

<span class="sig-name descname"><span class="pre">jsettings_ionic</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.jsettings_ionic"
class="headerlink" title="Link to this definition"></a>  
The JMinSettingsIonic object from the most recent JDFTx call. This
object contains only a ‘params’ attribute, which is a dictionary of the
input parameters for the ionic optimization.

Type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.jminsettings.JMinSettingsIonic"
class="reference internal"
title="pymatgen.io.jdftx.jminsettings.JMinSettingsIonic">JMinSettingsIonic</a>

<span class="sig-name descname"><span class="pre">xc_func</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.xc_func"
class="headerlink" title="Link to this definition"></a>  
The exchange-correlation functional used in the most recent JDFTx call.
See documentation for JDFTx online for a list of available
exchange-correlation functionals.

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">lattice_initial</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.lattice_initial"
class="headerlink" title="Link to this definition"></a>  
The initial lattice vectors of the most recent JDFTx call as a 3x3 numpy
array. In units of Angstroms.

Type<span class="colon">:</span>  
np.ndarray

<span class="sig-name descname"><span class="pre">lattice_final</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.lattice_final"
class="headerlink" title="Link to this definition"></a>  
The final lattice vectors of the most recent JDFTx call as a 3x3 numpy
array. In units of Angstroms.

Type<span class="colon">:</span>  
np.ndarray

<span class="sig-name descname"><span class="pre">lattice</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.lattice"
class="headerlink" title="Link to this definition"></a>  
The lattice vectors of the most recent JDFTx call as a 3x3 numpy array
(redundant to lattice_final).

Type<span class="colon">:</span>  
np.ndarray

<span class="sig-name descname"><span class="pre">a</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.a" class="headerlink"
title="Link to this definition"></a>  
Length of the first lattice vector. In units of Angstroms.

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">b</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.b" class="headerlink"
title="Link to this definition"></a>  
Length of the second lattice vector. In units of Angstroms.

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">c</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.c" class="headerlink"
title="Link to this definition"></a>  
Length of the third lattice vector. In units of Angstroms.

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">fftgrid</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.fftgrid"
class="headerlink" title="Link to this definition"></a>  
The FFT grid shape used in the most recent JDFTx call. Can be used to
properly shape densities dumped as binary files.

Type<span class="colon">:</span>  
list\[int\]

<span class="sig-name descname"><span class="pre">geom_opt</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.geom_opt"
class="headerlink" title="Link to this definition"></a>  
True if the most recent JDFTx call was a geometry optimization (lattice
or ionic).

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">geom_opt_type</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.geom_opt_type"
class="headerlink" title="Link to this definition"></a>  
The type of geometry optimization performed in the most recent JDFTx
call. Options are ‘lattice’ or ‘ionic’ if geom_opt, else “single point”.
(‘lattice’ optimizations perform ionic optimizations as well unless ion
positions are given in direct coordinates).

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">ecomponents</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.ecomponents"
class="headerlink" title="Link to this definition"></a>  
The components of the total energy in eV of the most recent JDFTx call.

Type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">efermi</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.efermi"
class="headerlink" title="Link to this definition"></a>  
The Fermi energy in eV of the most recent JDFTx call. Equivalent to
“mu”.

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">egap</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.egap"
class="headerlink" title="Link to this definition"></a>  
The band gap in eV of the most recent JDFTx call. (Only available if
eigstats was dumped).

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">emin</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.emin"
class="headerlink" title="Link to this definition"></a>  
The minimum energy in eV (smallest Kohn-Sham eigenvalue) of the most
recent JDFTx call. (Only available if eigstats was dumped).

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">emax</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.emax"
class="headerlink" title="Link to this definition"></a>  
The maximum energy in eV (largest Kohn-Sham eigenvalue) of the most
recent JDFTx call. (Only available if eigstats was dumped).

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">homo</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.homo"
class="headerlink" title="Link to this definition"></a>  
The energy in eV of the band-gap lower bound (Highest Occupied Molecular
Orbital) (Only available if eigstats was dumped).

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">lumo</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.lumo"
class="headerlink" title="Link to this definition"></a>  
The energy in eV of the band-gap upper bound (Lowest Unoccupied
Molecular Orbital) (Only available if eigstats was dumped).

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">homo_filling</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.homo_filling"
class="headerlink" title="Link to this definition"></a>  
The electron filling at the homo band-state. (Only available if eigstats
was dumped).

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">lumo_filling</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.lumo_filling"
class="headerlink" title="Link to this definition"></a>  
The electron filling at the lumo band-state. (Only available if eigstats
was dumped).

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">is_metal</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.is_metal"
class="headerlink" title="Link to this definition"></a>  
True if fillings of homo and lumo band-states are off-set by 1 and 0 by
at least an arbitrary tolerance of 0.01 (ie 1 - 0.015 and 0.012 for
homo/lumo fillings would be metallic, while 1-0.001 and 0 would not be).
(Only available if eigstats was dumped).

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">converged</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.converged"
class="headerlink" title="Link to this definition"></a>  
True if most recent SCF cycle converged (and geom forces converged is
calc is geom_opt)

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">etype</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.etype"
class="headerlink" title="Link to this definition"></a>  
String representation of total energy-type of system. Commonly “G”
(grand-canonical potential) for GC calculations, and “F” for canonical
(fixed electron count) calculations.

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">broadening_type</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.broadening_type"
class="headerlink" title="Link to this definition"></a>  
Type of broadening for electronic filling about Fermi-level requested.
Either “Fermi”, “Cold”, “MP1”, or “Gauss”.

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">broadening</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.broadening"
class="headerlink" title="Link to this definition"></a>  
Magnitude of broadening for electronic filling.

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">kgrid</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.kgrid"
class="headerlink" title="Link to this definition"></a>  
Shape of k-point grid used in calculation. (equivalent to k-point
folding)

Type<span class="colon">:</span>  
list\[int\]

<span class="sig-name descname"><span class="pre">truncation_type</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.truncation_type"
class="headerlink" title="Link to this definition"></a>  
Type of coulomb truncation used to prevent interaction between periodic
images along certain directions. “periodic” means no coulomb truncation
was used.

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">truncation_radius</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.truncation_radius"
class="headerlink" title="Link to this definition"></a>  
If spherical truncation_type, this is the radius of the coulomb
truncation sphere.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">pwcut</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.pwcut"
class="headerlink" title="Link to this definition"></a>  
The plane-wave cutoff energy in Hartrees used in the most recent JDFTx
call.

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">rhocut</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.rhocut"
class="headerlink" title="Link to this definition"></a>  
The density cutoff energy in Hartrees used in the most recent JDFTx
call.

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">pp_type</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.pp_type"
class="headerlink" title="Link to this definition"></a>  
The pseudopotential library used in the most recent JDFTx call.
Currently only “GBRV” and “SG15” are supported by this output parser.

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">total_electrons</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.total_electrons"
class="headerlink" title="Link to this definition"></a>  
The total number of electrons in the most recent JDFTx call (redundant
to nelectrons).

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">semicore_electrons</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.semicore_electrons"
class="headerlink" title="Link to this definition"></a>  
The number of semicore electrons in the most recent JDFTx call.

Type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">valence_electrons</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.valence_electrons"
class="headerlink" title="Link to this definition"></a>  
The number of valence electrons in the most recent JDFTx call.

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">total_electrons_uncharged</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.total_electrons_uncharged"
class="headerlink" title="Link to this definition"></a>  
The total number of electrons in the most recent JDFTx call, uncorrected
for charge. (ie total_electrons + charge)

Type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">semicore_electrons_uncharged</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.semicore_electrons_uncharged"
class="headerlink" title="Link to this definition"></a>  
The number of semicore electrons in the most recent JDFTx call,
uncorrected for charge. (ie semicore_electrons + charge)

Type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">valence_electrons_uncharged</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.valence_electrons_uncharged"
class="headerlink" title="Link to this definition"></a>  
The number of valence electrons in the most recent JDFTx call,
uncorrected for charge. (ie valence_electrons + charge)

Type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">nbands</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.nbands"
class="headerlink" title="Link to this definition"></a>  
The number of bands used in the most recent JDFTx call.

Type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">atom_elements</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.atom_elements"
class="headerlink" title="Link to this definition"></a>  
The list of each ion’s element symbol in the most recent JDFTx call.

Type<span class="colon">:</span>  
list\[str\]

<span class="sig-name descname"><span class="pre">atom_elements_int</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.atom_elements_int"
class="headerlink" title="Link to this definition"></a>  
The list of ion’s atomic numbers in the most recent JDFTx call.

Type<span class="colon">:</span>  
list\[int\]

<span class="sig-name descname"><span class="pre">atom_types</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.atom_types"
class="headerlink" title="Link to this definition"></a>  
Non-repeating list of each ion’s element symbol in the most recent JDFTx
call.

Type<span class="colon">:</span>  
list\[str\]

<span class="sig-name descname"><span class="pre">spintype</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.spintype"
class="headerlink" title="Link to this definition"></a>  
The spin type used in the most recent JDFTx call. Options are “none”,
“collinear”,

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">nspin</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.nspin"
class="headerlink" title="Link to this definition"></a>  
The number of spins used in the most recent JDFTx call.

Type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">nat</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.nat" class="headerlink"
title="Link to this definition"></a>  
The number of atoms in the most recent JDFTx call.

Type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">atom_coords_initial</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.atom_coords_initial"
class="headerlink" title="Link to this definition"></a>  
The initial atomic coordinates of the most recent JDFTx call.

Type<span class="colon">:</span>  
list\[list\[float\]\]

<span class="sig-name descname"><span class="pre">atom_coords_final</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.atom_coords_final"
class="headerlink" title="Link to this definition"></a>  
The final atomic coordinates of the most recent JDFTx call.

Type<span class="colon">:</span>  
list\[list\[float\]\]

<span class="sig-name descname"><span class="pre">atom_coords</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.atom_coords"
class="headerlink" title="Link to this definition"></a>  
The atomic coordinates of the most recent JDFTx call.

Type<span class="colon">:</span>  
list\[list\[float\]\]

<span class="sig-name descname"><span class="pre">structure</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.structure"
class="headerlink" title="Link to this definition"></a>  
The updated pymatgen Structure object of the most recent JDFTx call.

Type<span class="colon">:</span>  
<a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure">Structure</a>

<span class="sig-name descname"><span class="pre">trajectory</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.trajectory"
class="headerlink" title="Link to this definition"></a>  
The Trajectory object of the most recent JDFTx call.

Type<span class="colon">:</span>  
<a href="pymatgen.core.html#pymatgen.core.trajectory.Trajectory"
class="reference internal"
title="pymatgen.core.trajectory.Trajectory">Trajectory</a>

<span class="sig-name descname"><span class="pre">has_solvation</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.has_solvation"
class="headerlink" title="Link to this definition"></a>  
True if the most recent JDFTx call included a solvation calculation.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">fluid</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.fluid"
class="headerlink" title="Link to this definition"></a>  
The fluid used in the most recent JDFTx call.

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">is_gc</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.is_gc"
class="headerlink" title="Link to this definition"></a>  
True if the most recent slice is a grand canonical calculation.

Type<span class="colon">:</span>  
bool

<span class="sig-name descname"><span class="pre">eopt_type</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.eopt_type"
class="headerlink" title="Link to this definition"></a>  
The type of energy iteration used in the most recent JDFTx call.

Type<span class="colon">:</span>  
str

<span class="sig-name descname"><span class="pre">elecmindata</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.elecmindata"
class="headerlink" title="Link to this definition"></a>  
The JElSteps object from the most recent JDFTx call. This object
contains a series of JElStep objects in its ‘steps’ attribute, each
corresponding to a single energy iteration.

Type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.jelstep.JElSteps" class="reference internal"
title="pymatgen.io.jdftx.jelstep.JElSteps">JElSteps</a>

<span class="sig-name descname"><span class="pre">stress</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.stress"
class="headerlink" title="Link to this definition"></a>  
The stress tensor of the most recent JDFTx call as a 3x3 numpy array. In
units of eV/Angstrom^3.

Type<span class="colon">:</span>  
np.ndarray

<span class="sig-name descname"><span class="pre">strain</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.strain"
class="headerlink" title="Link to this definition"></a>  
The strain tensor of the most recent JDFTx call as a 3x3 numpy array.

Type<span class="colon">:</span>  
np.ndarray

<span class="sig-name descname"><span class="pre">nstep</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.nstep"
class="headerlink" title="Link to this definition"></a>  
The number of geometric optimization steps in the most recent JDFTx
call.

Type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">e</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.e" class="headerlink"
title="Link to this definition"></a>  
The final energy in eV of the most recent JDFTx call (equivalent to the
call’s etype).

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">grad_k</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.grad_k"
class="headerlink" title="Link to this definition"></a>  
The final norm of the preconditioned gradient for geometric optimization
of the most recent JDFTx call (evaluated as dot(g, Kg), where g is the
gradient and Kg is the preconditioned gradient). (written as “[<span
id="id164" class="problematic">\|</span>](#id163)grad\|\_K” in JDFTx
output).

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">alpha</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.alpha"
class="headerlink" title="Link to this definition"></a>  
The step size of the final geometric step in the most recent JDFTx call.

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">linmin</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.linmin"
class="headerlink" title="Link to this definition"></a>  
The final normalized projection of the geometric step direction onto the
gradient for the most recent JDFTx call.

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">abs_magneticmoment</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.abs_magneticmoment"
class="headerlink" title="Link to this definition"></a>  
The absolute magnetic moment of the most recent JDFTx call.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">tot_magneticmoment</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.tot_magneticmoment"
class="headerlink" title="Link to this definition"></a>  
The total magnetic moment of the most recent JDFTx call.

Type<span class="colon">:</span>  
float \| None

<span class="sig-name descname"><span class="pre">mu</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.mu" class="headerlink"
title="Link to this definition"></a>  
The Fermi energy in eV of the most recent JDFTx call.

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">elec_e</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.elec_e"
class="headerlink" title="Link to this definition"></a>  
The final energy in eV of the most recent electronic optimization step.

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">elec_nstep</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.elec_nstep"
class="headerlink" title="Link to this definition"></a>  
The number of electronic optimization steps in the most recent JDFTx
call.

Type<span class="colon">:</span>  
int

<span class="sig-name descname"><span class="pre">elec_grad_k</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.elec_grad_k"
class="headerlink" title="Link to this definition"></a>  
The final norm of the preconditioned gradient for electronic
optimization of the most recent JDFTx call (evaluated as dot(g, Kg),
where g is the gradient and Kg is the preconditioned gradient). (written
as “[<span id="id166" class="problematic">\|</span>](#id165)grad\|\_K”
in JDFTx output).

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">elec_alpha</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.elec_alpha"
class="headerlink" title="Link to this definition"></a>  
The step size of the final electronic step in the most recent JDFTx
call.

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">elec_linmin</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.elec_linmin"
class="headerlink" title="Link to this definition"></a>  
The final normalized projection of the electronic step direction onto
the gradient for the most recent JDFTx call.

Type<span class="colon">:</span>  
float

<span class="sig-name descname"><span class="pre">infile</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.infile"
class="headerlink" title="Link to this definition"></a>  
The JDFTXInfile object representing the input parameters of the
JDFTXOutfile.

Type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile">JDFTXInfile</a>

Magic Methods:  
\_\_getitem\_\_(key: str \| int) -\> Any: Decides behavior of how JDFTXOutfile objects are indexed. If the key is a  
string, it will return the value of the property with the same name. If
the key is an integer, it will return the slice of the JDFTXOutfile
object at that index.

\_\_len\_\_() -\> int: Returns the number of slices in the JDFTXOutfile
object. \_\_getattr\_\_(name: str) -\> Any: Returns the value of the
property with the same name as the input string. \_\_str\_\_() -\> str:
Returns a string representation of the JDFTXOutfile object.

<span class="sig-name descname"><span class="pre">a</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id167" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">abs_magneticmoment</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id168" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">alpha</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id169" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">as_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/outputs.py#L756-L770"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.as_dict"
class="headerlink" title="Link to this definition"></a>  
Convert the JDFTXOutfile object to a dictionary.

Returns<span class="colon">:</span>  
A dictionary representation of the JDFTXOutfile object.

Return type<span class="colon">:</span>  
dict

<span class="sig-name descname"><span class="pre">atom_coords</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id170" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">atom_coords_final</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id171" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">atom_coords_initial</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id172" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">atom_elements</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id173" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">atom_elements_int</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id174" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">atom_types</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id175" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">b</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id176" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">broadening</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id177" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">broadening_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id178" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">c</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id179" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">converged</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id180" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">e</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id181" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">efermi</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id182" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">egap</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id183" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">elec_alpha</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id184" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">elec_e</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id185" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">elec_grad_k</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id186" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">elec_linmin</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id187" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">elec_nstep</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id188" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">elecmindata</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="#pymatgen.io.jdftx.jelstep.JElSteps" class="reference internal"
title="pymatgen.io.jdftx.jelstep.JElSteps"><span
class="pre">JElSteps</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id189" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">electronic_output</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.electronic_output"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">emax</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id190" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">emin</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id191" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">eopt_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id192" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">etype</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id193" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">fftgrid</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id194" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">fluid</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id195" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">forces</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">np.ndarray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.forces"
class="headerlink" title="Link to this definition"></a>  

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_calc_dir</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">calc_dir</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Path</span></span>*, *<span class="n"><span class="pre">is_bgw</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">none_slice_on_error</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile"
class="reference internal"
title="pymatgen.io.jdftx.outputs.JDFTXOutfile"><span
class="pre">JDFTXOutfile</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/outputs.py#L672-L691"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.from_calc_dir"
class="headerlink" title="Link to this definition"></a>  
Create a JDFTXOutfile object from a directory containing JDFTx out
files.

Parameters<span class="colon">:</span>  
- **calc_dir** (*str* *\|* *Path*) – The path to the directory
  containing the JDFTx out files.

- **is_bgw** (*bool*) – Mark True if data must be usable for BGW
  calculations. This will change the behavior of the parser to be
  stricter with certain criteria.

- **none_slice_on_error** (*bool*) – If True, will return None if an
  error occurs while parsing a slice instead of halting the parsing
  process. This can be useful for parsing files with multiple slices
  where some slices may be incomplete or corrupted.

Returns<span class="colon">:</span>  
The JDFTXOutfile object.

Return type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile"
class="reference internal"
title="pymatgen.io.jdftx.outputs.JDFTXOutfile">JDFTXOutfile</a>

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">file_path</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Path</span></span>*, *<span class="n"><span class="pre">is_bgw</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">none_slice_on_error</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile"
class="reference internal"
title="pymatgen.io.jdftx.outputs.JDFTXOutfile"><span
class="pre">JDFTXOutfile</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/outputs.py#L693-L721"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.from_file"
class="headerlink" title="Link to this definition"></a>  
Create a JDFTXOutfile object from a JDFTx out file.

Parameters<span class="colon">:</span>  
- **file_path** (*str* *\|* *Path*) – The path to the JDFTx out file.

- **is_bgw** (*bool*) – Mark True if data must be usable for BGW
  calculations. This will change the behavior of the parser to be
  stricter with certain criteria.

- **none_slice_on_error** (*bool* *\|* *None*) – If True, will return
  None if an error occurs while parsing a slice instead of halting the
  parsing process. This can be useful for parsing files with multiple
  slices where some slices may be incomplete or corrupted. If False, all
  slices may raise errors. If None, only the final slice can raise an
  error upon parsing (default behavior)

Returns<span class="colon">:</span>  
The JDFTXOutfile object.

Return type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile"
class="reference internal"
title="pymatgen.io.jdftx.outputs.JDFTXOutfile">JDFTXOutfile</a>

<span class="sig-name descname"><span class="pre">geom_opt</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id196" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">geom_opt_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id197" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">grad_k</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id198" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">has_solvation</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id199" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">homo</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id200" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">homo_filling</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id201" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">infile</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile"><span
class="pre">JDFTXInfile</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id202" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">is_gc</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id203" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">is_metal</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id204" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">jsettings_electronic</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="#pymatgen.io.jdftx.jminsettings.JMinSettingsElectronic"
class="reference internal"
title="pymatgen.io.jdftx.jminsettings.JMinSettingsElectronic"><span
class="pre">JMinSettingsElectronic</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id205" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">jsettings_fluid</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="#pymatgen.io.jdftx.jminsettings.JMinSettingsFluid"
class="reference internal"
title="pymatgen.io.jdftx.jminsettings.JMinSettingsFluid"><span
class="pre">JMinSettingsFluid</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id206" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">jsettings_ionic</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="#pymatgen.io.jdftx.jminsettings.JMinSettingsIonic"
class="reference internal"
title="pymatgen.io.jdftx.jminsettings.JMinSettingsIonic"><span
class="pre">JMinSettingsIonic</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id207" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">jsettings_lattice</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="#pymatgen.io.jdftx.jminsettings.JMinSettingsLattice"
class="reference internal"
title="pymatgen.io.jdftx.jminsettings.JMinSettingsLattice"><span
class="pre">JMinSettingsLattice</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id208" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">jstrucs</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="#pymatgen.io.jdftx.joutstructures.JOutStructures"
class="reference internal"
title="pymatgen.io.jdftx.joutstructures.JOutStructures"><span
class="pre">JOutStructures</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id209" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">kgrid</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">int</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id210" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">lattice</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">np.ndarray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id211" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">lattice_final</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">np.ndarray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id212" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">lattice_initial</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">np.ndarray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id213" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">linmin</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id214" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">lumo</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id215" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">lumo_filling</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id216" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">mu</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id217" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">nat</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id218" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">nbands</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id219" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">nspin</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id220" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">nstep</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id221" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">pp_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id222" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">prefix</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id223" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">pwcut</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id224" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">rhocut</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id225" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">semicore_electrons</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id226" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">semicore_electrons_uncharged</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id227" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">slices</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><a href="#pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice"
class="reference internal"
title="pymatgen.io.jdftx.jdftxoutfileslice.JDFTXOutfileSlice"><span
class="pre">JDFTXOutfileSlice</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id228" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">spintype</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id229" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">strain</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">np.ndarray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id230" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">stress</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">np.ndarray</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id231" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">structure</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id232" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">to_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../../../.venv/lib/python3.11/site-packages/monty/dev.py#L772-L774"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.to_dict"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">to_jdftxinfile</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile"><span
class="pre">JDFTXInfile</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/outputs.py#L724-L732"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.to_jdftxinfile"
class="headerlink" title="Link to this definition"></a>  
Convert the JDFTXOutfile object to a JDFTXInfile object with the most
recent structure. If the input structure is desired, simply fetch
JDFTXOutfile.infile

Returns<span class="colon">:</span>  
A JDFTXInfile object representing the input parameters of the
JDFTXOutfile.

Return type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile">JDFTXInfile</a>

<span class="sig-name descname"><span class="pre">tot_magneticmoment</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id233" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">total_electrons</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id234" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">total_electrons_uncharged</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id235" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">trajectory</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="pymatgen.core.html#pymatgen.core.trajectory.Trajectory"
class="reference internal"
title="pymatgen.core.trajectory.Trajectory"><span
class="pre">Trajectory</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id236" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">truncation_radius</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id237" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">truncation_type</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id238" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">valence_electrons</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id239" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">valence_electrons_uncharged</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id240" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">vibrational_energy_components</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">float</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a
href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.vibrational_energy_components"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">vibrational_modes</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile.vibrational_modes"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">xc_func</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id241" class="headerlink"
title="Link to this definition"></a>  

<!-- -->

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">JDFTXOutputs</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">calc_dir:</span> <span class="pre">str</span> <span class="pre">\|</span> <span class="pre">\~pathlib.Path</span></span>*, *<span class="n"><span class="pre">outfile_name:</span> <span class="pre">str</span> <span class="pre">\|</span> <span class="pre">\~pathlib.Path</span> <span class="pre">\|</span> <span class="pre">None</span></span>*, *<span class="n"><span class="pre">store_vars:</span> <span class="pre">list\[str\]</span> <span class="pre">=</span> <span class="pre">\<factory\></span></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/outputs.py#L85-L331"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutputs" class="headerlink"
title="Link to this definition"></a>  
Bases: <span class="pre">`object`</span>

JDFTx outputs parsing class.

A class to read and process JDFTx outputs.

<span class="sig-name descname"><span class="pre">from_calc_dir(calc_dir</span></span>  
str \| Path, store_vars: list\[str\] = None) -\> JDFTXOutputs: Return
JDFTXOutputs object from the path to a directory containing JDFTx out
files.

<span class="sig-name descname"><span class="pre">calc_dir</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutputs.calc_dir"
class="headerlink" title="Link to this definition"></a>  
The path to the directory containing the JDFTx output files.

Type<span class="colon">:</span>  
str \| Path

<span class="sig-name descname"><span class="pre">store_vars</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutputs.store_vars"
class="headerlink" title="Link to this definition"></a>  
A list of the names of dump files to read and store.

Type<span class="colon">:</span>  
list\[str\]

<span class="sig-name descname"><span class="pre">paths</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutputs.paths"
class="headerlink" title="Link to this definition"></a>  
A dictionary of the paths to the dump files.

Type<span class="colon">:</span>  
dict\[str, Path\]

<span class="sig-name descname"><span class="pre">outfile</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutputs.outfile"
class="headerlink" title="Link to this definition"></a>  
The JDFTXOutfile object for the out file.

Type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile"
class="reference internal"
title="pymatgen.io.jdftx.outputs.JDFTXOutfile">JDFTXOutfile</a>

<span class="sig-name descname"><span class="pre">bandProjections</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutputs.bandProjections"
class="headerlink" title="Link to this definition"></a>  
The band projections. Stored in shape (nstates, nbands, nproj) where
nstates is nspin\*nkpts (nkpts may not equal prod(kfolding) if symmetry
reduction occurred), nbands is the number of bands, and nproj is the
number of projections. This shape is chosen instead of the pymatgen
convention of (nspin, nkpt, nbands, nion, nionproj) to save on memory as
nonionproj is different depending on the ion type. This array may also
be complex if specified in ‘band-projections-params’ in the JDFTx input,
allowing for pCOHP analysis.

Type<span class="colon">:</span>  
np.ndarray

<span class="sig-name descname"><span class="pre">eigenvals</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutputs.eigenvals"
class="headerlink" title="Link to this definition"></a>  
The eigenvalues. Stored in shape (nstates, nbands) where nstates is
nspin\*nkpts (nkpts may not equal prod(kfolding) if symmetry reduction
occurred) and nbands is the number of bands.

Type<span class="colon">:</span>  
np.ndarray

<span class="sig-name descname"><span class="pre">orb_label_list</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutputs.orb_label_list"
class="headerlink" title="Link to this definition"></a>  
A tuple of the orbital labels for the bandProjections file, where the
i’th element describes the i’th orbital. Orbital labels are formatted as
“\<ion\>#\<ion-number\>(\<orbital\>)”, where \<ion\> is the element
symbol of the ion, \<ion-number\> is the 1-based index of the ion-type
in the structure (ie C#2 would be the second carbon atom, but not
necessarily the second ion in the structure), and \<orbital\> is a
string describing “l” and “ml” quantum numbers (ie “p_x” or “d_yz”).
Note that while “z” corresponds to the “z” axis, “x” and “y” are
arbitrary and may not correspond to the actual x and y axes of the
structure. In the case where multiple shells of a given “l” are
available within the projections, a 0-based index will appear mimicking
a principle quantum number (ie “0px” for first shell and “1px” for
second shell). The actual principal quantum number is not stored in the
JDFTx output files and must be inferred by the user.

Type<span class="colon">:</span>  
tuple\[str, …\]

<span class="sig-name descname"><span class="pre">kpts</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutputs.kpts"
class="headerlink" title="Link to this definition"></a>  
A list of the k-points used in the calculation. Each k-point is a 3D
numpy array.

Type<span class="colon">:</span>  
list\[np.ndarray\]

<span class="sig-name descname"><span class="pre">wk_list</span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutputs.wk_list"
class="headerlink" title="Link to this definition"></a>  
A list of the weights for the k-points used in the calculation.

Type<span class="colon">:</span>  
list\[np.ndarray\]

<span class="sig-name descname"><span class="pre">bandProjections</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">NDArray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id242" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">bandstructure</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a
href="pymatgen.electronic_structure.html#pymatgen.electronic_structure.bandstructure.BandStructure"
class="reference internal"
title="pymatgen.electronic_structure.bandstructure.BandStructure"><span
class="pre">BandStructure</span></a><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutputs.bandstructure"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">calc_dir</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Path</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id243" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">eigenvals</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">NDArray</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id244" class="headerlink"
title="Link to this definition"></a>  

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_calc_dir</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">calc_dir</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Path</span></span>*, *<span class="n"><span class="pre">store_vars</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">outfile_name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Path</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.jdftx.outputs.JDFTXOutputs"
class="reference internal"
title="pymatgen.io.jdftx.outputs.JDFTXOutputs"><span
class="pre">JDFTXOutputs</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/outputs.py#L135-L156"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutputs.from_calc_dir"
class="headerlink" title="Link to this definition"></a>  
Create a JDFTXOutputs object from a directory containing JDFTx out
files.

Parameters<span class="colon">:</span>  
- **calc_dir** (*str* *\|* *Path*) – The path to the directory
  containing the JDFTx out files.

- **is_bgw** (*bool*) – Mark True if data must be usable for BGW
  calculations. This will change the behavior of the parser to be
  stricter with certain criteria.

- **none_slice_on_error** (*bool*) – If True, will return None if an
  error occurs while parsing a slice instead of halting the parsing
  process. This can be useful for parsing files with multiple slices
  where some slices may be incomplete or corrupted.

- **outfile_name** (*str* *\|* *Path*) – The name of the outfile to use.
  If None, will search for the outfile in the calc_dir. If provided,
  will concatenate with calc_dir as the outfile path. Use this if the
  calc_dir contains multiple files that may be mistaken for the outfile
  (ie multiple files with the ‘.out’ suffix).

Returns<span class="colon">:</span>  
The JDFTXOutputs object.

Return type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.outputs.JDFTXOutputs"
class="reference internal"
title="pymatgen.io.jdftx.outputs.JDFTXOutputs">JDFTXOutputs</a>

<span class="sig-name descname"><span class="pre">kpts</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">NDArray</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id245" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">orb_label_list</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">tuple</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="p"><span class="pre">...</span></span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id246" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">outfile</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="#pymatgen.io.jdftx.outputs.JDFTXOutfile"
class="reference internal"
title="pymatgen.io.jdftx.outputs.JDFTXOutfile"><span
class="pre">JDFTXOutfile</span></a>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id247" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">outfile_name</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Path</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.outputs.JDFTXOutputs.outfile_name"
class="headerlink" title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">paths</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Path</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id248" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">store_vars</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">\]</span></span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id249" class="headerlink"
title="Link to this definition"></a>  

<span class="sig-name descname"><span class="pre">wk_list</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">list</span><span class="p"><span class="pre">\[</span></span><span class="pre">NDArray</span><span class="p"><span class="pre">\]</span></span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">None</span>*<a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/io/jdftx/outputs.py"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#id250" class="headerlink"
title="Link to this definition"></a>  

</div>

<div id="module-pymatgen.io.jdftx.sets" class="section">

<span id="pymatgen-io-jdftx-sets-module"></span>

## pymatgen.io.jdftx.sets module<a href="#module-pymatgen.io.jdftx.sets" class="headerlink"
title="Link to this heading"></a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">JdftxInputSet</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">jdftxinput</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile"><span
class="pre">JDFTXInfile</span></a></span>*, *<span class="n"><span class="pre">structure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="pymatgen.core.html#pymatgen.core.structure.Structure"
class="reference internal"
title="pymatgen.core.structure.Structure"><span
class="pre">Structure</span></a></span>*<span class="sig-paren">)</span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/sets.py#L17-L75"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.sets.JdftxInputSet" class="headerlink"
title="Link to this definition"></a>  
Bases: <a href="pymatgen.io.html#pymatgen.io.core.InputSet"
class="reference internal" title="pymatgen.io.core.InputSet"><span
class="pre"><code class="sourceCode python">InputSet</code></span></a>

A class to represent a JDFTx input file as a JDFTx InputSet.

Parameters<span class="colon">:</span>  
**jdftxinput** – A JdftxInput object

Instantiate an InputSet.

Parameters<span class="colon">:</span>  
- **inputs** – The core mapping of filename: file contents that defines
  the InputSet data. This should be a dict where keys are filenames and
  values are InputFile objects or strings representing the entire
  contents of the file. If a value is not an InputFile object nor a str,
  but has a \_\_str\_\_ method, this str representation of the object
  will be written to the corresponding file. This mapping will become
  the .inputs attribute of the InputSet.

- **\*\*kwargs** – Any kwargs passed will be set as class attributes
  e.g. InputSet(inputs={}, foo=’bar’) will make InputSet.foo == ‘bar’.

*<span class="k"><span class="pre">static</span></span><span class="w"> </span>*<span class="sig-name descname"><span class="pre">from_file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">file</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.jdftx.sets.JdftxInputSet"
class="reference internal"
title="pymatgen.io.jdftx.sets.JdftxInputSet"><span
class="pre">JdftxInputSet</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/sets.py#L60-L75"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.sets.JdftxInputSet.from_file"
class="headerlink" title="Link to this definition"></a>  
Load a set of JDFTx inputs from a filename.

Parameters<span class="colon">:</span>  
**directory** – Input file to read JDFTx inputs from.

<span class="sig-name descname"><span class="pre">write_input</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">directory</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">\|</span></span><span class="w"> </span><span class="pre">Path</span></span>*, *<span class="n"><span class="pre">infile</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PathLike</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'init.in'</span></span>*, *<span class="n"><span class="pre">make_dir</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">overwrite</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/sets.py#L31-L58"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.sets.JdftxInputSet.write_input"
class="headerlink" title="Link to this definition"></a>  
Write JDFTx input file to a directory.

Parameters<span class="colon">:</span>  
- **directory** – Directory to write input files to.

- **make_dir** – Whether to create the directory if it does not already
  exist.

- **overwrite** – Whether to overwrite an input file if it already
  exists.

<!-- -->

<span class="sig-name descname"><span class="pre">condense_jdftxinputs</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">jdftxinput</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile"><span
class="pre">JDFTXInfile</span></a></span>*, *<span class="n"><span class="pre">jdftxstructure</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a href="#pymatgen.io.jdftx.inputs.JDFTXStructure"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXStructure"><span
class="pre">JDFTXStructure</span></a></span>*<span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">→</span> <span class="sig-return-typehint"><a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile"><span
class="pre">JDFTXInfile</span></a></span></span><a
href="https://github.com/materialsproject/pymatgen/blob/v2025.6.14/src/pymatgen/core/../io/jdftx/sets.py#L78-L102"
class="reference external"><span class="viewcode-link"><span
class="pre">[source]</span></span></a><a href="#pymatgen.io.jdftx.sets.condense_jdftxinputs"
class="headerlink" title="Link to this definition"></a>  
Combine JDFTXInfile and JDFTxStructure into complete JDFTXInfile.

Function combines a JDFTXInfile class with calculation settings and a
JDFTxStructure that defines the structure into one JDFTXInfile instance.

Parameters<span class="colon">:</span>  
- **jdftxinput** (<a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
  class="reference internal"
  title="pymatgen.io.jdftx.inputs.JDFTXInfile"><em>JDFTXInfile</em></a>)
  – A JDFTXInfile object with calculation settings.

- **jdftxstructure** (<a href="#pymatgen.io.jdftx.inputs.JDFTXStructure"
  class="reference internal"
  title="pymatgen.io.jdftx.inputs.JDFTXStructure"><em>JDFTXStructure</em></a>)
  – A JDFTXStructure object that defines the structure.

Returns<span class="colon">:</span>  
A JDFTXInfile that includes the calculation parameters and input
structure.

Return type<span class="colon">:</span>  
<a href="#pymatgen.io.jdftx.inputs.JDFTXInfile"
class="reference internal"
title="pymatgen.io.jdftx.inputs.JDFTXInfile">JDFTXInfile</a>

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
