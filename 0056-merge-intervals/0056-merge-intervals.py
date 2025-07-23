class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()

        if len(intervals) == 0:
            return []
        if len(intervals) == 1:
            return intervals

        prev = intervals[0]
        results = []
        for i in range(1, len(intervals)):
            if prev[1] >= intervals[i][0]:
                if intervals[i][1] < prev[1]:
                    continue
                else:
                    prev[1] = intervals[i][1]
            else:
                results.append(prev)
                prev = [intervals[i][0], intervals[i][1]]

        if not len(results) or results[-1] != prev:
            results.append(prev)

        return results
