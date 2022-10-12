from random import randint
from turtle import color

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from mpl_toolkits import mplot3d

import numpy as np
import random

# Generate random initial position
px = np.random.uniform(low=-10, high=10, size=(50,))
py = np.random.uniform(low=-10, high=10, size=(50,))
pz = np.random.uniform(low=-10, high=10, size=(50,))

points = np.column_stack([px,py,pz])

# Generate random initial speeds
vx = np.random.uniform(low=-5, high=5, size=(50,))
vy = np.random.uniform(low=-5, high=5, size=(50,))
vz = np.random.uniform(low=-5, high=5, size=(50,))

vit = np.column_stack([vx,vy,vz])

# Calculation of centroid and average speed vectors
centroid = np.array([px.mean(), py.mean(), pz.mean()])
v_moy = np.array([vx.mean(), vy.mean(), vz.mean()])

# Define forces coefficient
k1 = 0.5
k2 = 0.3
k3 = 3

# Create figure and axe
fig = plt.figure()
fig.patch.set_alpha(0.0)
fig.tight_layout()
ax = plt.axes(projection='3d')

# Function to update the animation
def animate(i):
    r_dir = np.random.uniform(low=-2, high=2, size=(3,))
    for n in range(points.shape[0]):

        # Attraction force
        F1 = k1 * (centroid - points[n])

        # Speed cohesion vector
        F2 = k2 * v_moy + r_dir

        # Array of repulsion for between 1 point and all the others
        rep = np.empty(shape=3)
        for m in range(points.shape[0]):
            if n != m:
                # Calculate the distance between 2 points
                r = points[n] - points[m]

                # Norme of the radius
                r_norm = (r[0]**2 + r[1]**2 + r[2]**2)**(1/2)

                # Force (vector / norme**3)
                F = (r / r_norm**3)

                # Add it to the array
                rep = np.column_stack([rep, F])

        # Final F3 force of repulsion by the mean of the cumulated forces
        F3 = k3 * np.array([rep[0].mean(), rep[1].mean(), rep[2].mean()])

        new_coords = points[n] + F1 + F2 + F3
        points[n] = new_coords
                
    ax.clear()
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], color='#00C853')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.tick_params(axis='z', colors='white')
    ax.set_xlim([-10,10])
    ax.set_ylim([-10,10])
    ax.set_zlim([-10,10])

ani = FuncAnimation(fig, animate, frames=50, interval=100, repeat=True)
#f = "test.gif"
#writergif = PillowWriter(fps=30) 
#ani.save(f, writer=writergif, codec='png', savefig_kwargs={"transparent": True, "facecolor": "none"})

ani.save(
    "test2.gif",
    codec="png",
    dpi=100,
    bitrate=-1,
    savefig_kwargs={"transparent": True, "facecolor": "none"},
)
#plt.show()