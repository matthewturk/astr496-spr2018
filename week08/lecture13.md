---
title: Lecture 13
layout: lecture
slideOptions:
  transition: none
  theme: white
  center: false
---

# Computing in Astronomy<!-- .element: class="centered" -->
### Matthew Turk<!-- .element: class="righted" -->
### Spring 2018<!-- .element: class="righted" -->
### Lecture 13 <!-- .element: class="righted" -->

---

## This Time

 * More on Trees and Bits
 * Update on Assignment 2
 * The C language
 * Compiling

---

## Trees and Bits

Last time, we spoke briefly about how to turn a tree into a series of bits.

If we have a bifurcating path, we can report our choice of direction as a
series of "left" or "right" choices.

If we had only a single dimension, we can then translate a bit series such as

```
011001
```

into a path that goes left, right, right, left, left, right.

---

## Bits in more dimensions

If we extend this to thinking about multiple dimensions, as long as we know the
order our dimensions go in, we can split this up into multiple sequential
choices.

For instance, when we progress from one level of an octree to the next, we need
to know which of the eight child nodes we go into.  These are determined by
whether they are low or high in the X, low or high in the Y, and low or high in
the Z.  (You can think of this as left/right, back/front, top/bottom.)

So instead of looking at this as a sequence of L/R choices, we now can split up
a series of 0's and 1's into a set of three choices:

```
011001
```

Becomes [left, front, top], [left, back, top].

---

## Bits

The next step requires that we think about bits as something we can move
around in a representation of a number.  If we have an 8-bit number, it is
represented as a sequence of bits.  If it is zero, it looks like:

```
00000000
```

If it is 1

```
00000001
```

---

## Bit Shifting

If we have our number 1 represented in an 8-bit container, we can shift it to
the left or the right.  The operators for doing so look like `<<` and `>>`.
When we shift a number, the bits that come in off the edges (left or right) are
always zero.

```
00000001 [ << 1 ]
00000010
```

If we shift to the right:

```
00000001 [ >> 1 ]
00000000
```

---

## Bit Shifting (again)

We can do multiple shifts, as well:

```
00000001 [ << 2 ]
00000100
```

There are also a set of logical operations we can conduct.  `OR`, `AND`, `NOT`
and `XOR` are the most common, as they have operators in C and Python.  (You
will occasionally see `NAND` as well, but much less commonly.)

---

## Bit Shifting and Trees

So, if we are progressing down a single bifurcating path in one dimension, we
can do this by:

 1. Decide if we are moving to the left or the right on this path.
 1. If left, set the rightmost bit to 0, else to 1.
 1. Bit shift the number to the left.

This means that the *left*-most values (i.e., the most significant digits)
correspond to the coarsest choices in our path.

---

## Bit Shifting and Multi-Dimensions

If we are doing this for a multi-dimensional path, we need to do additional
iterations:

 1. For each dimension (i.e., x,y,z):
    1. Decide if we are moving to the high or low in this dimension
    1. If low, set rightmost bit to 0, else to 1.
    1. Bit shift to the left by one.
 1. Progress down one level.

This means that paths that vary at fine levels are close in integer
representation in our bit-encoding; paths that vary early on (which may still
be close, spatially) vary at large values in integer representation.

---

## Assignment 2

Assignment 2 is now ready to go.

**Due: March 29, 2018**

That gives you several weeks from this Thursday, including Spring Break.

---

## C

Understanding how C works is one of the most important lessons you can take
away from this course.

This is not the same as learning C in detail.

---

## C: First Program

```c
#include <stdio.h>

int main(int argc, char** argv) {
  fprintf(stderr, "Hello there.\n");
  return 0;
}
```

What does this do?

Now, type it into a text editor.

---

## C: Making Something

On your command prompt, type this:

```
gcc that_program.c
```

What happens?

---

## C: Includes and Libraries

When we are using C, we make a distinction between "includes" and "libraries."
One occurs at compile time, while the other occurs at either linking time or
runtime.

When something is utilized in C, the compiler must understand what is being
utilized and what the end behavior of that is going to be.

The compiler does not need to know how or where to call a function.  That's for
the linker to figure out.

---

## C: Includes and Libraries 2

When we type:

```c
#include <stdio.h>
```

the _preprocessor_ knows that it needs to find a file called `stdio.h` and
include its contents in the top of the C file.  (That's right; it really does
include it!)

Any variables and functions that are defined or described in that header file
can now be used.

But what if the functions themselves are located somewhere else?

---

## C: Calling Functions

In C, we will be thinking of calling a series of functions as our fundamental
navigation operation.

```
#include <stdio.h>

void some_function() {
  fprintf(stderr, "Hello!\n");
}

int main(int argc, char** argv) {
  some_function();
}

```

Functions do *not* share local variables.  This is kinda important!

---

## C and Memory

In C, memory is a set of bits and bytes that can be allocated on either the
*stack* or the *heap*.

The *stack* is the memory that belongs to a given function.

The *heap* belongs to the entire program.

---

## Linking a C Program

What happens when we compile?

 1. The C preprocessor reads the file, includes all the includes, figures out
    macros, etc.
 1. The file is then parsed by the compiler and some form of machine code is
    output.
 1. If the compiler is asking to *link* the file, all functions are *resolved*.
 1. Either an executable or an object file is then output.

---

## Object Files and Executables

We can instruct a compiler to produce an "object" file.  This includes a set of
functions and variables that are exported as symbols.

Let's try this.

```
gcc -c that_program.c -o that_program.o
```

Now let's look at it using the command `nm`.

---

## Linking

When a program is linked, the functions are resolved either *dynamically* or
*statically*.  In the case of *dynamic* linking, the executable knows where to
go to load up a given function and use it later.  In the case of *static*
linking, the functions are basically copied into the executable.

Why would we want dynamic versus static?

 * Static: faster, and more reliable in some cases, but can have collisions
 * Dynamic: easier, and allows for new functions to be called at runtime

---

## Variable Types

There are a number of different types and variables that we can use.  The
standard syntax is to declare a variable by a type, then qualifiers for the
array or pointer nature, then a name.

For instance, a pointer uses `*` to indicate that it points to a value.  A
reference can be obtained by using `&`.

```c
float my_float = 1.0;
float *my_float_pointer = &my_float;
```

Pointers need to be initialized.

---

## Variable Types 2

We will be using these types primarily:

 * `char`
 * `int`
 * `long`
 * `float`
 * `double`

---

## Memory Allocation

You can allocate memory on the heap by calling the function `malloc`.  This
must then be deallocated using `free`.

`malloc` receives the size of the memory to allocate; `free` only receives a
pointer to the region.

```c
float *my_variables = malloc(sizeof(float) * 64);
free(my_variables);
```

---

## Showing Arguments

This program will output the number of arguments, then the arguments
themselves.

```c
#include <stdio.h>

int main(int argc, char** argv) {
  fprintf(stderr, "%d\n", argc);
  for (int i = 0; i < argc ; i++ ) {
    fprintf(stderr, "%s\n", argv[i]);
  }
  return 0;
}
```
