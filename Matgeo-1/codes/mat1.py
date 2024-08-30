import ctypes
import math

# Define a structure for the 2D vector in Python to match the C structure
class Vector(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double)]

# Load the shared object file
lib = ctypes.CDLL('./mat1.so')

# Specify the argument types and return type of the C function
lib.calculate_angle.argtypes = (Vector, Vector)
lib.calculate_angle.restype = ctypes.c_double

# Define the wind and boat vectors as per the problem
wind = Vector(36 * math.sqrt(2), 36 * math.sqrt(2))
boat = Vector(0, 51)

# Call the C function to calculate the angle
angle_radians = lib.calculate_angle(wind, boat)

# Convert the result from radians to degrees if necessary
angle_degrees = math.degrees(angle_radians)

# Print the result
print(f"The direction of the flag on the mast of the boat is {angle_degrees:.2f} degrees.")
