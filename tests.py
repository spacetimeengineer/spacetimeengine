#!/usr/bin/env python
from sympy import *
import curvature



a, b, c, t, x, y, z, x0, x1, x2, x3, dt, dx, dy, dz, dx0, dx1, dx2, dx3, dtau, r, th, ph, G, M, r, i, k, l = symbols('a b c t x y z x0 x1 x2 x3 dt dx dy dz dx0 dx1 dx2 dx3 dtau, r th ph G M r i k l')

def test_get_line_element():
    minkowski_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -1, 0, 0 ], [ 0, 0, -1, 0 ], [ 0, 0, 0, -1 ]])
    euclidian_infinitesimal_displacement_set = [ dt, dx, dy, dz ]
    pprint(get_line_element(minkowski_metric, euclidian_infinitesimal_displacement_set))
    
def test_connection():
    hypersphere_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -x0**2, 0, 0 ], [ 0, 0, -x0**2*sin(x1)**2, 0 ], [ 0, 0, 0, -x0**2*sin(x1)**2*sin(x2)**2 ]])
    minkowski_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -1, 0, 0 ], [ 0, 0, -1, 0 ], [ 0, 0, 0, -1 ]])
    #infentesimal_coordinate_set = [ dx0, dx1, dx2, dx3 ]
    hypersphere_coordinate_set = [ x0, x1, x2, x3 ]
    pprint(connection(hypersphere_metric, hypersphere_coordinate_set)[3])
    
def test_riemann_tensor():
    hypersphere_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -x0**2, 0, 0 ], [ 0, 0, -x0**2*sin(x1)**2, 0 ], [ 0, 0, 0, -x0**2*sin(x1)**2*sin(x2)**2 ]])
    minkowski_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -1, 0, 0 ], [ 0, 0, -1, 0 ], [ 0, 0, 0, -1 ]])
    #infentesimal_coordinate_set = [ dx0, dx1, dx2, dx3 ]
    coordinate_set = [ x0, x1, x2, x3 ]
    riemann = riemann_tensor(hypersphere_metric, coordinate_set)
    pprint(riemann[0])
    print("")
    pprint(riemann[1])
    print("")
    pprint(riemann[2])
    print("")
    pprint(riemann[3])
    print("")
    pprint(riemann[4])
    print("")
    pprint(riemann[5])
    print("")
    pprint(riemann[6])
    print("")
    pprint(riemann[7])
    print("")
    pprint(riemann[8])
    print("")
    pprint(riemann[9])
    print("")
    pprint(riemann[10])
    print("")
    pprint(riemann[11])
    print("")
    pprint(riemann[12])
    print("")
    pprint(riemann[13])
    print("")
    pprint(riemann[14])
    print("")
    pprint(riemann[15])
    print("")


def test_ricci_tensor():
    hypersphere_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -x0**2, 0, 0 ], [ 0, 0, -x0**2*sin(x1)**2, 0 ], [ 0, 0, 0, -x0**2*sin(x1)**2*sin(x2)**2 ]])
    minkowski_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -1, 0, 0 ], [ 0, 0, -1, 0 ], [ 0, 0, 0, -1 ]])
    infentesimal_coordinate_set = [ dx0, dx1, dx2, dx3 ]
    coordinate_set = [ x0, x1, x2, x3 ]
    pprint(ricci_tensor(hypersphere_metric, coordinate_set))
    
    
def test_ricci_scalar():
    hypersphere_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -x0**2, 0, 0 ], [ 0, 0, -x0**2*sin(x1)**2, 0 ], [ 0, 0, 0, -x0**2*sin(x1)**2*sin(x2)**2 ]])
    minkowski_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -1, 0, 0 ], [ 0, 0, -1, 0 ], [ 0, 0, 0, -1 ]])
    infentesimal_coordinate_set = [ dx0, dx1, dx2, dx3 ]
    coordinate_set = [ x0, x1, x2, x3 ]
    pprint(ricci_scalar(hypersphere_metric, coordinate_set))
    
