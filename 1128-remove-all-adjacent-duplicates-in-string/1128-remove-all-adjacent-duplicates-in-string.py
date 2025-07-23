class Solution:
    def removeDuplicates(self, s: str) -> str:
        word_stack = []
        for letter in s:
            is_removed = False
            while len(word_stack) and word_stack[-1] == letter:
                is_removed = True
                word_stack.pop()

            if not is_removed:
                word_stack.append(letter)

        return ''.join(word_stack)
        