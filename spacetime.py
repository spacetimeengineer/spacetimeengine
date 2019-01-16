#!/usr/bin/env python
from sympy import *

class SpaceTime:
    def __init__(self, metric_parameter, coordinate_set_parameter):
        # Initializes metric tensor class object.
        self.metric_coefficients = metric_parameter
        # Initializes inverse metric tensor class object.
        self.inverse_metric_coefficients = simplify(metric_parameter.inv())
        # Initializes coordinate set class object.
        self.coordinate_set = coordinate_set_parameter
        # Declares ( gravitational field ) connection class object.
        self.connection_coefficients = Matrix([
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
        
        # Declares Riemann curvature tensor class object.
        self.riemann_coefficients = Matrix([    
                                               [    
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
                                               ],
                                               [    
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
                                               ],
                                               [    
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
                                               ],
                                               [    
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
                                               ]    
                                           ])  
        
        self.riemann_coefficients_dddd = Matrix([    
                                                   [    
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
                                                   ],
                                                   [    
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
                                                   ],
                                                   [    
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
                                                   ],
                                                   [    
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
                                                   ]    
                                               ])  

        # Declares Ricci curvature tensor class object.
        self.ricci_coefficients = Matrix([
                                            [ 0, 0, 0, 0 ], 
                                            [ 0, 0, 0, 0 ], 
                                            [ 0, 0, 0, 0 ], 
                                            [ 0, 0, 0, 0 ]
                                        ])
        
        # Declares Ricci curvature tensor class object.
        self.ricci_scalar = 0
        
        # Declares Einstein curvature tensor class object.
        self.einstein_coefficients = Matrix([    
                                                [ 0, 0, 0, 0 ], 
                                                [ 0, 0, 0, 0 ], 
                                                [ 0, 0, 0, 0 ], 
                                                [ 0, 0, 0, 0 ]
                                           ])
        # Declares stress-energy tensor class object.
        self.stress_energy_coefficients = Matrix([
                                                     [ 0, 0, 0, 0 ], 
                                                     [ 0, 0, 0, 0 ], 
                                                     [ 0, 0, 0, 0 ], 
                                                     [ 0, 0, 0, 0 ]
                                                 ])
        # Declares cosmological constant class object.
        self.cosmological_constant = 0
        
        """
        Initializing object functions
        =============================
        """
        
        self.set_all_connection_coefficients("udd")
        #self.set_all_connection_coefficients("ddd")
        self.set_all_riemann_coefficients("uddd")
        #self.set_all_riemann_coefficients("dddd")
        self.set_all_ricci_coefficients("dd")
        #self.set_all_ricci_coefficients("uu")
        self.set_ricci_scalar()
        self.set_all_einstein_coefficients("dd")
        #self.set_all_einstein_coefficients("uu")
        self.set_all_stress_energy_coefficients("dd")
        #self.set_all_stress_energy_coefficients("uu")
        #self.set_all_weyl_coefficients()
        
    
    """
    Metric coefficient functions
    ============================
    """
    
    # Gets a single metric coefficients from class object.
    def get_metric_coefficient(self, index_config, mu, nu):
        if (index_config == "uu"):
            return self.inverse_metric_coefficients[mu, nu]
        elif(index_config == "dd"):
            return self.metric_coefficients[mu, nu]
        else:
            print("Invalid index_config string.")
    
    # Sets a single metric coefficient equal to a given expression.
    def set_metric_coefficient(self, index_config, mu, nu, expression):
        if (index_config == "uu"):
            self.inverse_metric_coefficients[mu,nu] = expression
        elif(index_config == "dd"):
            self.metric_coefficients[mu,nu] = expression
    
    # Prints a single metric tensor coefficient.
    def print_metric_coefficient(self, index_config, mu, nu):
        if (index_config == "uu"):
            print("")
            pprint(Eq(Symbol('g^%s%s' % (mu, nu)), self.inverse_metric_coefficients[mu,nu]))
        elif(index_config == "dd"):
            print("")
            pprint(Eq(Symbol('g_%s%s' % (mu, nu)), self.metric_coefficients[mu,nu]))
        
    # Prints all metric tensor coefficients.
    def print_all_metric_coefficients(self, index_config):
        if (index_config == "uu"):
            for mu in range(len(self.coordinate_set)):
                for nu in range(len(self.coordinate_set)):
                    self.print_metric_coefficient(index_config, mu, nu)
        elif(index_config == "dd"):
            for mu in range(len(self.coordinate_set)):
                for nu in range(len(self.coordinate_set)):
                    self.print_metric_coefficient(index_config, mu, nu)
        else:
            print("Invalid index_config string.")

    """
    Connection coefficient functions
    ================================
    """       
    
    # Gets a single connection coefficients from class object.
    def get_connection_coefficient(self, index_config, i, k, l):
        return self.connection_coefficients[i,k][l]
    
    # Sets a single connection coefficient equal to a given expression.
    def set_connection_coefficient(self, index_config, i, k, l, expression):
        if(index_config == "udd"):
            self.connection_coefficients[i,k][l] = expression
        elif(index_config == "ddd"):
            pass
            # We need a new object for the "ddd" index_config
        else:
            print("Invalid index_config string.")        
    
    # Sets all connection coefficient values for reuse. Allows for the removal of redundant calculations.
    def set_all_connection_coefficients(self, index_config):
        if(index_config == "udd"):
            for i in range(len(self.coordinate_set)):
                for k in range(len(self.coordinate_set)):
                    for l in range(len(self.coordinate_set)):
                        self.set_connection_coefficient(index_config, i, k, l, self.compute_connection_coefficient(index_config, i, k, l))
        elif(index_config == "ddd"):
            for i in range(len(self.coordinate_set)):
                for k in range(len(self.coordinate_set)):
                    for l in range(len(self.coordinate_set)):
                        self.set_connection_coefficient(index_config, i, k, l, self.compute_connection_coefficient(index_config, i, k, l))
        else:
            print("Invalid index_config string.")

    # Computes a single connection coefficient.
    def compute_connection_coefficient(self, index_config, i, k, l):
        connection = 0
        if index_config == "udd":
            for m in range(len(self.coordinate_set)):
                connection = connection+Rational('1/2')*self.inverse_metric_coefficients[m,i]*(diff(self.metric_coefficients[k,m], self.coordinate_set[l])+diff(self.metric_coefficients[l,m], self.coordinate_set[k])-diff(self.metric_coefficients[k,l], self.coordinate_set[m]))
            connection = simplify(connection)
            return connection
        elif index_config == "ddd":
            connection = Rational('1/2')*(diff(self.metric_coefficients[i,k], self.coordinate_set[l])+diff(self.metric_coefficients[i,l], self.coordinate_set[k])-diff(self.metric_coefficients[k,l], self.coordinate_set[i]))
            connection = simplify(connection)
            return connection
        else:
            print("Invalid index_config string.")
    
    # Prints a single connection coefficient.
    def print_connection_coefficient(self, index_config, i, j, k ):
        if(index_config == "udd"):
            print("")
            pprint(Eq(Symbol('Gamma^%s_%s%s' % (i, j, k)),self.get_connection_coefficient(index_config, i, j, k )))
        elif(index_config == "ddd"):
            print("")
            #pprint(Eq(Symbol('Gamma_%s%s%s' % (i, j, k)),self.get_connection_coefficient_ddd(index_config, i, j, k )))
        else:
            print("Invalid index_config string.")
    
    # Prints all connection coefficients.
    def print_all_connection_coefficients(self, index_config):
        if(index_config == "udd"):
            for lam in range(len(self.coordinate_set)):
                for mu in range(len(self.coordinate_set)):
                    for nu in range(len(self.coordinate_set)):
                        print("")
                        self.print_connection_coefficient(index_config, lam, mu, nu )
        elif(index_config == "ddd"):
            for lam in range(len(self.coordinate_set)):
                for mu in range(len(self.coordinate_set)):
                    for nu in range(len(self.coordinate_set)):
                        print("")
                        self.print_connection_coefficient(index_config, lam, mu, nu )
        else:
            print("Invalid index_config string.")
    
    """
    Riemann coefficient functions
    =============================
    """      
    
    # Gets a single Riemann coefficients from class object.
    def get_riemann_coefficient(self, index_config, rho, sig, mu, nu):
        # MUST TEST
        if(index_config == "uddd"):
            return self.riemann_coefficients[rho*16/len(self.coordinate_set)+sig][mu][nu]
        # MUST TEST
        elif(index_config == "dddd"):
            return self.riemann_coefficients_dddd[rho*16/len(self.coordinate_set)+sig][mu][nu]
        else:
            print("Invalid index_config string.")  
    
    # Sets a single Riemann coefficient equal to a given expression.
    def set_riemann_coefficient(self, index_config, rho, sig, mu, nu, expression):
        if(index_config == "uddd"):
            # MUST TEST
            self.riemann_coefficients[rho*16/len(self.coordinate_set)+sig][mu][nu] = expression
        elif(index_config == "dddd"):
            # MUST TEST
            pass
            # self.riemann_coefficients_dddd[rho, sig][mu, nu] = expression
        else:
            print("Invalid index_config string.")        
    
    # Sets all Riemann coefficients values for reuse. Allows for the removal of redundant calculations.
    def set_all_riemann_coefficients(self, index_config):
        if index_config == "uddd":
            for rho in range(len(self.coordinate_set)):
                for sig in range(len(self.coordinate_set)):
                    for mu in range(len(self.coordinate_set)):
                        for nu in range(len(self.coordinate_set)):
                            self.set_riemann_coefficient(index_config, rho, sig, mu, nu, self.compute_riemann_coefficient(index_config, rho, sig, mu, nu))
        elif index_config == "dddd":
            for rho in range(len(self.coordinate_set)):
                for sig in range(len(self.coordinate_set)):
                    for mu in range(len(self.coordinate_set)):
                        for nu in range(len(self.coordinate_set)):
                            # FIXME 
                            # TODO
                            pass
                            #self.set_riemann_coefficient(index_config, rho, sig, mu, nu, self.compute_riemann_coefficient_dddd(index_config, rho, sig, mu, nu))
        else:
            print("Invalid index_config string.")
    
    # Computes a single Riemann tensor coefficient.
    def compute_riemann_coefficient(self, index_config, rho, sig, mu, nu):
        riemann_coefficient = 0
        if index_config == "uddd":
            riemann_coefficient = diff(self.get_connection_coefficient("udd", rho, nu, sig), self.coordinate_set[mu]) - diff(self.get_connection_coefficient("udd", rho, mu, sig), self.coordinate_set[nu])    
            for lam in range(len(self.coordinate_set)):
                riemann_coefficient = riemann_coefficient + self.get_connection_coefficient("udd", rho, mu, lam)*self.get_connection_coefficient("udd", lam, nu, sig) - self.get_connection_coefficient("udd", rho, nu, lam)*self.get_connection_coefficient("udd", lam, mu, sig)
            riemann_coefficient = simplify(riemann_coefficient)
            return riemann_coefficient
        elif index_config == "dddd":
            riemann_coefficient = Rational('1/2')*(self.metric_coefficient("dd", rho, nu).diff(self.coordinate_set[sig]).diff(self.coordinate_set[mu]) + self.metric_coefficient("dd", sig, mu).diff(self.coordinate_set[rho]).diff(self.coordinate_set[nu])-self.metric_coefficient("dd", rho, mu).diff(self.coordinate_set[sig]).diff(self.coordinate_set[nu])-self.metric_coefficient("dd", sig, nu).diff(self.coordinate_set[rho]).diff(self.coordinate_set[mu]))
            for n in range(len(self.coordinate_set)):
                for p in range(len(self.coordinate_set)):
                    riemann_coefficient = riemann_coefficient + self.metric_coefficient("dd", n, p)*(self.get_connection_coefficient("udd", n, sig, mu)*self.get_connection_coefficient("udd", p, rho, nu)-self.get_connection_coefficient("udd", n, sig, nu)*self.get_connection_coefficient("udd", p, rho, mu))
            riemann_coefficient = simplify(riemann_coefficient)
            return riemann_coefficient
        else:
            print("Invalid index_config string.")
        

    # Prints a single Riemann coefficient.
    def print_riemann_coefficient(self, index_config, rho, sig, mu, nu):
        if index_config == "uddd":
            print("")
            pprint(Eq(Symbol('R^%s_%s%s%s' % (rho, sig, mu, nu)), self.get_riemann_coefficient(index_config, rho, sig, mu, nu)))
        elif index_config == "dddd":
            print("")
            pprint(Eq(Symbol('R_%s%s%s%s' % (rho, sig, mu, nu)), self.get_riemann_coefficient(index_config, rho, sig, mu, nu)))
        else:
            print("Invalid index_config string.")
            
    # Prints all connection coefficients.
    def print_all_riemann_coefficients(self, index_config):
        if index_config == "uddd":
            for rho in range(len(self.coordinate_set)):
                for sig in range(len(self.coordinate_set)):
                    for mu in range(len(self.coordinate_set)):
                        for nu in range(len(self.coordinate_set)):
                            self.print_riemann_coefficient(index_config, rho, sig, mu, nu)
        elif index_config == "dddd":
            for rho in range(len(self.coordinate_set)):
                for sig in range(len(self.coordinate_set)):
                    for mu in range(len(self.coordinate_set)):
                        for nu in range(len(self.coordinate_set)):
                            self.print_riemann_coefficient(index_config, rho, sig, mu, nu)
        else:
            print("Invalid index_config string.")
    
    
    """
    Ricci coefficient functions
    =============================
    """      
    
    # Gets a single Ricci coefficient from class object.
    def get_ricci_coefficient(self, index_config, mu, nu):
        if (index_config == "uu"):
            # Need to calculate R^{\mu\nu}
            pass
        elif(index_config == "dd"):
            return self.ricci_coefficients[mu,nu]
        else:
            print("Invalid index_config string.")
    
    # Sets a single Ricci coefficient from class object.
    def set_ricci_coefficient(self, index_config, mu, nu, expression):
        if (index_config == "uu"):
            # Need to calculate R^{\mu\nu}
            pass
        elif(index_config == "dd"):
            self.ricci_coefficients[mu,nu] = expression
        else:
            print("Invalid index_config string.")
    
    # Sets all Ricci coefficient values for reuse. Allows for the removal of redundant calculations.
    def set_all_ricci_coefficients(self, index_config):
        if(index_config == "uu"):
            for mu in range(len(self.coordinate_set)):
                for nu in range(len(self.coordinate_set)):
                    self.set_ricci_coefficient(index_config, mu, nu, self.compute_ricci_coefficient(index_config, mu, nu))
        elif(index_config == "dd"):
            for mu in range(len(self.coordinate_set)):
                for nu in range(len(self.coordinate_set)):
                    self.set_ricci_coefficient(index_config, mu, nu, self.compute_ricci_coefficient(index_config, mu, nu))
    
    # Computes a single Ricci tensor coefficient.
    def compute_ricci_coefficient(self, index_config, mu, nu):
        if index_config == "dd":
            ricci_coefficient = 0
            for lam in range(len(self.coordinate_set)):
                ricci_coefficient = ricci_coefficient + self.get_riemann_coefficient("uddd", lam, mu, lam, nu)
            ricci_coefficient = simplify(ricci_coefficient)
        elif index_config == "uu":
            print("")
        elif index_config == "ud" or index_config == "du":
            print("")
        else:
            print("Invalid index_config string.")
        return ricci_coefficient
    
    # Prints a single Ricci coefficient.
    def print_ricci_coefficient(self, index_config, mu, nu):
        if (index_config == "uu"):
            print("")
            pprint(Eq(Symbol('R^%s%s' % (mu, nu)), self.get_ricci_coefficient(index_config, mu, nu)))
        elif(index_config == "dd"):
            print("")
            pprint(Eq(Symbol('R_%s%s' % (mu, nu)), self.get_ricci_coefficient(index_config, mu, nu)))
        else:
            print("Invalid index_config string.")
    
    # Prints all Ricci coefficients.
    def print_all_ricci_coefficients(self, index_config):
        for mu in range(len(self.coordinate_set)):
            for nu in range(len(self.coordinate_set)):
                self.print_ricci_coefficient(index_config, mu, nu)
    
    
    """
    Ricci scalar functions
    ======================
    """
    
    # Gets Ricci scalar from class object.
    def get_ricci_scalar(self):
        return self.ricci_scalar  
    
    # Sets Ricci scalar from class object.
    def set_ricci_scalar(self):
        self.ricci_scalar = self.compute_ricci_scalar()
    
    # Computes Ricci scalar.
    def compute_ricci_scalar(self):
        ricci_scalar = 0
        for mu in range(len(self.coordinate_set)):
            for nu in range(len(self.coordinate_set)):
                ricci_scalar = ricci_scalar + self.inverse_metric_coefficients[mu, nu] * self.get_ricci_coefficient("dd", mu, nu)
        ricci_scalar = simplify(ricci_scalar)
        return ricci_scalar
    
    # Prints Ricci scalar.
    def print_ricci_scalar(self):
        print("")
        pprint(Eq(Symbol('R'), self.get_ricci_scalar()))
    
    """
    Einstein tensor functions
    =========================
    """
    
    # Gets a single Einstein coefficient from class object.
    def get_einstein_coefficient(self, index_config, mu, nu):
        if (index_config == "uu"):
            pass
            # Need to calculate R^{\mu\nu}
        elif(index_config == "dd"):
            return self.einstein_coefficients[mu, nu]
        else:
            print("Invalid index_config string.")
    
    # Sets a single Ricci coefficient from class object.
    def set_einstein_coefficient(self, index_config, mu, nu, expression):
        if (index_config == "uu"):
            pass
            # Need to calculate R^{\mu\nu}
        elif(index_config == "dd"):
            self.einstein_coefficients[mu, nu] = expression 
        else:
            print("Invalid index_config string.")  
    
    # Sets all Einstein coefficient values for reuse. Allows for the removal of redundant calculations.
    def set_all_einstein_coefficients(self, index_config):
        if (index_config=="uu"):
            for mu in range(len(self.coordinate_set)):
                for nu in range(len(self.coordinate_set)):
                    self.set_einstein_coefficient(index_config, mu, nu, self.compute_einstein_coefficient(index_config, mu, nu))
        elif (index_config == "dd"):
            for mu in range(len(self.coordinate_set)):
                for nu in range(len(self.coordinate_set)):
                    self.set_einstein_coefficient(index_config, mu, nu, self.compute_einstein_coefficient(index_config, mu, nu))
    
    # Computes a single Einstein tensor coefficient.
    def compute_einstein_coefficient(self, index_config, mu, nu):
        einstein_coefficient = 0
        if index_config == "dd":
            einstein_coefficient = self.get_ricci_coefficient("dd", mu, nu) - Rational('1/2') * self.get_ricci_scalar() * self.metric_coefficients[mu,nu]
            einstein_coefficient = simplify(einstein_coefficient)
        elif index_config == "uu":
            print("")
        elif index_config == "ud" or index_config == "du":
            print("")
        else:
            print("Invalid index_config string.")
        return einstein_coefficient
    
    # Prints a single Einstein coefficient.
    def print_einstein_coefficient(self, index_config, mu, nu):
        if (index_config == "uu"):
            pass
            # Need to calculate R^{\mu\nu}
        elif(index_config == "dd"):
            print("")
            pprint(Eq(Symbol('G_%s%s' % (mu, nu)), self.get_einstein_coefficient(index_config, mu, nu)))
        else:
            print("Invalid index_config string.")  
    
    # Prints all Ricci coefficients.
    def print_all_einstein_coefficients(self, index_config):
        for mu in range(len(self.coordinate_set)):
            for nu in range(len(self.coordinate_set)):
                self.print_einstein_coefficient(index_config, mu, nu)
    
    
    """
    Stress-energy-momentum tensor functions
    =======================================
    """
    
    # Gets a single stress-energy coefficient from class object.
    def get_stress_energy_coefficient(self, index_config, mu, nu):
        if (index_config == "uu"):
            pass
            # Need to calculate R^{\mu\nu}
        elif(index_config == "dd"):
            return self.stress_energy_coefficients[mu, nu]
        else:
            print("Invalid index_config string.")
    
    # Sets a single stress-energy coefficient from class object.
    def set_stress_energy_coefficient(self, index_config, mu, nu, expression):
        if (index_config == "uu"):
            pass
            # Need to calculate R^{\mu\nu}
        elif(index_config == "dd"):
            self.stress_energy_coefficients[mu, nu] = expression
        else:
            print("Invalid index_config string.")
    
    # Sets all stress-energy coefficient values for reuse. Allows for the removal of redundant calculations.
    def set_all_stress_energy_coefficients(self, index_config):
        if (index_config=="uu"):
            for mu in range(len(self.coordinate_set)):
                for nu in range(len(self.coordinate_set)):
                    self.set_stress_energy_coefficient(index_config, mu, nu, self.compute_stress_energy_coefficient(index_config, mu, nu))
        elif (index_config == "dd"):
            for mu in range(len(self.coordinate_set)):
                for nu in range(len(self.coordinate_set)):
                    self.set_stress_energy_coefficient(index_config, mu, nu, self.compute_stress_energy_coefficient(index_config, mu, nu))   
    
    # Computes a single stress-energy tensor coefficient.
    def compute_stress_energy_coefficient(self, index_config, mu, nu):
        stress_energy_coefficient = 0
        c, G = symbols('c G')
        if index_config == "dd":
            stress_energy_coefficient = c**4/(8*pi*G)*self.get_einstein_coefficient(index_config, mu, nu) + c**4/(8*pi*G) * self.cosmological_constant * self.metric_coefficients[mu,nu]
        elif index_config == "uu":
            stress_energy_coefficient = c**4/(8*pi*G)*self.get_einstein_coefficient(index_config, mu, nu)
        elif index_config == "ud" or index_config == "du":
            pass
        else:
            print("Invalid index_config string.")
        stress_energy_coefficient = simplify(stress_energy_coefficient)
        return stress_energy_coefficient

    # Prints a single stress-energy coefficient.
    def print_stress_energy_coefficient(self, index_config, mu, nu):
            print("")
            pprint(Eq(Symbol('T_%s%s' % (mu, nu)), self.get_stress_energy_coefficient(index_config, mu, nu)))
    
    # Prints all stress-energy coefficients.
    def print_all_stress_energy_coefficients(self, index_config):
        for mu in range(len(self.coordinate_set)):
            for nu in range(len(self.coordinate_set)):
                self.print_stress_energy_coefficient(index_config, mu, nu)
