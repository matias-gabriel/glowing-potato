class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        visited = set([])
        result = 0
        partial = 0

        for num in values:
            if num in visited:
                continue

            current = num
            while True:
                visited.add(current)
                partial += 1
                if current + 1 in values:
                    current = current + 1
                else:
                    result = max(partial, result)
                    partial = 0
                    break

        return result
