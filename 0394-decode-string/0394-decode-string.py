class Solution:
    def decodeString(self, s: str) -> str:
        brackets_stack = []
        idx = 0
        while idx < len(s):
            letter = s[idx]
            if letter.isnumeric():
                n = ""
                while letter.isnumeric():
                    n = n + letter
                    idx += 1
                    letter = s[idx]
                brackets_stack.append(n)
                continue
            elif letter != "]":
                brackets_stack.append(letter)
            else:
                inner_letters = []
                while "[" != brackets_stack[-1]:
                    inner_letter = brackets_stack.pop()
                    inner_letters.append(inner_letter)

                poped = brackets_stack.pop()
                inner_letters.reverse()
                value = int(brackets_stack.pop())

                new_s = list(value * inner_letters)

                brackets_stack = brackets_stack + new_s
            idx += 1

        return "".join(brackets_stack)
