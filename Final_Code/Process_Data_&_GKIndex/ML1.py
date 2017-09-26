import numpy as np


'''
# Stripping off last chars from a string
x = 'string12'
x = x.rstrip(x[-2:])
print x
'''


'''
# declaring an np matrix
matrix = np.zeros((3, 4))
print matrix
matrix[1, 2] = 4
print matrix
'''


matrix = np.zeros((100000, 24)).astype(np.uint16)


# user part
user = open("user.txt", "r")
userList = user.readlines()
userSize = len(userList)
userMatrix = np.zeros((943, 4)).astype(np.uint16)

for i in range(userSize) :
    temp = userList[i].split("|")
    del temp[-1]

    if temp[2] == 'M' :
        temp[2] = 0
    else :
        temp[2] = 1

    if temp[3] == 'administrator':
        temp[3] = 1
    if temp[3] == 'artist':
        temp[3] = 2
    if temp[3] == 'doctor':
        temp[3] = 3
    if temp[3] == 'educator':
        temp[3] = 4
    if temp[3] == 'engineer':
        temp[3] = 5
    if temp[3] == 'entertainment':
        temp[3] = 6
    if temp[3] == 'executive':
        temp[3] = 7
    if temp[3] == 'healthcare':
        temp[3] = 8
    if temp[3] == 'homemaker':
        temp[3] = 9
    if temp[3] == 'lawyer':
        temp[3] = 10
    if temp[3] == 'librarian':
        temp[3] = 11
    if temp[3] == 'marketing':
        temp[3] = 12
    if temp[3] == 'none':
        temp[3] = 13
    if temp[3] == 'other':
        temp[3] = 14
    if temp[3] == 'programmer':
        temp[3] = 15
    if temp[3] == 'retired':
        temp[3] = 16
    if temp[3] == 'salesman':
        temp[3] = 17
    if temp[3] == 'scientist':
        temp[3] = 18
    if temp[3] == 'student':
        temp[3] = 19
    if temp[3] == 'technician':
        temp[3] = 20
    if temp[3] == 'writer':
        temp[3] = 21

    userMatrix[i] = temp


# Item part
item = open("item.txt", "r")
itemList = item.readlines()
itemSize = len(itemList)

movieList = []
movieID = []
movieDate = []
movieGenre = np.zeros((1682, 19)).astype(np.uint16)
numDate = []

for i in range(itemSize):
    temp = itemList[i].split('|')
    movieID.append(int(temp[0]))
    movieList.append(temp[1])
    movieDate.append(temp[2])
    for j in range(19):
        movieGenre[i][j] = int(temp[5 + j])

#print movieDate

'''
dateSize = len(movieDate)
for i in range(dateSize):
    temp = movieDate[i]
    Date = int(temp[0])*10+int(temp[1])
    Year = int(temp[7])*1000+int(temp[8])*100+int(temp[9])*10+int(temp[10])
    if temp[3] == 'D':
        Month = 12
    if temp[3] == 'N':
        Month = 11
    if temp[3] == 'O':
        Month = 10
    if temp[3] == 'S':
        Month = 9
    if temp[3] == 'A' and temp[4] == 'u':
        Month = 8
    if temp[3] == 'A' and temp[4] == 'p':
        Month = 4
    if temp[3] == 'J' and temp[4] == 'u' and temp[5] == 'l':
        Month = 7
    if temp[3] == 'J' and temp[4] == 'u' and temp[5] == 'n':
        Month = 6
    if temp[3] == 'M' and temp[4] == 'a' and temp[5] == 'y':
        Month = 5
    if temp[3] == 'M' and temp[4] == 'a' and temp[5] == 'r':
        Month = 3
    if temp[3] == 'F':
        Month = 2
    if temp[3] == 'J' and temp[4] == 'a' and temp[5] == 'n':
        Month = 1
'''

# Final features matrix
data = open("data.txt", 'r')
dataList = data.readlines()
dataSize = len(dataList)
ratings = np.zeros([100000, 1]).astype(np.uint16)

for i in range(dataSize):
    temp = dataList[i].split("\t")
    userInd = int(temp[0])
    for j in range(4):
        matrix[i][j] = userMatrix[userInd-1][j]
    movIndex = int(temp[1])
    matrix[i][4] = movIndex
    for k in range(19):
        matrix[i][5 + k] = movieGenre[movIndex-1][k]
    ratings[i] = int(temp[2])

print matrix[5]
np.save("Matrix1.npy", matrix)
print ratings[5]
np.save("Ratings1.npy", ratings)
