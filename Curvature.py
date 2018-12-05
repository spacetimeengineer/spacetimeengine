#!/usr/bin/env python
from sympy import *


"""
Description
===========
Each notable formula contained in the Einstien Field Equations shall be represented in terms of a function, a latex representation where the index variables such as i, j, k, ect are explicitly utilized within the for loops. These for loops are representative of the Einstion summation convention wheras the summation takes place within the for loop.
"""

t, x, y, z, x0, x1, x2, x3, dt, dx, dy, dz, dx0, dx1, dx2, dx3, dtau, r, th, ph, G, M, r, c = symbols('t x y z x0 x1 x2 x3 dt dx dy dz dx0 dx1 dx2 dx3 dtau, r th ph G M r c')
init_printing(use_unicode=True)




def line_element(metric, coordinate_set):
    """
    Description
    ===========
    For a given metric and coordinate set: 

    Example
    =======
    minkowski_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -1, 0, 0 ], [ 0, 0, -1, 0 ], [ 0, 0, 0, -1 ]])
    4d_euclidian_set = [ t, x, y, z ]
    print( line_element(metric, coordinate_set) )

    LaTeX representation
    ====================
    ds^2 = g_{ij}dx^\mu dx^\nu 
    Where the covariant indices i and j are utilized as for-loop iteration variables.
    """

    line_element = 0
    one_forms = Matrix( [ [ 0 , 0 , 0 , 0 ], [ 0 , 0 , 0 , 0 ], [ 0 , 0 , 0 , 0 ], [ 0 , 0 , 0 , 0 ] ] )
    for i in range(len(coordinate_set)):
        for j in range(len(coordinate_set)):
            line_element = line_element + coordinate_set[i]*coordinate_set[j] * metric[i,j]
    return Eq(dtau**2,line_element)

def test_line_element():
    minkowski_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -1, 0, 0 ], [ 0, 0, -1, 0 ], [ 0, 0, 0, -1 ]])
    euclidian_set = [ dt, dx, dy, dz ]
    pprint(line_element(minkowski_metric, euclidian_set))
    


def connection(metric, coordinate_set):
    """
    Description
    ===========

    Example
    =======

    LaTeX representation
    ====================
    {\displaystyle \Gamma ^{i}_{kl}={\tfrac {1}{2}}g^{im}\left({\frac {\partial g_{mk}}{\partial x^{l}}}+{\frac {\partial g_{ml}}{\partial x^{k}}}-{\frac {\partial g_{kl}}{\partial x^{m}}}\right)
    """

    connection = Matrix( [ [ [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ], [ [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ], [ [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ], [ [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ] ] )
    inverse_metric = metric.inv()
    for j in range(len(coordinate_set)):
        for i in range(len(coordinate_set)):
            for m in range(len(coordinate_set)):
                christoffel_symbol = 0
                for k in range(len(coordinate_set)):
                    christoffel_symbol = christoffel_symbol+0.5*inverse_metric[k,m]*(diff(metric[i,k], coordinate_set[j])+diff(metric[j,k], coordinate_set[i])-diff(metric[i,j], coordinate_set[k]))
                connection[m,i][j]=simplify(christoffel_symbol)
    return connection

def test_connection():
    hypersphere_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -x0**2, 0, 0 ], [ 0, 0, -x0**2*sin(x1)**2, 0 ], [ 0, 0, 0, -x0**2*sin(x1)**2*sin(x2)**2 ]])
    minkowski_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -1, 0, 0 ], [ 0, 0, -1, 0 ], [ 0, 0, 0, -1 ]])
    infentesimal_coordinate_set = [ dx0, dx1, dx2, dx3 ]
    hypersphere_coordinate_set = [ x0, x1, x2, x3 ]
    pprint(connection(hypersphere_metric, hypersphere_coordinate_set))


"""
Important note!
connection[m,i][j]
maps to
connection[n][j]

where max(m+1)*max(i+1)=(n-1)

Basically it just turns some higher dimensional matrix to a list as such from left to right.
Problem is that it makes representing the array in more intuitive ways difficult.
This mapping formula will come in handly.

suggestion, make four matricies
"""




