import numpy as np

'''
# To copy the contents from ratings2 data file to text file
file = open("ratings2.dat", "r")
new = open("ratings2.txt", "a")
lines = file.readlines()
for rows in lines:
    new.write(rows)
new.close()
'''


matrix = np.zeros((1000209, 23)).astype(np.uint16)



# user part
user = open("users2.txt", "r")
userList = user.readlines()
userSize = len(userList)
userMatrix = np.zeros((6040, 4)).astype(np.uint16)

for i in range(userSize) :
    temp = userList[i].split("::")
    del temp[-1]

    temp[0] = int(temp[0])
    temp[2] = int(temp[2])
    temp[3] = int(temp[3])

    if temp[1] == 'M' :
        temp[1] = 0
    else :
        temp[1] = 1

    userMatrix[i] = temp



# item part
item = open("movies2.txt", "r")
itemList = item.readlines()
itemSize = len(itemList)

movieList = []
movieID = []
movieMatrix = np.zeros((3952, 19)).astype(np.uint16)

for i in range(itemSize):
    temp = itemList[i].split('::')
    if i != itemSize-1:
        temp[2] = temp[2].rstrip(temp[2][-1:])
    genreList = temp[2].split('|')
    genreSize = len(genreList)
    currInd = int(temp[0])-1
    for j in  range(genreSize) :
        if genreList[j] == 'Action':
            movieMatrix[currInd][0] = 1
        if genreList[j] == 'Adventure':
            movieMatrix[currInd][1] = 1
        if genreList[j] == 'Animation':
            movieMatrix[currInd][2] = 1
        if genreList[j] == "Children's":
            movieMatrix[currInd][3] = 1
        if genreList[j] == 'Comedy':
            movieMatrix[currInd][4] = 1
        if genreList[j] == 'Crime':
            movieMatrix[currInd][5] = 1
        if genreList[j] == 'Documentary':
            movieMatrix[currInd][6] = 1
        if genreList[j] == 'Drama':
            movieMatrix[currInd][7] = 1
        if genreList[j] == 'Fantasy':
            movieMatrix[currInd][8] = 1
        if genreList[j] == 'Film-Noir':
            movieMatrix[currInd][9] = 1
        if genreList[j] == 'Horror':
            movieMatrix[currInd][10] = 1
        if genreList[j] == 'Musical':
            movieMatrix[currInd][11] = 1
        if genreList[j] == 'Mystery':
            movieMatrix[currInd][12] = 1
        if genreList[j] == 'Romance':
            movieMatrix[currInd][13] = 1
        if genreList[j] == 'Sci-Fi':
            movieMatrix[currInd][14] = 1
        if genreList[j] == 'Thriller':
            movieMatrix[currInd][15] = 1
        if genreList[j] == 'War':
            movieMatrix[currInd][16] = 1
        if genreList[j] == 'Western':
            movieMatrix[currInd][17] = 1
    movieMatrix[currInd][18] = temp[0]
    movieList.append(temp[1])
#print movieList
#print movieMatrix[3]


# Final features matrix
data = open("ratings2.txt", 'r')
dataList = data.readlines()
dataSize = len(dataList)
ratings = np.zeros([1000209, 1]).astype(np.uint16)

tempList = np.zeros((3952)).astype(np.uint16)
for i in range(3952):
    tempList[i] = (movieMatrix[i][18])


for i in range(dataSize):
    temp = dataList[i].split("::")
    userInd = int(temp[0])
    movieInd = int(temp[1])
    ratings[i] = int(temp[2])
    for j in range(4):
        matrix[i][j] = userMatrix[userInd-1][j]
    #search = np.where(tempList==movieInd)
    #print int(search[0])
    matrix[i][4] = movieMatrix[movieInd-1][18]
    for k in range(18):
        matrix[i][5+k] = movieMatrix[movieInd-1][k]
    print("Rating "+str(i)+" completed")

#print matrix[5]
#print ratings[5]
np.save("Matrix2.npy", matrix)
np.save("Rating2.npy", ratings)
