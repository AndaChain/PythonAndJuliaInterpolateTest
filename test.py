#Numpy
import time
import datetime
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interpolate
from scipy.interpolate import interp1d
from scipy.interpolate import lagrange

from GUI_in import*


def fx(x):
    return np.cos(-x)**2/9.0

def interpolate(start,stop,step):

    x = np.linspace(start, stop, num=step, endpoint=True)
    y = fx(x)

    start_li = time.time_ns() # set start time 
    f1 = interp1d(x, y)
    end_li = time.time_ns()   # set end time
    time_li = end_li - start_li
    print("linear time", time_li)

    start_cu = time.time_ns() # set start time
    f2 = interp1d(x, y, kind='cubic')
    end_cu = time.time_ns()   # set end time
    time_cubic = end_cu - start_cu
    print("cubic time",time_cubic)

    start_qu = time.time_ns() # set start time 
    f3 = interp1d(x, y, kind='quadratic')
    end_qu = time.time_ns()   # set end time 
    time_qu = end_qu - start_qu
    print("quadratic time",time_qu)
        
    xnew = np.linspace(start, stop, num=step, endpoint=True)

    import matplotlib.pyplot as plt
    plt.plot(x, y, 'o', xnew, f1(xnew), '-', xnew, f2(xnew), '--', xnew, f3(xnew))
    plt.legend(['data', 'linear', 'cubic', 'quadratic'], loc='best')
    plt.savefig('my_plot.png')
    return [str(time_li*10^-9)+"10^-9",str(time_cubic*10^-9)+"10^-9",str(time_qu*10^-9)+"10^-9"]

if __name__ == "__main__":
    interpolate(0,100,1000)

