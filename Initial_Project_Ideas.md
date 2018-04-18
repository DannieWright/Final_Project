Computer science is really theoretical physics because it is building models. You still need to do 
experiments to test the created models, else you basically have a video game.


## 12 Steps
    1) Use version control
    2) Put your code in the cloud, in the open
    3) Add a README and a License
    4) Write docstrings
    5) Write tests
    6) Keep track of issues
    7) Automate the tests
    8) Automate the build (coming soon)
    9) Use continuous integration (coming soon)
    10) Monitor test coverage (coming soon)
    11) Write narrative documentation (coming soon)
    12) Catch errors as you type them (coming soon)
    
    
### 1)
Make a local repository.

### 2)
Connect the local repository to GitHub.

### 3)
README should have

    1) a brief description of what your code does;
    2) instructions for installing your code;
    3) what other code needs to be installed for it to work;
    4) one or two examples of how to invoke your code;
    5) optionally: who wrote the code, how to cite it, and who to contact for help. One good example of a 
    README file is here.
    
LICENSE.txt, pick a pre-existing one

### 4)
Write docstrings, be sure to have usage

    Examples:
    >>> square(5)
    25
    >>> square(2)
    4
    

### 5)
Type the following in the command line to test the examples in the function docstrings

    python -m doctest -v my_file.py
    
### 6)
Raise an issue on GitHub if there is an issue/potential feature/improvement you want in your code that you'll come back to later.

### 7)
Can use Nose to autorun test cases

if not installed do "pip install nose"

    1) First, go to your project directory and type nosetests --with-doctest. The nose executable is named 
    “nosetests” and the option --with-doctest tells it to also run any doctests it finds. You should get a
    message saying that some number of tests were run, with an “OK” at the end.
    2) To see how nosetests becomes really useful, either: (a) add a doctest in another file; or (b) add a 
    file called tests.py containing at least one function with “test” in the name. The test function should 
    check something and raise an exception if things are wrong.
    3) Now type nosetests --with-doctest again. You should see that your new tests were also run. To get more
    detailed output, try nosetests --with-doctest --vs.
    
    
    
What physics problem would you like to focus on?
  Possibly exercise 8.3
  
What is the numerical technique to solve it?
  Vector form of the Runge-Kutta method.
  
How will you make it "yours" if it is a canned problem from Newman. 
  I do not know. I will likely look more into deterministic chaos.
 








# 4/18/2018 Work

1) Identify general area  
?? What?? For a square Area = length * width.  
I am going to be working on Newman exercise 8.3, about the Lorenz Equations.   
I will likely also work on a nonlinear driven pendulum as a intro to deterministic chaos.

2) Write down relevant controlling equations  
$\frac{dx}{dt}=\sigma(y-x), \ \frac{dy}{dt}=rx-y-xz, \ \frac{dz}{dt}=xy-bz$

and

$\frac{d^2\theta}{dt^2}=-\frac{g}{l}\sin(\theta)-q\frac{d\theta}{dt}+F_d\sin(\Omega_Dt)$

3) Clarify specific scenario to be simulated
Simulating a greatly simplified convection problem. Going to show case of $\sigma=10$, 
$r=28$, $b=\frac{8}{3}$, $t_0=0$, and $t_f=50$, with initial conditions of (x, y, z) = (0, 1, 0). 
I will plot y versus time and z versus x. I would like to also set up animation to show the evolution
of z versus x over time.

Simulating a nonlinear driven pendulum. Going to show similar start consitions where the angle difference
between the two situations are modeled versus time to demonstrate deterministic properties with a low drive. 
Also show high drive force to show sensitivity to initial conditions.

4) Write down the numerical method you intend to use  
Fourth order Runge-Kutta method.

5) Write down boundary conditions for that scenario  
$r\approx24.74$ determines difference of single to double attractors.

6) Outline specific results to be obtained  
 describe the situation you are going to simulate  
 describe the output you expect to generate  
 Describe how you can verify that your results are correct or reasonable  
 
Lorenz  
Graphs of y versus time and z versus x. An animation to show the evolution of z versus x over time.
Should see different number of attractors based on $r$-value for z versus x varying $r$-values. Should see
butterfly effect for z versus x. Should see oscillatory function for y versus time.
Can verify solutions with Giordano or find other sources on it, it is apparently a fairly common problem.

Pendulum   
Graph $\Delta\theta$ versus time for high and low drive values. Possibly show animation of pendulum 
evolving over time. 
Should see exponential decrease and increases in the difference between the angles 
for a low and high driving force respectivly. Animation should show two oscilatory motions that begin to
vary greatly overtime for high force and stay very similiar for small force.
I can verify using Giordano.




7) Create a rough outline of major steps you have to take and a schedule for accomplishing them.
Have most of non-animation code done by 4/23/2018.
Have most of physics explanation and finish non-animation code by 4/27/2018.
Finish all code and explanation by 4/30/2018.
Work on and finish presentation parts, maybe adding to animations or looking at less simplified case for Lorenz
problem by final presentation.

Write down everything you can prior to class (i.e. 9:15 am). Ideally you will have A LOT of 
questions and ask them in class. There is nothing like scientific writing to clarify your 

What was the first question asking?
Not entirely sure about boundary conditions for these cases, figured I would model mostly variation in initial
conditions for the pendulum to see chaotic aspect, and would adjust $r$-value for the Lorenz, is this a good way to 
go about it?
questions! You will finish this outline for your Benchmark due Friday.
