# 🧠 材料科学与计算物理 AI Skills 库

<p align="center">
  <strong>为材料科学、计算化学、计算物理和科学计算精心策划的 AI 助手技能集合</strong>
</p>

<p align="center">
  <a href="#-快速开始">快速开始</a> •
  <a href="#-技能分类">技能分类</a> •
  <a href="#-自定义技能">自定义技能</a> •
  <a href="#-贡献指南">贡献指南</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
  <img src="https://img.shields.io/badge/Skills-45+-blue.svg" alt="Skills">
  <img src="https://img.shields.io/badge/兼容-Codex%20%7C%20Claude%20%7C%20Kiro-green.svg" alt="Compatible">
  <a href="https://github.com/hongyu-yu/matsci-ai-skills/stargazers">
    <img src="https://img.shields.io/github/stars/hongyu-yu/matsci-ai-skills?style=social" alt="GitHub stars">
  </a>
</p>

<p align="center">
  <a href="README.md">English</a> | <strong>中文</strong>
</p>

---

## 📖 概述

> **💡 理念：质量优于数量**
> 
> Skills 不是越多越好——关键是要有*合适的*技能。过多的 skills 会占用 AI 上下文，降低效果。本仓库包含**精心挑选**的技能集合，专门针对**材料科学**、**计算化学**和**计算物理**研究工作流程。

### ✨ 亮点

