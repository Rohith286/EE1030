import ctypes
import numpy as np

# Load the shared library
lib = ctypes.CDLL('./libmatrix_distance.so')

# Define the matrix creation function
lib.createMat.argtypes = (ctypes.c_int, ctypes.c_int)
lib.createMat.restype = ctypes.POINTER(ctypes.POINTER(ctypes.c_double))

# Define the matrix free function
lib.freeMat.argtypes = (ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.c_int)

# Define the matrix subtraction function
lib.Matsub.argtypes = (ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.c_int, ctypes.c_int)
lib.Matsub.restype = ctypes.POINTER(ctypes.POINTER(ctypes.c_double))

# Define the norm function
lib.Matnorm.argtypes = (ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.c_int)
lib.Matnorm.restype = ctypes.c_double

# Initialize points P and Q
P = np.array([[2], [-3]], dtype=np.double)
Q1 = np.array([[10], [3]], dtype=np.double)
Q2 = np.array([[10], [-9]], dtype=np.double)

# Convert numpy arrays to ctypes
P_c = (ctypes.POINTER(ctypes.c_double) * 2)(*map(ctypes.POINTER(ctypes.c_double), [ctypes.cast(P[i].ctypes.data, ctypes.POINTER(ctypes.c_double)) for i in range(P.shape[0])]))
Q1_c = (ctypes.POINTER(ctypes.c_double) * 2)(*map(ctypes.POINTER(ctypes.c_double), [ctypes.cast(Q1[i].ctypes.data, ctypes.POINTER(ctypes.c_double)) for i in range(Q1.shape[0])]))
Q2_c = (ctypes.POINTER(ctypes.c_double) * 2)(*map(ctypes.POINTER(ctypes.c_double), [ctypes.cast(Q2[i].ctypes.data, ctypes.POINTER(ctypes.c_double)) for i in range(Q2.shape[0])]))

# Calculate the difference P - Q1 and P - Q2
diff1 = lib.Matsub(Q1_c, P_c, 2, 1)
diff2 = lib.Matsub(Q2_c, P_c, 2, 1)

# Calculate the distance norms
distance1 = lib.Matnorm(diff1, 2)
distance2 = lib.Matnorm(diff2, 2)

print(f"Distance between P and Q1: {distance1:.2f}")
print(f"Distance between P and Q2: {distance2:.2f}")

# Free allocated memory
lib.freeMat(diff1, 2)
lib.freeMat(diff2, 2)
