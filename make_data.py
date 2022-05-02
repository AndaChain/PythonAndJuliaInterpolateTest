import numpy as np
import pandas as pd
import random
import time

def f(x): # input function
	return np.exp(-x)

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

def Interpolate(K):
	K = K # จำนวนจุดใช้ plot interpolate
	start = -2*np.pi # x น้อยสุด
	stop = 2*np.pi # x มากสุด
	w = open("data.csv","w")
	w.write("x,y\n")
	w.close()
	
	# data of x and y value
	x_arr = np.linspace(start,stop,K)
	y_arr = f(x_arr) 
	data = {
			'x': x_arr,
			'y': y_arr
	}
	
	# Make data frame of above data
	df = pd.DataFrame(data)
	
	# append data frame to CSV file
	df.to_csv('data.csv', mode='a', index=False, header=False)

if __name__ == '__main__':
	print(Interpolate(2**24))
	#x=pd.read_csv('GFG.csv')
	#print(x["x"].to_numpy())
	#a = np.asarray([ [1,2,3], [4,5,6], [7,8,9] ])
	#np.savetxt("foo.csv", a, delimiter=",")
	#x, y = random_dot(f, start, stop, K)
