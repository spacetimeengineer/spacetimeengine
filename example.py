#!/usr/bin/env python
import json
from sympy import *
from field_equations import Metric


def main():

    
    """
    Description
    ===========
    Each notable formula contained in the Einstien Field Equations shall be represented in terms of a function, a latex representation where the index variables such as i, j, k, ect are explicitly utilized within the for loops. These for loops are representative of the Einstion summation convention wheras the summation takes place within the for loop.
    """

    a, b, c, d, t, x, y, z, x0, x1, x2, x3, dt, dx, dy, dz, dx0, dx1, dx2, dx3, vx, vy, vz, vtau, dtau, dX, r, th, ph, G, M, r, i, k, l, R = symbols('a b c d t x y z x0 x1 x2 x3 dt dx dy dz dx0 dx1 dx2 dx3 vx vy vz vtau dtau dX, r th ph G M r i k l R')

    '''
    Goal, map indecies to for loops to latex for intuition.

    '''

    
    #psi = Symbol('psi')
    #the = Symbol('theta')
    #phi = Symbol('phi')

    hypersphere_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -x0**2, 0, 0 ], [ 0, 0, -x0**2*sin(x1)**2, 0 ], [ 0, 0, 0, -x0**2*sin(x1)**2*sin(x2)**2 ]])
    minkowski_metric = Matrix([[ 1, 0, 0, 0 ], [ 0, -1, 0, 0 ], [ 0, 0, -1, 0 ], [ 0, 0, 0, -1 ]])

    infinitesimal_displacement_four_vector = Matrix([ dt, dx, dy, dz ])
    coordinate_set = [ x0, x1, x2, x3 ]

    mt = Metric(hypersphere_metric, coordinate_set)

    #pprint(mt.metric_tensor()[0,0])
    #pprint(mt.inverse_metric_tensor())
    #pprint(Eq(dX**2,mt.line_element()))
    #pprint(solve(dX**2+mt.line_element(),vx))
    #pprint(mt.coordinate_set)
    #pprint(mt.riemann_tensor("uddd"))
    #riemann_tensor("uddd")[0-15 (the matricies themselves from top to bottom) ][0-3 (These are the rows) ][0-3 (This is the horizontal vector elements within a Matrix from left to right omulns)]
    #pprint(mt.riemann_tensor("uddd"))
    #pprint(mt.connection()[0,1][1])
    #pprint(mt.connection()[1,0][1])
    #pprint(mt.connection_coefficient("udd", 1, 2, 2))
    #pprint(mt.connection_coefficient("ddd", 2, 2, 2))
    #pprint(mt.riemann_coefficient("uddd", 3, 1, 1, 3))
    #pprint(mt.ricci_coefficient("dd", 0, 0))
    #pprint(mt.ricci_coefficient("dd", 1, 1))
    #pprint(mt.ricci_coefficient("dd", 2, 2))
    #pprint(mt.ricci_coefficient("dd", 3, 3))
    #pprint(mt.new_connection(0,1,1))
    #pprint(mt.new_connection(1,0,1))
    #pprint(mt.ricci_scalar())
    #pprint(simplify(mt.ricci_scalar()+12/x0**2==0))
    
    pprint(mt.einstein_coefficient("dd", 0, 0))
    pprint(mt.stress_energy_coefficient("dd", 0, 0))
    
if __name__ == "__main__":
    main()







