from collections import deque


class Solution(object):
    # min(i, j) = min( min(i-1, j), min(i+1, j), min(i, j-1) , min(i, j+1))
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """

        new_matrix = [[float("inf")] * len(i) for i in mat]

        queue = deque([])

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    new_matrix[i][j] = 0

        while queue:
            current = queue.popleft()
            i, j = current
            value = new_matrix[i][j]
            positions = [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]

            for position in positions:
                p_i, p_j = position
                if p_i >= 0 and p_i < len(mat) and p_j >= 0 and p_j < len(mat[0]):
                    if value + 1 <= new_matrix[p_i][p_j]:
                        new_matrix[p_i][p_j] = value + 1
                        queue.append((p_i, p_j))

        return new_matrix

        return mat
