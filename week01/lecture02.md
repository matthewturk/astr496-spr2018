---
title: Lecture 2
layout: lecture
slideOptions:
  transition: none
  theme: white
  center: false
---

# Computing in Astronomy<!-- .element: class="centered" -->
### Matthew Turk<!-- .element: class="righted" -->
### Spring 2018<!-- .element: class="righted" -->
### Lecture 2 <!-- .element: class="righted" -->

---

## Survey Results

 * Split between Windows and OSX, with a bit of Linux
 * Most have Python installed
 * Some experience with Python
 * Top interests: Simulations and Observations

---

## Assignment 1

For this assignment, you are to construct a Jupyter notebook that explores data
types that come with Python.

 * Demonstrate how lists, tuples, strings and arrays work
 * Explore how you might use iteration
 * Write functions to test performance of data structures

As per our discussion last week, you will be graded on the writeup that
accompanies this notebook.  You should either do this writeup inline in the
notebook or as a separate document.  Here are some areas to address:

 * Which data structures are the most performant for things like appending,
   slicing, etc?
 * When would you use a tuple?
 * Did you find anything surprising?

---

## Core Principles

 1. Understand the landscape
 1. Reduce your surface area of interaction
 1. Make it easier for Future You
 1. Fear is avoidable.

---

## Programming

 * Orientation
 * Types & data structures
 * Flow control
 * Libraries

---

## Orientation

 * `help()`
 * `dir()`
 * `import`
 * `print()`

---

## Types

 * Strings
 * Numbers
 * Lists
 * Dictionaries
 * Tuples

---

## Mutability

Mutability is whether or not you can change an object in-place.  Strings are
not mutable:

```python
>>> a = "hi there"
>>> a[4]
'h'
>>> a[4] = "r"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  TypeError: 'str' object does not support item assignment
```

But, lists are:

```python
>>> a = [1, 2, 3]
>>> a[2] = 5
>>> a
[1, 2, 5]
```

---

## Strings

Strings are collections of bytes that are associated with an encoding.  

```python
>>> name = b"Hi there"
>>> name.decode("ascii")
'Hi there'
>>> name
b'Hi there'
```

We can use unicode.

```python
>>> snowman = "☃"
>>> snowman.encode("utf-8")
b'\xe2\x98\x83'
>>> snowman
'☃'
```

---

## Unicode

```python
>>> snowman = b"\xe2\x98\x83"
>>> snowman.decode("utf-8")
'☃'
```

---

## Numbers - Integers

Python stores integers at arbitrary precision:

```python
>>> my_num = 7
>>> for i in range(6):
...     my_num *= my_num
...     print(my_num)
...
49
2401
5764801
33232930569601
1104427674243920646305299201
1219760487635835700138573862562971820755615294131238401
```

---

## Numbers - Floating Point

Floating point numbers are stored internally to precision as defined in
`sys.float_info`

```python
>>> import sys
>>> sys.float_info
sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308,
min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15,
mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
```

---

## Data Structures - Lists

 * Expandable
 * Mutable
 * Iterable
 * Hetereogeneous

```python
>>> b = [1, "hi", 2, "hello"]
>>> b
[1, 'hi', 2, 'hello']
>>> b[:2]
[1, 'hi']
```

---
## Data Structures - Tuples

 * Immutable
 * Iterable
 * Hetereogeneous

```python
>>> b = (1, "hi", 2, "hello")
>>> b
(1, 'hi', 2, 'hello')
>>> b[:2]
(1, 'hi')
>>> b[3] = 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  TypeError: 'tuple' object does not support item assignment
```

---

## Data Structures - Dictionaries

 * Mutable
 * Mapping from key to value
 * Keys must be "hashable" (immutable)
 * Ordering is not quite guaranteed

```python
>>> d = {'hi': 'word', 'there': 'word2'}
>>> d['hi']
'word'
```

---

## Data Structures - Sets

 * Unordered
 * One of each type
 * Fast

```python
>>> s = set([])
>>> s.update([1,2,3,1])
>>> s
{1, 2, 3}
```

---

## Data Structures - Arrays

 * Use `numpy` (as `np`)
 * Homogeneous (usually) data types
 * Fast for elementwise and uniform operations
 * Mutable
 * n-dimensional

```python
>>> import numpy as np
>>> a = np.random.random(10)
>>> a
array([ 0.7683637 ,  0.67162959,  0.25995079,  0.01814012,  0.06132318,
        0.23217367,  0.84638998,  0.16550409,  0.57083095,  0.7759668 ])
>>> b = np.arange(10)
>>> a + b
array([ 0.7683637 ,  1.67162959,  2.25995079,  3.01814012,  4.06132318,
        5.23217367,  6.84638998,  7.16550409,  8.57083095,  9.7759668 ])
```

---

## Flow Control - Conditionals

 * `if` can be paired with `elif` and `else`
 * There is no `switch`/`case` statement in Python
 * Conditionals can be nested and can have multiple boolean conditions
 * Evaluation is stopped after first breaking condition

```python
>>> if 1 > 2:
...     print("This is indeed a disturbing reality.")
... else:
...     print("Phew.")
...
Phew.
```

---

## Flow Control - Loops

 * `while` operates until a condition is no longer satisfied
 * `for` _iterates_.
 * Note that `for` consumes iterables, and does not evaluate truth (as in C)

```python
>>> s = "hello there"
>>> for v in s:
...     print(v)
...
h
e
l
l
o

t
h
e
r
e
```

---

## Flow Control - Loops

```python
>>> b = np.random.random(10)
>>> for v in b: print(v)
...
0.861358731463
0.770358747697
0.636375341094
0.503571020941
0.486648434293
0.672406873231
0.347108279042
0.536811502731
0.207512574733
0.106610687194
```

---

## Flow Control - Loops

```python
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
```

Note that `range(5)` goes from `0` to `4`.  Why?

---

## Libraries

 * We import modules and libraries
 * These are either local to our script or system-wide

```python
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> import h5py
>>> from collections import Counter
```

---
