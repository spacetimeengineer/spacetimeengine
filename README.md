
# spacetime-toolkit
A Python toolkit built using Sympy (A symbolic mathematics library) for exploring the Einstein field equations. This library is a free utility which enhances users with the tools for quickly working out the tedius formulas associated with solving the Einstein field equations. For any input metric tensor, any or all coefficients associated with the metric, connection, Riemann, Ricci, Einstein & stress-energy tensors can be computed. Run "example.py" to see for yourself


Running example.py
==================
Example.py is a good choice for someone new to the project becasue it demonstrates the functionality suite. Depending on the metric you use for input, the compute time may vary exponentially. To change the metric just swap it out for another one or build your own. There are many metric examples to help you understand how to build input parameters if you are a researcher.

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

    Γ⁰₁₂ = 0

    Γ⁰₁₃ = 0

    Γ⁰₂₀ = 0

    Γ⁰₂₁ = 0

    Γ⁰₂₂ = 0

    Γ⁰₂₃ = 0

    Γ⁰₃₀ = 0

    Γ⁰₃₁ = 0

    Γ⁰₃₂ = 0

    Γ⁰₃₃ = 0

    Γ¹₀₀ = 0

            1  
    Γ¹₀₁ = ────
           2⋅x₀

    Γ¹₀₂ = 0

    Γ¹₀₃ = 0

            1  
    Γ¹₁₀ = ────
           2⋅x₀

    Γ¹₁₁ = 0

    Γ¹₁₂ = 0

    Γ¹₁₃ = 0

    Γ¹₂₀ = 0

    Γ¹₂₁ = 0

           x₁⋅(2⋅G⋅M - 1)
    Γ¹₂₂ = ──────────────
                2        
               c ⋅x₀     

    Γ¹₂₃ = 0

    Γ¹₃₀ = 0

    Γ¹₃₁ = 0

    Γ¹₃₂ = 0

                             2    
           x₁⋅(2⋅G⋅M - 1)⋅sin (x₂)
    Γ¹₃₃ = ───────────────────────
                     2            
                    c ⋅x₀         

    Γ²₀₀ = 0

    Γ²₀₁ = 0

    Γ²₀₂ = 0

    Γ²₀₃ = 0

    Γ²₁₀ = 0

    Γ²₁₁ = 0

           1 
    Γ²₁₂ = ──
           x₁

    Γ²₁₃ = 0

    Γ²₂₀ = 0

           1 
    Γ²₂₁ = ──
           x₁

    Γ²₂₂ = 0

    Γ²₂₃ = 0

    Γ²₃₀ = 0

    Γ²₃₁ = 0

    Γ²₃₂ = 0

           -sin(2⋅x₂) 
    Γ²₃₃ = ───────────
                2     

    Γ³₀₀ = 0

    Γ³₀₁ = 0

    Γ³₀₂ = 0

    Γ³₀₃ = 0

    Γ³₁₀ = 0

    Γ³₁₁ = 0

    Γ³₁₂ = 0

           1 
    Γ³₁₃ = ──
           x₁

    Γ³₂₀ = 0

    Γ³₂₁ = 0

    Γ³₂₂ = 0

              1   
    Γ³₂₃ = ───────
           tan(x₂)

    Γ³₃₀ = 0

           1 
    Γ³₃₁ = ──
           x₁

              1   
    Γ³₃₂ = ───────
           tan(x₂)

    Γ³₃₃ = 0





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

