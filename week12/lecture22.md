---
title: Lecture 22
layout: lecture
slideOptions:
  transition: none
  theme: white
  center: false
---

# Computing in Astronomy<!-- .element: class="centered" -->
### Matthew Turk<!-- .element: class="righted" -->
### Spring 2018<!-- .element: class="righted" -->
### Lecture 22 <!-- .element: class="righted" -->

---

## Last Time

 * Chemistry
 * SymPy
 * Basic ODE solving

---

## This Time

 * More ODE Solving
 * Temperatures
 * Interpolation

---

## Upcoming Talk!

Dr. Kathryn Clancy, from the Department of Anthropology at the U of I will be
speaking at the Astronomy Department colloquium next Tuesday (April 17). She
will give her talk at 3:45 in room 134, with refreshments served at 3:30 in
room 222.

Title: "Gender harassment in science: is it just me?"

---

## Primordial Chemistry Review

In the early universe, we have these species:

 * Hydrogen: ${\rm H}$, ${\rm H}^{+}$, ${\rm H}^{-}$
 * Helium: ${\rm He}$, ${\rm He}^{+}$, ${\rm He}^{++}$
 * Electrons: ${\rm e}^{-}$
 * Molecular Hydrogen: ${\rm H}\_{2}$, ${\rm H}\_{2}^{+}$

We have a number of different reactions that we have identified.

Our first step will be a 6-species model, including hydrogen and helium but not
${\rm H}^{-}$ or molecular hydrogen.

---

## Primordial Chemistry Reactions

|||
|---|---|---|
| ${\rm H + e^{-}}$ | $\rightarrow$ | $\rm{H^{+} + e^{-} + e^{-}}$|
| ${\rm H^{+} + e^{-}}$ | $\rightarrow$ | $\rm{H + \gamma} $|
| ${\rm He + e^{-}}$ | $\rightarrow$ | ${\rm He^{+} + e^{-} + e^{-}}$|
| ${\rm He^{+} + e^{-}}$ | $\rightarrow$ | ${\rm He + \gamma}$|
| ${\rm He^{+} + e^{-}}$ | $\rightarrow$ | ${\rm He^{++} + e^{-} + e^{-}}$|
| ${\rm He^{++} + e^{-}}$ | $\rightarrow$ | ${\rm He^{+} + \gamma}$|
| ${\rm H + H}$ | $\rightarrow$ | ${\rm H^{+} + e^{-} + H}$|
| ${\rm H + He}$ | $\rightarrow$ | ${\rm H^{+} + e^{-} + He}$|
| ${\rm H + \gamma}$ | $\rightarrow$ | ${\rm H^{+} + e^{-}}$|
| ${\rm He + \gamma}$ | $\rightarrow$ | ${\rm He^{+} + e^{-}}$|
| ${\rm He^{+} + \gamma}$ | $\rightarrow$ | ${\rm He^{++} + e^{-}}$|

---

## Solving these in SymPy

Our first task today is to build these reactions into SymPy.  How are we going
to do this?  How do we assemble a reaction network?

---

## Our Derivation From Last Time

Last time, we determined that we could write the change in a given species over
time as a summation of the reactions that govern it:

$ \frac{\partial S\_i }{\partial t} = \sum\_{j}\sum\_{l} k\_{jl}S\_{j}S\_{l} + \sum\_{j}I\_{j}S\_{j}$

Here, $S\_i$ is the __number density__ of a given species, and we see negative
$k$ values when the reaction is "destructive" and positive $k$ when it is
"constructive$.

Let's see if we can organize this somehow with SymPy.

---

## Reaction Rates

We will need to find reaction rates for all of these species.  We will use the
Grackle method paper to find the different reaction rates and then utilize them
in our code.

https://arxiv.org/abs/1610.09591

---

## Temperature

For our current system, we have a reasonably simple equation of state for our
gas.  Given some specific internal energy $e$ we can write our equation for
temperature as:

$e = \frac{kT}{(\gamma - 1) \mu m\_{\rm H}} $

This is true under the assumption that $\gamma$ is identical for all of the
species.  If that is not true, we need to utilize a partial pressure approach
to compute the temperature.

---

## Density (1)

What do we know about density in our calculations?  Is it fixed?  Is it
changing?

Commonly, in a simulation it will be fixed over the course of a timestep.  But
we may choose to evolve it independently -- for instance, as a free-fall
problem, where we see how the gas behaves if we compress it over a "Free fall"
timescale.

$\frac{d\rho}{dt} = \frac{\rho}{t\_{\rm col}}$

---

## Density (2)

We define the collapse timescale ($t\_{\rm col}$) as 

$t\_{\rm col} = \frac{t\_{\rm ff}}{\sqrt{1 - f}}$

$f$ here is a thermal pressure value, and $t\_{\rm ff}$ is the free-fall
timescale itself, defined as:

$t\_{\rm ff} = \sqrt{\frac{3\pi}{32 G \rho}}$

---

## Constraints

How do we apply constraints?  For our purposes, we will allow the electron
fraction to be computed as a constraint following the update step.  Density
conservation will also be applied.

---

## Interpolation Tables

Computing reaction rates can be very computationall intensive.  Here, for
example, is the source for computing the rates $k\_1$ and $k\_2$ in Grackle:

```
      k1 = exp(-32.71396786375 
     &     + 13.53655609057*log_T_eV
     &     - 5.739328757388*log_T_eV**2 
     &     + 1.563154982022*log_T_eV**3
     &     - 0.2877056004391*log_T_eV**4
     &     + 0.03482559773736999*log_T_eV**5
     &     - 0.00263197617559*log_T_eV**6
     &     + 0.0001119543953861*log_T_eV**7
     &     - 2.039149852002e-6*log_T_eV**8)
         IF (T .lt. 1.0d9) then
            k2 = 4.881357e-6*T**(-1.5) 
     &           * (1.+1.14813e2
     &           * T**(-0.407))**(-2.242)
         ELSE
            k2 = tiny
         ENDIF
```

---

## Solving ODEs in SciPy

We will build a *callable* ODE integrator that constructs our equations,
updates our state vector, and then integrates.

The `odeint` function accepts an initial state vector, an update callable,
supplemental arguments, and a series of times at which to compute the values.

We will examine:

 * Error control
 * Timestep control
 * Interpolation error
