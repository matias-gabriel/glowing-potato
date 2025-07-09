class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences_set = set([])
        repeated = set([])
        sub_sequence = None
        for i in range(0, len(s) + 1 - 10):
            if sub_sequence == None:
                sub_sequence = s[i : i + 10]
            else:
                sub_sequence = sub_sequence[1:] + s[i - 1 + 10]
            if sub_sequence in sequences_set:
                repeated.add(sub_sequence)
            else:
                sequences_set.add(sub_sequence)

        return list(repeated)
