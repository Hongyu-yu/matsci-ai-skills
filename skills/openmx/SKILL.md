---
name: openmx
description: "OpenMX (openmx) workflows with emphasis on OpenMX v3.9: write and validate input .dat files (System.Name, Atoms.SpeciesAndCoordinates, scf.Kgrid, Band.kpath), run SCF/geometry optimization/band/DOS/NEB/ESM/SOC(+U)/unfolding/Wannier90/NEGF examples, and interpret outputs (.out/.scfout/restart). Trigger this skill whenever the user mentions OpenMX/openmx."
---

# OpenMX (v3.9-focused)

Use this skill when you need to run **OpenMX** calculations or prepare/inspect OpenMX inputs/outputs. The examples and notes here are aligned with the OpenMX v3.9 manual (`openmx3.9.pdf`) and this repo’s `openmx_example/` library.

## Example Library (This Repo)

This repository includes many ready-to-run OpenMX inputs under `openmx_example/`. Prefer starting from the closest example, then editing:

- `System.Name` (unique per run)
- `DATA.PATH` (points to `DFT_DATA19` / basis+pseudopotential directory on your system)
- `Atoms.*` and `<Definition.of.Atomic.Species ...>` (structure + basis/pseudo choices)

Example index: `references/examples.md` (NEB/ESM/work-function/NEGF/unfolding/SOC+U/etc.).

To search examples by feature:

```bash
python scripts/find_examples.py --pattern "MD\\.Type\\s+NEB"
```

If you run it from outside this repo, pass `--root /path/to/openmx_example` or set `OPENMX_EXAMPLE_DIR`.

## Quick Start (Run a Calculation)

1. Create an input file `work/<name>.dat` (see template below).
2. Run OpenMX (serial or MPI):
   - Serial: `openmx work/<name>.dat > work/<name>.std`
   - MPI: `mpirun -np <N> openmx work/<name>.dat > work/<name>.std`
3. Check results in `work/<System.Name>.out`.

If you need binary matrices for post-processing, set `HS.fileout=ON` to write `work/<System.Name>.scfout`.

## Input File Template (Minimal)

OpenMX input is keyword-based; order is flexible. A minimal, common structure:

```text
System.CurrrentDirectory   ./      # note the spelling in the manual
System.Name                mycalc

Species.Number  2
<Definition.of.Atomic.Species
H  H5.0-s1   H_PBE19
C  C5.0-s1p1 C_PBE19
Definition.of.Atomic.Species>

Atoms.Number  5
Atoms.SpeciesAndCoordinates.Unit  Ang
<Atoms.SpeciesAndCoordinates
1 C   0.000  0.000  0.000  2.0  0.5 0.5 0.5
2 H  -0.890 -0.629  0.000  0.5  0.5 0.5 0.5
Atoms.SpeciesAndCoordinates>

Atoms.UnitVectors.Unit  Ang
<Atoms.UnitVectors
10.0 0.0  0.0
0.0  10.0 0.0
0.0  0.0  10.0
Atoms.UnitVectors>

scf.XcType            GGA-PBE
scf.SpinPolarization  off        # off|on|nc
scf.Kgrid             1 1 1
scf.maxIter           100
scf.criterion         1.0e-10

HS.fileout            ON         # writes System.Name.scfout
```

## Outputs to Expect

Common outputs (controlled by `level.of.fileout` in the input):
- `work/<System.Name>.out`: main log (SCF history, energies, charges, geometry optimization history).
- `work/<System.Name> rst/`: restart directory.
- `work/<System.Name>.scfout`: binary Hamiltonian/overlap/density matrices when `HS.fileout=ON`.

## Reference

- Keyword cheat sheet: `references/keywords.md`
- Example catalog (this repo): `references/examples.md`

