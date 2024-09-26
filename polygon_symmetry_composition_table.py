import numpy as np


def polygon_symmetry_composition_table(n):
    """
    This function generates the symmetry composition table for an n-sided regular polygon.

    :param n: the number of sides of the regular polygon
    :return:
    """
    symmetries = np.zeros((2 * n, n), dtype=int)
    for i in range(2 * n):
        for j in range(n):
            # Calculate the result of applying the i-th symmetry to the j-th point of the polygon.
            # Subtract 1 to convert the result to 0-based indexing.
            symmetries[i, j] = apply_symmetry(i, j + 1, n) - 1
    composition_table = np.zeros((2 * n, 2 * n), dtype=int)
    for i in range(2 * n):
        for j in range(2 * n):
            result = np.zeros(n, dtype=int)
            for k in range(n):
                # Apply the i-th symmetry composed with the j-th symmetry to the k-th point of the polygon.
                result[k] = symmetries[i, symmetries[j, k]]
            # Find the index of the symmetry in the list of symmetries.
            # The `all` function is used to compare the arrays (consisting of each point of the polygon) element-wise.
            composition_table[i, j] = np.where(np.all(symmetries == result, axis=1))[0][0]
    return composition_table


def apply_symmetry(symmetry, point, n):
    """
    This function applies a symmetry to a point of an n-sided regular polygon.

    :param symmetry: the 0-based index of the symmetry to apply
    :param point: the 1-based index of the point to apply the symmetry to
    :param n: the number of sides of the regular polygon
    :return: the 1-based index of the point after applying the symmetry
    """
    if symmetry == 0:
        return point
    elif symmetry <= n:
        # reflection
        if n % 2 == 0 and symmetry > n / 2:
            # Reflect the polygon along the line of symmetry through the midpoint between the point and the next point if the symmetry is more than half of n.
            # (point - (2 * (point - (symmetry - n / 2)) - 1) + n - 1) % n + 1
            return (-point + 2 * symmetry) % n + 1
        else:
            # Reflect the polygon along the line of symmetry through the point if n is odd or the symmetry is less than or equals to half of n.
            # (point - (2 * (point - symmetry)) + n - 1) % n + 1
            return (-point + 2 * symmetry + n - 1) % n + 1
    else:
        # Rotate the polygon by `symmetry - n` steps counterclockwise.
        return (point + symmetry - 1) % n + 1


if __name__ == "__main__":
    print(polygon_symmetry_composition_table(3))
    print(polygon_symmetry_composition_table(4))
    print(polygon_symmetry_composition_table(5))
    print(polygon_symmetry_composition_table(6))
