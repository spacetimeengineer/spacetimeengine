spacetime-toolkit
=================
A Python toolkit built using Sympy (A symbolic mathematics library) for exploring the Einstein field equations. This library is a free utility which enhances users with the tools for quickly working out the tedius formulas associated with solving the Einstein field equations. For any input metric tensor, any or all coefficients associated with the metric, connection, Riemann, Ricci, Einstein & stress-energy tensors can be computed. Run "example.py" to see for yourself.


Running example.py
==================
Example.py is a good choice for someone new to the project becasue it demonstrates the functionality suite. Depending on the metric you use for input, the compute time may vary exponentially. There are other metric solutions available for study! To change the metric just swap it out for another one or build your own. There are many metric examples to help you understand how to build input parameters if you are a researcher.

    $ python example.py

What does it do?
================
Currently this library provides functions which works out the following formulas. It requires a metric tensor for input and computes the stress-energy tensor along with all related quantities required to compute it. Currently the metric cannot be solved for a stress tensor input but that feature is greatly desired. The reason for this is that the computations are mainly based of differentiation rather than integration. Any help or advice on this is greatly appreciated.

The Einstein field equations

![equation](https://latex.codecogs.com/png.latex?%5Cinline%20%5Cdpi%7B100%7D%20%5Chuge%20G_%7B%5Cmu%20%5Cnu%20%7D&plus;%5CLambda%20g_%7B%5Cmu%20%5Cnu%20%7D%3D%7B%5Cfrac%20%7B8%5Cpi%20G%7D%7Bc%5E%7B4%7D%7D%7DT_%7B%5Cmu%20%5Cnu%20%7D)

The Einstein tensor

![equation](https://latex.codecogs.com/png.latex?%5Cinline%20%5Cdpi%7B100%7D%20%5Chuge%20G_%7B%5Cmu%20%5Cnu%20%7D%3DR_%7B%5Cmu%20%5Cnu%20%7D-%7B%5Ctfrac%20%7B1%7D%7B2%7D%7DRg_%7B%5Cmu%20%5Cnu%20%7D)

The Ricci tensor

![equation](https://latex.codecogs.com/png.latex?%5Cinline%20%5Cdpi%7B100%7D%20%5Chuge%20R_%7Bij%7D%20%3D%20%7BR%5Ek%7D_%7Bikj%7D)

![equation](https://latex.codecogs.com/png.latex?%5Cinline%20%5Cdpi%7B100%7D%20%5Chuge%20R%5E%5Crho%7B%7D_%7B%5Csigma%5Cmu%5Cnu%7D%20%3D%20%5Cpartial_%5Cmu%5CGamma%5E%5Crho%7B%7D_%7B%5Cnu%5Csigma%7D%20-%20%5Cpartial_%5Cnu%5CGamma%5E%5Crho%7B%7D_%7B%5Cmu%5Csigma%7D%20&plus;%20%5CGamma%5E%5Crho%7B%7D_%7B%5Cmu%5Clambda%7D%5CGamma%5E%5Clambda%7B%7D_%7B%5Cnu%5Csigma%7D%20-%20%5CGamma%5E%5Crho%7B%7D_%7B%5Cnu%5Clambda%7D%5CGamma%5E%5Clambda%7B%7D_%7B%5Cmu%5Csigma%7D)

![equation](https://latex.codecogs.com/png.latex?%5Cinline%20%5Cdpi%7B100%7D%20%5Chuge%20%5CGamma%20%5E%7Bi%7D%7B%7D_%7Bkl%7D%3D%7B%5Ctfrac%20%7B1%7D%7B2%7D%7Dg%5E%7Bim%7D%5Cleft%28%7B%5Cfrac%20%7B%5Cpartial%20g_%7Bmk%7D%7D%7B%5Cpartial%20x%5E%7Bl%7D%7D%7D&plus;%7B%5Cfrac%20%7B%5Cpartial%20g_%7Bml%7D%7D%7B%5Cpartial%20x%5E%7Bk%7D%7D%7D-%7B%5Cfrac%20%7B%5Cpartial%20g_%7Bkl%7D%7D%7B%5Cpartial%20x%5E%7Bm%7D%7D%7D%5Cright%29)
Currently, as seen in example.py, for a given metric solution of the form:

![equation](https://latex.codecogs.com/png.latex?%5Cinline%20%5Cdpi%7B100%7D%20%5Chuge%20%5CGamma%20_%7Bcab%7D%3D%7B%5Ctfrac%20%7B1%7D%7B2%7D%7D%5Cleft%28%7B%5Cfrac%20%7B%5Cpartial%20g_%7Bca%7D%7D%7B%5Cpartial%20x%5E%7Bb%7D%7D%7D&plus;%7B%5Cfrac%20%7B%5Cpartial%20g_%7Bcb%7D%7D%7B%5Cpartial%20x%5E%7Ba%7D%7D%7D-%7B%5Cfrac%20%7B%5Cpartial%20g_%7Bab%7D%7D%7B%5Cpartial%20x%5E%7Bc%7D%7D%7D%5Cright%29)

![equation](https://latex.codecogs.com/png.latex?%5Cinline%20%5Cdpi%7B100%7D%20%5Chuge%20%7B%5Cdisplaystyle%20R_%7Bik%5Cell%20m%7D%3D%7B%5Cfrac%20%7B1%7D%7B2%7D%7D%5Cleft%28%7B%5Cfrac%20%7B%5Cpartial%20%5E%7B2%7Dg_%7Bim%7D%7D%7B%5Cpartial%20x%5E%7Bk%7D%5Cpartial%20x%5E%7B%5Cell%20%7D%7D%7D&plus;%7B%5Cfrac%20%7B%5Cpartial%20%5E%7B2%7Dg_%7Bk%5Cell%20%7D%7D%7B%5Cpartial%20x%5E%7Bi%7D%5Cpartial%20x%5E%7Bm%7D%7D%7D-%7B%5Cfrac%20%7B%5Cpartial%20%5E%7B2%7Dg_%7Bi%5Cell%20%7D%7D%7B%5Cpartial%20x%5E%7Bk%7D%5Cpartial%20x%5E%7Bm%7D%7D%7D-%7B%5Cfrac%20%7B%5Cpartial%20%5E%7B2%7Dg_%7Bkm%7D%7D%7B%5Cpartial%20x%5E%7Bi%7D%5Cpartial%20x%5E%7B%5Cell%20%7D%7D%7D%5Cright%29&plus;g_%7Bnp%7D%5Cleft%28%5CGamma%20%5E%7Bn%7D%7B%7D_%7Bk%5Cell%20%7D%5CGamma%20%5E%7Bp%7D%7B%7D_%7Bim%7D-%5CGamma%20%5E%7Bn%7D%7B%7D_%7Bkm%7D%5CGamma%20%5E%7Bp%7D%7B%7D_%7Bi%5Cell%20%7D%5Cright%29%7D)

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


This object has functions which allow the user to get / (set soon ) all coefficients associated with the metric, connection, Riemann tensor, Ricci tensor, Einstein tensor and stress-energy-momentum tensor. There are many operations available for analyzing the input metric. For example to find the connection coefficients just run

    >> spacetime.list_connection_coefficients("udd")
    
    
    Connection coefficients (udd)
    =============================
           -1  
    Γ⁰₀₀ = ────
           2⋅x₀

    Γ⁰₀₁ = 0

    Γ⁰₀₂ = 0

    Γ⁰₀₃ = 0

    Γ⁰₁₀ = 0

                4        
               c ⋅x₀     
    Γ⁰₁₁ = ──────────────
                        2
           2⋅(2⋅G⋅M - 1) 

    ...

Will print out all connection coefficients with an up-down-down summation index configuration which makes reference to the Christoffel symbols of the second kind. Anyone familiar with tensor calculus and the Einstein summation conventions should understand what I am talking about. Another example:
    
    >> spacetime.list_ricci_coefficients("dd")
    
    Ricci curvature tensor coefficients (dd)
    ========================================

    R₀₀ = 0

            1  
    R₀₁ = ─────
          x₀⋅x₁

    R₀₂ = 0

    R₀₃ = 0

            1  
    R₁₀ = ─────
          x₀⋅x₁

    R₁₁ = 0

    R₁₂ = 0

    R₁₃ = 0

    R₂₀ = 0

    R₂₁ = 0

                   2       
          2⋅G⋅M + c ⋅x₀ - 1
    R₂₂ = ─────────────────
                 2         
                c ⋅x₀      

    R₂₃ = 0

    R₃₀ = 0

    R₃₁ = 0

    R₃₂ = 0

          ⎛         2       ⎞    2    
          ⎝2⋅G⋅M + c ⋅x₀ - 1⎠⋅sin (x₂)
    R₃₃ = ────────────────────────────
                      2               
                     c ⋅x₀            


Who is it for?
==============
This library was written for researchers and students primarily however the goals of open source development community and the space industry will continue to influence the direction of this project. I am interested in a more general purpose library. I think Sympy tools are powerful becasue allows the the open source community rather than pure acedemia to run the narrative.

Status
======
Currently this project is in a state of development but core functions are stable. Repo and code need cleaning.

Prerequisites
=============
1.) Python

    $ sudo apt install python3-pip
    
2.) Sympy (Symbolic mathematics library written in python)

    $ pip install sympy

