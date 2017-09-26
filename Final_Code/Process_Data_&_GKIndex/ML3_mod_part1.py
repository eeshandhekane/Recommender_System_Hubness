import numpy as np

matrix = np.zeros((10000054/2, 20)).astype(np.uint32)

item = open("movies.dat", "r")
itemList = item.readlines()
itemSize = len(itemList)

movieList = []
movieID = []
movieMatrix = np.zeros((65133, 19)).astype(np.uint32)

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

data = open("ratings.dat", 'r')
dataList = data.readlines()
dataSize = len(dataList)/2
ratings = np.zeros([10000054/2, 1])

#tempList = np.zeros(10681).astype(np.uint32)
#for i in range(10681):
#    tempList[i] = (movieMatrix[i][18])


for i in range(dataSize):
    temp = dataList[i].split("::")
    userInd = long(temp[0])
    movieInd = int(temp[1])
    ratings[i] = (temp[2])
    #search = np.where(tempList==movieInd)
    #print int(search[0][0])
    matrix[i][1] = movieMatrix[movieInd-1][18]
    #for k in range(18):
    #    matrix[i][1+k] = movieMatrix[search[0][0]][k]
    for k in range(18):
        matrix[i][2+k] = movieMatrix[movieInd-1][k]
    print("Rating "+str(i)+" completed")
    matrix[i][0] = userInd

#print matrix[5]
#print ratings[5]
np.save("Ratings3part1.npy", ratings)
np.save("Matrix3part1.npy", matrix)