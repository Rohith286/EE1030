import sys  # for path to external scripts
sys.path.insert(0, '/Users/rohith/matgeo/codes/CoordGeo')  # path to my scripts

import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# local imports (assuming you have these functions defined in your own scripts)
from line.funcs import *  # You can replace this with the actual function name if needed
from triangle.funcs import *  # You can replace this with the actual function name if needed
from conics.funcs import circ_gen  # Replace with relevant function or remove if unused

# Function to calculate the unit vector
def unit_vector(v):
    return v / LA.norm(v)

# Given vectors a and b
a = np.array([1, 1, 2]).reshape(-1, 1)
b = np.array([2, 1, -2]).reshape(-1, 1)

# a) Unit vector in the direction of 6a
vector_6a = 6 * a
unit_6a = unit_vector(vector_6a)

# b) Unit vector in the direction of 2a - b
vector_2a_b = 2 * a - b
unit_2a_b = unit_vector(vector_2a_b)

print("Unit vector in the direction of 6a:\n", unit_6a)
print("\nUnit vector in the direction of 2a - b:\n", unit_2a_b)

# Create a 3D plot to visualize the vectors
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the vectors 6a and 2a-b
ax.quiver(0, 0, 0, vector_6a[0], vector_6a[1], vector_6a[2], color='blue', label='6a')
ax.quiver(0, 0, 0, vector_2a_b[0], vector_2a_b[1], vector_2a_b[2], color='red', label='2a - b')

# Plot the unit vectors
ax.quiver(0, 0, 0, unit_6a[0], unit_6a[1], unit_6a[2], color='green', label='Unit vector of 6a', linestyle='dashed')
ax.quiver(0, 0, 0, unit_2a_b[0], unit_2a_b[1], unit_2a_b[2], color='purple', label='Unit vector of 2a - b', linestyle='dashed')

# Set labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()

#if using termux
# plt.savefig('chapters/12/11/3/6/figs/fig.pdf')
# subprocess.run(shlex.split("termux-open chapters/12/11/3/6/figs/fig.pdf"))
#else:
# plt.show()
