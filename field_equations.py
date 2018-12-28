#!/usr/bin/env python
import json
from sympy import *



class Metric:
    
    def __init__(self, m, cs):
        self.metric = m
        self.inverse_metric = m.inv()
        self.coordinate_set = cs
        #self.infentesimal_displacement_four_vector
        self.x_velocity = None
        self.y_velocity = None
        self.z_velocity = None
        self.tau_velocity = None
        
        
    def line_element(self):
        """
        Description
        ===========
        Returns the metric line element.

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
        for i in range(len(self.coordinate_set)):
            for j in range(len(self.coordinate_set)):
                line_element = line_element + self.coordinate_set[i]*self.coordinate_set[j] * self.metric[i,j]
        line_element = simplify(line_element)
        return line_element

    def metric_tensor(self):
        """
        Description
        ===========
        Returns a list of all metric element equalities.
        
        Example
        =======

        LaTeX representation
        ====================
        """
        return self.metric
        
    def inverse_metric_tensor(self):
        return self.inverse_metric

    
    def connection_coefficient(self, index_config, i, k, l):
        connection = 0
        if index_config == "udd":
            for m in range(len(self.coordinate_set)):
                connection = connection+Rational('1/2')*self.inverse_metric[m,i]*(diff(self.metric[k,m], self.coordinate_set[l])+diff(self.metric[l,m], self.coordinate_set[k])-diff(self.metric[k,l], self.coordinate_set[m]))
            connection = simplify(connection)
        elif index_config == "ddd":
            connection = Rational('1/2')*(diff(self.metric[i,k], self.coordinate_set[l])+diff(self.metric[i,l], self.coordinate_set[k])-diff(self.metric[k,l], self.coordinate_set[i]))
            connection = simplify(connection)
        else:
            print("Invalid index_config string.")
        return connection
    
    def riemann_coefficient(self, index_config, rho, sig, mu, nu):
        if index_config == "uddd":
            riemann_coefficient = diff(self.connection_coefficient("udd", rho, nu, sig), self.coordinate_set[mu]) - diff(self.connection_coefficient("udd", rho, mu, sig), self.coordinate_set[nu])    
            for lam in range(len(self.coordinate_set)):
                #There is a problem here.
                riemann_coefficient = riemann_coefficient + self.connection_coefficient("udd", rho, mu, lam)*self.connection_coefficient("udd", lam, nu, sig) - self.connection_coefficient("udd", rho, nu, lam)*self.connection_coefficient("udd", lam, mu, sig)
            riemann_coefficient = simplify(riemann_coefficient)
            # Should remove this from function and place in a listing function.
            #pprint(Eq(Symbol('R^%s_%s%s%s' % (rho, sig, mu, nu)),riemann_coefficient))
        elif index_config == "dddd":
            print("")
        else:
            print("Invalid index_config string.")
        
        return riemann_coefficient
    
    def ricci_coefficient(self, index_config, mu, nu):
        if index_config == "dd":
            ricci_coefficient = 0
            for lam in range(len(self.coordinate_set)):
                #There is a problem here.
                ricci_coefficient = ricci_coefficient + self.riemann_coefficient("uddd", lam, mu, lam, nu)
            ricci_coefficient = simplify(ricci_coefficient)
            # Should remove this from function and place in a listing function.
            #pprint(Eq(Symbol('R^_%s%s' % (mu, nu)), ricci_coefficient))
        elif index_config == "uu":
            print("")
        elif index_config == "ud" or index_config == "du":
            print("")
        else:
            print("Invalid index_config string.")
        
        return ricci_coefficient

    def ricci_scalar(self):
        ricci_scalar = 0
        for mu in range(len(self.coordinate_set)):
            for nu in range(len(self.coordinate_set)):
                ricci_scalar = ricci_scalar + self.inverse_metric[mu, nu] * self.ricci_coefficient("dd", mu, nu)
        ricci_scalar = simplify(ricci_scalar)
        #pprint(Eq(Symbol('R'),ricci_scalar))
        return ricci_scalar

    def einstein_coefficient(self, index_config, mu, nu):
        ricci_scalar = self.ricci_scalar()
        if index_config == "dd":
            for mu in range(len(self.coordinate_set)):
                for nu in range(len(self.coordinate_set)):
                    einstein_coefficient = self.ricci_coefficient("dd", mu, nu) - Rational('1/2') * ricci_scalar * self.metric[mu,nu]
                    einstein_coefficient = simplify(einstein_coefficient)
                    #Remove and place in listing function.
                    pprint(Eq(Symbol('G_%s%s' % (mu, nu)), einstein_coefficient))
        elif index_config == "uu":
            print("")
        elif index_config == "ud" or index_config == "du":
            print("")
        else:
            print("Invalid index_config string.")
        
        return einstein_coefficient

    def stress_energy_coefficient(self, index_config, mu, nu):
        c, G = symbols('c G')
        if index_config == "dd":
            for mu in range(len(self.coordinate_set)):
                for nu in range(len(self.coordinate_set)):
                    stress_energy_coefficient = c**4/(8*pi*G)*self.einstein_coefficient("dd", mu, nu)
                    stress_energy_coefficient = simplify(stress_energy_coefficient)
                    #Remove and place in listing function.
                    pprint(Eq(Symbol('T_%s%s' % (mu, nu)), stress_energy_coefficient))
        elif index_config == "uu":
            print("")
        elif index_config == "ud" or index_config == "du":
            print("")
        else:
            print("Invalid index_config string.")
        
        return stress_energy_coefficient
        
    def proper_time_geodesics(self):
        return ricci_tensor
    
    def coordinate_time_geodesics(self):
        return ricci_tensor
    
    def proper_time_geodesic_deviation(self):
        return ricci_tensor
    
    def coordinate_time_geodesic_deviation(self):   
        return ricci_tensor
    
    def get_coordinate_four_velocity(self):
        """
        Description
        ===========
        Example
        =======
        LaTeX representation
        ====================
        """
        
        """
        Psuedocode
        ==========
        
        Using the line element solve for each velocity component with respect to coordinate time.
        
        """
        coordinate_four_veocity = Matrix([0, 0, 0, 0])
        line_element = get_line_element(metric, infinitesimal_displacement_set)
        pprint(line_element)
        coordinate_four_veocity[0]=solve(line_element, infinitesimal_displacement_set[0])
        coordinate_four_veocity[1]=solve(line_element, infinitesimal_displacement_set[1])
        coordinate_four_veocity[2]=solve(line_element, infinitesimal_displacement_set[2])
        #coordinate_four_veocity[3]=solve(line_element, infinitesimal_displacement_set[3])
        print("")
        print(coordinate_four_veocity[0])
        print("")
        print(coordinate_four_veocity[1])
        print("")
        print(coordinate_four_veocity[2])
        #print("")
        #print(coordinate_four_veocity[3])

        return coordinate_four_veocity
    
    def get_proper_four_velocity(self):
        """
        Description
        ===========
        Example
        =======
        LaTeX representation
        ====================
        """
        
        """
        Psuedocode
        ==========
        
        Using the line element solve for each velocity component with respect to proper time.
        
        """
        coordinate_four_veocity = Matrix([0, 0, 0, 0])
        line_element = get_line_element(metric, infinitesimal_displacement_set)
        pprint(line_element)
        coordinate_four_veocity[0]=solve(line_element, infinitesimal_displacement_set[0])
        coordinate_four_veocity[1]=solve(line_element, infinitesimal_displacement_set[1])
        coordinate_four_veocity[2]=solve(line_element, infinitesimal_displacement_set[2])
        #coordinate_four_veocity[3]=solve(line_element, infinitesimal_displacement_set[3])
        print("")
        print(coordinate_four_veocity[0])
        print("")
        print(coordinate_four_veocity[1])
        print("")
        print(coordinate_four_veocity[2])
        #print("")
        #print(coordinate_four_veocity[3])

        return coordinate_four_veocity
    
    def get_connection():
        return self.connection


