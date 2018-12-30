# spacetime-toolkit
A Python toolkit built with Sympy (A symbolic math library) for exploring the Einstein field equations. This library is a free utility which enhances users with the tools to quickly working out the tedius calculations involved in the Einstein field equations.

What does it do?
================

Who is it for?
==============
This library was written

Status
======
Currently this project is in a state of development but core functions are stable. Repo and code need cleaning.

How to use?
===========
Currently this project is in a state of development, however the core functionality appears stable and has passed each test. To demonstrate this software just run example.py

Prerequisites
=============
1.) Python
2.) Sympy

(You can install sympy with pip)

Running example.py
==================
Example.py is a good choice for someone new to the project becasue it demonstrates the entire functionality suite. Depending on the metric you use for inpute the calculation time may vary exponentially.

In the example you can see various spacetimes which are a primary argument.

    coordinate_set = [ x0, x1, x2, x3 ]
    mt = Metric(reissner_nordstrom_spacetime, coordinate_set)

To change the metric just swap it out for another one or build your own. Sympy appears quite rhobust!

Project Goals
=============

1.) For a given metric tensor and coordinate set, provide functions which compute all of the following quantities:
    Connection Coefficients
    Ricci tensor, 
    Ricci scalar, 
    Einstien tensor,
    Stress Tensor,
    Geodesic equations,
    Plotting velocities, orbits, geodesic paths.
    
2.) Print the previous terms in a clean and intuitive predefined format which bypasses the limitations imposed by sympy.

3.) Computing all geodesics equations for a given metric, coordinate set, parameterization type and initial conditions.

4.) Plotting any or all acceleration vectors, velocity vectors, position vectors for any or all spacelike,timelike and null geodesics.

5.) Provide visualization tools which can be configured to match any metric.

6.) Provide a configuration file which allows the user to customize the output profile for a given metric and coordinate set.

Project Purpose
===============
 1.) To provide code which demonstrates general relativity and can be studied.
 2.) To provide code which can be utalized by researchers or engineers.
 3.) To provide concrete numeric calculations directly from the symbolic form of the einstien field equations.
 4.) Provide context by integrating latex representations of the functions.

TODOs
=====
So much.. 

Timeline
========
Jan - Einstiens Field Equation + Geodesics
Feb - Plotting trajectories
Mar - Config file customizations.
