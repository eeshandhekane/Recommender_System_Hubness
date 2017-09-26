1. GKIC.py
This python function is used to evaluate the Goodman-Kruskal Index for data for which distance matrix is known. The inputs are given in command line- The first input is the path of the file containing distance matrix, stored as numpy array (.npy). The second input is the path to the .npy file containing vector of classes for the corresponding data. The third argument is the number of iterations to be performed to calculate the index.
e.g. python GKIC.py distMatrix.npy ratings.npy 3000

2. GKIBC.py, GKIEuc.py
These python function are used to evaluate the Goodman-Kruskal Index for data for which the feature vectors of the data are known. The inputs are given in command line- The first input is the path of the file containing features matrix, stored as numpy array (.npy). The second input is the path to the .npy file containing vector of classes for the corresponding data. The third argument is the number of iterations to be performed to calculate the index. GKIBC.py evaluates Goodman-Kruskal Index using Cosine Distance Metric, and GKIEuc.py does the same by using Euclidean Distance. 
e.g. python GKIBC.py featureMatrix.npy ratings.npy 3000

3. iris.py
This program is used to create the ratings vector and IRIS Feature Vectors and store them in distinct files.

4. ML1.py
This program does the same job as above for MovieLens 100k dataset. 

5. ML2_mod.py
This program does the same job as above for MovieLens 1m dataset. 

6. ML3_mod_part1.py, ML3_mod_part2.py
This program does the same job as above for MovieLens 10m dataset. 

7. sampler1.py, sampler2.py, sampler3.py
These programs take out 10k entries from the datasets to create smaller datasets which can be used for analysis of the hubness reduction algorithms. This is done because of time and space constraints on our machines.
