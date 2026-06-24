class Solution(object):
    def checkInclusion(self, s1, s2):
        s1 = ''.join(sorted(s1))
        a = False
        for i in range(len(s2)-len(s1)+1):
            c_w = s2[i:i+len(s1)]
            if ''.join(sorted(c_w)) == s1:
                a = True
                break
        return a