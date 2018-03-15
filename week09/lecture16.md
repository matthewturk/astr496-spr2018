---
title: Lecture 16
layout: lecture
slideOptions:
  transition: none
  theme: white
  center: false
---

# Computing in Astronomy<!-- .element: class="centered" -->
### Matthew Turk<!-- .element: class="righted" -->
### Spring 2018<!-- .element: class="righted" -->
### Lecture 16 <!-- .element: class="righted" -->

---

## This Time

 * Review Assignment
 * More on mpi4py
 * Visualizing particles

---

## Assignment Number Two

You can, but not required to, work in groups of up to four.  This assignment is
hard.

The number of people in your group *will* affect your grading scale.

Furthermore, you must detail in your writeup the process of collaboration.

https://classroom.github.com/g/Rc7zMJ64

If you work alone, you are expected to at least make an effort to implement the
tree code.

---

## mpi4py again

Last time, we experimented with mpi4py.

This time, let's break down what is occurring in each section.

We execute a command:

```
mpirun -np 4 python test_mpi.py
```

What happens?

---

## mpi4py process

```
mpirun -np 4 python test_mpi.py
```

 1. `mpirun` is started, with `argc` and `argv` indicting `-np 4 python
    test_mpi.py`
 1. `mpirun` sets up the basis for communication between processors, and
    initializes any structures at the operating system level
 1. Four processes are forked: one for each process.  These each have slightly
    modified environments, including their rank.
 1. In each forked process, `python` is executed with the remaining arguments
    (`test_mpi.py`).

---

## Walking through an MPI Script

```python
      from mpi4py import MPI
      import numpy as np

      N = 1024

      if MPI.COMM_WORLD.rank == 0:
          for i in range(MPI.COMM_WORLD.size - 1):
              arr = np.random.random(N)
              MPI.COMM_WORLD.Send([arr, MPI.DOUBLE], dest = i + 1)
      else:
          input_arr = np.empty(N, dtype="float64")
          value = MPI.COMM_WORLD.Recv([input_arr, MPI.DOUBLE], source = 0)

      MPI.COMM_WORLD.barrier()
```

How does this execute?

---

## Walking through an MPI Script

```python
****  from mpi4py import MPI
      import numpy as np

      N = 1024

      if MPI.COMM_WORLD.rank == 0:
          for i in range(MPI.COMM_WORLD.size - 1):
              arr = np.random.random(N)
              MPI.COMM_WORLD.Send([arr, MPI.DOUBLE], dest = i + 1)
      else:
          input_arr = np.empty(N, dtype="float64")
          value = MPI.COMM_WORLD.Recv([input_arr, MPI.DOUBLE], source = 0)

      MPI.COMM_WORLD.barrier()
```

We start out at the same place.

---

## Walking through an MPI Script

```python
      from mpi4py import MPI
      import numpy as np

      N = 1024

****  if MPI.COMM_WORLD.rank == 0:
          for i in range(MPI.COMM_WORLD.size - 1):
              arr = np.random.random(N)
              MPI.COMM_WORLD.Send([arr, MPI.DOUBLE], dest = i + 1)
      else:
          input_arr = np.empty(N, dtype="float64")
          value = MPI.COMM_WORLD.Recv([input_arr, MPI.DOUBLE], source = 0)

      MPI.COMM_WORLD.barrier()
```

Our first point of divergence is here.  Note that the processors might get
there at different times!

---

## Walking through an MPI Script

```python
      from mpi4py import MPI
      import numpy as np

      N = 1024

      if MPI.COMM_WORLD.rank == 0:
*         for i in range(MPI.COMM_WORLD.size - 1):
              arr = np.random.random(N)
              MPI.COMM_WORLD.Send([arr, MPI.DOUBLE], dest = i + 1)
      else:
 ***      input_arr = np.empty(N, dtype="float64")
          value = MPI.COMM_WORLD.Recv([input_arr, MPI.DOUBLE], source = 0)

      MPI.COMM_WORLD.barrier()
```

Our root processor sticks around and starts iterating.

---

## Walking through an MPI Script

