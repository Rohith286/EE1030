#Code by GVV Sharma
#May 15, 2024
#released under GNU GPL
#Drawing a triangle given a,angle B and b+c

import sys                                          #for path to external scripts
sys.path.insert(0, '/Users/rohith/Documents/matgeo/codes/CoordGeo')        #path to my scripts
import numpy as np
import numpy.linalg as LA
import scipy.linalg as SA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#Input parameters
a=6
angBdeg=60
angB = np.deg2rad(angBdeg)
k=math.sqrt(31) + 5 
[A,B,C] = tri_const(a,k,angB)

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)


#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')

# Labeling the coordinates and showing them
tri_coords = np.block([[A,B,C]])
plt.scatter(tri_coords[0,:], tri_coords[1,:], color='red')  # Plot points
vert_labels = ['A', 'B', 'C']

for i, txt in enumerate(vert_labels):
    # Create label with point name and coordinates
    label = f'{txt} ({tri_coords[0,i]:.2f}, {tri_coords[1,i]:.2f})'
    plt.annotate(label,  # this is the text including coordinates
                 (tri_coords[0,i], tri_coords[1,i]),  # this is the point to label
                 textcoords="offset points",  # how to position the text
                 xytext=(5,10),  # increased distance from text to points (x,y)
                 ha='center',  # horizontal alignment can be left, right or center
                 fontsize=12,  # Adjust the font size
                 color='black')  # Set a color for the labels

# Rest of the plot setup
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()  # minor
plt.axis('equal')

#if using termux
plt.savefig('/Users/rohith/Desktop/mat5/figs')
#else
#plt.show()