#!/usr/bin/env python
# coding: utf-8
import math
import numpy as np

def DataPh():
    spec_names = ['A', 'H', 'AH', 'H2A', 'OH']
    Model = [[1, 0,1,1,0], [0,1,1,2,-1]]
    log_beta = np.array([0, 0, 10, 17, -14.0744])

    beta = []
    for i in log_beta:
        beta.append(10 ** i)
    c0 = [0.01, 0.02]
    c_added = [0, -0.15]

    ncomp = len(c0)
    v0 = 0.05
    v_added = []
    v_tot = []
    for i in np.arange(0, 0.005+0.000005, 0.000005):
        v_added.append(i)
        v_tot.append(v0+i)
    nvol = len(v_added)
    C_tot = np.zeros((nvol, ncomp), dtype=float)
    for i in range(ncomp):
        C_tot[:, i]=(np.divide(np.add(v0 * c0[i], np.multiply(c_added[i], v_added)), v_tot))
    c_comp_guess = c_comp_guess = np.array([[1,1]])*1e-10
    c =np.zeros((nvol, np.size(beta)))
    for i in range(nvol):
        c[i, :] = NewtonRaphson(Model, beta, C_tot[i, :],c_comp_guess, i)
        c_comp_guess=np.array([c[i,:ncomp]])
    out=[]
    for i in range(len(c[0])):
        temp=[]
        for j in c:
            temp.append(j[i])
        out.append(temp)
    pH_calc = []
    for i in c:
        pH_calc.append(-math.log10(i[1]))
    sig_R=0.002
    np.random.seed(0)
    random_numbers = np.random.randn(len(pH_calc))
    pH_meas = []
    for i in range(len(random_numbers)):
        pH_meas.append(pH_calc[i]+(sig_R*random_numbers[i]))
    max_out_ls = []
    min_out_ls = []
    for i in out:
        max_out_ls.append(max(i))
        min_out_ls.append(min(i))
    max_out = max(max_out_ls)
    min_out = min(min_out_ls)
    stepy = math.ceil((max_out - min_out)/0.002)+1
    yaxis = []
    for i in range(stepy):
        yaxis.append(0.002*i)
    max_pH = max(pH_meas)
    min_pH = min(pH_meas)
    stepx = math.ceil((max_pH - min_pH)/5)+1
    xaxis = []
    for i in range(stepx):
        xaxis.append(5*i)
    return (out,spec_names,pH_meas, min_pH, max_pH, min_out, max_out)

    
# def add(a, lst):
#     for i in range(len(lst)):
#         lst[i] = a + lst[i]
#     return lst


# def mult(a, lst):
#     for i in range(len(lst)):
#         lst[i] = a * lst[i]
#     return lst


# def div(lst1, lst2):
#     out = []
#     for i in range(len(lst1)):
#         out.append(lst1[i] / lst2[i])
#     return out

def NewtonRaphson(Model, beta, c_tot,c, i):
    """
    ncomp=len(c_tot)
    nspec=len(beta)
    idx=0
    c_spec=[]
    while idx<=99:
        idx+=1
        c_spec=beta*prod
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




