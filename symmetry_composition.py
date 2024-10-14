import numpy as np


def compute_symmetry_composition(symmetries):
    vertices = np.linspace(1, len(symmetries[0]), len(symmetries[0]), dtype=int)
    for symmetry in symmetries:
        new_object = np.zeros(len(vertices), dtype=int)
        for i in range(len(vertices)):
            new_object[symmetry[i] - 1] = vertices[i]
        vertices = new_object
    return vertices


if __name__ == "__main__":
    print(f"Investigation 18 Introduction: {compute_symmetry_composition([[4, 3, 2, 1], [4, 3, 2, 1], [4, 3, 2, 1]])}")
    print(f"Activity 18.3 (a): (bc)^2: {compute_symmetry_composition([[4, 3, 2, 1], [2, 3, 4, 1], [4, 3, 2, 1], [2, 3, 4, 1]])}")
    print(f"Activity 18.3 (a): b^2c^2: {compute_symmetry_composition([[4, 3, 2, 1], [4, 3, 2, 1], [2, 3, 4, 1], [2, 3, 4, 1]])}")
    print(f"Activity 18.3 (b): (ab)^2: {compute_symmetry_composition([[3, 4, 1, 2], [4, 3, 2, 1], [3, 4, 1, 2], [4, 3, 2, 1]])}")
    print(f"Activity 18.3 (b): a^2b^2: {compute_symmetry_composition([[3, 4, 1, 2], [3, 4, 1, 2], [4, 3, 2, 1], [4, 3, 2, 1]])}")
