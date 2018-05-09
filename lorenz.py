
# coding: utf-8

# In[1]:


import numpy as np
import pylab as plt
from RungeKutta import vectorRungeKutta as rk


# In[2]:


def lorenz (r, t, state):
    """
    Description:calculates the values of the differential equations 
                that describe the Lorenz equations
    
    Parameters: r - (x, y, z), all floats
                t - float, time of calculation
                state - (sigma, rho, beta), constants for state of calculation
    
    Returned:1 x 3 numpy array of floats [fx, fy, fz]
    
    Usage:
    >>> r = (0.0, 1.0, 1.0)
    >>> state = (10.0, 28.0, 8.0 / 3.0)
    >>> lorenz (r, 0, state)
    array([ 10.        ,  -1.        ,  -2.66666667])
    """
    x, y, z = r
    sigma, rho, beta = state
    
    fx = sigma * (y - x)
    fy = x * (rho - z) - y
    fz = x * y - beta * z
    
    return np.array ([fx, fy, fz], float)


def lorenzSolution (r0, interval, steps, state, breaks = 1):
    """
    Description:returns the solution to the differential equations 
                that describe the Lorenz equations using Runge-Kutta's
                fourth order method
    
    Parameters:r0 - (x0, y0, z0) the initial values for x, y, and z
                    all floats
               interval - touple (t1, t2), both are floats
               steps - float, number of steps for Runge-Kutta method
               breaks - number of times to break up interval Runge-Kutta
                       calculation. MUST be >= 1, int
    
    Returned:m x 4 numpy array, [time, x, y, z]
    
    Usage:
    >>> sigma = 10.0
    >>> rho = 28.0
    >>> beta = 8.0 / 3.0
    >>> state = (sigma, rho, beta)
    >>> r0 = (0, 1, 0)
    >>> interval = (0, 1)
    >>> steps = 10
    >>> solution = lorenzSolution (r0, interval, steps, state)
    >>> solution
    array([[  0.        ,   0.        ,   1.        ,   0.        ],
           [  0.1       ,   0.79861927,   2.21410102,   0.05958108],
           [  0.2       ,   2.95275817,   6.62577401,   0.76031252],
           [  0.3       ,   9.31067541,  19.11133766,   7.50573648],
           [  0.4       ,  19.16625002,  22.11863919,  38.98453169],
           [  0.5       ,  10.07950841,  -7.48347292,  39.04833824],
           [  0.6       ,  -2.316505  ,  -9.14448955,  27.83851748],
           [  0.7       ,  -6.44260654,  -9.41513193,  25.25733091],
           [  0.8       ,  -8.62327961, -10.39493442,  26.11467541],
           [  0.9       ,  -9.67790294, -10.00294941,  28.45195757],
           [  1.        ,  -9.18413095,  -8.04678495,  29.33471295]])
    """
    numIndepVars = 3
    return rk (lorenz, numIndepVars, r0, interval, steps, state, order = 4, breaks = breaks)

