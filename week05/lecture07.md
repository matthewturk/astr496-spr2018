---
title: Lecture 7
layout: lecture
slideOptions:
  transition: none
  theme: white
  center: false
---

# Computing in Astronomy<!-- .element: class="centered" -->
### Matthew Turk<!-- .element: class="righted" -->
### Spring 2018<!-- .element: class="righted" -->
### Lecture 7 <!-- .element: class="righted" -->

---

## Announcements

 * As noted on Moodle and Slack, homework has been postponed until the 20th of
   February.  A rubric is now available.
 * Computational environments are getting tricky.  I am in the process of
   deploying a Jupyterhub instance that we can all use.
 * Received feedback about the course so far.

---

## Where You Should Be

 * Basic familiarity with these Python concepts:
   * Lists (`b = [1, 2, 'there', 3]`)
   * Dictionaries (`a['hi'] = 2`)
   * Numpy arrays (`arr.min() + arr.max()`)
   * Iteration (`for x in y`)
   * Conditionals (`if`, `elif`, `else`)
 * Basic visualizations.
 * Can motivate making decisions for reproducibility

---

## Today

 * What is a class in python, and why would we use them?
 * Creating our image class
 * Basic image operations using `Pillow`

---

## Classes in Python

Think of classes like a mold that you use to make lots of things that are
mostly alike.

 * _Methods_ are functions that are defined on _instances_ of classes.  These
   all receive an argument that is the instance being operated on (`self`).
 * Classes can have affiliated data, and we can on-demand or automatically
   process data.
 * We will use classes to record _state_ or to collect related routines.

---

## Class Syntax

The keyword `class` defines a class body.

```python
class SomeTypeOfObject:
    pass

obj = SomeTypeOfObject()
```

This class does nothing!  And note that we are free to modify instances in
python:

```python
obj.something_new = "abcdefg"
```

---

## Special Methods: init

`__init__` is called when a class is created.  This is often done to perform
initialization tasks like setting member data, or constructing helper objects.

For instance, let's create an example class:

```python
import numpy as np

class MyDataset:
    def __init__(self, size):
        self.size = size
        self.data = np.random.random(size)
```

We can now instantiate that class by executing:

```python
my_dataset = MyDataset(128)
print(my_dataset)
```

This doesn't print out `my_dataset.data`!

---

## Special Methods: Operators

A number of different operators are also defined for classes, so that you can
meaningfully do things like addition, subtraction, etc.

Let's now extend our `MyDataset` class to support a few of these.

```python
import numpy as np

class MyDataset:
    def __init__(self, size):
        self.size = size
        self.data = np.random.random(size)

    def __add__(self, other):
        return MyDataset(self.size)
```

Here, we've created a new `__add__` method that operates in **flagrant
violation** of the normal rules of addition.  But at least we can do this:

```python
a = my_dataset(128)
b = my_dataset(256)
c = a + b
d = b + a
```

#### Quick check: What are the sizes of c and d?

---

## Normal Methods

We can implement methods that accept zero to many arguments, as well.

```python
import numpy as np
import matplotlib.pyplot as plt

class MyDataset:
    def __init__(self, size):
        self.size = size
        self.data = np.random.random(size)

    def plot(self, filename, ylabel = ""):
        plt.clf()
        plt.plot(self.data)
        plt.ylabel(ylabel)
        plt.savefig(filename)
```

We can also have optional arguments, as you see here with the `ylabel`
variable.  If it is supplied, it overrides the default value.

---

## Interaction

Today, we will be constructing an `ImageData` class.  We want it to be able to
do the following things:

 * Start from either existing data or non-existing data
 * Plot our image
 * Blend images together
 * Operate on images

---

## Basics with Images

Today we'll start out with some basic image manipulation.

 * Reading and saving image data
 * Displaying images using matplotlib
 * Histograms and shifting channels
 * Clipping
 * Build out our image class

---

## Reading Image Data

We will use the `Pillow` library for reading data in.  `Pillow` has support for
an enormous number of image operations, but also has something of a learning
curve.

```python
from PIL import Image
my_image = Image.open("wherespoochie.jpg")
```
