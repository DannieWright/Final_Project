
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def vectorRungeKutta (func, dimension, r0, interval, numSteps, *args, order=1, 
                      breaks = 1, bVerbose=False):
    """
    Description: returns the Runge-Kutta solution to the given vector
    
    Parameters: func - function with parameters (vector, float, *args) for
                        an ODE of the form r' = f (r, t, *args)
                dimension - dimension of vector r
                r0 - initial condition for vector r 
                interval - tuple domain of solution, floats
                numSteps - number of steps. MUST be >= 1, int
                *args - additional arguments for func
                order - 1 for first order Runge-Kutta (Euler method)
                        2 for second order Runge-Kutta
                        4 for fourth order Runge-Kutta
                breaks - number of times to break up the interval for calculation.
                        MUST be >= 1, int
                bVerbose - print debugging information
                        
    Returned: (t, r_1, ..., r_dimension), as (numSteps + 1)x(dimension + 1) 
                numpy array.
    """
    #set interval and step size
    a, b = interval
    h = (b - a) / (numSteps * breaks)
    
    #one first break store initial value, subsequent breaks already have their 
    #initial values so do not store them
    bFirst = True
    index = 1
    
    #set final solution to None for first calculation
    solutionF = np.array([])
    
    for j in range (breaks):
        #initialize results as zero
        solution = np.zeros ((numSteps + 1, dimension + 1))
        
        #if calculating first break, use given starting state and interval start
        if 0 == j:
            t = a
            r = r0
        #else use previous break's ending value for starting state and new interval start
            
        #if it is the first break, solve first case for break
        if bFirst:
            solution[0,0] = t
            solution[0,1:] = r

        #solve each case
        for i in range (index, numSteps + 1):

            #first order Runge-Kutta (Euler method)
            if 1 == order:
                r += h * func (r, t, *args)

            #second order Runge-Kutta
            elif 2 == order:
                k1 = h * func (r, t, *args)
                k2 = h * func (r + 0.5 * k1, t + 0.5 * h, *args)
                r += k2

            #fourth order Runge-Kutta
            elif 4 == order:
                k1 = h * func (r, t, *args)
                k2 = h * func (r + 0.5 * k1, t + 0.5 * h, *args)
                k3 = h * func (r + 0.5 * k2, t + 0.5 * h, *args)
                k4 = h * func (r + k3, t + h, *args)
                r += (k1 + 2 * k2 + 2 * k3 + k4) / 6

            #increment time
            t += h

            if bVerbose:
                print ("step: {}, t: {}, r: {}, r.shape: {}".format (i, t, r, r.shape))

            #add new solution values
            solution[i,0] = t
            solution[i,1:] = r
            
        #add last break's solution to overall solution
        if 0 != solutionF.size:
            solutionF = np.concatenate ((solutionF, solution))
        else:
            solutionF = solution
            bFirst = False
            index = 0
            
    return solutionF

