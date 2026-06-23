class Solution(object):
    def isPalindrome(self, s):
        n = []
        for i in s:
            if i.isalnum():
                n.append(i.lower())
        return n == n[::-1]
        