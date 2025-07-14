class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
      # table n * m where n = len(text1), m = len(text2)
      # sub problem lcs(n, m) = max( lcs(n - 1, m), lcs(n, m-1 ), lcs(n-1, m-1)
      # xyzabcdez
      # xyzabcdet
      # example
      # table = [
      0, 0 , 0 , 0,
      0, 0 , 0 , 0
      0, 0 , 0 , 0
      matrix = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)] 

      for i in range(1,len(text1) + 1):
        for j in range(1,len(text2) + 1):
          if text1[i-1] == text2[j-1]:
            matrix[i][j] = matrix[i-1][j-1] + 1
          else:
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])


      return matrix[len(text1)][len(text2)]
