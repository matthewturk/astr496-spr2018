---
title: Lecture 14
layout: lecture
slideOptions:
  transition: none
  theme: white
  center: false
---

# Computing in Astronomy<!-- .element: class="centered" -->
### Matthew Turk<!-- .element: class="righted" -->
### Spring 2018<!-- .element: class="righted" -->
### Lecture 14 <!-- .element: class="righted" -->

---

## This Time

 * Arrays and Pointers in C
 * Flow control in C
 * Structs and memory
 * Comparisons between C and Python

---

## Assignment Number Two

Big change in plans: you will be able, but not required, to work in groups of
up to four.  This assignment is hard.

The number of people in your group *will* affect your grading scale.

Furthermore, you must detail in your writeup the process of collaboration.

https://classroom.github.com/g/Rc7zMJ64

---

## Arrays and Pointers

For the purposes of this class, we will be using these terms somewhat
interchangeably, with the principal distinction being one of _intent_.

We think of an array as a sequence of identical data types in memory:

```
item1
item2
item3
item4
item5
```

These are laid out linearly, and there may be gaps if the items are not
multiples of 32 bits in size.

---

## Arrays and Pointers 2

The first element in this array exists at a memory location.  We know that the
space between them can be calculated deterministically.

For instance, if we know the position of `item1` and we know that the items are
64 bits in size (with no additional padding) we can calculate that `item2` is
located at `item1` plus 64 bits.

If we have a pointer to `item1`, we can thus increment that pointer by 64 bits
to point to `item2`.  These two notations will produce the same results:

```c
item* item1 = &first_item;
item1_inc = item1 + 1;
item1_arr = item1[1];
```

Why?

---

## Flow Control in C

Last time, we learned a bit of the basics of using C.  We will today learn
three essential flow control methods:

 * `for` looping
 * `if`, `else if` and `else`
 * `switch`

We're going to skip learning `while` for now.

---

## Flow Control in C: for loops

A `for` loop in C is composed of an initialization step, an evaluation step
(when this is no longer true, the loop breaks) and an update step.  This takes
on this syntax:

```c
for (initializer ; condition ; update) {
   ...
}
```

Within the initializer and the update, we can specify multiple steps to be
taken.  These are separated by commas.

Why might we use this?

---

## Flow Control in C: Pointers in Loops

```c
for (int count = 0, item_type* item = &first_item;
     item != NULL;
     item++, count++) {
 ...
}
```

What does this do?

---

## Flow Control: ifs

We can utilize a conditional statement with one or more possibilities like so:

```c
if (condition1) {
} else if (condition2) {
 ...

} else {
 ...
}
```

Note that we need these to be boolean conditions; we can use the boolean
operators `&&` (and), `||` (or) and `!` (not) to chain multiple conditions or 

---

## Structs and Memory

In C, a collection of variables can be defined in a `struct` like so:

```c
struct name {
  float a;
  int b;
}
```

In this case, there will be a single object `name` that is composed of a
floating point value member `a` and an integer member `b`.  

We won't be talking about unions because unions are for if you feel like you're
really clever and I really just don't feel like that today.

---

## Structs and Type Definitions

If you intend to use a struct multiple times you will want to utilize a
`typedef` declaration to simplify access to that type of object.  (Note the
distinction here between a specific object and type that defines the object.)

```c
typedef struct name {
  float a;
  int b;
} type_name;
```

Now, we can define a new variable as being of type `type_name`:

```c
type_name this_object;
```

The name of our variable is `this_object`, in this case.

---

## Struct Sizes

The size of a struct is determined by two factors: the alignment of the
structure in memory, and the sum total of the items within the struct.

The process of "struct-packing" for memory is one that has received a
considerable amount of attention, but the main message to take away is that it
is not a 100% safe assumption that `sizeof(struct_type)` is equal to the sizes
of the member types.

---

## Struct Allocation

A corollary to this is that it is not necessarily true that if you allocate an
array of `n_items` of `struct_type` using `calloc` that it will be the same
size as `sizeof(struct_type) * n_items`.

(We have to remain aligned!)

---

## Casting: Avada Kedavra

Let's talk about one of the single most dangerous things you can do in C:
casting.

I can make one object look like another:

```c
int k = 5;
float j = (float)k;
```

This makes my integer into a floating point.  I can do this with pointers, too.

```c
int* k = &my_value;
float* j = (float*) k;
```

But what if the types are not the same size?

---

## Opaque Data

This is often used to pass things around when we don't necessarily know what
their type will be until later -- if we have a container data structure, for
instance.

```c
void *opaque = (void*) my_pointer;
```

We can now pass this around, under the assumption that at some later point
we'll use it correctly.

**This is pretty dangerous, but cool and useful.**

---

## Python versus C

Let's build a loop in C and a loop in Python, and let's figure out what happens
at each step.

```python
s = 0
for i in range(1000):
  for j in range(1000):
    s += i * j
```

```c
int s = 0;
for (int i = 0; i < 1000; i++) {
  for (int j = 0; j < 1000; j++) {
    s += i * j;
  }
}
```

What happens if we turn this into an array?
