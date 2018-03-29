---
title: Lecture 17
layout: lecture
slideOptions:
  transition: none
  theme: white
  center: false
---

# Computing in Astronomy<!-- .element: class="centered" -->
### Matthew Turk<!-- .element: class="righted" -->
### Spring 2018<!-- .element: class="righted" -->
### Lecture 18 <!-- .element: class="righted" -->

---

## This Time

 * A Bit More About Trees
 * "Databases"
 * Navigating SQL
 * Navigating Pandas

---

## Trees

We haven't really talked about recursion, or about class composition.

Let's talk about this for trees.

---

## A Basic Binary Tree

For our trees, we need to know what constitutes a "leaf" node (where we find
data) and what constitutes a "branch node" (which exists to guide decision
making).

When we construct a tree, we are placing things according to some decision
making process, and when we find things in a tree, we use that same decision
making process to figure out where to look for them.

---

## A Basic Binary Tree

Think of this as a Choose Your Own Adventure novel.

 * If you want to go left, turn to page 36.
 * If you want to go right, turn to page 51.

You keep doing this until you get to an ending.

---

## Implementing This

Let's implement a Choose Your Own Adventure.  We'll use classes for each page.

```python
class Page:
    def __init__(self, text):
        self.text = text
        self.choices = []

    def add_choice(self, choice_name, page):
        self.choices.append((choice_name, page))

    def make_choice(self):
        print(self.text)
        if len(self.choices) == 0:
            print("You have died.")
            return
        else:
            for i, c in enumerate(self.choices):
                print("{}: {}".format(i, c[0]))
            answer = int(input("Which do you want?"))
            self.choices[answer][1].make_choice()
```

---

## Implementing

```python
p1 = Page("You find yourself in a classroom.")
p2 = Page("You're outside in the hallway.")
p3 = Page("The professor calls on you.")
p4 = Page("It's raining and your feet are cold.")
p5 = Page("You answer correctly.")
p6 = Page("Wrong answer!")

p1.add_choice("Leave?", p3)
p1.add_choice("Stay inside?", p3)

p2.add_choice("Go in the classroom?", p1)
p2.add_choice("Go outside?", p4)

p3.add_choice("Guess?", p5)
p3.add_choice("Guess!", p6)
```

---

## Automating This

We constructed this by inserting new leaves into it.  We made decisions based
on our choices.

**NOTE**: This is cyclic.  That means we can see things we've seen before!
Your trees will not be.

---

## Finding Things with Trees

Now, let's try looking at this from the perspective of inserting values and
then finding them.

Let's implement our searching game using this system, and instead of choosing
our index interactively, we simply choose each time based on the odd or even
length of the text?

---

## Let's Implement a Searching Tree

Now, let's extend this to spatial locations.

We need to identify our "refinement" criteria, and our searching and sorting
order.

---

## "Databases"

* http://use.yt/upload/72ce3a25
* http://use.yt/upload/df738fe6

We will be using "databases" in two different forms; we will not (yet) be
handling joins.

Download and gunzip these two files: `asu.tsv` and `hipparcos.db`.

---

## SQL: Terminology

SQL, or Structured Query Language, is a method of interacting with databases.
We will use these terms for our discussion:

 * "column": an attribute, where all are of the same type
 * "row": an entry, or a data value, with multiple "columns"
 * "table": a collection of rows
 * "schema": the definition of a row
 * "index": a method of speeding access
 * "database": one or more tables that are related

---

## SQL: Verbs and Usage

These are the commands you will need to utilize:

 * `SELECT` and `FROM` are the means of getting row information back from a SQL
   database
 * `WHERE` is used to provide conditions for selection
 * We can change our results using `DISTINCT`, `ORDER BY`, etc
 * We can aggregate with thing like `MAX()`

---

## SQL


We'll use SQLite, and we will utilize a handful of operations.  Start `sqlite3`
with this command:

```bash
sqlite3 hipparcos.db
```

Try out a bit of experimentation by looking at the `.tables` command:

```
sqlite> .tables
```

We have one table, `objects`.

---

## Exercise: Explore

Let's explore this dataset a bit.  First, I will show some basics, and then you
will do some sample problems.

 * Selecting data
 * Aggregating data
 * How would we visualize this?

---

## Pandas

Pandas is a convenient way to interact with data that is of the type we're
handling here.

We will load our data in using pandas:

```
df = pd.read_csv("asu.tsv", delimiter=";", comment="#")
```
