#!/usr/bin/env python
from sympy import *
from field_equations import Metric


def main():

    
    """
    Description
    ===========
    Each notable formula contained in the Einstien Field Equations shall be represented in terms of a function, a latex representation where the index variables such as i, j, k, ect are explicitly utilized within the for loops. These for loops are representative of the Einstion summation convention wheras the summation takes place within the for loop.
    """

    a, b, c, d, s, k, t, x, y, z, x0, x1, x2, x3, dt, dx, dy, dz, dx0, dx1, dx2, dx3, vx, vy, vz, vtau, dtau, dX, r, th, ph, G, M, r, i, k, l, R, v, f, w  = symbols('a b c d s k t x y z x0 x1 x2 x3 dt dx dy dz dx0 dx1 dx2 dx3 vx vy vz vtau dtau dX, r th ph G M r i k l R v f w')

    '''
    Goal, map indecies to for loops to latex for intuition.

    '''
    tau = Symbol('tau')
    
    #x0 = Function('x0')(tau)
    #x1 = Function('x1')(tau)
    #x2 = Function('x2')(tau)
    #x3 = Function('x3')(tau)
    

    #psi = Symbol('psi')
    #the = Symbol('theta')
    #phi = Symbol('phi')

    
    schwarzschild_spacetime = Matrix([
                                  [ ((1 - 2 * G * M) / ( x0 * c**2 )), 0, 0, 0 ], 
                                  [ 0, - ((1 - 2 * G * M) / ( x0 * c**2 ))**(-1), 0, 0 ], 
                                  [ 0, 0, - x1**2, 0 ], 
                                  [ 0, 0, 0, - x1**2 * sin(x2)**2 ]
                              ])
    
    
    ellis_drainhole_spacetime = Matrix([
                                  [ 1, 0, 0, 0 ], 
                                  [ 0, - 1, 0, 0 ], 
                                  [ 0, 0, - ( k**2 + x1 ** 2 ), 0 ], 
                                  [ 0, 0, 0, - (k**2 + x1 ** 2) * sin(x2)**2 ]
                              ])
    
    hypersphere_metric = Matrix([
                                    [ 1, 0, 0, 0 ],
                                    [ 0, -x0**2, 0, 0 ],
                                    [ 0, 0, -x0**2*sin(x1)**2, 0 ],
                                    [ 0, 0, 0, -x0**2*sin(x1)**2*sin(x2)**2 ]
                                ])
    
    minkowski_metric = Matrix([
                                  [ 1, 0, 0, 0 ], 
                                  [ 0, -1, 0, 0 ], 
                                  [ 0, 0, -1, 0 ], 
                                  [ 0, 0, 0, -1 ]
                              ])
    
    
    f = Rational('1/2') * w**(-2)
    godel_spacetime = Matrix([
                                  [ f, 0, f * 2*E**(2 * x1), 0 ], 
                                  [ 0, -1, 0, 0 ], 
                                  [ f * 2*E**(2 * x1), 0, -f*Rational('1/2')*E**x1, 0 ], 
                                  [ 0, 0, 0, -f ]
                              ])


    milne_spacetime = Matrix([
                                  [ 1, 0, 0, 0 ], 
                                  [ 0, -x0**2, 0, 0 ], 
                                  [ 0, 0, -x0**2*sinh(x1)**2, 0 ],
                                  [ 0, 0, 0, -x0**2*sinh(x1)**2*sin(x2)**2 ]
                             ])
    
    
    
    a, J, M, c, delt, sigm = symbols('a J M c Delta Sigma')
    a = J / ( M * c )
    rs = 2 * G * M / ( c**2 )
    sigm = x1**2 + a**2 * cos(x2)**2
    delt = (r**2 - x0 * rs + a**2)
    
    
    kerr_spacetime = Matrix([
                              [ (1 - rs * x1 / sigm ), 0, 0, 2 * G * M / ( c**2 ) ], 
                              [ 0, -1 * ( delt / sigm ), 0, 0 ], 
                              [ 0, 0, -1 * sigm, 0 ],
                              [ 2 * G * M / ( c**2 ), 0, 0, -1 * (x1**2 + a**2 + (rs*x1*a**2/sigm)*sin(x2))*sin(x2) ]
                            ])

    #Ref: https://en.wikipedia.org/wiki/Taub%E2%80%93NUT_space
    #Latex: 
    U, m, l = symbols('U m l')
    U = (2 * m * x0 + l**2 - x0**2) / ( x0**2 + l**2 )
    taub_nut_spacetime = Matrix([
                                    [ U**(-1), 0, 0, 0 ], 
                                    [ 0, -4 * l**2 * U, -1 * cos(x2) * (4 * l**2 * U), 0 ], 
                                    [ 0, -1 * cos(x2) * (4 * l**2 * U), -1 * (x0**2 + l**2), 0 ],
                                    [ 0, 0, 0, -1 * (x0**2 + l**2) * sin(x2) - (4 * l**2 * U) * cos(x2)**2 ]
                                ])
    
    
    
    
    ozsvath_schucking_spacetime = Matrix([
                                             [ 1, 0, -2*x3, 0 ], 
                                             [ 0, 0, 1*x3, 0 ], 
                                             [ -2*x3, 1*x3, -1, 1 ], 
                                             [ 0, 0, 1, 1 ]
                                         ])
    
    
    G, M, c, Q, k = symbols('G M c Q k')
    rs = 2 * G * M / ( c**2 )
    rq = Q**2 * G * k / c**4
    reissner_nordstrom_spacetime = Matrix([
                                              [ (1 + rs / x1 + rq**2 / x0**2), 0, 0, 0 ], 
                                              [ 0, -1 * (1 + rs / x1 + rq**2 / x0**2)**(-1), 0, 0 ], 
                                              [ 0, 0, -x1**2, 0 ], 
                                              [ 0, 0, 0, -x1**2 * sin(x2)**2 ]
                                          ])

    
    
    G, M, c, Q, k = symbols('G M c Q k')
    rs = 2 * G * M / ( c**2 )
    rq = Q**2 * G * k / c**4
    kerr_newman_spacetime = Matrix([
                                              [ (1 + rs / x1 + rq**2 / x0**2), 0, 0, 0 ], 
                                              [ 0, -1 * (1 + rs / x1 + rq**2 / x0**2)**(-1), 0, 0 ], 
                                              [ 0, 0, -x1**2, 0 ], 
                                              [ 0, 0, 0, -x1**2 * sin(x2)**2 ]
                                          ])
    
    
    
    

    """
    xs = Function('x')(x0)
    vs = xs.diff(x0)
    rs = sqrt((x1-xs)**2 + x2**2 + x3**2)
    fs = tanh(s * (rs + R)) - tanh(s * (rs - R)) / (2 * tanh( s * R ))

    # The classic warp drive exat solution. (This takes a long time to process!!!)
    alcubierre_spacetime = Matrix([
                                   [ (vs**2 * fs**2 - 1), -2*vs*fs, -2*vs*fs, -2*vs*fs ], 
                                   [ -2*vs*fs, -1, 0, 0 ], 
                                   [ -2*vs*fs, 0, -1, 0 ], 
                                   [ -2*vs*fs, 0, 0, -1 ]
                               ])
    """


    coordinate_set = [ x0, x1, x2, x3 ]
    mt = Metric(reissner_nordstrom_spacetime, coordinate_set)

        
    """
    Configuration
    =============
    Make sure the coordinate_set is utilized in the metric which will be applied to it.
    The general coordinate_set -> [ x0, x1, x2, x3 ] is usefule because you need only swith out the metric when performing tests.
    Note: Build a function which swaps symbols for something more desireable.
    """

        
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
    #pprint(mt.ricci_scalar())
    #pprint(simplify(mt.ricci_scalar()+12/x0**2==0))
    #pprint(mt.einstein_coefficient("dd", 0, 0))
    #pprint(mt.stress_energy_coefficient("dd", 0, 0))
    #mt.list_metric_components("dd")
    print("")
    print("")
    print("Metric tensor coefficients (dd)")
    print("================================")
    mt.list_metric_coefficients("dd")
    
    print("")
    print("")
    print("Connection coefficients (udd)")
    print("=============================")
    mt.list_connection_coefficients("udd")
    
    print("")
    print("")
    print("Connection coefficients (ddd)")
    print("=============================")
    mt.list_connection_coefficients("ddd")
    
    print("")
    print("")
    print("Riemann curvature tensor coefficients (uddd)")
    print("============================================")
    mt.list_riemann_coefficients("uddd")
    
    print("")
    print("")
    print("Einstein curvature tensor coefficients (dddd)")
    print("=============================================")
    mt.list_riemann_coefficients("dddd")
    
    print("")
    print("")
    print("Ricci curvature tensor coefficients (dd)")
    print("========================================")
    mt.list_ricci_coefficients("dd")
    
    print("")
    print("")
    print("Einstein tensor coefficients (dd)")
    print("=================================")
    mt.list_einstein_coefficients("dd")
    
    print("")
    print("")
    print("Stress-energy-momentum tensor coefficients (dd)")
    print("===============================================")
    mt.list_stress_energy_coefficients("dd")
    
    print("")
    print("")
    print("General geodesic equations parameterized by propter time.")
    print("=========================================================")
    mt.proper_time_geodesics(0,0,0)
    
    # Print out general geodesic equations.
    # Solve for accelleration, velocity adn position vectors.
    # Plot all vectors with respect to all relevent parameters.
    
if __name__ == "__main__":
    main()







