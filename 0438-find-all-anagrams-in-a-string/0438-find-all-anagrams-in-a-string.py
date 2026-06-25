class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []
        ans = []
        pcount = [0] * 26
        scount = [0] * 26
        for ch in p:
            pcount[ord(ch) - ord('a')] += 1
        for ch in s[:len(p)]:
            scount[ord(ch) - ord('a')] += 1
        if scount == pcount:
            ans.append(0)
        for i in range(len(p), len(s)):
            scount[ord(s[i]) - ord('a')] += 1
            scount[ord(s[i-len(p)]) - ord('a')] -= 1
            if scount == pcount:
                ans.append(i - len(p) + 1)
        return ans