# C964 — Computer Science Capstone (course site)

**Live site:** https://ashejim.github.io/C964/intro.html

A Jupyter Book course site I author and maintain for WGU's Computer Science capstone (C964). It walks students task-by-task through their final project: topic approval (Task 1), building a machine-learning application (Task 2 Part C) with complete worked examples for supervised classification and regression, and the accompanying documentation and presentation (Tasks 2 A, B, and D).

Created and maintained by course faculty as a supplementary resource — not an official WGU page. The stars and forks here are largely capstone students using the material.

## Building locally

This book targets Jupyter Book 1.x (pre-MyST): `pip install "jupyter-book<2"`, then `pip install -r requirements.txt`, then `jb build .` from the repo root.

If the build errors on missing kernels: VS Code writes machine-specific kernel names into notebook metadata. Run `python update_kernels.py` to normalize them.
