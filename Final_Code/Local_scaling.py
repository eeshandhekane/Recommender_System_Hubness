from sklearn.neighbors import NearestNeighbors
import numpy as np
import argparse
import math
import scipy.spatial.distance as Dist

parser = argparse.ArgumentParser(description='Given data matrix, gives you locally scaled distance matrix')
parser.add_argument('-f','--File',type=str,action='store',required=True,help='File ***path*** without spaces. In case with spaces then example: "hello\ world"')
parser.add_argument('-n','--Nneighbors',type=int,action='store',default=7,help='The number of neighbours to be considered while applying local scaling.')

args = parser.parse_args()

InputData = np.load(args.File)
r,c = InputData.shape
print r
print c

N_neighbours = args.Nneighbors
neigh = NearestNeighbors(n_neighbors=N_neighbours, metric='l2', n_jobs=-2)
print "Creating neighbours tree"
neigh.fit(InputData)
print "Created neighbours tree"
dist, ind = neigh.kneighbors(InputData,return_distance=True)
print "Getting neighbours"
resData = np.zeros((r,r))

sigma = np.zeros(r)
print "Calculating sigma"
for i in range(0,r):
	sigma[i] = np.std(dist[i])
print "Creating the distance matrix"
for i in range(0,r):
	for j in range(i,r):
		temp = -1 * (Dist.euclidean(InputData[i],InputData[j]) ** 2)
		resData[i][j] = resData[j][i] = math.exp(temp/(sigma[i]*sigma[j]))
	print i
print "Saving the distance matrix"
destPath = args.File
destPath = destPath.split('.')
destPath = destPath[0]
np.save(destPath + "_LScaled.npy",resData)