#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function prototypes (already provided by you)
double **createMat(int m, int n);
void printMat(double **p, int m, int n);
double **Matadd(double **a, double **b, int m, int n);
double **Matsub(double **a, double **b, int m, int n);
double **Matscale(double **a, int m, int n, double k);
double **Matunit(double **a, int m);
double Matnorm(double **a, int m);


int main() {
    // Define vector a = [1, 1, 2]^T
    double **a = createMat(3, 1);
    a[0][0] = 1.0; // i component
    a[1][0] = 1.0; // j component
    a[2][0] = 2.0; // k component

    // Define vector b = [2, 1, -2]^T
    double **b = createMat(3, 1);
    b[0][0] = 2.0; // i component
    b[1][0] = 1.0; // j component
    b[2][0] = -2.0; // k component

    // Part (a):  6a
    double **scaled_a = Matscale(a, 3, 1, 6.0);  // Scale vector a by 6
    double **unit_scaled_a = Matunit(scaled_a, 3); // Find the unit vector
    printf("Unit vector in the direction of 6a:\n");
    printMat(unit_scaled_a, 3, 1);

    // Part (b):  2a - b
    double **scaled_two_a = Matscale(a, 3, 1, 2.0);  // Scale vector a by 2
    double **two_a_minus_b = Matsub(scaled_two_a, b, 3, 1); // Subtract b from 2a
    double **unit_two_a_minus_b = Matunit(two_a_minus_b, 3); // Find the unit vector
    printf("Unit vector in the direction of 2a - b:\n");
    printMat(unit_two_a_minus_b, 3, 1);

    // Free dynamically allocated memory
    free(a);
    free(b);
    free(scaled_a);
    free(unit_scaled_a);
    free(scaled_two_a);
    free(two_a_minus_b);
    free(unit_two_a_minus_b);

    return 0;
}

// Create a matrix
double **createMat(int m, int n) {
    double **a = (double **)malloc(m * sizeof(double *));
    for (int i = 0; i < m; i++) {
        a[i] = (double *)malloc(n * sizeof(double));
    }
    return a;
}

// Print a matrix
void printMat(double **p, int m, int n) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            printf("%lf ", p[i][j]);
        }
        printf("\n");
    }
}

// Add matrices
double **Matadd(double **a, double **b, int m, int n) {
    double **c = createMat(m, n);
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            c[i][j] = a[i][j] + b[i][j];
        }
    }
    return c;
}

// Subtract matrices
double **Matsub(double **a, double **b, int m, int n) {
    double **c = createMat(m, n);
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            c[i][j] = a[i][j] - b[i][j];
        }
    }
    return c;
}

// Scale matrix
double **Matscale(double **a, int m, int n, double k) {
    double **c = createMat(m, n);
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            c[i][j] = k * a[i][j];
        }
    }
    return c;
}

// Compute the norm of a vector
double Matnorm(double **a, int m) {
    double sum = 0.0;
    for (int i = 0; i < m; i++) {
        sum += a[i][0] * a[i][0];
    }
    return sqrt(sum);
}

// Compute the unit vector
double **Matunit(double **a, int m) {
    double **c = createMat(m, 1);
    double norm = Matnorm(a, m);
    for (int i = 0; i < m; i++) {
        c[i][0] = a[i][0] / norm;
    }
    return c;
}
