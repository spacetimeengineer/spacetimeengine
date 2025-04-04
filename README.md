================================================================================
SpacetimeEngine: Symbolic Einstein Field Equation Analyzer
================================================================================

A Python utility built on Sympy (a symbolic mathematics library) that analyzes any given metric solution to the Einstein field equations.

Einstein Field Equations:
    G_{μν} + Λg_{μν} = (8πG / c⁴) T_{μν}

--------------------------------------------------------------------------------
Prerequisites
--------------------------------------------------------------------------------

Linux
-----
1. Install Python 3:
    $ sudo apt install python3

2. Install pip3:
    $ sudo apt install python3-pip

3. Install git:
    $ sudo apt-get install git

MacOS
-----
1. Install Homebrew:
    $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

2. Set Python environment variable:
    $ export PATH="/usr/local/opt/python/libexec/bin:$PATH"

3. Install git:
    $ brew install git

4. Install Python 3 and pip3:
    $ brew install python3
    $ brew postinstall python3

Windows
-------
1. Install Python 3 and pip3:
    https://www.python.org/downloads/

2. Install git:
    https://gitforwindows.org/

--------------------------------------------------------------------------------
Installation
--------------------------------------------------------------------------------

With pip3:
----------
1. Install package:
    $ pip3 install spacetimeengine

2. Enter Python shell:
    $ python3

3. Import the package:
    >>> from spacetimeengine import *

4. Create a SpaceTime object (Schwarzschild example):
    >>> schwarzschild_spacetime = SpaceTime(Solution().schwarzschild())

With git:
---------
1. Clone the repository:
    $ git clone https://github.com/spacetimeengineer/spacetimeengine

2. Navigate to the sample directory:
    $ cd spacetimeengine/spacetimeengine/samples

3. Run the example:
    $ python3 example.py

--------------------------------------------------------------------------------
Suggested Use
--------------------------------------------------------------------------------

SpacetimeEngine is useful for students and researchers studying General Relativity. If you're analyzing a metric solution in published literature, this tool can compute curvature tensors and help verify or explore their physical implications.

It is especially useful for validating metrics, checking errors, and learning how different tensors arise from a given spacetime configuration.

--------------------------------------------------------------------------------
Metric Tensor
--------------------------------------------------------------------------------

Any solution to the Einstein field equations is represented by a metric tensor, often in matrix form. SpacetimeEngine uses Sympy's Matrix object to represent this tensor.

Example: Schwarzschild Metric

g_{μν} =
⎡  (1 - 2GM/rc²)        0         0               0             ⎤
⎢       0         -1/(1 - 2GM/rc²)  0               0             ⎥
⎢       0              0         -r²              0             ⎥
⎣       0              0          0         -r²sin²θ         ⎦

--------------------------------------------------------------------------------
Constructing a Solution (In Development)
--------------------------------------------------------------------------------

All metric solutions are packaged into an array with the following elements:
1. Metric (Sympy Matrix)
2. Coordinate set
3. Index configuration (e.g., "dd", "uu")
4. Cosmological constant

Example: Schwarzschild solution

    def schwarzschild(self):
        x0, x1, x2, x3 = symbols('t r theta phi')
        coordinate_set = [x0, x1, x2, x3]
        G, M, c = symbols('G M c')

        metric = Matrix([
            [ (1 - (2*G*M)/(x1*c**2)), 0, 0, 0 ],
            [ 0, -1/(1 - (2*G*M)/(x1*c**2)), 0, 0 ],
            [ 0, 0, -x1**2, 0 ],
            [ 0, 0, 0, -x1**2*sin(x2)**2 ]
        ])

        index_config = "dd"
        cosmological_constant = 0

        return [metric, coordinate_set, index_config, cosmological_constant]

To use:

    >>> spacetime = SpaceTime(Solution().schwarzschild())

Note: Only certain index configurations are currently supported.

--------------------------------------------------------------------------------
Stress-Energy-Momentum Tensor
--------------------------------------------------------------------------------

The tensor T_{μν} represents the distribution of mass and energy. The cosmological constant (Λ) can be set as a parameter.

Example:

    >>> cosmological_constant = 0
    >>> mu = 0  # dt
    >>> nu = 1  # dr
    >>> index_config = "dd"
    >>> spacetime.print_stress_energy_coefficient(index_config, mu, nu)

    0

(Schwarzschild is a vacuum solution, so T_{μν} = 0)

--------------------------------------------------------------------------------
Einstein Tensor
--------------------------------------------------------------------------------

G_{μν} = R_{μν} - (1/2)Rg_{μν}

Describes curvature of spacetime.

Example:

    >>> mu = 0
    >>> nu = 1
    >>> index_config = "dd"
    >>> spacetime.print_einstein_coefficient(index_config, mu, nu)

    G₀₁ = 0

--------------------------------------------------------------------------------
Ricci Tensor
--------------------------------------------------------------------------------

The Ricci tensor R_{μν} measures how much volumes in curved space deviate from flat space.

    R_{ij} = R^k_{ikj}

Example:

    >>> spacetime.print_ricci_coefficient("dd", 3, 2)

    R₃₂ = 0

--------------------------------------------------------------------------------
Riemann Tensor
--------------------------------------------------------------------------------

Measures how the metric deviates from flat space at a point.

    R^ρ_{σμν} = ∂μΓ^ρ_{νσ} - ∂νΓ^ρ_{μσ} + Γ^ρ_{μλ}Γ^λ_{νσ} - Γ^ρ_{νλ}Γ^λ_{μσ}

Example:

    >>> spacetime.print_reimann_coefficient("uddd", 3, 2, 2, 3)

            -2⋅G⋅M 
    R³₂₂₃ = ───────
              2    
             c ⋅x₁

--------------------------------------------------------------------------------
References
--------------------------------------------------------------------------------

- Metric Tensor: https://en.wikipedia.org/wiki/Metric_tensor
- Stress-Energy Tensor: https://en.wikipedia.org/wiki/Stress-energy_tensor
- Einstein Tensor: https://en.wikipedia.org/wiki/Einstein_tensor
- Ricci Tensor: https://en.wikipedia.org/wiki/Ricci_curvature
- Riemann Tensor: https://en.wikipedia.org/wiki/Riemann_curvature_tensor
