class Solution(object):
    def flipAndInvertImage(self, image):
        res = []
        for i in image:
            i.reverse()
            for x in range(len(i)):
                i[x] = 1  - i[x]
            res.append(i)
        return res
        