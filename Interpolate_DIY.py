import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from sympy import *

def fx(x):
    return np.cos(-x)**2/9.0

class Interpolation():
    def __init__(self):
        self.result = []
    def linear_function(self,x,y) :
        self.result = []
        X = Symbol('x')
        for i in range(1,len(x)) :
            a1 = y[i-1]/(x[i-1]-x[i])
            a2 = y[i]/(x[i]-x[i-1])
            self.result.append([(a1*(X-x[i]))+(a2*(X-x[i-1])),x[i-1],x[i]])

    #----------------------------------------------------------------------------

    def quadratic_function(self,x,y) :
        self.result = []
        a_initial = 0
        b_initial = 0
        X = Symbol('x')
        for i in range(1,len(x)) :
            if i == 1 :
                matrix_A = np.array([[x[i-1],1],[x[i],1]])
                matrix_B = np.array([y[i-1],y[i]])
                output = np.linalg.solve(matrix_A,matrix_B)
                b_initial = output[0]
                equation = (b_initial*X) + output[1]
                self.result.append([equation,x[i-1],x[i]])
            elif i == 2 :
                row1 = [2*x[i-1],1,0]
                row2 = [(x[i-1])**2,x[i-1],1]
                row3 = [(x[i])**2,x[i],1]
                matrix_A = np.array([row1,row2,row3])
                matrix_B = np.array([b_initial,y[i-1],y[i]])
                output = np.linalg.solve(matrix_A,matrix_B)
                a_initial = output[0]
                b_initial = output[1]
                equation = (a_initial*(X**2)) + (b_initial*X) + output[2]
                self.result.append([equation,x[i-1],x[i]])
            else:
                row1 = [2*x[i-1],1,0]
                row2 = [(x[i-1])**2,x[i-1],1]
                row3 = [(x[i])**2,x[i],1]
                matrix_A = np.array([row1,row2,row3])
                matrix_B = np.array([(2*a_initial*x[i-1]) + b_initial,y[i-1],y[i]])
                output = np.linalg.solve(matrix_A,matrix_B)
                a_initial = output[0]
                b_initial = output[1]
                equation = (a_initial*(X**2)) + (b_initial*X) + output[2]
                self.result.append([equation,x[i-1],x[i]])

    #----------------------------------------------------------------------------

    def set_function(self,x):
        X = Symbol('x')
        y = []
        for i in x :
            for j in self.result:
                if j[1] <= i <= j[2] :
                    f = j[0]
                    y.append(f.subs({X:i}))
                    break
        return y

    #----------------------------------------------------------------------------
        
def main():
    start = -2*np.pi
    stop = 2*np.pi
    step = 10
    x = np.linspace(start, stop, num=step, endpoint=True)
    y = fx(x)
    
    #-----------------------linear------------------------------
    linear_interpolated = Interpolation()
    interpo = linear_interpolated.linear_function(x,y)

    new_x = np.linspace(start, stop, num=step*10, endpoint=True)
    function_y =  linear_interpolated.set_function(new_x)

    #-----------------------quadratic------------------------------
    quadratic_interpolated = Interpolation()
    interpo2 = quadratic_interpolated.quadratic_function(x,y)

    function_y2 =  quadratic_interpolated.set_function(new_x)

    f3 = interp1d(x, y, kind='quadratic')

    #-----------------------Plot------------------------------
    plt.plot(x, y, 'o', new_x, f3(new_x), '-', new_x, function_y2, '--')
    plt.legend(['data', 'AI_quadratic', 'quadratic'], loc='best')
    plt.show()

main()
