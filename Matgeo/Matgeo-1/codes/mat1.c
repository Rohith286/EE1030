#include <stdio.h>
#include <math.h>

// Define the structure for a 2D vector
typedef struct {
    double x;
    double y;
} Vector;

// Function to compute the resultant vector
Vector calculate_resultant_vector(Vector wind, Vector boat) {
    Vector resultant;
    resultant.x = wind.x; // x component remains the same as wind
    resultant.y = wind.y - boat.y; // y component is wind - boat
    return resultant;
}

// Function to compute the angle using arctan
double calculate_angle(Vector wind, Vector boat) {
    Vector resultant = calculate_resultant_vector(wind, boat);
    return atan(resultant.y / resultant.x); // Angle in radians
}
