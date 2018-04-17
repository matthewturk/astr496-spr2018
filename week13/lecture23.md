---
title: Lecture 23
layout: lecture
slideOptions:
  transition: none
  theme: white
  center: false
---

# Computing in Astronomy<!-- .element: class="centered" -->
### Matthew Turk<!-- .element: class="righted" -->
### Spring 2018<!-- .element: class="righted" -->
### Lecture 23 <!-- .element: class="righted" -->

---

## Last Time

 * Chemistry and ODEs
 * Interpolation
 * Temperatures and other constraints

---

## This Time

 * A Fun Diversion
 * Constructing an ODE chemistry solver

---

## Talk Today!

Dr. Kathryn Clancy, from the Department of Anthropology at the U of I will be
speaking at the Astronomy Department colloquium next Tuesday (April 17). She
will give her talk at 3:45 in room 134, with refreshments served at 3:30 in
room 222.

Title: "Gender harassment in science: is it just me?"

---

## A Fun Diversion

Let's talk about Web Assembly.

Go to [webassembly.studio](https://webassembly.studio/)

 * How?
 * Why?
 * When?

---

## Chemistry ODEs

We have built out some basic systems for ODEs in Python.

Today, we will break into smaller groups and continue this trend.

---

## ODE Solving for Real in SciPy

Today, for real, we will be solving ODEs using `scipy.integrate.ode`.  Set
up the initial code:

```
N = 1024
T = np.logspace(1, 8, N)
T_eV = T / 11605.
log_T_eV = np.log(T_eV)
k1 = np.exp(-32.71396786375
          + 13.53655609057*log_T_eV
          - 5.739328757388*log_T_eV**2 
          + 1.563154982022*log_T_eV**3
          - 0.2877056004391*log_T_eV**4
          + 0.03482559773736999*log_T_eV**5
          - 0.00263197617559*log_T_eV**6
          + 0.0001119543953861*log_T_eV**7
          - 2.039149852002e-6*log_T_eV**8)
k2 = 4.881357e-6*T**(-1.5)* (1.+1.14813e2 * T**(-0.407))**(-2.242)
```

---

## ODE Solving for Real in SciPy

We now need to construct a right-hand side updater.  This requires that we
understand our state vector.  We will solve the ionization and recombination
problem of atomic hydrogen.

What should our state vector be?  What are the components that we can vary?

---

## ODE Solving using `ode`

We will be using the `ode` class in `scipy.integrate`.  This is an
object-oriented method that allows you to specify a number of characteristics
about the system while you solve.

```
integrator = scipy.integrate.ode( f , jac = None )
integrator.set_initial_value( initial_state_vector )
integrator.set_f_params( ... )
integrator.set_integrator( "integrator_name" )
integrator.integrate( next_t )
```

Let's now set this up for our simple problem.

---

## Abstracting This

What are the assumptions we made here?

How can we change them?

How can we make this easier to use?



