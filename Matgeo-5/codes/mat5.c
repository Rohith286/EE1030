#include <stdio.h>
#include <math.h>
#include <stdlib.h>

// Function declarations
double **createMat(int m, int n);
void point_gen(FILE *fptr, double **A, double **B, int no_rows, int no_cols, int num_points);
void freeMat(double **mat, int m);

// Point generation function
void point_gen(FILE *fptr, double **A, double **B, int no_rows, int no_cols, int num_points) {
    for (double i = 0; i <= num_points; i++) {
        double t = i / num_points; // Parameter t goes from 0 to 1
        double x = A[0][0] + t * (B[0][0] - A[0][0]);
        double y = A[1][0] + t * (B[1][0] - A[1][0]);
        fprintf(fptr, "%lf,%lf\n", x, y);
    }
}

// Function to generate 2D triangle with vertex B as origin
void twoDtriangle_gen(double sideAB, double sideBC, double angleABC, char filename[]) {
    double xA, yA, xB, yB, xC, yC;

    // Place B at origin (0, 0)
    xB = 0;
    yB = 0;

    // Calculating coordinates for C using sideBC and angleABC
    xA = sideAB * cos(angleABC);
    yA = sideAB * sin(angleABC);

    
    xC = sideBC;
    yC = 0;

    int m = 2, n = 1;

    // Open file for writing
    FILE *fptr = fopen(filename, "w");
    if (fptr == NULL) {
        printf("Error opening file!\n");
        return;
    }

    // Create matrices for vertices A, B, and C
    double **A = createMat(m, n);
    double **B = createMat(m, n);
    double **C = createMat(m, n);

    A[0][0] = xA;
    A[1][0] = yA;
    B[0][0] = xB;
    B[1][0] = yB;
    C[0][0] = xC;
    C[1][0] = yC;

    // Generate points along the edges of the triangle
    point_gen(fptr, A, B, m, n, 20);  // AB edge
    point_gen(fptr, B, C, m, n, 20);  // BC edge
    point_gen(fptr, C, A, m, n, 20);  // CA edge

    // Free memory
    freeMat(A, m);
    freeMat(B, m);
    freeMat(C, m);

    // Close file
    fclose(fptr);
}

int main() {
    double sideAB = 5.0;  // Given side length AB = 5 cm
    double sideBC = 6.0;  // Given side length BC = 6 cm
    double angleABC = M_PI / 3;  // Angle ABC = 60 degrees (in radians)

    // Generate the triangle with vertex B as origin and save points to file
    twoDtriangle_gen(sideAB, sideBC, angleABC, "triangle_points.dat");

    return 0;
}

// Helper function to create a matrix
double **createMat(int m, int n) {
    double **mat = (double **)malloc(m * sizeof(double *));
    for (int i = 0; i < m; i++) {
        mat[i] = (double *)malloc(n * sizeof(double));
    }
    return mat;
}

// Helper function to free a matrix
void freeMat(double **mat, int m) {
    for (int i = 0; i < m; i++) {
        free(mat[i]);
    }
    free(mat);
}
