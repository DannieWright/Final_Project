# Final_Project

This code numerically models the Lorenz equations and a damped driven nonlinear pendulum using the Runge-Kutta methods. The Runge-Kutta method solves an arbitrary number of differential equations and is found in the RungeKutta.py file.

For the main project to work the RungeKutta.py file must be present. In the absense of the file, the RungeKutta.ipynb file can be converted to a .py file in Jupyter Notebook by going to File->Download as->Python (.py). Then place the .py file in the directory for use and import it with "import RungeKutta". Numpy is the only requirement for this package.

## RungeKutta.py:

### vectorRungeKutta

#### def vectorRungeKutta (func, dimension, r0, interval, numSteps, *args, order=1, bVerbose=False):

#### Description: returns the Runge-Kutta solution to the given vector
    
#### Parameters: 
   func - function with parameters (vector, float, *args) for
                   an ODE of the form r' = f (r, t, *args)
   dimension - dimension of vector r
   r0 - initial condition for vector r 
   interval - domain of solution
   numSteps - number of steps
   *args - additional arguments for func
   order - 1 for first order Runge-Kutta (Euler method)
           2 for second order Runge-Kutta
           4 for fourth order Runge-Kutta
   bVerbose - print debugging information
                        
Returned: (t, r_1, ..., r_dimension), as (numSteps + 1)x(dimension + 1) 
          numpy array.

#### Usage:

##### import needed packages:
from RungeKutta import vectorRungeKutta as rk
import numpy as np

##### ordinary differential function for calculation
def ODE (r, t):
   x, y = r
   return np.array ([x * y, x * t], float)

##### set initial state
x0 = 1
y0 = 4
r0 = (x0, y0)

##### number of dimensions/independant variables
dim = 2

##### interval of solution
interval = (0, 1)

##### number of steps for Runge-Kutta method, determines accuracy
steps = 100000

##### order for Runge-Kutta method, increase has better accuracy
order = 4

##### use the function
rk.vectorRungeKutta (ODE, dim, r0, interval, steps, order = order)

##### Output:
array([[  0.00000000e+00,   1.00000000e+00,   4.00000000e+00],
       [  1.00000000e-05,   1.00004000e+00,   4.00000000e+00],
       [  2.00000000e-05,   1.00008000e+00,   4.00000000e+00],
       ..., 
       [  9.99980000e-01,   3.68146529e+03,   8.48844557e+01],
       [  9.99990000e-01,   3.68459229e+03,   8.49212855e+01],
       [  1.00000000e+00,   3.68772330e+03,   8.49581468e+01]])

[Presentation](https://drive.google.com/open?id=1IMgNnLmswsDnQJt_CLs0p3njH_Yr4FvHy-orAj_HOgA)


Written by Dannie Wright, wri94711@pacificu.edu