```python
      from mpi4py import MPI
      import numpy as np

      N = 1024

      if MPI.COMM_WORLD.rank == 0:
          for i in range(MPI.COMM_WORLD.size - 1):
              arr = np.random.random(N)
*             MPI.COMM_WORLD.Send([arr, MPI.DOUBLE], dest = i + 1)
      else:
          input_arr = np.empty(N, dtype="float64")
 ***      value = MPI.COMM_WORLD.Recv([input_arr, MPI.DOUBLE], source = 0)

      MPI.COMM_WORLD.barrier()
```

We then get to the part where the root sends to process 1.

---

## Walking through an MPI Script

```python
      from mpi4py import MPI
      import numpy as np

      N = 1024

      if MPI.COMM_WORLD.rank == 0:
          for i in range(MPI.COMM_WORLD.size - 1):
*             arr = np.random.random(N)
              MPI.COMM_WORLD.Send([arr, MPI.DOUBLE], dest = i + 1)
      else:
          input_arr = np.empty(N, dtype="float64")
  **      value = MPI.COMM_WORLD.Recv([input_arr, MPI.DOUBLE], source = 0)

 *    MPI.COMM_WORLD.barrier()
```

Root sends to process 1, process 1 completes, and then root regenerates an
array and sends it to process 2.

---

## Walking through an MPI Script

```python
      from mpi4py import MPI
      import numpy as np

      N = 1024

      if MPI.COMM_WORLD.rank == 0:
          for i in range(MPI.COMM_WORLD.size - 1):
              arr = np.random.random(N)
*             MPI.COMM_WORLD.Send([arr, MPI.DOUBLE], dest = i + 1)
      else:
          input_arr = np.empty(N, dtype="float64")
   *      value = MPI.COMM_WORLD.Recv([input_arr, MPI.DOUBLE], source = 0)

 **   MPI.COMM_WORLD.barrier()
```

---

## Walking through an MPI Script

```python
      from mpi4py import MPI
      import numpy as np

      N = 1024

      if MPI.COMM_WORLD.rank == 0:
          for i in range(MPI.COMM_WORLD.size - 1):
              arr = np.random.random(N)
*             MPI.COMM_WORLD.Send([arr, MPI.DOUBLE], dest = i + 1)
      else:
          input_arr = np.empty(N, dtype="float64")
          value = MPI.COMM_WORLD.Recv([input_arr, MPI.DOUBLE], source = 0)

 ***  MPI.COMM_WORLD.barrier()
```

Root continues on through its loop, and all the other processes finish, until
finally we're at the `Barrier` together:

---

## Walking through an MPI Script

```python
      from mpi4py import MPI
      import numpy as np

      N = 1024

      if MPI.COMM_WORLD.rank == 0:
          for i in range(MPI.COMM_WORLD.size - 1):
              arr = np.random.random(N)
              MPI.COMM_WORLD.Send([arr, MPI.DOUBLE], dest = i + 1)
      else:
          input_arr = np.empty(N, dtype="float64")
          value = MPI.COMM_WORLD.Recv([input_arr, MPI.DOUBLE], source = 0)

****  MPI.COMM_WORLD.barrier()
```

Now, we can move past the barrier, and we're done.

---

## Other MPI operations

This is one method of distributing information to all the processors:

 * One processor generates the data
 * The other processors each wait for it in turn

But, if we know the data is not changing, there are more efficient ways of
doing this.

---

## MPI Broadcasting

```c
int MPI_Bcast( void *buffer, int count, MPI_Datatype datatype, int root, 
               MPI_Comm comm )
```

The `MPI_Bcast` function (`Bcast` and `bcast` in mpi4py) allows one processor
(called `root` here, but that can be specified) to be the _source_ process and
the others to be _destination_ processes.

---

## All versus non-all

We will see distinctions between functions that distribute the result to all
other process and those that do not.  Typically, those that do will be prefixed
with `All`.

Will these functions be more or less efficient than the ones that only have a
single root?

---

## MPI Gathering

Often, we will want to distribute information out to all processors.  This can
be in the form of a fixed size of data, or a size of data that varies based on
the specific process.

The first case would look something like this:

 * Each process (of N total) has M items of data
 * We want to collect all N * M pieces of data.

