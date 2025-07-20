class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_dict = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }

        def r(idx, s, results):
            if idx == len(digits):
                results.append(s)
                return

            d = int(digits[idx])

            for w in phone_dict[d]:
                r(idx + 1, s + w, results)

        if not digits:
            return []

        results = []

        r(0, "", results)

        return results
