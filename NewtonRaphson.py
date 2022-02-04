# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 15:02:14 2022
@author: sheld
"""
import numpy as np
from numpy import matlib
def NewtonRaphson(Model, beta, c_tot, c, i):
    """
    Parameters
    ----------
    Model : TYPE 
        DESCRIPTION.
    beta : TYPE np 2-d array with dtype int64
        DESCRIPTION.
    c_tot : TYPE
        DESCRIPTION.
    c : TYPE Numpy array
        DESCRIPTION.
    i : TYPE int
        DESCRIPTION.
    Returns
    -------
    None.
    """
    ncomp = np.size(c_tot)
    nspec= np.size(beta)
    c_tot[c_tot==0] = 1e-15
    #print(c_tot)
    it=0
    while it<=99:
        it = it+1
        
        
        tile = np.tile(np.transpose(c), (1, nspec))
        c_spec=np.multiply(beta,np.prod(np.power(tile, Model), axis=0))
        c_tot_calc = np.sum(np.multiply(Model, np.tile(c_spec, (ncomp, 1))), axis=1)
        c_tot_calc - np.transpose(c_tot_calc)
        d = np.subtract(c_tot, c_tot_calc)
        if np.all(np.absolute(d)< 1e-15):
            return c_spec
        J_s = np.zeros((ncomp, ncomp))
        for j in range(ncomp):
            for k in range(ncomp):
                J_s[j][k] = np.sum(np.multiply(np.multiply(Model[j], Model[k]), c_spec))
                J_s[k][j] = J_s[j][k]
                
        delta_c = np.matmul(np.linalg.solve(J_s.T, d.T).T,np.diag(c[0]))
        c = c+delta_c
        while np.any(c <= 0):
            delta_c = 0.5*delta_c
            c = c-delta_c
            if np.all(np.absolute(delta_c) < 1e-15):
                break
    if it>99:
        print("No convergence at C_spec({0}, :)\n".format(i))
    return c_spec