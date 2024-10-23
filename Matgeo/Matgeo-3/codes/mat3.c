#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function declarations
double **createMat(int m, int n);
double **Matsub(double **a, double **b, int m, int n);
double Matnorm(double **a, int m);
void printMat(double **p, int m, int n);
void freeMat(double **matrix, int rows);

// Main function
int main() {
    // Declare variables for a, b, x, y
    double a = 3; // Arbitrary value for a
    double b = 4; // Arbitrary value for b
    double x, y;

    // Matrices for points P(x, y), A(a + b, b - a), B(a - b, a + b)
    double **P = createMat(2, 1);
    double **A = createMat(2, 1);
    double **B = createMat(2, 1);

    // Initialize points A(a + b, b - a) and B(a - b, a + b)
    A[0][0] = a + b;
    A[1][0] = b - a;

    B[0][0] = a - b;
    B[1][0] = a + b;

    // Loop to calculate the locus of points satisfying bx = ay
    for (x = -10; x <= 10; x += 1) {
        y = (b * x) / a;  // From bx = ay, y = (b * x) / a

        // Set point P(x, y)
        P[0][0] = x;
        P[1][0] = y;

        // Find the distance from P to A and P to B
        double **PA_diff = Matsub(P, A, 2, 1);
        double **PB_diff = Matsub(P, B, 2, 1);

        double dist_PA = Matnorm(PA_diff, 2);
        double dist_PB = Matnorm(PB_diff, 2);

        // Print the results
        printf("P(%.2f, %.2f): dist(PA) = %.2f, dist(PB) = %.2f\n", x, y, dist_PA, dist_PB);

        // Check if P is equidistant from A and B
        if (fabs(dist_PA - dist_PB) < 1e-6) {
            printf("P(%.2f, %.2f) is equidistant from A and B.\n", x, y);
        }

        // Free allocated memory for differences
        freeMat(PA_diff, 2);
        freeMat(PB_diff, 2);
    }

    // Free allocated memory
    freeMat(P, 2);
    freeMat(A, 2);
    freeMat(B, 2);

    return 0;
}

// Function to create a matrix
double **createMat(int m, int n) {
    double **matrix = (double **)malloc(m * sizeof(double *));
    for (int i = 0; i < m; i++) {
        matrix[i] = (double *)malloc(n * sizeof(double));
    }
    return matrix;
}

// Function to free a matrix
void freeMat(double **matrix, int rows) {
    for (int i = 0; i < rows; i++) {
        free(matrix[i]);
    }
    free(matrix);
}

// Function for matrix subtraction
double **Matsub(double **a, double **b, int m, int n) {
    double **c = createMat(m, n);
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            c[i][j] = a[i][j] - b[i][j];
        }
    }
    return c;
}

// Function to calculate the norm (Euclidean distance)
double Matnorm(double **a, int m) {
    double sum = 0;
    for (int i = 0; i < m; i++) {
        sum += a[i][0] * a[i][0];
    }
    return sqrt(sum);
}

// Function to print a matrix
void printMat(double **p, int m, int n) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            printf("%lf ", p[i][j]);
        }
        printf("\n");
    }
}
