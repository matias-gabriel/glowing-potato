class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        text1 = list(s)
        text2 = list(s)
        text2.reverse()
        matrix = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)] 

        for i in range(1,len(text1) + 1):
            for j in range(1,len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    matrix[i][j] = matrix[i-1][j-1] + 1
                else:
                    matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])


        return matrix[len(text1)][len(text2)]
