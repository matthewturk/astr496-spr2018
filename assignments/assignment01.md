---
layout: default
title: Assignment 1 - Data Containers
due: 2018-02-20
---

# Assignment 1 - Data Containers

**Due: 2018-02-20**

For this assignment, you are to construct a Jupyter notebook that explores data
types in Python.

 * Demonstrate how lists, tuples, strings and arrays work
 * Explore how you might use iteration
 * Write functions to test performance of data structures

You should test these structures:

 * sets
 * lists
 * dicts
 * numpy arrays

You will be graded on the writeup that accompanies this notebook.  You should
either do this writeup inline in the notebook or as a separate document.  Here
are some areas to address:

 * Which data structures should you use if:
   * You do or do not know their size in advance
   * You want to have different data types in each
   * You want to be able to remove things from the middle or the end
   * You need to quickly perform mathematics on the elements
 * For each data structure, address:
   * How well does it perform when it is empty (0 items), when it is
     medium-sized (10000 elements) and when it is large (10 or 100 million
     elements)?  Some things you may want to evaluate -- how long does it take
     to sum all the elements, to insert an element, to append an element, to
     join two containers.
 * Did you find anything surprising?

Here are a few tips:

 * Ensure that when you run timing tests, you test exactly what you think you
   are testing.  For instance, make sure you're just testing the actual
   operations -- not any setup or teardown costs.
 * If you can, re-use functions.  You may not be able to in all cases, however.
 * Please write everything up; the majority of your grade will be based on what
   you say about your experiences and what you learned.  This class is not
   meant to simply instruct you in how to code, but how to think about what you
   code.
 * When you time things, time how long it takes to do something *multiple*
   times, not just one time.

An example of what the code might look like for a list is as follows:

```python
import time

small = 10
medium = 10000
large = 10000000

small_list = []
medium_list = []
large_list = []

for i in range(small):
    small_list.append(i)

for i in range(medium):
    medium_list.append(i)

for i in range(large):
    large_list.append(i)

Ntimes = 100

t1 = time.time()
for i in range(Ntimes):
    max(small_list)
t2 = time.time()

small_max = (t2 - t1)/Ntimes

t1 = time.time()
for i in range(Ntimes):
    max(medium_list)
t2 = time.time()

medium_max = (t2 - t1)/Ntimes

t1 = time.time()
for i in range(Ntimes):
    max(large_list)
t2 = time.time()

large_max = (t2 - t1)/Ntimes
```

Here, note that we're also increasing the size of the list!  So we'd probably
want to look at each of the times divided by the size of each list.  That way,
we'll know how performance changes as a function of the size of the container.
