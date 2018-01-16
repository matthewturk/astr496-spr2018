---
title: Lecture 1
layout: lecture
---
# Computing in Astronomy
## Matthew Turk
## Spring 2018

---
# Basics

11:00AM-12:30PM Tuesdays and Thursdays

Matthew Turk - mjturk@illinois.edu
Office Hours: Appointment

TA Ko-Yun (Monica) Huang - khuang33@illinois.edu

[matthewturk.github.io/astr496-spr2018](https://matthewturk.github.io/astr496-spr2018)

# Syllabus

Four units:

 1. Basics of Computation
 2. Astro Computation
 3. Simulations
 4. Data

---

# Unit 1: Basics

* Week 1 (Jan 16): Conversational Computation
* Week 2 (Jan 23): Basics of Python for Science
* Week 3 (Jan 30): TBA
* Week 4 (Feb 6): Reproducible Research

We will be covering the basics of "conversational computation," and how to
apply a computational toolkit.

---

# Unit 2: Astro Computation

* Week 5 (Feb 13): Images and Observations
* Week 6 (Feb 20): ODE solvers
* Week 7 (Feb 27): Memory, Instructions, and Speed
* Week 8 (Mar 6): Introduction to Simulations

During this unit, we will be exploring some items specific to astronomical
calculations, including astropy, applying ODE solvers, and how issues related
to memory and CPU instruction can impact performance.

---

# Unit 3: Simulations

* Week 9 (Mar 13): Simulations: Particles
* Week 10 (Mar 20): **No Class** (Spring Break)
* Week 11 (Mar 27): Simulations: Grids
* Week 12 (Apr 3): Visualization

During this unit, we will be exploring and utilizing simulation codes such as
Gadget and Enzo.

---

# Unit 4: Data

* Week 13 (Apr 10): Data Storage
* Week 14 (Apr 17): Databases and SQL
* Week 15 (Apr 24): Accelerators
* Week 16 (May 1): Future Directions

We will 

---

# Overview - Themes
1. What are the components of an effective visualization of quantitative data?
1. What tools and ecosystems are available for visualizing data?
1. What systems can be put in place to generate visualizations rapidly and with high-fidelity representation?

---
# Overview - Goals

* Students will be able to communicate information and data through visual representation
* Students will be able to examine a visualization and understand how it can be improved upon
* Students will have facility with the commonplace tools used for visualization, and a deeper understanding of where those tools have shortcomings

---
# Initial steps with Viz

The first thing we're going to do is set up our visualization environment.

We'll import a few things and go from there.


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

Now we have a few things imported, so let's check out where to go from here.


```python
pd.read_csv("hello.csv")
```
