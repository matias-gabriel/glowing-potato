class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)

        def r(idx, current, path, result):
            if idx >= n:
                return
            if current > target:
                return
            if current == target:
                print(current)
                result.append(path[:])

            # r(idx, current) = r(idx+1, current + cand), r(idx, current+cand)
            for i in range(idx, n):
                path.append(candidates[i])
                r(i, current + candidates[i], path, result)
                path.pop()

        result = []
        r(0, 0, [], result)
        return result
