# import numpy as np
# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """

#         matrix = np.transpose(matrix)

#         matrix = matrix.tolist()


#         for i in range(len(matrix)):
#             matrix[i] = matrix[i][::-1]

#         print(matrix)

#         return matrix


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        # transpose - rows become cols cols become rows
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]

        print(matrix)

        return matrix
