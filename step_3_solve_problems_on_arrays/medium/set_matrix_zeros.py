#https://leetcode.com/problems/set-matrix-zeroes/description/

from typing import List

def setZeroes(matrix: List[List[int]]) -> None:
    """
    Modify the matrix in-place to set entire rows and columns to zero if an element is zero.
    """
    row = len(matrix)
    col = len(matrix[0])

    zero_rows = set()
    zero_cols = set()

    # Identify all rows and columns that contain a zero
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    # Set identified rows to zero
    for r in zero_rows:
        for j in range(col):
            matrix[r][j] = 0

    # Set identified columns to zero
    for c in zero_cols:
        for i in range(row):
            matrix[i][c] = 0

if __name__ == "__main__":
    # Example matrix
    mat = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 8, 9]
    ]
    setZeroes(mat)
    print("Processed Matrix:")
    for row in mat:
        print(row)
