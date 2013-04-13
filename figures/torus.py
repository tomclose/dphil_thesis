from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

def surf(u, v):
    X = np.cos(u)*(4 + np.cos(v))
    Y = np.sin(u)*(4 + np.cos(v))
    Z = np.sin(v)
    return X,Y,Z

ux, vx =  np.meshgrid(np.linspace(0, 2*np.pi, 20),
                      np.linspace(0, 2*np.pi, 20))
x,y,z = surf(ux, vx)

fig = plt.figure()
ax = fig.gca(projection="3d")
ax.set_zlim([-5, 5])

plot = ax.plot_wireframe(x,y,z, rstride=1, cstride=1)

plt.show()

