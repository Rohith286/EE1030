#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function to dynamically create a matrix
double **createMat(int rows, int cols) {
    double **matrix = (double **)malloc(rows * sizeof(double *));
    for (int i = 0; i < rows; i++) {
        matrix[i] = (double *)malloc(cols * sizeof(double));
    }
    return matrix;
}

// Function to free dynamically allocated matrix
void freeMat(double **matrix, int rows) {
    for (int i = 0; i < rows; i++) {
        free(matrix[i]);
    }
    free(matrix);
}

// Function for matrix subtraction
double **Matsub(double **a, double **b, int m, int n) {
    int i, j;
    double **c = createMat(m, n);
    for (i = 0; i < m; i++) {
        for (j = 0; j < n; j++) {
            c[i][j] = a[i][j] - b[i][j];
        }
    }
    return c;
}

// Function for matrix transpose
double **transposeMat(double **a, int m, int n) {
    int i, j;
    double **c = createMat(n, m);
    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            c[i][j] = a[j][i];
        }
    }
    return c;
}

// Function for matrix multiplication
double **Matmul(double **a, double **b, int m, int n, int p) {
    int i, j, k;
    double **c = createMat(m, p);
    double temp = 0;
    for (i = 0; i < m; i++) {
        for (k = 0; k < p; k++) {
            for (j = 0; j < n; j++) {
                temp += a[i][j] * b[j][k];
            }
            c[i][k] = temp;
            temp = 0;
        }
    }
    return c;
}

// Function to calculate the norm of a matrix
double Matnorm(double **a, int m) {
    double sum = 0;
    for (int i = 0; i < m; i++) {
        sum += a[i][0] * a[i][0];
    }
    return sqrt(sum);
}

// Main function
int main() {
    // Create matrices for points P and Q
    double **P = createMat(2, 1);
    double **Q1 = createMat(2, 1);
    double **Q2 = createMat(2, 1);

    // Initialize point P(2, -3)
    P[0][0] = 2;
    P[1][0] = -3;

    // Initialize point Q(10, y)
    Q1[0][0] = 10;
    Q2[0][0] = 10;

    // Possible values of y
    double y1 = 3;
    double y2 = -9;

    Q1[1][0] = y1;
    Q2[1][0] = y2;

    // Find difference P - Q1
    double **diff1 = Matsub(Q1, P, 2, 1);
    double **diff2 = Matsub(Q2, P, 2, 1);

    // Calculate distance norms
    double distance1 = Matnorm(diff1, 2);
    double distance2 = Matnorm(diff2, 2);

    printf("y1 = %lf", y1);
    printf("y2 = %lf", y2);
    printf("Distance between P and Q1: %.2f\n", distance1);
    printf("Distance between P and Q2: %.2f\n", distance2);

    // Free allocated memory
    freeMat(P, 2);
    freeMat(Q1, 2);
    freeMat(Q2, 2);
    freeMat(diff1, 2);
    freeMat(diff2, 2);

    return 0;
}
