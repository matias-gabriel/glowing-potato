class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash_s1 = {}
        hash_s2 = {}

        for i in s1:
            if i not in hash_s1:
                hash_s1[i] = 0

            hash_s1[i] = hash_s1[i] + 1

        n_s1 = len(s1)
        n_s2 = len(s2)

        for i in range(n_s2 - n_s1 + 1):
            if i == 0:
                for j in s2[0:n_s1]:
                    if j not in hash_s2:
                        hash_s2[j] = 0
                    hash_s2[j] = hash_s2[j] + 1
            else:
                hash_s2[s2[i - 1]] = hash_s2[s2[i - 1]] - 1
                if hash_s2[s2[i - 1]] == 0:
                    del hash_s2[s2[i - 1]]
                j = i + n_s1 - 1
                if s2[j] not in hash_s2:
                    hash_s2[s2[j]] = 0
                hash_s2[s2[j]] = hash_s2[s2[j]] + 1
            if hash_s2 == hash_s1:
                return True

        return False