def riemann_tensor(metric, coordinate_set):
    """
    Description
    ===========

    Example
    =======

    LaTeX representation
    ====================
    R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma}
    - \partial_\nu\Gamma^\rho{}_{\mu\sigma}
    + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma}
    - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}
    """
    christoffel_symbol = connection(metric, coordinate_set)
    riemann_tensor = Matrix( [ [ [ [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ], [ [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ], [ [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ], [ [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ] ], [ [ [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ], [ [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ], [ [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ], [ [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ] ], [ [ [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ], [ [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ], [ [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ], [ [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ] ], [ [ [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ], [ [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ], [ [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ], [ [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ] ] ] )

    for a in range(len(coordinate_set)):
        for b in range(len(coordinate_set)):
            for g in range(len(coordinate_set)):
                for d in range(len(coordinate_set)):
                    riemann_component = diff(christoffel_symbol[d,b][a],coordinate_set[g]) - diff(christoffel_symbol[g,b][a],coordinate_set[d])
                    for u in range(len(coordinate_set)):
                        riemann_component = riemann_component + christoffel_symbol[d,b][u]*christoffel_symbol[g,u][a] - christoffel_symbol[g,b][u]*christoffel_symbol[d,u][a]
                    riemann_tensor[d,g][b][a] = simplify(riemann_component)

    return riemann_tensor

def test_riemann_tensor():
    hypersphere_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -x0**2, 0, 0 ], [ 0, 0, -x0**2*sin(x1)**2, 0 ], [ 0, 0, 0, -x0**2*sin(x1)**2*sin(x2)**2 ]])
    minkowski_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -1, 0, 0 ], [ 0, 0, -1, 0 ], [ 0, 0, 0, -1 ]])
    infentesimal_coordinate_set = [ dx0, dx1, dx2, dx3 ]
    coordinate_set = [ x0, x1, x2, x3 ]
    pprint(riemann_tensor(hypersphere_metric, coordinate_set)[15][3][3])


def ricci_tensor(metric, coordinate_set):
    """
    Status
    ======
    The Rieman tensor indexes are very likely wrong becasue they are untested. These need to be tested, understood and documented.

    Description
    ===========
    Returns the Ricci tensor for a given metric and coordinate set.
    Example
    =======

    LaTeX representation
    ====================
    R_{mn} = R^{g}_{mgn}
    """

    ricci_tensor = Matrix( [ [ 0 , 0 , 0 , 0 ], [ 0 , 0 , 0 , 0 ], [ 0 , 0 , 0 , 0 ], [ 0 , 0 , 0 , 0 ] ] )
    riemann = riemann_tensor(metric, coordinate_set)
    for m in range(len(coordinate_set)):
        for n in range(len(coordinate_set)):
            ricci_component = 0
            for g in range(len(coordinate_set)):
                # Untested. Need to swap indicies and test.
                ricci_component =  ricci_component + riemann[(1+n)*(g+1)-1][m][g]
    	    ricci_tensor[m,n] = ricci_component
    ricci_tensor = simplify(ricci_tensor)

    return ricci_tensor

def test_ricci_tensor():
    hypersphere_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -x0**2, 0, 0 ], [ 0, 0, -x0**2*sin(x1)**2, 0 ], [ 0, 0, 0, -x0**2*sin(x1)**2*sin(x2)**2 ]])
    minkowski_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -1, 0, 0 ], [ 0, 0, -1, 0 ], [ 0, 0, 0, -1 ]])
    infentesimal_coordinate_set = [ dx0, dx1, dx2, dx3 ]
    coordinate_set = [ x0, x1, x2, x3 ]
    pprint(ricci_tensor(hypersphere_metric, coordinate_set))


def ricci_scalar(metric_tensor, coordinate_set):
    """
    Description
    ===========

    Example
    =======

    LaTeX representation
    ====================

    """

    inverse_metric_tensor = metric_tensor.inv()
    ricci = ricci_tensor(metric_tensor, coordinate_set)
    ricci_scalar = 0
    for a in range(len(coordinate_set)):
        for b in range(len(coordinate_set)):
            ricci_scalar = ricci_scalar + inverse_metric_tensor[a,b] * ricci[a,b]
    ricci_scalar = simplify(ricci_scalar)


    return ricci_scalar

def test_ricci_scalar():
    hypersphere_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -x0**2, 0, 0 ], [ 0, 0, -x0**2*sin(x1)**2, 0 ], [ 0, 0, 0, -x0**2*sin(x1)**2*sin(x2)**2 ]])
    minkowski_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -1, 0, 0 ], [ 0, 0, -1, 0 ], [ 0, 0, 0, -1 ]])
    infentesimal_coordinate_set = [ dx0, dx1, dx2, dx3 ]
    coordinate_set = [ x0, x1, x2, x3 ]
    pprint(ricci_scalar(hypersphere_metric, coordinate_set))

def einstein_tensor(metric_tensor, coordinate_set):
    """
    Description
    ===========

    Example
    =======

    LaTeX representation
    ====================

    """
    einstein_tensor = Matrix( [ [ 0 , 0 , 0 , 0 ], [ 0 , 0 , 0 , 0 ], [ 0 , 0 , 0 , 0 ], [ 0 , 0 , 0 , 0 ] ] )
    scalar = ricci_scalar(metric_tensor, coordinate_set)
    ricci = ricci_tensor(metric_tensor, coordinate_set)
    for m in range(len(coordinate_set)):
        for n in range(len(coordinate_set)):
            einstein_component = ricci[m,n]-(scalar/2)*metric_tensor[m,n]
            einstein_tensor[m,n] = einstein_component

    return einstein_tensor


