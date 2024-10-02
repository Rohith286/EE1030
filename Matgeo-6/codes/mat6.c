#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "libs/matfun.h"
#include "libs/geofun.h"

// Function to calculate the intersection of two lines in normal form
double **line_inter(double **n1, double c1, double **n2, double c2) {
    double **intersection = createMat(2, 1);
    intersection[0][0] = -((n1[1][0] * c2 - n2[1][0] * c1) / (n1[0][0] * n2[1][0] - n2[0][0] * n1[1][0]));
    intersection[1][0] = -((n2[0][0] * c1 - n1[0][0] * c2) / (n1[0][0] * n2[1][0] - n2[0][0] * n1[1][0]));
    return intersection;
}

int main() {
    FILE *fptr;
    fptr = fopen("circle.dat", "w"); 

    if (fptr == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Normal vector for Line 1: x - y = -2 
    double **n1 = createMat(2, 1);
    n1[0][0] = 1;
    n1[1][0] = -1;
    double c1 = -2;

    // Normal vector for Line 2: 4x - 3y = 0
    double **n2 = createMat(2, 1);
    n2[0][0] = 4;
    n2[1][0] = -3;
    double c2 = 0;

    // Normal vector for Line 3: 3x - 2y = 0
    double **n3 = createMat(2, 1);
    n3[0][0] = 3;
    n3[1][0] = -2;
    double c3 = 0;

    double **P1 = line_inter(n1, c1, n2, c2); // Intersection of Line 1 and Line 2
    double **P2 = line_inter(n1, c1, n3, c3); // Intersection of Line 1 and Line 3
    double **P3 = line_inter(n2, c2, n3, c3); // Intersection of Line 2 and Line 3

    //Writing the POI in the file
    fprintf(fptr, "%lf %lf\n", P1[0][0], P1[1][0]);
    fprintf(fptr, "%lf %lf\n", P2[0][0], P2[1][0]);
    fprintf(fptr, "%lf %lf\n", P3[0][0], P3[1][0]);

    // Printing the intersection points
    printf("Intersection Points:\n");
    printf("P1 (Line 1 and Line 2): ");
    printMat(P1, 2, 1);
    printf("P2 (Line 1 and Line 3): ");
    printMat(P2, 2, 1);
    printf("P3 (Line 2 and Line 3): ");
    printMat(P3, 2, 1);

    // Free the dynamically allocated matrices
    freeMat(n1, 2);
    freeMat(n2, 2);
    freeMat(n3, 2);
    freeMat(P1, 2);
    freeMat(P2, 2);
    freeMat(P3, 2);

    fclose(fptr); 
    return 0;
}
