
# coding: utf-8

# In[1]:


import numpy as np


# In[62]:


def vectorRungeKutta (func, dimension, r0, interval, numSteps, *args, order=1, bVerbose=False):
    """
    Description: returns the Runge-Kutta solution to the given vector
    
    Parameters: func - function with parameters (vector, float, *args) for
                        an ODE of the form r' = f (r, t, *args)
                dimension - dimension of vector r
                r0 - initial condition for vector r 
                interval - domain of solution
                numSteps - number of steps
                *args - additional arguments for func
                order - 1 for first order Runge-Kutta (Euler method)
                        2 for second order Runge-Kutta
                        4 for fourth order Runge-Kutta
                        
    Returned: (t, r_1, ..., r_dimension), as (numSteps + 1)x(dimension + 1) 
                numpy array.
    """
    
    #set interval and step size
    a, b = interval
    h = (b - a) / numSteps
    
    #initialize results as zero
    solution = np.zeros ((numSteps + 1, dimension + 1))
    
    #solve first case
    r = r0
    t = a
    solution[0,0] = t
    solution[0,1:] = r
    
    #solve each case
    for i in range (1, numSteps + 1):

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
            print ("step: {}, t: {}, r: {}".format (i, t, r))
        
        #add new solution values
        solution[i,0] = t
        solution[i,1:] = r
    
    return solution

