class Solution(object):
    def checkIsPermutation(self, n, m):
        # O(n/s1)
        letters_m = {}
        letters_n = {}

        for letter in n:
            if letter in letters_n:
                letters_n[letter] = letters_n[letter] + 1
            else: 
                letters_n[letter]=0

        for letter in m:
            if letter in letters_m:
                letters_m[letter] = letters_m[letter] + 1
            else:
                letters_m[letter]=0


        return letters_m == letters_n

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        s1_len = len(s1)
        s2_len = len(s2)

        
        # O(s2*s1)
        for i, item in enumerate(s2):
            if i + s1_len > s2_len:
                return False

            s2_slice = s2[i:i+s1_len]

            if self.checkIsPermutation(s1,s2_slice):
                print(s2_slice, s1)
                return True
        
        return False

            
        