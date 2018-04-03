---
title: Lecture 19
layout: lecture
slideOptions:
  transition: none
  theme: white
  center: false
---

# Computing in Astronomy<!-- .element: class="centered" -->
### Matthew Turk<!-- .element: class="righted" -->
### Spring 2018<!-- .element: class="righted" -->
### Lecture 19 <!-- .element: class="righted" -->

---

## This Time

 * Databases for Real
 * Some More Pandas
 * Optimizing Python Code with Cython

---

## Making a Database

Let's start with our data from last time.

```python
import pandas as pd
import sqlite3

hp_df = pd.read_csv("asu.tsv", delimiter=";", comment='#',
                    skiprows=[199, 200], skipinitialspace=True)
conn = sqlite3.connect("hipparcos.db")
conn.cursor().execute("drop table if exists objects")
hp_df.to_sql("objects", conn)
conn.close()
```

---

## Exploring Via SQL and Pandas

Let's take a look at some of the columns and how to use them for selection in
both Pandas and SQL.  Let's say we wanted to figure out the number of each
spectral type.

We could start with this in SQL:

```
SELECT SpType FROM objects;
```

and this in Pandas:

```
hp_df["SpType"]
```

---

## Exploring Via SQL and Pandas

Let's break down the SQL and Pandas commands a bit further and refine them.

```
SELECT SpType, COUNT(*) FROM objects GROUP BY SpType;
```

This will find each unique entry in `SpType` and collate results by that.  We
can further sort this:

```
SELECT SpType, COUNT(*) FROM objects GROUP BY SpType ORDER BY COUNT(*);
```

---

## Back to Pandas

Let's do this in Pandas now:

```
hp_df.groupby("SpType").size()
```

We can sort by using the `sort_values()` function.

```
hp_df.groupby("SpType").size().sort_values()
```

---

## Exercise

For your exercise, in SQL and in Pandas, figure out how to subselect based on
coordinates and use that to compute spectral types over bands in the sky.

---

## Optimizing Code in Python with Cython

[Cython](https://cython.org/) is a Python-like language that mixes C and Python
code.  It enables you to write high-performance code while still using many of
the data structures you use in python.

Make sure Cython is installed.  (It probably is.)

```
%load_ext Cython
```

In the next cell:

```
%%cython
cdef int i, j
cdef double val
for i in range(10000):
    for j in range(10000):
        val += i * j
print(val)
```

---

## Cython Code

There are a few things about Cython that we need to identify.  The first is
that we can define functions, as well:

```
%%cython
def hi(int j):
    print(j)
```

The next is that we can call C code, and we have a special `cimport` function
to import from external headers.

The final and most important thing is that we almost always want to declare our
types.

---

## Cython: MORE!

We'll now see how to declare and use:

 * arrays (from numpy)
 * external C functions from the standard library
 * python objects
