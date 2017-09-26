import numpy as np
'''
data =  np.load("Matrix1.npy")
data_new = data[0:10000, :]

#np.save("Matrix1_new.npy", data_new)

print data_new
'''
data =  np.load("Ratings1.npy")
data_new = data[0:10000, :]

np.save("Ratings1_new.npy", data_new)

print data_new