import numpy as np

n = 4
addition_table = np.array([[1, 0, 3, 2],
                           [0, 1, 2, 3],
                           [3, 2, 1, 0],
                           [2, 3, 0, 1]])
multiplication_table = np.array([[1, 1, 0, 0],
                                 [1, 1, 1, 1],
                                 [0, 1, 3, 2],
                                 [0, 1, 2, 3]])

for a in range(n):
    for b in range(n):
        for c in range(n):
            print(f"{a * n ** 2 + b * n + c + 1}. Testing {a}, {b}, and {c}")
            if addition_table[addition_table[a, b], c] != addition_table[a, addition_table[b, c]]:
                print("Addition is not associative")
            if multiplication_table[multiplication_table[a, b], c] != multiplication_table[a, multiplication_table[b, c]]:
                print("Multiplication is not associative")
            if addition_table[a, multiplication_table[b, c]] != multiplication_table[addition_table[a, b], addition_table[a, c]]:
                print("Addition is not distributive over multiplication")
            if multiplication_table[a, addition_table[b, c]] != addition_table[multiplication_table[a, b], multiplication_table[a, c]]:
                print("Multiplication is not distributive over addition")
            print()
