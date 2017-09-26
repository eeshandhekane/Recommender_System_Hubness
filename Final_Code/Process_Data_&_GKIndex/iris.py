import numpy as np
import random

iris = open("iris.txt", "r")
iris_ext =open("iris_ext.txt", "a")
lines = iris.readlines()
#print lines

matrix = np.zeros((15000, 4))
combined = np.zeros((15000, 5))
ratings = np.zeros((15000, 1))

numLine = len(lines)

for itr in range(100):
    offset = 150*itr
    for rows in range(numLine):
        temp = lines[rows].split(',')
        for j in range(4):
            combined[rows + offset][j] = float(temp[j])
            matrix[rows + offset][j] = float(temp[j])
        if rows!= len(lines) - 1:
            temp[-1] = (temp[-1]).rstrip((temp[-1])[-1:])
 #           print temp
        if temp[-1] == 'Iris-versicolor':
               ratings[rows + offset] = 2
               combined[rows + offset][4] = 2
        if temp[-1] == 'Iris-setosa':
               ratings[rows + offset] = 1
               combined[rows + offset][4] = 1
        if temp[-1] == 'Iris-virginica':
               ratings[rows + offset] = 3
               combined[rows + offset][4] = 3


for i in range(15000):
    for j in range(4):
        randChange = (float)(random.random())/10;
        rNum = random.randint(1, 2)
        if rNum == 1:
            sign = +1
        else:
            sign = -1
        combined[i][j] = combined[i][j]+sign*randChange
        matrix[i][j] = matrix[i][j]+sign*randChange

#print ratings
print len(combined)
#print matrix


np.save("MatrixIRIS", matrix)
np.save("RatingsIRIS", ratings)
np.save("CombinedIRIS", combined)