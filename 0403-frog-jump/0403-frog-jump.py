class Solution(object):
    # 0  -> 1 k
    # 1 -> (1, 2)
    def cross(self, current_k, current_stone, last_tone ,stones, memo):
        if last_tone == current_stone:
            return True

        memo_a = memo.get((current_stone, current_stone + current_k + 1), None)
        memo_b = memo.get((current_stone, current_stone + current_k), None)
        memo_c = memo.get((current_stone, current_stone + current_k - 1), None)

        if memo_a or memo_b or memo_c:
            return True

        result_a = False
        result_b = False
        result_c = False

        if current_k >= 0 and memo_a is None:
            if (current_stone + current_k + 1 in stones):
                result_a = self.cross(current_k + 1, current_stone + current_k + 1, last_tone ,stones, memo)
                memo[(current_stone, current_stone + current_k + 1)] = result_a 
        if current_k >=1 and memo_b is None:
            if (current_stone + current_k in stones):
                result_b = self.cross(current_k, current_stone + current_k, last_tone ,stones, memo)
                memo[(current_stone, current_stone + current_k)] =  result_b
        if current_k >=2 and memo_c is None:
            if (current_stone + current_k - 1 in stones):
                result_c = self.cross(current_k - 1, current_stone + current_k - 1, last_tone ,stones, memo)
                memo[(current_stone, current_stone + current_k - 1)] = result_c

        result = result_a or result_b or result_c

        return result

    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        memo = {}
        res = self.cross(0,stones[0],stones[-1], set(stones), memo)
        return res

        
        