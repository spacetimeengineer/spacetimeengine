# spacetime-toolkit
A Python toolkit built using Sympy (A symbolic mathematics library) for exploring the Einstein field equations. This library is a free utility which enhances users with the tools for quickly working out the tedius calculations involved in the Einstein field equations.

What does it do?
================

Currently, for a given metric solution of the form:

    schwarzschild_spacetime = Matrix([
                                         [ ((1 - 2 * G * M) / ( x0 * c**2 )), 0, 0, 0 ], 
                                         [ 0, - ((1 - 2 * G * M) / ( x0 * c**2 ))**(-1), 0, 0 ], 
                                         [ 0, 0, - x1**2, 0 ], 
                                         [ 0, 0, 0, - x1**2 * sin(x2)**2 ]
                                     ]) 

and a coordinate set to define the metric in terms of:

    coordinate_set = [ x0, x1, x2, x3 ]
    
which in this case references the spherical coordinate system: [ x0, x1, x2, x3 ] --> [ t, r, θ, φ ]
It list all coefficients associated with the metric, connection, riemann tensor, ricci tensor, einstien tensor and stress energy tensor.


Who is it for?
==============
This library was written for researchers and students primarily however the goals of open source development community and the space industry continue to influence the direction of this project. 

Status
======
Currently this project is in a state of development but core functions are stable. Repo and code need cleaning.

How to use?
===========
Currently this project is in a state of development, however the core functionality appears stable and has passed each test. To demonstrate this software just run example.py

Prerequisites
=============
1.) Python
2.) Sympy (You can install sympy with pip)

Running example.py
==================
Example.py is a good choice for someone new to the project becasue it demonstrates the entire functionality suite. Depending on the metric you use for inpute the calculation time may vary exponentially.

In the example you can see various spacetimes which are a primary argument.

    coordinate_set = [ x0, x1, x2, x3 ]
    mt = Metric(reissner_nordstrom_spacetime, coordinate_set)

To change the metric just swap it out for another one or build your own.
