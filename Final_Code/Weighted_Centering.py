import argparse
import numpy as np
import gc

gc.enable()
parser = argparse.ArgumentParser(description='Process input feature vectors(Data Matrix) and apply weighted centering on the vectors.')
parser.add_argument('-f','--file',type=str,action='store',default='sample.npy',required=True,help='File ***path*** without spaces. In case with spaces then example: "hello\ world"')
parser.add_argument('-g','--gamma',type=float,action='store',default=0,help='The gamma value')

args = parser.parse_args()
file_name = args.file
gamma = args.gamma
print file_name

InputData = np.load(args.file)
r,c = InputData.shape
print r
print c

a = np.mean(InputData,axis=0)
d = np.zeros(r)
for i in range(0,r):
	d[i] = (np.dot(InputData[i] , a))**gamma

d = d / np.linalg.norm(d,1)
print d

a = np.add(np.zeros(c),InputData[0]*d[0])
for i in range(1,r):
	a = np.add(a,InputData[i]*d[i])

# Update the origin
InputData = InputData.astype(np.float32)
a = np.divide(a,-1)
for i in range(0,r):
	InputData[i] = np.add(InputData[i],a)
destPath = args.file
destPath = destPath.split('.')
destPath = destPath[0]

np.save(destPath + "_w_centered_" + str(gamma) + ".npy",InputData)