class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # lee(t(c)o,de))
        # ))

        parenthesis_stack = []

        for idx, letter in enumerate(s):
            if letter not in [")", "("]:
                continue

            if letter == ")":
                if len(parenthesis_stack):
                    last_item = parenthesis_stack[-1][0]
                    if last_item == "(":
                        parenthesis_stack.pop()
                        continue

            parenthesis_stack.append((letter, idx))

        result = ""
        not_allowed_idx = set([i[1] for i in parenthesis_stack])

        for idx, s in enumerate(s):
            if idx in not_allowed_idx:
                continue

            result += s

        return result
