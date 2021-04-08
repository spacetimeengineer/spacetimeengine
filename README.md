![alt text](https://github.com/spacetimeengineer/spacetimeengine/blob/master/resources/spacetimeengine_logo.png)

A Python utility built on Sympy (A symbolic mathematics library) which will analyze any given metric solution to the Einstein field equations. 

![equation](https://latex.codecogs.com/png.latex?%5Cdpi%7B100%7D%20%5Chuge%20G_%7B%5Cmu%5Cnu%7D%20&plus;%20%5CLambda%20g_%7B%5Cmu%5Cnu%7D%20%3D%20%5Cfrac%7B8%5Cpi%20G%7D%7Bc%5E4%7DT_%7B%5Cmu%5Cnu%7D)

Prerequisites (Linux)
=====================

1.) Install Python3

    $ sudo apt install python3

2.) Install pip3

    $ sudo apt install python3-pip

3.) Install git

    $ sudo apt-get install git
    
Prerequisites (MacOS)
=====================
  
1.) Install homebrew  
    
    $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" brew doctor
    
2.) Set python as an enviornmental varible. 

    $ export PATH="/usr/local/opt/python/libexec/bin:$PATH"
    
2.) Install git

    $ brew install git
    
3.) Install python3 and pip3 (https://docs.python-guide.org/starting/install3/osx/)

    $ brew install python3
    $ brew postinstall python3
    
Prerequisites (Windows)
=======================
1.) Install Python3 & pip3

    Navigate to https://www.python.org/downloads/
    
3.) Install git

    Navigate to https://gitforwindows.org/
    
Installation with pip3
======================

1.) Install with pip3

    $ pip3 install spacetimeengine    
    
2.) Enter python shell

    $ python3
    
3.) Import spacetimeengine

    >> from spacetimeengine import *
    
4.) Create a SpaceTime object which describes the Schwarzschild spacetime

    >> schwarzschild_spacetime = SpaceTime(Solution().schwarzschild())
    
5.) Enjoy watching the coefficients get computed.

Installation with git
=====================

1.) Clone repository

    $ git clone https://github.com/spacetimeengineer/spacetimeengine

2.) Enter directory

    $ cd spacetimeengine/spacetimeengine/samples
    
3.) Run example.py

    $ python3 example.py

Suggested Use
=============
If you are a student or researcher, and you find yourself reading a publication based in General Relativity which provides metric solutions, then this utility can be used for working out the curvature coefficients which associate with the solution provided by the user. This can be a helpful utility as you read through the literature because you will be able to cross-reference the information provided by the literature with the values the spacetimeengine provides (this is why I developed it originally). More commonly, this utility can be used for error checking.
    
