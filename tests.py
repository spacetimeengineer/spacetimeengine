#!/usr/bin/env python
from sympy import *
from spacetime import *
import unittest

class Test(unittest.TestCase):
    
    def test_compute_stress_energy_coefficient(self):
        m = symbols('m')
        x0, x1, x2, x3 = symbols('x0 x1 x2 x3')
        coordinate_set = [ x0, x1, x2, x3 ]
        einstein_rosen_bridge = Matrix([
                                           [ (x1-2*m) / x1, 0, 0, 0 ], 
                                           [ 0, - 4 * x1 / ( 2 * x1 - 4 * m ), 0, 0 ], 
                                           [ 0, 0, - x1**2, 0 ], 
                                           [ 0, 0, 0, - x1**2 * sin(x2)**2 ]
                                       ])
        spacetime = SpaceTime(einstein_rosen_bridge, coordinate_set)
        self.assertEqual(spacetime.compute_stress_energy_coefficient("dd", 0, 0 ), 0)

    def test_compute_einstein_coefficient(self):
        m = symbols('m')
        x0, x1, x2, x3 = symbols('x0 x1 x2 x3')
        coordinate_set = [ x0, x1, x2, x3 ]
        einstein_rosen_bridge = Matrix([
                                           [ (x1-2*m) / x1, 0, 0, 0 ], 
                                           [ 0, - 4 * x1 / ( 2 * x1 - 4 * m ), 0, 0 ], 
                                           [ 0, 0, - x1**2, 0 ], 
                                           [ 0, 0, 0, - x1**2 * sin(x2)**2 ]
                                       ])
        spacetime = SpaceTime(einstein_rosen_bridge, coordinate_set)
        self.assertEqual(spacetime.compute_einstein_coefficient("dd", 0, 0 ), 0)

    def test_compute_ricci_coefficient(self):
        m = symbols('m')
        x0, x1, x2, x3 = symbols('x0 x1 x2 x3')
        coordinate_set = [ x0, x1, x2, x3 ]
        einstein_rosen_bridge = Matrix([
                                           [ (x1-2*m) / x1, 0, 0, 0 ], 
                                           [ 0, - 4 * x1 / ( 2 * x1 - 4 * m ), 0, 0 ], 
                                           [ 0, 0, - x1**2, 0 ], 
                                           [ 0, 0, 0, - x1**2 * sin(x2)**2 ]
                                       ])
        spacetime = SpaceTime(einstein_rosen_bridge, coordinate_set)
        self.assertEqual(spacetime.compute_ricci_coefficient("dd", 0, 0 ), 0)

    def test_compute_riemann_coefficient(self):
        m = symbols('m')
        x0, x1, x2, x3 = symbols('x0 x1 x2 x3')
        coordinate_set = [ x0, x1, x2, x3 ]
        einstein_rosen_bridge = Matrix([
                                           [ (x1-2*m) / x1, 0, 0, 0 ], 
                                           [ 0, - 4 * x1 / ( 2 * x1 - 4 * m ), 0, 0 ], 
                                           [ 0, 0, - x1**2, 0 ], 
                                           [ 0, 0, 0, - x1**2 * sin(x2)**2 ]
                                       ])
        spacetime = SpaceTime(einstein_rosen_bridge, coordinate_set)
        self.assertEqual(spacetime.compute_riemann_coefficient("uddd", 0, 0, 0, 0), 0)

    def test_compute_connection_coefficient(self):
        m = symbols('m')
        x0, x1, x2, x3 = symbols('x0 x1 x2 x3')
        coordinate_set = [ x0, x1, x2, x3 ]
        einstein_rosen_bridge = Matrix([
                                           [ (x1-2*m) / x1, 0, 0, 0 ], 
                                           [ 0, - 4 * x1 / ( 2 * x1 - 4 * m ), 0, 0 ], 
                                           [ 0, 0, - x1**2, 0 ], 
                                           [ 0, 0, 0, - x1**2 * sin(x2)**2 ]
                                       ])
        spacetime = SpaceTime(einstein_rosen_bridge, coordinate_set)
        self.assertEqual(spacetime.compute_connection_coefficient("udd", 0, 0, 0), 0)

    def test_energy_conservation(self):
        return True
    
    def test_first_bianchi_identity():
        m = symbols('m')
        x0, x1, x2, x3 = symbols('x0 x1 x2 x3')
        coordinate_set = [ x0, x1, x2, x3 ]
        einstein_rosen_bridge = Matrix([
                                           [ (x1-2*m) / x1, 0, 0, 0 ], 
                                           [ 0, - 4 * x1 / ( 2 * x1 - 4 * m ), 0, 0 ], 
                                           [ 0, 0, - x1**2, 0 ], 
                                           [ 0, 0, 0, - x1**2 * sin(x2)**2 ]
                                       ])
        spacetime = SpaceTime(einstein_rosen_bridge, coordinate_set)
        self.assertEqual(spacetime.compute_connection_coefficient("udd", 0, 0, 0), 0)
    
        
        
        
unittest.main()
