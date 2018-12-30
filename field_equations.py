#!/usr/bin/env python
import json
from sympy import *

class Metric:
    
    def __init__(self, m, cs):
        self.metric = m
        self.inverse_metric = simplify(m.inv())
        self.coordinate_set = cs
        
    def line_element(self):
        line_element = 0
        one_forms = Matrix( [ [ 0 , 0 , 0 , 0 ], [ 0 , 0 , 0 , 0 ], [ 0 , 0 , 0 , 0 ], [ 0 , 0 , 0 , 0 ] ] )
        for i in range(len(self.coordinate_set)):
            for j in range(len(self.coordinate_set)):
                line_element = line_element + self.coordinate_set[i]*self.coordinate_set[j] * self.metric[i,j]
        line_element = simplify(line_element)
        return line_element

    def metric_tensor(self):
        return self.metric
    
    def metric_coefficient(self, index_config, mu, nu):
        if (index_config == "uu"):
            return self.inverse_metric[mu,nu]
        elif(index_config == "dd"):
            return self.metric[mu,nu]
        else:
            print("Invalid index_config string.")
        
    def list_metric_coefficients(self, index_config):
        if (index_config == "uu"):
            for mu in range(len(self.coordinate_set)):
                for nu in range(len(self.coordinate_set)):
                    pprint(Eq(Symbol('g^%s%s' % (mu, nu)), self.inverse_metric[mu,nu]))
        elif(index_config == "dd"):
            for mu in range(len(self.coordinate_set)):
                for nu in range(len(self.coordinate_set)):
                    print("")
                    pprint(Eq(Symbol('g_%s%s' % (mu, nu)), self.metric[mu,nu]))
        else:
            print("Invalid index_config string.")
    
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
    
    def list_connection_coefficients(self, index_config):
        if(index_config == "udd"):
            for lam in range(len(self.coordinate_set)):
                for mu in range(len(self.coordinate_set)):
                    for nu in range(len(self.coordinate_set)):
                        print("")
                        pprint(Eq(Symbol('Gamma^%s_%s%s' % (lam, mu, nu)),self.connection_coefficient(index_config, lam, mu, nu )))
        elif(index_config == "ddd"):
            for lam in range(len(self.coordinate_set)):
                for mu in range(len(self.coordinate_set)):
                    for nu in range(len(self.coordinate_set)):
                        print("")
                        pprint(Eq(Symbol('Gamma_%s%s%s' % (lam, mu, nu)),self.connection_coefficient(index_config, lam, mu, nu )))
        else:
            print("Invalid index_config string.")
    
    def riemann_coefficient(self, index_config, rho, sig, mu, nu):
        riemann_coefficient = 0
        if index_config == "uddd":
            riemann_coefficient = diff(self.connection_coefficient("udd", rho, nu, sig), self.coordinate_set[mu]) - diff(self.connection_coefficient("udd", rho, mu, sig), self.coordinate_set[nu])    
            for lam in range(len(self.coordinate_set)):
                riemann_coefficient = riemann_coefficient + self.connection_coefficient("udd", rho, mu, lam)*self.connection_coefficient("udd", lam, nu, sig) - self.connection_coefficient("udd", rho, nu, lam)*self.connection_coefficient("udd", lam, mu, sig)
            riemann_coefficient = simplify(riemann_coefficient)
        elif index_config == "dddd":
            riemann_coefficient = Rational('1/2')*(self.metric_coefficient("dd", rho, nu).diff(self.coordinate_set[sig]).diff(self.coordinate_set[mu]) + self.metric_coefficient("dd", sig, mu).diff(self.coordinate_set[rho]).diff(self.coordinate_set[nu])-self.metric_coefficient("dd", rho, mu).diff(self.coordinate_set[sig]).diff(self.coordinate_set[nu])-self.metric_coefficient("dd", sig, nu).diff(self.coordinate_set[rho]).diff(self.coordinate_set[mu]))
            for n in range(len(self.coordinate_set)):
                for p in range(len(self.coordinate_set)):
                    riemann_coefficient = riemann_coefficient + self.metric_coefficient("dd", n, p)*(self.connection_coefficient("udd", n, sig, mu)*self.connection_coefficient("udd", p, rho, nu)-self.connection_coefficient("udd", n, sig, nu)*self.connection_coefficient("udd", p, rho, mu))
            riemann_coefficient = simplify(riemann_coefficient)
        else:
            print("Invalid index_config string.")
        
        return riemann_coefficient
    
    def list_riemann_coefficients(self, index_config):
        if index_config == "uddd":
            for i in range(len(self.coordinate_set)):
                for j in range(len(self.coordinate_set)):
                    for k in range(len(self.coordinate_set)):
                        for l in range(len(self.coordinate_set)):
                            print("")
                            pprint(Eq(Symbol('R^%s_%s%s%s' % (i, j, k, l)), self.riemann_coefficient(index_config, i, j, k, l)))
        elif index_config == "dddd":
            for i in range(len(self.coordinate_set)):
                for j in range(len(self.coordinate_set)):
                    for k in range(len(self.coordinate_set)):
                        for l in range(len(self.coordinate_set)):
                            print("")
                            pprint(Eq(Symbol('R_%s%s%s%s' % (i, j, k, l)), self.riemann_coefficient(index_config, i, j, k, l)))
        else:
            print("Invalid index_config string.")
    
    def ricci_coefficient(self, index_config, mu, nu):
        if index_config == "dd":
            ricci_coefficient = 0
            for lam in range(len(self.coordinate_set)):
                ricci_coefficient = ricci_coefficient + self.riemann_coefficient("uddd", lam, mu, lam, nu)
            ricci_coefficient = simplify(ricci_coefficient)
        elif index_config == "uu":
            print("")
        elif index_config == "ud" or index_config == "du":
            print("")
        else:
            print("Invalid index_config string.")
        
        return ricci_coefficient

    def list_ricci_coefficients(self, index_config):
        for mu in range(len(self.coordinate_set)):
            for nu in range(len(self.coordinate_set)):
                print("")
                pprint(Eq(Symbol('R_%s%s' % (mu, nu)), self.ricci_coefficient(index_config, mu, nu)))
    
    def ricci_scalar(self):
        ricci_scalar = 0
        for mu in range(len(self.coordinate_set)):
            for nu in range(len(self.coordinate_set)):
                ricci_scalar = ricci_scalar + self.inverse_metric[mu, nu] * self.ricci_coefficient("dd", mu, nu)
        ricci_scalar = simplify(ricci_scalar)
        #pprint(Eq(Symbol('R'),ricci_scalar))
        return ricci_scalar

    def einstein_coefficient(self, index_config, mu, nu):
        einstein_coefficient = 0
        ricci_scalar = self.ricci_scalar()
        if index_config == "dd":
                einstein_coefficient = self.ricci_coefficient("dd", mu, nu) - Rational('1/2') * ricci_scalar * self.metric[mu,nu]
                einstein_coefficient = simplify(einstein_coefficient)
        elif index_config == "uu":
            print("")
        elif index_config == "ud" or index_config == "du":
            print("")
        else:
            print("Invalid index_config string.")
        
        return einstein_coefficient

    def list_einstein_coefficients(self, index_config):
        for mu in range(len(self.coordinate_set)):
            for nu in range(len(self.coordinate_set)):
                print("")
                pprint(Eq(Symbol('G_%s%s' % (mu, nu)), self.einstein_coefficient(index_config, mu, nu)))
    
    def stress_energy_coefficient(self, index_config, mu, nu, cosmological_constant):
        stress_energy_coefficient = 0
        c, G = symbols('c G')
        if index_config == "dd":
            stress_energy_coefficient = c**4/(8*pi*G)*self.einstein_coefficient("dd", mu, nu) + c**4/(8*pi*G) * cosmological_constant * self.metric[mu,nu]
        elif index_config == "uu":
            print("")
        elif index_config == "ud" or index_config == "du":
            print("")
        else:
            print("Invalid index_config string.")
        
        return simplify(stress_energy_coefficient)

    def list_stress_energy_coefficients(self, index_config):
        for mu in range(len(self.coordinate_set)):
            for nu in range(len(self.coordinate_set)):
                print("")
                pprint(Eq(Symbol('T_%s%s' % (mu, nu)), self.stress_energy_coefficient(index_config, mu, nu, Symbol('Lambda'))))
    
    def proper_time_geodesics(self, lam, mu, nu):
        for lam in range(len(self.coordinate_set)):
            acc = 0
            for mu in range(len(self.coordinate_set)):
                for nu in range(len(self.coordinate_set)):
                    acc = acc + self.connection_coefficient("udd",lam,mu,nu)*diff(self.coordinate_set[mu],Symbol('tau'))*diff(self.coordinate_set[nu],Symbol('tau'))
            expr = self.coordinate_set[lam].diff(Symbol('tau')).diff(Symbol('tau'))
            pprint(Eq(expr,acc))
            print("")

    def coordinate_time_geodesics(self):
        return ricci_tensor
    
    def proper_time_geodesic_deviation(self):
        return ricci_tensor
    
    def coordinate_time_geodesic_deviation(self):   
        return ricci_tensor
