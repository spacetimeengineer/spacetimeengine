#!/usr/bin/env python
from sympy import *

def get_schwarzschild_metric():
    """
    Status
    ======
    Fix docstrings, write and test.

    Description
    ===========
    Returns the Schwarzschild metric tensor.
    Example
    =======
    >>> from sympy import *
    >>> print(get_schwarzschild_metric())
    >>> 

    LaTeX representation (Needs tweaking to reflect function precicely)
    ====================
    c^{2}{d\tau }^{2}=\left(1-{\frac {r_{\mathrm {s} }}{r}}\right)c^{2}\,dt^{2}+\left(1-{\frac {r_{\mathrm {s} }}{r}}\right)^{-1}\,dr^{2}+r^{2}\left(d\theta ^{2}+\sin ^{2}\theta \,d\varphi ^{2}\right),} {\displaystyle -c^{2}\,{d\tau }^{2}=-\left(1-{\frac {r_{\mathrm {s} }}{r}}\right)c^{2}\,dt^{2}+\left(1-{\frac {r_{\mathrm {s} }}{r}}\right)^{-1}\,dr^{2}+r^{2}\left(d\theta ^{2}+\sin ^{2}\theta \,d\varphi ^{2}\right),}
    """

    return schwarzschild_metric

def get_friedmann_lemaitre_robertson_walker_metric():
    """
    Status
    ====== 
    
    Description
    ===========
    Returns Friedmann Lemaitre Robertson Walker metric.

    Examples
    ========
    >>> from sympy import *
    >>> print(get_friedmann_lemaitre_robertson_walker_metric())
    >>> 

    LaTeX representation
    ====================

    """
    return schwarzschild_metric

def get_taub_nut_metric():
    """
    Status
    ======
    
    Description
    ===========
    Returns Taub-Nut metric.

    Examples
    ========
    >>> from sympy import *
    >>> print(get_taub_nut_metric())
    >>> 

    LaTeX representation
    ====================

    """
    return taub_nut_metric

def get_milne_metric():
    """
    Status
    ======
    
    Description
    ===========
    Returns Milne metric.

    Examples
    ========
    >>> from sympy import *
    >>> print(get_milne_metric())
    >>> 

    LaTeX representation
    ====================

    """
    return milne_metric

def get_kerr_metric():
    """
    Status
    ======
    
    Description
    ===========
    Returns Kerr metric.

    Examples
    ========
    >>> from sympy import *
    >>> print(get_kerr_metric())
    >>> 

    LaTeX representation
    ====================

    """
    return kerr_metric

def get_kerns_wild_metric():
    """
    Status
    ======

    Description
    ===========
    Returns Kerns-Wild metric.

    Examples
    ========
    >>> from sympy import *
    >>> print(get_kerns_wild_metric())
    >>> 

    LaTeX representation
    ====================

    """
    return kerns_wild_metric

def get_double_kerr_metric():
    """
    Status
    ======
    
    Description
    ===========
    Returns Double-Kerr metric.

    Examples
    ========
    >>> from sympy import *
    >>> print(get_double_kerr_metric())
    >>> 

    LaTeX representation
    ====================

    """
    return double_kerr_metric

def get_khan_penrose_metric():
    """
    Status
    ======

    Description
    ===========
    Returns Khan metric.

    Examples
    ========
    >>> from sympy import *
    >>> print(get_khan_penrose_metric())
    >>> 

    LaTeX representation
    ====================

    """
    return khan_metric

def get_gowdy_metric():
    """
    Status
    ======

    Description
    ===========
    Returns Gowdy metric.

    Examples
    ========
    >>> from sympy import *
    >>> print(get_gowdy_metric())
    >>> 

    LaTeX representation
    ====================

    """
    return gowdy_metric

def get_ehlers_metric():
    """
    Status
    ======

    Description
    ===========
    Returns Ehlers metric.

    Examples
    ========
    >>> from sympy import *
    >>> print(get_ehlers_metric())
    >>> 

    LaTeX representation
    ====================

    """
    return ehlers_metric

