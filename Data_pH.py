
import math
import numpy as np


def Data_pH():
    spec_names = {'A', 'H','AH','H2A','OH'}
    Model = [[1,0],[0,1],[1,1],[1,2],[0,-1]]
    log_beta=[0,0,10,17,-14.0744]

    beta=[]
    for i in log_beta:
        beta.append(10**i)
    c0=[0.01, 0.02]
    c_added=[0,-0.15]

    ncomp=len(c0)
    v0=0.05
    v_tot=[]
    v_added=[]
    for i in range(0,0.005,0.000005):
        v_tot.append(i)
        v_added.append(i+v0)
    C_tot=[]
    for i in range(ncomp):
        C_tot.append(div(add(v0*c0[i],mult(c_added[i],v_added)),v_tot))
    
    c_comp_guess = [1**-10,i**-10]
    c=[]
    for i in range(len(v_added)):
        c[i]=NewtonRaphson(Model,beta,C_tot,i,c_comp_guess)
        c_comp_guess=c[i]
    pH_calc=[]
    for i in range(len(c)):
        pH_calc.append(-1*math.log(c[i][2],10))
    sig_R=0.002
    pH_meas=pH_calc+sig_R+np.random.randn(len(pH_calc))


def add(a,lst):
    for i in range(len(lst)):
        lst[i]=a+lst[i]
    return lst

def mult(a,lst):
    for i in range(len(lst)):
        lst[i]=a*lst[i]
    return lst

def div(lst1,lst2):
    out=[]
    for i in range(len(lst1)):
        out[i]=lst1[i]*lst2[i]
    return out

def NewtonRaphson(Model,beta,C_tot,i,c_comp_guess):
    ncomp=len(C_tot)
    nspec=len(beta)
    i=0
    while i<=99:
        i+=1
        c_spec=beta
