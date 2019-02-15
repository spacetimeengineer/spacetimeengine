#!/usr/bin/env python
from sympy import *
from spacetimeengine.spacetime import *
from spacetimeengine.solutions import *
import unittest

class Test(unittest.TestCase):
    
    def test_compute_stress_energy_coefficient(self):
        black_hole = SpaceTime(Solution().schwarzschild(), True)
        vacuum_stress_energy_tensor_dd = Matrix([
                                                    [ 0, 0, 0, 0 ], 
                                                    [ 0, 0, 0, 0 ], 
                                                    [ 0, 0, 0, 0 ], 
                                                    [ 0, 0, 0, 0 ]
                                                ])
        self.assertEqual(black_hole.stress_energy_tensor_dd, vacuum_stress_energy_tensor_dd)

    def test_compute_einstein_coefficient(self):
        black_hole = SpaceTime(Solution().schwarzschild(), True)
        vacuum_einstein_tensor_dd = Matrix([
                                                [ 0, 0, 0, 0 ], 
                                                [ 0, 0, 0, 0 ], 
                                                [ 0, 0, 0, 0 ], 
                                                [ 0, 0, 0, 0 ]
                                            ])
        self.assertEqual(black_hole.einstein_tensor_dd, vacuum_einstein_tensor_dd)

    def test_compute_ricci_coefficient(self):
        black_hole = SpaceTime(Solution().schwarzschild(), True)
        vacuum_ricci_tensor_dd = Matrix([
                                            [ 0, 0, 0, 0 ], 
                                            [ 0, 0, 0, 0 ], 
                                            [ 0, 0, 0, 0 ], 
                                            [ 0, 0, 0, 0 ]
                                        ])
        self.assertEqual(black_hole.ricci_tensor_dd, vacuum_ricci_tensor_dd)

    def test_compute_riemann_coefficient(self):
        black_hole = SpaceTime(Solution().schwarzschild(), True)
        # The ommision of the Matrix object is due to the form in which the riemann tensor was constructed in the SpaceTime class. 
        # Sympy does not handle multidimensional matricies in a straitforward way.
        vacuum_riemann_tensor_uddd = [[ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ]]
        self.assertEqual(black_hole.riemann_tensor_uddd[15], vacuum_riemann_tensor_uddd)

    def test_compute_connection_coefficient(self):
        flat_spacetime = SpaceTime(Solution().minkowski(), True)
        # The ommision of the Matrix object is due to the form in which the riemann tensor was constructed in the SpaceTime class. 
        # Sympy does not handle multidimensional matricies in a straitforward way.
        vacuum_christoffel_symbols_udd = Matrix([
                                                    [
                                                        [ 0, 0, 0, 0 ], 
                                                        [ 0, 0, 0, 0 ], 
                                                        [ 0, 0, 0, 0 ], 
                                                        [ 0, 0, 0, 0 ]
                                                    ],
                                                    [
                                                        [ 0, 0, 0, 0 ], 
                                                        [ 0, 0, 0, 0 ], 
                                                        [ 0, 0, 0, 0 ], 
                                                        [ 0, 0, 0, 0 ]
                                                    ],
                                                    [
                                                        [ 0, 0, 0, 0 ], 
                                                        [ 0, 0, 0, 0 ], 
                                                        [ 0, 0, 0, 0 ], 
                                                        [ 0, 0, 0, 0 ]
                                                    ],
                                                    [
                                                        [ 0, 0, 0, 0 ], 
                                                        [ 0, 0, 0, 0 ], 
                                                        [ 0, 0, 0, 0 ], 
                                                        [ 0, 0, 0, 0 ]
                                                    ]
                                                ])
        self.assertEqual(flat_spacetime.christoffel_symbols_udd, vacuum_christoffel_symbols_udd)

    def test_first_bianchi_identity(self):
        black_hole = SpaceTime(Solution().schwarzschild(), True)
        a = black_hole.get_riemann_coefficient("dddd", 0, 1, 2, 3)
        b = black_hole.get_riemann_coefficient("dddd", 0, 2, 3, 1)
        c = black_hole.get_riemann_coefficient("dddd", 0, 3, 1, 2)

        self.assertEqual(a + b + c, 0)

    def test_riemann_skew_symmetry(self):
        black_hole = SpaceTime(Solution().schwarzschild(), True)
        a = black_hole.get_riemann_coefficient("dddd", 0, 1, 2, 3)
        b = black_hole.get_riemann_coefficient("dddd", 1, 0, 2, 3)
        c = black_hole.get_riemann_coefficient("dddd", 0, 1, 3, 2)

        self.assertEqual(a, -1*b)
        self.assertEqual(a, -1*c)

unittest.main()