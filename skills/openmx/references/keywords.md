# OpenMX keyword quick reference (v3.9-focused)

## Core system + structure

- `System.CurrrentDirectory`: working directory (manual uses this spelling).
- `System.Name`: base name for outputs (`System.Name.out`, `System.Name.scfout`, `System.Name rst/`).
- `DATA.PATH`: location of basis/pseudopotential data (often `../DFT_DATA19` in examples).
- `Species.Number`: number of species.
- `<Definition.of.Atomic.Species ... Definition.of.Atomic.Species>`: basis + pseudopotential mapping per species.
- `Atoms.Number`: number of atoms.
- `Atoms.SpeciesAndCoordinates.Unit`: coordinate unit (e.g., `Ang`).
- `<Atoms.SpeciesAndCoordinates ... Atoms.SpeciesAndCoordinates>`: atom list.
- `Atoms.UnitVectors.Unit`: unit cell vector unit.
- `<Atoms.UnitVectors ... Atoms.UnitVectors>`: 3×3 cell vectors.

## SCF / electronic settings

- `scf.XcType`: `LDA|LSDA-CA|LSDA-PW|GGA-PBE`.
- `scf.SpinPolarization`: `off|on|nc` (noncollinear is `nc`).
- `scf.SpinOrbit.Coupling`: enable SOC (commonly used with `nc`).
- `scf.Kgrid`: Monkhorst-Pack grid `n1 n2 n3`.
- `scf.maxIter`: SCF max iterations.
- `scf.criterion`: SCF convergence threshold (Hartree).

## Band + DOS + matrix outputs

- `scf.EigenvalueSolver`: `DC|Cluster|Band`.
- `Band.Nkpath` and `<Band.kpath ... Band.kpath>`: k-path definition.
- `Dos.fileout`: `ON` to compute DOS/PDOS.
- `HS.fileout`: `ON` to write `System.Name.scfout` (Hamiltonian/overlap/density matrices).

Examples in this repo:
- Band + `HS.fileout=ON`: `openmx_example/Fe_Bulk_jx.dat`, `openmx_example/Co_Bulk_jx.dat`, `openmx_example/Ni_Bulk_jx.dat`
- SOC + Z2: `openmx_example/Bi2Se3-Z2.dat`, `openmx_example/Bi111-Z2.dat`
- Unfolding: `openmx_example/unfolding_example/`

