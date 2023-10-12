from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import math

class DemonstrationOne():
    def __init__(self):
        pass
    fig = plt.figure()
 
    # syntax for 3-D projection and mesh grids
    ax = plt.axes(projection ='3d')
    x = np.linspace(-5, 5, 100)  # Adjust the range and resolution as needed
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)

    # Defining space curve
    t = np.linspace(-3, 3, 25) # start at 0, stop at 100
    x_r = t
    y_r = (1 / 2) * (t ** 2) - (1 / 2)
    z_r = (1 / 2) * (t ** 2) + (1 / 2)
    
    # Define surface equations
    z1 = np.sqrt(X ** 2 + Y ** 2)
    z2 = 1 + Y


    # Plot the first surface
    ax.plot_surface(X, Y, z1, cmap='Blues', label='z=sqrt(x^2 + y^2)', alpha=0.3)

    # Plot the second surface
    ax.plot_surface(X, Y, z2, cmap='Oranges', label='z=1 + y', alpha=0.3)
    ax.plot3D(x_r, y_r, z_r, 'TEAL')

    # Set title to graph and show
    ax.set_title('Problem 1')
    plt.show()

class DemonstrationTwo():
    def __init__(self):
        pass
    fig = plt.figure()
 
    # syntax for 3-D projection and mesh grids
    ax = plt.axes(projection ='3d')
    x = np.linspace(-5, 5, 100)  # Adjust the range and resolution as needed
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    
    # Define surface equations
    z1 = np.sqrt(X ** 2 + Y ** 2)
    # z2 = 1 + Y


    # Plot the first surface
    ax.plot_surface(X, Y, z1, cmap='Blues', label='z=sqrt(x^2 + y^2)', alpha=1)

    # Plot the second surface
    # ax.plot_surface(X, Y, z2, cmap='Oranges', label='z=1 + y', alpha=0.3)

    # Set title to graph and show
    ax.set_title('Problem 1')
    plt.show()

class DemonstrationThree():
    def __init__(self):
        pass
    fig = plt.figure()
 
    # syntax for 3-D projection and mesh grids
    ax = plt.axes(projection ='3d')
    x = np.linspace(-5, 5, 100)  # Adjust the range and resolution as needed
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)

    # Defining space curve
    # t = np.linspace(-3, 3, 25) # start at 0, stop at 100
    # x_r = t
    # y_r = (1 / 2) * (t ** 2) - (1 / 2)
    # z_r = (1 / 2) * (t ** 2) + (1 / 2)
    
    # Define surface equations
    # z1 = np.sqrt(X ** 2 + Y ** 2)
    z2 = 1 + Y


    # Plot the first surface
    # ax.plot_surface(X, Y, z1, cmap='Blues', label='z=sqrt(x^2 + y^2)', alpha=0.3)

    # Plot the second surface
    ax.plot_surface(X, Y, z2, cmap='Oranges', label='z=1 + y', alpha=1)
    # ax.plot3D(x_r, y_r, z_r, 'TEAL')

    # Set title to graph and show
    ax.set_title('Problem 1')
    plt.show()

class DemonstrationFour():
    def __init__(self):
        pass
    fig = plt.figure()
 
    # syntax for 3-D projection and mesh grids
    ax = plt.axes(projection ='3d')
    x = np.linspace(-5, 5, 100)  # Adjust the range and resolution as needed
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)

    # Defining space curve
    t = np.linspace(-3, 3, 25) # start at 0, stop at 100
    x_r = t
    y_r = (1 / 2) * (t ** 2) - (1 / 2)
    z_r = (1 / 2) * (t ** 2) + (1 / 2)
    
    # Define surface equations
    # z1 = np.sqrt(X ** 2 + Y ** 2)
    # z2 = 1 + Y


    # Plot the first surface
    # ax.plot_surface(X, Y, z1, cmap='Blues', label='z=sqrt(x^2 + y^2)', alpha=0.3)

    # Plot the second surface
    # ax.plot_surface(X, Y, z2, cmap='Oranges', label='z=1 + y', alpha=0.3)
    ax.plot3D(x_r, y_r, z_r, 'TEAL')

    # Set title to graph and show
    ax.set_title('Problem 1')
    plt.show()
    

