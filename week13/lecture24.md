---
title: Lecture 24
layout: lecture
slideOptions:
  transition: none
  theme: white
  center: false
---

# Computing in Astronomy<!-- .element: class="centered" -->
### Matthew Turk<!-- .element: class="righted" -->
### Spring 2018<!-- .element: class="righted" -->
### Lecture 24 <!-- .element: class="righted" -->

---

## This Time

 * Putting it all together
 * Speed and ODE Solvers
 * Converting our n-body solver
 * Debugging
 * Calling external C routines

---

## Putting it all together: Final Project

Your final project will be a python package, built out of your two existing
python packages.

It will consist of your chemistry solver and your n-body integrator.  You will
augment these with new initial conditions and you will allow for either to be
run.

---

## Speed and ODE Solvers

As we saw on Tuesday, there are difficulties with speed in ODE solvers.

How can we address this?

 * Vector operations
 * Cython or C

---

## Converting Our N-Body Solver

Today, we will:

 * Convert our N-body solver to use SciPy ODE interface
 * Solve direct integration for different ODE solvers for two, three and five
   particles
 * Write a Cython-based force computation system

---

## Compiling Cython

For very simple Cython modules, we can use this command:

```
cythonize our_module.pyx
```

This produces an `our_module.c` file which is then compiled in-place.

---

## Augmenting setup.py

```
from distutils.core import setup
from Cython.Build import cythonize
import numpy as np

setup(
    name = "Force Computation",
    ext_modules = cythonize("our_module.pyx", include_path = [np.get_include()]),
)
```

---

## Advanced Cython

We can provide options that explain which C functions to call.  For instance,
at the top of a file we can specify:

```
# distutils: sources = other.c, another.c
```

We can also optimize using:

```
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
```

---

## Debugging and GDB

GDB is a debugger, but there are only a handful of commands we will likely need
to use for our purposes:

 * `run` (with arguments)
 * `c` for continue
 * `bt` for backtrace
 * `print` to show a variable
 * `list` to see the source

We will in particular be looking at how to compile such that we can get
debugging information and so that we can find where an error occurs.
Breakpoints are for more advanced tests, but we might be able to look at some
"sleep" related calls.
