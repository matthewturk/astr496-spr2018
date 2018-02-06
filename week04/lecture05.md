---
title: Lecture 5
layout: lecture
slideOptions:
  transition: none
  theme: white
  center: false
---

# Computing in Astronomy<!-- .element: class="centered" -->
### Matthew Turk<!-- .element: class="righted" -->
### Spring 2018<!-- .element: class="righted" -->
### Lecture 5 <!-- .element: class="righted" -->

---

<!-- .slide: class="two-floating-elements" -->

## Files, Data, and Organization

* Text
  * ASCII (raw)
  * CSV / TSV
  * JSON
* Binary
  * HDF5
  * FITS
  * PNG/BMP/GIF/JPG/etc
* Query-based
  * SQL
  * JSON/REST

<div class="right" markdown=1>

![](diagrams/row_col.svg)

</div>

---

## Organization

| | Column 1 | Column 2 | Column 3 | Column 4 |
|-|-|-|-|-|
|Row 1|11|21|31|41|
|Row 2|12|22|32|42|
|Row 3|13|23|33|43|

Internally, this data is stored linearly, with one value immediately following
another.  We can do this in two methods:

||||||||||||
|:-|-|-|-|-|-|-|-|-|-|-|-|-|
| Row | 11 | 21 | 31 | 41 | 12 | 22 | 32 | 42 | 13 | 23 | 33 | 43 |
| Column | 11 | 12 | 13 | 21 | 22 | 23 | 31 | 32 | 33 | 41 | 42 | 43 |
<!-- .element: class="fragment" -->

---

### Organization: Row

||||||||||
|-|-|-|-|-|-|-|-|-|-|-|
| 11 <!--.element: class="table-hl" -->| <!--.element: class="table-hl" -->21 | 31 | 41 | 12 | 22 | 32 | 42 | 13 | 23 | 33 | 43 |

In row-oriented storage, successive _fields_ for a single _record_ are
adjacent.

<div style="height: 2.0em;"></div>

### Organization: Column

||||||||||
|-|-|-|-|-|-|-|-|-|-|-|
| 11 <!--.element: class="table-hl" -->| 12 | 13 | <!-- .element: class="table-hl" --> 21 | 22 | 23 | 31 | 32 | 33 | 41 | 42 | 43 |

In column-oriented storage, successive _records_ for a single _field_ are
adjacent.

---

## CSV (Comma-separated values)

| Column 1 | Column 2 | Column 3 | Column 4 | Column 5 |
|-|-|-|-|-|
| . | . | . | . | . |
| . | . | . | . | . |
| . | . | . | . | . |
| . | . | . | . | . |

<div style="height: 2.0em;"></div>

 * Lowest-common denominator format
 * Flexible delimiters
 * Ad hoc comments and headers
 * Row-oriented
 * Row-size can vary: no implicit indexing

---

```
...
390,1.83970e-003,-4.53930e-004,1.21520e-002
395,4.61530e-003,-1.04640e-003,3.11100e-002
400,9.62640e-003,-2.16890e-003,6.23710e-002
405,1.89790e-002,-4.43040e-003,1.31610e-001
410,3.08030e-002,-7.20480e-003,2.27500e-001
415,4.24590e-002,-1.25790e-002,3.58970e-001
420,5.16620e-002,-1.66510e-002,5.23960e-001
425,5.28370e-002,-2.12400e-002,6.85860e-001
...
```

---

```

390,1.83970e-003,-4.53930e-004,1.21520e-002
```

If we assume ASCII encoding, this becomes:

| | | |
|-|-|-|
|"390" <!-- .element: class="table-hl" --> |51 |57 |48 |
<!-- .element: style="margin-left: 0.2em;" -->

Breaking this further down, we encode each character:

||||||||||
|-|-|-|-|-|-|-|-|-|
|51 <!-- .element: class="table-hl" --> | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 |
|57 <!-- .element: class="table-hl" --> | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 1 |
|48 <!-- .element: class="table-hl" --> | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
<!-- .element: style="margin-left: 0.2em;" -->

---
```

390,1.83970e-003,-4.53930e-004,1.21520e-002
```

This is then translated into a floating point number:

||||||||||
|-|-|-|-|-|-|-|-|-|
|390.0 <!-- .element: class="table-hl" --> | 0 | 0 | 0 | 0 | 0 | 96 | 120 | 64 |
<!-- .element: style="margin-left: 0.2em;" -->

---
```

390,1.83970e-003,-4.53930e-004,1.21520e-002
```

|||||||||||||
|-|-|-|-|-|-|-|-|-|-|-|-|
| "1.83970e-03" <!-- .element: class="table-hl" -->| 49 | 46 | 56 | 51 | 57 | 55 | 48 | 101 | 45 | 48 | 51 |
<!-- .element: style="margin-left: 0.2em;"-->

And this is translated into a floating pointer number as well:

