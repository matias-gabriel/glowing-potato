class Solution(object):
    def generate_permutation(self, nums, indexes, selected, permutations):

        for idx, i in enumerate(nums):
            if idx in indexes:
                continue

            indexes.add(idx)
            selected.append(i)
            if len(selected) == len(nums):
                permutations.append(list(selected))
            else:
                self.generate_permutation(nums, indexes, list(selected),permutations)
            selected.pop()
            indexes.remove(idx)



                

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutations = []
        self.generate_permutation(nums, set([]), [], permutations)
        return permutations
        