[Metric Tensor](https://en.wikipedia.org/wiki/Metric_tensor)
===============

Generally speaking, any metric solution to the Einstein field equations will be packaged into a geometric object known as the metric tensor. The metric tensor is often represented in matrix form and the spacetimeengine package adopts this representation.

![equation](https://latex.codecogs.com/png.latex?%5Cdpi%7B100%7D%20%5Chuge%20g_%7B%5Cmu%5Cnu%7D%3D%5Cbegin%7Bbmatrix%7D%20%5Cleft%20%28%201-%5Cfrac%7B2GM%7D%7Brc%5E%7B2%7D%7D%20%5Cright%20%29%20%26%200%20%26%200%20%26%200%20%5C%5C%200%20%26%20-%5Cleft%20%28%201-%5Cfrac%7B2GM%7D%7Brc%5E%7B2%7D%7D%20%5Cright%20%29%5E%7B-1%7D%20%26%200%20%26%200%20%5C%5C%200%20%26%200%20%26%20-r%5E%7B2%7D%20%26%200%20%5C%5C%200%20%26%200%20%26%200%20%26%20-r%5E%7B2%7D%5Csin%5E%7B2%7D%5Ctheta%20%5Cend%7Bbmatrix%7D)

The spacetimeengine package employs the Sympy 'Matrix' object for packaging the metric tensor and it serves as the essential parameter for constructing a 'SpaceTime' object. The Solutions module currently stores some well-known metrics for study, but these can be used for understanding how to construct new solutions.

Constructing a solution (In development)
=======================
Currently, all metric solutions are packaged by specifying four key parameters and storing them in an array. These parameters include an index configuration for the given metric solution, the coordinates to define the metric in terms of, the metric itself, and the cosmological constant. It is important to note that a zero-valued cosmological constant indicates the employment of a classical formulation to the Einstein field equations. Below represents a valid definition of the Schwarzschild stationary black hole solution.

    def schwarzschild(self):    

        # Assigns meaning to the coordinates.
        x0, x1, x2, x3 = symbols('t r theta phi')
        # Groups the coordinates in an array.
        coordinate_set = [x0, x1, x2, x3]
        
        
        # Constants required to describe the metric.
        G, M, c = symbols('G M c')
        
        
        # Metric.
        metric = Matrix([    
                            [ (1-(2*G*M)/(x1*c**2)), 0, 0, 0 ], 
                            [ 0, - (1-(2*G*M)/(x1*c**2))**(-1), 0, 0 ], 
                            [ 0, 0, - x1**2, 0 ], 
                            [ 0, 0, 0, - x1**2*sin(x2)**2 ]
                        ])
        
        # Describes the index configuration which which the metric represents.
        index_config = "dd"
        
        
        # Cosmological constant.
        cosmological_constant = 0
        
        
        # An array detailing the solution.
        solution_array = [ metric, coordinate_set, index_config, cosmological_constant ]
        
        
        # Returns solution
        return solution_array
                                        
It may be helpful to store the solutions in a separate module. I prefer to keep my solutions in a 'Solution()' class, which can be found in the 'solutions' module. To construct a 'SpaceTime' object just execute the command below, but first consider the given solution since high complexity solutions can take exponentially longer to process.

    >>> spacetime = SpaceTime(Solution().schwarzschild())

The index configuration in this case is "dd" which represents a down-down configuration, which reflects a double covariant index configuration. These can be "uu", "dd", "ud", "du", but this library currently only supports certain index configurations depending on the quantity in question.

[Stress-Energy-Momentum Tensor](https://en.wikipedia.org/wiki/Stress%E2%80%93energy_tensor)
=============================
The Einstein field equations describe the equivilence of space-time curvature to mass-energy. The mass-energy is described by the coefficents encompassed within the stress-energy-momentum tensor denoted by T_{\mu\nu}. The cosmological constant denoted by Lambda is treated as an input parameter (since it is independent of the metric in most cases) and represents the dark energy thought to be responsble for the accellerated expansion of the cosmos. 

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
In differential geometry, the Ricci curvature tensor represents the amount by which the volume of a narrow conical piece of a small geodesic ball in a curved Riemannian manifold deviates from that of the standard ball in Euclidean space. As such, it provides one way of measuring the degree to which the geometry determined by a given Riemannian metric might differ from that of ordinary Euclidean n-space.

![equation](https://latex.codecogs.com/png.latex?%5Cinline%20%5Cdpi%7B100%7D%20%5Chuge%20R_%7Bij%7D%20%3D%20%7BR%5Ek%7D_%7Bikj%7D)

    >>> mu = 0 # (dt)
    >>> nu = 1 # (dr)
    >>> index_config = "dd"
    >>> spacetime.print_ricci_coefficient(index_config, 3, 2)
    
    R₃₂ = 0


[Riemann Tensor](https://en.wikipedia.org/wiki/Riemann_curvature_tensor)
================
In the mathematical field of differential geometry, the Riemann curvature tensor is the most common method used to express the curvature of Riemannian manifolds. It assigns a tensor to each point of a Riemannian manifold (i.e., it is a tensor field), that measures the extent to which the metric tensor is not locally isometric to that of Euclidean space.

![equation](https://latex.codecogs.com/png.latex?%5Cinline%20%5Cdpi%7B100%7D%20%5Chuge%20R%5E%5Crho%7B%7D_%7B%5Csigma%5Cmu%5Cnu%7D%20%3D%20%5Cpartial_%5Cmu%5CGamma%5E%5Crho%7B%7D_%7B%5Cnu%5Csigma%7D%20-%20%5Cpartial_%5Cnu%5CGamma%5E%5Crho%7B%7D_%7B%5Cmu%5Csigma%7D%20&plus;%20%5CGamma%5E%5Crho%7B%7D_%7B%5Cmu%5Clambda%7D%5CGamma%5E%5Clambda%7B%7D_%7B%5Cnu%5Csigma%7D%20-%20%5CGamma%5E%5Crho%7B%7D_%7B%5Cnu%5Clambda%7D%5CGamma%5E%5Clambda%7B%7D_%7B%5Cmu%5Csigma%7D)


    >>> index_config = "uddd"
    >>> spacetime.print_reimann_coefficient(index_config, 3, 2, 2, 3)
    
            -2⋅G⋅M 
    R³₂₂₃ = ───────
              2    
             c ⋅x₁ 

![equation](https://latex.codecogs.com/png.latex?%5Cinline%20%5Cdpi%7B100%7D%20%5Chuge%20%7B%5Cdisplaystyle%20R_%7Bik%5Cell%20m%7D%3D%7B%5Cfrac%20%7B1%7D%7B2%7D%7D%5Cleft%28%7B%5Cfrac%20%7B%5Cpartial%20%5E%7B2%7Dg_%7Bim%7D%7D%7B%5Cpartial%20x%5E%7Bk%7D%5Cpartial%20x%5E%7B%5Cell%20%7D%7D%7D&plus;%7B%5Cfrac%20%7B%5Cpartial%20%5E%7B2%7Dg_%7Bk%5Cell%20%7D%7D%7B%5Cpartial%20x%5E%7Bi%7D%5Cpartial%20x%5E%7Bm%7D%7D%7D-%7B%5Cfrac%20%7B%5Cpartial%20%5E%7B2%7Dg_%7Bi%5Cell%20%7D%7D%7B%5Cpartial%20x%5E%7Bk%7D%5Cpartial%20x%5E%7Bm%7D%7D%7D-%7B%5Cfrac%20%7B%5Cpartial%20%5E%7B2%7Dg_%7Bkm%7D%7D%7B%5Cpartial%20x%5E%7Bi%7D%5Cpartial%20x%5E%7B%5Cell%20%7D%7D%7D%5Cright%29&plus;g_%7Bnp%7D%5Cleft%28%5CGamma%20%5E%7Bn%7D%7B%7D_%7Bk%5Cell%20%7D%5CGamma%20%5E%7Bp%7D%7B%7D_%7Bim%7D-%5CGamma%20%5E%7Bn%7D%7B%7D_%7Bkm%7D%5CGamma%20%5E%7Bp%7D%7B%7D_%7Bi%5Cell%20%7D%5Cright%29%7D)

    >>> spacetime.print_riemann_coefficient("dddd", 2, 0, 2, 0)

                ⎛         2  ⎞
            G⋅M⋅⎝2⋅G⋅M - c ⋅r⎠
    R₂₀₂₀ = ──────────────────
                   4  2       
                  c ⋅r        


[Christoffel symbols of the First Kind](https://en.wikipedia.org/wiki/Christoffel_symbols)
=======================================

The connection coefficients or 'Christoffel symbol' are an array of numbers which represent the metric connection. The metric connection can be used to measure distances along curved manifolds. In General Relativity, the metric connection actually identifies the meaning of the gravitational field and can be used to track trajectories through spacetime.

![equation](https://latex.codecogs.com/png.latex?%5Cinline%20%5Cdpi%7B100%7D%20%5Chuge%20%5CGamma%20_%7Bcab%7D%3D%7B%5Ctfrac%20%7B1%7D%7B2%7D%7D%5Cleft%28%7B%5Cfrac%20%7B%5Cpartial%20g_%7Bca%7D%7D%7B%5Cpartial%20x%5E%7Bb%7D%7D%7D&plus;%7B%5Cfrac%20%7B%5Cpartial%20g_%7Bcb%7D%7D%7B%5Cpartial%20x%5E%7Ba%7D%7D%7D-%7B%5Cfrac%20%7B%5Cpartial%20g_%7Bab%7D%7D%7B%5Cpartial%20x%5E%7Bc%7D%7D%7D%5Cright%29)

    >>> spacetime.print_connection_coefficient("ddd", 1, 0, 0)

           -G⋅M 
    Γ₁₀₀ = ─────
            2  2
           c ⋅r 

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

In differential geometry, the Weyl curvature tensor, named after Hermann Weyl, is a measure of the curvature of spacetime or, more generally, a pseudo-Riemannian manifold. Like the Riemann curvature tensor, the Weyl tensor expresses the tidal force that a body feels when moving along a geodesic. The Weyl tensor differs from the Riemann curvature tensor in that it does not convey information on how the volume of the body changes, but rather only how the shape of the body is distorted by the tidal force.

![equation](https://latex.codecogs.com/png.latex?%5Cdpi%7B100%7D%20%5Chuge%20%7B%5Cdisplaystyle%20C_%7Bik%5Cell%20m%7D%3DR_%7Bik%5Cell%20m%7D&plus;%7B%5Cfrac%20%7B1%7D%7Bn-2%7D%7D%5Cleft%28R_%7Bim%7Dg_%7Bk%5Cell%20%7D-R_%7Bi%5Cell%20%7Dg_%7Bkm%7D&plus;R_%7Bk%5Cell%20%7Dg_%7Bim%7D-R_%7Bkm%7Dg_%7Bi%5Cell%20%7D%5Cright%29&plus;%7B%5Cfrac%20%7B1%7D%7B%28n-1%29%28n-2%29%7D%7DR%5Cleft%28g_%7Bi%5Cell%20%7Dg_%7Bkm%7D-g_%7Bim%7Dg_%7Bk%5Cell%20%7D%5Cright%29%2C%7D)

    >>> index_config = "dddd"
    >>> spacetime.print_weyl_coefficient(index_config, 3, 2, 2, 3)

                       2   
            2⋅G⋅M⋅r⋅sin (θ)
    C₃₂₂₃ = ───────────────
                    2      
                   c      

[Schouten Tensor](https://en.wikipedia.org/wiki/Schouten_tensor) (Experimental)
=================

![equation](https://latex.codecogs.com/png.latex?%5Cdpi%7B100%7D%20%5Chuge%20P_%7Bij%7D%20%3D%20%5Cfrac%7B1%7D%7Bn-2%7D%5Cleft%20%28%20R_%7Bij%7D%20-%20%5Cfrac%7BR%7D%7B2d-2%7D%5C%3A%20g_%7Bij%7D%20%5Cright%20%29)

    >>> spacetime.get_schouten_coefficient("dd",0,0)

                                    2
              ⎛         2  ⎞ ⎛d    ⎞ 
          G⋅M⋅⎝2⋅G⋅M - c ⋅r⎠⋅⎜──(t)⎟ 
                             ⎝dt   ⎠ 
    P₀₀ = ───────────────────────────
                      4  3           
                     c ⋅r         


[Geodesics parametrized by proper time](https://en.wikipedia.org/wiki/Geodesics_in_general_relativity#Mathematical_expression) (Experimental)
=======================================
This is a measure of the local acceleration; that which could be measured by an accelerometer.

![equation](https://latex.codecogs.com/png.latex?%5Cdpi%7B100%7D%20%5Chuge%20%5Cfrac%7Bd%5E%7B2%7Dx%5E%7B%5Clambda%7D%7D%7Bd%5Ctau%5E%7B2%7D%7D&plus;%5CGamma%5E%7B%5Clambda%7D_%7B%5Cmu%5Cnu%7D%5Cfrac%7Bdx%5E%7B%5Cmu%7D%7D%7Bd%5Ctau%7D%5Cfrac%7Bdx%5E%7B%5Cnu%7D%7D%7Bd%5Ctau%7D%3D0)

    >>> spacetime.print_proper_acceleration(0)

[Geodesics parametrized by coordinate time](https://en.wikipedia.org/wiki/Geodesics_in_general_relativity#Equivalent_mathematical_expression_using_coordinate_time_as_parameter) (Experimental)
===========================================
This is a measure of the accelleration one observers another undergoing.

![equation](https://latex.codecogs.com/png.latex?%5Cdpi%7B100%7D%20%5Chuge%20%5Cfrac%7Bd%5E%7B2%7Dx%5E%7B%5Clambda%7D%7D%7Bdt%5E%7B2%7D%7D%3D%5CGamma%5E%7B0%7D_%7B%5Cmu%5Cnu%7D%5Cfrac%7Bdx%5E%7B%5Cmu%7D%7D%7Bdt%7D%5Cfrac%7Bdx%5E%7B%5Cnu%7D%7D%7Bdt%7D%5Cfrac%7Bdx%5E%7B%5Clambda%7D%7D%7Bdt%7D%5C%3B-%5C%3B%5CGamma%5E%7B%5Clambda%7D_%7B%5Cmu%5Cnu%7D%5Cfrac%7Bdx%5E%7B%5Cmu%7D%7D%7Bdt%7D%5Cfrac%7Bdx%5E%7B%5Cnu%7D%7D%7Bdt%7D)

    >>> spacetime.print_coordinate_acceleration(0)

[Geodesic deviation equation](https://en.wikipedia.org/wiki/Geodesic_deviation#Mathematical_definition) (Experimental)
=============================
This is a measure of how much two initial paralell geodesic paths will deviate or converge. 

![equation](https://latex.codecogs.com/png.latex?%5Cdpi%7B100%7D%20%5Chuge%20%5Cfrac%7Bd%5E%7B2%7D%5Cxi%5E%7B%5Clambda%7D%7D%7Bdt%5E%7B2%7D%7D%3D-%5C%3BR%5E%7B%5Clambda%7D_%7B%5Cmu%5Cnu%5Cell%7D%5Cfrac%7Bdx%5E%7B%5Cmu%7D%7D%7Bdt%7D%5Cfrac%7Bdx%5E%7B%5Cnu%7D%7D%7Bdt%7D%5Cxi%5E%7B%5Cell%7D)

    >>> spacetime.print_separation_geodesic_acceleration(0)

Using with Jupyter Notebook (In development)
===========================
Jupyter notebook has become very popular tool for python development in recent years.  It is great for science and research and this api is no exception. In order to use with Jupyter notebook the only thing to consider is the printing system. 

Buy me a cold brew
==================
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=NL2XB2BMMGT6G&currency_code=USD&source=url)
