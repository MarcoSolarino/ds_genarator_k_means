import random
import csv
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import sklearn.datasets as sk

# np.random.seed()
X, y = sk.make_blobs(n_samples=1000, n_features=2, centers=4, cluster_std=1)

array = X.tolist()

for a in array:
    a.append(0)

nparray = np.array(array)

np.savetxt("dataset.csv", nparray, delimiter=",", fmt='%f')

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(X[:, 0], X[:, 1], X[:, 2], marker='.')
#
# ax.set_xlabel('X Axis')
# ax.set_ylabel('Y Axis')
# ax.set_zlabel('Z Axis')
#
# plt.show()

fig = plt.figure()
plt.scatter(X[:, 0], X[:, 1])
plt.show()
