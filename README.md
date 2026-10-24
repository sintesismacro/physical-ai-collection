<img src="https://raw.githubusercontent.com/sintesismacro/.github/main/profile/assets/banner.png" alt="SINTESIS — Intelligence becomes abundant; verified judgement becomes scarce." width="100%">

# The Physical AI Collection

**Open-source projects across the physical layers of AI — collected by judgement, not by fame.**

Intelligence is becoming physical: chips, memory, data centres, power, grid, cooling, power
electronics, robots and sensors. This collection keeps the open-source projects that build that
body, one layer at a time. Every entry is dated and was opened and checked by hand. Projects run by
communities, universities, foundations and public research institutes are read through the two
voices of the [Forward Evidence Ledger](https://github.com/sintesismacro/ledger):

- **Becoming** — the project extends what the physical body of intelligence can do.
- **Returning** — the project removes a necessity: efficiency, measurement of waste, or a scarce
  input made common.

Explore it on the map: [**the Observatory**](https://sintesismacro.github.io/observatory/#atlas),
where each Atlas layer shows its projects next to its forecasts.

## The collection

<!-- collection:start -->
**31 projects** across ten layers · 24 read (14 Becoming, 10 Returning) · 7 company-owned, facts only · last verified 23 October 2026

### Accelerated compute

| Project | What it does | Licence | Reading |
| --- | --- | --- | --- |
| [OpenROAD](https://github.com/The-OpenROAD-Project/OpenROAD) | Automates digital chip layout from register-transfer-level design to GDSII. | `BSD-3-Clause` | **Returning** — Removes the need for a licensed design flow to take a chip to layout. |
| [Chipyard](https://github.com/ucb-bar/chipyard) | Framework for designing, simulating and implementing custom RISC-V systems-on-chip. | `BSD-3-Clause` | **Becoming** — Lets small teams build custom accelerators, extending who can make silicon. |
| [Apache TVM](https://github.com/apache/tvm) | Machine-learning compiler that deploys models across many hardware targets. | `Apache-2.0` | **Returning** — Compiles once for many targets, reducing dependence on any single accelerator stack. |
| [Triton](https://github.com/triton-lang/triton) | Language and compiler for writing efficient custom deep-learning kernels. | `MIT` | Facts only (company-owned) |

### High-bandwidth memory

| Project | What it does | Licence | Reading |
| --- | --- | --- | --- |
| [gem5](https://github.com/gem5/gem5) | Modular simulator of processors, memory systems and full computer systems. | `BSD-3-Clause` | **Becoming** — Lets new memory and processor designs be explored before any silicon exists. |
| [Ramulator 2](https://github.com/CMU-SAFARI/ramulator2) | Cycle-accurate DRAM simulator for memory controllers and new DRAM standards. | `MIT` | **Becoming** — Tests the memory layer that most often limits AI systems, before it is built. |

### Advanced packaging and foundry

| Project | What it does | Licence | Reading |
| --- | --- | --- | --- |
| [SkyWater SKY130 Open Source PDK](https://github.com/google/skywater-pdk) | Open process design kit for a 130 nm process — design rules, device models, libraries. | `Apache-2.0` | Facts only (company-owned) |
| [IHP Open PDK](https://github.com/IHP-GmbH/IHP-Open-PDK) | Open process design kit for IHP's 130 nm SiGe BiCMOS technology (labelled preview). | `Apache-2.0` | **Returning** — Opens a foundry process to anyone, removing the scarcity of access for research designs. |

### Data centres

| Project | What it does | Licence | Reading |
| --- | --- | --- | --- |
| [CodeCarbon](https://github.com/mlco2/codecarbon) | Estimates the emissions of computing from measured CPU, GPU and RAM power and grid intensity. | `MIT` | **Returning** — Makes the energy cost of each workload visible, the first step to removing it. |
| [Kepler](https://github.com/sustainable-computing-io/kepler) | Measures energy use of Kubernetes containers, pods and nodes. | `Apache-2.0` | **Returning** — Meters energy per container, so waste in shared clusters can be found and cut. |
| [Scaphandre](https://github.com/hubblo-org/scaphandre) | Agent measuring power use of hosts, virtual machines and Kubernetes workloads. | `Apache-2.0` | **Returning** — Turns power into a monitored metric, so idle capacity stops hiding. |
| [Zeus](https://github.com/ml-energy/zeus) | Measures and optimises the energy consumption of deep-learning workloads. | `Apache-2.0` | **Returning** — Cuts the energy of training and inference without new hardware. |

### Power generation

| Project | What it does | Licence | Reading |
| --- | --- | --- | --- |
| [PyPSA](https://github.com/PyPSA/PyPSA) | Python framework for simulating and optimising power and energy systems. | `MIT` | **Becoming** — Plans the generation and storage that new load requires. |
| [pvlib python](https://github.com/pvlib/pvlib-python) | Functions and classes for simulating the performance of photovoltaic systems. | `BSD-3-Clause` | **Becoming** — Models the output of new solar generation for planning and operation. |

### Transmission and grid

| Project | What it does | Licence | Reading |
| --- | --- | --- | --- |
| [pandapower](https://github.com/e2nIEE/pandapower) | Automated power-flow and optimisation studies of electric grids. | `BSD-3-Clause` | **Becoming** — Tests whether a grid can absorb new load before it is connected. |
| [PowerModels.jl](https://github.com/lanl-ansi/PowerModels.jl) | Julia package for steady-state power-network optimisation across formulations. | `BSD-3-Clause` | **Becoming** — Gives planners comparable models of how far a network can be pushed. |
| [Grid2Op](https://github.com/Grid2op/grid2op) | Testbed for reinforcement-learning agents that operate power grids. | `MPL-2.0` | **Becoming** — Intelligence learning to run its own body — agents operating the grid. |
| [VeraGrid (formerly GridCal)](https://github.com/SanPen/VeraGrid) | Power-system planning and simulation, as a library or desktop application. | `MPL-2.0` | **Becoming** — Open planning software for the grid build-out. |

### Cooling

| Project | What it does | Licence | Reading |
| --- | --- | --- | --- |
| [OpenFOAM](https://github.com/OpenFOAM/OpenFOAM-dev) | Computational fluid dynamics toolbox, including conjugate heat transfer solvers. | `GPL-3.0` | **Becoming** — Designs the airflow and liquid loops that let compute run denser. |
| [Modelica Buildings Library](https://github.com/lbl-srg/modelica-buildings) | Models of HVAC, district energy and data-centre cooling for design and control. | `BSD-3-Clause` | **Returning** — Tunes cooling controls so the same work needs less energy. |
| [3D-ICE](https://github.com/esl-epfl/3d-ice) | Thermal simulation of 3D-stacked chips with liquid microchannel cooling. | `GPL-3.0-or-later` | **Becoming** — Cools inside the chip stack — a condition for denser compute. |

### Power electronics

| Project | What it does | Licence | Reading |
| --- | --- | --- | --- |
| [ngspice](https://ngspice.sourceforge.io/) | Mixed-signal circuit simulator with power-transistor models including self-heating. | `BSD-3-Clause` | **Becoming** — Simulates the converters that move power into machines. |
| [gym-electric-motor](https://github.com/upb-lea/gym-electric-motor) | Simulated electric motors and converters for classical and reinforcement-learning control. | `MIT` | **Becoming** — Trains the control of drives — the muscles of embodiment. |
| [FEM Magnetics Toolbox](https://github.com/upb-lea/FEM_Magnetics_Toolbox) | Sets up finite-element simulations of magnetic components for power electronics. | `GPL-3.0` | **Returning** — Replaces prototype iterations with simulation. |

### Robotics and actuators

| Project | What it does | Licence | Reading |
| --- | --- | --- | --- |
| [MuJoCo](https://github.com/google-deepmind/mujoco) | Physics engine for multi-joint dynamics with contact, used in robotics research. | `Apache-2.0` | Facts only (company-owned) |
| [Isaac Lab](https://github.com/isaac-sim/IsaacLab) | Unified robot-learning framework built on the Isaac Sim simulator. | `BSD-3-Clause` | Facts only (company-owned) |
| [LeRobot](https://github.com/huggingface/lerobot) | PyTorch models, datasets and tools for real-world robot learning. | `Apache-2.0` | Facts only (company-owned) |
| [Open X-Embodiment](https://github.com/google-deepmind/open_x_embodiment) (dataset) | Open robot-learning datasets converted into one unified episode format. | `Apache-2.0 (code); CC-BY-4.0 (other materials)` | Facts only (company-owned) |

### Sensors and machine vision

| Project | What it does | Licence | Reading |
| --- | --- | --- | --- |
| [OpenCV](https://github.com/opencv/opencv) | Library of image-processing and computer-vision algorithms. | `Apache-2.0` | **Returning** — Made machine vision a common library; the algorithm is no longer the scarce input. |
| [Open3D](https://github.com/isl-org/Open3D) | C++ and Python library for processing 3D data. | `MIT` | Facts only (company-owned) |
| [Point Cloud Library](https://github.com/PointCloudLibrary/pcl) | C++ algorithms for processing 3D point clouds. | `BSD-3-Clause` | **Becoming** — Gives machines depth perception from lidar and depth sensors. |
<!-- collection:end -->

## Rules

1. **Verified, dated, live.** Every project was opened on the date in `verified`; archived
   projects, projects without an open-source licence and projects with no activity for two years
   are left out. The `basis` field says what was checked.
2. **Projects, not companies.** Projects owned by a company, listed or private, appear with facts
   only: what they do and their licence. They carry no reading, and the collection never names a
   ticker or comments on a company.
3. **One reading, one reason.** Every other project carries one reading and a one-line reason,
   written as a judgement of 24 October 2026, open to challenge.
4. **Checked by CI.** [`tools/build.py`](tools/build.py) enforces these rules and renders the
   tables above from [`collection.yaml`](collection.yaml).

## Propose a project

Open an issue with the **Propose a project** form. A proposal needs the repository, its layer,
its licence and one sentence on what it does. Readings are added by the editor after review.

## Licence and notice

The collection (`collection.yaml` and this README) is © 2026 SINTESIS UG (haftungsbeschränkt) and
licensed under [CC BY 4.0](LICENSE). Each listed project keeps its own licence, shown in the
table. Nothing here is investment advice or a view on any company or security.

[sintesismacro.com](https://www.sintesismacro.com) · <office@sintesismacro.com>

<sub>Prepared 24 October 2026 · Revised 24 October 2026</sub>
