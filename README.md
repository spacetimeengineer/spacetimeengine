![alt text](https://github.com/spacetimeengineer/spacetimeengine/blob/master/resources/spacetimeengine_logo.png)

A Python utility built on Sympy (A symbolic mathematics library) which will analyze any given metric solution to the Einstein field equations.

![equation](https://latex.codecogs.com/png.latex?%5Cdpi%7B100%7D%20%5Chuge%20G_%7B%5Cmu%5Cnu%7D%20&plus;%20%5CLambda%20g_%7B%5Cmu%5Cnu%7D%20%3D%20%5Cfrac%7B8%5Cpi%20G%7D%7Bc%5E4%7DT_%7B%5Cmu%5Cnu%7D)

# Prerequisites (Linux)

1.) Install Python3

    $ sudo apt install python3

2.) Install pip3

    $ sudo apt install python3-pip

3.) Install git

    $ sudo apt-get install git

# Prerequisites (MacOS)

1.) Install homebrew  

    $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" brew doctor

2.) Set python as an environmental variable. 

    $ export PATH="/usr/local/opt/python/libexec/bin:$PATH"

3.) Install git

    $ brew install git

4.) Install python3 and pip3 (https://docs.python-guide.org/starting/install3/osx/)

    $ brew install python3
    $ brew postinstall python3

# Prerequisites (Windows)

1.) Install Python3 & pip3

    Navigate to https://www.python.org/downloads/

2.) Install git

    Navigate to https://gitforwindows.org/

# Installation with pip3

1.) Install with pip3

    $ pip3 install spacetimeengine  

2.) Enter python shell

    $ python3

3.) Import spacetimeengine

    >> from spacetimeengine import *

4.) Create a SpaceTime object which describes the Schwarzschild spacetime

    >> schwarzschild_spacetime = SpaceTime(Solution().schwarzschild())

5.) Enjoy watching the coefficients get computed.

# Installation with git

1.) Clone repository

    $ git clone https://github.com/spacetimeengineer/spacetimeengine

2.) Enter directory

    $ cd spacetimeengine/spacetimeengine/samples

3.) Run example.py

    $ python3 example.py

# Suggested Use

If you are a student or researcher, and you find yourself reading a publication based in General Relativity which provides metric solutions, then this utility can be used for working out the curvature coefficients associated with the solution provided by the user. This can be a helpful utility as you read through the literature because you will be able to cross-reference the information provided by the literature with the values the spacetimeengine provides (this is why I developed it originally). More commonly, this utility can be used for error checking.

## [Metric Tensor](https://en.wikipedia.org/wiki/Metric_tensor)

Generally speaking, any metric solution to the Einstein field equations will be packaged into a geometric object known as the metric tensor. The metric tensor is often represented in matrix form, and the spacetimeengine package adopts this representation.

![equation](https://latex.codecogs.com/png.latex?%5Cdpi%7B100%7D%20%5Chuge%20g_%7B%5Cmu%5Cnu%7D%3D%5Cbegin%7Bbmatrix%7D%20%5Cleft%20%28%201-%5Cfrac%7B2GM%7D%7Brc%5E%7B2%7D%7D%20%5Cright%20%29%20%26%200%20%26%200%20%26%200%20%5C%5C%200%20%26%20-%5Cleft%20%28%201-%5Cfrac%7B2GM%7D%7Brc%5E%7B2%7D%7D%20%5Cright%20%29%5E%7B-1%7D%20%26%200%20%26%200%20%5C%5C%200%20%26%200%20%26%20-r%5E%7B2%7D%20%26%200%20%5C%5C%200%20%26%200%20%26%200%20%26%20-r%5E%7B2%7D%5Csin%5E%7B2%7D%5Ctheta%20%5Cend%7Bbmatrix%7D)

The spacetimeengine package employs the Sympy 'Matrix' object for packaging the metric tensor and it serves as the essential parameter for constructing a 'SpaceTime' object. The Solutions module currently stores some well-known metrics for study, but these can be used for understanding how to construct new solutions.

# Constructing a solution (In development)

Currently, all metric solutions are packaged by specifying four key parameters and storing them in an array. These parameters include an index configuration for the given metric solution, the coordinates to define the metric in terms of, the metric itself, and the cosmological constant. It is important to note that a zero-valued cosmological constant indicates the employment of a classical formulation to the Einstein field equations. Below represents a valid definition of the Schwarzschild stationary black hole solution.

```python
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
    
    # Describes the index configuration which the metric represents.
    index_config = "dd"
    
    # Cosmological constant.
    cosmological_constant = 0
    
    # An array detailing the solution.
    solution_array = [ metric, coordinate_set, index_config, cosmological_constant ]
    
    # Returns solution
    return solution_array
