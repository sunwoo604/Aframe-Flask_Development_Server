# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 12:40:23 2022
@author: sheld
"""

import numpy as np
from NewtonRaphson import NewtonRaphson
import itertools

def predictModel(pH_meas_real, init_spec_name, c_0,c_added, v_0, v_inc, max_elements):
    """
    Predict the chemical model given a list of pH measurements and initial species
    Parameters
    ----------
    pH_meas_real : TYPE list of floats
        DESCRIPTION. List of pH measurements
    init_spec_name : TYPE list
        DESCRIPTION. List of species that the user started with
    c_0 : TYPE list of ints
        DESCRIPTION. List of initial concentrations for each species
    c_added : TYPE list of ints
        DESCRIPTION. List of concentrations added for each species
    v_0 : TYPE int
        DESCRIPTION. Initial volume
    v_inc : TYPE int 
        DESCRIPTION. Volume increments between solutions
    max_elements: TYPE int
        DESCRIPTION. Number of elements that the last species in the model may have.
            Determines stopping point for model generation algorithm.
    Returns
    -------
    TYPE List of lists (2-d list)
        DESCRIPTION. Species name of the top 5 models
    """
    pH_meas_real = np.array(pH_meas_real)
    c_0 = np.array(c_0)
    c_added=np.array(c_added)
    ncomp=np.size(c_0)
    nvol=np.size(pH_meas_real)
    if len(c_0)!=len(c_added):
        return 'Initial Concentration needs to have same dimension as Added Concentration'
    v_added = np.arange(0,v_inc*nvol,v_inc)
    v_tot   = v_0+v_added
    C_tot = np.zeros((nvol, ncomp), dtype=float)
    
    for j in range(ncomp):
        C_tot[:,j]= (v_0*c_0[0,j]+v_added*c_added[0,j])/v_tot
        
    
    beta_spec_list = {'AH': 10, 'AHH':17}
    for spec in init_spec_name:
        beta_spec_list[spec] = 0 
        
    def generateSpeciesNames(spec_name):
        """
        Generates a new list of species that we want to check and add it to the queue
        Parameters
        ----------
        spec_name : TYPE list of strings
            DESCRIPTION. Prior species within the chemical model
        nelements : TYPE int
            DESCRIPTION. Number of elements belonging to the species we will in the chemical model
        Returns
        -------
        list
            DESCRIPTION. New list of species to check for fit
        """
        comb_list = list(itertools.combinations_with_replacement(spec_name[0:ncomp], len(spec_name)))
        comb_list = [''.join(sorted(s)) for s in comb_list]
        
        #Tentatively creating dictionary to generate unique random betas
        #NEXT STEP: Calculating betas
        for comb in comb_list:
            if comb not in beta_spec_list:
                beta = np.random.randint(18, 30)
                beta_spec_list[comb] = beta
        return [spec_name + [s] for s in comb_list]
    
    def generateChemModel(speciesName):
        """
        Generates 2-d array model of elements given species names
        Parameters
        ----------
        speciesName : TYPE 1-d list
            DESCRIPTION. List of species names
        Returns
        -------
        model : TYPE 2-d array of ints
            DESCRIPTION. Chemical model of elements
        betas : TYPE 2-d array of floats
            DESCRIPTION. Betas values for each species (column in the model)
        """
        model = []
        for i in range(len(speciesName)):
            vec=[]
            for spec in init_spec_name:
                vec.append(speciesName[i].count(spec))
            model.append(vec)
        
        #generate betas
        #For now, betas are initialized randomly using a dictionary
        betas = [beta_spec_list[comb] for comb in speciesName]
            
        betas = 10**np.array([betas], dtype='float64')
        model = np.array(model).T
        
        return model, betas
    
    
    def testModel(chem_model, beta, C_tot):
        """
        Replicates the Data_pH.m matlab file to test if the model's pH_meas is close to pH_meas_real
        Parameters
        ----------
        chem_model : TYPE 2-d array of ints
            DESCRIPTION. Chemical model of elements
        betas : TYPE 2-d array of floats
            DESCRIPTION. Betas values for each species (column in the model)
        C_tot : TYPE 2-d array
            DESCRIPTION. Total concentrations for each solution
        Returns
        -------
        diff : TYPE np.double
            DESCRIPTION. Difference between measured pH from algorithm and real measured pH, taken as inner product
        """
        C=np.zeros((nvol, np.size(beta)))
        c_comp_guess = np.array([[1,1]])*1e-10
        for i in range(nvol):
            C[i, :]=NewtonRaphson(chem_model, beta, C_tot[i, :], c_comp_guess, i)
            c_comp_guess=np.array([C[i,:ncomp]])
        pH_calc=-1*np.log10(C[:, 2])
        sig_R = 0.002
        pH_meas=pH_calc+sig_R*np.random.random(pH_calc.shape)
        diff = np.linalg.norm(pH_meas_real-pH_meas, ord=2)
        return diff
    
    np.random.seed(4)
    queue = generateSpeciesNames(init_spec_name)
    count = 0
    
    #List for top 5 predicted species names and their diffs
    topSpeciesNames = []
    
    while len(queue)!=0: 
        
        np.random.seed(4)
        speciesName=queue.pop(0)
        if len(speciesName)-ncomp+1>max_elements:
            continue
        chem_model, beta=generateChemModel(speciesName)
        print(speciesName)
        print(chem_model)
        diff=testModel(chem_model, beta, C_tot)
        
        #c
        if len(topSpeciesNames)<5 :
            topSpeciesNames.append((speciesName, diff))
            topSpeciesNames.sort(key = lambda x: x[1])
        elif topSpeciesNames[4][1]>diff:
            topSpeciesNames.pop()
            topSpeciesNames.append((speciesName, diff))
            topSpeciesNames.sort(key = lambda x: x[1])
        
        queue.extend(generateSpeciesNames(speciesName))
        count+=1
    #Use regex to generate valid species name
    #Ask Fereshteh how to format species name strings?
    return [x[0] for x in topSpeciesNames]