import numpy as np
import matplotlib.pyplot as plt

# Load the points from the text file
points = np.genfromtxt("circle.dat", delimiter=' ', dtype=float)

# Check if points were loaded correctly
if points.shape[1] != 2:
    raise ValueError("The file does not contain valid coordinate data.")

# Assign points in the order A, C, and B
A = points[0]  # First point from circle.dat
C = points[1]  # Second point from circle.dat
B = points[2]  # Third point from circle.dat

# Print the coordinates of A, C, and B
print(f"Coordinates of Triangle Vertices:\nA: {A}\nC: {C}\nB: {B}")

# Function to calculate the circumcircle center and radius
def circumcircle(A, B, C):
    D = 2 * (A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1]))

    if D == 0:
        raise ValueError("The points are collinear, no circumcircle exists.")

    # Circumcenter coordinates (Ox, Oy)
    Ox = ((A[0]**2 + A[1]**2) * (B[1] - C[1]) +
          (B[0]**2 + B[1]**2) * (C[1] - A[1]) +
          (C[0]**2 + C[1]**2) * (A[1] - B[1])) / D

    Oy = ((A[0]**2 + A[1]**2) * (C[0] - B[0]) +
          (B[0]**2 + B[1]**2) * (A[0] - C[0]) +
          (C[0]**2 + C[1]**2) * (B[0] - A[0])) / D

    # Radius of the circumcircle
    center = np.array([Ox, Oy])
    radius = np.linalg.norm(A - center)
    
    return center, radius

# Calculate the circumcenter and radius
center, radius = circumcircle(A, B, C)
print(f"Circumcircle Center: {center}, Radius: {radius}")

# Function to generate circle points
def circ_gen(center, radius, num_points=1000):
    theta = np.linspace(0, 2 * np.pi, num_points)
    x_circ = radius * np.cos(theta) + center[0]
    y_circ = radius * np.sin(theta) + center[1]
    return x_circ, y_circ

# Generate the circumcircle
x_circ, y_circ = circ_gen(center, radius)

# Plotting the circumcircle and triangle
plt.figure(figsize=(8, 8))

# Plot the triangle
plt.plot([A[0], B[0]], [A[1], B[1]], 'b-', label='AB')
plt.plot([B[0], C[0]], [B[1], C[1]], 'b-', label='BC')
plt.plot([C[0], A[0]], [C[1], A[1]], 'b-', label='CA')

# Plot points A, C, B
plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], color=['red', 'green', 'blue'], zorder=5)
plt.text(A[0], A[1], f'A({A[0]:.2f}, {A[1]:.2f})', fontsize=10, verticalalignment='bottom', horizontalalignment='right')
plt.text(B[0], B[1], f'B({B[0]:.2f}, {B[1]:.2f})', fontsize=10, verticalalignment='bottom', horizontalalignment='right')
plt.text(C[0], C[1], f'C({C[0]:.2f}, {C[1]:.2f})', fontsize=10, verticalalignment='bottom', horizontalalignment='right')

# Plot the circumcircle
plt.plot(x_circ, y_circ, 'orange', label=f'Circumcircle (Radius = {radius:.2f})')

# Mark the circumcenter
plt.scatter(center[0], center[1], color='purple', zorder=5)
plt.text(center[0], center[1], f'Center({center[0]:.2f}, {center[1]:.2f})', fontsize=10, verticalalignment='top', horizontalalignment='right')

# Set plot labels and settings
plt.xlabel('x')
plt.ylabel('y')
plt.title('Circumcircle and Triangle formed by Points A, C, and B')
plt.grid(True)
plt.legend(loc='upper right')
plt.axis('equal')

# Show the plot
plt.show()
