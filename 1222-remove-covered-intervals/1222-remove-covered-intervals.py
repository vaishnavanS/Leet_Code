class Solution(object):
    def removeCoveredIntervals(self, l):
        l.sort()
        x,y = l[0]
        c = 1
        for i in range(1,len(l)):
            a,b = l[i][0],l[i][1]
            if b<=y:
                continue
            if a == x:
                y = b
                continue
            c += 1
            x,y = a,b
        return c