import numpy as np
def roots(*coeffs):
    print(coeffs)
    matrix = np.eye(len(coeffs) - 1, k=-1)
    print(matrix)
    matrix[:,-1] = np.array(coeffs[:0:-1]) / -coeffs[0]
    return np.linalg.eigvals(matrix)

print(roots(1, 2, 1))