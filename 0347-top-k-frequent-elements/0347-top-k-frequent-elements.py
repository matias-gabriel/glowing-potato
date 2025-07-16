class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        
        for n in nums:
            if n not in frequency:
                frequency[n] = 1
            else:
                frequency[n]= frequency[n] + 1

        result = []

        for key in frequency.keys():
            result.append((frequency[key], key))

        result.sort()

        return [ i[1] for i in result[(-1*k):]]