def test_einstein_tensor():
    hypersphere_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -x0**2, 0, 0 ], [ 0, 0, -x0**2*sin(x1)**2, 0 ], [ 0, 0, 0, -x0**2*sin(x1)**2*sin(x2)**2 ]])
    minkowski_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -1, 0, 0 ], [ 0, 0, -1, 0 ], [ 0, 0, 0, -1 ]])
    infentesimal_coordinate_set = [ dx0, dx1, dx2, dx3 ]
    coordinate_set = [ x0, x1, x2, x3 ]
    pprint(einstein_tensor(hypersphere_metric, coordinate_set))

def test_stress_energy_tensor():
    hypersphere_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -x0**2, 0, 0 ], [ 0, 0, -x0**2*sin(x1)**2, 0 ], [ 0, 0, 0, -x0**2*sin(x1)**2*sin(x2)**2 ]])
    minkowski_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -1, 0, 0 ], [ 0, 0, -1, 0 ], [ 0, 0, 0, -1 ]])
    infentesimal_coordinate_set = [ dx0, dx1, dx2, dx3 ]
    coordinate_set = [ x0, x1, x2, x3 ]
    pprint(stress_energy_tensor(hypersphere_metric, coordinate_set))
    
    
def test_geodesic_equations():
    hypersphere_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -x0**2, 0, 0 ], [ 0, 0, -x0**2*sin(x1)**2, 0 ], [ 0, 0, 0, -x0**2*sin(x1)**2*sin(x2)**2 ]])
    minkowski_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -1, 0, 0 ], [ 0, 0, -1, 0 ], [ 0, 0, 0, -1 ]])
    infentesimal_coordinate_set = [ dx0, dx1, dx2, dx3 ]
    coordinate_set = [ x0, x1, x2, x3 ]
    pprint(geodesic_equations(hypersphere_metric, coordinate_set))
    

def test_geodesic_velocities():
    hypersphere_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -x0**2, 0, 0 ], [ 0, 0, -x0**2*sin(x1)**2, 0 ], [ 0, 0, 0, -x0**2*sin(x1)**2*sin(x2)**2 ]])
    minkowski_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -1, 0, 0 ], [ 0, 0, -1, 0 ], [ 0, 0, 0, -1 ]])
    infentesimal_coordinate_set = [ dx0, dx1, dx2, dx3 ]
    coordinate_set = [ x0, x1, x2, x3 ]
    pprint(geodesic_velocities(hypersphere_metric, coordinate_set))
    
def test_geodesic_paths():
    hypersphere_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -x0**2, 0, 0 ], [ 0, 0, -x0**2*sin(x1)**2, 0 ], [ 0, 0, 0, -x0**2*sin(x1)**2*sin(x2)**2 ]])
    minkowski_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -1, 0, 0 ], [ 0, 0, -1, 0 ], [ 0, 0, 0, -1 ]])
    infentesimal_coordinate_set = [ dx0, dx1, dx2, dx3 ]
    coordinate_set = [ x0, x1, x2, x3 ]
    pprint(geodesic_paths(hypersphere_metric, coordinate_set))

def test_print_connection():
    hypersphere_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -x0**2, 0, 0 ], [ 0, 0, -x0**2*sin(x1)**2, 0 ], [ 0, 0, 0, -x0**2*sin(x1)**2*sin(x2)**2 ]])
    minkowski_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -1, 0, 0 ], [ 0, 0, -1, 0 ], [ 0, 0, 0, -1 ]])
    infentesimal_coordinate_set = [ dx0, dx1, dx2, dx3 ]
    coordinate_set = [ x0, x1, x2, x3 ]
    print_connection(hypersphere_metric, coordinate_set)
    
def test_get_coordinate_four_velocity():
    minkowski_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -1, 0, 0 ], [ 0, 0, -1, 0 ], [ 0, 0, 0, -1 ]])
    euclidian_infinitesimal_displacement_set = [ dt, dx, dy, dz ]
    four_velocity = get_coordinate_four_velocity(minkowski_metric, euclidian_infinitesimal_displacement_set)
    return four_velocity

#test_get_line_element()
#test_connection()
#test_riemann_tensor()
#test_ricci_tensor()
#test_ricci_scalar()
#test_einstein_tensor()
#test_stress_energy_tensor()
#test_get_coordinate_four_velocity()

def test_first_bianchi_identity():
    return True

def test_second_bianchi_identity():
    return True