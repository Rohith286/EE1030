import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL('./mat3.so')

# Define argument and return types for the functions
lib.createMat.restype = ctypes.POINTER(ctypes.POINTER(ctypes.c_double))
lib.Matsub.restype = ctypes.POINTER(ctypes.POINTER(ctypes.c_double))
lib.Matnorm.restype = ctypes.c_double

# Function to free memory in C
def free_matrix(matrix, rows):
    lib.freeMat(matrix, rows)

# Function to create a matrix
def create_matrix(m, n):
    lib.createMat.argtypes = [ctypes.c_int, ctypes.c_int]
    return lib.createMat(m, n)

# Function to subtract two matrices
def subtract_matrices(a, b, m, n):
    lib.Matsub.argtypes = [ctypes.POINTER(ctypes.POINTER(ctypes.c_double)),
                           ctypes.POINTER(ctypes.POINTER(ctypes.c_double)),
                           ctypes.c_int, ctypes.c_int]
    return lib.Matsub(a, b, m, n)

# Function to calculate norm (Euclidean distance)
def matrix_norm(matrix, m):
    lib.Matnorm.argtypes = [ctypes.POINTER(ctypes.POINTER(ctypes.c_double)),
                            ctypes.c_int]
    return lib.Matnorm(matrix, m)

# Values of a and b
a = 3
b = 4

# Create matrices for A and B
A = create_matrix(2, 1)
B = create_matrix(2, 1)

# Initialize A(a + b, b - a) and B(a - b, a + b)
A[0][0] = a + b
A[1][0] = b - a
B[0][0] = a - b
B[1][0] = a + b

# Lists to store points for plotting
x_vals = []
y_vals = []

# Loop over values of x and calculate y and distances
for x in np.linspace(-10, 10, 100):
    y = (b * x) / a  # y = (b * x) / a from bx = ay
    x_vals.append(x)
    y_vals.append(y)

    # Create matrix P for point P(x, y)
    P = create_matrix(2, 1)
    P[0][0] = x
    P[1][0] = y

    # Calculate distances PA and PB
    PA_diff = subtract_matrices(P, A, 2, 1)
    PB_diff = subtract_matrices(P, B, 2, 1)

    dist_PA = matrix_norm(PA_diff, 2)
    dist_PB = matrix_norm(PB_diff, 2)

    print(f"P({x:.2f}, {y:.2f}): dist(PA) = {dist_PA:.2f}, dist(PB) = {dist_PB:.2f}")

    # Free allocated memory for differences
    free_matrix(PA_diff, 2)
    free_matrix(PB_diff, 2)
    free_matrix(P, 2)

# Free the matrices A and B
free_matrix(A, 2)
free_matrix(B, 2)

# Plotting the graph
plt.plot(x_vals, y_vals, label=f"bx = ay (a={a}, b={b})", color='blue')

# Plot points A and B
plt.scatter([a + b], [b - a], color='red', label='Point A(a+b, b-a)')
plt.scatter([a - b], [a + b], color='green', label='Point B(a-b, a+b)')

# Labels and titles
plt.xlabel('x')
plt.ylabel('y')
plt.title('Locus of Points Satisfying bx = ay with Points A and B')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
