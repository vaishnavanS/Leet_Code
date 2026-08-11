from itertools import permutations
class Solution(object):
    def permute(self, nums):
        a = []
        for i in permutations(nums):
            a.append(i)
        return a