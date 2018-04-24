---
title: Lecture 25
layout: lecture
slideOptions:
  transition: none
  theme: white
  center: false
---

# Computing in Astronomy<!-- .element: class="centered" -->
### Matthew Turk<!-- .element: class="righted" -->
### Spring 2018<!-- .element: class="righted" -->
### Lecture 25 <!-- .element: class="righted" -->

---

## Last Time

 * ODEs
 * Cython
 * Not Quite Calling External Functions

---

## This Time

 * Calling External Functions
 * Halo Finding
   * Friends-of-friends
   * Union Find and Disjoint Sets
   * Parallelism

---

## Calling External Functions

Cython can be used to call external C functions.  To do this:

```
cdef extern from "something.h":
    cdef void hello_world()
```

This declares the function, much like in a `.h` file.  You can declare these
separately in `.pxd` files.

You must also link against the appropriate file or library.

---

## Halo Finding

Think of topographic maps.  We draw these by identifying individual "height"
values and linking them between regions.

Halo finding in astrophysical simulations typically follows one of a handful of
methods:

 * Simple Friends-of-Friends
 * Density-based estimates (i.e., eliminating saddlepoints)
 * Phase-space (6D) linking with iterative unbinding
 * Folding methods (ORIGAMI)

---

## Friends-of-Friends

How do we identify structures?

Identify a linking length $L$ that we use to connect sets.

---

<!-- .slide: data-background-image="images/structures1.jpg" data-background-size="contain" -->

---

## Union Find Algorithm

How do we do this when accumulating particles in a halo?  We can use a Disjoint
Set and a Union Find process.

 * For each particle, assign a unique ID.  This is its set.
 * Look within the linking length radius.  If any particle is part of the 

We can call this a process of assigning "Contours" (or "Sets") and ensuring
that they are flattened.

We will build this.
