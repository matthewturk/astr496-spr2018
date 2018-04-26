---
title: Lecture 26
layout: lecture
slideOptions:
  transition: none
  theme: white
  center: false
---

# Computing in Astronomy<!-- .element: class="centered" -->
### Matthew Turk<!-- .element: class="righted" -->
### Spring 2018<!-- .element: class="righted" -->
### Lecture 26 <!-- .element: class="righted" -->

---

## Last Time

 * Calling C functions in Cython
 * Halos

---

## This Time

 * Radio data
 * (Brief) Radiation Transport
 * Physically-Motivated Visualization

---

## Radio Data

(Monica is going to do this part.)

---

## Radiation Transport Equation

The simplest form of the radiation transport equation, in the presence of
emission and absorption but the absence of scattering, can be written as such:

$ \frac{dI\_{\nu}}{ds} = j\_{\nu} - \alpha\_{\nu}ds $

The change in the intensity at a wavelength is only related to the local
emission ($j\_{\nu}$) and absorption ($\alpha\_{\nu}$) and the path length it
traverses.

---

## Radiation Transport: Scattering

When a photon is "absorbed," it may be re-radiated out immediately.  This
re-radiation will be proportional to the absorption coefficient.

This will either be isotropic, or a function of the angle of incidence.  To
account for this, we redefine $j\_{\nu}$ as follows:

$j\_{\nu} = \alpha\_{\nu}\int\frac{d\Omega}{4\pi}I\_{\nu}$

---

## Radiation Transport: Simulations

Let us consider two cases: grids and particles.

If we represent each as a set of gas parcels, how would we compute radiation
transport?

---

## Walking a Grid

Given a line parameterized by

$ \vec{x}(t) = \vec{x\_0} + \vec{x'} t $

we can compute the position of this at a given time in a _piecewise_ fashion.
That is, the position along each dimension is separable.

Given a regular spaced set of lines in each dimension, we can thus compute the
crossing time of each one of those lines (or planes).

---

## Covering the Sky

There are a handful of ways to tile the sky:

 * Hierarchical Triangular Mesh (HTM)
 * HEALPix
 * TOAST

---

## Why cover the sky?

In the limit of large distances, a source emitting spherically-symmetrically
with a fixed number of rays will have a very small covering fraction of the
sky.

---

## Visualization

How does this relate to visualization?

We can conduct volume rendering by creating and then computing the emission and
transmission of colors through a simulation.

Using this, we can even produce synthetic spectra.
