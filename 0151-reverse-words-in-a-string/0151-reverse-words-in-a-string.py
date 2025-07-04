def swap(i, j, word):
    aux = word[i]
    word[i] = word[j]
    word[j] = aux

class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.strip().split()

        left = 0
        right = len(word) - 1

        while left < right:
            swap(left, right, word)
            left+=1
            right-=1

        return " ".join(word)

        