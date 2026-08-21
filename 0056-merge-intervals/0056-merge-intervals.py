class Solution(object):
    def merge(self, l):
        l.sort()
        k = []
        a,b = l[0]
        for i in range(1,len(l)):
            c,d = l[i]
            if b>=c:
                b = max(b,d)
            else:
                k.append([a,b])
                a,b = c,d
        k.append([a,b])
        return k        