---
layout: default
title: Assignment 2 - Particle Code
due: 2018-03-29
---

# Assignment 2 - Particle Code

**Due: 2018-03-29**

This assigment is to build an N-body code that functions in 3D.

Your N-body code should be built in Python, and will need to meet these
requirements:

### Integrators

You need to implement integrators that can be toggled by a parameter (specified
at runtime) in each of these methods:

   * Direct Euler
   * Semi-implicit Euler
   * Leapfrog

### Force Calculation

You need to implement force calculation via both:

   * Tree (with variable parameters)
   * Direct calculation ($N^2$)
   * No inter-particle force calculation (i.e., strictly background)

### Background Potentials

You will need to implement background potentials.  

  * Constant and zero background
  * Springy-background

### Initial Conditions

Your initial conditions files will be in HDF5, and will follow this data
format:

```
  /particle_positions     [Nx3] float64
  /particle_velocities    [Nx3] float64
  /particle_masses        [N]   float64
```

### Demonstration

Your work must include a notebook that demonstrates the particle evolution over
time for each of the initial conditions settings that are provided.

### Reproducible Research

Following the guidelines outlined in week 4's lectures, your work must be
structured in a manner that enables people to reproduce it and examine it.

### Write-Up

Your code must be documented; this does not mean extensive comments, but it
does mean that each routine must have a brief outline of what it is doing.  You
must also provide a notebook or other report that walks through how to utilize
the code and what to expect.

You must evaluate the following items:

 * How does the speed of execution change as you increase the number of
   particles for each of the integration methods and force calculation methods?
 * What do the different integration and force calculation methods produce in
   terms of accuracy and end points for each of the types of initial
   conditions?
 * How can parameters for the tree change results?
