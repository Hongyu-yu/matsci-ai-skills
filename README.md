# 🧠 AI Skills Library for Materials Science & Computational Physics

<p align="center">
  <strong>A curated collection of AI assistant skills for materials science, computational chemistry, computational physics, and scientific computing</strong>
</p>

<p align="center">
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-skill-categories">Skills</a> •
  <a href="#-custom-skills">Custom Skills</a> •
  <a href="#-contributing">Contributing</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
  <img src="https://img.shields.io/badge/Skills-45+-blue.svg" alt="Skills">
  <img src="https://img.shields.io/badge/Compatible-Codex%20%7C%20Claude%20%7C%20Kiro-green.svg" alt="Compatible">
</p>

<p align="center">
  <strong>English</strong> | <a href="README_CN.md">中文</a>
</p>

---

## 📖 Overview

> **💡 Philosophy: Quality over Quantity**
> 
> Skills are not about having as many as possible — it's about having the *right* ones. Too many skills can overwhelm the AI context and reduce effectiveness. This repository contains a **carefully curated** collection of skills specifically selected for **materials science**, **computational chemistry**, and **computational physics** research workflows.

### ✨ Highlights

- **8 Pymatgen sub-skills** — The powerful [Pymatgen](https://pymatgen.org/) library is split into focused modules (core, analysis, I/O, symmetry, etc.) for better AI context management
- **OpenMX skill** — Dedicated support for [OpenMX](http://www.openmx-square.org/) DFT calculations (v3.9 focused)
- **Curated community skills** — Hand-picked skills for scientific computing, ML, and document processing

This repository contains a comprehensive library of **skills** - structured knowledge modules that enhance AI assistants' capabilities in specific domains. Each skill provides:

| Feature | Description |
|---------|-------------|
| 🎯 **Domain Expertise** | Specialized knowledge for specific scientific tasks |
| 📝 **Code Patterns** | Ready-to-use implementation templates |
| ✅ **Best Practices** | Industry-standard approaches and guidelines |
| 📚 **Reference Materials** | Documentation, examples, and scripts |

### Compatibility

These skills are designed to work with multiple AI coding assistants:
- **OpenAI Codex** - Via skills integration
- **Anthropic Claude** - Via project knowledge
- **AWS Kiro** - Via skills system

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/hongyu-yu/matsci-ai-skills.git
cd matsci-ai-skills
```

### 2. Use with Your AI Assistant

Point your AI assistant to the relevant skill directory. Each skill contains:

```
skills/
└── skill-name/
    ├── SKILL.md           # Main skill definition (required)
    ├── README.md          # Detailed documentation (optional)
    ├── references/        # Reference materials
    ├── scripts/           # Example scripts
    └── examples/          # Usage examples
```

### 3. Reference in Conversations

Simply mention the skill topic in your conversation, and the AI will leverage the relevant knowledge.

---

## 📂 Skill Categories

### 🔬 Materials Science & Computational Chemistry

#### Pymatgen Ecosystem (⭐ Custom)

| Skill | Description |
|-------|-------------|
| [pymatgen-core](skills/pymatgen-core/) | Core structures: Element, Specie, Composition, Lattice, Structure, Molecule |
| [pymatgen-analysis](skills/pymatgen-analysis/) | Phase diagrams, Pourbaix, reactions, structure matching, surfaces, elasticity |
| [pymatgen-io](skills/pymatgen-io/) | Non-VASP I/O: CIF, XYZ, Gaussian, CP2K, QE, ABINIT, LAMMPS, etc. |
| [pymatgen-io-vasp](skills/pymatgen-io-vasp/) | VASP I/O: input generation, POTCAR handling, output parsing |
| [pymatgen-ext](skills/pymatgen-ext/) | External data: Materials Project (MPRester), OPTIMADE, COD |
| [pymatgen-phonon](skills/pymatgen-phonon/) | Phonon band structure, DOS, Gruneisen, IR spectra |
| [pymatgen-symmetry](skills/pymatgen-symmetry/) | Space group analysis, standardization, k-path generation |
| [pymatgen-electronic-structure](skills/pymatgen-electronic-structure/) | DOS, band structures, COHP/COOP, plotting utilities |

#### DFT Codes & Simulation Tools

| Skill | Description | Origin |
|-------|-------------|--------|
| [openmx](skills/openmx/) | OpenMX v3.9 DFT calculations and workflows | ⭐ Custom |
| [vasp](skills/vasp/) | VASP DFT calculation setup and analysis | Community |
| [python-ase](skills/python-ase/) | Atomic Simulation Environment workflows | Community |
| [fairchem](skills/fairchem/) | Meta's FAIRChem ML potentials for materials | Community |
| [materials-databases](skills/materials-databases/) | AFLOW & Materials Project database access | Community |
| [materials-properties](skills/materials-properties/) | First-principles property calculations with ASE | Community |

---

### 🐍 Python Scientific Computing

| Skill | Description |
|-------|-------------|
| [python-jax](skills/python-jax/) | JAX high-performance computing with autodiff |
| [python-optimization](skills/python-optimization/) | Mathematical optimization (scipy, pyomo, cvxpy, GEKKO) |
| [python-multiobjective-optimization](skills/python-multiobjective-optimization/) | Pareto optimization (pymoo, NSGA-II, MOEA/D) |
| [python-plotting](skills/python-plotting/) | Matplotlib, Seaborn, Plotly visualization |
| [python-regression-statistics](skills/python-regression-statistics/) | Statistical modeling and outlier detection |
| [scikit-learn](skills/scikit-learn/) | Machine learning with scikit-learn |
| [sympy](skills/sympy/) | Symbolic mathematics |
| [astropy](skills/astropy/) | Astronomy and astrophysics |
| [fluidsim](skills/fluidsim/) | Computational fluid dynamics |

---

### 🤖 Deep Learning & ML

| Skill | Description |
|-------|-------------|
| [pytorch-lightning](skills/pytorch-lightning/) | PyTorch Lightning training framework |
| [torch-geometric](skills/torch-geometric/) | Graph Neural Networks (PyG) |
| [transformers](skills/transformers/) | Hugging Face Transformers |

---

### 🔄 ML Symmetry & Equivariance

| Skill | Description |
|-------|-------------|
| [symmetry-discovery-questionnaire](skills/symmetry-discovery-questionnaire/) | Identify data symmetries collaboratively |
| [symmetry-group-identifier](skills/symmetry-group-identifier/) | Map symmetries to mathematical groups |
| [symmetry-validation-suite](skills/symmetry-validation-suite/) | Validate symmetry assumptions empirically |
| [equivariant-architecture-designer](skills/equivariant-architecture-designer/) | Design equivariant neural networks |
| [model-equivariance-auditor](skills/model-equivariance-auditor/) | Verify model equivariance |

---

### 📄 Document Processing

| Skill | Description |
|-------|-------------|
| [pdf](skills/pdf/) | PDF manipulation and extraction |
| [docx](skills/docx/) | Word document processing |
| [pptx](skills/pptx/) | PowerPoint manipulation |
| [xlsx](skills/xlsx/) | Excel spreadsheet processing |
| [markitdown](skills/markitdown/) | Convert files to Markdown |
| [latex-posters](skills/latex-posters/) | LaTeX poster creation |

---

### 🧩 Decision & Analysis Frameworks

| Skill | Description |
|-------|-------------|
| [brainstorming](skills/brainstorming/) | Structured ideation techniques |
| [planning](skills/planning/) | Project planning methodologies |
| [decision-matrix](skills/decision-matrix/) | Multi-criteria decision analysis |
| [causal-inference-root-cause](skills/causal-inference-root-cause/) | Root cause analysis |
| [decomposition-reconstruction](skills/decomposition-reconstruction/) | System decomposition |
| [design-of-experiments](skills/design-of-experiments/) | DOE methodologies |
| [estimation-fermi](skills/estimation-fermi/) | Fermi estimation |
| [meta-prompt-engineering](skills/meta-prompt-engineering/) | Prompt optimization |
| [postmortem](skills/postmortem/) | Incident analysis |
| [systems-thinking-leverage](skills/systems-thinking-leverage/) | Systems thinking |

---

### 🛠️ Utilities

| Skill | Description |
|-------|-------------|
| [memory](skills/memory/) | File-based long-term memory |
| [skill-creator](skills/skill-creator/) | Create new skills |

---

## ⭐ Custom Skills

The following skills were **created by the repository maintainer** specifically for materials science research workflows:

### 🎯 Why Custom Skills?

**Pymatgen** is one of the most powerful Python libraries for materials science, but its extensive API can be overwhelming. Instead of creating a single monolithic skill, I split it into **8 focused sub-skills** covering different modules:
- `pymatgen-core` → Structure manipulation
- `pymatgen-analysis` → Thermodynamics & phase diagrams  
- `pymatgen-io` / `pymatgen-io-vasp` → File I/O
- `pymatgen-ext` → External databases
- `pymatgen-phonon` → Phonon analysis
- `pymatgen-symmetry` → Symmetry operations
- `pymatgen-electronic-structure` → DOS & band structures

**OpenMX** is a powerful DFT code based on localized basis sets, widely used for large-scale calculations. I created a dedicated skill (`openmx`) covering input preparation, calculation workflows, and output parsing for OpenMX v3.9.

### 🏆 Custom-Built Skills

| Skill | Description | Highlights |
|-------|-------------|------------|
| **pymatgen-core** | Pymatgen core objects and structure manipulation | Element, Specie, Composition, Lattice, Structure, Molecule |
| **pymatgen-analysis** | Materials analysis workflows | Phase diagrams, Pourbaix, reactions, surfaces, elasticity |
| **pymatgen-io** | Non-VASP file I/O | CIF, XYZ, Gaussian, CP2K, QE, ABINIT, LAMMPS |
| **pymatgen-io-vasp** | VASP-specific I/O | Input generation, POTCAR, output parsing |
| **pymatgen-ext** | External data access | Materials Project, OPTIMADE, COD |
| **pymatgen-phonon** | Phonon analysis | Band structure, DOS, Gruneisen, IR spectra |
| **pymatgen-symmetry** | Symmetry analysis | Space groups, standardization, k-paths |
| **pymatgen-electronic-structure** | Electronic structure | DOS, bands, COHP/COOP, plotting |
| **openmx** | OpenMX DFT workflows | v3.9 focused, SCF, bands, DOS, NEB, SOC |

These custom skills include:
- ✅ Detailed workflow examples from real research experience
- ✅ Best practices and common pitfalls
- ✅ Integration patterns between tools
- ✅ Ready-to-run example scripts

---

## 📋 Requirements

### Core Dependencies

```bash
# Core scientific computing
pip install numpy scipy matplotlib pandas

# Materials science
pip install ase pymatgen phonopy mp-api

# Machine learning
pip install torch scikit-learn

# Document processing
pip install python-docx python-pptx openpyxl pypdf
```

### Environment Setup

Some skills may reference environment-specific configurations. Before using:

1. **Python Environment** - Update conda/virtualenv activation commands as needed
2. **Data Paths** - Update paths to datasets or pseudopotential directories
3. **API Keys** - Set up required API keys (e.g., Materials Project API key)

```bash
# Example: Set Materials Project API key
export MP_API_KEY="your_api_key_here"
```

---

## 🤝 Contributing

We welcome contributions from the community! This is intended to be a **long-term maintained** repository.

### How to Contribute

1. **Fork** the repository
2. **Create** a new skill directory under `skills/`
3. **Add** a `SKILL.md` with the skill definition (required)
4. **Include** reference materials, scripts, and examples
5. **Submit** a Pull Request

### Skill Structure Template

```
skills/
└── your-skill-name/
    ├── SKILL.md           # Required: Main skill definition
    ├── README.md          # Optional: Detailed documentation
    ├── references/        # Reference materials and docs
    │   └── *.md
    ├── scripts/           # Example scripts
    │   └── *.py
    └── examples/          # Usage examples
        └── *.md
```

### SKILL.md Template

```yaml
---
name: your-skill-name
description: "Brief description of when to use this skill"
metadata:
  short-description: short name
---

# Skill Title

## Overview
[What this skill does]

## When to Use This Skill
[Trigger conditions]

## Core Capabilities
[Main features]

## Quick Workflow
[Step-by-step guide]

## Resources
[Links to references, scripts, examples]
```

### Contribution Guidelines

- 📝 Follow the existing skill structure
- 🔍 Ensure skills are well-documented
- ✅ Test scripts before submitting
- 🌐 Remove any personal/private paths or credentials
- 📚 Include references to official documentation

---

## 📜 License

This project is licensed under the **MIT License** - see individual skill directories for any additional licensing information.

---

## 📬 Contact

- **Issues**: [GitHub Issues](https://github.com/hongyu-yu/matsci-ai-skills/issues)
- **Discussions**: [GitHub Discussions](https://github.com/hongyu-yu/matsci-ai-skills/discussions)

---

<p align="center">
  <strong>⭐ If you find this useful, please give it a star! ⭐</strong>
  <br>
  <em>Your star helps others discover this resource and motivates continued development.</em>
</p>

<p align="center">
  <a href="https://github.com/hongyu-yu/matsci-ai-skills/stargazers">
    <img src="https://img.shields.io/github/stars/hongyu-yu/matsci-ai-skills?style=social" alt="GitHub stars">
  </a>
</p>

<p align="center">
  <em>This is a community-maintained collection. Skills are provided as-is and may require adaptation for your specific use case.</em>
</p>
