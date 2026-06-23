class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        c = 0
        for i in str(stones):
            for j in str(jewels):
                if i == j:
                    c+=1
        return c