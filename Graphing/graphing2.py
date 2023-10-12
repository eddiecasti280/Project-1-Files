from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import math
 
fig = plt.figure()
 
# syntax for 3-D projection
ax = plt.axes(projection ='3d')

x = np.linspace(-5, 5, 100) 
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

t = np.linspace(-1, 1, 5) 
# circumvents a value error where a non-scalar is broadcast to a scalar array
x_r = 1 * (t ** 0)
y_r = 2 + (13 * t)
z_r = (-13 * t)


eq1 = (5 / 2) * X - Y - (1 / 2)
eq2 = 6 - 4 * X - Y

ax.plot_surface(X,Y, eq1, cmap='Oranges', label='z=(5/2)x-y-(1/2)')
ax.plot_surface(X, Y, eq2, cmap='Blues', label='z=1 + y')
ax.plot3D(x_r, y_r, z_r, 'TEAL')

ax.set_title('Problem 2')

plt.show()