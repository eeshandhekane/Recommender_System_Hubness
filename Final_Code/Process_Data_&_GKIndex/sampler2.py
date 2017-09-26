import numpy as np
'''
data =  np.load("Matrix2.npy")
data_new = data[0:10000, :]

np.save("Matrix2_new.npy", data_new)

print data_new
'''

data =  np.load("Rating2.npy")
data_new = data[0:10000, :]

np.save("Ratings2_new.npy", data_new)

print data_new
