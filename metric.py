#!/usr/bin/env python
import json
from sympy import *
import field_equations


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
        return self.line_element

    def metric_tensor(self):
        return self.metric
        
    def inverse_metric_tensor(self):
        return self.inverse_metric
        
    def connection(self):
        return self.connection
        
    def riemann_tensor(self, index_config):
        return self.riemann_tensor

    def ricci_tensor(self):
        return self.ricci_tensor

    def ricci_scalar(self):
        return self.ricci_scalar

    def einstein_tensor(self):
        return self.einstein_tensor

    def stress_energy_tensor(self):
        return self.stress_energy_tensor
        
    def proper_time_geodesics(self):
        return self.proper_time_geodesics
    
    def coordinate_time_geodesics(self):
        return coordinate_time_geodesics
    
    def proper_time_geodesic_deviation_equations(self):
        return proper_time_geodesic_deviation_equations
    
    def coordinate_time_geodesic_deviation_equations(self):   
        return coordinate_time_geodesic_deviation_equations
    
    def get_coordinate_four_velocity(self):
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
    