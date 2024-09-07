import numpy as np
import matplotlib.pyplot as plt

# Define points
P = np.array([2, -3]).reshape(-1, 1)
x1 = 10
y1 = 3  # One possible value for y
y2 = -9  # Second possible value for y

# Point Q1 and Q2 for the two y-values
Q1 = np.array([x1, y1]).reshape(-1, 1)
Q2 = np.array([x1, y2]).reshape(-1, 1)

# Function to generate points on the line
def line_gen(A, B):
    len = 10
    dim = A.shape[0]
    x_AB = np.zeros((dim, len))
    lam_1 = np.linspace(0, 1, len)
    for i in range(len):
        temp1 = A + lam_1[i] * (B - A)
        x_AB[:, i] = temp1.T
    return x_AB

# Generating line points for both pairs
line1 = line_gen(P, Q1)
line2 = line_gen(P, Q2)

# Plotting the points and lines
plt.plot(line1[0, :], line1[1, :], label=f'Line P to Q1 (10, {y1})')
plt.plot(line2[0, :], line2[1, :], label=f'Line P to Q2 (10, {y2})')

# Plot the points
plt.plot(P[0], P[1], 'bo', label='P(2, -3)')
plt.plot(Q1[0], Q1[1], 'ro', label=f'Q1(10, {y1})')
plt.plot(Q2[0], Q2[1], 'go', label=f'Q2(10, {y2})')

# Adding labels
plt.text(P[0]+0.2, P[1], 'P(2, -3)')
plt.text(Q1[0]+0.2, Q1[1], f'Q1(10, {y1})')
plt.text(Q2[0]+0.2, Q2[1], f'Q2(10, {y2})')

# Set plot limits and title
plt.xlim(0, 12)
plt.ylim(-10, 5)
plt.grid(True)
plt.legend()
plt.title('Distance between P(2, -3) and Q(10, y)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show plot
plt.show()
