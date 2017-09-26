import argparse
import numpy as np

parser = argparse.ArgumentParser(description='Process input feature vectors(Data Matrix) and apply centering on the vectors.')
parser.add_argument('-f','--file',type=str,action='store',default='sample.npy',required=True,help='File ***path*** without spaces. In case with spaces then example: "hello\ world"')

args = parser.parse_args()
print args.file

# Read input data
InputData = np.load(args.file).astype(np.float32)
r,c = InputData.shape
print r
print c

a = np.mean(InputData,axis=0)
# Update the origin
a = np.divide(a,-1)
for i in range(0,r):
	InputData[i] = np.add(InputData[i],a)
destPath = args.file
destPath = destPath.split('.')
destPath = destPath[0]
print a
np.save(destPath + "_centered.npy",InputData)