class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        s1_len = len(s1)
        s2_len = len(s2)
        sorted_s1 = sorted(s1)

        for i, item in enumerate(s2):
            if i + s1_len > s2_len:
                return False

            sorted_s2_slice = sorted(s2[i:i+s1_len])

            if sorted_s2_slice == sorted_s1:
                return True
        
        return False

            
        