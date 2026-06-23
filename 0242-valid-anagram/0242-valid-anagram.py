class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st = ''.join(sorted(s))
        ts = ''.join(sorted(t))
        return st==ts