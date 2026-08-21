class Solution(object):
    def findRepeatedDnaSequences(self, s):
        d = {}
        a = []
        for i in range(len(s)-10+1):
            b = s[i:i+10]
            if b in d:
                d[b] += 1
            else:
                d[b] = 1
        for i,j in d.items():
            if j>=2:
                a.append(i)
        return a
        