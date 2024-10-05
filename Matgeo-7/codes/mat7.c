#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include "libs/matfun.h"
#include "libs/geofun.h"

// Generate points for the parabola y^2 = x (both quadrants)
void parab_y2_x_gen(FILE *fptr, double a, int num_points) {
    double t_max = sqrt(4); // For y=2, x will be 4
    double **point = createMat(2, 1);   // Create a 2x1 point matrix

    // Generate points for positive and negative branches
    for (double t = 0; t <= t_max; t += t_max / num_points) {
        point[0][0] = t * t;     // x = y^2
        point[1][0] = t;         // Positive branch
        fprintf(fptr, "%lf,%lf\n", point[0][0], point[1][0]);  // First quadrant point
        fprintf(fptr, "%lf,%lf\n", point[0][0], -point[1][0]); // Fourth quadrant point (negative y)
    }
    freeMat(point, 2);  // Free dynamically allocated memory
}

// Function to calculate y = sqrt(x) for y^2 = x
double function(double x) {
    return sqrt(x);  // y = sqrt(x) for y^2 = x
}

// Calculate the area under the curve from lower_limit to upper_limit using numerical integration
double area(double lower_limit, double upper_limit) {
    double sum = 0;
    for (double i = lower_limit; i <= upper_limit; i += 1e-7) {
        sum += function(i) * 1e-7;  // Approximation using rectangles
    }
    return sum;
}

// Function to find the value of 'a' that divides the area into two equal parts
double find_a() {
    double total_area = area(0, 4);  // Total area from 0 to 4
    double half_area = total_area / 2;  // Half of the total area
    double lower_bound = 0.0;
    double upper_bound = 4.0;
    double a;

    // Bisection method to find 'a'
    while ((upper_bound - lower_bound) > 1e-6) {
        a = (lower_bound + upper_bound) / 2.0;
        double area_a = area(0, a);  // Area up to a^2
        if (area_a < half_area) {
            lower_bound = a;  // Move the lower bound up
        } else {
            upper_bound = a;  // Move the upper bound down
        }
    }
    return a;
}

int main() {
    // Find the value of 'a'
    double a_value = find_a();
    printf("The value of a that divides the area into two equal parts is: %lf\n", a_value);

    // Prepare for writing points to file
    FILE *fptr = fopen("parab.dat", "w");
    if (fptr == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Generate points of the parabola in both quadrants and write to the file
    parab_y2_x_gen(fptr, a_value, 100);  // Generate 100 points in both quadrants

    // Write the total area to the file
    double total_area = area(0, 4);  // Calculate the total area again
    fprintf(fptr, "The total area under the curve from 0 to 4 is %lf\n", total_area);

    // Close the file and free allocated memory
    fclose(fptr);

    return 0;
}