||||||||||
|-|-|-|-|-|-|-|-|-|
|1.83970e-003 <!-- .element: class="table-hl" -->  | 2 | 166 | 103 | 213 | 66 | 36 | 94 | 63 |
<!-- .element: style="margin-left: 0.2em;"-->

---

## JSON

| | | |
|:-|:-|:-|
| Record 1 | Record 2 | Record 3 |

<div style="height: 2.0em;"></div>

 * Row-oriented
 * Potentially-unknown subcomponent sizes (lists of lists)
 * Common response to REST APIs
 * Multiple types
   * String
   * Number
   * Object (JSON)
   * Array (list)
   * Boolean
   * null

---

```
[
 ...
 {"Agency Name":"University of Illinois",
  "Address":"501 E Daniel",
  "City":"Champaign",
  "Zip code":61820,
  "Year Acquired":1992,
  "Year Constructed":1935,
  "Square Footage":21845,
  "Total Floors":5
 }, 
 ...
]
```

<div style="height: 2.0em;"></div>

 * `[` and `]` indicate an array
 * `{` and `}` indicate a JSON object (or mapping)
 * `"` indicates a string
 * Numbers are, well, numbers.

---

## HDF5

| | | |
|:-|:-|:-|
| Column 1 | Column 2 | Column 3 |

<div style="height: 2.0em;"></div>

 * Columnar, chunked store
 * Flexible data types in-memory and on-disk
 * Hyperslab and boolean indexing
 * Fine-grained key/val metadata
 * Groups & hierarchies
 * Extensible types:
   * Numeric
   * Fixed-length strings
   * Variable strings

---

## Trivia

Is floating point math associative?

---

```python
import numpy as np

N = 1000

small = np.float32(1e-8)
big = np.float32(1.0)

tot1 = np.float32(0.0)
tot2 = np.float32(0.0)

for i in range(N):
    tot1 += small
tot1 += big

tot2 += big
for i in range(N):
    tot2 += small

print("Totals: ", tot1, tot2)
```

---

```python
import numpy as np

x = np.float32(16777216.0)
print(x + 0.9)

```

---

## Reproducibility vs Replicability

Can I reproduce your results, given your methods and data?

Can I replicate your findings?

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

## Rule 1: Keeping Track

(Not just for Future You!)

 * What did you do?
 * Why did you do it?
 * Can you redo it now?

Notes get out of date.  Executable workflows are much less likely to get out of
date.

Always separate the _doing_ from the _deciding_.

---

## Rule 2: Avoiding Manual Data Manipulation

> "So then I took the values that looked like outliers and I removed them."

> "I just looked at all the stuff that seemed significant."

> "Sure, I can go through and do it again."

Every step should be scripted, even if it's hard to do so.

---

## Rule 3: Archive Exact Versions

Behavior can change over time, for better or for worse.

```python
>>> import numpy as np
>>> a1 = np.random.random((512,512,512)).astype("f4")
>>> a1.sum(axis=0).sum(axis=0).sum(axis=0)
67110312.0
>>> a1.sum()
16777216.0
```

---

## Rule 4: Version Control All Custom Scripts

Let's learn git!  

It's the worst.<!-- .element: class="fragment" -->

---

## Test Case: Image Blending 

Last time we met, we explored image blending from multiple sources.

Let's apply our simple rules to that.

---

## git: part 1

Create a repository and add some files to it.

```bash
mkdir image_blending
cd image_blending
git init
```

Now, let's edit our image-blending file.

```bash
nano image_blending.py
git add image_blending.py
git commit
```

---

## Automation: pydoit

We need a way to do things again and again, and only when needed.

We will be using [pydoit](http://pydoit.org/) as a task manager and executor.

`pydoit` looks for tasks in a file called `dodo.py` in the current directory.
This defines one or more "tasks," which are defined by actions, dependencies,
outputs and metadata.

```python
def task_hello():
    """hello py """

    def python_hello(times, text, targets):
        with open(targets[0], "a") as output:
            output.write(times * text)

    return {'actions': [(python_hello, [3, "py!\n"])],
            'targets': ["hello.txt"],
            }
```

---

## Running Things

```python
def task_download():
  return {'actions': [['wget', '...']],
          'targets': ["output_filename"] }
```

```python
def task_rename():
  return {'actions': [['mv', 'something', 'else']],
          'targets': ['else'],
          'file_deps': ['something'] }
```

---

## Putting it Together

Let's now construct a `doit` system that blends our images.  We have three
images, $I_1$, $I_2$ and $I_3$, which we combine like so:

$\begin{bmatrix}R_f \\\ G_f \\\ B_f \end{bmatrix} = \begin{bmatrix}R_1 & R_2 & R_3 \\\ G_1 & G_2 & G_3 \\\ B_1 & B_2 & B_3 \end{bmatrix} \begin{bmatrix} I_1 \\\ I_2 \\\ I_3 \end{bmatrix}$

How should we construct a system that manages downloading these images,
combining them, and possibly even annotating?
