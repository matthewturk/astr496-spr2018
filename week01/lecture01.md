---
title: Lecture 1
layout: lecture
slideOptions:
  transition: none
  theme: white
  center: false
---

# Computing in Astronomy<!-- .element: class="centered" -->
## Matthew Turk<!-- .element: class="centered" -->
## Spring 2018<!-- .element: class="centered" -->

---

## Basics

 * 11:00AM-12:20PM Tuesdays and Thursdays
 * Matthew Turk - mjturk@illinois.edu
 * Office Hours: Appointment
 * TA Ko-Yun (Monica) Huang - khuang33@illinois.edu
 * [matthewturk.github.io/astr496-spr2018](https://matthewturk.github.io/astr496-spr2018)

---

## Intake Survey

https://goo.gl/jRE7i3

---

## Resources

 * Moodle: https://learn.illinois.edu/course/view.php?id=28149
 * Slack: [astr496-spr2018](https://astr496-spr2018.slack.com/)
 * GitHub: [MatthewTurk/astr496-spr2018](https://github.com/MatthewTurk/astr496-spr2018)
 * Webpage: [matthewturk.github.io/astr496-spr2018](https://matthewturk.github.io/astr496-spr2018)

---

## Slack

 * Team is at `astr496-spr2018.slack.com`
   * `#general` : General announcements
   * `#assignments` : Help with assignments
   * `#help` : General help with Python, Javascript, visualization, etc
   * `#lectures` : During lectures, post links, comments, questions here
 * Use the `@` sign appropriately: `@[person]`, `@here`, `@channel`
 * Conduct will be held to same standards as any educational venue.
 * Web client, standalone client and mobile devices can access this team.
 * At the end of the semester, the team will be discontinued.

---

## Overview

I intend for this class to be hard, but also _fun_.

---

## Overview - Themes

1. How can you maximize your effectiveness as a researcher?
1. What is the ecosystem of astronomical computing like?
1. How do we use what we know about how computers work to maximize our efficiency?

---

## Overview - Goals

* Students will know where to go to find information to solve problems
* Students will be able to handle data from several different formats and sources
* Students will have facility with the commonplace tools used for astronomical computing, and a deeper understanding of where those tools have shortcomings

---

## Core Principles

 1. Understand the landscape
 1. Reduce your surface area of interaction
 1. Make it easier for Future You
 1. Fear is avoidable.

---

## Four Units

  1. Basics of Computation
  1. Astro Computation
  1. Simulations
  1. Data

---

## Unit 1: Basics

* Week 1 (Jan 16): Conversational Computation
* Week 2 (Jan 23): Basics of Python for Science
* Week 3 (Jan 30): TBA
* Week 4 (Feb 6): Reproducible Research

We will be covering the basics of "conversational computation," and how to apply a computational toolkit.

---

## Unit 2: Astro Computation

* Week 5 (Feb 13): Images and Observations
* Week 6 (Feb 20): ODE solvers
* Week 7 (Feb 27): Memory and Speed
* Week 8 (Mar 6): Introduction to Simulations

During this unit, we will be exploring some items specific to astronomical calculations, including astropy, applying ODE solvers, and how issues related to memory and CPU instruction can impact performance.

---

## Unit 3: Simulations

* Week 9 (Mar 13): Simulations: Particles
* Week 10 (Mar 20): **No Class** (Spring Break)
* Week 11 (Mar 27): Simulations: Grids
* Week 12 (Apr 3): Visualization

During this unit, we will be exploring and utilizing simulation codes such as Gadget and Enzo.

---

## Unit 4: Data

* Week 13 (Apr 10): Data Storage
* Week 14 (Apr 17): Databases and SQL
* Week 15 (Apr 24): Accelerators
* Week 16 (May 1): Future Directions

We will cover data formats, databases, writing and using SQL, and then talk a bit about accelerators such as GPUs and Xeon Phis.

---

## Structure of Class

Each class will begin with a lecture, which will last between 30-60 minutes.  The remaining time will be hands-on, _collaborative_ work.

You are expected to follow along with that work.

---

## Grading

* For each unit, you will conduct a project.  These projects will be _very_ broadly defined.  
* Projects will be assigned the Thursday of the first week of a unit.
* Projects will be due the Thursday _following_ the conclusion of the unit.
* You will be expected to struggle with these projects.
* You will not be expected to complete them completely successfully.

---

## Plagiarism

 * Plagiarism is about copying ideas.
 * Cite all code you utilize from elsewhere.


---

## Approach

We will be approaching computation as a set of experiments.

Each experiment has setup time, experimentation time, teardown time, and reflection time.

---

## Thought Experiment

You have a computational problem that requires you to read data from disk and process that data.

How do we estimate the cost of this?

---

## Ingredients

| | | |
|:-|-:|-:|
| Generic setup time | $t_s$ | $1$ |
| Specific setup time | $t_i$ | $N$ |
| Specific process time | $t_p$ | $?$ |

---

## Example: Image Processing

 * Write a bunch of code
 * Read $N_d$ bytes of data from disk
 * Process and display $N_d$ bytes of data
 
Total time: $t_s + N_d \times t_i + N_d \times t_p$

---

## Example: Image Processing

What if we decide we need to make a slight change?

We can execute the entire workflow ("experiment"), start to finish, until we reach the outcome we are satisfied with.  This may take $N_e$ times.

Total time: $N_e \times (t_s + N_d \ times t_i + N_d \times t_p )$

This is sub-optimal.

---

## Example: Image Processing

Think of things in terms of "dependencies."  What does task 1 depend on?  What does task 2 depend on?  What does task 3 depend on?

 1. Write a bunch of code
 1. Read $N_d$ bytes of data from disk
 1. Process and display $N_d$ bytes of data


---


## Example: Simulating Something

 1. Write the simulation platform
 2. Generate initial conditions
 3. Simulate
 4. Analyze

What are the costs and dependencies here?

---

## Initial steps

We have three goals today:

 1. Set up Python environment
 1. Load a sample FITS file
 1. Look at that FITS file

---

## Install Conda

The first thing we're going to do is set up our computing environment.  Some of you may already have such an environment set up.  The simplest way is to use Conda.

 1. Visit https://www.anaconda.com/
 2. Download and install the Python 3.6 package.
 3. `activate` to use.
 4. Make sure you have `astropy`, `matplotlib` and `ipywidgets`.
 5. Start `jupyter notebook`

---

---

