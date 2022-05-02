import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import random
print(random.randrange(1000,1000))
def set_graph(): # set display graph function
	plt.ylim(0, 1/9)
	plt.xlim(-2*np.pi, 2*np.pi)
	plt.grid()
	plt.legend(["real",'data', 'linear', 'quadratic', 'cubic'], loc='best')

def f(x): # input function
	return np.cos(-x)**2/9.0

def random_dot(f, start, stop, n_dot): # randomly data function
	x_og = np.linspace(start,stop,n_dot)
	x = np.array([])
	for i in range(n_dot):
		x_ran = random.choice(x_og)
		if(x_ran not in x):
			x = np.append(x, np.array([x_ran]))
	x = np.sort(x)
	y = f(x)
	return x,y

def real_func(start, stop, K_real): # real function
	x_real = np.linspace(start,stop, num=K_real)
	y_real = f(x_real)
	plt.plot(x_real,y_real)

def make_func(f, start, stop, K, O): # interpolate function
	#x,y = random_dot(f, start, stop, K)
	x = np.linspace(start,stop, num=K)
	y = f(x)
	y_li = interp1d(x,y,kind="linear")
	y_qu = interp1d(x,y,kind="quadratic")
	y_cu = interp1d(x,y,kind="cubic")

	xnew = np.linspace(min(x), max(x), num=O)
	plt.plot(x,y,"o")
	plt.plot(xnew,y_li(xnew),"-")
	plt.plot(xnew,y_qu(xnew),"-")
	plt.plot(xnew,y_cu(xnew),"--")

if __name__ == '__main__':
	K = 2**5 # จำนวนจุดใช้ plot interpolate
	K_real = 5000 # จำนวนจุดใช้ plot real function
	O = K*2 # ระยะที่ไป plot interpolate
	start = -2*np.pi # x น้อยสุด
	stop = 2*np.pi # x มากสุด
	real_func(start, stop, K_real)
	make_func(f, start, stop, K, O)
	set_graph() # set graph
	
	plt.show()
