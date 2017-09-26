from __future__ import division
import numpy as np
import random as r
from scipy.spatial import distance
import sys

# Input the distance matrix as D, and the class vector as C, number of iterations is optional and is itr

def D(a, b, VV):
    return VV[a][b]
    #item1 = VV[a]
    #item2 = VV[b]
    #return distance.euclidean(item1, item2)

inList = sys.argv
inLen = len(inList)

V = np.load(inList[1])
C = np.load(inList[2])
itr = long(inList[3])

Qc = 0
Qd = 0
    #size = D.shape
    #matSize = size[0]
size = C.shape
classSize = size[0]

classList = []
classCount = 0
classes = []

C = C.tolist()
#V = VV.tolist()

for i in range(classSize):
    if C[i] not in classList:
        classList.append(C[i])
        classCount = classCount+1
        classes.append([])
        classes[-1].append(i)
    else :
        j = 0
        while(classList[j]) != C[i]:
            j = j+1
        classes[j].append(i)


    #print classes
ans = 0.0
for trials in range(500):
    Qc = 0
    Qd = 0
    for iterations in range(itr):
        classI = r.randint(0, classCount-1)
        classK = r.randint(0, classCount-1)
        classL = r.randint(0, classCount-1)
        while classK == classL:
            classL = r.randint(0, classCount-1)

        i = r.choice(classes[classI])
        j = r.choice(classes[classI])
        k = r.choice(classes[classK])
        l = r.choice(classes[classL])

        if V[i][j] <= V[k][l]:
            Qc = Qc+1
        else:
            Qd = Qd+1
    trialAns = (float)(Qc-Qd)/(Qc+Qd)
    ans = ans + trialAns

file = open("Result1.txt", "a")
ans = (float)(ans)/500
file.write("Input = " + inList[1] + " " + inList[2] + " " + "\t\t\t" +"Goodman-Kruskal Index = " + str(ans)+"\n")