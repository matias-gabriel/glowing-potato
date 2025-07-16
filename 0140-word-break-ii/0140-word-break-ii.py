class Solution:
    # r(idx, result, memo)
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        def r(idx, memo):
            if idx == len(s):
                return [""]
            if idx > len(s):
                return []
            if idx in memo:
                return memo[idx]


            results = []
            for j in range(idx, len(s)):
                word = s[idx:j+1]
                if word in word_set:
                    for w in r(j+1,memo):
                        results.append(f"{word} {w}".strip())

            memo[idx] = results

            return results

        return r(0, {})


                

        