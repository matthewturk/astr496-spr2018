---
title: Lecture 6
layout: lecture
slideOptions:
  transition: none
  theme: white
  center: false
---

# Computing in Astronomy<!-- .element: class="centered" -->
### Matthew Turk<!-- .element: class="righted" -->
### Spring 2018<!-- .element: class="righted" -->
### Lecture 6 <!-- .element: class="righted" -->

---

## Trivia of the Day

How many job IDs does one project need?

---

## Principles of Reproducible Research

Sandve et al
([10.1371/journal.pcbi.1003285](https://doi.org/10.1371/journal.pcbi.1003285)),
"Ten Simple Rules for Reproducible Computational Research."

 1. For Every Result, Keep Track of How It Was Produced
 2. Avoid Manual Data Manipulation Steps
 3. Archive the Exact Versions of All External Programs Used
 4. Version Control All Custom Scripts
 5. Record All Intermediate Results, When Possible in Standardized Formats
 6. For Analyses That Include Randomness, Note Underlying Random Seeds
 7. Always Store Raw Data behind Plots
 8. Generate Hierarchical Analysis Output, Allowing Layers of Increasing Detail
    to Be Inspected
 9. Connect Textual Statements to Underlying Results
 10. Provide Public Access to Scripts, Runs, and Results

---

## Rule 5: Record all Intermediate Results

Imagine this workflow:

```python
import numpy as np
import glob

results = []

for fn in glob.glob("my_data/*.npz"):
    data = np.fromfile(fn)
    new_data = really_long_calculation(data)
    results.append(new_data)

process_results(results)

```

Modification of the `process_results` routine would mean doing everything over
again!

What is an alternate, using the tools we know?

---

## Rule 6: Note Underlying Random Seeds

```python
>>> import numpy as np
>>> a1 = np.random.seed(0x4d3d3d3)
>>> print(a1)
0.76017901417031175
```

What if you use a random selection of values from a large dataset?

```python
>>> data = np.fromfile("really_big.npz")
>>> subselection = np.random.choice(data, size = 100000)
>>> process(subselection)
```

Distinguish between reproducibility and replicability.

---

## Rule 7: Always Store Raw Data Behind Plots

Your collaborators will almost always want you to make changes to the fonts.

---

## Rule 10: Public Access

Your data, and your scripts, should be available in a way that does not require
permission and that is maximally easy to use.

An emerging practice is to store code, and in some cases data, on GitHub.

Let's set up a sample repository.

(Later in the semester we will discuss data repositories.)

---

## Quickly Storing Data

We want to store our data in a way that is:

 * Self-describing, so we know what it is
 * As lossless as possible
 * Stable

---

## HDF5

HDF5 is a hierarchical data format that is simple and straightforward to use in
Python.

In HDF5, *groups* are like directories; they contain datasets and can have
metadata affiliated with them.

In HDF5, datasets are N-dimensional arrays that can be subselected.

---

## h5py: Writing

To store data using `h5py`, we can create a dataset:

```python
import h5py
import numpy as np

d = np.random.random((128, 128, 128))
f = h5py.File("my_data.h5", "w")
f.create_dataset("/my_data", data=d)
f.close()
```

Note a few things: the HDF5 format is structured like Unix directories.  So we
have `/my_data` which is at the root level.  We can create groups like so:

```python
f.create_group("/datasets")
f.create_dataset("/datasets/data1", data=d)
```

---

## h5py: Reading

We can read data back in by accessing the file like a dictionary:

```python
f["/datasets/data1"]
```

This obtains a handle to the dataset, but does *not* yet conduct any disk IO.
It waits until you request specific items to do any disk access.

This means you can read just some bits at a time!

```python
tenpercent = f["/datasets/data1"][::10]
```

To read everything, use `[:]` or `.value`.

---

## pydoit (continued)

```python
from doit.tools import run_once

filenames = ['502nmos.zip', '656nmos.zip', '673nmos.zip']
base_url = "https://www.spacetelescope.org/static/projects/fits_liberator/datasets/eagle/"

def task_download():
  actions = []
  for filename in filenames:
    actions.append(['wget', base_url + filename])
  return {'actions': actions,
          'targets': filenames,
          'uptodate': [run_once]}

def task_unzip():
  actions = []
  targets = []
  file_dep = []
  for filename in filenames:
    actions.append( ['unzip', '-o', filename] )
    file_dep.append(filename)
    targets.append( filename.replace('.zip', '.fits') )
  return {'actions': actions,
          'file_dep': file_dep,
          'targets': targets}

```

---

## Putting it All Together

We'll continue with our image blending, but we will also look at how to build a
paper.

An example paper template:

https://bitbucket.org/data-exp-lab/dxl-paper-template

