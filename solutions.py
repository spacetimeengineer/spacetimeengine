#!/usr/bin/env python
from sympy import *

class Solution:
    
    def minkowski(self):
        """
        Description
        ===========
        Returns the Friedmann Lemaitre Robertson Walker metric which describes the spacetime for an expanding universe.
        Examples
        ========
        >>> print(Solution().minkowski())
        >>> 
        LaTeX representation
        ====================
        """
        
        # Index configuration for the metric
        index_config = "dd"
        # Physical constants.
        c = symbols('c')
        # Assigns meaning to the coordinates.
        #x0, x1, x2, x3 = symbols('t x y z')
        x0, x1, x2, x3 = symbols('t r theta phi')
        # Reference to the coordiante system.
        coordinate_set = [x0, x1, x2, x3]
        # Cosmological constant.
        cosmological_constant = 0
        # Metric solution.
        
        """
        metric = Matrix([
                              [ c**2, 0, 0, 0 ], 
                              [ 0, -1, 0, 0 ], 
                              [ 0, 0, -1, 0 ], 
                              [ 0, 0, 0, -1 ]
                          ])
        """

        """
        metric = Matrix([
                              [ 1, 0, 0, 0 ], 
                              [ 0, -1, 0, 0 ], 
                              [ 0, 0, -1, 0 ], 
                              [ 0, 0, 0, -1 ]
                          ])
        """
        
        metric = Matrix([
                              [ 1, 0, 0, 0 ], 
                              [ 0, -1, 0, 0 ], 
                              [ 0, 0, -x1**2, 0 ], 
                              [ 0, 0, 0, -x1**2*sin(x2)**2 ]
                          ])
                    
        # An array detailing the solution.
        solution_array = [ metric, coordinate_set, index_config, cosmological_constant ]
        return solution_array
    
    def weak_field_approximation(self):
        """
        Description
        ===========
        Returns the Friedmann Lemaitre Robertson Walker metric which describes the spacetime for an expanding universe.
        Examples
        ========
        >>> print(Solution().minkowski())
        >>> 
        LaTeX representation
        ====================
        """
        
        # Index configuration for the metric
        index_config = "dd"
        # Assigns meaning to the coordinates.
        x0, x1, x2, x3 = symbols('t r theta phi')
        # Physical constants.
        Ph = symbols('Phi')(x1)
        c = symbols('c')
        # Reference to the coordiante system.
        coordinate_set = [x0, x1, x2, x3]
        # Cosmological constant.
        cosmological_constant = 0
        # Metric solution.
        metric = Matrix([
                              [ (1+2*Ph/c**2)*c**2, 0, 0, 0 ], 
                              [ 0, -1/(1+2*Ph/c**2), 0, 0 ], 
                              [ 0, 0, -x1**2, 0 ], 
                              [ 0, 0, 0, -x1**2*sin(x2)**2 ]
                          ])
                    
        # An array detailing the solution.
        solution_array = [ metric, coordinate_set, index_config, cosmological_constant ]
        return solution_array
    
    
    def schwarzschild(self):    
        """
        Description
        ===========
        Returns the classic black hole solution. Uncharged and rotationally stationary.
        Examples
        ========
        >>> print(Solution().schwarzschild())
        >>> 
        LaTeX representation
        ====================
        """
        
        # Index configuration for the metric
        index_config = "dd"
        # Physical constants.
        G, M, c = symbols('G M c')
        # Assigns meaning to the coordinates.
        x0, x1, x2, x3 = symbols('t r theta phi')
        # Reference to the coordiante system.
        coordinate_set = [x0, x1, x2, x3]
        # Cosmological constant.
        cosmological_constant = 0
        # Metric solution.
        metric = Matrix([    
                            [ (1-(2*G*M)/(x1*c**2)), 0, 0, 0 ], 
                            [ 0, - (1-(2*G*M)/(x1*c**2))**(-1), 0, 0 ], 
                            [ 0, 0, - x1**2, 0 ], 
                            [ 0, 0, 0, - x1**2*sin(x2)**2 ]
                        ])
        
        # An array detailing the solution.
        solution_array = [ metric, coordinate_set, index_config, cosmological_constant ]
        return solution_array
    
    def friedmann_lemaitre_robertson_walker(self):
        """
        Description
        ===========
        Returns the Friedmann Lemaitre Robertson Walker metric which describes the spacetime for an expanding universe.
        Examples
        ========
        >>> print(Solution().friedmann_lemaitre_robertson_walker())
        >>> 
        LaTeX representation
        ====================
        """
        
        # Index configuration for the metric
        index_config = "dd"
        # Required symbols and constants.
        a, k = symbols('a k')
        # Assigns meaning to the coordinates.
        x0, x1, x2, x3 = symbols('t r theta phi')
        # Reference to the coordiante system.
        coordinate_set = [x0, x1, x2, x3]
        # Cosmological constant.
        cosmological_constant = 0
        # Metric solution.
        metric = Matrix([
                            [ 1, 0, 0, 0 ], 
                            [ 0, - a**2*(1-k*x1**2)**(-1), 0, 0 ], 
                            [ 0, 0, - a**2*x1**2, 0 ], 
                            [ 0, 0, 0, - a**2*x1**2*sin(x2)**2 ]
                        ])
        
        # An array detailing the solution.
        solution_array = [ metric, coordinate_set, index_config, cosmological_constant ]
        return solution_array

    # Most famous wormhole solution.
    def einstein_rosen_bridge(self):
        """
        Description
        ===========
        Returns the metric for the most famous wormhole solution.
        Examples
        ========
        >>> print(Solution().einstein_rosen_bridge())
        >>> 
        LaTeX representation
        ====================
        """
        
        # Index configuration for the metric
        index_config = "dd"
        # Required symbols and constants.
        m = symbols('m')
        # Assigns meaning to the coordinates.
        x0, x1, x2, x3 = symbols('t r theta phi')
        # Reference to the coordiante system.
        coordinate_set = [x0, x1, x2, x3]
        # Cosmological constant.
        cosmological_constant = 0
        # Metric solution.
        metric = Matrix([
                            [ (x1-2*m) / x1, 0, 0, 0 ], 
                            [ 0, - 4 * x1 / ( 2 * x1 - 4 * m ), 0, 0 ], 
                            [ 0, 0, - x1**2, 0 ], 
                            [ 0, 0, 0, - x1**2 * sin(x2)**2 ]
                        ])
        
        # An array detailing the solution.
        solution_array = [ metric, coordinate_set, index_config, cosmological_constant ]
        return solution_array
    
    def taub_nut(self):
        """
        Description
        ===========
        Returns Taub-Nut metric.
        Examples
        ========
        >>> print(taub_nut())
        >>> 
        LaTeX representation
        ====================
        """
        
        U, m, l = symbols('U m l')
        U = (2 * m * x0 + l**2 - x0**2) / ( x0**2 + l**2 )
        taub_nut_metric = Matrix([
                                        [ U**(-1), 0, 0, 0 ], 
                                        [ 0, -4 * l**2 * U, -1 * cos(x2) * (4 * l**2 * U), 0 ], 
                                        [ 0, -1 * cos(x2) * (4 * l**2 * U), -1 * (x0**2 + l**2), 0 ],
                                        [ 0, 0, 0, -1 * (x0**2 + l**2) * sin(x2) - (4 * l**2 * U) * cos(x2)**2 ]
                                    ])
        
        return taub_nut_metric

    def milne(self):
        """
        Description
        ===========
        Returns Milne metric.
        Examples
        ========
        >>> print(Solution().milne())
        >>> 
        LaTeX representation
        ====================
        """
        
        # Index configuration for the metric
        index_config = "dd"
        # Required symbols and constants.
        c = symbols('c')
        # Assigns meaning to the coordinates.
        x0, x1, x2, x3 = symbols('t r theta phi')
        # Reference to the coordiante system.
        coordinate_set = [x0, x1, x2, x3]
        # Cosmological constant.
        cosmological_constant = 0
        # Metric solution.
        metric = Matrix([
                                  [ 1, 0, 0, 0 ], 
                                  [ 0, -x0**2, 0, 0 ], 
                                  [ 0, 0, -x0**2*sinh(x1)**2, 0 ],
                                  [ 0, 0, 0, -x0**2*sinh(x1)**2*sin(x2)**2 ]
                             ])
        
        # An array detailing the solution.
        solution_array = [ metric, coordinate_set, index_config, cosmological_constant ]
        return solution_array

    def kerr(self):
        """
        Description
        ===========
        Returns Kerr metric.
        Examples
        ========
        >>> print(Solution().kerr())
        >>> 
        LaTeX representation
        ====================
        """
        x0, x1, x2, x3 = symbols('x0 x1 x2 x3')
        a, J, M, c, G, r, delt, sigm = symbols('a J M c G r Delta Sigma')
        a = (J/(M*c))
        rs = (2*G*M/(c**2))
        sigm = (x1**2 + (J/(M*c))**2 * cos(x2)**2)
        delt = (r**2 - x0 * (2*G*M/(c**2)) + (J/(M*c))**2)
        kerr_metric = Matrix([
                                    [ (1 - rs * x1 / (x1**2 + (J/(M*c))**2 * cos(x2)**2) ), 0, 0, (2*G*M/(c**2))*x1*(J/(M*c))*sin(x2)**2 / (x1**2 + (J/(M*c))**2 * cos(x2)**2) ], 
                                    [ 0, -1 * ( (r**2 - x0 * (2*G*M/(c**2)) + (J/(M*c))**2) / (x1**2 + (J/(M*c))**2 * cos(x2)**2) ), 0, 0 ], 
                                    [ 0, 0, -1 * (x1**2 + (J/(M*c))**2 * cos(x2)**2), 0 ],
                                    [ (2*G*M/(c**2))*x1*(J/(M*c))*sin(x2)**2 / (x1**2 + (J/(M*c))**2 * cos(x2)**2), 0, 0, -1 * (x1**2 + (J/(M*c))**2 + (rs*x1*(J/(M*c))**2/(x1**2 + (J/(M*c))**2 * cos(x2)**2))*sin(x2))*sin(x2) ]
                                ])

        return kerr_metric

    def alcubierre(self):
        """
        Description
        ===========
        Returns the famous Alcubierre 'warp-drive' metric solution.
        Examples
        ========
        >>> from sympy import *
        >>> print(Solution().alcubierre())
        >>> 
        LaTeX representation
        ====================
        """
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
    
    def ellis(self):
        """
        Description
        ===========
        Returns the original wormhole solution.
        Examples
        ========
        >>> print(Solution().ellis())
        >>> 
        LaTeX representation
        ====================
        """

        ellis_drainhole_metric = Matrix([
                                               [ 1, 0, 0, 0 ], 
                                               [ 0, - 1, 0, 0 ], 
                                               [ 0, 0, - ( k**2 + x1 ** 2 ), 0 ], 
                                               [ 0, 0, 0, - (k**2 + x1 ** 2) * sin(x2)**2 ]
                                           ])
        return ellis_drainhole_metric
    
    def kerns_wild(self):
        """
        Description
        ===========
        Returns Kerns-Wild metric.
        Examples
        ========
        >>> print(Solution().kerns_wild())
        >>> 
        LaTeX representation
        ====================
        """
        return kerns_wild_metric

    def double_kerr(self):
        """
        Description
        ===========
        Returns Double-Kerr metric.
        Examples
        ========
        >>> print(Solution().double_kerr())
        >>> 
        LaTeX representation
        ====================
        """
        return double_kerr_metric

    def khan_penrose(self):
        """
        Description
        ===========
        Returns Khan metric.
        Examples
        ========
        >>> print(Solution().khan_penrose())
        >>> 
        LaTeX representation
        ====================
        """
        return khan_metric

    def gowdy(self):
        """
        Description
        ===========
        Returns Gowdy metric.
        Examples
        ========
        >>> print(Solution().gowdy())
        >>> 
        LaTeX representation
        ====================
        """
        return gowdy_metric

    def ehlers(self):
        """
        Description
        ===========
        Returns Ehlers metric.
        Examples
        ========
        >>> print(Solution().ehlers())
        >>> 
        LaTeX representation
        ====================
        """
        return ehlers_metric

    def weyl(self):
        """
        Description
        ===========
        Returns Weyl metric.
        Examples
        ========
        >>> print(Solution().weyl())
        >>> 
        LaTeX representation
        ====================
        """
        return weyl_metric

    def beck(self):
        """
        Description
        ===========
        Returns Beck metric.
        Examples
        ========
        >>> print(Solution().beck())
        >>> 
        LaTeX representation
        ====================
        """
        return beck_metric

    def ernst(self):
        """
        Description
        ===========
        Returns Ernst metric.
        Examples
        ========
        >>> print(Solution().ernst())
        >>> 
        LaTeX representation
        ====================
        """
        return ernst_metric

    def kasner(self):
        """
        Description
        ===========
        Returns Kanser metric.
        Examples
        ========
        >>> print(Solution().kasner())
        >>> 
        LaTeX representation
        ====================
        """
        return kasner_metric

    def kruskal_szekeres(self):
        """
        Description
        ===========
        Returns Kruskal Szekeres metric.
        Examples
        ========
        >>> print(Solution().kruskal_szekeres())
        >>> 
        LaTeX representation
        ====================
        """
        return kruskal_szekeres_metric


    #Electrovacum solutions.

    def reissner_nordstrom(self):
        """
        Description
        ===========
        Returns Reissner Nordstrom metric.
        Examples
        ========
        >>> print(Solution().reissner_nordstrom())
        >>> 
        LaTeX representation
        ====================
        """
        
        G, M, c, Q, k = symbols('G M c Q k')
        rs = 2 * G * M / ( c**2 )
        rq = Q**2 * G * k / c**4
        reissner_nordstrom_spacetime = Matrix([
                                                  [ (1 + rs / x1 + rq**2 / x0**2), 0, 0, 0 ], 
                                                  [ 0, -1 * (1 + rs / x1 + rq**2 / x0**2)**(-1), 0, 0 ], 
                                                  [ 0, 0, -x1**2, 0 ], 
                                                  [ 0, 0, 0, -x1**2 * sin(x2)**2 ]
                                              ])
        
        return kruskal_szekeres_metric

    def kerr_newman(self):
        """
        Description
        ===========
        Returns Kerr-Newman metric.
        Examples
        ========
        >>> print(Solution().kerr_newman())
        >>> 
        LaTeX representation
        ====================
        """
        
        x0, x1, x2, x3 = symbols('t r psi theta')
        G, M, c, Q, k = symbols('G M c Q k')
        rs = 2 * G * M / ( c**2 )
        rq = Q**2 * G * k / c**4
        kerr_newman_metric = Matrix([
                                           [ (1 + rs / x1 + rq**2 / x0**2), 0, 0, 0 ], 
                                           [ 0, -1 * (1 + rs / x1 + rq**2 / x0**2)**(-1), 0, 0 ], 
                                           [ 0, 0, -x1**2, 0 ], 
                                           [ 0, 0, 0, -x1**2 * sin(x2)**2 ]
                                       ])
        
        return kerr_newman_metric

    def melvin(self):
        """
        Description
        ===========
        Returns Melvin metric.
        Examples
        ========
        >>> print(Solution().melvin())
        >>> 
        LaTeX representation
        ====================
        """
        return melvin_metric

    def garfinkle_melvin(self):
        """
        Description
        ===========
        Returns Garfinkle Melvin metric.
        Examples
        ========
        >>> print(Solution().garfinkle_melvin())
        >>> 
        LaTeX representation
        ====================
        """
        return garfinkle_melvin_metric

    def bertotti_robinson(self):
        """
        Description
        ===========
        Returns Bertotti Robinson metric.
        Examples
        ========
        >>> print(Solution().bertotti_robinson())
        >>> 
        LaTeX representation
        ====================
        """
        return bertotti_robinson_metric

    def vaidya(self):
        """
        Description
        ===========
        Returns Vaidya metric.
        Examples
        ========
        >>> print(Solution().vaidya())
        >>> 
        LaTeX representation
        ====================
        """
        return vaidya_metric

    def ozsvath_schucking(self):
        """
        Description
        ===========
        Returns the ozsvath schucking metric.
        Examples
        ========
        >>> print(Solution().ozsvath_schucking())
        >>> 
        LaTeX representation
        ====================
        """
        ozsvath_schucking_metric = Matrix([
                                                 [ 1, 0, -2*x3, 0 ], 
                                                 [ 0, 0, 1*x3, 0 ], 
                                                 [ -2*x3, 1*x3, -1, 1 ], 
                                                 [ 0, 0, 1, 1 ]
                                             ])
        return ozsvath_schucking_metric
    
    def godel(self):
        """
        Description
        ===========
        Returns Godel metric. A famous classic spacetime which describes time travel.
        Examples
        ========
        >>> print(Solution().godel())
        >>> 
        LaTeX representation
        ====================
        ds^{2}={\frac {1}{2\omega ^{2}}}\left[-(dt+e^{x}dy)^{2}+dx^{2}+{\tfrac {1}{2}}e^{2x}dy^{2}+dz^{2}\right],\qquad -\infty <t,x,y,z<\infty ,} {\displaystyle ds^{2}={\frac {1}{2\omega ^{2}}}\left[-(dt+e^{x}dy)^{2}+dx^{2}+{\tfrac {1}{2}}e^{2x}dy^{2}+dz^{2}\right],\qquad -\infty <t,x,y,z<\infty
        """
        
        f = Rational('1/2') * w**(-2)
        godel_metric = Matrix([
                                      [ f, 0, f * 2*E**(2 * x1), 0 ], 
                                      [ 0, -1, 0, 0 ], 
                                      [ f * 2*E**(2 * x1), 0, -f*Rational('1/2')*E**x1, 0 ], 
                                      [ 0, 0, 0, -f ]
                                  ])
        
        return godel_metric
    
    def gem(self):    
        """
        Description
        ===========
        Returns the classic black hole solution. Uncharged and rotationally stationary.
        Examples
        ========
        >>> print(Solution().schwarzschild())
        >>> 
        LaTeX representation
        ====================
        """
        x0, x1, x2, x3 = symbols('x0 x1 x2 x3')
        c = symbols('c')
        Ph = symbols('Phi')(x0)
        ax = symbols('ax')(x1)
        ay = symbols('ay')(x2)
        az = symbols('az')(x3)
        
        minkowski_metric = Matrix([
                                      [ 1, 0, 0, 0 ], 
                                      [ 0, -1, 0, 0 ], 
                                      [ 0, 0, -1, 0 ], 
                                      [ 0, 0, 0, -1 ]
                                  ])
        
        h_tilde_tensor = Matrix([
                                    [ 4*Ph / c**2, - ax/c**2, - ax/c**2, - az/c**2 ], 
                                    [ - ax/c**2, 0, 0, 0 ], 
                                    [ - ay/c**2, 0, 0, 0 ], 
                                    [ - az/c**2, 0, 0, 0 ]
                                ])
        h_tilde_scalar = 0
        gravitomagnetic_metric = minkowski_metric + h_tilde_tensor + Rational('1/2') * minkowski_metric * h_tilde_scalar
        
        
        return gravitomagnetic_metric
    
    
    def alt_gem(self):    
        """
        Description
        ===========
        Returns the classic black hole solution. Uncharged and rotationally stationary.
        Examples
        ========
        >>> print(Solution().schwarzschild())
        >>> 
        LaTeX representation
        ====================
        """
        x0, x1, x2, x3 = symbols('x0 x1 x2 x3')
        c = symbols('c')
        Ph = symbols('Phi')(x0)
        ax = symbols('ax')(x1)
        ay = symbols('ay')(x2)
        az = symbols('az')(x3)
        
        
        
        minkowski_metric = Matrix([
                                      [ 1, 0, 0, 0 ], 
                                      [ 0, -1, 0, 0 ], 
                                      [ 0, 0, -1, 0 ], 
                                      [ 0, 0, 0, -1 ]
                                  ])
        
        h_tilde_tensor = Matrix([
                                    [ 2*Ph / c**2, - ax/c**2, - ax/c**2, - az/c**2 ], 
                                    [ - ax/c**2, Ph / c**2, 0, 0 ], 
                                    [ - ay/c**2, 0, Ph / c**2, 0 ], 
                                    [ - az/c**2, 0, 0, Ph / c**2 ]
                                ])
        h_tilde_scalar = 0
        gravitomagnetic_metric = minkowski_metric + h_tilde_tensor + Rational('1/2') * minkowski_metric * h_tilde_scalar
        
        
        return gravitomagnetic_metric
