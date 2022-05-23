#Numpy
import datetime
import numpy as np
import matplotlib.pyplot as plt
#import scipy.interpolate as interpolate
from scipy.interpolate import interp1d
#from scipy.interpolate import lagrange
from sympy import *

def fx(x):
    return np.cos(-x)**2/9.0

class Interpolation():
    def __init__(self):
        self.result = []
        
    def linear_function(self,x,y) :
        X = Symbol('x')
        for i in range(1,len(x)) :
            a1 = y[i-1]/(x[i-1]-x[i])
            a2 = y[i]/(x[i]-x[i-1])
            self.result.append([(a1*(X-x[i]))+(a2*(X-x[i-1])),x[i-1],x[i]])
            
    def set_linear(self,x):
        X = Symbol('x')
        y = []
        for i in x :
            for j in self.result:
                if j[1] <= i <= j[2] :
                    f = j[0]
                    y.append(f.subs({X:i}))
                    break
        return y
        
def main():
    start = -2*np.pi
    stop = 2*np.pi
    step = 1000
    x = np.linspace(start, stop, num=step, endpoint=True)
    y = fx(x)
    
    linear_interpolated = Interpolation()
    interpo = linear_interpolated.linear_function(x,y)

    new_x = np.linspace(start, stop, num=step*10, endpoint=True)
    function_y =  linear_interpolated.set_linear(new_x)


main()
