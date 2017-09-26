import numpy as np
'''
data =  np.load("Matrix3part1.npy")
data_new = data[0:10000, :]

np.save("Matrix3_new.npy", data_new)

print data_new
'''
data =  np.load("Ratings3part1.npy")
data_new = data[0:10000, :]

np.save("Ratings3_new.npy", data_new)

print data_new