In this case, we can use a _gather_ operation, in either `MPI_Gather` or
`MPI_Allgather` form:

```c
int MPI_Gather(const void *sendbuf, int sendcount, MPI_Datatype sendtype,
               void *recvbuf, int recvcount, MPI_Datatype recvtype,
               int root, MPI_Comm comm)

int MPI_Allgather(const void *sendbuf, int sendcount, MPI_Datatype sendtype,
                  void *recvbuf, int recvcount, MPI_Datatype recvtype,
                  MPI_Comm comm)
```

---

## MPI Scatter

We can also scatter data from one root processor to all the other processors.

```c
int MPI_Scatter(const void *sendbuf, int sendcount, MPI_Datatype sendtype,
               void *recvbuf, int recvcount, MPI_Datatype recvtype, int root,
               MPI_Comm comm)
```

There is an "All scatter" method, but it operates slightly differently:

```c
int MPI_Alltoall(const void *sendbuf, int sendcount, MPI_Datatype sendtype,
                 void *recvbuf, int recvcount, MPI_Datatype recvtype,
                 MPI_Comm comm)
```

---

## Vector operations

If you really want to have fun, you can use the _vector_ form of these
operators:

```c
int MPI_Gatherv(const void *sendbuf, int sendcount, MPI_Datatype sendtype,
                void *recvbuf, const int *recvcounts, const int *displs,
                MPI_Datatype recvtype, int root, MPI_Comm comm)
int MPI_Allgatherv(const void *sendbuf, int sendcount, MPI_Datatype sendtype,
                   void *recvbuf, const int *recvcounts, const int *displs,
                   MPI_Datatype recvtype, MPI_Comm comm)
int MPI_Scatterv(const void *sendbuf, const int *sendcounts, const int *displs,
                 MPI_Datatype sendtype, void *recvbuf, int recvcount,
                 MPI_Datatype recvtype, int root, MPI_Comm comm)
int MPI_Alltoallv(const void *sendbuf, const int *sendcounts,
                  const int *sdispls, MPI_Datatype sendtype, void *recvbuf,
                  const int *recvcounts, const int *rdispls,
                  MPI_Datatype recvtype, MPI_Comm comm)
```

---

## Non-Blocking Communications

MPI has the ability to send and receive data with the _promise_ that the
communication will complete.  This allows the communication to be non-blocking.

For instance, imagine that when processing data, you need to pass it off to
another processor, but you do not need to wait for it to be passed off to move
onto the next item.

(This is not dissimilar to how email works.)

You can "post" a send or a receive, and you can check to see if it has
completed.

---

## Non-Blocking Operations

```c
int MPI_Isend(const void *buf, int count, MPI_Datatype datatype, int dest,
              int tag, MPI_Comm comm, MPI_Request *request)
int MPI_Irecv(void *buf, int count, MPI_Datatype datatype, int source,
              int tag, MPI_Comm comm, MPI_Request *request)
```

Note the `MPI_Request` objects here.  These are used in status checks:

```c
int MPI_Wait(MPI_Request *request, MPI_Status *status)
int MPI_Waitany(int count, MPI_Request array_of_requests[], int *indx,
               MPI_Status *status)
int MPI_Waitall(int count, MPI_Request array_of_requests[], 
               MPI_Status array_of_statuses[])
```

---

## Visualizing Particles

Formally, what are particles defined as in our simulations?

$ \rho( \mathbf{\vec{x}} ) = \delta (\mathbf{\vec{x}} - \mathbf{\vec{x\_i}}) M\_i $

What does this look like?

(Are they?)

---

## Platonic Ideals

What is the point of simulation?  What is the meaning we are trying to extract
from this data?

---

## Alternate Particle Visualizations

We will explore alternate methods of visualizing particles:

 * Patches (i.e., top-hat)
 * Gaussian functions
 * Uniform local density

To keep in mind:

 * How will this change with the size of the image?
 * Are there free parameters?
 * What is the assumption being presented versus that being given in the
   simulation?

---

## Visualizing Particles in Parallel

Visualizing optically-thin particles is an ideal application of parallel
computing!
