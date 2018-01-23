---
title: Lecture 3
layout: lecture
slideOptions:
  transition: none
  theme: white
  center: false
---

# Computing in Astronomy<!-- .element: class="centered" -->
### Matthew Turk<!-- .element: class="righted" -->
### Spring 2018<!-- .element: class="righted" -->
### Lecture 3 <!-- .element: class="righted" -->

---

## Python for Science

 * Arrays
 * Loops, functions, and scripts
 * Matplotlib
 * `ipywidgets`

---

## Data Structures - Arrays

 * Use `numpy` (as `np`)
 * Homogeneous (usually) data types
 * Fast for elementwise and uniform operations
 * Mutable
 * n-dimensional

---

## Arrays: Concepts

 * Iterating is slow, so try not to do it
 * If you can batch your operations, do that
 * Use built-in functions as much as possible
 * There is data behind these, and we can mess about with that

---

## Arrays: Types

 * Basic types of arrays:
   * https://docs.scipy.org/doc/numpy-1.13.0/user/basics.types.html
   * floating point (16, 32, 64, kinda-80)
   * integer (8, 16, 32, 64) both signed and unsigned
   * boolean (stored as `uint8`)
 * Can create new, compound data-type (`dtype`) objects

```python
>>> import numpy as np
>>> ndt = np.dtype( [ ("x", "f8"), ("y", "f8"),
...                   ("vel_x", "f8"), ("vel_y", "f8") ] )
>>> particles = np.random.random(100).view(ndt)
```

---

## Arrays: Back up a moment

 * Numpy arrays are pointers to blocks of data.
 * `.flags` , `.ndim`, `.shape` and `.stride` tell us about that data
 * We can have multiple things point to the same set of data

```python
>>> a = np.zeros(8, dtype="u1")
>>> b = a.view("u8")
>>> b
array([0], dtype=uint64)
>>> a[-1] = 255
>>> b
array([18374686479671623680], dtype=uint64)
```

---

## Arrays: Creating

 * Supply to `np.array()` some iterable
 * Use `np.mgrid`, `np.zeros`, `np.ones`, `np.random.random`, ...
 * Stack or concatenate other arrays
 * Read from file, etc

---

## Arrays: Selection

 * New _virtual_ dimensions can be added using `None` or `...` (ellipsis)
 * Index-based selection
 * Boolean selection

```python
>>> import numpy as np
>>> a = np.random.random(5)
>>> a > 0.7
array([False,  True,  True, False,  True], dtype=bool)
>>> a[a>0.7]
array([ 0.96330603,  0.95319968,  0.83365543])
>>> b = np.array([5, 9, 1, 4, 3])
>>> b[a>0.7]
array([9, 1, 3])
```

---

## Arrays: Doing stuff

 * Arrays can be operated on by a set of functions known as `ufunc` operators.
 * These can be binary or unary, and can operate elementwise (including
   broadcasting)
 * Common ufuncs, used by math operations:
   * `np.add` 
   * `np.subtract`
   * `np.divide`
   * `np.multiply`

---

## Arrays: Doing stuff

 * Other ufuncs which can be used from Numpy:
   * `np.power`
   * `np.sqrt`
   * `np.tan`
   * `np.arctan2` (What is this one?)
   * `np.max`, `np.min`, `np.maximum`, `np.minimum`
   * `np.clip`
 * Some accepts `output` arguments to minimize memory usage

```python
>>> a = np.random.random(10)
>>> a = np.clip(a, 0.2, 0.5, a)
```

---

## Riddle 1: Temporary Arrays

What happens when we do this?  What arrays are created, when, and how long do
they last?

```python
>>> a = np.random.random(100)
>>> b = (a * a + 2) - 1
```

---

## Arrays: Multi-Dimensional Selection

 * We can select along multiple dimensions using comma-separated slices
 * We can use `:` (colon) to indicate we want everything along a given
   dimension.

```python
>>> import numpy as np
>>> xy = np.mgrid[0.0:1.0:128j, 0.0:1.0:128j]
>>> v = np.random.random((128, 128))
>>> print(xy[0, :, 0])
[ 0.          0.00787402  0.01574803  0.02362205  0.03149606  0.03937008
  0.04724409  0.05511811  0.06299213  0.07086614  0.07874016  0.08661417
  0.09448819  0.1023622   0.11023622  0.11811024  0.12598425  0.13385827
  0.14173228  0.1496063   0.15748031  0.16535433  0.17322835  0.18110236
  ...
```

---

## Riddle 2: Cut by radius

```python
>>> import numpy as np
>>> xy = np.mgrid[0.0:1.0:128j, 0.0:1.0:128j]
>>> v = np.random.random((128, 128))
```

 * How do we compute the radius of each point from 0?
 * How would we change this to go from -0.5 to 0.5?

---

## Arrays: Broadcasting

 * You can "broadcast" arrays along virtual dimensions.
 * For instance, if I have an `(N, 3)` array, I can subtract from it a `(3,)`
   shaped array.

```python
>>> a1 = np.random.random((10, 3))
>>> a2 = np.random.random((3,))
>>> (a1 - a2).shape
(10, 3)
```

We can use this to our advantage to reduce memory consumption:

```python
>>> x = np.mgrid[0.0:1.0:10j]
>>> y = np.mgrid[0.0:1.0:10j]
>>> (x[:,None] - y[None,:]).shape
(10, 10)
```

---

## Flow Control - Functions

 * Functions can be defined using `def`
 * These accept both _positional_ and _named_ arguments

```python
>>> def show_bits(arr, say_hi = False):
...     print(np.unpackbits(arr.view('u1')))
...     if say_hi:
...         print("Also, hi")
...
>>> show_bits(np.random.random(1))
[1 1 1 0 1 0 0 1 0 1 1 1 1 0 0 1 1 1 1 1 1 0 1 0 0 0 0 0 0 1 1 0 1 0 1 1 1
 1 0 0 1 0 0 0 1 1 0 1 1 1 1 0 0 0 0 1 0 0 1 1 1 1 1 1]
```

---

## Case Study -- A Set of Files

 * Python has a *ton* of modules you can use.
 * Let's check out a few today!  Specifically, let's take a look at `glob`.
 * `glob.glob` takes a filename pattern and then supplies everything that
   matches that pattern.

```python
>>> import glob
>>> for fn in glob.glob("*.fits"):
...     print(fn)
galaxy1.fits
galaxy3.fits
galaxy2.fits
```

---

## Loops, Ordering, and Enumerating

 * We have three common iteration modifiers
   * `sorted` : return the iterables in sorted order
   * `reversed` : reverse the iterator
   * `enumerate` : give me the index as well
 * `glob` is not necessarily sorted, but we can wrap it in `sorted`

```python
>>> import glob
>>> for fn in sorted(glob.glob("*.fits")):
...     print(fn)
galaxy1.fits
galaxy2.fits
galaxy3.fits
```

 * We can use enumerate to figure out which file we're on:

```python
>>> import glob
>>> for fn in enumerate(sorted(glob.glob("*.fits"))):
...     print(fn)
(0, 'galaxy1.fits')
(1, 'galaxy2.fits')
(2, 'galaxy3.fits')
```

---

## Case Study: Putting it all together

We can unpack our sorted enumeration.

```python
>>> import glob
>>> for i, fn in enumerate(sorted(glob.glob("*.fits"))):
...     print(i)
0
1
2
```

---

## Hands-on: Some GAIA data

Download `gaia_validp.h5` from Slack.

---
