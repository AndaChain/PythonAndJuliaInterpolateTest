#Numpy
import datetime
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interpolate
from scipy.interpolate import interp1d
from scipy.interpolate import lagrange

def fx(x):
    return np.cos(-x)**2/9.0

def interpolate():

    start = -2*np.pi
    stop = 2*np.pi
    step = 5000
    x = np.linspace(start, stop, num=step, endpoint=True)
    y = fx(x)

    start_li = datetime.datetime.now() # set start time 
    f1 = interp1d(x, y)
    end_li = datetime.datetime.now()   # set end time
    time_li = end_li - start_li
    print("linear time", time_li)

    start_cu = datetime.datetime.now() # set start time
    f2 = interp1d(x, y, kind='cubic')
    end_cu = datetime.datetime.now()   # set end time
    time_cubic = end_cu - start_cu
    print("cubic time",time_cubic)

    start_qu = datetime.datetime.now() # set start time 
    f3 = interp1d(x, y, kind='quadratic')
    end_qu = datetime.datetime.now()   # set end time 
    time_qu = end_qu - start_qu
    print("quadratic time",time_qu)
        
    xnew = np.linspace(start, stop, num=step, endpoint=True)

    import matplotlib.pyplot as plt
    plt.plot(x, y, 'o', xnew, f1(xnew), '-', xnew, f2(xnew), '--', xnew, f3(xnew))
    plt.legend(['data', 'linear', 'cubic', 'quadratic'], loc='best')
    plt.savefig('my_plot.png')
    return [str(time_li),str(time_cubic),str(time_qu)]

interpolate()

