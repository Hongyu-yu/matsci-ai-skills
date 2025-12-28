# OpenMX example catalog (from `openmx_example/`)

Use these as starting points: copy a `.dat`, edit `System.Name`, fix `DATA.PATH`, then run `openmx`.

## Basic SCF / band / DOS

- Band path + `.scfout`: `openmx_example/Fe_Bulk_jx.dat`, `openmx_example/Co_Bulk_jx.dat`, `openmx_example/Ni_Bulk_jx.dat`
- Dense k-grid: `openmx_example/Si2_k50x50x50.dat`

## Geometry optimization (MD.Type = BFGS/DIIS/RF/EF/…)

- Many small-to-medium systems: `openmx_example/geoopt_example/`

## NEB (reaction path)

- `openmx_example/C2H4_NEB.dat`
- `openmx_example/Si8_NEB.dat`

## ESM / work function / surfaces

- Work function sweeps: `openmx_example/*_WorkFunc_*.dat` (e.g., `Al111_WorkFunc_0E.dat` … `Al111_WorkFunc_7E.dat`)
- ESM interface example: `openmx_example/Al-Si111_ESM.dat`, `openmx_example/Al-Si111_ESM-on2_m0.01.dat`
- Au(111) surface workflows (band/dos/mo): `openmx_example/Au111Surface_*.dat`

## SOC / noncollinear / +U / topological invariants

- SOC + Z2: `openmx_example/Bi2Se3-Z2.dat`, `openmx_example/Bi111-Z2.dat` (variants: `*_trivial-Z2.dat`, `*_weak-Z2.dat`)
- Noncollinear + SOC + U: `openmx_example/FeO_NC.dat`, `openmx_example/CoO_NC.dat`, `openmx_example/MnO_NC.dat`
- Additional SOC/noncollinear inputs: `openmx_example/wf_example/`, `openmx_example/force_example/`

## Band unfolding

- Unfolding configs: `openmx_example/unfolding_example/`

## Wannier90 / MLWF interface

- `openmx_example/Si-Wannier90.dat`
- `openmx_example/SrVO3-Wannier90.dat`

## NEGF / transport

- `openmx_example/negf_example/` (also `openmx_example/NEGF-*.dat`)

## Large-scale / performance

- Large systems: `openmx_example/large_example/`, `openmx_example/large2_example/`, `openmx_example/large3_example/`

## Finding an example by feature

```bash
python scripts/find_examples.py --pattern "MD\\.Type\\s+NEB|ESM\\.switch|Unfolding\\.Electronic\\.Band|HS\\.fileout\\s+on"
```

