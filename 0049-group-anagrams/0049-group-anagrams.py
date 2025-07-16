class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for w in strs:
            s_w = ''.join(sorted(w))
            if s_w in anagrams:
                anagrams[s_w].append(w)
            else:
                anagrams[s_w] = [w]

        
        result = []
        for k in anagrams.keys():
            result.append(anagrams[k])
        
        return result

        