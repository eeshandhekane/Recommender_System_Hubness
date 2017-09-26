from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import argparse
from sklearn import metrics

parser = argparse.ArgumentParser(description='Given distance matrix, gives you globally scaled distance matrix')
parser.add_argument('-d','--DMatrix',type=str,action='store',required=True,help='Distance matrix file ***path*** without spaces. In case with spaces then example: "hello\ world"')

args = parser.parse_args()

D = np.load(args.DMatrix)
m = D.shape[0]
Res = np.zeros((m,m))
print "Completed reading distance matrix"
for i in range(0,m):
	for j in range(i,m):
		t = D[i][j]
		Res[i][j] = Res[j][i] = (np.dot(np.where(D[i]>t,1,0) , np.where(D[j]>t,1,0)))/float(m)
	print i

destPath = args.DMatrix
destPath = destPath.split('.')
destPath = destPath[0]
np.save(destPath + "_GScaled.npy",Res)