# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 18:44:28 2022
@author: sheld
"""

import NewtonRaphson as nr
import ModelPredictive as mp
import numpy as np


Model = np.array([[1,0,1,1], 
                  [0,1,1,2]]) #Species name: ['A', 'H' ,'AH' ,'AHH']
beta = 10**np.array([[0,0,10,17]], dtype='float64')
c_comp_guess=np.array([[1,1]])*1e-10
i=0
ncomp=np.size(c_comp_guess)
v_0=.050
v_inc = .000005
v_added = np.arange(0,0.005, v_inc)
nvol    = np.size(v_added); 
v_tot   = v_0+v_added
C_tot = np.zeros((nvol, ncomp))
c_0     = np.array([[0.01, 0.02]]); 
c_added    = np.array([[0, -0.15]])
for j in range(ncomp):
    C_tot[:, j]= (v_0*c_0[0,j]+v_added*c_added[0,j])/v_tot
C=np.zeros((nvol, np.size(beta)))
for i in range(nvol):
    C[i, :]=nr.NewtonRaphson(Model, beta, C_tot[i, :], c_comp_guess, i)
    c_comp_guess=np.array([C[i,:ncomp]])
pH_calc=-1*np.log10(C[:, 2]) #How should the 2 change for general case?
np.random.seed(4)
sig_R = 0.002
pH_meas=pH_calc+sig_R*np.random.random(pH_calc.shape)
pH_meas = pH_meas.tolist()

print(mp.predictModel(pH_meas, ['A', 'H'], c_0, c_added, 0.05, 0.000005, 4))