def get_weyl_metric():
    """
    Status
    ======

    Description
    ===========
    Returns Weyl metric.

    Examples
    ========
    >>> from sympy import *
    >>> print(get_weyl_metric())
    >>> 

    LaTeX representation
    ====================

    """
    return weyl_metric

def get_beck_metric():
    """
    Status
    ======
    
    Description
    ===========
    Returns Beck metric.

    Examples
    ========
    >>> from sympy import *
    >>> print(get_beck_metric())
    >>> 

    LaTeX representation
    ====================

    """
    return beck_metric

def get_ernst_metric():
    """
    Status
    ======

    Description
    ===========
    Returns Ernst metric.

    Examples
    ========
    >>> from sympy import *
    >>> print(get_ernst_metric())
    >>> 

    LaTeX representation
    ====================

    """
    return ernst_metric

def get_kasner_metric():
    """
    Status
    ======
    
    Description
    ===========
    Returns Kanser metric.

    Examples
    ========
    >>> from sympy import *
    >>> print(get_kasner_metric())
    >>> 

    LaTeX representation
    ====================

    """
    return kasner_metric

def get_kruskal_szekeres_metric():
    """
    Status
    ======

    Description
    ===========
    Returns Kruskal Szekeres metric.

    Examples
    ========
    >>> from sympy import *
    >>> print(get_kruskal_szekeres_metric())
    >>> 

    LaTeX representation
    ====================

    """
    return kruskal_szekeres_metric


#Electrovacum solutions.

def get_reissner_nordstrom_metric():
    """
    Status
    ======

    Description
    ===========
    Returns Reissner Nordstrom metric.

    Examples
    ========
    >>> from sympy import *
    >>> print(get_reissner_nordstrom_metric())
    >>> 

    LaTeX representation
    ====================

    """
    return kruskal_szekeres_metric

def get_kerr_newman_metric():
    """
    Status
    ======

    Description
    ===========
    Returns Kerr-Newman metric.

    Examples
    ========
    >>> from sympy import *
    >>> print(get_kerr_newman_metric())
    >>> 

    LaTeX representation
    ====================

    """
    return kerr_newman_metric

def get_melvin_metric():
    """
    Status
    ======

    Description
    ===========
    Returns Melvin metric.

    Examples
    ========
    >>> from sympy import *
    >>> print(get_melvin_metric())
    >>> 

    LaTeX representation
    ====================

    """
    return melvin_metric

def get_garfinkle_melvin_metric():
    """
    Status
    ======

    Description
    ===========
    Returns Garfinkle Melvin metric.

    Examples
    ========
    >>> from sympy import *
    >>> print(get_garfinkle_melvin_metric())
    >>> 

    LaTeX representation
    ====================

    """
    return garfinkle_melvin_metric

def get_bertotti_robinson_metric():
    """
    Status
    ======

    Description
    ===========
    Returns Bertotti Robinson metric.

    Examples
    ========
    >>> from sympy import *
    >>> print(get_bertotti_robinson_metric())
    >>> 

    LaTeX representation
    ====================

    """
    return bertotti_robinson_metric

def get_vaidya_metric():
    """
    Status
    ======

    Description
    ===========
    Returns Vaidya metric.

    Examples
    ========
    >>> from sympy import *
    >>> print(get_vaidya_metric())
    >>> 

    LaTeX representation
    ====================

    """
    return vaidya_metric

def get_godel_metric():
    """
    Status
    ======

    Description
    ===========
    Returns Godel metric.

    Examples
    ========
    >>> from sympy import *
    >>> print(get_vaidya_metric())
    >>> 

    LaTeX representation
    ====================
    ds^{2}={\frac {1}{2\omega ^{2}}}\left[-(dt+e^{x}dy)^{2}+dx^{2}+{\tfrac {1}{2}}e^{2x}dy^{2}+dz^{2}\right],\qquad -\infty <t,x,y,z<\infty ,} {\displaystyle ds^{2}={\frac {1}{2\omega ^{2}}}\left[-(dt+e^{x}dy)^{2}+dx^{2}+{\tfrac {1}{2}}e^{2x}dy^{2}+dz^{2}\right],\qquad -\infty <t,x,y,z<\infty
    """
    return godel_metric

