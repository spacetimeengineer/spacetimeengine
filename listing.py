"""
    FIX: Need to figure out how to get symbols in a the indices in expressions like pprint(Eq(Symbol('Gamma^%s_%s%s' % (0, 0, 0))))
    Currently only a and x seem to work. I have not tried all.

"""

def list_metric_components(self, index_config):
    """
    Description
    ===========
    Prints the connection coefficients in a clear readable form.
    Example
    =======
    
    LaTeX representation
    ====================

    """
    if (index_config == "uu"):
        for mu in range(len(self.coordinate_set)):
            for nu in range(len(self.coordinate_set)):
                pprint(Eq(Symbol('g^%s%s' % (mu, nu))))
    elif(index_config == "dd"):
        for mu in range(len(self.coordinate_set)):
            for nu in range(len(self.coordinate_set)):
                pprint(Eq(Symbol('g_%s%s' % (mu, nu))))
    else:
        pass
            

def list_connection_components(connection):
    """
    Description
    ===========
    Prints the connection coefficients in a clear readable form.
    Example
    =======
    
    LaTeX representation
    ====================

    """
    # If index_config == "udd" then it prints the christoffell symbols of the second kind; \Gamma ^{\lambda}_{\mu\nu}.
    if(index_config == "udd"):
        for lam in range(len(self.coordinate_set)):
            for mu in range(len(self.coordinate_set)):
                for nu in range(len(self.coordinate_set)):
                    pprint(Eq(Symbol('Gamma^%s_%s%s' % (0, 0, 0))))
    # If index_config == "ddd" then it prints the christoffell symbols of the first kind; \Gamma_{\lambda\mu\nu}
    elif(index_config == "ddd"):
        for lam in range(len(self.coordinate_set)):
            for mu in range(len(self.coordinate_set)):
                for nu in range(len(self.coordinate_set)):
                    pprint(Eq(Symbol('Gamma_%s%s%s' % (0, 0, 0))))
    else:
        print("Invalid index_config input")

        
def list_riemann_components(connection):
    """
    Description
    ===========
    Prints the Riemann coefficients in a clear readable form.
    Example
    =======
    
    LaTeX representation
    ====================

    """
    if(index_config == "uddd"):
        for i in range(len(self.coordinate_set)):
            for j in range(len(self.coordinate_set)):
                for k in range(len(self.coordinate_set)):
                    for l in range(len(self.coordinate_set)):
                        pprint(Eq(Symbol('R^%s_%s%s%s' % (i, j, k, l))))
    elif(index_config == "dddd"):
        for i in range(len(self.coordinate_set)):
            for j in range(len(self.coordinate_set)):
                for k in range(len(self.coordinate_set)):
                    for l in range(len(self.coordinate_set)):
                        pprint(Eq(Symbol('R^%s_%s%s%s' % (i, j, k, l))))
    else:
        print("Invalid index_config input")
        
def list_ricci_components(connection):
    """
    Description
    ===========
    Prints the Ricci coefficients in a clear readable form.
    Example
    =======
    
    LaTeX representation
    ====================

    """
    for mu in range(len(self.coordinate_set)):
        for nu in range(len(self.coordinate_set)):
            pprint(Eq(Symbol('R^%s%s' % (mu, nu))))

def list_ricci_scalar(connection):
    """
    Description
    ===========
    Prints the Ricci scalar in a clear readable form.
    Example
    =======
    
    LaTeX representation
    ====================

    """
    pprint(Eq(Symbol('R'),0))
        
def list_proper_time_geodesic_equations(connection):
    """
    Description
    ===========
    Prints the proper time geodesic equations in a clear readable form.
    Example
    =======
    
    LaTeX representation
    ====================

    """
    for n in range(len(self.coordinate_set)):
        pprint(Eq(Symbol('R^%s%s' % (mu, nu))))
        
def list_coordinate_time_geodesic_equations(connection):
    """
    Description
    ===========
    Prints the coordinate time geodesic equations in a clear readable form.
    Example
    =======
    
    LaTeX representation
    ====================

    """
    max_columns = 3
    for n in range(len()):
        pprint(connection)