import pymongo
import numpy as np
import matplotlib.pyplot as plt
import time

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["database"]
mycol = mydb["Interpolate_1"]

def Interpolate(row):
	size = 0
	mongo_docs = [{"x":0, "y":1}]
	x_arr = np.arange(0, (2**10)*np.pi, np.pi/(2**10))
	y_arr = np.cos(x_arr)
	while(row > size):
		for x in x_arr:
			y = np.cos(x)
			mydict = {"x":x, "y":y}
			mongo_docs += [mydict]
		mycol.insert_many(mongo_docs)
		size += 1
	print(x_arr, y_arr)
	#plt.plot(x_arr, y_arr, '-')
	#plt.show()

Interpolate(2**16)
