#Code by GVV Sharma
#May 15, 2024
#released under GNU GPL
#Drawing a triangle given a,angle B and b+c

import sys                                          # for path to external scripts
sys.path.insert(0, '/Users/rohith/Documents/matgeo/codes/CoordGeo')  # path to my scripts
import numpy as np
import numpy.linalg as LA
import scipy.linalg as SA
import matplotlib.pyplot as plt
import matplotlib.patches as patches  # for drawing the arc
import math

# local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

# Function to draw an arc for the angle at point B
def draw_angle_arc(ax, B, A, C, angle, radius=1):
    # Calculate angle at B in degrees
    angle_deg = np.degrees(angle)
    
    # Create an arc centered at B with specified angle range and radius
    arc = patches.Arc(B, 2*radius, 2*radius, angle=0, theta1=0, theta2=angle_deg, color='green', lw=2)
    ax.add_patch(arc)
    
    # Find the midpoint of the arc to place the angle label
    mid_angle = angle / 2
    mid_x = B[0] + radius * np.cos(mid_angle)
    mid_y = B[1] + radius * np.sin(mid_angle)
    
    # Label the angle at B
    ax.text(mid_x, mid_y, f'{angle_deg:.1f}°', fontsize=12, color='green')

# Input parameters
a = 6
angBdeg = 60  # Angle at B in degrees
angB = np.deg2rad(angBdeg)  # Convert angle to radians
k = math.sqrt(31) + 5 
[A, B, C] = tri_const(a, k, angB)

# Generating all lines
x_AB = line_gen(A, B)
x_BC = line_gen(B, C)
x_CA = line_gen(C, A)

# Plotting all lines
fig, ax = plt.subplots()
ax.plot(x_AB[0, :], x_AB[1, :], label='$AB$')
ax.plot(x_BC[0, :], x_BC[1, :], label='$BC$')
ax.plot(x_CA[0, :], x_CA[1, :], label='$CA$')

# Labeling the coordinates and showing them
tri_coords = np.block([[A, B, C]])
ax.scatter(tri_coords[0, :], tri_coords[1, :], color='red')  # Plot points
vert_labels = ['A', 'B', 'C']

for i, txt in enumerate(vert_labels):
    # Create label with point name and coordinates
    label = f'{txt} ({tri_coords[0,i]:.2f}, {tri_coords[1,i]:.2f})'
    ax.annotate(label,  # this is the text including coordinates
                (tri_coords[0,i], tri_coords[1,i]),  # this is the point to label
                textcoords="offset points",  # how to position the text
                xytext=(5,10),  # increased distance from text to points (x,y)
                ha='center',  # horizontal alignment can be left, right or center
                fontsize=12,  # Adjust the font size
                color='black')  # Set a color for the labels

# Drawing the angle arc at B (vertex)
draw_angle_arc(ax, B, A, C, angB, radius=1)  # Draw arc for 60 degrees

# Rest of the plot setup
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.legend(loc='best')
ax.grid()  # minor
ax.set_aspect('equal', adjustable='datalim')

# Save or display the plot
#if using termux
plt.savefig('/Users/rohith/Desktop/mat5/figs')
#else
plt.show()