def lorenzPlot (r0, state, interval, steps, bPlots = None, plotDim = None, startPlot = 1,
                titles = None, bCrit = False, breaks = 1, plotInterval = None):
    """
    Description: plots x, y, and z versus time, and z versus x for solution
                 to the lorenz equations. MUST call plot() to display
                 
    Parameters: r0 - initial (x, y, z) values, floats
                state - lorenz parameters (sigma, rho, state), floats
                interval - tuple for Runge-Kutta evaluation, floats
                steps - number of steps for Runge-Kutta method, int
                bPlots - booleans about whether to display x v t, y v t, 
                        z v t, and x v z, in that order. By default all
                        are displayed. MUST specify all four, booleans
                plotDim - subplot number of (rows, columns). MUST have 
                        rows + columns >= number of true values in bPlots,
                        ints
                startPlots - subplot start number. MUST be >= 1, int
                titles - additional text to add to title of each subplot.
                        If specify, MUST specify for number of true values
                        in bPlots. Does support LaTeX, string
                bCrit - add lines to time-dependant functions that show
                        critical point values
                breaks - number of times to break up interval Runge-Kutta
                        calculation. MUST be >= 1, int
                plotInterval - tuple of interval to plot. MUST be subset
                        of interval, floats
                        
    Returned: m x 4 numpy array, [time, x, y, z]
    
    Usage:
    >>> #set plot size
    >>> plt.figure(figsize=(16, 16))
    >>> 
    >>> #set constants and starting condition
    >>> sigma = 10.0
    >>> rho = 28.0
    >>> beta = 8.0 / 3.0
    >>> state = (sigma, rho, beta)
    >>> r0 = (0.0, 1.0, 0.0)
    >>> 
    >>> #set solution interval and accuracy
    >>> interval = (0.0, 50.0)
    >>> steps = 1000000
    >>> 
    >>> #plot Lorenz solution
    >>> solution = lorenzPlot (r0, state, interval, steps)
    >>> solution
    array([[  0.        ,   0.        ,   1.        ,   0.        ],
           [  0.1       ,   0.79861927,   2.21410102,   0.05958108],
           [  0.2       ,   2.95275817,   6.62577401,   0.76031252],
           [  0.3       ,   9.31067541,  19.11133766,   7.50573648],
           [  0.4       ,  19.16625002,  22.11863919,  38.98453169],
           [  0.5       ,  10.07950841,  -7.48347292,  39.04833824],
           [  0.6       ,  -2.316505  ,  -9.14448955,  27.83851748],
           [  0.7       ,  -6.44260654,  -9.41513193,  25.25733091],
           [  0.8       ,  -8.62327961, -10.39493442,  26.11467541],
           [  0.9       ,  -9.67790294, -10.00294941,  28.45195757],
           [  1.        ,  -9.18413095,  -8.04678495,  29.33471295]])
    >>> plt.show ()
    """

    #establish initial plot values
    plotLabelXPos = 0.075
    plotLabelYPos = 0.95
    plotLabelFontSize = 20 
    
    #initialize subplot number
    count = startPlot
    
    #set which plots will be plotted
    if None != bPlots:
        bX, bY, bZ, bXZ = bPlots
    else:
        bX = bY = bZ = bXZ = True

    #establish number of subplots
    numPlots = 0
    if bX:
        numPlots += 1;
    if bY:
        numPlots += 1;
    if bZ:
        numPlots += 1;
    if bXZ:
        numPlots += 1;
        
    #set number of subplot rows and columns
    if None != plotDim:
        rows, cols = plotDim
    #allows only two columns per row by default w/ 1 < numPlots
    elif 1 < numPlots:
        rows = int (numPlots / 2) 
        cols = int (numPlots - rows)
    else:
        rows = cols = 1   
        
    #establishes index values of interval to plot
    #if specified, calculate indices of solution to plot
    if None != plotInterval:
        a, b = interval
        ap, bp = plotInterval
        stepPerIndex = steps * breaks / (b - a)
        ai = int (ap * stepPerIndex)
        bi = int (bp * stepPerIndex)
    #by default plot all values of the solution
    else:
        ai, bi = (0, -1)
        
    #solve Lorenz equations
    solution = lorenzSolution (r0, interval, steps, state, breaks = breaks)
    
    #establish critical points
    if bCrit:
        sigma, rho, beta = state
        tVals = [solution[ai,0], solution[bi,0]]
        xCrit, yCrit, zCrit = lorenzCriticalPoints (rho, beta)
        
        xVals = np.array ([xCrit, xCrit], float)
        yVals = np.array ([yCrit, yCrit], float)
        zVals = np.array ([zCrit, zCrit], float)

    # x vs time
    if bX:
        ax = plt.subplot(rows, cols, count)
        ax.set_xlabel("t (s)")
        ax.set_ylabel("x")
        if None != titles:
            ax.set_title ("Lorenz Equations X versus Time {}".format (titles[count - startPlot]))
        else:
            ax.set_title ("Lorenz Equations X versus Time")
            
        ax.text (plotLabelXPos, plotLabelYPos, "({})".format (count), fontsize=plotLabelFontSize, 
                 transform=ax.transAxes)
        plt.plot (solution[ai:bi,0], solution[ai:bi,1], "-k")
        
        #graph critical points
        if bCrit:
            plt.plot (tVals, xVals, "--b")
            plt.plot (tVals, -1 * xVals, "--y")
        
        count += 1
    
    # y vs time
    if bY:
        ax = plt.subplot(rows, cols, count)
        ax.set_xlabel ("t (s)")
        ax.set_ylabel ("y")
        if None != titles:
            ax.set_title ("Lorenz Equations Y versus Time {}".format (titles[count - startPlot]))
        else:
            ax.set_title ("Lorenz Equations Y versus Time")
            
        ax.text (plotLabelXPos, plotLabelYPos, "({})".format (count), fontsize=plotLabelFontSize, 
                 transform=ax.transAxes)
        plt.plot (solution[ai:bi,0], solution[ai:bi,2], "-k")
        
        #graph critical points
        if bCrit:
            plt.plot (tVals, yVals, "--b")
            plt.plot (tVals, -1 * yVals, "--y")
        
        count += 1
    
    # z vs time
    if bZ:
        ax = plt.subplot (rows, cols, count)
        ax.set_xlabel ("t (s)")
        ax.set_ylabel ("z")
        if None != titles:
            ax.set_title ("Lorenz Equations Z versus Time {}".format (titles[count - startPlot]))
        else:
            ax.set_title ("Lorenz Equations Z versus Time")

        ax.text (plotLabelXPos, plotLabelYPos, "({})".format (count), fontsize=plotLabelFontSize, 
                 transform=ax.transAxes)
        plt.plot (solution[ai:bi,0], solution[ai:bi,3], "-k")
        
        #graph critical points
        if bCrit:
            plt.plot (tVals, zVals, "--b")
        
        count += 1
    
    # x vs z
    if bXZ:
        ax = plt.subplot(rows, cols, count)
        ax.set_xlabel ("x")
        ax.set_ylabel ("z")
        if None != titles:
            ax.set_title ("Lorenz Equations Z versus X {}".format (titles[count - startPlot]))
        else:
            ax.set_title ("Lorenz Equations Z versus X")
        ax.text (plotLabelXPos, plotLabelYPos, "({})".format (count), fontsize=plotLabelFontSize, 
                 transform=ax.transAxes)
        plt.plot (solution[ai:bi,1], solution[ai:bi,3], "-k")
     
        count += 1
    
    return solution

def lorenzCriticalPoints (rho, beta):
    """
    Description: returns positive critical points for the Lorenz equation
                with the given rho and beta values
    
    Parameters: rho - float
                beta - float
                
    Returned: positive citical values for [x, y, z] as float numpy array
    >>> rho = 28.0
    >>> beta = 8.0 / 3.0
    >>> crit = lorenzCriticalPoints (rho, beta)
    >>> crit
    array([  8.48528137,   8.48528137,  27.        ])
    """
    x = y = np.sqrt (beta * (rho - 1))
    z = rho - 1
    
    return np.array ([x, y, z], float)

