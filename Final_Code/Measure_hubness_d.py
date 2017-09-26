import argparse
import numpy as np
from sklearn.neighbors import NearestNeighbors
import scipy.stats as sp


parser = argparse.ArgumentParser(description='Measures hubness(Skewness) given distance matrix')
parser.add_argument('-f','--file',type=str,action='store',required=True,help='File ***path*** without spaces. In case with spaces then example: "hello\ world"')
parser.add_argument('-k','--KNeighbours',type=int,action='store',default=10,help='Number of neighbours')
parser.add_argument('-r','--Ratio',type=float,action='store',default=0.05,help='Percentage of random samples')

args = parser.parse_args()
print args.file

InputData = np.load(args.file)
Ratio = args.Ratio
r,c = InputData.shape
print r
print c

N_neighbours = args.KNeighbours

print "Creating the random points"
N_random_points = int(r*Ratio)
permute = np.random.permutation(r)

print "Getting the neighbours for the randomly chosen points"
Nk = np.zeros(r)
List = []
for i in range(0,N_random_points):
	List.append(InputData[permute[i]].argsort()[:N_neighbours][::1].tolist())
List = np.array(List).astype(np.uint16)
print List
List = np.reshape(List, List.shape[0]*List.shape[1])

print "Calculating Nk"
for i in range(0,r):
	Nk[i] = np.where(List==i)[0].shape[0]

print Nk
sum1 = 0
for i in Nk:
	sum1 += i
print sum1
print "Skewness is: " + str(sp.skew(Nk))