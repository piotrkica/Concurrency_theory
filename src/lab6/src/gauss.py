import threading
import numpy as np


def task_A(matrix, A_array, i, k):
    """
    Thread function responsible for "A" operation (finding multiplication factor)
    :param matrix: processed matrix
    :param A_array: array to store factors
    :param i: index of row on diagonal
    :param k: index of row below diagonal
    """
    A_array[k] = matrix[k, i] / matrix[i, i]


def task_B(matrix, A_array, B_array, i, k, j):
    """
    Thread function responsible for "B" operation (factor and matrix element multiplication)
    :param matrix: processed matrix
    :param A_array: array of precalculated factors
    :param B_array: array to store multiplication results
    :param i: index of row on diagonal
    :param k: index of row below diagonal
    :param j: index of column
    """
    B_array[j] = A_array[k] * matrix[i][j]


def task_C(matrix, B_array, k, j):
    """
    Thread function responsible for "C" operation (matrix element subtracted with factor*element)
    :param matrix: processed matrix
    :param B_array: array of precalculated elements to subtract with
    :param k: index of row below diagonal
    :param j: index of column
    """
    matrix[k][j] -= B_array[j]


def parallel_gauss(matrix) -> np.ndarray:
    """
    Main function to do gaussian elimination using threads. For educational purpose on Trace Theory course.
    :param matrix: matrix to process
    :return: solved matrix with gaussian elimination, requires backwards_solving function for end result
    """
    n = len(matrix)
    for i in range(0, n - 1):
        for k in range(i + 1, n):
            A_tasks = []
            A_array = np.zeros(n)
            for j in range(i + 1, n):
                A_tasks.append(threading.Thread(target=task_A, args=(matrix, A_array, i, k)))
            for a_task in A_tasks:
                a_task.start()
            for a_task in A_tasks:
                a_task.join()

            B_tasks = []
            B_array = np.zeros(n + 1)
            for j in range(i, n + 1):
                B_tasks.append(threading.Thread(target=task_B, args=(matrix, A_array, B_array, i, k, j)))
            for b_task in B_tasks:
                b_task.start()
            for b_task in B_tasks:
                b_task.join()

            C_tasks = []
            for j in range(i, n + 1):
                C_tasks.append(threading.Thread(target=task_C, args=(matrix, B_array, k, j)))
            for c_task in C_tasks:
                c_task.start()
            for c_task in C_tasks:
                c_task.join()
    return matrix


def backwards_solving(matrix: np.ndarray) -> np.ndarray:
    """
    Function to finish solving gaussian elimination - ones on main diagonal as only values
    :param matrix: matrix solved with gaussian elimination
    :return: solved and rounded matrix
    """
    n = len(matrix)
    rhs = matrix[:, -1]
    solved_rhs = np.zeros_like(rhs)

    solved_rhs[n - 1] = rhs[n - 1] / matrix[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        sum_other = 0
        for j in range(i + 1, n):
            sum_other += matrix[i, j] * solved_rhs[j]
        solved_rhs[i] = (rhs[i] - sum_other) / matrix[i, i]

    return np.append(np.eye(n), solved_rhs.reshape(n, 1), axis=1)
