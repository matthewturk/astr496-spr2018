---
title: Lecture 11
layout: lecture
slideOptions:
  transition: none
  theme: white
  center: false
---

# Computing in Astronomy<!-- .element: class="centered" -->
### Matthew Turk<!-- .element: class="righted" -->
### Spring 2018<!-- .element: class="righted" -->
### Lecture 11 <!-- .element: class="righted" -->

---

## Where We Are

 * Last week
   * Data formats
   * Primitive integration of particles
 * This week
   * More advanced particle integration
   * Implementing variable integrators
 * Self-gravity
   * How does it work?  How can we implement this?
   * Particle Mesh

---

## Force Equations

$ \mathbf{\vec{F}} = m\mathbf{\vec{a}} $

$ \frac{d\mathbf{\vec{x}}}{dt} = \mathbf{\vec{v}} $

$ \frac{d\mathbf{\vec{v}}}{dt} = -\mathbf{\vec{\nabla}} \phi $

This is thus a second-order differential equation, which we can write as:

$ \frac{d^2\mathbf{\vec{r}}}{dt^2} = \frac{\mathbf{\vec{F}}}{m} $

We will explore this in two limits:

 * Massless particles in an external force
 * Interacting, mass-ed particles

---

## Force Summation

We can write the *net* force on a given particle by summing the forces acting
on it.  In the case of an ensemble of particles (denoted by the index $i$),
this can be written as:

$ \mathbf{\vec{F}}\_{i} = -\sum\_{i\neq j}\frac{G m\_i m\_j (\vec{r\_i} - \vec{r\_j})}{|\vec{r\_i} - \vec{r\_j}|^3} $

Note that the cubic power in the denominator arises from directing the force
via a (normalized) $\hat{r}$ vector.

---

## External Potential

If we are integrating our particles in a background, static potential (in the
absence of inter-particle interactions) we can eliminate the piece-wise force
summation.

$ \mathbf{\vec{F}}\_{i} = -\mathbf{\vec{\nabla}} \phi\_{\mathrm{ext}}$

---

## Exact Integration

There are a handful of situations where we can integrate this exactly.  If we
assume that our potential is constant everywhere and in a single direction
(taken to be $\hat{x}$ for simplicity) we can calculate our equations of
motion:

$ \mathbf{\vec{a}}(t) = a\_0 \hat{x} $

$ \mathbf{\vec{v}}(t) = \mathbf{\vec{v}}\_0 + a\_0 t $

$ \mathbf{\vec{x}}(t) = \mathbf{\vec{v}}\_0 t + \frac{1}{2} a\_0 t^2 + \mathbf{\vec{x}}\_{0} $

We'll use this as a comparison for examining our error-over-time.

---

## Basic (Bad) Integration

We can try out using the Euler method for integration.

This assumes that our acceleration is constant over our timestep.  If we fix
our timestep at $dt = t_0$, under this assumption we can integrate as follows:

$ \mathbf{\vec{x}}\_{t+dt} = \mathbf{\vec{x}}\_{t} + \mathbf{\vec{v}}\_{t}dt$

$ \mathbf{\vec{v}}\_{t+dt} = \mathbf{\vec{v}}\_{t} + \mathbf{\vec{a}}\_{t}dt$

---

## Error Calculation

We'll compute our residual error by summing the squares of the distances
between our exact and integrated values, normalizing by the sum of the squares.

$ E = \frac{||\mathbf{\vec{x}}\_{ex} - \mathbf{\vec{x}}\_{int} ||}{ ||\mathbf{\vec{x}}\_{ex} + \mathbf{\vec{x}}\_{int} ||} $

---

## How does this break down?

We now have both an integration scheme and an analytic solution to compare
against.  Let's examine this by building an integrator that operates under a
static potential.

 1. Build a base `Particle` class.  We can use what we built last week.
 1. Implement a base `Potential` class.  We will implement a method called
    `compute` that accepts a time and a position vector and returns a force.
 1. Construct a method on our `Particle` class that updates a state based on a
    set of piecewise forces.
 1. Construct a `System` class that collects particles and potentials, tracks
    time, and updates the system when necessary.
 1. Evaluate the increase in error over time as a function of timescale.

---

## Not Great

Seems like things are a bit strange with this.  We can make a simple
modification to our Euler integration to transform it to a semi-implicit
calculation; we replace the _current_ velocity with the _new_ velocity when
updating the position.

$ \mathbf{\vec{x}}\_{t+dt} = \mathbf{\vec{x}}\_{t} + \mathbf{\vec{v}}\_{t+dt}dt$

$ \mathbf{\vec{v}}\_{t+dt} = \mathbf{\vec{v}}\_{t} + \mathbf{\vec{a}}\_{t}dt$

Let's now modify our integrator to account for this, and examine our error over
time.

---

## Leapfrog

The leapfrog integration scheme is a second-order accurate method that uses
"half-steps" to mitigate the error introduced by the assumption of constant
acceleration.

$ \mathbf{\vec{x}}\_{t+dt/2} = \mathbf{\vec{x}}\_{t} + \frac{1}{2}dt\mathbf{\vec{v}}\_{t} $

$ \mathbf{\vec{v}}\_{t+dt} = \mathbf{\vec{v}}\_{t} + dt\mathbf{\vec{a}}(\mathbf{\vec{x}}\_{t+dt/2})$

$ \mathbf{\vec{x}}\_{t+dt} = \mathbf{\vec{x}}\_{t+dt/2} + \frac{1}{2}dt\mathbf{\vec{v}}\_{t+dt}$

Let's now modify our integrator to account for this, and examine our error over
time.

---

## Particle Ensembles

Gravity is a $\frac{1}{r^2}$ function.  As two particles become closer
together, this becomes a singularity and acceleration increases without bound.

(Why doesn't this happen "in real life"?)

How can we mitigate this?

---

## Softening Length

We can modify this using a softening length ($\epsilon$) to ensure that
particles never get "too close."

$ \mathbf{\vec{F}}\_{i} = -\sum\_{i\neq j}\frac{G m\_i m\_j (\vec{r\_i} - \vec{r\_j})}{(|\vec{r\_i} - \vec{r\_j}|^2 + \epsilon^2)^{3/2}} $

---

## Particle Ensemble Integration

Now, update your solver to allow for computation of piecewise forces between
particles.

 1. Add in a piecewise `Particle`-to-`Particle` method for computing a force.
 1. Make the softening length a parameter.
 1. Compute the net forces and update inside the `System` class.

Why is this current method non-ideal?

---

## Next Class

In the next class, we will discuss:

 * Tree methods
 * Initial conditions and data formats for them
 * Putting this together with more visualization

---

## Next Assignment

Your next assignment is to build a particle integrator.  You may do this
digitally (via source code) or manually (via photometers).

 * Implement each of these methods for integration:
   * Direct Euler
   * Semi-implicit Euler
   * Leapfrog
   * Tree (this one is the hardest - don't work on it yet)
 * Implement a few simple background potentials:
   * Constant and zero background
   * Springy-background
 * Demonstrate how particles behave
   * In absence of pairwise interactions
   * As an ensemble that includes pairwise interactions

(But wait, there's more!)

---

## Next Assignment

You must follow the guidelines we have gone over for reproducible research.

 * Post your code in a repository on GitHub.  How to do this will be made
   explicit shortly.
 * You should have a `dodo.py` file for `pydoit` and this should execute a set
   of test problems.
 * Visualizations of error, trajectories, and so forth should be output after
   each execution.
 * Initial conditions should be read in from a file or set of files.
