spacetime-engine (beta)
========================
A Python toolkit built using Sympy (A symbolic mathematics library) for exploring the Einstein field equations. This library is a free utility which enhances users with the tools for working out the various coefficients associated for a given solution to the Einstein field equations:

![equation](https://latex.codecogs.com/png.latex?%5Cdpi%7B100%7D%20%5Chuge%20G_%7B%5Cmu%5Cnu%7D%20&plus;%20%5CLambda%20g_%7B%5Cmu%5Cnu%7D%20%3D%20%5Cfrac%7B8%5Cpi%20G%7D%7Bc%5E4%7DT_%7B%5Cmu%5Cnu%7D)

Installation
============
1.) Install Python

    $ sudo apt install python3-pip
    
2.) Install Sympy (Symbolic mathematics library written in python)

    $ pip install sympy
    
3.) Clone repository

    $ git clone https://github.com/spacetimeengineer/spacetime-engine

4.) Enter directory

    $ cd spacetime-engine

Suggested Use
=============
If you are a student or researcher and find yourself reading a publication based in General Relativity which provides metric values then this utility can be used for working out the curvature coefficients that associate with the metric. This can be helpful as you read through the publication since you will be able to cross reference the information provided by the toolkit and the publication for richer analysis (This is why I developed it originally).

Running example.py
==================
Example.py is a good choice for someone new to the project becasue it demonstrates the functionality suite. Depending on the metric you use for input, the compute time may vary exponentially. There are other metric solutions available for study! To change the metric just swap it out for another one or build your own. There are many metric examples to help you understand how to build input parameters.

    $ python example.py

Using the spacetime-engine
==========================

First, import Sympy and the SpaceTime class.
    
    >>> from sympy import *
    >>> from spacetime import SpaceTime
    
Next, define the mathematical symbols required for expressing a given solution. In this example we will be using the Schwarzschild vacuum solution.
    
    >>>     G = Symbol('G')
    >>>     M = Symbol('M')
    >>>     c = Symbol('c')
    >>>     t = Symbol('t')
    >>>     r = Symbol('r')
    >>>     th = Symbol('theta')
    >>>     ph = Symbol('phi')

Next, define a coordinate set which the metric will define in terms of. This will serve as one of two input parameters for the SpaceTime object.

    >>> spherical_coordinate_set = [ t, r, th, ph ]
    

