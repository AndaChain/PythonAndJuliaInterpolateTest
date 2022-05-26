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

    start_li = time.time() # set start time 
    f1 = interp1d(x, y)
    end_li = time.time()   # set end time
    if end_li - start_li < 0.000001:
        time_li = "It's less than 1 us"
    else:
        time_li = "{:.6f}".format(round(end_li - start_li, 6))
    print("linear time", time_li)

    start_cu = time.time() # set start time
    f2 = interp1d(x, y, kind='cubic')
    end_cu = time.time()   # set end time
    if end_cu - start_cu < 0.000001:
        time_cu = "It's less than 1 us"
    else:
        time_cu = "{:.6f}".format(round(end_cu - start_cu, 6))
    print("cubic time",time_cu)

    start_qu = time.time() # set start time 
    f3 = interp1d(x, y, kind='quadratic')
    end_qu = time.time()   # set end time 
    if end_qu - start_qu < 0.000001:
        time_qu = "It's less than 1 us"
    else:
        time_qu = "{:.6f}".format(round(end_qu - start_qu, 6))
    print("quadratic time",time_qu)
        
    xnew = np.linspace(start, stop, num=step * 10, endpoint=True)

    import matplotlib.pyplot as plt
    plt.clf()
    plt.plot(x, y, 'o', xnew, f1(xnew), '-', xnew, f2(xnew), '--', xnew, f3(xnew))
    plt.legend(['data', 'linear', 'cubic', 'quadratic'], loc='best')
    plt.savefig('my_plot.png')
    return [time_li,time_cu,time_qu]

if __name__ == "__main__":
    interpolate(1,10,1500)

