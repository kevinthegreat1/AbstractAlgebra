import sys
import numpy as np

def multiplication_table(n):
    """
    This function generates a multiplication table for Z_n, the number system of integers modulo n.
    """
    table = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            table[i, j] = (i * j) % n
    return table

if __name__ == '__main__':
    np.set_printoptions(threshold=sys.maxsize, linewidth=sys.maxsize)
    print(multiplication_table(6))
    print(multiplication_table(8))
    print(multiplication_table(145))
    print(multiplication_table(475))