[Metric Tensor](https://en.wikipedia.org/wiki/Metric_tensor)
===============

Generally any metric solution to the Einstein field equations will be packaged into a geometric object known as the Metric Tensor. The metric tensor is often represented in matrix form and the spacetime-toolkit prefers this representation.

![equation](https://latex.codecogs.com/png.latex?%5Cdpi%7B100%7D%20%5Chuge%20%5C%3A%5C%3A%20g_%7B%5Cmu%5Cnu%7D%3D%5Cleft%20%5B%20%5Cbegin%7Barray%7D%7Bccccc%7D%20g_%7B00%7D%20%26%20g_%7B01%7D%20%26%20g_%7B02%7D%20%26%20g_%7B03%7D%5C%5C%20g_%7B10%7D%20%26%20g_%7B11%7D%20%26%20g_%7B12%7D%20%26%20g_%7B13%7D%5C%5C%20g_%7B20%7D%20%26%20g_%7B21%7D%20%26%20g_%7B22%7D%20%26%20g_%7B23%7D%5C%5C%20g_%7B30%7D%20%26%20g_%7B31%7D%20%26%20g_%7B32%7D%20%26%20g_%7B33%7D%20%5Cend%7Barray%7D%20%5Cright%20%5D)

The spacetime-toolkit employs the Sympy 'Matrix' object for packaging the metric tensor and it serves as one of two input parameters for constructing a 'SpaceTime' object.

    >>> schwarzschild_spacetime = Matrix([    
                                            [ (1-(2*G*M)/(r*c**2)), 0, 0, 0 ], 
                                            [ 0, - (1-(2*G*M)/(r*c**2))**(-1), 0, 0 ], 
                                            [ 0, 0, - r**2, 0 ], 
                                            [ 0, 0, 0, - r**2*sin(th)**2 ]
                                        ])
                                        
To construct a 'SpaceTime' object just execute the below command and consider the solution given since high complexity solutions can take exponentially longer to process.

    >>> spacetime = SpaceTime(schwarzschild_spacetime, spherical_coordinate_set)

After a few moments (if you are using the Schwarzschild solution) you will be able to call various coefficients which associate with the given spacetime.

[Stress-Energy-Momentum Tensor](https://en.wikipedia.org/wiki/Stress%E2%80%93energy_tensor)
=============================
The Einstein field equations describe the equivilence of space-time curvature and mass-energy. The mass-energy is represented by the coefficents encompassed within the stress-energy-momentum tensor denoted by T_{\mu\nu}. The cosmological constant denoted by Lambda is treated as an input parameter and represents the dark energy thought to be responsble for the accellerated expansion of the cosmos.

![equation](https://latex.codecogs.com/png.latex?%5Cdpi%7B100%7D%20%5Chuge%20T_%7B%5Cmu%20%5Cnu%20%7D%3D%7B%5Cfrac%20%7Bc%5E%7B4%7D%7D%7B8%5Cpi%20G%7D%7D%5Cleft%20%28%20G_%7B%5Cmu%20%5Cnu%20%7D&plus;%5CLambda%20g_%7B%5Cmu%20%5Cnu%20%7D%20%5Cright%20%29)


    >>> cosmological_constant = 0
    >>> mu = 0 # (dt)
    >>> nu = 1 # (dr)
    >>> index_config = "dd"
    >>> spacetime.print_stress_energy_coefficient(index_config, mu, nu, cosmological_constant)
    
    0

Since the Schwarzschild solution is a vacuum solution, any stress energy coefficient will yield a zero.

[The Einstein Tensor](https://en.wikipedia.org/wiki/Einstein_tensor)
=====================
The Einstein tensor denoted by $G_{\my\nu}$ desribes the curvature of spacetime and allows the Einstein field equations to be written in concise form.

![equation](https://latex.codecogs.com/png.latex?%5Cinline%20%5Cdpi%7B100%7D%20%5Chuge%20G_%7B%5Cmu%20%5Cnu%20%7D%3DR_%7B%5Cmu%20%5Cnu%20%7D-%7B%5Ctfrac%20%7B1%7D%7B2%7D%7DRg_%7B%5Cmu%20%5Cnu%20%7D)

    >>> mu = 0 # (dt)
    >>> nu = 1 # (dr)
    >>> index_config = "dd"
    >>> spacetime.print_einstein_coefficient(index_config, mu, nu)
    
    G₀₁ = 0


[Ricci Tensor](https://en.wikipedia.org/wiki/Ricci_curvature)
===============
![equation](https://latex.codecogs.com/png.latex?%5Cinline%20%5Cdpi%7B100%7D%20%5Chuge%20R_%7Bij%7D%20%3D%20%7BR%5Ek%7D_%7Bikj%7D)

    >>> mu = 0 # (dt)
    >>> nu = 1 # (dr)
    >>> index_config = "dd"
    >>> pprint(spacetime.get_ricci_coefficient(index_config, 3, 2))
    
    R₃₂ = 0


[Riemann Tensor](https://en.wikipedia.org/wiki/Riemann_curvature_tensor)
========================
![equation](https://latex.codecogs.com/png.latex?%5Cinline%20%5Cdpi%7B100%7D%20%5Chuge%20R%5E%5Crho%7B%7D_%7B%5Csigma%5Cmu%5Cnu%7D%20%3D%20%5Cpartial_%5Cmu%5CGamma%5E%5Crho%7B%7D_%7B%5Cnu%5Csigma%7D%20-%20%5Cpartial_%5Cnu%5CGamma%5E%5Crho%7B%7D_%7B%5Cmu%5Csigma%7D%20&plus;%20%5CGamma%5E%5Crho%7B%7D_%7B%5Cmu%5Clambda%7D%5CGamma%5E%5Clambda%7B%7D_%7B%5Cnu%5Csigma%7D%20-%20%5CGamma%5E%5Crho%7B%7D_%7B%5Cnu%5Clambda%7D%5CGamma%5E%5Clambda%7B%7D_%7B%5Cmu%5Csigma%7D)


    >>> index_config = "uddd"
    >>> spacetime.print_reimann_coefficient(index_config, 3, 2, 2, 3)
    
            -2⋅G⋅M 
    R³₂₂₃ = ───────
              2    
             c ⋅x₁ 

![equation](https://latex.codecogs.com/png.latex?%5Cinline%20%5Cdpi%7B100%7D%20%5Chuge%20%7B%5Cdisplaystyle%20R_%7Bik%5Cell%20m%7D%3D%7B%5Cfrac%20%7B1%7D%7B2%7D%7D%5Cleft%28%7B%5Cfrac%20%7B%5Cpartial%20%5E%7B2%7Dg_%7Bim%7D%7D%7B%5Cpartial%20x%5E%7Bk%7D%5Cpartial%20x%5E%7B%5Cell%20%7D%7D%7D&plus;%7B%5Cfrac%20%7B%5Cpartial%20%5E%7B2%7Dg_%7Bk%5Cell%20%7D%7D%7B%5Cpartial%20x%5E%7Bi%7D%5Cpartial%20x%5E%7Bm%7D%7D%7D-%7B%5Cfrac%20%7B%5Cpartial%20%5E%7B2%7Dg_%7Bi%5Cell%20%7D%7D%7B%5Cpartial%20x%5E%7Bk%7D%5Cpartial%20x%5E%7Bm%7D%7D%7D-%7B%5Cfrac%20%7B%5Cpartial%20%5E%7B2%7Dg_%7Bkm%7D%7D%7B%5Cpartial%20x%5E%7Bi%7D%5Cpartial%20x%5E%7B%5Cell%20%7D%7D%7D%5Cright%29&plus;g_%7Bnp%7D%5Cleft%28%5CGamma%20%5E%7Bn%7D%7B%7D_%7Bk%5Cell%20%7D%5CGamma%20%5E%7Bp%7D%7B%7D_%7Bim%7D-%5CGamma%20%5E%7Bn%7D%7B%7D_%7Bkm%7D%5CGamma%20%5E%7Bp%7D%7B%7D_%7Bi%5Cell%20%7D%5Cright%29%7D)

[Christoffel symbols of the First Kind](https://en.wikipedia.org/wiki/Christoffel_symbols)
=======================================

The connection coefficients or 'Christoffel symbol' are an array of numbers which represent the metric connection. The metric connection can be used to measure distances along curved manifolds. In General Relativity, the metric connection actually identifies the meaning of the gravitational field and can be used to track trajectories through spacetime.

![equation](https://latex.codecogs.com/png.latex?%5Cinline%20%5Cdpi%7B100%7D%20%5Chuge%20%5CGamma%20_%7Bcab%7D%3D%7B%5Ctfrac%20%7B1%7D%7B2%7D%7D%5Cleft%28%7B%5Cfrac%20%7B%5Cpartial%20g_%7Bca%7D%7D%7B%5Cpartial%20x%5E%7Bb%7D%7D%7D&plus;%7B%5Cfrac%20%7B%5Cpartial%20g_%7Bcb%7D%7D%7B%5Cpartial%20x%5E%7Ba%7D%7D%7D-%7B%5Cfrac%20%7B%5Cpartial%20g_%7Bab%7D%7D%7B%5Cpartial%20x%5E%7Bc%7D%7D%7D%5Cright%29)


[Christoffel symbols of the Second Kind](https://en.wikipedia.org/wiki/Christoffel_symbols)
=======================================

![equation](https://latex.codecogs.com/png.latex?%5Cinline%20%5Cdpi%7B100%7D%20%5Chuge%20%5CGamma%20%5E%7Bi%7D%7B%7D_%7Bkl%7D%3D%7B%5Ctfrac%20%7B1%7D%7B2%7D%7Dg%5E%7Bim%7D%5Cleft%28%7B%5Cfrac%20%7B%5Cpartial%20g_%7Bmk%7D%7D%7B%5Cpartial%20x%5E%7Bl%7D%7D%7D&plus;%7B%5Cfrac%20%7B%5Cpartial%20g_%7Bml%7D%7D%7B%5Cpartial%20x%5E%7Bk%7D%7D%7D-%7B%5Cfrac%20%7B%5Cpartial%20g_%7Bkl%7D%7D%7B%5Cpartial%20x%5E%7Bm%7D%7D%7D%5Cright%29)

    >>> index_config = "udd"
    >>> spacetime.print_connection_coefficient(index_config, 1, 3, 3)

           ⎛         2   ⎞    2    
           ⎝2⋅G⋅M - c ⋅x₁⎠⋅sin (x₂)
    Γ¹₃₃ = ────────────────────────
                       2           
                      c            

[Weyl Tensor](https://en.wikipedia.org/wiki/Weyl_tensor)
=============
![equation](https://latex.codecogs.com/png.latex?%5Cdpi%7B100%7D%20%5Chuge%20%7B%5Cdisplaystyle%20C_%7Bik%5Cell%20m%7D%3DR_%7Bik%5Cell%20m%7D&plus;%7B%5Cfrac%20%7B1%7D%7Bn-2%7D%7D%5Cleft%28R_%7Bim%7Dg_%7Bk%5Cell%20%7D-R_%7Bi%5Cell%20%7Dg_%7Bkm%7D&plus;R_%7Bk%5Cell%20%7Dg_%7Bim%7D-R_%7Bkm%7Dg_%7Bi%5Cell%20%7D%5Cright%29&plus;%7B%5Cfrac%20%7B1%7D%7B%28n-1%29%28n-2%29%7D%7DR%5Cleft%28g_%7Bi%5Cell%20%7Dg_%7Bkm%7D-g_%7Bim%7Dg_%7Bk%5Cell%20%7D%5Cright%29%2C%7D)

    >>> index_config = "dddd"
    >>> spacetime.print_weyl_coefficient(index_config, 3, 2, 2, 3)

                       2   
            2⋅G⋅M⋅r⋅sin (θ)
    C₃₂₂₃ = ───────────────
                    2      
                   c      
