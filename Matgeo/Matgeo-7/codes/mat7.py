import numpy as np
import matplotlib.pyplot as plt

# Load points from the 'parab.dat' file (assuming it has 200 points)
points = np.loadtxt('parab.dat', delimiter=',', comments='The', max_rows=200)

# Extract x and y values
x = points[:, 0]
y = points[:, 1]

# Define a2 and a3 at x = 4 (from y^2 = x => y = ±sqrt(4))
x_a2_a3 = 4
y_a2_a3 = np.sqrt(x_a2_a3)

a2 = np.array([x_a2_a3, -y_a2_a3])  # Point a2 (in the 4th quadrant)
a3 = np.array([x_a2_a3, y_a2_a3])   # Point a3 (in the 1st quadrant)

# Define a0 and a1 for a specific 'a' value (a = 2.52)
a_value = 2.52
y_a0_a1 = np.sqrt(a_value)

a0 = np.array([a_value, -y_a0_a1])  # Point a0 (in the 4th quadrant)
a1 = np.array([a_value, y_a0_a1])   # Point a1 (in the 1st quadrant)

# Plot and label points a2 and a3
plt.scatter(a2[0], a2[1], color='red', zorder=5, label='$a_2(4, -2.00)$')
plt.scatter(a3[0], a3[1], color='red', zorder=5, label='$a_3(4, 2.00)$')

# Plot and label points a0 and a1
plt.scatter(a0[0], a0[1], color='green', zorder=5, label=f'$a_0({a_value:.2f}, {-y_a0_a1:.2f})$')
plt.scatter(a1[0], a1[1], color='green', zorder=5, label=f'$a_1({a_value:.2f}, {y_a0_a1:.2f})$')

# Add vertical line at x = 4
plt.axvline(x=4, color='red', linestyle='--', label='$x = 4$')

# Fill the area between the parabola and x = a_value (0 to a_value) with solid green color
plt.fill_between(x, y, -y, where=(x <= a_value), color='lightgreen', alpha=1, label='Shaded Region 1 (0 to a)')

# Fill the area between the parabola and x = 4 (a_value to 4) with solid blue color
plt.fill_between(x, y, -y, where=((x > a_value) & (x <= 4)), color='magenta', alpha=1, label='Shaded Region 2 (a to 4)')

# Set limits to avoid issues with undefined regions
plt.xlim(0, 4.5)
plt.ylim(-2.5, 2.5)

# Label the axes and add a title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solid Shaded Region with Points $a_0$, $a_1$, $a_2$, and $a_3$')

# Set grid, equal scaling, and legend
plt.grid(True)
plt.axis('equal')
plt.legend()

# Save the plot as an image (optional)
plt.savefig('parabola_with_a0_a1_a2_a3_and_two_solid_shaded_regions.png')

# Show the plot
plt.show()
