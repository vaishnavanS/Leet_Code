class Solution(object):
    def hammingWeight(self, n):
        c = 0
        a = str(bin(n)[2:])
        for z in a:
            if z == '1':
                c += 1
        return c
            