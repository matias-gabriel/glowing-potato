class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences_set = set([])
        repeated = set([])

        for i in range(len(s) + 1 - 10):
            sub_sequence = s[i : i + 10]
            if sub_sequence in sequences_set:
                repeated.add(sub_sequence)
            else:
                sequences_set.add(sub_sequence)

        return list(repeated)
