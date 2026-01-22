Plan for repository setup and package split

1) Define scope and inventory
- Clarify the mission and boundaries for the all-inclusive repo.
- Inventory poeticpenny: scripts, notebooks, libraries, pipelines, utilities.
- Tag each item by purpose, dependencies, and users (you vs group).

2) Decide the target package map
- Group items into candidate packages (data IO, spectral analysis, plotting, pipelines, simulations, utilities).
- Define API boundaries and minimal dependencies for each package.
- Decide what stays top-level tools vs standalone packages.

3) Set up the new repository structure
- Create the repo named exactly as this directory.
- Add README, CONTRIBUTING, LICENSE, and a docs skeleton.
- Define a standard package layout (e.g., packages/<name>/ or src/<name>/).

4) Extract packages from poeticpenny
- Start with the highest-value, most reusable code.
- Move code into package folders, preserving history where possible.
- Replace direct script usage with package imports.

5) Stabilize and document each package
- Add minimal tests per package.
- Write short usage docs and example scripts/notebooks.
- Define internal versioning and release approach.

6) Transition and cleanup
- Mark legacy paths in poeticpenny as deprecated.
- Add a migration guide mapping old paths/functions to new packages.
- Set up basic CI (lint/test) once structure is stable.