- **8 个 Pymatgen 子技能** — 强大的 [Pymatgen](https://pymatgen.org/) 库被拆分为专注的模块（core、analysis、I/O、symmetry 等），以便更好地管理 AI 上下文
- **OpenMX 技能** — 专门支持 [OpenMX](http://www.openmx-square.org/) DFT 计算（聚焦 v3.9 版本）
- **精选社区技能** — 手工挑选的科学计算、机器学习和文档处理技能

本仓库包含一个全面的 **skills** 库——结构化的知识模块，用于增强 AI 助手在特定领域的能力。每个 skill 提供：

| 特性 | 描述 |
|------|------|
| 🎯 **领域专业知识** | 针对特定科学任务的专业知识 |
| 📝 **代码模式** | 即用型实现模板 |
| ✅ **最佳实践** | 行业标准方法和指南 |
| 📚 **参考资料** | 文档、示例和脚本 |

### 兼容性

这些 skills 设计用于多种 AI 编程助手：
- **OpenAI Codex** - 通过 skills 集成
- **Anthropic Claude** - 通过 Project Knowledge
- **AWS Kiro** - 通过 skills 系统

---

## 🚀 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/hongyu-yu/matsci-ai-skills.git
cd matsci-ai-skills
```

### 2. 与 AI 助手配合使用

将 AI 助手指向相关的 skill 目录。每个 skill 包含：

```
skills/
└── skill-name/
    ├── SKILL.md           # 主要技能定义（必需）
    ├── README.md          # 详细文档（可选）
    ├── references/        # 参考资料
    ├── scripts/           # 示例脚本
    └── examples/          # 使用示例
```

### 3. 使用示例

**与 Claude 配合使用：**
1. 在 Claude 的skills目录中添加需要的skills文件夹
2. 直接对话："帮我创建一个 Fe2O3 的结构并导出为 POSCAR"

**与 Codex 配合使用：**
1. 将相关 skill 文件添加到 `.codex/skills/` 目录
2. Codex 会自动识别并使用这些技能

---

## 📂 技能分类

### 🔬 材料科学与计算化学

#### Pymatgen 生态系统（⭐ 自定义）

| 技能 | 描述 |
|------|------|
| [pymatgen-core](skills/pymatgen-core/) | 核心结构：Element、Specie、Composition、Lattice、Structure、Molecule |
| [pymatgen-analysis](skills/pymatgen-analysis/) | 相图、Pourbaix 图、反应、结构匹配、表面、弹性 |
| [pymatgen-io](skills/pymatgen-io/) | 非 VASP I/O：CIF、XYZ、Gaussian、CP2K、QE、ABINIT、LAMMPS 等 |
| [pymatgen-io-vasp](skills/pymatgen-io-vasp/) | VASP I/O：输入生成、POTCAR 处理、输出解析 |
| [pymatgen-ext](skills/pymatgen-ext/) | 外部数据：Materials Project (MPRester)、OPTIMADE、COD |
| [pymatgen-phonon](skills/pymatgen-phonon/) | 声子能带结构、DOS、Gruneisen、红外光谱 |
| [pymatgen-symmetry](skills/pymatgen-symmetry/) | 空间群分析、标准化、k 路径生成 |
| [pymatgen-electronic-structure](skills/pymatgen-electronic-structure/) | DOS、能带结构、COHP/COOP、绑图工具 |

#### DFT 代码与模拟工具

| 技能 | 描述 | 来源 |
|------|------|------|
| [openmx](skills/openmx/) | OpenMX v3.9 DFT 计算和工作流程 | ⭐ 自定义 |
| [vasp](skills/vasp/) | VASP DFT 计算设置和分析 | 社区 |
| [python-ase](skills/python-ase/) | 原子模拟环境工作流程 | 社区 |
| [fairchem](skills/fairchem/) | Meta 的 FAIRChem 机器学习势 | 社区 |
| [materials-databases](skills/materials-databases/) | AFLOW 和 Materials Project 数据库访问 | 社区 |
| [materials-properties](skills/materials-properties/) | 使用 ASE 的第一性原理性质计算 | 社区 |

---

### 🐍 Python 科学计算

| 技能 | 描述 |
|------|------|
| [python-jax](skills/python-jax/) | JAX 高性能计算与自动微分 |
| [python-optimization](skills/python-optimization/) | 数学优化（scipy、pyomo、cvxpy、GEKKO） |
| [python-multiobjective-optimization](skills/python-multiobjective-optimization/) | Pareto 优化（pymoo、NSGA-II、MOEA/D） |
| [python-plotting](skills/python-plotting/) | Matplotlib、Seaborn、Plotly 可视化 |
| [python-regression-statistics](skills/python-regression-statistics/) | 统计建模和异常值检测 |
| [scikit-learn](skills/scikit-learn/) | scikit-learn 机器学习 |
| [sympy](skills/sympy/) | 符号数学 |
| [astropy](skills/astropy/) | 天文学和天体物理学 |
| [fluidsim](skills/fluidsim/) | 计算流体动力学 |

---

### 🤖 深度学习与机器学习

| 技能 | 描述 |
|------|------|
| [pytorch-lightning](skills/pytorch-lightning/) | PyTorch Lightning 训练框架 |
| [torch-geometric](skills/torch-geometric/) | 图神经网络（PyG） |
| [transformers](skills/transformers/) | Hugging Face Transformers |

---

### 🔄 机器学习对称性与等变性

| 技能 | 描述 |
|------|------|
| [symmetry-discovery-questionnaire](skills/symmetry-discovery-questionnaire/) | 协作识别数据对称性 |
| [symmetry-group-identifier](skills/symmetry-group-identifier/) | 将对称性映射到数学群 |
| [symmetry-validation-suite](skills/symmetry-validation-suite/) | 经验验证对称性假设 |
| [equivariant-architecture-designer](skills/equivariant-architecture-designer/) | 设计等变神经网络 |
| [model-equivariance-auditor](skills/model-equivariance-auditor/) | 验证模型等变性 |

---

### 📄 文档处理

| 技能 | 描述 |
|------|------|
| [pdf](skills/pdf/) | PDF 操作和提取 |
| [docx](skills/docx/) | Word 文档处理 |
| [pptx](skills/pptx/) | PowerPoint 操作 |
| [xlsx](skills/xlsx/) | Excel 电子表格处理 |
| [markitdown](skills/markitdown/) | 文件转换为 Markdown |
| [latex-posters](skills/latex-posters/) | LaTeX 海报创建 |

---

### 🧩 决策与分析框架

| 技能 | 描述 |
|------|------|
| [brainstorming](skills/brainstorming/) | 结构化头脑风暴技术 |
| [planning](skills/planning/) | 项目规划方法论 |
| [decision-matrix](skills/decision-matrix/) | 多准则决策分析 |
| [causal-inference-root-cause](skills/causal-inference-root-cause/) | 根因分析 |
| [decomposition-reconstruction](skills/decomposition-reconstruction/) | 系统分解 |
| [design-of-experiments](skills/design-of-experiments/) | 实验设计方法论 |
| [estimation-fermi](skills/estimation-fermi/) | 费米估算 |
| [meta-prompt-engineering](skills/meta-prompt-engineering/) | 提示词优化 |
| [postmortem](skills/postmortem/) | 事故分析 |
| [systems-thinking-leverage](skills/systems-thinking-leverage/) | 系统思维 |

---

### 🛠️ 工具

| 技能 | 描述 |
|------|------|
| [memory](skills/memory/) | 基于文件的长期记忆 |
| [skill-creator](skills/skill-creator/) | 创建新技能 |

---

## ⭐ 自定义技能

以下技能由**仓库维护者**专门为材料科学研究工作流程创建：

### 🎯 为什么要自定义技能？

**Pymatgen** 是材料科学领域最强大的 Python 库之一，但其庞大的 API 可能让人望而生畏。我没有创建一个单一的庞大技能，而是将其拆分为 **8 个专注的子技能**，覆盖不同模块：
- `pymatgen-core` → 结构操作
- `pymatgen-analysis` → 热力学和相图
- `pymatgen-io` / `pymatgen-io-vasp` → 文件 I/O
- `pymatgen-ext` → 外部数据库
- `pymatgen-phonon` → 声子分析
- `pymatgen-symmetry` → 对称性操作
- `pymatgen-electronic-structure` → DOS 和能带结构

**OpenMX** 是一个基于局域基组的强大 DFT 代码，广泛用于大规模计算。我创建了一个专门的技能（`openmx`），涵盖 OpenMX v3.9 的输入准备、计算工作流程和输出解析。

### 🏆 自定义技能列表

| 技能 | 描述 | 亮点 |
|------|------|------|
| **pymatgen-core** | Pymatgen 核心对象和结构操作 | Element、Specie、Composition、Lattice、Structure、Molecule |
| **pymatgen-analysis** | 材料分析工作流程 | 相图、Pourbaix、反应、表面、弹性 |
| **pymatgen-io** | 非 VASP 文件 I/O | CIF、XYZ、Gaussian、CP2K、QE、ABINIT、LAMMPS |
| **pymatgen-io-vasp** | VASP 专用 I/O | 输入生成、POTCAR、输出解析 |
| **pymatgen-ext** | 外部数据访问 | Materials Project、OPTIMADE、COD |
| **pymatgen-phonon** | 声子分析 | 能带结构、DOS、Gruneisen、红外光谱 |
| **pymatgen-symmetry** | 对称性分析 | 空间群、标准化、k 路径 |
| **pymatgen-electronic-structure** | 电子结构 | DOS、能带、COHP/COOP、绑图 |
| **openmx** | OpenMX DFT 工作流程 | 聚焦 v3.9、SCF、能带、DOS、NEB、SOC |

这些自定义技能包括：
- ✅ 来自真实研究经验的详细工作流程示例
- ✅ 最佳实践和常见陷阱
- ✅ 工具之间的集成模式
- ✅ 即用型示例脚本

---

## 📋 依赖要求

### 核心依赖

```bash
# 核心科学计算
pip install numpy scipy matplotlib pandas

# 材料科学
pip install ase pymatgen phonopy mp-api

# 机器学习
pip install torch scikit-learn

# 文档处理
pip install python-docx python-pptx openpyxl pypdf
```

### 环境设置

某些技能可能引用特定环境的配置。使用前请：

1. **Python 环境** - 根据需要更新 conda/virtualenv 激活命令
2. **数据路径** - 更新数据集或赝势目录的路径
3. **API 密钥** - 设置所需的 API 密钥（如 Materials Project API 密钥）

```bash
# 示例：设置 Materials Project API 密钥
export MP_API_KEY="your_api_key_here"
```

---

## 🤝 贡献指南

欢迎社区贡献！这是一个**长期维护**的仓库。

### 如何贡献

1. **Fork** 本仓库
2. 在 `skills/` 下**创建**新的技能目录
3. **添加** `SKILL.md` 技能定义（必需）
4. **包含**参考资料、脚本和示例
5. **提交** Pull Request

### 技能结构模板

```
skills/
└── your-skill-name/
    ├── SKILL.md           # 必需：主要技能定义
    ├── README.md          # 可选：详细文档
    ├── references/        # 参考资料和文档
    │   └── *.md
    ├── scripts/           # 示例脚本
    │   └── *.py
    └── examples/          # 使用示例
        └── *.md
```

### 贡献准则

- 📝 遵循现有的技能结构
- 🔍 确保技能文档完善
- ✅ 提交前测试脚本
- 🌐 移除任何个人/私有路径或凭据
- 📚 包含官方文档的引用

---

## 📜 许可证

本项目采用 **MIT 许可证** - 查看各技能目录了解额外的许可信息。

---

## 📬 联系方式

- **Issues**: [GitHub Issues](https://github.com/hongyu-yu/matsci-ai-skills/issues)
- **Discussions**: [GitHub Discussions](https://github.com/hongyu-yu/matsci-ai-skills/discussions)

---

<p align="center">
  <strong>⭐ 如果觉得有用，请给个 Star！⭐</strong>
  <br>
  <em>您的 Star 帮助更多人发现这个资源，也是对持续开发的鼓励。</em>
</p>

<p align="center">
  <em>这是一个社区维护的集合。技能按原样提供，可能需要根据您的具体用例进行调整。</em>
</p>
