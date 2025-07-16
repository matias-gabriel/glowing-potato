class Solution:
    # r(idx, result, memo)
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)

        def r(idx, current, result, memo):
            if idx == len(s):
                result.append(" ".join(current))
            if idx > len(s):
                return

            for j in range(idx, len(s)):
                word = s[idx : j + 1]
                if word in word_set:
                    current.append(word)
                    r(j + 1, current, result, memo)
                    current.pop()

        result = []

        r(0, [], result, {})

        return result
