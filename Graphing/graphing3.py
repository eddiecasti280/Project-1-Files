import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.cm as cm
from matplotlib.colors import Normalize

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

v1 = np.array([5, 1, -3]) # A
v2 = np.array([1, -1, 0]) # B
v3 = np.array([2,-2,0]) # proj A onto B
v4 = np.array([3,3,-3]) # Orthogonal part

ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='r', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='b', arrow_length_ratio=0.1)
# ax.quiver(0, 0, 0, v3[0], v3[1], v3[2], color='g', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, v4[0], v4[1], v4[2], color='y', arrow_length_ratio=0.1)

ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])
plt.show()