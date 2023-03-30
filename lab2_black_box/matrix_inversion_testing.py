import random
import numpy as np


def generate_random_matrix(n: int) -> [[float]]:
    matrix = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            matrix[i][j] = round(random.uniform(-50.00, 50.00), 2)
    return matrix


def generate_dia_matrix(n: int) -> [[float]]:
    matrix = np.zeros((n, n), dtype=float)
    for i in range(n):
        matrix[i][i] = round(random.uniform(-50.00, 50.00), 2)
    return matrix


print(generate_dia_matrix(2))


def assert_result(A: np.ndarray, A_inversion: np.ndarray):
    assert A is not None
    assert A.shape == A_inversion.shape
    product = np.matmul(A, A_inversion)
    identity = np.identity(A.shape[0])
    print(product)
    print(identity)
    return np.allclose(product, identity)


# m = generate_dia_matrix(2)
# m_inverse = np.linalg.inv(m)
# print(assert_result(m, m_inverse))


def run_tests(nr_test: int = 100):
    for i in range(nr_test):
        m = generate_random_matrix(random.randint(2, 100))
        m_inverse = np.linalg.inv(m)
        print(assert_result(m, m_inverse))

run_tests(2)
# print(assert_res(np.matrix([[1.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 3.0]]),
#                  np.matrix([[1.0, 0.0, 0.0], [0.0, 1 / 2, 0.0], [0.0, 0.0, 1 / 3]])))
