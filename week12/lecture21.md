---
title: Lecture 20
layout: lecture
slideOptions:
  transition: none
  theme: white
  center: false
---

# Computing in Astronomy<!-- .element: class="centered" -->
### Matthew Turk<!-- .element: class="righted" -->
### Spring 2018<!-- .element: class="righted" -->
### Lecture 21 <!-- .element: class="righted" -->

---

## Last Time

 * Programming Philosophy
 * Testing

---

## This Time

 * Chemistry
 * Ordinary Differential Equations

---

## (Primordial) Chemistry

This one we're going to do on the board.  But, the basics:

 * We have several species in the universe.
 * We need to see how they change as a function of temperature and gas
   composition

---

## SymPy

Today, we will explore SymPy for symbolic computing.

---

## ODE Solving in SciPy

We will utilize the `scipy.integrate.odeint`.  This takes a function (callable)
that returns a derivative at a given time.

---

## Next Assignment

Your next assignment is to develop an ODE solver that follows the evolution of
the nine species of H, H+, H-, He, He+, He++, H2, H2+ and e-.

 * Look up the chemical kinetic rate equations
 * Develop a right-hand side
 * Utilize the SciPy integrators to evolve a network of reactions drawn from
   the Grackle methods paper.

You will have until May 1.
