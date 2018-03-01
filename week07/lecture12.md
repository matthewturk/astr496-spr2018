---
title: Lecture 12
layout: lecture
slideOptions:
  transition: none
  theme: white
  center: false
---

# Computing in Astronomy<!-- .element: class="centered" -->
### Matthew Turk<!-- .element: class="righted" -->
### Spring 2018<!-- .element: class="righted" -->
### Lecture 12 <!-- .element: class="righted" -->

---

## This Time

 * Trees
   * What is a tree?
   * Types of trees: Octree and kD-tree
   * How can we construct a tree?
   * How would we use a tree?
 * Data for Initial Conditions
   * Format
   * Validator
 * Assignment

---

## Trees: Why?

Let's say we have an unsorted array of values.  For instance, the alphabet:

```
['Y', 'C', 'X', 'Q', 'W', 'T', 'I', 'R', 'J', 'U', 'S', 'F', 'L', 'P', 'D',
'M', 'G', 'E', 'O', 'B', 'K', 'H', 'A', 'N', 'V', 'Z']
```

If you wanted to find the position of the letter `H` and what its neighbors
are, you will need to inspect every single element until you find it.

---

## Trees: Why?

Let's say now that our array is sorted, and we have some function $f(E)$ that
tells us if $E$ is greater than, less than or equal to the value we're looking
for.

We can now do a bisection search.  If the array is 25 elements long and sorted,
we can search in order.  Evaluating $f(E\_{13}$ tells us if we should examine
the upper half or the lower half, and then we can bisect each half until we
find out number.


---

## Trees: Why?

So this solves our problem, right?  If we want to find the neighbors to an
object, we just need a function $f(E)$ that tells us if the element we're
examining is to the left or the right of the object we're seeking.

But, making this work in more than one dimension requires a bit more work.

---

## Trees

Imagine now that you have multiple dimensions along which an array can be
ordered.  We now need to be able to place those elements into a structure that
allows us to "sort" them in such a way.

If we are sorting along two dimensions, we need to be able to traverse along
two dimensions as well.

(Pause for diagram)

---

## Trees: Constructing a Tree

When building a tree, given a set of elements that need to be inserted, the
rough outline is that for each element:

 * Identify the "root" node of the tree
 * Find leaf node for element:
   * If current node is acceptable, terminate recursion
   * Identify which of "child" nodes element falls into
   * If current node is unacceptable, add "child" nodes

The choice of refinement _method_ is the primary distinction between Octree (or
Quadtree) and kD-tree data structures.  The choice of refinement _criteria_
depends on the purpose of the tree.

---

## Trees: Octree

In an octree, each node is refined by inserting planes along three dimensions.
In the case of MX Octrees this is defined as the center point of the node,
whereas in the case of PR Octrees this is stored in a node.

Octree nodes can contain several pieces of information, although some of these
may be redundant with the data structure itself.

```
left_edge[3]
right_edge[3]
parent_node
children_nodes[8]
elements[N]
central_point[3] (PR)
metadata
```

The metadata may include, for instance, center of mass and total mass of
particles in a node.

---

## Trees: kD-tree

In a kD-tree, each node is divided in half; the dimension along which it is
divided is cycled depending on the level of the node.  (First x, then y, then
z, etc.)

We will likely not use kD-trees in this class, although they do provide ample
opportunities for fast point selection and region selection, and by their
nature provide a good method for identifying N nearest neighbors.

---

## Sorting Values

Whether something is on the left or the right can be expressed as `0` or `1`.
That's a single bit.  So we need three bits to describe which of the eight
children in an octree a point belongs to, right?

We can utilize the "Morton" ordering to encode the position of an object in an
octree by a series of three bits, one after the other.

If we do this such that our high-bit values are the "coarse" nodes, we can
figure out the greatest common ancestor by doing a "logical and" and looking
for common prefixes.

---

## Sorting Values

For instance, we can represent the root node, then the right, right,
right octant as:

```
000 - 111
```

Let's try this with deeper refinement levels.

---

## Barnes-Hut Method

How do we use a tree to determine the sum of forces acting on a given region?

For every particle, we evaluate the external gravitational forces:

 * Starting at root node, examine distance and size
 * If `size / distance` is greater than our parameter, descend into its child
   nodes.
 * Otherwise, use the center-of-mass and total mass as the force from its
   elements.

---

## Assignment Update

We will be using Github Classroom.  You will receive a URL that will allow you
to access the repository.

Additionally, now that we have tree algorithms, we're going to try out
vectorization of our operations.
