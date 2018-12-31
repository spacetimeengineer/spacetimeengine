# spacetime-toolkit
A Python toolkit built using Sympy (A symbolic mathematics library) for exploring the Einstein field equations. This library is a free utility which enhances users with the ability to quickly work out the tedius calculations involved associated with the Einstein field equations. For any input metric tensor, all the Connection, Riemann, Ricci, Einsteinn & Stress-Ennergy coefficients can be computed. Run "example.py" to see for yourself

What does it do?
================

Currently, as seen in example.py, for a given metric solution of the form:

    >> schwarzschild_spacetime = Matrix([
                                         [ ((1 - 2 * G * M) / ( x0 * c**2 )), 0, 0, 0 ], 
                                         [ 0, - ((1 - 2 * G * M) / ( x0 * c**2 ))**(-1), 0, 0 ], 
                                         [ 0, 0, - x1**2, 0 ], 
                                         [ 0, 0, 0, - x1**2 * sin(x2)**2 ]
                                     ]) 

and a coordinate set to define the metric in terms of:

    >> coordinate_set = [ x0, x1, x2, x3 ]
    
( which in this case references the spherical coordinate system: [ x0, x1, x2, x3 ] --> [ t, r, θ, φ ] ) will serve as input parameters for the Spacetime object;


    >> spacetime = SpaceTime(schwarzschild_spacetime, coordinate_set)


This object has functions list all coefficients associated with the metric, connection, Riemann tensor, Ricci tensor, Einstein tensor and stress-energy-momentum tensor. There are many operations available for analyzing the input metric. For example to find the connection coefficients just run

    >> spacetime.list_connection_coefficients("udd")

Will print out all connection coefficients with an up-down-down summation index configuration which makes reference to the Christoffel symbols of the second kind.


Who is it for?
==============
This library was written for researchers and students primarily however the goals of open source development community and the space industry continue to influence the direction of this project. 

Status
======
Currently this project is in a state of development but core functions are stable. Repo and code need cleaning.

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
