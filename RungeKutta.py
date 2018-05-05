
# coding: utf-8

# In[1]:


import numpy as np


# In[62]:


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

    #set overall interval values
    a0, b0 = interval

    #initialize results as zero
    solution = np.zeros ((numSteps * breaks + 1, dimension + 1))
    
    for j in range (breaks):
    
        #if calculating first break, use given starting state
        if 0 == j:
            r = r0
        #else use previous break's ending value for starting state
        else:
            r = (solution[endBreak,1], solution[endBreak,2], solution[endBreak,3])

        #set interval and step size for current break
        a = b0 / breaks * j + a0
        b = b0 / breaks * (j + 1)
        h = (b - a) / numSteps

        #set solution array index value for end/beginning of current break
        endBreak = numSteps * (j + 1) - 1
        begBreak = numSteps * j
        
        #solve first case for break
        t = a
        solution[begBreak,0] = t
        solution[begBreak,1:] = r

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
            solution[i + begBreak,0] = t
            solution[i + begBreak,1:] = r
    
    return solution

