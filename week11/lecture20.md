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
### Lecture 20 <!-- .element: class="righted" -->

---

## This Time

 * Phases of Programming
 * Testing

---

## Assignment Thoughts

Today's class has been inspired somewhat by seeing your assignments.

---

## Phases of Programming

 1. Messing about.
 1. Doing it lots of times.
 1. Helping others do it.
 1. Letting go.

---

## Phase One: Messing About

What are the characteristics of exploratory programming?

 * You aren't sure if you're going to need to do this again.
 * You don't know if it's going to have some results.
 * You haven't decided on a final set of implementation methods.

What are some environments you can use for this?

 * Interactive shell
 * Jupyter

---

## Phase Two: Doing it lots of times

Let's imagine now that you're doing something many, many times.  What does this
look like in an interactive shell?

What are some ways you can make this *easier* for yourself?

Brainstorm time: What are the "pain points" you ran into in your assignment?

---

## Phase Two: Doing it lots of times

How can we make this easier?

 * Take things out of interactive-only environments
 * Transform flat things into routines
 * Try to identify collections of data as classes
 * Make things work from the command line

---

## Phase Two: Remove Interactivity

Every time you are required to type something, or change a variable, you reduce
your ability to quickly conduct experiments.

For instance, you can remove the need to run inside Jupyter by converting to a
script:

```
jupyter nbconvert my_notebook.ipynb --to python
```

This will create a new Python script called `my_notebook.py`.  You can augment
this with arguments.  pydoit allows for arguments as well.

---

## Phase Two: Flat into Routines

Code can grow organically.  But it is not write-only.

```python
k = 0
for i in range(100):
    k += 1
print(k)

j = 0
for i in range(200):
    j += 1
print(j)
```

We can see there are two very similar statements here.  Can we transform this?

```python
def loopit(n):
    v = 0
    for i in range(n):
        v += 1
    print(v)

loopit(100)
loopit(200)
```

---

## Phase Two: Identify Collections of Data

Identifying a _type_ of data collection is the first step to creating it as a
reusable object.

If you have multiple sets of data that are related, for instance:

```
positions1
velocities1
positions2
velocities2
```

You may consider turning these into a class, and extending it with methods.

---

## Phase Three: Helping others do it

We can also create packages.  There exist ways, such as
[cookiecutter](https://github.com/audreyr/cookiecutter), to create simple
Python packages.

We can lay things out in a standard way:

```
README.md
/pkg_name/__init__.py
/pkg_name/file1.py
/pkg_name/file2.py
/pkg_name/file3.py
/tests/test_this.py
/doc/
```

Under `pkg_name` (which should be your package's name) you can place multiple
files that you import from.  Separation of these files helps to identify
responsibilities of different components and improve readability.

---

## Phase Four: Letting go

Managing collaboration on a project is difficult.  Version control and code
review helps with this.

What do we need to think about when bringing code in to a project?

 * Does this code meet the standards we set for the project?
 * Do we see any stylistic changes needed?
 * Are the algorithms correct?
 * Is it documented and tested?
 * What side-effects might it have?

---

## Phase Transitions

Each step in this process requires a slight "phase transition."  These are
*hard*.

What do you know about phase transitions?

---

## Testing

Testing is crucial to the development of software.

What are some reasons to test?

---

## Testing: Reasons Why

A few common reasons to add a test to a piece of code:

 * To make sure a specific is produced
 * To avoid back-tracking on fixed bugs (regressions)
 * To ensure that new code stays functional
 * To verify that old functionality still works

There are many more, but the biggest reason to add a test to a piece of code is
_piece of mind._

---

## Testing Framework

We will be using [pytest](https://pytest.org/).

pytest operates through assertions.  You run it with `pytest` at the command
line.

It will detect which tests to run, and inspect them to see what they may need.


---

## pytest examples 2

```python
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
```

---
## pytest examples 2

(Taken from pytest docs)

```python
import pytest
def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()
```

