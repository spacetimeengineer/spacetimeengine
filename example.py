#!/usr/bin/env python
from sympy import *
from IPython.display import display
from field_equations import SpaceTime


def main():
    init_printing()
    
    a, b, c, d, s, k, t, x, y, z, x0, x1, x2, x3, dt, dx, dy, dz, dx0, dx1, dx2, dx3, vx, vy, vz, vtau, dtau, dX, r, th, ph, G, M, r, i, k, l, R, v, f, w  = symbols('a b c d s k t x y z x0 x1 x2 x3 dt dx dy dz dx0 dx1 dx2 dx3 vx vy vz vtau dtau dX, r th ph G M r i k l R v f w')

    
    
    # The classic black hole solution. Uncharged and rotationally stationary.
    # PASSES!
    schwarzschild_spacetime = Matrix([    
                                          [ (1-(2*G*M)/(x1*c**2)), 0, 0, 0 ], 
                                          [ 0, - (1-(2*G*M)/(x1*c**2))**(-1), 0, 0 ], 
                                          [ 0, 0, - x1**2, 0 ], 
                                          [ 0, 0, 0, - x1**2*sin(x2)**2 ]
                                     ])
    """
    # Flat spacetime expressed in hyperspherical coordinates.
    # PASSES!
    milne_spacetime = Matrix([
                                  [ 1, 0, 0, 0 ], 
                                  [ 0, -x0**2, 0, 0 ], 
                                  [ 0, 0, -x0**2*sinh(x1)**2, 0 ],
                                  [ 0, 0, 0, -x0**2*sinh(x1)**2*sin(x2)**2 ]
                             ])
    
    # Friedmann Lemaitre Robertson Walker solution.
    a, k = symbols('a k')
    # PASSES!
    friedmann_lemaitre_robertson_walker_solution = Matrix([
                                                              [ 1, 0, 0, 0 ], 
                                                              [ 0, - a**2*(1-k*x1**2)**(-1), 0, 0 ], 
                                                              [ 0, 0, - a**2*x1**2, 0 ], 
                                                              [ 0, 0, 0, - a**2*x1**2*sin(x2)**2 ]
                                                          ])
    
    # Most famous wormhole solution.
    m = symbols('m')
    einstein_rosen_bridge = Matrix([
                                       [ (x1-2*m) / x1, 0, 0, 0 ], 
                                       [ 0, - 4 * x1 / ( 2 * x1 - 4 * m ), 0, 0 ], 
                                       [ 0, 0, - x1**2, 0 ], 
                                       [ 0, 0, 0, - x1**2 * sin(x2)**2 ]
                                   ])
    
    # Rotataing uncharged black hole.
    a, J, M, c, delt, sigm = symbols('a J M c Delta Sigma')
    a = (J/(M*c))
    rs = (2*G*M/(c**2))
    sigm = (x1**2 + (J/(M*c))**2 * cos(x2)**2)
    delt = (r**2 - x0 * (2*G*M/(c**2)) + (J/(M*c))**2)
    kerr_spacetime = Matrix([
                                [ (1 - rs * x1 / (x1**2 + (J/(M*c))**2 * cos(x2)**2) ), 0, 0, (2*G*M/(c**2))*x1*(J/(M*c))*sin(x2)**2 / (x1**2 + (J/(M*c))**2 * cos(x2)**2) ], 
                                [ 0, -1 * ( (r**2 - x0 * (2*G*M/(c**2)) + (J/(M*c))**2) / (x1**2 + (J/(M*c))**2 * cos(x2)**2) ), 0, 0 ], 
                                [ 0, 0, -1 * (x1**2 + (J/(M*c))**2 * cos(x2)**2), 0 ],
                                [ (2*G*M/(c**2))*x1*(J/(M*c))*sin(x2)**2 / (x1**2 + (J/(M*c))**2 * cos(x2)**2), 0, 0, -1 * (x1**2 + (J/(M*c))**2 + (rs*x1*(J/(M*c))**2/(x1**2 + (J/(M*c))**2 * cos(x2)**2))*sin(x2))*sin(x2) ]
                            ])
    
    
    
    # Original wormhole solution.
    #PASSES
    ellis_drainhole_spacetime = Matrix([
                                           [ 1, 0, 0, 0 ], 
                                           [ 0, - 1, 0, 0 ], 
                                           [ 0, 0, - ( k**2 + x1 ** 2 ), 0 ], 
                                           [ 0, 0, 0, - (k**2 + x1 ** 2) * sin(x2)**2 ]
                                       ])
    
    #PASSES
    hypersphere_metric = Matrix([
                                    [ 1, 0, 0, 0 ],
                                    [ 0, -x0**2, 0, 0 ],
                                    [ 0, 0, -x0**2*sin(x1)**2, 0 ],
                                    [ 0, 0, 0, -x0**2*sin(x1)**2*sin(x2)**2 ]
                                ])
    
    # Flat spacetime.
    minkowski_metric = Matrix([
                                  [ 1, 0, 0, 0 ], 
                                  [ 0, -1, 0, 0 ], 
                                  [ 0, 0, -1, 0 ], 
                                  [ 0, 0, 0, -1 ]
                              ])
    
    # A famous spacetime which describes time travel.
    f = Rational('1/2') * w**(-2)
    godel_spacetime = Matrix([
                                  [ f, 0, f * 2*E**(2 * x1), 0 ], 
                                  [ 0, -1, 0, 0 ], 
                                  [ f * 2*E**(2 * x1), 0, -f*Rational('1/2')*E**x1, 0 ], 
                                  [ 0, 0, 0, -f ]
                              ])
    
    
    # Rotataing uncharged black hole.
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
    # 
    ozsvath_schucking_spacetime = Matrix([
                                             [ 1, 0, -2*x3, 0 ], 
                                             [ 0, 0, 1*x3, 0 ], 
                                             [ -2*x3, 1*x3, -1, 1 ], 
                                             [ 0, 0, 1, 1 ]
                                         ])
    #
    G, M, c, Q, k = symbols('G M c Q k')
    rs = 2 * G * M / ( c**2 )
    rq = Q**2 * G * k / c**4
    reissner_nordstrom_spacetime = Matrix([
                                              [ (1 + rs / x1 + rq**2 / x0**2), 0, 0, 0 ], 
                                              [ 0, -1 * (1 + rs / x1 + rq**2 / x0**2)**(-1), 0, 0 ], 
                                              [ 0, 0, -x1**2, 0 ], 
                                              [ 0, 0, 0, -x1**2 * sin(x2)**2 ]
                                          ])
    # Rotataing charged black hole.
    G, M, c, Q, k = symbols('G M c Q k')
    rs = 2 * G * M / ( c**2 )
    rq = Q**2 * G * k / c**4
    kerr_newman_spacetime = Matrix([
                                       [ (1 + rs / x1 + rq**2 / x0**2), 0, 0, 0 ], 
                                       [ 0, -1 * (1 + rs / x1 + rq**2 / x0**2)**(-1), 0, 0 ], 
                                       [ 0, 0, -x1**2, 0 ], 
                                       [ 0, 0, 0, -x1**2 * sin(x2)**2 ]
                                   ])
    
    
    # The classic warp drive solution. (This takes a long time to process!!!) (I suspect the compute time diverges. I think there is some recursive error)
    # Does not crash.
    xs = symbols('x_s')(x0)
    vs = xs.diff(x0)
    rs = sqrt((x1-xs)**2 + x2**2 + x3**2)
    fs = tanh(s * (rs + R)) - tanh(s * (rs - R)) / (2 * tanh( s * R ))
    alcubierre_spacetime = Matrix([
                                      [ (vs**2 * fs**2 - 1), -2*vs*fs, -2*vs*fs, -2*vs*fs ], 
                                      [ -2*vs*fs, -1, 0, 0 ], 
                                      [ -2*vs*fs, 0, -1, 0 ], 
                                      [ -2*vs*fs, 0, 0, -1 ]
                                  ])
    
    
    # Rotataing uncharged black hole.
    a, J, M, c, delt, sigm = symbols('a J M c Delta Sigma')
    a = (J/(M*c))
    rs = (2*G*M/(c**2))
    sigm = (x1**2 + (J/(M*c))**2 * cos(x2)**2)
    delt = (r**2 - x0 * (2*G*M/(c**2)) + (J/(M*c))**2)
    kerr_spacetime = Matrix([
                                [ (1 - rs * x1 / (x1**2 + (J/(M*c))**2 * cos(x2)**2) ), 0, 0, (2*G*M/(c**2))*x1*(J/(M*c))*sin(x2)**2 / (x1**2 + (J/(M*c))**2 * cos(x2)**2) ], 
                                [ 0, -1 * ( (r**2 - x0 * (2*G*M/(c**2)) + (J/(M*c))**2) / (x1**2 + (J/(M*c))**2 * cos(x2)**2) ), 0, 0 ], 
                                [ 0, 0, -1 * (x1**2 + (J/(M*c))**2 * cos(x2)**2), 0 ],
                                [ (2*G*M/(c**2))*x1*(J/(M*c))*sin(x2)**2 / (x1**2 + (J/(M*c))**2 * cos(x2)**2), 0, 0, -1 * (x1**2 + (J/(M*c))**2 + (rs*x1*(J/(M*c))**2/(x1**2 + (J/(M*c))**2 * cos(x2)**2))*sin(x2))*sin(x2) ]
                            ])
    
    
    """
    
    coordinate_set = [ x0, x1, x2, x3 ]
    spacetime = SpaceTime(schwarzschild_spacetime, coordinate_set)

    
    
    print("")
    print("")
    print("Metric tensor coefficients (dd)")
    print("================================")
    spacetime.list_metric_coefficients("dd")
    
    print("")
    print("")
    print("Connection coefficients (udd)")
    print("=============================")
    spacetime.list_connection_coefficients("udd")
    
    print("")
    print("")
    print("Connection coefficients (ddd)")
    print("=============================")
    spacetime.list_connection_coefficients("ddd")
    
    print("")
    print("")
    print("Riemann curvature tensor coefficients (uddd)")
    print("============================================")
    spacetime.list_riemann_coefficients("uddd")
    
    print("")
    print("")
    print("Einstein curvature tensor coefficients (dddd)")
    print("=============================================")
    spacetime.list_riemann_coefficients("dddd")
    
    print("")
    print("")
    print("Ricci curvature tensor coefficients (dd)")
    print("========================================")
    spacetime.list_ricci_coefficients("dd")
    
    print("")
    print("")
    print("Einstein tensor coefficients (dd)")
    print("=================================")
    spacetime.list_einstein_coefficients("dd")
    
    print("")
    print("")
    print("Stress-energy-momentum tensor coefficients (dd)")
    print("===============================================")
    spacetime.list_stress_energy_coefficients("dd")
    
    print("")
    print("")
    print("General geodesic equations parameterized by propter time.")
    print("=========================================================")
    spacetime.proper_time_geodesics(0,0,0)
    
    # Print out general geodesic equations.
    # Solve for accelleration, velocity adn position vectors.
    # Plot all vectors with respect to all relevent parameters.
    
if __name__ == "__main__":
    main()







