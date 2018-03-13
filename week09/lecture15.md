---
title: Lecture 15
layout: lecture
slideOptions:
  transition: none
  theme: white
  center: false
---

# Computing in Astronomy<!-- .element: class="centered" -->
### Matthew Turk<!-- .element: class="righted" -->
### Spring 2018<!-- .element: class="righted" -->
### Lecture 15 <!-- .element: class="righted" -->

---

## This Time

 * Parallelism and Concurrency
 * MPI in C and Python

---

## Thought Experiment

Everyone is going to vote on their favorite movie 1980's time travel movie,
from the following two choices:

 * Back to the Future
 * Bill and Ted's Excellent Adventure

---

## Tell me your answers

When I call on you, tell me your answers.

---

## Hold on

This is dumb.  I'll pass out paper, and everybody write down your answer.
Then, pass them forward and I'll count them up.

---

## Ugh one more time

This time, just converse amongst the people in your row, then we'll figure out
the total number of votes for each of the two options.

---

## Synchronization

We just tried three different methods of computing a sum.

The first required me to visit each person in turn, getting their answer, and
then continuing.  So we had:

 * 1 accumulation variable
 * N visits to dataset components
 * N synchronization steps

---

## Synchronization

The second involved each person writing down their answer and passing it
forward.

 * N+1 accumulation variables
 * 0 visits to dataset components
 * 1 synchronization step

---

## Synchronization

The final method involved local aggregation.

 * R+1 accumulation variables
 * R visits to dataset components
 * R synchronization steps

---

## Amdahl's Law

You are bottlenecked by the part of your program that cannot be parallelized.

**Example:**  You are writing a paper with five friends.  You can all
write six pages an hour, and the proposal needs to be 36 pages.

It takes you an hour to print the paper out.

It takes you one hour to all work together and write the entire paper.

Even if you had infinite friends, it would still take you at least an hour to
do the entire process.

---

## Amdahl's Law

$\lim\_{s\rightarrow \infty} S = \frac{1}{1 - p}$

In the theoretical limit of infinite parallelism, we can only ever achieve a
speedup that is limited by the part of the program that *can't* be sped up.

---

## Why Parallelize?

There are principally two reasons to parallelize an operation:

 * To make things go faster (strong scaling)
 * To make bigger things go at all (weak scaling)

Note that we will be discussing strong and weak scaling from the perspective of
_algorithms_, not from the perspective of hardware.

"Processor count" is used as shorthand for "number of worker nodes or
processors."

---

## Strong Scaling

If you have a fixed problem size -- for instance, you are simulating $1024^3$
particles, strong scaling would be the rate at which the simulation finished as
a function of the number of processors that are used.  If it took half as long
to run with twice as many processors, it would be ideally scaling.

You can evaluate the strong scaling of an approach to a problem by looking at
the time to completion as a function of the number of processors applied to the
problem.  If $t \times N$ is constant, the problem is scaling strongly.o

---

## Weak Scaling

Weak scaling evaluates the ability of an approach to increase the scale of a
problem _and_ the processor count and keep the time to completion constant.

For instance, if we were examining our particle simulation and we wanted to
evaluate weak scaling, we would look at the time to completion for $1024^3$ on
$N$ processors, and then evaluate the time to completion for $2048^3$ on
$8\times N$ processors.  If they were identically, it would be weakly scaling.

---

## Parallel Processing

When we will discuss parallel processing, we will likely think of it in this
model:

 1. Initialize a task or problem to conduct
 1. Break this task up into smaller pieces (and distribute them?)
 1. Each worker processes their own task
 1. Collect results (if needed)

There is a similar but slightly different model that we may experiment with:

 1. Initialize a task or problem to conduct
 1. Create a queue of jobs to execute
 1. Workers process jobs and ask for new ones when done
 1. Collect results (if needed)

Which situations would be good for each of these?

---

## Message Passing

We will be discussing one method for parallelism called the Message Passing
Interface (MPI).

There are many different methods for conducting parallel operations; some of
these are based on the task-queue model, and others are based on explicit
parallelism.

---

## Running a Parallel Program

There are several pieces of information that a program needs to be able to
execute in parallel.

 * "Who am I?"
 * "How was I invoked?"
 * "Who are my peers?"
 * "How do I talk to them?"

When you run an MPI program, these are supplied to it via environment variables
or other control features; however, these are all _implementation specific_ and
outside the realm of what you actually need to know.

```bash
mpirun -np 4 ./my_parallel_program
```

---

<!-- .slide: data-background-image="images/whenyoudothingsright.jpg" data-background-size="contain" --> 

---

## MPI Init

The first thing in an MPI program in C that you need to execute is `MPI_Init`.
This constructs the necessary in-memory data structures so that you can pass
information between processors or tasks.

MPI Communicators define a set of tasks that can communicate information.
Whenever you pass information around, you will use one of these objects.

---

## MPI Communicators

The base-level communicator is the `COMM_WORLD`.  This is set up at startup.

There are two very helpful functions to use with MPI communicators:

 * `MPI_Comm_size (MPI_Comm comm, int *size)`  what is the size of this
   communicator?
 * `MPI_Comm_rank (MPI_Comm comm, int *rank)`  what is my rank in this
   communicator?

---

## Sending and Receiving Data

MPI requires that you describe several pieces of information about data before
it can handle it:

 * How big is this data?
 * What type is the data? (Let's talk about this, though)
 * Where is it going?
 * Does it have a "tag"?

Additionally, the destination (usually) has to have a place for it to be stuck
set up.  You can't receive mail without a mailbox.

---

## Operations: Send and Receive

The operations `MPI_Recv` and `MPI_Send` are how we pass information around.
Let's dig into these:


 * `int MPI_Send(const void *buf, int count, MPI_Datatype datatype, int dest, int tag, MPI_Comm comm)`
 * `int MPI_Recv(void *buf, int count, MPI_Datatype datatype, int source, int tag, MPI_Comm comm, MPI_Status *status)`

Note that these are *blocking* operations.  What do you suppose that means?

---

## Operations: Reductions

Because MPI understands data types, we can also execute operations using
information about those datatimes.

 * `MPI_MAX`
 * `MPI_MIN`
 * `MPI_SUM`
 * `MPI_PROD`
 * `MPI_LAND`
 * `MPI_LOR`
 * `MPI_BAND`
 * `MPI_BOR`
 * `MPI_MAXLOC`
 * `MPI_MINLOC`

---

## Operations: All-reductions

There are two ways we can call a 'reduce' operation.

 * `int MPI_Reduce(const void *sendbuf, void *recvbuf, int count, MPI_Datatype datatype, MPI_Op op, int root, MPI_Comm comm)`
 * `int MPI_Allreduce(const void *sendbuf, void *recvbuf, int count, MPI_Datatype datatype, MPI_Op op, MPI_Comm comm)`

What do you think the differences are?

---

## mpi4py

mpi4py is a Python wrapper of MPI.  Let's use it!
