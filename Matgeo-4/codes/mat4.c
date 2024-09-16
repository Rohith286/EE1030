#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function declarations
double **Matadd(double **a, double **b, int m, int n);
double **Matsub(double **a, double **b, int m, int n);
double **Matscale(double **a, int m, int n, double k);
double **Matunit(double **a, int m);
double **createMat(int m, int n);
void printMat(double **p, int m, int n);
void freeMat(double **a, int m);
double Matnorm(double **a, int m);

// Function for creating a matrix of size m x n
double **createMat(int m, int n) {
    double **a = (double **)malloc(m * sizeof(double *));
    for (int i = 0; i < m; i++) {
        a[i] = (double *)malloc(n * sizeof(double));
    }
    return a;
}

// Function to free the memory of a matrix
void freeMat(double **a, int m) {
    for (int i = 0; i < m; i++) {
        free(a[i]);
    }
    free(a);
}

// Function for matrix addition
double **Matadd(double **a, double **b, int m, int n) {
    double **c = createMat(m, n);
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            c[i][j] = a[i][j] + b[i][j];
        }
    }
    return c;
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

// Function for scaling a matrix by a constant k
double **Matscale(double **a, int m, int n, double k) {
    double **c = createMat(m, n);
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            c[i][j] = k * a[i][j];
        }
    }
    return c;
}

// Function for printing a matrix
void printMat(double **p, int m, int n) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            printf("%lf ", p[i][j]);
        }
        printf("\n");
    }
}

// Function to calculate the norm (magnitude) of a vector (matrix of size m x 1)
double Matnorm(double **a, int m) {
    double sum = 0;
    for (int i = 0; i < m; i++) {
        sum += a[i][0] * a[i][0];
    }
    return sqrt(sum);
}

// Function to find the unit vector of a vector a
double **Matunit(double **a, int m) {
    double norm = Matnorm(a, m);
    double **c = createMat(m, 1);
    for (int i = 0; i < m; i++) {
        c[i][0] = a[i][0] / norm;
    }
    return c;
}

// Main function to calculate the required vectors and print results
int main() {
    // Define vectors a and b as 3x1 matrices (i, j, k components)
    double **a = createMat(3, 1);
    double **b = createMat(3, 1);

    // Assign values to vector a: [1, 1, 2] (i, j, k components)
    a[0][0] = 1;
    a[1][0] = 1;
    a[2][0] = 2;

    // Assign values to vector b: [2, 1, -2] (i, j, k components)
    b[0][0] = 2;
    b[1][0] = 1;
    b[2][0] = -2;

    // 1. Calculate unit vector for 6a
    double **scaled_a = Matscale(a, 3, 1, 6);  // Scale a by 6
    double **unit_6a = Matunit(scaled_a, 3);   // Find unit vector

    // Print result for 6a
    printf("Unit vector in the direction of 6a:\n");
    printMat(unit_6a, 3, 1);

    // 2. Calculate unit vector for 2a - b
    double **scaled_2a = Matscale(a, 3, 1, 2); // Scale a by 2
    double **sub_ab = Matsub(scaled_2a, b, 3, 1);  // 2a - b
    double **unit_ab = Matunit(sub_ab, 3);  // Find unit vector

    // Print result for 2a - b
    printf("Unit vector in the direction of 2a - b:\n");
    printMat(unit_ab, 3, 1);

    // Free allocated memory
    freeMat(a, 3);
    freeMat(b, 3);
    freeMat(scaled_a, 3);
    freeMat(unit_6a, 3);
    freeMat(scaled_2a, 3);
    freeMat(sub_ab, 3);
    freeMat(unit_ab, 3);

    return 0;
}