def test_einstein_tensor():
    hypersphere_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -x0**2, 0, 0 ], [ 0, 0, -x0**2*sin(x1)**2, 0 ], [ 0, 0, 0, -x0**2*sin(x1)**2*sin(x2)**2 ]])
    minkowski_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -1, 0, 0 ], [ 0, 0, -1, 0 ], [ 0, 0, 0, -1 ]])
    infentesimal_coordinate_set = [ dx0, dx1, dx2, dx3 ]
    coordinate_set = [ x0, x1, x2, x3 ]
    pprint(einstein_tensor(hypersphere_metric, coordinate_set))


def stress_energy_tensor(metric_tensor, coordinate_set):
    """
    Description
    ===========

    Example
    =======

    LaTeX representation
    ====================

    """
    stress_energy_tensor = c**4/(8*pi*G)*einstein_tensor(metric_tensor, coordinate_set)

    return stress_energy_tensor

def test_stress_energy_tensor():
    hypersphere_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -x0**2, 0, 0 ], [ 0, 0, -x0**2*sin(x1)**2, 0 ], [ 0, 0, 0, -x0**2*sin(x1)**2*sin(x2)**2 ]])
    minkowski_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -1, 0, 0 ], [ 0, 0, -1, 0 ], [ 0, 0, 0, -1 ]])
    infentesimal_coordinate_set = [ dx0, dx1, dx2, dx3 ]
    coordinate_set = [ x0, x1, x2, x3 ]
    pprint(stress_energy_tensor(hypersphere_metric, coordinate_set))

def geodesic_equations(metric, coordinate_set, parameterization):
    """
    Description
    ===========
    Returns a set geodesic equations for a given metric and coordinate_set in both proper time and coordinate time parameterizations.
    Example
    =======

    LaTeX representation
    ====================

    """

    return geodesics_equations

def test_geodesic_equations():
    hypersphere_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -x0**2, 0, 0 ], [ 0, 0, -x0**2*sin(x1)**2, 0 ], [ 0, 0, 0, -x0**2*sin(x1)**2*sin(x2)**2 ]])
    minkowski_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -1, 0, 0 ], [ 0, 0, -1, 0 ], [ 0, 0, 0, -1 ]])
    infentesimal_coordinate_set = [ dx0, dx1, dx2, dx3 ]
    coordinate_set = [ x0, x1, x2, x3 ]
    pprint(geodesic_equations(hypersphere_metric, coordinate_set))

def geodesic_velocities(metric, coordinate_set):
    """
    Description
    ===========

    Example
    =======

    LaTeX representation
    ====================

    """

    return geodesic_velocities

def test_geodesic_velocities():
    hypersphere_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -x0**2, 0, 0 ], [ 0, 0, -x0**2*sin(x1)**2, 0 ], [ 0, 0, 0, -x0**2*sin(x1)**2*sin(x2)**2 ]])
    minkowski_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -1, 0, 0 ], [ 0, 0, -1, 0 ], [ 0, 0, 0, -1 ]])
    infentesimal_coordinate_set = [ dx0, dx1, dx2, dx3 ]
    coordinate_set = [ x0, x1, x2, x3 ]
    pprint(geodesic_velocities(hypersphere_metric, coordinate_set))

def geodesic_paths(metric, coordinate_set):
    """
    Description
    ===========

    Example
    =======

    LaTeX representation
    ====================

    """

    return geodesic_paths

def test_geodesic_paths():
    hypersphere_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -x0**2, 0, 0 ], [ 0, 0, -x0**2*sin(x1)**2, 0 ], [ 0, 0, 0, -x0**2*sin(x1)**2*sin(x2)**2 ]])
    minkowski_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -1, 0, 0 ], [ 0, 0, -1, 0 ], [ 0, 0, 0, -1 ]])
    infentesimal_coordinate_set = [ dx0, dx1, dx2, dx3 ]
    coordinate_set = [ x0, x1, x2, x3 ]
    pprint(geodesic_paths(hypersphere_metric, coordinate_set))

def print_connection(connection):
    """
    Description
    ===========
    Prints the connection coefficients in a clear readable form.
    Example
    =======
    
    LaTeX representation
    ====================

    """
    max_columns = 3
    for n in range(len()):
        pprint(connection)
    
def test_print_connection():
    hypersphere_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -x0**2, 0, 0 ], [ 0, 0, -x0**2*sin(x1)**2, 0 ], [ 0, 0, 0, -x0**2*sin(x1)**2*sin(x2)**2 ]])
    minkowski_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -1, 0, 0 ], [ 0, 0, -1, 0 ], [ 0, 0, 0, -1 ]])
    infentesimal_coordinate_set = [ dx0, dx1, dx2, dx3 ]
    coordinate_set = [ x0, x1, x2, x3 ]
    print_connection(hypersphere_metric, coordinate_set)


def plot_geodesics(metric, coordinate_set):
    return 


#test_line_element()
#test_connection()
#test_riemann_tensor()
#test_ricci_tensor()
#test_ricci_scalar()
#test_einstein_tensor()
test_stress_energy_tensor()
