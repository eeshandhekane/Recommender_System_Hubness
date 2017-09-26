import argparse
import numpy as np
from sklearn.neighbors import NearestNeighbors
import scipy.stats as sp


parser = argparse.ArgumentParser(description='Measures hubness(Skewness) given data matrix')
parser.add_argument('-f','--file',type=str,action='store',required=True,help='File ***path*** without spaces. In case with spaces then example: "hello\ world"')
parser.add_argument('-k','--KNeighbours',type=int,action='store',default=10,help='Number of neighbours')
parser.add_argument('-m','--DMeasure',type=str,action='store',default='euclidean',help='Distance measure')
parser.add_argument('-r','--Ratio',type=float,action='store',default=0.05,help='Percentage of random samples')

args = parser.parse_args()
print args.file

InputData = np.load(args.file)
r,c = InputData.shape
print r
print c

# Initializing the args parameters
Metric = args.DMeasure
N_neighbours = args.KNeighbours
Ratio = args.Ratio

# Initializing the classifier
if Metric == 'cosine':
	neigh = NearestNeighbors(n_neighbors=N_neighbours, metric=Metric, n_jobs=-2, algorithm='brute')
else:
	neigh = NearestNeighbors(n_neighbors=N_neighbours, metric=Metric, n_jobs=-2)
neigh.fit(InputData)

print "Creating the random points"
N_random_points = int(r*Ratio)
permute = np.random.permutation(r)
Random_points = np.zeros((N_random_points,c))
for i in range(0,N_random_points):
	Random_points[i] = InputData[permute[i]]

print "Getting the neighbours for the randomly chosen points"
Nk = np.zeros(r)
res = neigh.kneighbors(Random_points,return_distance=False)
res = np.reshape(res, res.shape[0]*res.shape[1])
print res

print "Calculating Nk"
for i in range(0,r):
	Nk[i] = np.where(res==i)[0].shape[0]

print "Skewness is: " + str(sp.skew(Nk))