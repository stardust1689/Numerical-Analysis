import numpy as np 
#Allows for built-in math functions (sin(), exp(), etc.)
def bisect_w(a,b,w):
# a and b: initial points to test.
# w: minimum width between updated a and b for bisection method satisfaction.
    print(a,'-',b,'//',abs(b-a))
    def f(x):
        return (5-x)*np.exp(x) - 5 
        # Function of interest
    if f(a)*f(b) < 0:
        while abs(b-a) > w:
            x_k = (a+b)/2
            if f(a)*f(x_k) < 0:
                b = x_k
                print(a,'-',b,'//',abs(b-a))
            elif f(b)*f(x_k) < 0:
                a = x_k
                print(a,'-',b,'//',abs(b-a))
        return x_k
        # Returns x_star approximation
    else:
        return 'No solution enclosed'