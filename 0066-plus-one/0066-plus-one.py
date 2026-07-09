class Solution(object):
    def plusOne(self, digits):
        b = ""
        for i in digits:
            b += str(i)
        c = int(b)
        c += 1
        d = str(c)
        e = []
        for i in d:
            if i.isdigit():
                e.append(int(i))
        return e