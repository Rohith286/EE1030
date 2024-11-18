import math

def matInput(size):
    try:
        mat = []
        for i in range(size):
            row = []
            for j in range(size):
                real = float(input(f"Element [{i + 1}][{j + 1}] : "))
                row.append(complex(real, 0))
            mat.append(row)
        return mat
    except ValueError:
        print("Invalid input! Please enter numeric values only.")
        raise

def matMul(A, B, size):
    result = []
    for i in range(size):
        row = []
        for j in range(size):
            total = 0
            for k in range(size):
                total += A[i][k] * B[k][j]
            row.append(total)
        result.append(row)
    return result
    
def householder_redn(vec): # householder reduction
    size = len(vec)
    norm = math.sqrt(sum(abs(x) ** 2 for x in vec))
    if norm < 1e-10:
        idMat = [] # identity matrix
        for i in range(size):
            row = []
            for j in range(size):
                if i == j:
                    row.append(1)
                else:
                    row.append(0)
            idMat.append(row)
        return idMat
    e1 = [] # building e1
    for i in range(size):
        if i == 0:
            e1.append(1)
        else:
            e1.append(0)
    sign = -1 if vec[0].real >= 0 else 1
    v = []
    for i in range(size):
        v.append(vec[i] + sign*norm*e1[i])
    norm_v = math.sqrt(sum(abs(x) ** 2 for x in v))
    if norm_v < 1e-10: # if vec is effectively zero => no need to take the reflection
        idMat = []
        for i in range(size):
            row = []
            for j in range(size):
                if i == j:
                    row.append(1)
                else:
                    row.append(0)
            idMat.append(row)
        return idMat
    for i in range(size):
        v[i] /= norm_v
    H = []
    for i in range(size):
        row = []
        for j in range(size):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        H.append(row)
    for i in range(size):
        for j in range(size):
            H[i][j] -= 2 * v[i] * v[j].conjugate()
    return H

def qrd(A, size): # A = QR
    Q = []
    for i in range(size):
        row = []
        for j in range(size):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        Q.append(row)
    R = [row[:] for row in A]
    for k in range(size - 1):
        x = []
        for i in range(k, size):
            x.append(R[i][k])
        partial_H_k = householder_redn(x)
        H_k = [] # making H_k from partial_H_k
        for i in range(size):
            row = []
            for j in range(size):
                if i == j:
                    row.append(1)
                else:
                    row.append(0)
            H_k.append(row)
        for i in range(k, size):
            for j in range(k, size):
                H_k[i][j] = partial_H_k[i - k][j - k]
        R = matMul(H_k, R, size)
        Q = matMul(Q, H_k, size)
    return Q, R

def Evalues(A, size):
    tol = 1e-9
    max_iter = 100
    curr_A = [row[:] for row in A]
    for _ in range(max_iter):
        Q, R = qrd(curr_A, size)
        new_A = matMul(R, Q, size)
        diff = 0
        for i in range(size):
            for j in range(size):
                diff += abs(new_A[i][j] - curr_A[i][j])
        curr_A = new_A
        if diff < tol:
            break
    print("\nEigenvalues:")
    for i in range(size):
        eigval = curr_A[i][i] # printing the diagonal entries
        if abs(eigval.imag) < tol:
            print(f"Eigenvalue {i + 1} = {eigval.real:.6f}")

def main():
    try:
        size = int(input("Enter the size of the matrix (n x n): "))
        if size <= 0:
            print("Matrix size must be a positive integer.")
            return
        print("\nEnter the elements of the matrix (real entries only):")
        A = matInput(size)
        Evalues(A, size)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
