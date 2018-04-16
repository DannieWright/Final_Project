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
 
