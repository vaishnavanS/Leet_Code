class Solution(object):
    def fib(self, n):
        a,b = 0,1
        c = 0
        for i in range(n):
            c = a+b
            a = b
            b = c
        return a
        