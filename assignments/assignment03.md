---
layout: default
title: Assignment 3 - Chemistry Solver
due: 2018-03-29
---

# Assignment 3 - Chemistry Solver

**Due: 2018-05-04**

Your next assignment is to develop an ODE solver that follows the evolution of
the nine species of H, H+, H-, He, He+, He++, H2, H2+ and e-.

You can use the [Grackle](https://arxiv.org/abs/1610.09591) method paper for
this assignment.

 * Look up the chemical kinetic rate equations
 * Develop a right-hand side calculation.  You may do this by hand, or using
   SymPy as we did in class.
 * Calculate the rate coefficients as a function of temperature; you can assume
   an ideal gas law for the temperature.
 * Utilize the SciPy integrators to evolve a network of reactions drawn from
   the Grackle methods paper.

You will have until May 4.  (May the Fourth be with you.)

You should produce the following items:

 * Python code that runs from the command line that accepts
   * Initial H ionization fraction
   * Initial He ionization fraction
   * Molecular hydrogen fraction
   * Density
   * Time to evolve to
   * Integrator to use inside `scipy.integrate.ode`
 * An integrator that updates based on some safety factor until the time is
   reached
 * A set of visualizations that show overall change in the various fractions.
 * A writeup

### Write-Up

Your code must be documented; this does not mean extensive comments, but it
does mean that each routine must have a brief outline of what it is doing.  You
must also provide a notebook or other report that walks through how to utilize
the code and what to expect.

You must evaluate the following items:

 * When is it slower and faster?  When it is near equilibrium or far?
 * Do you see any particularly interesting regions in phase space?
 * What was easy or hard?
